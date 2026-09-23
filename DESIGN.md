# Design direction

A personal portfolio for Cihat Karaboğa, a mobile software engineer. Help a
prospective collaborator understand his specialty, inspect his work, and contact him.

Editorial minimal: typography does the work. No cards, chips, or pastel
illustration boxes — hairlines, whitespace, and one accent color.

## Visual system

- Light: canvas `#f6f6f3`, ink `#111113`, secondary `#55555b`, tertiary `#6b6b72`,
  hairline `#e0e0db`.
- Dark: canvas `#0c0c0d`, ink `#ededeb`, secondary `#a1a1a7`, tertiary `#8a8a91`,
  hairline `#242427`.
- Accent: cobalt `#3659db`, the one color on an ink-and-paper page; its
  text-level form in dark mode is `#8fa2ff`. The accent is rare: the period after
  the name, active nav, hover, the current role, selection. Every text token passes WCAG AA on its canvas.
- Inter Tight (400/500) for everything. Instrument Serif italic is the single
  second voice — one phrase per section at most (*solid engineering*, *boring
  releases*, *in mind?*). System monospace only inside the code preview motif.
- 80rem wrap on a 12-column grid. Each section is a hairline, a small label in
  columns 1–3, and content in columns 4–12. Meta columns (dates, stack groups)
  share one width so rows align down the page.

## Composition

```text
brand                    section navigation            EN | TR   theme
role · Istanbul + live time                         ● open to new projects
Cihat
Karaboğa.                       (display name, cobalt period)
subtitle with serif phrase      lead + "Get in touch" pill + work link
─────────────────────────────────────────────────────────────────────
Selected work     01  mirro                    macOS app      2026 ↗
                  02  Flutter App Boilerplate  Tooling        2026 ↗
                  03  Traffic Racer            Game           2025 ↗
                  04  karaboga.dev             Website        2026 ↗
Experience        date   company / role / outcome
About             one large statement, two short supporting notes
Stack             group  comma-separated tools
Contact           large title, large email link + copy, alternate address
```

The memorable moments are the display name rising out of its mask on load and
the work list: on hover-capable pointers the other rows dim and a small preview
card trails the cursor, leaning into horizontal movement. Each project has its
own flat-color motif (a phone in a Mac window, a folder tree, a road, the site
itself). These are decorative interface studies — `aria-hidden`, never shown on
touch or coarse pointers, and every row still carries its description in text.

Avoid gradients (the road's lane dashes are the one pattern), decorative metrics,
card grids, tag chips, and scroll-hidden content.

## Interaction and accessibility

Keep all navigation available on mobile in a second header row. Give links and
controls 44px touch targets, visible focus, and clear selected states. Preserve
English/Turkish switching and system-aware light/dark themes. Phrases set in the
serif are separate i18n keys so translations stay plain `textContent`. All content
and links remain usable without JavaScript; enhancement controls (language, theme,
copy, clock, preview) appear only with JavaScript. Reduced motion removes every
animation and makes the preview follow without easing. Clipboard success and
failure must be announced accurately.

## Logo assets

*Karaboğa* means "black bull", so the mark is literally that: an off-white bull
head on an ink `#111113` tile — a crescent of horns, a tapering head, and two
angular eye cutouts that echo code chevrons. Three shapes, no outline, no badge:
an accent dot was tried and dropped because on an app icon it reads as an unread
notification. In the dark header the tile melts into the canvas and the bull
floats; in light mode it sits as a crisp black tile.

`favicon.svg` is the production vector source. The 16/32/48px ICO frames and the
180/192/512px PNGs are rendered from it in Chrome (each size rendered natively,
not downscaled) with transparent corners. `logo-concept.png` preserves the
earlier cobalt exploration and is not deployed in Docker.
