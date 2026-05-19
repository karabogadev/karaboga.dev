# karaboga.dev

Personal site of **Cihat Karaboğa** — mobile software engineer, Türkiye.

A single static page. `index.html` is fully self-contained: inline CSS, no
JavaScript, no web fonts, and the avatar embedded as a data URI — so the page
renders in a single request. Built for speed and SEO with semantic HTML,
Open Graph + Twitter cards, JSON-LD structured data, a sitemap and a manifest.

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
| `avatar.jpg` | Portrait used by structured data and the share card |
| `manifest.webmanifest` | PWA manifest |
| `robots.txt`, `sitemap.xml` | Crawler directives |
| `nginx.conf`, `Dockerfile` | Container deployment |
| `og.html`, `avatar-src.png` | Build sources — not deployed |

## Regenerate images

`og.png` is a 1200×630 screenshot of `og.html`. The avatar is resized from
`avatar-src.png` (the inline copy in `index.html` and the standalone
`avatar.jpg`). Re-render if either source changes.

The Docker image copies `icon-512.png` to `og.png` when the real file is not in
the repo so builds succeed; commit `og.png` for correct social preview and then
add it to the `COPY` line in the `Dockerfile` (and remove the `RUN cp` there).
