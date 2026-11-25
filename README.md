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

## Media integrity gate — run it before committing assets

Assets under `docs/{en,zh}/assets/` are fetched from Notion / S3 and converted (GIF → H.264 MP4).
**Partial downloads are silent**: a truncated MP4 still reports width/height with exit code 0,
and a truncated GIF keeps its declared duration while losing frames.

So every asset change must pass:

```bash
python3 tools/verify_media.py --asset-dir docs/en/assets --asset-dir docs/zh/assets
```

Exit code `0` = all files pass, `1` = failures (listed per file), `2` = bad usage.

The gate checks, per file:

1. **Parseability** — video: `ffprobe` opens it and stderr contains no decode errors
   (`partial file`, `invalid nal unit size`, `moov atom not found`, …);
   images: `sips` can read the dimensions (ffmpeg rejects some valid PNGs with `chunk too big`)
2. **Frame count > 0** (parsed via `-of json`)
3. **Duration > 0** for video containers
4. **File size** above a minimum threshold

Optional `--manifest` additionally compares each asset's **frame count and duration against its
source**, so a silently truncated file cannot pass.

See `tools/ref/media-integrity.md` in the assistant workspace for the full rationale.

## i18n

Locales live in `docs/en/` and `docs/zh/`. Navigation is kept in sync with `nav_translations`
in `mkdocs.yml`, so the sidebar shows the matching language in both locales.

## Deployment

`main` → GitHub Pages. The built site is published under `/doc/` on the project homepage
(`https://unrealzoo.site/doc/`), so `site_url` in `mkdocs.yml` includes the `/doc/` prefix.
