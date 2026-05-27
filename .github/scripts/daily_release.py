#!/usr/bin/env python3
"""
daily_release.py — Meliorism2 automated homepage updater.

Run by GitHub Actions at 08:00 UTC (midnight PST) daily.
Finds today's pre-built archive issue, reads its metadata comments,
and updates index.html to show it as the current issue.

Usage:
  python3 daily_release.py              # use today's date (UTC = PST date at midnight)
  python3 daily_release.py 2026-05-28   # override date (for testing or catchup)
"""

import re
import sys
import glob
import os
from datetime import datetime, timezone


def slug_to_title(slug):
    if not slug:
        return "Untitled"
    return " ".join(w.capitalize() for w in slug.split("-"))


def get_meta(content, key):
    m = re.search(rf"<!-- meliorism2:{re.escape(key)}: (.+?) -->", content)
    return m.group(1).strip() if m else None


DIMENSION_COLORS = {
    "somatic":              "var(--dim-witnessing)",
    "body intelligence":    "var(--dim-witnessing)",
    "witnessing":           "var(--dim-witnessing)",
    "brave spaces":         "var(--dim-brave)",
    "living income":        "var(--dim-income)",
    "becoming adaptable":   "var(--dim-income)",
    "in-person presence":   "var(--dim-presence)",
    "presence":             "var(--dim-presence)",
    "gender":               "var(--dim-gender)",
}


def dimension_color(dimension):
    if not dimension:
        return "var(--dim-witnessing)"
    d = dimension.lower()
    for key, val in DIMENSION_COLORS.items():
        if key in d:
            return val
    return "var(--dim-witnessing)"


def format_display_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %-d, %Y")
    except Exception:
        return date_str


def find_archive_file(date_str):
    matches = glob.glob(f"archive/{date_str}-*.html")
    # Exclude index.html and non-issue files
    matches = [m for m in matches if re.match(r"archive/\d{4}-\d{2}-\d{2}-.+\.html$", m)]
    return sorted(matches)[0] if matches else None


def count_archive_issues():
    return len([
        f for f in glob.glob("archive/*.html")
        if re.match(r"archive/\d{4}-\d{2}-\d{2}-.+\.html$", f)
    ])


def get_concept(content, slug):
    """Get concept text from metadata comment or fall back to entry-sub."""
    concept = get_meta(content, "concept")
    if concept:
        return concept
    m = re.search(r'class="entry-sub"[^>]*>\s*([^<]+)\s*<', content)
    if m:
        return m.group(1).strip()
    return ""


def get_link_text(content):
    """Get the entry CTA button text to reuse as the featured link text."""
    m = re.search(r'class="entry-enter"[^>]*>\s*([^<]+)\s*<', content)
    return m.group(1).strip() if m else "Read the issue →"


def update_index(archive_file, issue_meta):
    with open("index.html") as f:
        idx = f.read()

    slug        = issue_meta["slug"]
    issue_num   = issue_meta["issue_num"]
    title       = issue_meta["title"]
    dimension   = issue_meta["dimension"]
    display_date = issue_meta["display_date"]
    concept     = issue_meta["concept"]
    dim_color   = issue_meta["dim_color"]
    archive_path = issue_meta["archive_path"]
    link_text   = issue_meta["link_text"]
    issue_count = issue_meta["issue_count"]

    # ── Hero CTA link ────────────────────────────────────────────────────────
    idx = re.sub(
        r'(<a href=")[^"]*(" class="hero-cta">Read Current Issue</a>)',
        rf'\g<1>{archive_path}\g<2>',
        idx
    )

    # ── Featured card border color ───────────────────────────────────────────
    idx = re.sub(
        r'(\.featured-card \{[^}]*border-left: 4px solid )var\(--dim-[a-z]+\)',
        rf'\g<1>{dim_color}',
        idx
    )

    # ── Featured dimension color ─────────────────────────────────────────────
    idx = re.sub(
        r'(\.featured-dimension \{[^}]*color: )var\(--dim-[a-z]+\)',
        rf'\g<1>{dim_color}',
        idx
    )

    # ── Issue number ─────────────────────────────────────────────────────────
    idx = re.sub(
        r'(<div class="featured-meta">[^<]*<span>Issue )\d+(</span>)',
        rf'\g<1>{issue_num}\g<2>',
        idx
    )

    # ── Display date ─────────────────────────────────────────────────────────
    idx = re.sub(
        r'(<span>)[A-Za-z]+ \d+, \d+(</span>\s*<span class="sep">·</span>\s*<span class="featured-dimension">)',
        rf'\g<1>{display_date}\g<2>',
        idx
    )

    # ── Dimension label ──────────────────────────────────────────────────────
    idx = re.sub(
        r'(<span class="featured-dimension">)[^<]*(</span>)',
        rf'\g<1>{dimension}\g<2>',
        idx
    )

    # ── Issue title ──────────────────────────────────────────────────────────
    idx = re.sub(
        r'(<h2 class="featured-title">)[^<]*(</h2>)',
        rf'\g<1>{title}\g<2>',
        idx
    )

    # ── Concept paragraph ────────────────────────────────────────────────────
    concept_clean = concept.replace("\\", "\\\\")
    idx = re.sub(
        r'(<p class="featured-concept">).*?(</p>)',
        rf'\g<1>\n        {concept_clean}\n      \g<2>',
        idx,
        flags=re.DOTALL
    )

    # ── Featured read link ───────────────────────────────────────────────────
    idx = re.sub(
        r'(<a href=")[^"]*(" class="featured-link">\s*).*?(\s*</a>)',
        rf'\g<1>{archive_path}\g<2>{link_text}\g<3>',
        idx,
        flags=re.DOTALL
    )

    # ── Archive count ────────────────────────────────────────────────────────
    idx = re.sub(
        r'(Access the Archive · )\d+( issues →)',
        rf'\g<1>{issue_count}\g<2>',
        idx
    )

    with open("index.html", "w") as f:
        f.write(idx)


def main():
    date_str = sys.argv[1].strip() if len(sys.argv) > 1 and sys.argv[1].strip() else None
    if not date_str:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"Looking for issue on: {date_str}")

    archive_file = find_archive_file(date_str)
    if not archive_file:
        print(f"No archive file found for {date_str} — nothing to release today.")
        sys.exit(0)

    print(f"Found: {archive_file}")

    with open(archive_file) as f:
        content = f.read()

    slug       = get_meta(content, "slug") or ""
    issue_num  = get_meta(content, "issue") or "???"
    title      = get_meta(content, "title") or slug_to_title(slug)
    dimension  = get_meta(content, "dimension") or "Practitioner Work"
    concept    = get_concept(content, slug)
    link_text  = get_link_text(content)
    dim_color  = dimension_color(dimension)
    display_date = format_display_date(date_str)
    archive_path = f"/archive/{os.path.basename(archive_file)}"
    issue_count = count_archive_issues()

    meta = {
        "slug": slug,
        "issue_num": issue_num,
        "title": title,
        "dimension": dimension,
        "concept": concept,
        "link_text": link_text,
        "dim_color": dim_color,
        "display_date": display_date,
        "archive_path": archive_path,
        "issue_count": issue_count,
    }

    print(f"  Issue {issue_num}: {title}")
    print(f"  Dimension: {dimension}")
    print(f"  Concept: {concept[:80]}..." if len(concept) > 80 else f"  Concept: {concept}")

    update_index(archive_file, meta)

    # Write slug to /tmp for the commit message
    with open("/tmp/release_slug", "w") as f:
        f.write(f"{date_str}-{slug}" if slug else date_str)

    print(f"✓ index.html updated for Issue {issue_num}: {title}")


if __name__ == "__main__":
    main()
