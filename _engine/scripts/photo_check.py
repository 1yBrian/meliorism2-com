#!/usr/bin/env python3
"""photo_check.py — Unsplash attribution gate.

For every Unsplash photo referenced in the file (image or background), require:
- A visible attribution line "Photo by NAME on Unsplash"
- Two clickable links: photographer profile and unsplash.com
- UTM params on at least one Unsplash link (?utm_source=meliorism2 or similar)

Per PHOTO-PROTOCOL.md — ironclad.

Usage:
    python3 photo_check.py archive/2026-05-30-*.html
"""
import re, sys, pathlib

UTM_REQUIRED = "utm_source"
UNSPLASH_HOST_PATTERN = re.compile(r'unsplash\.com|images\.unsplash\.com', re.IGNORECASE)
ATTRIBUTION_PATTERN = re.compile(r'Photo\s+by\s+[^<\n]+?\s+on\s+(?:<a[^>]+>)?Unsplash', re.IGNORECASE)

def main():
    if len(sys.argv) < 2:
        print("Usage: photo_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    has_unsplash_asset = bool(UNSPLASH_HOST_PATTERN.search(html))
    # Also detect locally-downloaded Unsplash images by filename hint or alt text
    has_unsplash_hint = bool(re.search(r'unsplash', html, re.IGNORECASE))

    if not (has_unsplash_asset or has_unsplash_hint):
        print(f"PASS: {path.name} no Unsplash content detected.")
        sys.exit(0)

    if not ATTRIBUTION_PATTERN.search(html):
        print(f"FAIL: {path.name} uses Unsplash content but no 'Photo by NAME on Unsplash' attribution found.")
        sys.exit(1)

    # Check for the two-link requirement
    unsplash_links = re.findall(r'<a[^>]+href="[^"]*unsplash\.com[^"]*"', html, re.IGNORECASE)
    if len(unsplash_links) < 2:
        print(f"FAIL: {path.name} attribution needs two unsplash.com links (photographer profile + unsplash.com).")
        sys.exit(1)

    # At least one Unsplash link must carry UTM
    if not any(UTM_REQUIRED in link for link in unsplash_links):
        print(f"FAIL: {path.name} Unsplash links missing utm_source — required by Unsplash developer terms.")
        sys.exit(1)

    print(f"PASS: {path.name} Unsplash attribution complete.")
    sys.exit(0)

if __name__ == "__main__":
    main()
