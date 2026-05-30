#!/usr/bin/env python3
"""
exploratorium_check.py — the Signature Law's Layer-3 invariant (advisory).

THE TEST (Design Grammar System / Signature Law, Invariant 2):
  An interaction is valid only if the READER'S INPUT CHANGES THE SYSTEM she is inside.
  A slider that updates a number with no downstream effect, a toggle that reveals
  pre-written text, a quiz with a "correct" answer, or animation that plays regardless
  of input = DECORATION, not interaction.

HEURISTIC, advisory only — it never blocks deploy. It measures the *machinery* that
distinguishes system-changing interaction from decoration. Thresholds are calibrated
against the real archive (2026-05): the Annotated Estimate (the 9/9 exemplar) vs.
The Briefing (0/9, decoration). A low score demands a human confirm Invariant 2 by hand.

Measured discriminators (from the archive):
  STRONG (input changes downstream state):
    - input→recompute loop: an input source (oninput / input listener / .value reads)
      whose values flow into output writes (textContent / innerHTML)
    - branching on a reader value: if(...value/choice/prediction/rating/reading...)
    - persisted reader state: localStorage / sessionStorage
  DECORATION-only:
    - output writes (textContent/innerHTML) or class reveals with NO input source feeding them

Calibration (oninput | .value | branch-on-value | localStorage):
    annotated-estimate  6 | 31 | 8 | 0   -> STRONG (input loop + branching)
    barograph           1 |  2 | 2 | 0   -> STRONG (input loop + branching)
    hive-deliberates    0 |  0 | 0 | 2   -> STRONG (persistence)
    briefing            0 |  0 | 0 | 0   -> DECORATION
    23-minute-problem   0 |  0 | 0 | 0   -> DECORATION

Usage:
    python3 exploratorium_check.py archive/2026-05-30-the-provenance-document.html
"""
import re, sys, pathlib

def count(pattern, text):
    return len(re.findall(pattern, text, re.I))

def main():
    if len(sys.argv) < 2:
        print("Usage: exploratorium_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    # --- input sources (the reader puts something in) ---
    oninput   = count(r"oninput\s*=|addEventListener\(\s*['\"]input['\"]", html)
    onchange  = count(r"onchange\s*=|addEventListener\(\s*['\"]change['\"]", html)
    valreads  = count(r"\.value\b", html)
    input_source = oninput + onchange + (1 if valreads >= 2 else 0)

    # --- output sinks (the system writes back) ---
    out_writes = count(r"textContent\s*=|innerHTML\s*=", html)

    # --- the three STRONG signals ---
    input_loop = bool(input_source and out_writes and valreads >= 2)
    branch_on_value = count(
        r"if\s*\([^)]*\b(value|choice|prediction|selected|reading|rating|answer|input)\b", html) >= 1
    persisted = bool(re.search(r"\b(localStorage|sessionStorage)\.(set|get)Item", html))

    strong = []
    if input_loop:      strong.append(f"input→recompute loop ({oninput+onchange} input handlers, {valreads} value reads → {out_writes} output writes)")
    if branch_on_value: strong.append("branches downstream logic on a stored reader value")
    if persisted:       strong.append("persists reader state (localStorage/sessionStorage)")

    # --- decoration-only signals (present, but no input feeding them) ---
    reveal = count(r"classList\.(add|toggle|remove)\(\s*['\"](show|active|open|revealed|flip)", html)
    deco = []
    if not strong:
        if out_writes:
            deco.append(f"{out_writes} output write(s) with no reader input feeding them — static reveal")
        if reveal:
            deco.append("class-toggle reveals of pre-written content")
        if re.search(r"(setTimeout|setInterval|requestAnimationFrame|@keyframes)", html):
            deco.append("time-driven animation, no input dependency")

    print(f"Exploratorium reporter — {path.name}  (REPORT-ONLY · machinery, not meaning)")
    if strong:
        print("  Interactive machinery detected (necessary, NOT sufficient):")
        for s in strong: print(f"    · {s}")
    if deco:
        print("  Only static-reveal machinery detected (no reader-input source):")
        for s in deco: print(f"    · {s}")
    if not strong and not deco:
        print("  No interaction machinery detected at all.")

    # NO automated PASS/WARN verdict. Calibration against the real archive proved a regex
    # cannot separate stakes from vibe: the Annotated Estimate (9/9 exemplar) and the
    # 23-Minute Problem (2/9 decoration) are structurally indistinguishable to a scanner —
    # both reveal content on a handler; the difference is what the reveal MEANS. Invariant 2
    # is meaning-level. This script reports the machinery it sees and hands the verdict to a
    # human. It NEVER blocks and NEVER auto-passes — a false green here trains the team to
    # ignore the one test that matters most.
    print("\n  ── INVARIANT 2 IS A HUMAN CALL ──")
    print("  A scanner sees machinery, not meaning. Answer by hand before publish:")
    print("    1. Does the reader put something of her own in (a choice, a number, a position)?")
    print("    2. Would a DIFFERENT input produce a GENUINELY different experience?")
    print("    3. Or does every reader, whatever they do, end at the same pre-written place?")
    print("  If (3): it's decoration — vibe without stakes. Redesign so her input changes the world.")
    sys.exit(0)  # report-only: never blocks, never auto-passes

if __name__ == "__main__":
    main()
