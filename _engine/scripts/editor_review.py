#!/usr/bin/env python3
"""editor_review.py — The editor function. Runs every deterministic gate against an issue.

Replaces the previous "list of linters" with a real editorial review:
prints results grouped by tier, names every law violated by source document,
exits 0 (ready to ship), 1 (blocked — at least one HARD gate failed),
or 2 (regression — every HARD gate passed but at least one SOFT gate warned).

Gate tiers:

  HARD GATES — failure blocks publish.
    image_check        — every image ref resolves
    citation_check     — closing citations block + footnote integrity
    ledger_check       — DESIGN-LEDGER row complete + uniqueness
    typography_floor   — no font below 0.8rem
    palette_check      — dark backgrounds declared + justified
    truth_lint         — banned promises / over-claims / future studies
    unsplash_url_check — no hotlinked Unsplash URLs
    photo_check        — if Unsplash used, attribution complete
    help_rule_check    — Help Rule

  SOFT GATES — failure warns, does not block.
    cta_check          — contextual entry CTA
    voice_drift_check  — patterns from LEARNING-LOG
    section_title_score — non-blog title scoring
    link_check         — external links (skipped if --skip-links)

Usage:
    python3 editor_review.py archive/2026-05-30-*.html
    python3 editor_review.py archive/2026-05-30-*.html --skip-links

Source documents this enforces:
    _engine/PUBLICATION-SOUL.md      (the three non-negotiables, the architect frame)
    _engine/DESIGN-ENGINE.md         (Earned Advance, Generative Layers, typography floor)
    _engine/DESIGN-LEDGER.md         (uniqueness across 365 issues)
    _engine/LEARNING-LOG.md          (Flagged design notes + Voice Drift Watch)
    08 - The Intermodal Hub/.../MELIORISM2-DIRECTIVE.md  (governing publication doc)
    08 - The Intermodal Hub/.../PHOTO-PROTOCOL.md        (image standards)
"""
import sys, subprocess, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = REPO / "_engine" / "scripts"

HARD_GATES = [
    ("image_check.py",         "Hero image resolves",       "PHOTO-PROTOCOL"),
    ("citation_check.py",      "Citations block + integrity","PUBLICATION-SOUL"),
    ("ledger_check.py",        "Design Ledger uniqueness",  "DESIGN-LEDGER"),
    ("typography_floor.py",    "Typography floor ≥0.8rem",  "DESIGN-ENGINE §HARD TYPOGRAPHY FLOOR"),
    ("palette_check.py",       "Palette earned",            "LEARNING-LOG (Black-default flagged)"),
    ("truth_lint.py",          "Truth (deterministic)",     "CLAUDE.md Recurring Issues"),
    ("unsplash_url_check.py",  "No hotlinked Unsplash",     "PHOTO-PROTOCOL Rule 2"),
    ("photo_check.py",         "Unsplash attribution",      "PHOTO-PROTOCOL Rule 1"),
    ("help_rule_check.py",     "Help Rule",                 "CLAUDE.md Lexicon"),
]

SOFT_GATES = [
    ("cta_check.py",           "Contextual entry CTA",      "MELIORISM2-DIRECTIVE §2"),
    ("voice_drift_check.py",   "Voice drift",               "LEARNING-LOG §Voice Drift Watch"),
    ("section_title_score.py", "Non-blog title scoring",    "MELIORISM2-DIRECTIVE §15"),
    ("link_check.py",          "External links",            "L5 hygiene"),
]

# REPORT-ONLY tools — run, print, but produce NO pass/fail verdict. These cover
# meaning-level invariants no scanner can judge (calibration proved a regex mislabels
# the exemplar). The verdict is the editor's, reading against the Signature Law checklist.
REPORTERS = [
    ("exploratorium_check.py", "Exploratorium (Invariant 2) — HUMAN CALL", "Signature Law"),
]

COLORS = {"pass": "\033[32m", "warn": "\033[33m", "fail": "\033[31m", "off": "\033[0m"}

def run(script: str, target: pathlib.Path) -> tuple[int, str]:
    path = SCRIPTS / script
    if not path.exists():
        return -1, f"  (script missing: {script})"
    r = subprocess.run(["python3", str(path), str(target)], capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).rstrip()

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print("Usage: editor_review.py <archive/file.html> [--skip-links]"); sys.exit(2)
    target = pathlib.Path(args[0])
    if not target.exists():
        print(f"FAIL: {target} not found"); sys.exit(1)

    print(f"\n══════ EDITORIAL REVIEW ══════")
    print(f"  Issue: {target.name}")
    print(f"  Source: {target.resolve()}\n")

    hard_failed, soft_warned = [], []

    print("─── HARD GATES (block on fail) ───")
    for script, label, source in HARD_GATES:
        code, out = run(script, target)
        if code == 0:
            print(f"  ✅ {label:30} [{source}]")
        else:
            hard_failed.append((label, source, out))
            print(f"  ❌ {label:30} [{source}]")
            for line in out.splitlines():
                print(f"      {line}")

    print("\n─── SOFT GATES (warn on fail) ───")
    for script, label, source in SOFT_GATES:
        if script == "link_check.py" and "--skip-links" in flags:
            print(f"  ⊘  {label:30} skipped"); continue
        code, out = run(script, target)
        if code == 0:
            print(f"  ✅ {label:30} [{source}]")
        else:
            soft_warned.append((label, source, out))
            print(f"  ⚠️  {label:30} [{source}]")
            for line in out.splitlines():
                print(f"      {line}")

    print("\n─── REPORTERS (no verdict — human reads these) ───")
    for script, label, source in REPORTERS:
        _, out = run(script, target)
        print(f"  📋 {label:42} [{source}]")
        for line in out.splitlines():
            print(f"      {line}")

    print()
    if hard_failed:
        print(f"VERDICT: BLOCKED — {len(hard_failed)} hard gate(s) failed. Issue does not ship.")
        print("  NOTE: a green pipeline is necessary, not sufficient — the meaning-level")
        print("  invariants (physics derived, removal-not-installation, 'how did they know')")
        print("  are confirmed by the editor, not the gates. Read the reporters above.")
        sys.exit(1)
    if soft_warned:
        print(f"VERDICT: REGRESSION — all hard gates pass; {len(soft_warned)} soft gate(s) warn.")
        print("        Ship is technically allowed; rebuild recommended.")
        sys.exit(2)
    print("VERDICT: READY — every automated gate passed.")
    print("  Final call is the editor's: read the reporters above and confirm the meaning-level")
    print("  invariants (Exploratorium, physics-derived, removal-not-installation, 'how did they know').")
    sys.exit(0)

if __name__ == "__main__":
    main()
