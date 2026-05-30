#!/usr/bin/env python3
"""preflight.py — Pre-release validator. Runs every night at 8 PM PT.

Targets the NEXT day's archive file by default (i.e. tomorrow's UTC date).
Runs every deterministic gate against it. If any fail, prints specifics and
exits 1 — the workflow then alerts via Telegram.

If no archive file exists for tomorrow, exits 2 (separate signal — "no issue
prepared" — so monitor can promote an evergreen reserve).

Usage:
    python3 _engine/scripts/preflight.py [YYYY-MM-DD]
"""
import sys, subprocess, pathlib, glob, re
from datetime import datetime, timezone, timedelta

REPO = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "_engine" / "scripts"

GATES = [
    ("citation_check.py", "Citations"),
    ("photo_check.py",    "Photo attribution"),
    ("truth_lint.py",     "Truth (deterministic)"),
    ("link_check.py",     "External links"),
]

def find_archive(date_str: str) -> pathlib.Path | None:
    matches = list((REPO / "archive").glob(f"{date_str}-*.html"))
    matches = [m for m in matches if re.match(r"\d{4}-\d{2}-\d{2}-.+\.html$", m.name)]
    return sorted(matches)[0] if matches else None

def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else (datetime.now(timezone.utc) + timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"Pre-flight target: {date_str}")
    arch = find_archive(date_str)
    if not arch:
        print(f"NO_ARCHIVE: no file for {date_str}. Evergreen reserve will be promoted.")
        sys.exit(2)
    print(f"Checking: {arch.relative_to(REPO)}")
    failed = []
    for script, label in GATES:
        path = SCRIPTS / script
        if not path.exists():
            print(f"  [{label}] script missing — skipped"); continue
        result = subprocess.run(["python3", str(path), str(arch)], capture_output=True, text=True)
        print(f"--- {label} ---")
        print(result.stdout, end="")
        if result.stderr: print(result.stderr, end="")
        if result.returncode != 0:
            failed.append(label)
    if failed:
        print(f"\nPRE-FLIGHT FAIL: {', '.join(failed)}")
        sys.exit(1)
    print("\nPRE-FLIGHT PASS — ready for release.")
    sys.exit(0)

if __name__ == "__main__":
    main()
