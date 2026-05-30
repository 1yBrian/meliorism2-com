#!/usr/bin/env python3
"""section_title_score.py — Scoring standard from MELIORISM2-DIRECTIVE.md §15.

Each h2/h3 section title earns +1 if it:
  - uses a specific named concept, person, place, year, or phenomenon, OR
  - is evocative / narrative / poetic, OR
  - is accessed via interactive navigation (card, tab, panel, hotspot)

Sections that do NOT earn the point: generic newsletter titles
("The Research", "The Data", "Sources", "Background", "Key Takeaways",
"Introduction", "Conclusion", etc.)

  - Issue scoring below 7 = regression (warn)
  - Issue scoring below 5 = gate failure (fail)

Usage:
    python3 section_title_score.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

GENERIC_TITLES = {
    "the research", "the data", "the evidence", "the findings", "the takeaway",
    "key takeaways", "key insights", "sources", "background", "context",
    "introduction", "conclusion", "summary", "the concept", "the principle",
    "the framework", "the research anchors", "three research anchors",
    "the application", "applications", "implications",
}

NAMED_NOUN_RE = re.compile(r"\b(?:19|20)\d{2}\b|[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+|[A-Z]{2,}")
POETIC_HINTS_RE = re.compile(r"\b(?:the|a)\s+(?:[a-z]+\s+){0,2}[a-z]+(?:'s|’s|’)?\s+[a-z]+\b", re.IGNORECASE)

H_RE = re.compile(r"<(h[1-3])[^>]*>([^<]+)</\1>", re.IGNORECASE)

def earns_point(title: str) -> bool:
    norm = title.strip().lower()
    if norm in GENERIC_TITLES:
        return False
    # Specific named concept/person/place/year
    if NAMED_NOUN_RE.search(title):
        return True
    # Evocative / narrative — has at least 3 words and isn't on the generic list
    words = norm.split()
    if len(words) >= 3 and norm not in GENERIC_TITLES:
        return True
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: section_title_score.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    titles = [(m.group(1), m.group(2).strip()) for m in H_RE.finditer(html)]
    if not titles:
        print(f"FAIL: {path.name} has no h1/h2/h3 headings to score.")
        sys.exit(1)

    earning, generic = [], []
    score = 0
    for tag, title in titles:
        if earns_point(title):
            earning.append(title); score += 1
        else:
            generic.append(title)

    # +1 for citation depth (>6 sources)
    citation_pattern = re.compile(r'\[(\d+)\]')
    cite_max = max([int(n) for n in citation_pattern.findall(html)] or [0])
    if cite_max > 6:
        score += 1
    # +2 for immersive cover (entry-bg with background image)
    if re.search(r'class="entry-bg"[^>]*>|\.entry-bg\s*\{[^}]*background[^}]*url\(', html):
        score += 2

    msg = (
        f"  Sections earning point ({len(earning)}): " + (', '.join(f'\"{t}\"' for t in earning[:6]) + ('…' if len(earning)>6 else '')) + "\n"
        f"  Generic titles (no point): " + (', '.join(f'\"{t}\"' for t in generic[:6]) + ('…' if len(generic)>6 else '') if generic else "(none)") + f"\n"
        f"  Citation depth bonus: {'+1' if cite_max>6 else '0'} (max footnote: [{cite_max}])\n"
        f"  Immersive cover bonus: {'+2' if score>=len(earning)+(1 if cite_max>6 else 0)+2 else '0'}\n"
        f"  Total score: {score}"
    )

    if score < 5:
        print(f"FAIL: {path.name} scores {score} — gate failure (below 5). Rebuild.")
        print(msg); sys.exit(1)
    if score < 7:
        print(f"WARN: {path.name} scores {score} — regression (below 7).")
        print(msg); sys.exit(0)  # warn only, do not block
    print(f"PASS: {path.name} scores {score}.")
    print(msg); sys.exit(0)

if __name__ == "__main__":
    main()
