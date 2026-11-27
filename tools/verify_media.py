#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
媒体完整性校验器（提交前门禁）

背景：批量下载 Notion / S3 素材时，curl 超时会产生**半截文件**，而且
  - 被截断的 MP4，ffprobe 仍会打印出宽高且**退出码为 0** → 只看退出码/宽高会漏判
    （典型报错："partial file" / "Invalid NAL unit size"）
  - 被截断的 GIF 帧数变少 → 动画看起来"跳格/被截断"，而容器时长可能仍然"正常"
  - ffmpeg 解不了某些合法 PNG（"chunk too big"）→ PNG 必须用 sips 判，不能用 ffprobe

本工具做四项检查，任何一项不通过即以非零退出码失败：
  1. 可解析性：视频用 ffprobe 且 stderr 无解码错误；静态图用 sips 取尺寸
  2. 帧数：可读帧数 > 0
  3. 时长：视频容器时长 > 0
  4. 体积：文件不小于阈值（默认 1KB）

可选：给出 manifest 时额外核对 **帧数 + 时长与源素材一致**。

用法：
  python3 tools/verify-media-integrity.py --asset-dir docs/en/assets
  python3 tools/verify-media-integrity.py --asset-dir X --manifest M --json

注意：本机 exec 预检只允许裸 `python <file>.py`，带参数请用包装脚本调用。

manifest 格式（JSON）：
{
  "tolerance": {"frames_ratio": 0.02, "duration_abs": 0.3},
  "assets": {
    "avt_interior_1.mp4": {"source": "/tmp/src_full/Offline_UndergroundParking.gif"},
    "avt_palaces_1.mp4": {"frames": 160, "duration": 44.35}
  }
}
"""
import argparse
import json
import os
import re
import subprocess
import sys

MEDIA_EXT = ('.gif', '.mp4', '.m4v', '.webm', '.mov', '.png', '.jpg', '.jpeg', '.webp')
VIDEO_EXT = ('.gif', '.mp4', '.m4v', '.webm', '.mov')
IMAGE_EXT = ('.png', '.jpg', '.jpeg', '.webp')
BAD_MARKERS = ('partial file', 'invalid nal unit size', 'moov atom not found',
               'truncat', 'error splitting the input', 'invalid data found',
               'end of file reached', 'stream 0, offset')


def probe_video(path):
    """返回 (frames, duration, w, h, errors)"""
    errs = []
    try:
        r = subprocess.run(
            ['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0',
             '-show_entries', 'stream=nb_read_frames,width,height',
             '-show_entries', 'format=duration', '-of', 'json', path],
            capture_output=True, text=True, timeout=300)
    except Exception as e:
        return (0, 0.0, 0, 0, [f'ffprobe 调用失败: {e}'])

    stderr = (r.stderr or '').lower()
    for m in BAD_MARKERS:
        if m in stderr:
            errs.append(f'解码报错({m.strip()}) —— 文件可能被截断')
            break

    # 用 JSON 取值：按位置解析会在「帧数恰好等于宽度」时出错
    frames = dur = w = h = 0
    try:
        data = json.loads(r.stdout or '{}')
        streams = data.get('streams') or []
        if streams:
            st = streams[0]
            w = int(st.get('width') or 0)
            h = int(st.get('height') or 0)
            fr = st.get('nb_read_frames')
            if fr in (None, 'N/A'):
                fr = st.get('nb_frames')
            frames = int(fr) if fr not in (None, 'N/A') else 0
        dur = float((data.get('format') or {}).get('duration') or 0)
    except Exception:
        errs.append('ffprobe 输出无法解析为 JSON')

    if not w or not h:
        errs.append('取不到宽高（容器可能只有文件头）')
    if frames <= 0:
        errs.append('帧数为 0')
    return (frames, dur, w, h, errs)


def probe_image(path):
    """静态图：纯 Python 解析文件头取尺寸（跨平台；ffmpeg 对合法 PNG 会误报 chunk too big）"""
    errs = []
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from image_size import image_size
        w, h = image_size(path)
        if not w or not h:
            return (0, 0.0, 0, 0, ['无法读取图片尺寸（文件可能损坏）'])
        return (1, 0.0, w, h, errs)
    except Exception as e:
        return (0, 0.0, 0, 0, [f'图片尺寸读取失败: {e}'])


def check_file(path, min_size, manifest_entry, tol):
    res = {'file': os.path.basename(path), 'path': path, 'errors': []}
    size = os.path.getsize(path)
    res['size'] = size
    if size < min_size:
        res['errors'].append(f'体积过小: {size} < {min_size} bytes')

    ext = os.path.splitext(path)[1].lower()
    if ext in IMAGE_EXT:
        frames, dur, w, h, errs = probe_image(path)
    else:
        frames, dur, w, h, errs = probe_video(path)
        if dur <= 0:
            errs.append('时长为 0（容器可能只有文件头）')
    res.update({'frames': frames, 'duration': round(dur, 3), 'width': w, 'height': h})
    res['errors'].extend(errs)

    if manifest_entry and not res['errors']:
        exp_frames = manifest_entry.get('frames')
        exp_dur = manifest_entry.get('duration')
        src = manifest_entry.get('source')
        if src and os.path.exists(src):
            sf, sd, _, _, _ = (probe_video(src) if os.path.splitext(src)[1].lower() in VIDEO_EXT
                               else probe_image(src))
            exp_frames = exp_frames if exp_frames is not None else sf
            exp_dur = exp_dur if exp_dur is not None else sd
        if exp_frames:
            ratio = tol['frames_ratio']
            if frames < exp_frames * (1 - ratio) or frames > exp_frames * (1 + ratio):
                res['errors'].append(f'帧数与源不符: 实际 {frames} vs 源 {exp_frames}')
        if exp_dur:
            da = tol['duration_abs']
            if abs(dur - exp_dur) > max(da, exp_dur * 0.05):
                res['errors'].append(f'时长与源不符: 实际 {dur:.2f}s vs 源 {exp_dur:.2f}s')
    return res


def main():
    ap = argparse.ArgumentParser(description='媒体完整性校验（帧数/时长/可解析性/体积）')
    ap.add_argument('--asset-dir', action='append', required=True, help='资源目录（可重复）')
    ap.add_argument('--manifest', help='源素材对照 manifest (JSON)')
    ap.add_argument('--min-size', type=int, default=1024, help='最小体积阈值（字节）')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    ap.add_argument('--frames-ratio', type=float, default=0.02, help='帧数允许偏差比例')
    ap.add_argument('--duration-abs', type=float, default=0.3, help='时长允许绝对偏差（秒）')
    args = ap.parse_args()

    tol = {'frames_ratio': args.frames_ratio, 'duration_abs': args.duration_abs}
    manifest = {}
    if args.manifest:
        try:
            data = json.load(open(args.manifest, encoding='utf-8'))
            manifest = data.get('assets', data)
            tol.update(data.get('tolerance', {}) or {})
        except Exception as e:
            print(f'!! manifest 读取失败: {e}', file=sys.stderr)
            return 2

    files = []
    for d in args.asset_dir:
        if not os.path.isdir(d):
            print(f'!! 目录不存在: {d}', file=sys.stderr)
            return 2
        for root, _, names in os.walk(d):
            for n in names:
                if n.lower().endswith(MEDIA_EXT):
                    files.append(os.path.join(root, n))

    results = [check_file(p, args.min_size, manifest.get(os.path.basename(p)), tol) for p in sorted(files)]
    failed = [r for r in results if r['errors']]
    total_size = sum(r['size'] for r in results)

    if args.json:
        print(json.dumps({'checked': len(results), 'failed': len(failed),
                          'total_bytes': total_size, 'results': results},
                         ensure_ascii=False, indent=1))
    else:
        for r in failed:
            print(f"✗ {r['file']}: {'; '.join(r['errors'])}")
        print(f"检查 {len(results)} 个媒体文件，失败 {len(failed)} 个，合计 {total_size/1048576:.1f} MB")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
