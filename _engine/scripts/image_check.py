#!/usr/bin/env python3
"""image_check.py — Every image reference resolves to a real file.

Catches: CSS url('foo.jpg') or src="foo.jpg" pointing to a file that doesn't exist.
This is the "no broken hero" gate. Today's Provenance Document failed exactly this.

Usage:
    python3 image_check.py archive/2026-05-30-the-provenance-document.html
"""
import re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]

URL_RE = re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", re.IGNORECASE)
SRC_RE = re.compile(r"""(?:src|href)\s*=\s*['"]([^'"]+)['"]""", re.IGNORECASE)

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}

def is_image_ref(ref: str) -> bool:
    if ref.startswith(("data:", "http://", "https://", "mailto:", "tel:", "#", "javascript:")):
        return False
    ext = pathlib.Path(ref.split("?")[0].split("#")[0]).suffix.lower()
    return ext in IMAGE_EXTS

def resolve(file_path: pathlib.Path, ref: str) -> pathlib.Path:
    """Resolve ref relative to the HTML file, then absolute from repo root."""
    ref = ref.split("?")[0].split("#")[0]
    if ref.startswith("/"):
        return REPO / ref.lstrip("/")
    return (file_path.parent / ref).resolve()

def main():
    if len(sys.argv) < 2:
        print("Usage: image_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    refs = set()
    for m in URL_RE.finditer(html):
        if is_image_ref(m.group(1)): refs.add(m.group(1))
    for m in SRC_RE.finditer(html):
        if is_image_ref(m.group(1)): refs.add(m.group(1))

    if not refs:
        print(f"FAIL: {path.name} declares no images. Every issue needs a hero.")
        sys.exit(1)

    missing = []
    for ref in sorted(refs):
        resolved = resolve(path, ref)
        if not resolved.exists():
            missing.append((ref, str(resolved.relative_to(REPO)) if REPO in resolved.parents else str(resolved)))

    if missing:
        print(f"FAIL: {path.name} references {len(missing)} image(s) that don't exist:")
        for ref, resolved in missing:
            print(f"  '{ref}' → {resolved}")
        sys.exit(1)
    print(f"PASS: {path.name} all {len(refs)} image refs resolve.")
    sys.exit(0)

if __name__ == "__main__":
    main()
