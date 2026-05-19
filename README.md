# karaboga.dev

Personal site of **Cihat Karaboğa** — mobile software engineer, Türkiye.

A single static page. `index.html` is self-contained — inline CSS and a tiny
inline theme script, no build step. Built for speed and SEO with semantic HTML,
Open Graph + Twitter cards, JSON-LD structured data, a sitemap and a manifest.
The UI uses the Geist webfont (Google Fonts) with a system-font fallback.

## Develop locally

Serve the folder so root-absolute paths (`/favicon.svg`, `/og.png`, …) resolve:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

## Deploy

### Docker / nginx

```bash
docker build -t karaboga-dev .
docker run --rm -p 8080:80 karaboga-dev
```

`nginx.conf` adds gzip, long-cache headers for static assets, and wires up the
custom `404.html`.

### GitHub Pages

Push to GitHub, then **Settings → Pages → Source: `main` / root**. Set the
custom domain to `karaboga.dev` (this adds a `CNAME` file).

## Files

| File | Purpose |
|------|---------|
| `index.html` | The page — markup, inline CSS, SEO metadata, JSON-LD |
| `404.html` | Themed not-found page |
| `og.png` | 1200×630 social share image |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-*.png` | Icons |
| `manifest.webmanifest` | PWA manifest |
| `robots.txt`, `sitemap.xml` | Crawler directives |
| `nginx.conf`, `Dockerfile` | Container deployment |
| `og.html` | Build source for `og.png` — not deployed |

## Regenerate the OG image

`og.png` is a 1200×630 render of `og.html`. After editing `og.html`, re-render
and commit `og.png` — the `Dockerfile` `COPY`s it directly:

```bash
chrome --headless --window-size=1200,630 --force-device-scale-factor=1 \
  --hide-scrollbars --virtual-time-budget=5000 \
  --screenshot=og.png "file://$PWD/og.html"
```

On macOS, `chrome` is `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.
