#!/usr/bin/env python3
"""
auto_publish.py — the deterministic daily PUBLISH step (Task 2 of 2).

Brian's design: two daily scheduled tasks — pre-write (readiness) then
ready-to-print → confirm ready → publish. Default: a new issue published daily
IF it passes all checks AND has the minimums. No Telegram.

This script is the publish half. It is DETERMINISTIC and FREE:
  1. Find TODAY's issue in archive/ (newest YYYY-MM-DD-*.html with date <= today).
  2. Run editor_review.py (all HARD gates: image, citation, ledger, typography,
     palette, truth, unsplash, photo, help-rule). Exit 0 = passes all checks.
  3. If it passes → run build-pages.py (makes today's issue the live hero) →
     deploy via deploy-api.sh.
  4. If it FAILS or no issue exists → do NOT publish; the prior day stays live.
  5. Log every run to _engine/auto-publish.log.

NEVER calls a paid API. NEVER generates content. Only publishes what already
exists and already passes the gate. (The generative "pre-write" is a separate,
human-/charge-gated step per the iron rule.)

Usage:
  python3 auto_publish.py            # publish today's issue if it passes
  python3 auto_publish.py --dry-run  # do everything EXCEPT deploy (test mode)
  python3 auto_publish.py 2026-05-31 # target a specific date
"""
import sys, subprocess, pathlib, re
from datetime import datetime, timezone, timedelta

REPO = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "_engine" / "scripts"
LOG = REPO / "_engine" / "auto-publish.log"

def log(msg):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    line = f"[{stamp}] {msg}"
    print(line)
    try:
        with open(LOG, "a") as f: f.write(line + "\n")
    except Exception: pass

def find_today_issue(date_str):
    """Newest dated issue with date <= target (matches build-pages hero logic)."""
    files = []
    for m in (REPO / "archive").glob("*.html"):
        mt = re.match(r"(\d{4}-\d{2}-\d{2})-.+\.html$", m.name)
        if mt and mt.group(1) <= date_str:
            files.append((mt.group(1), m))
    if not files: return None
    files.sort()
    return files[-1][1]  # newest <= today

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO))
    return r.returncode, (r.stdout + r.stderr)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    date_str = args[0] if args else datetime.now(timezone.utc).strftime("%Y-%m-%d")

    log(f"=== auto_publish run · target {date_str}{' · DRY-RUN' if dry else ''} ===")
    issue = find_today_issue(date_str)
    if not issue:
        log(f"NO_ISSUE for {date_str}. Nothing to publish; prior day stays live.")
        sys.exit(3)
    log(f"Today's issue: {issue.name}")

    # ── GATE: all hard checks must pass ──
    code, out = run(["python3", str(SCRIPTS / "editor_review.py"), str(issue), "--skip-links"])
    verdict = [l for l in out.splitlines() if l.startswith("VERDICT")]
    log("Gate: " + (verdict[0] if verdict else f"exit {code}"))
    if code != 0:
        # show which hard gates failed
        for l in out.splitlines():
            if "❌" in l or "FAIL" in l: log("  " + l.strip())
        log("BLOCKED — issue does not pass checks. Not publishing.")
        sys.exit(1)

    # ── PUBLISH: rebuild homepage/archive so today's issue is the hero ──
    code, out = run(["python3", str(SCRIPTS / "build-pages.py")])
    if code != 0:
        log("build-pages FAILED — not deploying."); log(out[-400:]); sys.exit(1)
    log("build-pages: homepage + archive regenerated (today is hero).")

    if dry:
        log("DRY-RUN: would deploy index.html, archive/index.html, and the issue. Stopping.")
        sys.exit(0)

    # ── DEPLOY (free: GitHub file push) ──
    code, out = run(["bash", "deploy-api.sh",
                     f"auto-publish {date_str}: {issue.stem}",
                     "index.html", "archive/index.html", str(issue.relative_to(REPO))])
    if code != 0:
        log("DEPLOY FAILED."); log(out[-400:]); sys.exit(1)
    log(f"✓ PUBLISHED {issue.name} — live. (commit pushed)")
    sys.exit(0)

if __name__ == "__main__":
    main()
