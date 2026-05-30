#!/usr/bin/env python3
"""voice_drift_check.py — Watch for patterns flagged in LEARNING-LOG.md Voice Drift section.

Reads `_engine/LEARNING-LOG.md` and extracts every row under "Voice Drift Watch."
Each row has a Pattern + Risk + Instruction. The script applies the instruction
heuristically (typically: at most N occurrences, or banned register).

Currently enforced:
  - "The practitioner who X is doing Y" — at most 1 per issue
  - "This is not X. This is Y." — at most 1 per issue
  - Decision-maker register ("here's what to do") — flagged
  - Watcher register ("here's what to notice") — flagged

Usage:
    python3 voice_drift_check.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
LOG = REPO / "_engine" / "LEARNING-LOG.md"

CHECKS = [
    ("practitioner_who_x", r"\bthe\s+practitioner\s+who\s+\w+\s+is\s+\w+ing\b", 1,
     "'The practitioner who X is doing Y' pattern — max 1 per issue (Voice Drift Watch)."),
    ("this_is_not_x", r"\bthis\s+is\s+not\s+[A-Z]?\w+[\.\,]\s+this\s+is\s+\w+", 1,
     "'This is not X. This is Y.' pattern — max 1 per issue (reserve for moment of highest impact)."),
    ("decision_maker_register", r"\bhere(?:'s|\s+is)\s+what\s+to\s+do\b", 0,
     "Decision-maker register — wrong audience position. The reader is the architect, not the decision-maker."),
    ("watcher_register", r"\bhere(?:'s|\s+is)\s+what\s+to\s+(?:notice|watch\s+for|look\s+for)\b", 0,
     "Watcher register — adjacent but still wrong. The full job is building conditions, not just observing."),
]

def main():
    if len(sys.argv) < 2:
        print("Usage: voice_drift_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()
    # Strip HTML tags to scan prose only
    prose = re.sub(r"<[^>]+>", " ", html)

    violations = []
    for key, pat, max_count, msg in CHECKS:
        hits = re.findall(pat, prose, re.IGNORECASE)
        if len(hits) > max_count:
            violations.append(f"  [{key}] {len(hits)} matches (max {max_count}) — {msg}")

    if violations:
        print(f"FAIL: {path.name} voice drift detected:")
        for v in violations: print(v)
        sys.exit(1)
    print(f"PASS: {path.name} voice drift watch clean.")
    sys.exit(0)

if __name__ == "__main__":
    main()
