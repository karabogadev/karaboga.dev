# karaboga.dev

Personal site of **Cihat Karaboğa** — mobile software engineer, Türkiye.

A single static page. `index.html` is self-contained — inline CSS and a small
inline script, no build step. Built for speed and SEO with semantic HTML,
Open Graph + Twitter cards, JSON-LD structured data, a sitemap and a manifest.
Type is Inter Tight with Instrument Serif italic accents (Google Fonts) and
system-font fallbacks. The design system is documented in `DESIGN.md`.

Sections: introduction with a live Istanbul clock, a numbered selected-work list
with cursor-following previews on pointer devices, experience, about, stack, and
contact. Navigation stays visible on mobile. The project previews are lightweight
HTML/CSS motifs, not product screenshots.

## Themes and language

Light/dark follows the system preference and is overridable from the header;
the choice is stored in `localStorage` and applied before first paint.

The page ships in English so crawlers index a complete English document.
Turkish is applied on top from an inline dictionary keyed by `data-i18n`
attributes — every value is plain text set through `textContent`. Language
resolution order is `?lang=` → `localStorage` → `navigator.language` → English,
and switching rewrites `?lang=` so a Turkish link is shareable. There is no
`hreflang`: both languages live at the same URL, so advertising them as
alternates would be a duplicate signal rather than a useful one. Separate
`/tr/` pages would be the fix if real bilingual SEO is ever needed.

Storage failures do not prevent the page from loading. Without JavaScript, all
content and navigation remain available; enhancement controls stay hidden. Email
copying works independently for `cihat@karaboga.dev` and
`cihattkaraboga@gmail.com`. It announces success, or selects the address when clipboard
access is unavailable. Reduced-motion preferences disable animation.

To add or change a string, add the `data-i18n` attribute to the element and the
matching key to the `STRINGS.tr` object — the English side is snapshotted from
the markup at load, so it never needs a second dictionary.
A phrase set in the serif italic is its own key on its own `<em>`, so no
translation ever needs markup.

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
docker run --rm -p 8080:3000 karaboga-dev
```

`nginx.conf` adds gzip, long-cache headers for static assets, and wires up the
custom `404.html`.

### GitHub Pages

Push to GitHub, then **Settings → Pages → Source: `main` / root**. Set the
custom domain to `karaboga.dev` (this adds a `CNAME` file).

## Files

| File | Purpose |
|------|---------|
| `DESIGN.md` | Visual system and interaction principles |
| `index.html` | The page — markup, inline CSS, SEO metadata, JSON-LD |
| `404.html` | Themed not-found page |
| `privacy.html` | Privacy policy, served at `/privacy` (site + SaaS Idea Scout Google OAuth) |
| `og.png` | 1200×630 social share image |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-*.png` | Icons |
| `manifest.webmanifest` | PWA manifest |
| `robots.txt`, `sitemap.xml` | Crawler directives |
| `nginx.conf`, `Dockerfile` | Container deployment |
| `og.html` | Build source for `og.png` — not deployed |
| `logo-concept.png` | Generated logo exploration — not deployed in Docker |

## Regenerate the OG image

`og.png` is a 1200×630 render of `og.html`. After editing `og.html`, re-render
and commit `og.png` — the `Dockerfile` `COPY`s it directly:

```bash
chrome --headless --window-size=1200,630 --force-device-scale-factor=1 \
  --hide-scrollbars --virtual-time-budget=5000 \
  --screenshot=og.png "file://$PWD/og.html"
```

On macOS, `chrome` is `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.
