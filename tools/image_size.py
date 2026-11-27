#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台图片尺寸读取（纯 Python，无外部依赖）

为什么不用 sips：sips 是 macOS 专有命令，放到 GitHub Actions（Linux）上会把
所有 PNG/JPG 判成「无法读取尺寸」→ 媒体关卡在 CI 上必然假失败。
也不用 ffprobe：ffmpeg 对某些合法 PNG 报 `chunk too big`（误杀）。

实现：直接解析文件头
  - PNG: 字节 16..24 = width, height (big-endian uint32)
  - JPEG: 扫描 SOF0/1/2 等标记，取 height, width
  - GIF: 字节 6..10 = width, height (little-endian uint16)
  - WebP: RIFF 容器，VP8/VP8L/VP8X 三种变体
"""
import struct
import sys


def image_size(path):
    """返回 (width, height)；失败返回 (0, 0)"""
    try:
        with open(path, 'rb') as f:
            head = f.read(32)
            if len(head) < 16:
                return (0, 0)

            # PNG
            if head[:8] == b'\x89PNG\r\n\x1a\n':
                w, h = struct.unpack('>II', head[16:24])
                return (int(w), int(h))

            # GIF
            if head[:6] in (b'GIF87a', b'GIF89a'):
                w, h = struct.unpack('<HH', head[6:10])
                return (int(w), int(h))

            # WebP
            if head[:4] == b'RIFF' and head[8:12] == b'WEBP':
                chunk = head[12:16]
                if chunk == b'VP8 ':
                    f.seek(26)
                    d = f.read(6)
                    w = struct.unpack('<H', d[2:4])[0] & 0x3FFF
                    h = struct.unpack('<H', d[4:6])[0] & 0x3FFF
                    return (int(w), int(h))
                if chunk == b'VP8L':
                    f.seek(21)
                    b = f.read(1)[0]
                    bits = struct.unpack('<I', f.read(3) + b'\x00')[0]
                    return (int((bits & 0x3FFF) + 1), int(((bits >> 14) & 0x3FFF) + 1))
                if chunk == b'VP8X':
                    f.seek(24)
                    d = f.read(10)
                    w = int.from_bytes(d[4:7], 'little') + 1
                    h = int.from_bytes(d[7:10], 'little') + 1
                    return (w, h)
                return (0, 0)

            # JPEG
            if head[:2] == b'\xff\xd8':
                f.seek(2)
                while True:
                    marker = f.read(2)
                    if len(marker) < 2:
                        break
                    if marker[0] != 0xFF:
                        continue
                    m = marker[1]
                    if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                        continue
                    seg = f.read(2)
                    if len(seg) < 2:
                        break
                    length = struct.unpack('>H', seg)[0]
                    if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                             0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                        data = f.read(5)
                        if len(data) >= 5:
                            h, w = struct.unpack('>HH', data[1:5])
                            return (int(w), int(h))
                        break
                    f.seek(length - 2, 1)
                return (0, 0)
    except Exception:
        return (0, 0)
    return (0, 0)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(p, image_size(p))
