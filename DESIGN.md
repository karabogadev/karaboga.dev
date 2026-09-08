# Design direction

A personal portfolio for Cihat Karaboğa, a mobile software engineer. Help a
prospective collaborator understand his specialty, inspect his work, and contact him.

## Visual system

- Canvas: `#f7f8fc`; paper: `#ffffff`; ink: `#192238`.
- Secondary text: `#576176`; blue: `#3659db`; lavender: `#e9eafd`.
- Dark mode: `#101522` canvas, `#171e2e` paper, `#edf0fa` ink, `#aab4ca`
  secondary text, `#a9b9ff` interactive text.
- Manrope for expressive headings and readable body text. System monospace only
  for actual code in the project illustration.
- 1160px content width; generous section spacing; left-aligned text; distinct
  heading, project, and supporting-content scales.

## Composition

```text
brand             section navigation          language / theme
name + specialty + contact       interactive mobile interface study
selected work                    GitHub link
mirror app project               architecture project
game project                     website project
experience introduction          career timeline
about                            technology groups
contact invitation               two emails + individual copy actions
social links                     copyright
```

The memorable element is a device illustration grounded in mobile development.
Project illustrations explain their subject: a phone mirrored into a Mac window,
architecture, a driving game, and the portfolio itself. They are interface studies,
not claimed product screenshots. Work is a two-by-two grid so a fourth project stays
balanced.
Avoid decorative metrics, repetitive numbered headings, gradients, and scroll-hidden
content. The brand mark is a white geometric bull on cobalt blue, with angular eye cutouts
that echo code chevrons. Blue connects the identity to interactive controls.

## Interaction and accessibility

Keep all navigation available on mobile in a second header row. Give links and
controls generous touch targets, visible focus, and clear selected states. Preserve
English/Turkish switching and system-aware light/dark themes. All content and links
remain usable without JavaScript; enhancement controls appear only with JavaScript.
Respect reduced motion. Clipboard success and failure must be announced accurately.

## Plan review

Replaced the old narrow numbered rail with a wider portfolio composition. Kept the
bold visual treatment in the mobile study; surrounding sections use quiet typography
and spacing. Retained the static, self-contained page and original career facts.

## Logo assets

`favicon.svg` is the production vector source. PNG app icons and the multi-size
ICO are rasterized from this SVG so every placement uses the same mark.
`logo-concept.png` preserves the built-in image-generation exploration; the final
vector simplifies that exploration for clarity at favicon sizes.

Image-generation prompt: a single geometric white bull head on cobalt `#3659db`,
wide upward horns, a tapered face, and subtle angular code-chevron eyes; flat,
symmetric, no text, shadows, gradients, or mascot styling; readable at 16px.
