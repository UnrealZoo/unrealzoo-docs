#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建产物资源引用自检：扫描 site/ 下所有 html 的本地 src/href，检查文件是否存在"""
import os
import re
import sys
from urllib.parse import unquote

SITE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'site')
MEDIA = ('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.webm', '.svg')


def main():
    if not os.path.isdir(SITE):
        print('site/ 不存在，先构建', file=sys.stderr)
        return 2
    missing = {}
    checked = 0
    for root, _, files in os.walk(SITE):
        for f in files:
            if not f.endswith('.html'):
                continue
            p = os.path.join(root, f)
            html = open(p, encoding='utf-8', errors='ignore').read()
            refs = re.findall(r'(?:src|href)="([^"#?]+)"', html)
            for r in refs:
                if r.startswith(('http://', 'https://', '//', 'data:', 'mailto:')):
                    continue
                if not r.lower().endswith(MEDIA):
                    continue
                dec = unquote(r)
                if dec.startswith('/'):
                    # 站点部署在子路径（如 /doc/）→ 绝对路径按部署前缀还原到 site/
                    rel = dec.lstrip('/')
                    for prefix in ('doc/',):
                        if rel.startswith(prefix):
                            rel = rel[len(prefix):]
                            break
                    target = os.path.normpath(os.path.join(SITE, rel))
                else:
                    target = os.path.normpath(os.path.join(root, dec))
                checked += 1
                if not os.path.exists(target):
                    missing.setdefault(dec, []).append(os.path.relpath(p, SITE))
    if missing:
        print(f'失效资源引用 {len(missing)} 个（扫描 {checked} 处）：')
        for k, v in list(missing.items())[:30]:
            print(f'  ✗ {k}  ({len(v)} 处, 例如 {v[0]})')
        return 1
    print(f'资源引用自检通过（扫描 {checked} 处，0 失效）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
