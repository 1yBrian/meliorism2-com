#!/usr/bin/env python3
"""typography_floor.py — No font-size below 0.8rem anywhere.

Source: MELIORISM2-DIRECTIVE.md §7d "The Floor" + DESIGN-ENGINE.md "HARD TYPOGRAPHY FLOOR".
Brian standard — non-negotiable. The engine-proof run violated this and had to be fixed after.

Usage:
    python3 typography_floor.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

FONT_SIZE_RE = re.compile(r"font-size\s*:\s*(\d*\.?\d+)\s*(rem|em|px)", re.IGNORECASE)
FLOOR_REM = 0.8
FLOOR_PX = 13  # 0.8rem at 16px base

def violates(value: float, unit: str) -> bool:
    if unit == "rem" or unit == "em":
        return value < FLOOR_REM
    if unit == "px":
        return value < FLOOR_PX
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: typography_floor.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    violations = []
    for m in FONT_SIZE_RE.finditer(html):
        val = float(m.group(1)); unit = m.group(2).lower()
        if violates(val, unit):
            # Find approximate line number
            line_no = html[:m.start()].count("\n") + 1
            violations.append((line_no, f"{val}{unit}"))

    if violations:
        print(f"FAIL: {path.name} has {len(violations)} font-size(s) below the {FLOOR_REM}rem floor:")
        for line, size in violations[:20]:
            print(f"  line ~{line}: font-size:{size}")
        if len(violations) > 20:
            print(f"  ...and {len(violations)-20} more")
        sys.exit(1)
    print(f"PASS: {path.name} typography floor respected.")
    sys.exit(0)

if __name__ == "__main__":
    main()
