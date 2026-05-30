#!/usr/bin/env python3
"""rollback.py — Re-promote yesterday's (or specified) issue to the homepage.

Wraps daily_release.py with a date override. Then prints the curl command
to push index.html via the GitHub Contents API (no raw git push).

Usage:
    python3 _engine/scripts/rollback.py              # roll back to yesterday
    python3 _engine/scripts/rollback.py 2026-05-28   # roll back to specific date
"""
import sys, subprocess, pathlib
from datetime import datetime, timezone, timedelta

REPO = pathlib.Path(__file__).resolve().parents[2]
DAILY = REPO / ".github" / "scripts" / "daily_release.py"

def main():
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    else:
        date_str = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"Rolling homepage back to: {date_str}")
    result = subprocess.run(["python3", str(DAILY), date_str], cwd=str(REPO))
    if result.returncode != 0:
        print("daily_release.py failed during rollback."); sys.exit(1)
    print("\nindex.html patched locally. To publish:")
    print(f"  cd {REPO}")
    print(f'  ./deploy-api.sh "Rollback: re-promote {date_str} [manual]" index.html')

if __name__ == "__main__":
    main()
