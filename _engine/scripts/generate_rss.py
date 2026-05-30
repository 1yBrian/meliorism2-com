#!/usr/bin/env python3
"""generate_rss.py — Build feed.xml (RSS 2.0) at repo root.

Reads every issue in archive/, sorts by date desc, emits the 30 most recent.
Pulls title/dimension/concept from <!-- meliorism2:* --> metadata.

Usage:
    python3 _engine/scripts/generate_rss.py
"""
import re, pathlib, datetime, html as html_mod, email.utils as eut

BASE = "https://meliorism2.com"
REPO = pathlib.Path(__file__).resolve().parents[2]
MAX_ITEMS = 30

def get_meta(content: str, key: str) -> str | None:
    m = re.search(rf"<!-- meliorism2:{re.escape(key)}: (.+?) -->", content)
    return m.group(1).strip() if m else None

def get_concept(content: str) -> str:
    c = get_meta(content, "concept")
    if c: return c
    m = re.search(r'class="entry-sub"[^>]*>\s*([^<]+)\s*<', content)
    return m.group(1).strip() if m else ""

def rfc822(date_str: str) -> str:
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").replace(hour=11)
        return eut.format_datetime(dt.replace(tzinfo=datetime.timezone.utc))
    except Exception:
        return eut.format_datetime(datetime.datetime.now(datetime.timezone.utc))

def main():
    issues = []
    for p in sorted((REPO / "archive").glob("*.html"), reverse=True):
        if not re.match(r"\d{4}-\d{2}-\d{2}-.+\.html$", p.name): continue
        content = p.read_text()
        date = p.name[:10]
        slug = get_meta(content, "slug") or p.stem[11:]
        title = get_meta(content, "title") or " ".join(w.capitalize() for w in slug.split("-"))
        dimension = get_meta(content, "dimension") or ""
        concept = get_concept(content)
        url = f"{BASE}/archive/{p.name}"
        issues.append((date, title, dimension, concept, url, slug))
        if len(issues) >= MAX_ITEMS: break

    if not issues:
        print("No issues found."); return

    items = []
    for date, title, dimension, concept, url, slug in issues:
        items.append(
            "    <item>\n"
            f"      <title>{html_mod.escape(title)}</title>\n"
            f"      <link>{url}</link>\n"
            f"      <guid isPermaLink=\"true\">{url}</guid>\n"
            f"      <pubDate>{rfc822(date)}</pubDate>\n"
            f"      <category>{html_mod.escape(dimension)}</category>\n"
            f"      <description>{html_mod.escape(concept)}</description>\n"
            "    </item>"
        )

    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        '  <channel>\n'
        '    <title>Meliorism 2.0</title>\n'
        f'    <link>{BASE}/</link>\n'
        f'    <atom:link href="{BASE}/feed.xml" rel="self" type="application/rss+xml" />\n'
        '    <description>Daily, research-grounded briefings for trainers, coaches, and educators. By Brian Oney (Meliorist Group).</description>\n'
        '    <language>en-us</language>\n'
        f'    <lastBuildDate>{eut.format_datetime(datetime.datetime.now(datetime.timezone.utc))}</lastBuildDate>\n'
        + "\n".join(items) + "\n"
        '  </channel>\n'
        '</rss>\n'
    )

    target = REPO / "feed.xml"
    target.write_text(rss)
    print(f"✓ wrote {target} ({len(issues)} items)")

if __name__ == "__main__":
    main()
