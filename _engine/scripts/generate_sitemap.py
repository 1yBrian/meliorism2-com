#!/usr/bin/env python3
"""generate_sitemap.py — Build sitemap.xml at repo root.

Includes: homepage, about, weather, topics/, archive issues.
lastmod = file mtime (UTC) in ISO-8601.

Usage:
    python3 _engine/scripts/generate_sitemap.py
"""
import pathlib, datetime, sys

BASE = "https://meliorism2.com"
REPO = pathlib.Path(__file__).resolve().parents[2]

ROOT_PAGES = ["index.html", "about.html", "weather.html", "founding.html", "calendar.html"]
TOPIC_DIR = "topics"
ARCHIVE_DIR = "archive"

def url_for(rel_path: str) -> str:
    # Extensionless canonical: drop .html for top-level pages, keep for archive (matches current canonicals)
    if rel_path == "index.html":
        return f"{BASE}/"
    if rel_path.startswith(f"{TOPIC_DIR}/") and rel_path.endswith(".html"):
        return f"{BASE}/{rel_path}"
    return f"{BASE}/{rel_path}"

def lastmod_for(p: pathlib.Path) -> str:
    return datetime.datetime.utcfromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%dT%H:%M:%SZ")

def emit(url, lastmod, priority="0.7", changefreq="weekly"):
    return (
        "  <url>\n"
        f"    <loc>{url}</loc>\n"
        f"    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>{changefreq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        "  </url>\n"
    )

def main():
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    # Root pages
    for name in ROOT_PAGES:
        p = REPO / name
        if not p.exists(): continue
        priority = "1.0" if name == "index.html" else "0.8"
        changefreq = "daily" if name == "index.html" else "weekly"
        out.append(emit(url_for(name), lastmod_for(p), priority, changefreq))
    # Topic hubs
    for p in sorted((REPO / TOPIC_DIR).glob("*.html")):
        out.append(emit(url_for(f"{TOPIC_DIR}/{p.name}"), lastmod_for(p), "0.7", "weekly"))
    # Archive issues
    for p in sorted((REPO / ARCHIVE_DIR).glob("*.html")):
        if not p.stem[0].isdigit(): continue  # skip index.html, library-concept.html, etc.
        out.append(emit(url_for(f"{ARCHIVE_DIR}/{p.name}"), lastmod_for(p), "0.6", "monthly"))
    out.append("</urlset>\n")
    target = REPO / "sitemap.xml"
    target.write_text("\n".join(out))
    print(f"✓ wrote {target} ({len(out)-3} URLs)")

if __name__ == "__main__":
    main()
