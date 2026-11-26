#!/bin/bash
# 构建文档前先过媒体完整性关卡：任一媒体损坏/缺失 → 直接失败，不产出 site/
#
# 用法：
#   scripts/build_docs.sh              # 校验 + 构建
#   scripts/build_docs.sh --check-only # 只校验
#
# 背景：2026-11-24 一批被截断的媒体一路提交并发布，根因是没有任何下载/构建路径
# 会调用完整性校验。现在这里是唯一强制关卡。

set -euo pipefail
cd "$(dirname "$0")/.."

PY=python3
ASSETS_EN=docs/en/assets
ASSETS_ZH=docs/zh/assets

echo "==> [1/3] 媒体完整性关卡"
$PY tools/verify_media.py --asset-dir "$ASSETS_EN" --asset-dir "$ASSETS_ZH"

if [ "${1:-}" = "--check-only" ]; then
  echo "==> 只校验模式，跳过构建"
  exit 0
fi

echo "==> [2/3] 构建静态站点"
$PY -m mkdocs build

echo "==> [3/3] 构建后资源引用自检"
$PY tools/check_asset_refs.py || {
  echo "!! 构建产物存在失效资源引用，构建视为失败" >&2
  exit 1
}

echo "==> OK：媒体关卡通过，站点已构建到 site/"
