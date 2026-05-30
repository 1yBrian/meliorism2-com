#!/usr/bin/env python3
"""preflight.py — Pre-release validator. Runs every night at 8 PM PT.

Targets the NEXT day's archive file by default. Runs the full editorial review.

  exit 0 — ready (every gate passed)
  exit 1 — blocked (at least one HARD gate failed; human action needed)
  exit 2 — regression (HARD pass, SOFT warn — ships but flagged)
  exit 3 — NO_ARCHIVE (no file for tomorrow; evergreen reserve should promote)

If exit 1 or 2 or 3, the workflow telegrams Brian.

Usage:
    python3 _engine/scripts/preflight.py [YYYY-MM-DD]
"""
import sys, subprocess, pathlib, re
from datetime import datetime, timezone, timedelta

REPO = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "_engine" / "scripts"

def find_archive(date_str: str) -> pathlib.Path | None:
    matches = list((REPO / "archive").glob(f"{date_str}-*.html"))
    matches = [m for m in matches if re.match(r"\d{4}-\d{2}-\d{2}-.+\.html$", m.name)]
    return sorted(matches)[0] if matches else None

def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].strip() else (
        datetime.now(timezone.utc) + timedelta(days=1)
    ).strftime("%Y-%m-%d")
    print(f"Pre-flight target: {date_str}")
    arch = find_archive(date_str)
    if not arch:
        print(f"NO_ARCHIVE: no file for {date_str}. Evergreen reserve should promote.")
        sys.exit(3)
    print(f"Checking: {arch.relative_to(REPO)}\n")
    # Run the full editor review
    result = subprocess.run(["python3", str(SCRIPTS / "editor_review.py"), str(arch), "--skip-links"])
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
