#!/usr/bin/env python3
"""Find gaps and leaks in a Search Console performance export.

Usage: python3 scripts/gsc.py EXPORT [--min-impressions N]

EXPORT is the zip from Search Console → Performance → Export → Download CSV,
or the Queries.csv inside it (English or Turkish UI).

  LEAKS  page-1 queries whose CTR is under half of what this site's own
         queries at a similar position get. Fix first: rewrite the title and
         opening of the page that already ranks.
  GAPS   queries seen past page 1 that never got a click. Candidates for the
         next note.

Only the numbers in the export are used. CTR is recomputed from clicks and
impressions, so the locale's percent format doesn't matter.
"""

import argparse
import csv
import io
import statistics
import sys
import zipfile

BANDS = ((1, 3), (4, 6), (7, 10))
MIN_PEERS = 3  # fewer queries than this in a band → compare against all of page 1


def is_queries(text):
    head = text.split("\n", 1)[0].lower()
    return "quer" in head or "sorgu" in head


def read_queries(path):
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if n.lower().endswith(".csv")]
            texts = (z.read(n).decode("utf-8-sig") for n in names)
            text = next((t for t in texts if is_queries(t)), None)
            if text is None:
                sys.exit(f"no queries CSV in {path} (found: {', '.join(names)})")
    else:
        with open(path, encoding="utf-8-sig") as f:
            text = f.read()
        if not is_queries(text):
            sys.exit(f"{path} is not a queries export (expected Queries.csv)")
    return list(csv.reader(io.StringIO(text)))


def parse(rows):
    # columns are positional in every UI language: query, clicks, impressions, CTR, position
    out = []
    for row in rows[1:]:
        if len(row) < 5 or not row[0].strip():
            continue
        clicks = int("".join(c for c in row[1] if c.isdigit()) or 0)
        impressions = int("".join(c for c in row[2] if c.isdigit()) or 0)
        position = float(row[4].replace(",", "."))
        if impressions:
            out.append(
                {
                    "query": row[0].strip(),
                    "clicks": clicks,
                    "impressions": impressions,
                    "ctr": clicks / impressions,
                    "position": position,
                }
            )
    return out


def band_of(position):
    for lo, hi in BANDS:
        if position < hi + 0.5:
            return (lo, hi)
    return None


def leaks(queries, min_impressions):
    page1 = [q for q in queries if q["position"] < 10.5]
    if len(page1) < MIN_PEERS:
        print(f"\nonly {len(page1)} page-1 queries: too few to judge CTR, skipping leaks")
        return []
    overall = statistics.median(q["ctr"] for q in page1)
    medians = {}
    for band in BANDS:
        peers = [q["ctr"] for q in page1 if band_of(q["position"]) == band]
        medians[band] = statistics.median(peers) if len(peers) >= MIN_PEERS else overall
    found = []
    for q in page1:
        expected = medians[band_of(q["position"])]
        if q["impressions"] >= min_impressions and expected and q["ctr"] < expected / 2:
            found.append({**q, "expected": expected})
    return sorted(found, key=lambda q: -q["impressions"])


def gaps(queries, min_impressions):
    found = [
        q
        for q in queries
        if q["position"] >= 10.5 and q["clicks"] == 0 and q["impressions"] >= min_impressions
    ]
    return sorted(found, key=lambda q: -q["impressions"])


def table(title, rows, expected):
    print(f"\n{title} ({len(rows)})")
    if not rows:
        print("  none")
        return
    width = min(max(len(r["query"]) for r in rows), 60)
    head = f"  {'query':<{width}}  {'impr':>7}  {'clicks':>6}  {'pos':>5}  {'ctr':>6}"
    print(head + ("  site median" if expected else ""))
    for r in rows:
        line = (
            f"  {r['query'][:width]:<{width}}  {r['impressions']:>7}  {r['clicks']:>6}"
            f"  {r['position']:>5.1f}  {r['ctr']:>6.1%}"
        )
        print(line + (f"  {r['expected']:>11.1%}" if expected else ""))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("export")
    p.add_argument("--min-impressions", type=int, default=20)
    args = p.parse_args()

    queries = parse(read_queries(args.export))
    print(f"{len(queries)} queries, min {args.min_impressions} impressions")
    table("LEAKS — rewrite the ranking page's title and opening", leaks(queries, args.min_impressions), True)
    table("GAPS — candidates for the next note", gaps(queries, args.min_impressions), False)


if __name__ == "__main__":
    main()
