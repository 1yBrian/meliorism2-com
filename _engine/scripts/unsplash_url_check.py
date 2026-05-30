#!/usr/bin/env python3
"""unsplash_url_check.py — No raw Unsplash CDN URLs.

PHOTO-PROTOCOL Rule 2: "Local files only. Never embed a raw Unsplash CDN URL."

Hotlinking breaks when Unsplash changes their CDN URL structure and violates
their developer terms.

Usage:
    python3 unsplash_url_check.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

# Only the CDN hosts are forbidden. unsplash.com/@user and unsplash.com?utm... are
# the REQUIRED attribution links and must not be flagged.
UNSPLASH_CDN_RE = re.compile(r'(?:src|href)\s*=\s*["\']https?://(?:images|source|plus)\.unsplash\.com/', re.IGNORECASE)
UNSPLASH_BG_RE  = re.compile(r'url\(\s*["\']?https?://(?:images|source|plus)\.unsplash\.com/', re.IGNORECASE)

def main():
    if len(sys.argv) < 2:
        print("Usage: unsplash_url_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    bad = []
    for m in UNSPLASH_CDN_RE.finditer(html):
        bad.append(("src/href", html[m.start():m.start()+120].replace("\n", " ")))
    for m in UNSPLASH_BG_RE.finditer(html):
        bad.append(("background url()", html[m.start():m.start()+120].replace("\n", " ")))

    if bad:
        print(f"FAIL: {path.name} has {len(bad)} hotlinked Unsplash URL(s) — must be downloaded locally.")
        for kind, snippet in bad[:5]:
            print(f"  [{kind}] {snippet}…")
        sys.exit(1)
    print(f"PASS: {path.name} no Unsplash CDN hotlinks.")
    sys.exit(0)

if __name__ == "__main__":
    main()
