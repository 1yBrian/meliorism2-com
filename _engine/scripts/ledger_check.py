#!/usr/bin/env python3
"""ledger_check.py — DESIGN-LEDGER row exists for this issue and is fully populated.

Source: DESIGN-LEDGER.md + DESIGN-ENGINE.md Uniqueness Guarantee.
Today's Provenance Document deployed with "NEEDS BACKFILL" — that row should have
blocked the deploy. This script enforces:

  1. Ledger row exists for the issue's date or slug.
  2. All 5 coordinates populated: Weather, Archetype, Container, Primitive, Primary Hue.
     ("—" or "NEEDS BACKFILL" or empty = fail.)
  3. (container × primitive) pair not used in any prior issue.
  4. Primary hue not used in last 7 issues.
  5. Container family not used in last 14 issues.
  6. Archetype not same as immediately prior issue.

Container family taxonomy (from DESIGN-LEDGER.md):
   Instruments · Documents · Rooms/Chambers · Maps/Charts ·
   Natural spaces · Workbenches · Theaters · Archives

Usage:
    python3 ledger_check.py archive/2026-05-30-the-provenance-document.html
"""
import re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
LEDGER = REPO / "_engine" / "DESIGN-LEDGER.md"

# Container family heuristics — keywords map to families
FAMILY_KEYWORDS = {
    "Instruments":     ["barograph", "instrument", "gauge", "scope", "meter", "altimeter"],
    "Documents":       ["document", "log", "estimate", "chart", "register", "ledger", "letter", "report"],
    "Rooms/Chambers":  ["room", "chamber", "booth", "court", "theater", "hall", "operating room", "studio"],
    "Maps/Charts":     ["map", "chart", "diagram", "atlas", "blueprint"],
    "Natural spaces":  ["tide pool", "field", "river", "forest", "ocean", "shore", "beach", "meadow"],
    "Workbenches":     ["bench", "workshop", "lab", "kitchen", "shop"],
    "Theaters":        ["theater", "stage", "auditorium", "courtroom", "amphitheater"],
    "Archives":        ["archive", "vault", "library", "registry", "morgue"],
}

EMPTY_VALUES = {"", "—", "-", "—", "needs backfill", "tbd", "?", "n/a", "none"}

def get_meta(html: str, key: str) -> str | None:
    m = re.search(rf"<!-- meliorism2:{re.escape(key)}: (.+?) -->", html)
    return m.group(1).strip() if m else None

def parse_ledger() -> list[dict]:
    """Parse the main ledger table — return list of dicts ordered by row."""
    if not LEDGER.exists():
        return []
    text = LEDGER.read_text()
    # Find first markdown table block under "## Ledger"
    section = re.search(r"## Ledger\s*\n(.*?)\n##", text, re.DOTALL)
    if not section: return []
    rows = []
    for line in section.group(1).splitlines():
        if not line.strip().startswith("|"): continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 9: continue
        if cells[0].lower() in ("issue", ":---", "----", "---"): continue
        if not cells[0].replace("-", "").strip(): continue
        rows.append({
            "issue":     cells[0],
            "date":      cells[1],
            "slug":      cells[2],
            "weather":   cells[3],
            "archetype": cells[4],
            "container": cells[5],
            "primitive": cells[6],
            "hue":       cells[7],
            "notes":     cells[8] if len(cells) > 8 else "",
        })
    return rows

def is_empty(val: str) -> bool:
    return val.lower().strip() in EMPTY_VALUES

def family_of(container: str) -> str | None:
    c = container.lower()
    for fam, kws in FAMILY_KEYWORDS.items():
        if any(kw in c for kw in kws):
            return fam
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: ledger_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()
    slug = get_meta(html, "slug") or path.stem[11:]
    date = get_meta(html, "date") or path.stem[:10]

    rows = parse_ledger()
    if not rows:
        print(f"FAIL: DESIGN-LEDGER.md not found or empty. Cannot check uniqueness.")
        sys.exit(1)

    # Find the row for this issue
    row = next((r for r in rows if r["slug"] == slug or r["date"] == date), None)
    if not row:
        print(f"FAIL: No DESIGN-LEDGER row for {slug} ({date}). Add a row before publishing.")
        sys.exit(1)

    # Check all 5 coordinates populated
    missing = [k for k in ("weather", "archetype", "container", "primitive", "hue") if is_empty(row[k])]
    if missing:
        print(f"FAIL: {slug} ledger row incomplete. Missing: {missing}.")
        print(f"  Generated coordinates required before publish (DESIGN-ENGINE Generation Protocol).")
        sys.exit(1)

    # Find prior issues (rows above this one in the ledger)
    idx = rows.index(row)
    prior = rows[:idx]
    prior_with_data = [r for r in prior if not any(is_empty(r[k]) for k in ("weather","archetype","container","primitive","hue"))]

    violations = []

    # 1. (container × primitive) never repeats
    pair = (row["container"].lower(), row["primitive"].lower())
    for r in prior_with_data:
        if (r["container"].lower(), r["primitive"].lower()) == pair:
            violations.append(f"(container × primitive) repeats: {row['container']} × {row['primitive']} (last in {r['slug']})")

    # 2. Same primary hue within rolling 7-issue window
    for r in prior_with_data[-7:]:
        if r["hue"].lower() == row["hue"].lower():
            violations.append(f"Primary hue '{row['hue']}' reused within 7 issues (also in {r['slug']})")

    # 3. Same container family within rolling 14-issue window
    fam = family_of(row["container"])
    if fam:
        for r in prior_with_data[-14:]:
            if family_of(r["container"]) == fam:
                violations.append(f"Container family '{fam}' reused within 14 issues ({r['slug']} also used {fam})")
                break

    # 4. Same archetype as immediately prior issue
    if prior_with_data:
        prev = prior_with_data[-1]
        if prev["archetype"].lower() == row["archetype"].lower():
            violations.append(f"Archetype '{row['archetype']}' same as prior issue ({prev['slug']})")

    if violations:
        print(f"FAIL: {slug} ledger uniqueness violations:")
        for v in violations: print(f"  {v}")
        sys.exit(1)

    print(f"PASS: {slug} ledger row complete + unique across all enforcement rules.")
    sys.exit(0)

if __name__ == "__main__":
    main()
