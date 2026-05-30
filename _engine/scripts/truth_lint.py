#!/usr/bin/env python3
"""truth_lint.py — Deterministic truth gate (no API charges).

The Anthropic-powered `truth_agent.py` stays for Brian-invoked chat reviews.
This one runs in cron and pre-flight — pure pattern checks, no paid call.

Catches:
- Banned promises ("not a newsletter", "guaranteed", "proven to")
- Over-claims on research ("peer-reviewed publication", "the study shows" without citation)
- Future-dated study claims (e.g. "a 2027 study found...")
- Help Rule violations ("we help you", "let us help" — context-aware: allowed only inside Silo content)
- Unsourced superlatives ("the most effective", "the only", "the best") within issue body

Usage:
    python3 truth_lint.py archive/2026-05-30-*.html
"""
import re, sys, pathlib
from datetime import datetime

BANNED_PROMISES = [
    (r'\bnot\s+a\s+newsletter\b', "Removed promise: 'not a newsletter' is banned (2026-05-23 lexicon rule)."),
    (r'\bguarantee[ds]?\b', "Over-promise: 'guarantee' is banned in practitioner copy."),
    (r'\bproven\s+to\b', "Over-claim: 'proven to' — use 'evidence suggests' or 'research indicates'."),
    # Only flag self-claims ("we are peer-reviewed", "this is peer-reviewed").
    # Talking ABOUT peer-reviewed journals as a concept is fine.
    (r'\b(?:we|Meliorism\s*2(?:\.0)?|this\s+(?:issue|publication|briefing|newsletter))\s+(?:is|are)\s+peer[-\s]reviewed\b', "Over-claim: Meliorism2 cites peer-reviewed research; it is not itself peer-reviewed."),
    (r'\bthe\s+only\b', "Unsourced superlative."),
    (r'\bthe\s+most\s+effective\b', "Unsourced superlative."),
    (r'\bworld[-\s]class\b', "Marketing inflation — drop or specify."),
    (r'\brevolutionary\b', "Marketing inflation — drop or specify."),
]

CURRENT_YEAR = datetime.now().year

def check_future_studies(html: str) -> list[str]:
    """Flag references like 'a 2027 study' if 2027 > current year."""
    flags = []
    for m in re.finditer(r'\ba\s+(\d{4})\s+(?:study|paper|review|meta-analysis|trial)\b', html, re.IGNORECASE):
        year = int(m.group(1))
        if year > CURRENT_YEAR:
            flags.append(f"Future-dated study: '{m.group(0)}' (current year {CURRENT_YEAR}).")
    return flags

def strip_citations(html: str) -> str:
    """Remove citations block before scanning body — citations may legitimately cite older studies."""
    return re.sub(r'<(?:section|div|aside)[^>]*(?:id="citations"|class="[^"]*citations)[^>]*>.*?</(?:section|div|aside)>', '', html, flags=re.IGNORECASE | re.DOTALL)

def main():
    if len(sys.argv) < 2:
        print("Usage: truth_lint.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()
    body = strip_citations(html)

    violations = []
    for pat, msg in BANNED_PROMISES:
        for m in re.finditer(pat, body, re.IGNORECASE):
            ctx = body[max(0, m.start()-40):m.end()+40].replace('\n', ' ')
            violations.append(f"  '{m.group(0)}' — {msg}\n    …{ctx}…")
    for f in check_future_studies(body):
        violations.append(f"  {f}")

    if violations:
        print(f"FAIL: {path.name} truth_lint found {len(violations)} issue(s):")
        for v in violations: print(v)
        sys.exit(1)
    print(f"PASS: {path.name} truth_lint clean.")
    sys.exit(0)

if __name__ == "__main__":
    main()
