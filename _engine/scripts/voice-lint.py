#!/usr/bin/env python3
"""
voice-lint.py — deterministic, FREE pre-check for the Meliorism2 voice rules.

Flags soft-overclaim patterns (unverified superlatives, absolutes, hype, guaranteed
outcomes) in issue prose — the same SOFT_OVERCLAIMS class the (paid, LLM) truth agent
catches, but instantly and for free. Run it before staging to clean prose up front.

Usage:
  python3 _engine/scripts/voice-lint.py                 # lint all archive issues
  python3 _engine/scripts/voice-lint.py archive/X.html  # lint one file
  python3 _engine/scripts/voice-lint.py --strict        # exit 1 if any findings (for pipeline gating)

Detect-only by design — it never rewrites your prose. It tells you where to soften.
"""
import sys, re, glob, os, html as html_lib

# High-precision only: patterns that are almost always an overclaim when stated as fact.
# (Bare "every/always/transforms" were dropped — too many legitimate uses to be useful.)
PATTERNS = [
    ("superlative",   r"\bthe (?:most|single most|only|furthest)\b"),
    ("superlative",   r"\bmost (?:important|replicated|expensive|powerful|dangerous|useful|forwarded|accurate|read)\b"),
    ("superlative",   r"\blandmark\b|\bdefinitive(?:ly)?\b|\bunparalleled\b"),
    ("hype",          r"\bchanges? everything\b|\bunlike anything\b|\bgame-?chang\w*|\brevolutionary\b"),
    ("guaranteed",    r"\bguarantee(?:d|s)?\b|\bby day \d+\b|\byou(?:'ll| will) (?:have|get|gain)\b|\bin \d+ days you\b"),
    ("absolute",      r"\bfull stop\b|\bevery single\b|\bno exception"),
    ("false-certain", r"\bclose(?:s)? the case\b|\bproven to\b"),
]
COMPILED = [(label, re.compile(rx, re.I)) for label, rx in PATTERNS]

def extract_text(h):
    t = re.sub(r'<script[^>]*>.*?</script>', ' ', h, flags=re.DOTALL)
    t = re.sub(r'<style[^>]*>.*?</style>', ' ', t, flags=re.DOTALL)
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html_lib.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

def lint(path):
    text = extract_text(open(path).read())
    hits = []
    for label, rx in COMPILED:
        for m in rx.finditer(text):
            s = max(0, m.start() - 45); e = min(len(text), m.end() + 45)
            hits.append((label, m.group(0), text[s:e].strip()))
    return hits

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    strict = '--strict' in sys.argv
    files = args if args else sorted(glob.glob(os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "archive", "[0-9]*.html")))
    total = 0; flagged_files = 0
    for f in files:
        hits = lint(f)
        if not hits:
            continue
        flagged_files += 1; total += len(hits)
        print(f"\n{os.path.basename(f)}  ({len(hits)})")
        for label, phrase, ctx in hits:
            print(f"  [{label:13}] “{phrase}”  …{ctx}…")
    print(f"\n{'─'*60}\nvoice-lint: {total} flags across {flagged_files}/{len(files)} files")
    if strict and total:
        sys.exit(1)

if __name__ == '__main__':
    main()
