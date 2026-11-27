# UnrealZoo Documentation

Bilingual (EN / 中文) documentation for UnrealZoo, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed to GitHub Pages.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000
# or build a static site and serve it
mkdocs build && python3 -m http.server 8000
```

## Repository layout

```
docs/
  en/          English pages
  zh/          Chinese pages
  assets/      images, videos, GIF-derived clips (media lives here)
  assets/scenes/  scene gallery thumbnails
  assets/*.json    generated data (scene gallery)
tools/
  verify_media.py   media integrity gate (run before committing assets)
mkdocs.yml
```

## Media pipeline — one entry point, gated before every build

Assets under `docs/{en,zh}/assets/` come from Notion. The 2026-11-24 incident: a batch of
**truncated** files was committed and published because the download step only checked
"does the file exist". A later integrity checker existed but **nothing called it**.

Now there is a single entry point and a mandatory gate:

```bash
# 1) fetch / refresh media (download → validate → optional transcode → manifest)
python3 tools/fetch_media.py --spec tools/media-spec.json \
    --asset-dir docs/en/assets --asset-dir docs/zh/assets \
    --encode-gif-to-mp4 --manifest tools/media-manifest.json

# 2) build with the gate (media check → mkdocs build → reference check)
bash scripts/build_docs.sh
```

`scripts/build_docs.sh` refuses to produce `site/` when any media file fails the integrity
check, and also fails when the built HTML references assets that do not exist.

### CI — the gate runs server-side too

`.github/workflows/docs-gate.yml` runs `scripts/build_docs.sh` on every push and PR to
`main` (and can be triggered manually). A failing media check, a broken build, or a broken
asset reference **fails the workflow** — so corrupted media cannot reach `main` by accident.

The workflow installs `ffprobe` (media validation) and the docs dependencies, then runs the
same script you can run locally.

### The integrity gate

```bash
python3 tools/verify_media.py --asset-dir docs/en/assets --asset-dir docs/zh/assets
```

Exit code `0` = all pass, `1` = failures (listed per file), `2` = bad usage. Per file it checks:

1. **Parseability** — video: `ffprobe` opens it and stderr contains no decode errors
   (`partial file`, `invalid nal unit size`, `moov atom not found`, …);
   images: `sips` can read the dimensions (ffmpeg rejects some valid PNGs with `chunk too big`)
2. **Frame count > 0** (parsed via `-of json`)
3. **Duration > 0** for video containers
4. **File size** above a minimum threshold

Optional `--manifest` additionally compares each asset's **frame count and duration against its
source**, so a silently truncated file cannot pass.

> A truncated MP4 still reports width/height with **exit code 0** — the real signal is in stderr.
> A truncated GIF keeps its declared duration while losing frames. Hence: parseability +
> frame count + duration + size, never one of them alone.

### `tools/media-spec.json`

Declares which Notion page holds which media and what the file is called in the docs.
`fetch_media.py` fetches a **fresh signed URL** per asset (S3 signatures expire in ~1 hour),
resumes partial downloads, validates before renaming `.part` → final name, and writes
`tools/media-manifest.json` with the expected frame count and duration for later comparison.

## i18n

Locales live in `docs/en/` and `docs/zh/`. Navigation is kept in sync with `nav_translations`
in `mkdocs.yml`, so the sidebar shows the matching language in both locales.

## Deployment

`main` → GitHub Pages. The built site is published under `/doc/` on the project homepage
(`https://unrealzoo.site/doc/`), so `site_url` in `mkdocs.yml` includes the `/doc/` prefix.
