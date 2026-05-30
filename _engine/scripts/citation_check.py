#!/usr/bin/env python3
"""citation_check.py — Citations gate.

Pass: file has a citations block AND every [N] footnote marker resolves to an entry.
Fail: missing block, empty block, or orphan footnote.

Usage:
    python3 citation_check.py archive/2026-05-30-the-provenance-document.html
Exit 0 = pass, 1 = fail.
"""
import re, sys, pathlib

CITATIONS_PATTERNS = [
    r'<section[^>]*id="citations"',
    r'<section[^>]*class="[^"]*citations',
    r'<div[^>]*id="citations"',
    r'<aside[^>]*class="[^"]*citations',
    r'<h2[^>]*>\s*(?:Citations|References|Sources|Footnotes)\s*</h2>',
]

def find_citations_block(html: str) -> str | None:
    """Return the citations block contents, or None if not found."""
    for pat in CITATIONS_PATTERNS:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            # Grab from match start to closing tag (best-effort: closing section/div/aside)
            tail = html[m.start():]
            close = re.search(r'</(?:section|div|aside|article)>', tail)
            if close:
                return tail[:close.end()]
            return tail
    return None

def extract_footnote_markers(html: str) -> list[str]:
    """Find inline [N] or <sup>N</sup> footnote markers in the body (excluding citations block)."""
    block = find_citations_block(html)
    if block:
        body = html.replace(block, "")
    else:
        body = html
    markers = re.findall(r'\[(\d+)\]', body)
    markers += re.findall(r'<sup[^>]*>(\d+)</sup>', body)
    return sorted(set(markers), key=int)

def extract_citation_ids(block: str) -> list[str]:
    """Find numbered entries inside the citations block."""
    ids = re.findall(r'(?:^|\n)\s*(?:<li[^>]*>)?\s*\[?(\d+)\]?[\.\)]?\s', block)
    ids += re.findall(r'id="cite-(\d+)"', block)
    ids += re.findall(r'id="ref-(\d+)"', block)
    return sorted(set(ids), key=int)

def main():
    if len(sys.argv) < 2:
        print("Usage: citation_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    block = find_citations_block(html)
    markers = extract_footnote_markers(html)
    if not block:
        if markers:
            print(f"FAIL: {path.name} has footnote markers {markers} but no citations block.")
            sys.exit(1)
        print(f"FAIL: {path.name} has no citations block. Every issue ships with sources.")
        sys.exit(1)

    ids = extract_citation_ids(block)
    if not ids and not markers:
        print(f"FAIL: {path.name} citations block is empty.")
        sys.exit(1)

    orphans = [m for m in markers if m not in ids]
    if orphans:
        print(f"FAIL: {path.name} has orphan footnote markers {orphans} (no matching entry).")
        sys.exit(1)

    print(f"PASS: {path.name} citations OK ({len(ids)} entries, {len(markers)} markers).")
    sys.exit(0)

if __name__ == "__main__":
    main()
