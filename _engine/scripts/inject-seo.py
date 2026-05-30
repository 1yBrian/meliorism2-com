#!/usr/bin/env python3
"""
inject-seo.py — backfill SEO/AEO/GEO into Meliorism2.com issue pages.

For each archive/*.html issue (not index.html), idempotently injects into <head>:
  - meta description, canonical
  - Open Graph + Twitter card
  - Article JSON-LD (author=Brian Oney, publisher=Meliorist Group, isPartOf the series)
…and a fine-print backlink block (brianoney.com + melioristgroup.com) before </body>.

Idempotent via the <!-- m2-seo --> sentinel. Re-run any time (e.g. after new issues ship).
Run from repo root:  python3 _engine/scripts/inject-seo.py
"""
import re, json, html as ihtml, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://meliorism2.com"
SENTINEL = "<!-- m2-seo -->"

BACKLINK = (
    '\n  ' + SENTINEL + '\n'
    '  <div style="font-family:\'Courier Prime\',monospace;font-size:0.72rem;'
    'letter-spacing:0.04em;text-align:center;color:#8a8070;background:#1a1714;'
    'padding:18px 24px;line-height:1.7;">\n'
    '    Meliorism 2.0 is a research instrument and daily briefing published by\n'
    '    <a href="https://brianoney.com" style="color:#c8a87a;text-decoration:none;">Brian Oney</a> ·\n'
    '    <a href="https://melioristgroup.com" style="color:#c8a87a;text-decoration:none;">Meliorist Group</a>,\n'
    '    San Francisco.\n'
    '  </div>\n'
)

def title_of(htmltext):
    m = re.search(r"<title>(.*?)</title>", htmltext, re.S)
    raw = ihtml.unescape(m.group(1)).strip() if m else "Meliorism 2.0"
    # Drop "Meliorism2.com ·" and any "Issue NNN ·" prefixes -> human title
    parts = [p.strip() for p in raw.split("·")]
    issue_no = None
    title = parts[-1]
    for p in parts:
        mm = re.match(r"Issue\s+0*(\d+)", p, re.I)
        if mm: issue_no = mm.group(1)
    return title, issue_no, raw

def head_block(fname, title, issue_no, raw_title):
    base = os.path.basename(fname)
    canonical = f"{SITE}/archive/{base}"
    dm = re.match(r"(\d{4}-\d{2}-\d{2})", base)
    date = dm.group(1) if dm else None
    desc = (f"{title} — an issue of Meliorism 2.0, the daily research-grounded briefing "
            f"by Brian Oney (Meliorist Group) for trainers, coaches, and educators.")
    desc = desc[:300]
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "name": raw_title,
        "url": canonical,
        "mainEntityOfPage": canonical,
        "inLanguage": "en",
        "author": {"@type": "Person", "name": "Brian Oney", "url": "https://brianoney.com"},
        "publisher": {"@type": "Organization", "name": "Meliorist Group", "url": "https://melioristgroup.com"},
        "isPartOf": {"@type": "CreativeWorkSeries", "name": "Meliorism 2.0", "url": SITE},
    }
    if date: article["datePublished"] = date
    if issue_no: article["articleSection"] = f"Issue {issue_no}"
    j = "\n".join("  " + l for l in json.dumps(article, indent=2, ensure_ascii=False).splitlines())
    return (
        f'  {SENTINEL}\n'
        f'  <meta name="description" content="{ihtml.escape(desc, quote=True)}">\n'
        f'  <link rel="canonical" href="{canonical}">\n'
        f'  <meta property="og:type" content="article">\n'
        f'  <meta property="og:title" content="{ihtml.escape(title, quote=True)}">\n'
        f'  <meta property="og:description" content="{ihtml.escape(desc, quote=True)}">\n'
        f'  <meta property="og:url" content="{canonical}">\n'
        f'  <meta property="og:site_name" content="Meliorism 2.0">\n'
        f'  <meta name="twitter:card" content="summary">\n'
        f'  <script type="application/ld+json">\n{j}\n  </script>\n'
    )

def process(fname):
    t = open(fname).read()
    if SENTINEL in t:
        return "skip"
    title, issue_no, raw = title_of(t)
    # inject into head (before first </head>)
    if "</head>" in t:
        t = t.replace("</head>", head_block(fname, title, issue_no, raw) + "</head>", 1)
    # inject backlink before last </body>
    if "</body>" in t:
        idx = t.rfind("</body>")
        t = t[:idx] + BACKLINK + t[idx:]
    open(fname, "w").write(t)
    return "done"

if __name__ == "__main__":
    issues = sorted(f for f in glob.glob(os.path.join(ROOT, "archive", "*.html"))
                    if os.path.basename(f) != "index.html")
    done = skip = 0
    for f in issues:
        r = process(f)
        done += (r == "done"); skip += (r == "skip")
    print(f"issues processed: {len(issues)} | injected: {done} | already-had-sentinel: {skip}")
