#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
媒体单一入口：Notion → 下载 → 逐帧/时长校验 → 编码 → 清单 → 非零退出

为什么要有这个（2026-11-24 事故复盘）：
  - 11-24 那批素材一路提交并发布，根因是**批量下载只判「文件存在」**，没判内容完整性
  - 事后补的 `verify-media-integrity.py` 只是个**可选工具**，没有任何下载/构建路径会调用它
  → 所以必须把「下载」和「校验」合成一个入口，并且接进构建前步骤

本工具的契约：
  1. 只接受 spec 文件描述的素材清单（页面 → 目标文件名 → 是否需要转码）
  2. 每个文件都从 Notion 现场取**新鲜签名 URL**（S3 签名 1 小时过期）
  3. 下载用断点续传，落到 .part，**校验通过才改名**为正式名
  4. 校验项：可解析性 + 帧数 > 0 + 时长 > 0 + 体积下限（与 verify-media-integrity 同源）
  5. 可选转码：GIF → H.264 MP4 + JPEG 海报（保帧保时序：-fps_mode passthrough）
  6. 生成/更新 media-manifest.json（记录期望帧数与时长，供后续比对）
  7. **任一素材失败 → 退出码非 0**，可直接作为构建/CI 的前置关卡

用法：
  python3 tools/fetch-media.py --spec tools/media-spec.json --asset-dir docs/en/assets
  python3 tools/fetch-media.py --spec tools/media-spec.json --asset-dir docs/en/assets \\
      --asset-dir docs/zh/assets --encode-gif-to-mp4 --manifest media-manifest.json
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

BAD_MARKERS = ('partial file', 'invalid nal unit size', 'moov atom not found',
               'truncat', 'error splitting the input', 'invalid data found',
               'end of file reached', 'stream 0, offset')
VIDEO_EXT = ('.gif', '.mp4', '.m4v', '.webm', '.mov')
IMAGE_EXT = ('.png', '.jpg', '.jpeg', '.webp')


# ---------------------------------------------------------------- Notion

def notion_token():
    for p in ('/Users/funway/.openclaw/config/mcporter.json', '/tmp/mc.json'):
        if os.path.exists(p):
            d = json.load(open(p))
            servers = d.get('servers') or d.get('mcpServers') or {}
            env = (servers.get('notion') or {}).get('env') or {}
            if env.get('NOTION_TOKEN'):
                return env['NOTION_TOKEN']
    raise SystemExit('!! 找不到 NOTION_TOKEN（检查 mcporter 配置）')


def napi(token, path):
    out = subprocess.run(['curl', '-s', '-m', '40', f'https://api.notion.com/v1/{path}',
                          '-H', f'Authorization: Bearer {token}',
                          '-H', 'Notion-Version: 2025-09-03'],
                         capture_output=True, text=True, timeout=60).stdout
    try:
        return json.loads(out)
    except Exception:
        return {}


def nwalk(token, pid, depth=0):
    for b in napi(token, f'blocks/{pid}/children?page_size=100').get('results', []):
        yield b
        if b.get('has_children') and depth < 3:
            yield from walk_(token, b['id'], depth + 1)


def walk_(token, pid, depth=0):
    for b in napi(token, f'blocks/{pid}/children?page_size=100').get('results', []):
        yield b
        if b.get('has_children') and depth < 3:
            yield from walk_(token, b['id'], depth + 1)


def find_media(token, page_id, want_name, kind):
    """在页面里找同名媒体块，返回新鲜签名 URL"""
    for b in walk_(token, page_id):
        if b.get('type') != kind:
            continue
        o = b.get(kind, {}) or {}
        u = (o.get('file') or {}).get('url') or ''
        if not u:
            continue
        fn = u.split('?')[0].split('/')[-1]
        from urllib.parse import unquote
        if unquote(fn) == want_name or fn == want_name:
            return u
    return ''


# ---------------------------------------------------------------- 校验

def probe(path):
    """返回 (frames, duration, w, h, errors)"""
    errs = []
    if os.path.splitext(path)[1].lower() in IMAGE_EXT:
        try:
            r = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', path],
                               capture_output=True, text=True, timeout=60)
            m = re.search(r'pixelWidth:\s*(\d+)', r.stdout or '')
            n = re.search(r'pixelHeight:\s*(\d+)', r.stdout or '')
            if not m or not n:
                return (0, 0.0, 0, 0, ['sips 无法读取尺寸'])
            return (1, 0.0, int(m.group(1)), int(n.group(1)), errs)
        except Exception as e:
            return (0, 0.0, 0, 0, [f'sips 失败: {e}'])

    try:
        r = subprocess.run(
            ['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0',
             '-show_entries', 'stream=nb_read_frames,width,height',
             '-show_entries', 'format=duration', '-of', 'json', path],
            capture_output=True, text=True, timeout=900)
    except Exception as e:
        return (0, 0.0, 0, 0, [f'ffprobe 失败: {e}'])
    err = (r.stderr or '').lower()
    for m in BAD_MARKERS:
        if m in err:
            errs.append(f'解码报错({m.strip()})')
            break
    frames = dur = w = h = 0
    try:
        j = json.loads(r.stdout or '{}')
        st = (j.get('streams') or [{}])[0]
        w = int(st.get('width') or 0); h = int(st.get('height') or 0)
        fr = st.get('nb_read_frames')
        if fr in (None, 'N/A'):
            fr = st.get('nb_frames')
        frames = int(fr) if fr not in (None, 'N/A') else 0
        dur = float((j.get('format') or {}).get('duration') or 0)
    except Exception:
        errs.append('ffprobe 输出无法解析')
    if not w or not h:
        errs.append('取不到宽高')
    if frames <= 0:
        errs.append('帧数为 0')
    if dur <= 0:
        errs.append('时长为 0')
    return (frames, dur, w, h, errs)


def valid(path, min_size=1024):
    if not (os.path.exists(path) and os.path.getsize(path) >= min_size):
        return False, (0, 0.0, 0, 0, ['文件不存在或过小'])
    fr, du, w, h, errs = probe(path)
    return (not errs), (fr, du, w, h, errs)


# ---------------------------------------------------------------- 下载

def download(url, dest, min_size=1024, max_rounds=200):
    tmp = dest + '.part'
    for _ in range(max_rounds):
        try:
            subprocess.run(['curl', '-sL', '-C', '-', '--max-time', '180', '-o', tmp, url],
                           capture_output=True, timeout=200)
        except Exception:
            pass
        ok, info = valid(tmp, min_size)
        if ok:
            os.replace(tmp, dest)
            return True, info
        time.sleep(1)
    return False, (0, 0.0, 0, 0, ['续传后仍未通过校验'])


# ---------------------------------------------------------------- 编码

def encode_gif_to_mp4(src, dst_base, width=720, crf=30):
    mp4 = dst_base + '.mp4'
    jpg = dst_base + '.jpg'
    tmp = mp4 + '.tmp.mp4'
    vf = f"scale='min({width},iw)':-2:flags=lanczos,hqdn3d=2:3:3:3"
    r = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-err_detect', 'ignore_err',
                        '-y', '-i', src, '-vf', vf, '-fps_mode', 'passthrough',
                        '-enc_time_base', '1/1000', '-c:v', 'libx264', '-crf', str(crf),
                        '-preset', 'veryslow', '-tune', 'stillimage', '-pix_fmt', 'yuv420p',
                        '-movflags', '+faststart', '-an', tmp], capture_output=True, timeout=1800)
    if not (os.path.exists(tmp) and os.path.getsize(tmp) > 3000):
        if os.path.exists(tmp):
            os.remove(tmp)
        return None, None, (r.stderr or '')[:120]
    os.replace(tmp, mp4)
    pt = jpg + '.tmp.jpg'
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', src,
                    '-vf', f"select=eq(n\\,0),scale='min({width},iw)':-2:flags=lanczos",
                    '-frames:v', '1', '-q:v', '6', pt], capture_output=True, timeout=300)
    if os.path.exists(pt) and os.path.getsize(pt) > 1000:
        os.replace(pt, jpg)
    elif os.path.exists(pt):
        os.remove(pt)
    return mp4, jpg, None


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser(description='媒体单一入口：下载→校验→编码→清单')
    ap.add_argument('--spec', required=True, help='spec JSON')
    ap.add_argument('--asset-dir', action='append', required=True, help='目标目录（可重复）')
    ap.add_argument('--manifest', help='清单输出/更新路径')
    ap.add_argument('--encode-gif-to-mp4', action='store_true', help='GIF → MP4 + 海报')
    ap.add_argument('--width', type=int, default=720, help='MP4 最大宽度')
    ap.add_argument('--crf', type=int, default=30, help='x264 crf')
    ap.add_argument('--min-size', type=int, default=1024, help='最小体积阈值')
    ap.add_argument('--workers', type=int, default=5)
    ap.add_argument('--skip-existing', action='store_true', help='已存在且校验通过的直接跳过')
    args = ap.parse_args()

    spec = json.load(open(args.spec, encoding='utf-8'))
    token = notion_token()
    manifest_path = args.manifest or os.path.join(os.path.dirname(args.spec), 'media-manifest.json')
    manifest = {}
    if os.path.exists(manifest_path):
        try:
            manifest = json.load(open(manifest_path, encoding='utf-8')).get('assets', {})
        except Exception:
            manifest = {}

    targets = []
    for page in spec.get('pages', []):
        for item in page.get('media', []):
            targets.append((page['page_id'], item['name'], item.get('kind', 'video'),
                            item.get('out'), item.get('encode', 'copy')))

    def work(t):
        page_id, name, kind, out, enc = t
        out_name = out or name
        res = {'name': out_name, 'ok': False, 'msg': ''}
        for adir in args.asset_dir:
            dst = os.path.join(adir, out_name)
            if args.skip_existing:
                ok, info = valid(dst, args.min_size)
                if ok:
                    res.update({'ok': True, 'msg': '已存在（跳过）',
                                'frames': info[0], 'duration': info[1], 'size': os.path.getsize(dst)})
                    return res
            url = find_media(token, page_id, name, kind)
            if not url:
                res['msg'] = f'未在 Notion 找到 {name}'
                return res
            raw = dst + '.src'
            ok, info = download(url, raw, args.min_size)
            if not ok:
                res['msg'] = f'{name}: 下载后校验失败 {info[4]}'
                return res
            if enc == 'gif2mp4' and args.encode_gif_to_mp4:
                mp4, jpg, err = encode_gif_to_mp4(raw, dst, args.width, args.crf)
                if not mp4:
                    res['msg'] = f'{name}: 转码失败 {err}'
                    return res
                if adir != args.asset_dir[-1]:
                    shutil.copy(mp4, os.path.join(adir, os.path.basename(mp4)))
                    if jpg and os.path.exists(jpg):
                        shutil.copy(jpg, os.path.join(adir, os.path.basename(jpg)))
                os.remove(raw)
                fr, du, w, h, errs = probe(mp4)
                if errs:
                    res['msg'] = f'{name}: 转码后仍异常 {errs}'
                    return res
                res.update({'ok': True, 'msg': '已转码', 'frames': fr, 'duration': du,
                            'size': os.path.getsize(mp4)})
                manifest[out_name] = {'frames': fr, 'duration': round(du, 3),
                                      'source_frames': info[0], 'source_duration': round(info[1], 3)}
                continue
            shutil.copy(raw, dst)
            os.remove(raw)
            fr, du, w, h, errs = probe(dst)
            if errs:
                res['msg'] = f'{name}: 落盘后校验失败 {errs}'
                return res
            res.update({'ok': True, 'msg': '已下载', 'frames': fr, 'duration': du,
                        'size': os.path.getsize(dst)})
            manifest[out_name] = {'frames': fr, 'duration': round(du, 3)}
        return res

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for r in ex.map(work, targets):
            results.append(r)
            flag = '✓' if r['ok'] else '✗'
            print(f"  {flag} {r['name']:44s} {r['msg']}", flush=True)

    failed = [r for r in results if not r['ok']]
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump({'assets': manifest}, f, ensure_ascii=False, indent=1)

    print(f'\n素材 {len(results)} 项，成功 {len(results)-len(failed)}，失败 {len(failed)}；'
          f'清单已写入 {manifest_path}')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
