#!/usr/bin/env python3
"""palette_check.py — Dark/black backgrounds must be EARNED.

Rule from LEARNING-LOG.md (2026-05-27):
  "Black as default entry screen | Flagged | Dark backgrounds must be earned
   from content. Not a default. Open palette is the baseline."

Default palette is light/open. To use a dark or near-black entry screen,
the issue must declare both:
    <!-- meliorism2:palette: dark -->
    <!-- meliorism2:palette-justification: <one sentence on why dark is earned> -->

A justification under 20 characters or containing template phrases ("default",
"because", "always") is a fail — it must name a specific reason from content.

Usage:
    python3 palette_check.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

# Heuristic: if any of the first 5 background declarations include a very-dark color, flag.
DARK_BG_RE = re.compile(
    r"background[^;]*:[^;]*"
    r"(?:#0[0-9a-f]{1,2}[0-9a-f]{0,3}"     # #0xx or #0xxx or #0xxxxx pattern (very dark hex)
    r"|#1[0-2][0-9a-f]{1,4}"                # #1x0..#12x (also very dark)
    r"|rgba?\(\s*[0-9]{1,2}\s*,\s*[0-9]{1,2}\s*,\s*[0-9]{1,2}"  # low-rgb
    r")",
    re.IGNORECASE
)

LAZY_JUSTIFICATIONS = {"default", "always", "looks good", "house style", "house", "standard", "n/a", "none"}
MIN_JUSTIFICATION_LEN = 20

def get_meta(html: str, key: str) -> str | None:
    m = re.search(rf"<!-- meliorism2:{re.escape(key)}: (.+?) -->", html)
    return m.group(1).strip() if m else None

def has_dark_entry(html: str) -> bool:
    # Look for backgrounds tied to entry/hero/main-screen classes
    blocks = re.findall(
        r"\.(?:entry|hero|cover|entry-bg|hero-bg|main-screen|entry-screen)[^{]*\{[^}]*\}",
        html, re.IGNORECASE | re.DOTALL
    )
    for blk in blocks:
        if DARK_BG_RE.search(blk):
            return True
    # Fallback: scan first ~3kb of style block
    style_m = re.search(r"<style[^>]*>(.{0,3000})", html, re.IGNORECASE | re.DOTALL)
    if style_m and DARK_BG_RE.search(style_m.group(1)):
        return True
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: palette_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    declared = (get_meta(html, "palette") or "").lower().strip()
    justification = get_meta(html, "palette-justification") or ""
    dark_detected = has_dark_entry(html)

    if dark_detected and declared != "dark":
        print(f"FAIL: {path.name} uses dark entry-screen colors but did not declare:")
        print('  <!-- meliorism2:palette: dark -->')
        print('  <!-- meliorism2:palette-justification: ... -->')
        print("  LEARNING-LOG rule: dark backgrounds must be earned from content. Default is light.")
        sys.exit(1)

    if declared == "dark":
        if len(justification.strip()) < MIN_JUSTIFICATION_LEN:
            print(f"FAIL: {path.name} declares dark palette with no real justification.")
            print(f"  Got: '{justification}'  (need ≥{MIN_JUSTIFICATION_LEN} chars naming why this subject earns dark)")
            sys.exit(1)
        if justification.lower().strip() in LAZY_JUSTIFICATIONS:
            print(f"FAIL: {path.name} dark-palette justification is lazy: '{justification}'.")
            print("  Name the content reason. Example: 'Issue 027 earned dark because tide + night + co-presence have genuine depth.'")
            sys.exit(1)
        print(f"PASS: {path.name} dark palette earned — justification: '{justification[:60]}...'")
        sys.exit(0)

    print(f"PASS: {path.name} light palette (default).")
    sys.exit(0)

if __name__ == "__main__":
    main()
