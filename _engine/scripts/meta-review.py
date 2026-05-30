#!/usr/bin/env python3
"""
meta-review.py — structural audit of the Meliorism2 archive (FREE, no API).

Surfaces the things an editor should resolve before amplifying SEO:
  - duplicate / near-duplicate TITLES
  - DATE collisions (two issues on one day)
  - near-identical FILES (content overlap — true duplicates)
  - dimension balance (coverage across the taxonomy)

Reads the issue dataset from archive/index.html and the files themselves.
Run from repo root:  python3 _engine/scripts/meta-review.py
"""
import re, glob, os, html as html_lib
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def issues():
    # Audit the ACTUAL files on disk (not the index list, which can miss dupes/collisions).
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "archive", "[0-9]*.html"))):
        b = os.path.basename(p)
        h = open(p).read()
        m = re.search(r"<title>(.*?)</title>", h, re.S)
        raw = html_lib.unescape(m.group(1)).strip() if m else b
        title = raw.split("·")[-1].strip()          # human title after the last separator
        dm = re.match(r"(\d{4}-\d{2}-\d{2})", b)
        out.append({"file": b, "title": title, "date": dm.group(1) if dm else ""})
    return out

def prose(path):
    t = open(path).read()
    t = re.sub(r'<script[^>]*>.*?</script>', ' ', t, flags=re.DOTALL)
    t = re.sub(r'<style[^>]*>.*?</style>', ' ', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t); t = html_lib.unescape(t)
    return set(re.sub(r'\s+', ' ', t.lower()).split())

def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0

def main():
    items = issues()
    print(f"META REVIEW — {len(items)} issues\n{'='*60}")

    # 1. Duplicate / near-duplicate titles
    by_title = defaultdict(list)
    for it in items:
        by_title[it.get("title", "").strip().lower()].append(it["file"])
    dup_titles = {t: fs for t, fs in by_title.items() if len(fs) > 1}
    print(f"\n[1] DUPLICATE TITLES: {len(dup_titles)}")
    for t, fs in dup_titles.items():
        print(f"    “{t}” → {', '.join(fs)}")

    # 2. Date collisions
    by_date = defaultdict(list)
    for it in items:
        by_date[it.get("date", "")].append(it["file"])
    dup_dates = {d: fs for d, fs in by_date.items() if len(fs) > 1}
    print(f"\n[2] DATE COLLISIONS: {len(dup_dates)}")
    for d, fs in dup_dates.items():
        print(f"    {d} → {', '.join(fs)}")

    # 3. Near-identical files (content overlap > 0.6 Jaccard on word sets)
    print(f"\n[3] NEAR-IDENTICAL FILES (content overlap > 0.6):")
    paths = [os.path.join(ROOT, "archive", it["file"]) for it in items if os.path.exists(os.path.join(ROOT, "archive", it["file"]))]
    bag = {p: prose(p) for p in paths}
    seen = set(); pairs = 0
    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            sim = jaccard(bag[paths[i]], bag[paths[j]])
            if sim > 0.6:
                pairs += 1
                print(f"    {sim:.2f}  {os.path.basename(paths[i])}  ≈  {os.path.basename(paths[j])}")
    if not pairs:
        print("    none above threshold")

    # 4. Dimension balance
    dims = Counter(it.get("dimension", "—") for it in items)
    print(f"\n[4] DIMENSION BALANCE ({len(dims)} dimensions):")
    for k, v in dims.most_common():
        print(f"    {v:2}  {k}")

    print(f"\n{'='*60}\nRecommend (editor's call): merge/redirect duplicate titles & true-duplicate files;")
    print("give date-collision issues distinct canonical URLs; thin 1-issue dimensions will fill in over time.")

if __name__ == '__main__':
    main()
