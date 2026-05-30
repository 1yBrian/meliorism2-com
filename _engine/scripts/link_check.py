#!/usr/bin/env python3
"""link_check.py — Dead link gate.

HEAD every external href. Fail on 4xx/5xx. Skip mailto:, tel:, #anchors, javascript:.
Timeout per request: 8s. Concurrent: 8 workers.

Usage:
    python3 link_check.py archive/2026-05-30-*.html [--allow-redirect]
"""
import re, sys, pathlib, urllib.request, urllib.error, concurrent.futures, ssl

TIMEOUT = 8
WORKERS = 8
HREF_RE = re.compile(r'href="([^"]+)"', re.IGNORECASE)
SRC_RE  = re.compile(r'src="(https?://[^"]+)"', re.IGNORECASE)

def is_external(url: str) -> bool:
    if not url: return False
    if url.startswith(("mailto:", "tel:", "#", "javascript:", "data:")): return False
    return url.startswith(("http://", "https://"))

def check(url: str) -> tuple[str, int | str]:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Meliorism2-LinkCheck/1.0"})
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            return url, r.status
    except urllib.error.HTTPError as e:
        # Some hosts reject HEAD; retry with GET (range 0-0 to stay cheap)
        if e.code in (403, 405, 501):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Meliorism2-LinkCheck/1.0", "Range": "bytes=0-0"})
                with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                    return url, r.status
            except Exception as e2:
                return url, f"GET-{type(e2).__name__}"
        return url, e.code
    except Exception as e:
        return url, type(e).__name__

def main():
    if len(sys.argv) < 2:
        print("Usage: link_check.py <file.html>"); sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: {path} not found"); sys.exit(1)
    html = path.read_text()

    urls = set()
    for m in HREF_RE.finditer(html):
        if is_external(m.group(1)): urls.add(m.group(1))
    for m in SRC_RE.finditer(html):
        if is_external(m.group(1)): urls.add(m.group(1))

    if not urls:
        print(f"PASS: {path.name} no external links to check."); sys.exit(0)

    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for url, status in ex.map(check, urls):
            ok = isinstance(status, int) and status < 400
            if not ok:
                failures.append((url, status))

    if failures:
        print(f"FAIL: {path.name} has {len(failures)} broken link(s):")
        for u, s in failures: print(f"  {s} :: {u}")
        sys.exit(1)
    print(f"PASS: {path.name} all {len(urls)} external links OK.")
    sys.exit(0)

if __name__ == "__main__":
    main()
