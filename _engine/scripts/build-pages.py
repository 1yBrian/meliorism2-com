#!/usr/bin/env python3
"""
build-pages.py — generate structural pages for Meliorism2.com from the issue dataset.

Builds (all claim-clean, schema-rich, interlinked):
  /about.html                      — publication About (origin story, Brian Oney / Meliorist Group)
  /topics/index.html               — Topics (dimensions) index
  /topics/<slug>.html  × 5         — one hub per core dimension, listing its issues

Reads the issue dataset straight from archive/index.html's JS array, so it stays in sync.
Run from repo root:  python3 _engine/scripts/build-pages.py
NOTE: these are NOT dated issue files, so deploying them does NOT trigger the (paid) truth agent.
"""
import re, json, html as ihtml, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://meliorism2.com"
EMAIL = "brian@melioristgroup.com"

# Taxonomy → one hub per dimension. An expanding set (target 13+ → a book).
# Descriptions are DRAFT — refine in Brian's voice anytime; re-run this script to update.
DIMS = [
    ("witnessing-authentic-humanity", "Witnessing Authentic Humanity",
     "Seeing people as they actually are — beneath role, performance, and assumption — and what that asks of a practitioner."),
    ("brave-spaces", "Brave Spaces",
     "Building rooms that can hold discomfort without harm, where honesty is possible and real change can happen."),
    ("living-income", "Living Income",
     "The economics of practitioner work — value, pricing, and being paid for what you actually do."),
    ("in-person-presence", "In-Person Presence",
     "What embodied, in-the-room presence does that mediated interaction cannot — and why it still matters."),
    ("gender-generational-difference", "Gender & Generational Difference",
     "How gender and generation shape trust, learning, and communication in practitioner settings."),
    ("critical-consciousness", "Critical Consciousness",
     "Seeing the systems, incentives, and power structures shaping a situation — and helping clients act with that awareness."),
    ("becoming-adaptable", "Becoming Adaptable",
     "Building the capacity to adjust — staying effective and grounded as tools, conditions, and expectations shift."),
    ("somatic-body-intelligence", "Somatic / Body Intelligence",
     "What the body registers before the mind names it — using somatic signal as practitioner information."),
    ("adventure", "Adventure",
     "Risk, exploration, and the practice of moving toward the unfamiliar on purpose."),
]

def issues():
    h = open(os.path.join(ROOT, "archive", "index.html")).read()
    objs = re.findall(r'\{[^{}]*?file:"[^"]+\.html"[^{}]*?\}', h)
    out = []
    for o in objs:
        d = dict(re.findall(r'(\w+):"((?:[^"\\]|\\.)*)"', o))
        if "file" in d:
            d["url"] = f"{SITE}/archive/{d['file']}"
            out.append(d)
    out.sort(key=lambda x: x.get("date", ""), reverse=True)
    return out

STYLE = """
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
  :root{--cream:#faf8f5;--surface:#f0ebe5;--accent:#8b6f47;--accent-dark:#6b5235;--text:#1e1e1e;--text-muted:#5a5550;--dark-bg:#1a1714}
  html{font-size:18px;scroll-behavior:smooth}
  body{font-family:'Crimson Text',Georgia,serif;background:var(--cream);color:var(--text);line-height:1.7;overflow-x:hidden}
  a{color:var(--accent);text-decoration:none}
  .nav{position:sticky;top:0;z-index:100;background:var(--cream);border-bottom:1px solid #d8cfc4;display:flex;align-items:center;justify-content:space-between;padding:0 48px;height:64px}
  .nav-logo{font-family:'Courier Prime',monospace;font-weight:700;font-size:1.05rem;letter-spacing:0.12em;color:var(--text);text-transform:uppercase}
  .nav-links{display:flex;gap:28px;list-style:none}
  .nav-links a{font-family:'Courier Prime',monospace;font-size:0.8rem;letter-spacing:0.08em;color:var(--text-muted);text-transform:uppercase}
  .nav-links a:hover{color:var(--accent)}
  .wrap{max-width:860px;margin:0 auto;padding:64px 32px}
  .crumb{font-family:'Courier Prime',monospace;font-size:0.72rem;letter-spacing:0.08em;color:var(--text-muted);text-transform:uppercase;margin-bottom:28px}
  .eyebrow{font-family:'Courier Prime',monospace;font-size:0.75rem;letter-spacing:0.14em;color:var(--accent);text-transform:uppercase;margin-bottom:20px}
  h1{font-size:clamp(2.2rem,5vw,3.2rem);font-weight:600;line-height:1.15;margin-bottom:24px}
  h2{font-size:1.5rem;font-weight:600;margin:40px 0 16px}
  p{margin-bottom:18px;font-size:1.12rem}
  .lead{font-size:1.3rem;line-height:1.75;color:var(--text);margin-bottom:32px}
  .issue{display:block;padding:20px 0;border-bottom:1px solid #d8cfc4}
  .issue .d{font-family:'Courier Prime',monospace;font-size:0.72rem;letter-spacing:0.08em;color:var(--text-muted)}
  .issue .t{font-size:1.2rem;font-weight:600;color:var(--text);display:block;margin:4px 0 6px}
  .issue .c{font-size:0.98rem;color:var(--text-muted);font-style:italic}
  .dimgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:#d8cfc4;border:1px solid #d8cfc4;margin-top:24px}
  .dimgrid a{background:var(--cream);padding:28px;display:block}
  .dimgrid a:hover{background:var(--surface)}
  .dimgrid .t{font-size:1.25rem;font-weight:600;color:var(--text);display:block;margin-bottom:8px}
  .dimgrid .c{font-size:0.95rem;color:var(--text-muted)}
  footer{background:var(--dark-bg);color:#8a8070;padding:40px 48px;font-family:'Courier Prime',monospace;font-size:0.75rem;line-height:1.9;text-align:center}
  footer a{color:#c8a87a}
  @media(max-width:700px){.nav{padding:0 20px}.nav-links{gap:14px}.dimgrid{grid-template-columns:1fr}}
"""

def shell(title, desc, canon, schema, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{ihtml.escape(title)}</title>
  <meta name="description" content="{ihtml.escape(desc, quote=True)}">
  <link rel="canonical" href="{canon}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{ihtml.escape(title, quote=True)}">
  <meta property="og:description" content="{ihtml.escape(desc, quote=True)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:site_name" content="Meliorism 2.0">
  <meta name="twitter:card" content="summary">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{schema}
  </script>
  <style>{STYLE}</style>
</head>
<body>
  <nav class="nav">
    <a href="/" class="nav-logo">Meliorism2.com</a>
    <ul class="nav-links">
      <li><a href="/archive/">Library</a></li>
      <li><a href="/topics/">Topics</a></li>
      <li><a href="/about.html">About</a></li>
      <li><a href="/founding.html">Founding</a></li>
    </ul>
  </nav>
{body}
  <footer>
    Meliorism 2.0 — a research instrument and daily briefing published by
    <a href="https://brianoney.com">Brian Oney</a> · <a href="https://melioristgroup.com">Meliorist Group</a>, San Francisco.<br>
    <a href="mailto:{EMAIL}">{EMAIL}</a> · © 2026 Meliorist Group
  </footer>
</body>
</html>
"""

def issue_row(it):
    return (f'      <a class="issue" href="{it["url"]}">'
            f'<span class="d">{it.get("date","")}</span>'
            f'<span class="t">{ihtml.escape(it.get("title",""))}</span>'
            f'<span class="c">{ihtml.escape(it.get("concept",""))}</span></a>')

def build_dimension(slug, name, desc, items):
    mine = [it for it in items if it.get("dimension") == name]
    rows = "\n".join(issue_row(it) for it in mine) or "      <p>Issues in this topic are on the way.</p>"
    canon = f"{SITE}/topics/{slug}.html"
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": f"{name} — Meliorism 2.0", "url": canon, "description": desc,
        "isPartOf": {"@type": "WebSite", "name": "Meliorism 2.0", "url": SITE + "/"},
        "mainEntity": {"@type": "ItemList", "numberOfItems": len(mine),
            "itemListElement": [{"@type": "ListItem", "position": i+1, "url": it["url"], "name": it.get("title","")}
                                for i, it in enumerate(mine)]},
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Topics", "item": SITE + "/topics/"},
            {"@type": "ListItem", "position": 3, "name": name, "item": canon}]},
    }, indent=2, ensure_ascii=False)
    schema = "\n".join("  " + l for l in schema.splitlines())
    body = f"""  <main class="wrap">
    <div class="crumb"><a href="/">Home</a> › <a href="/topics/">Topics</a> › {ihtml.escape(name)}</div>
    <div class="eyebrow">Topic</div>
    <h1>{ihtml.escape(name)}</h1>
    <p class="lead">{ihtml.escape(desc)}</p>
    <h2>Issues in this topic ({len(mine)})</h2>
{rows}
  </main>"""
    return canon, shell(f"{name} — Meliorism 2.0", desc, canon, schema, body)

def build_topics_index(items):
    canon = f"{SITE}/topics/"
    cards = "\n".join(
        f'      <a href="/topics/{slug}.html"><span class="t">{ihtml.escape(name)}</span>'
        f'<span class="c">{ihtml.escape(desc)}</span></a>'
        for slug, name, desc in DIMS)
    schema = json.dumps({"@context":"https://schema.org","@type":"CollectionPage",
        "name":"Topics — Meliorism 2.0","url":canon,
        "description":"The dimensions Meliorism 2.0 covers — the recurring obstacles practitioners face.",
        "isPartOf":{"@type":"WebSite","name":"Meliorism 2.0","url":SITE+"/"}}, indent=2, ensure_ascii=False)
    schema = "\n".join("  " + l for l in schema.splitlines())
    body = f"""  <main class="wrap">
    <div class="crumb"><a href="/">Home</a> › Topics</div>
    <div class="eyebrow">Topics</div>
    <h1>What Meliorism 2.0 covers</h1>
    <p class="lead">Every issue names one obstacle getting in your clients' way. Those obstacles cluster into a handful of recurring dimensions — the themes the publication returns to.</p>
    <div class="dimgrid">
{cards}
    </div>
  </main>"""
    return canon, shell("Topics — Meliorism 2.0",
        "The dimensions Meliorism 2.0 covers — the recurring obstacles practitioners face, with every issue grouped by theme.",
        canon, schema, body)

def build_about():
    canon = f"{SITE}/about.html"
    desc = ("Meliorism 2.0 is a daily, research-grounded briefing by Brian Oney (Meliorist Group) for trainers, "
            "coaches, and educators — built first as a research instrument, then published openly.")
    schema = json.dumps({"@context":"https://schema.org","@type":"AboutPage",
        "name":"About — Meliorism 2.0","url":canon,"description":desc,
        "mainEntity":{"@type":"Person","name":"Brian Oney","url":"https://brianoney.com",
            "jobTitle":"Advisor, Trainer, Writer, and developer of Meliorism 2.0",
            "worksFor":{"@type":"Organization","name":"Meliorist Group","url":"https://melioristgroup.com"},
            "sameAs":["https://brianoney.com","https://melioristgroup.com"]},
        "publisher":{"@type":"Organization","name":"Meliorist Group","url":"https://melioristgroup.com"}},
        indent=2, ensure_ascii=False)
    schema = "\n".join("  " + l for l in schema.splitlines())
    body = f"""  <main class="wrap">
    <div class="crumb"><a href="/">Home</a> › About</div>
    <div class="eyebrow">About</div>
    <h1>About Meliorism 2.0</h1>
    <p class="lead">Meliorism 2.0 is a daily briefing for trainers, coaches, educators, and knowledge workers navigating an AI-shaped economy. Each issue names one specific obstacle getting in your clients' way, traces its mechanism, and gives you language to reach for in the room.</p>
    <h2>Where it came from</h2>
    <p>Brian Oney originally built Meliorism 2.0 to feed his own brain — a daily research instrument for gathering the ideas, research, and perspectives that sharpen his practice as a Meliorist 2.0. He needed that signal and couldn't find it, so he made it. The same feed that develops his thinking is now open to anyone whose work is human-centered and wants to stay that way.</p>
    <h2>Who publishes it</h2>
    <p>Meliorism 2.0 is written and published by <a href="https://brianoney.com">Brian Oney</a>, a business advisor, trainer, and the developer of the Meliorism 2.0 philosophy, through <a href="https://melioristgroup.com">Meliorist Group</a> — his research and applied philosophy practice in San Francisco.</p>
    <h2>What it stands on</h2>
    <p>Each issue cites its sources and traces the mechanism from research to practice. No motivational padding. No product pitches. The standard is signal: read it, follow the thread, and adapt the insight with confidence.</p>
    <h2>The topics it returns to</h2>
    <p>The work clusters into recurring dimensions — the obstacles practitioners face again and again. <a href="/topics/">Browse the topics →</a></p>
    <h2>Support the work</h2>
    <p>Meliorism 2.0 is donation-based, with no paywall. If it earns your support, you can sustain it. <a href="/founding.html">Become a founding supporter →</a></p>
  </main>"""
    return canon, shell("About — Meliorism 2.0", desc, canon, schema, body)

def run():
    items = issues()
    os.makedirs(os.path.join(ROOT, "topics"), exist_ok=True)
    written = []
    for slug, name, desc in DIMS:
        canon, html = build_dimension(slug, name, desc, items)
        path = os.path.join(ROOT, "topics", f"{slug}.html")
        open(path, "w").write(html); written.append(f"topics/{slug}.html")
    canon, html = build_topics_index(items)
    open(os.path.join(ROOT, "topics", "index.html"), "w").write(html); written.append("topics/index.html")
    canon, html = build_about()
    open(os.path.join(ROOT, "about.html"), "w").write(html); written.append("about.html")
    print("built:")
    for w in written: print("  ", w)
    # coverage report
    from collections import Counter
    covered = sum(1 for it in items if it.get("dimension") in {n for _, n, _ in DIMS})
    print(f"issues={len(items)} | covered-by-5-hubs={covered} | off-taxonomy={len(items)-covered}")

if __name__ == "__main__":
    run()
