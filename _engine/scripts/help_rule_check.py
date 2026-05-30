#!/usr/bin/env python3
"""help_rule_check.py — The Help Rule (Brian's lexicon law).

From CLAUDE.md: "Never use 'help' anywhere unless inside a quoted source."
Precise verbs to prefer: support, build, deliver, advise, execute, act, solve.

Usage:
    python3 help_rule_check.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

# Strip quoted content (single, double, smart quotes, blockquotes) before scanning
def strip_quoted(html: str) -> str:
    # Strip blockquote sections
    out = re.sub(r"<blockquote[^>]*>.*?</blockquote>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # Strip citations block (often contains "help" in source titles)
    out = re.sub(r'<(?:section|aside|div)[^>]*(?:id="citations"|class="[^"]*citations)[^>]*>.*?</(?:section|aside|div)>',
                 "", out, flags=re.DOTALL | re.IGNORECASE)
    # Strip text inside HTML comments
    out = re.sub(r"<!--.*?-->", "", out, flags=re.DOTALL)
    return out

HELP_RE = re.compile(r"\b(help|helps|helped|helping|helper|helpful|helpfully)\b", re.IGNORECASE)

def main():
    if len(sys.argv) < 2:
        print("Usage: help_rule_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()
    body = strip_quoted(html)

    matches = []
    for m in HELP_RE.finditer(body):
        ctx_start = max(0, m.start() - 40)
        ctx_end = m.end() + 40
        ctx = body[ctx_start:ctx_end].replace("\n", " ").strip()
        matches.append((m.group(0), ctx))

    if matches:
        print(f"FAIL: {path.name} violates Help Rule ({len(matches)} instance(s)):")
        for word, ctx in matches[:10]:
            print(f"  '{word}' — …{ctx}…")
        print("  Prefer: support, build, deliver, advise, execute, act, solve.")
        sys.exit(1)
    print(f"PASS: {path.name} Help Rule respected.")
    sys.exit(0)

if __name__ == "__main__":
    main()
