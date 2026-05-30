#!/usr/bin/env python3
"""cta_check.py — Entry CTA standards.

Source: MELIORISM2-DIRECTIVE.md §2 + §11 Permanent Rules.

Banned: "READ →", "Read more", "Continue", "Click here", anything generic.
Required: contextual phrasing tied to the format ("Enter the room",
"Step inside", "Open the log", "Walk through the room", etc.)

Usage:
    python3 cta_check.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

BANNED_CTA_PATTERNS = [
    r'\bREAD\s*[→>\-]',
    r'\b(?:read\s+more|continue|click\s+here|learn\s+more|find\s+out\s+more)\b',
]

ENTRY_CTA_RE = re.compile(r'class="entry-enter"[^>]*>\s*([^<]+?)\s*<', re.IGNORECASE)
HERO_CTA_RE  = re.compile(r'class="hero-cta"[^>]*>\s*([^<]+?)\s*<', re.IGNORECASE)

def main():
    if len(sys.argv) < 2:
        print("Usage: cta_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    violations = []
    for m in ENTRY_CTA_RE.finditer(html):
        cta = m.group(1)
        for pat in BANNED_CTA_PATTERNS:
            if re.search(pat, cta, re.IGNORECASE):
                violations.append(f"entry CTA banned: '{cta}'")
    for m in HERO_CTA_RE.finditer(html):
        cta = m.group(1)
        for pat in BANNED_CTA_PATTERNS:
            if re.search(pat, cta, re.IGNORECASE):
                violations.append(f"hero CTA banned: '{cta}'")

    if violations:
        print(f"FAIL: {path.name} CTA violations:")
        for v in violations: print(f"  {v}")
        print("  Use contextual CTAs tied to the format ('Enter the room', 'Open the log', 'Walk the chart').")
        sys.exit(1)
    print(f"PASS: {path.name} CTAs contextual.")
    sys.exit(0)

if __name__ == "__main__":
    main()
