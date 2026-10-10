# Writing notes

Rules every post under `/notes/` follows — whether Cihat writes it or an AI
drafts it from his brief. The point of a note is to put something on the
internet that wasn't there before: a thing that actually happened in his work.
If a draft could have been written by someone who wasn't there, it isn't done.

## The brief (input)

One note = one keyword + one true story. Fill this in before any drafting:

```text
Keyword:      the query someone types (from Search Console, or a real question)
What happened: the project, the problem, what was tried, what worked
Numbers:      only ones that were measured — with where they came from
Sources:      repo + file paths, commit, PR, screenshot, store listing
Next step:    what a reader who wants more should do (repo, contact, related note)
```

## Rules

1. **Every fact has a source.** Code facts cite a file in a public repo; numbers
   come from the brief. No source → the sentence goes. Never estimate, round up
   or "typically" a number.
2. **The real example comes first.** The first screen says what happened, in
   which project, and what broke. Background comes after, if at all.
3. **Say what didn't work.** The dead ends are the information gain — nobody
   else has them.
4. **Title earns the click.** Name the specific thing (tool, error, version,
   number), not the topic. Under ~60 characters. No "ultimate guide".
5. **Description answers the query.** The meta description is the one-sentence
   answer an AI overview could quote, not a teaser.
6. **Versions are explicit.** Package, SDK, OS and tool versions as they were
   when it happened. Advice without a version expires silently.
7. **Code is real.** Excerpts are verbatim from the repo, trimmed with `// …`,
   and link to the file at a commit — not to `main`, which moves.
8. **Limits are stated.** What the approach doesn't handle, said plainly, near
   the end.
9. **One clear next step.** Each note ends with exactly one: the repo, a related
   note, or getting in touch.
10. **Plain English, first person.** Short sentences. No filler intros, no
    "in today's fast-paced world", no recap paragraph.
11. **Cihat reads it before it ships.** An AI draft is a draft. Nothing is
    deployed until he has read every line and would say it out loud.

## Publishing checklist

- [ ] `notes/<slug>.html` from `notes/_template.html` — slug is the keyword,
      lowercase, hyphenated
- [ ] `<title>`, description, canonical, OG, and `BlogPosting` JSON-LD filled;
      `datePublished` / `dateModified` match the visible date
- [ ] Listed at the top of `notes/index.html` and in the home page Notes section
      (keep the latest three there)
- [ ] `sitemap.xml` entry with `lastmod`; bump `lastmod` for `/notes/` too
- [ ] Linked from at least one older note where it genuinely helps
- [ ] Deployed, then `scripts/indexnow.sh https://karaboga.dev/notes/<slug>`
- [ ] Shared where the readers are (see below), linking back to the note

## Beyond the site

AI answers repeat the names they keep seeing next to a topic, on other sites
more than on your own. After a note ships:

- Cross-post to dev.to or Medium with the canonical URL set to the karaboga.dev
  note.
- Link the note from the README of the repo it's about.
- Share it where Flutter developers already talk (r/FlutterDev, Flutter Türkiye
  communities, X) — as a useful answer, not a link drop.

## Finding the next keyword

Export Search Console → Performance (last 3 months) and run:

```bash
python3 scripts/gsc.py ~/Downloads/karaboga.dev-Performance-on-Search-*.zip
```

**Leaks** (page 1, clicks below what that position usually gets on this site)
are fixed first: rewrite the title and opening of the page that ranks. **Gaps**
(seen past page 1, never clicked) become the next brief.
