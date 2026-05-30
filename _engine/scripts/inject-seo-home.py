#!/usr/bin/env python3
"""
inject-seo-home.py — SEO/AEO/GEO for Meliorism2.com homepage + archive index.

Homepage (index.html):
  - meta description, canonical, Open Graph/Twitter
  - JSON-LD @graph: WebSite + Organization (Meliorist Group / Brian Oney) + Blog series
  - a visible "Recent issues" list (latest 6) so issues are human- AND crawler-visible
  - footer backlinks to brianoney.com + melioristgroup.com

Archive index (archive/index.html):
  - meta description, canonical, Open Graph
  - CollectionPage + ItemList enumerating ALL issues as static JSON-LD
    (the card grid is JS-rendered, so this is what makes issues visible to AI/search)
  - footer backlinks

Idempotent via <!-- m2-seo-page -->. Run from repo root: python3 _engine/scripts/inject-seo-home.py
"""
import re, json, html as ihtml, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://meliorism2.com"
S = "<!-- m2-seo-page -->"

def issues():
    out = []
    for f in glob.glob(os.path.join(ROOT, "archive", "*.html")):
        b = os.path.basename(f)
        if b == "index.html":
            continue
        h = open(f).read()
        m = re.search(r"<title>(.*?)</title>", h, re.S)
        raw = ihtml.unescape(m.group(1)).strip() if m else b
        title = raw.split("·")[-1].strip()
        dm = re.match(r"(\d{4}-\d{2}-\d{2})", b)
        out.append({"title": title, "date": dm.group(1) if dm else "", "url": f"{SITE}/archive/{b}"})
    out.sort(key=lambda x: x["date"], reverse=True)
    return out

def home_head(items):
    desc = ("Meliorism 2.0 is a daily, research-grounded briefing by Brian Oney (Meliorist Group) "
            "for trainers, coaches, and educators navigating an AI-shaped economy. Each issue names "
            "one obstacle getting in your clients' way and gives you language for the room.")
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "name": "Meliorism 2.0", "url": SITE + "/",
         "description": desc,
         "publisher": {"@type": "Organization", "name": "Meliorist Group", "url": "https://melioristgroup.com"}},
        {"@type": "Organization", "name": "Meliorist Group", "url": "https://melioristgroup.com",
         "description": "A research and applied philosophy practice in San Francisco, founder Brian Oney.",
         "founder": {"@type": "Person", "name": "Brian Oney", "url": "https://brianoney.com"},
         "sameAs": ["https://brianoney.com", "https://melioristgroup.com"]},
        {"@type": "Blog", "name": "Meliorism 2.0", "url": SITE + "/",
         "description": desc,
         "author": {"@type": "Person", "name": "Brian Oney", "url": "https://brianoney.com"},
         "publisher": {"@type": "Organization", "name": "Meliorist Group", "url": "https://melioristgroup.com"}},
    ]}
    j = "\n".join("  " + l for l in json.dumps(graph, indent=2, ensure_ascii=False).splitlines())
    return (
        f'  {S}\n'
        f'  <meta name="description" content="{ihtml.escape(desc, quote=True)}">\n'
        f'  <link rel="canonical" href="{SITE}/">\n'
        f'  <meta property="og:type" content="website">\n'
        f'  <meta property="og:title" content="Meliorism 2.0 — Daily briefings for practitioners">\n'
        f'  <meta property="og:description" content="{ihtml.escape(desc, quote=True)}">\n'
        f'  <meta property="og:url" content="{SITE}/">\n'
        f'  <meta property="og:site_name" content="Meliorism 2.0">\n'
        f'  <meta name="twitter:card" content="summary">\n'
        f'  <script type="application/ld+json">\n{j}\n  </script>\n'
    )

def recent_section(items):
    rows = "\n".join(
        f'      <a class="row" href="{it["url"]}">'
        f'<span class="d">{it["date"]}</span>'
        f'<span class="t">{ihtml.escape(it["title"])}</span></a>'
        for it in items[:6])
    return (
        f'  {S}\n'
        '  <style>\n'
        '    .m2-recent{padding:64px 80px;border-bottom:1px solid #d8cfc4;display:grid;'
        'grid-template-columns:280px 1fr;gap:64px;align-items:start;}\n'
        '    .m2-recent .lbl{font-family:\'Courier Prime\',monospace;font-size:0.72rem;letter-spacing:0.16em;'
        'text-transform:uppercase;color:var(--text-muted);padding-top:6px;}\n'
        '    .m2-recent .list{max-width:720px;}\n'
        '    .m2-recent a.row{display:block;padding:16px 0;border-bottom:1px solid #d8cfc4;text-decoration:none;}\n'
        '    .m2-recent a.row .d{font-family:\'Courier Prime\',monospace;font-size:0.72rem;color:var(--text-muted);letter-spacing:0.08em;}\n'
        '    .m2-recent a.row .t{font-size:1.1rem;font-weight:600;color:var(--text);display:block;margin-top:4px;}\n'
        '    .m2-recent a.more{display:inline-block;margin-top:24px;font-family:\'Courier Prime\',monospace;'
        'font-size:0.82rem;letter-spacing:0.1em;color:var(--text-muted);text-decoration:none;text-transform:uppercase;'
        'border-bottom:1px solid #c0b8b0;padding-bottom:2px;}\n'
        '    @media(max-width:900px){.m2-recent{grid-template-columns:1fr;padding:48px 32px;gap:24px;}}\n'
        '  </style>\n'
        '  <section class="m2-recent">\n'
        '    <div class="lbl">Recent issues</div>\n'
        '    <div class="list">\n'
        f'{rows}\n'
        '      <a class="more" href="/archive/">Browse the full library →</a>\n'
        '    </div>\n'
        '  </section>\n\n'
    )

def archive_head(items):
    desc = ("The Practitioner's Library — every issue of Meliorism 2.0, the daily research-grounded "
            "briefing by Brian Oney (Meliorist Group) for trainers, coaches, and educators.")
    item_list = {"@context": "https://schema.org", "@type": "CollectionPage",
        "name": "The Practitioner's Library — Meliorism 2.0", "url": f"{SITE}/archive/",
        "description": desc,
        "isPartOf": {"@type": "WebSite", "name": "Meliorism 2.0", "url": SITE + "/"},
        "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "url": it["url"], "name": it["title"]}
            for i, it in enumerate(items)]}}
    j = "\n".join("  " + l for l in json.dumps(item_list, indent=2, ensure_ascii=False).splitlines())
    return (
        f'  {S}\n'
        f'  <meta name="description" content="{ihtml.escape(desc, quote=True)}">\n'
        f'  <link rel="canonical" href="{SITE}/archive/">\n'
        f'  <meta property="og:type" content="website">\n'
        f'  <meta property="og:title" content="The Practitioner\'s Library — Meliorism 2.0">\n'
        f'  <meta property="og:description" content="{ihtml.escape(desc, quote=True)}">\n'
        f'  <meta property="og:url" content="{SITE}/archive/">\n'
        f'  <meta property="og:site_name" content="Meliorism 2.0">\n'
        f'  <script type="application/ld+json">\n{j}\n  </script>\n'
    )

def run():
    items = issues()
    # --- homepage ---
    ip = os.path.join(ROOT, "index.html")
    t = open(ip).read()
    if S not in t:
        t = t.replace("</head>", home_head(items) + "</head>", 1)
        t = t.replace("  <!-- FOUNDING STRIP -->", recent_section(items) + "  <!-- FOUNDING STRIP -->", 1)
        t = t.replace(
            "      <span>© 2026 Meliorist Group · San Francisco</span>",
            '      <span>© 2026 <a href="https://melioristgroup.com" style="color:inherit;">Meliorist Group</a> · San Francisco</span>\n'
            '      <span>Published by <a href="https://brianoney.com" style="color:inherit;">Brian Oney</a></span>', 1)
        open(ip, "w").write(t)
        print("index.html: injected")
    else:
        print("index.html: already had sentinel, skipped")
    # --- archive index ---
    ap = os.path.join(ROOT, "archive", "index.html")
    a = open(ap).read()
    if S not in a:
        a = a.replace("</head>", archive_head(items) + "</head>", 1)
        # footer backlink: add a line near the existing back-link
        a = a.replace(
            '      <div><a href="/">&#8592; Back to meliorism2.com</a></div>',
            '      <div><a href="/">&#8592; Back to meliorism2.com</a></div>\n'
            '      <div style="font-size:0.72rem;">Published by <a href="https://brianoney.com">Brian Oney</a> · <a href="https://melioristgroup.com">Meliorist Group</a></div>', 1)
        open(ap, "w").write(a)
        print(f"archive/index.html: injected (ItemList of {len(items)} issues)")
    else:
        print("archive/index.html: already had sentinel, skipped")

if __name__ == "__main__":
    run()
