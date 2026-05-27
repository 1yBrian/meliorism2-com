#!/usr/bin/env python3
"""
Truth Agent — Meliorism2 pre-publish integrity check
Reads an issue HTML, sends prose to Claude, flags three problem categories.

Usage:
  python3 _engine/truth_agent.py archive/YYYY-MM-DD-slug.html

Exit codes:
  0 = PASS or WARN  — deploy allowed (warnings noted in report)
  1 = BLOCKED       — over-promises found; fix before deploying
  2 = ERROR         — agent couldn't run; deploy continues with warning
"""

import sys, os, re, json, html as html_lib
from datetime import datetime
from pathlib import Path

# ── HTML → readable text ──────────────────────────────────────────────────────

def extract_text(html_content):
    text = re.sub(r'<script[^>]*>.*?</script>', ' ', html_content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<!--(?!meliorism2).*?-->', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html_lib.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_metadata(html_content):
    meta = {}
    for m in re.finditer(r'<!--\s*meliorism2:(\w+):\s*(.+?)\s*-->', html_content):
        meta[m.group(1)] = m.group(2)
    return meta

# ── Claude API call ───────────────────────────────────────────────────────────

PROMPT_TEMPLATE = """You are the Truth Agent for Meliorism2.com — a daily practitioner publication for trainers, coaches, and educators. Your job is to read a draft issue and flag three categories of problems before it publishes. Be precise. Only flag real problems. Do not invent issues.

Issue: "{title}" ({slug})

---
{text}
---

Flag these three categories:

CATEGORY 1 — OVER-PROMISES (blocks deployment)
Unverified claims about frequency, timing, universality, or guaranteed outcomes that the publication cannot currently back up.
Examples to catch: specific times ("every morning at 4 AM"), absolute universals ("always," "every practitioner," "proven to"), unverified reach claims ("practitioners worldwide"), promises the publication cannot guarantee.
Do NOT flag: claims made within cited research findings, historical facts with sources, qualified statements ("research suggests").

CATEGORY 2 — NEEDS CITATION (warning only, does not block)
Specific statistics, percentages, named studies, named researchers, or empirical findings presented as fact without a visible citation nearby or in the bibliography.
Do NOT flag: general observations, practitioner heuristics, named concepts that are explained in context.

CATEGORY 3 — SOFT OVERCLAIMS (warning only, does not block)
Editorial overstatement that inflates the claim beyond what's demonstrated.
Examples: "changes everything," "unlike anything else," "the most important," "completely transforms."

Respond in EXACTLY this format — no preamble, no commentary, nothing before or after:

OVER_PROMISES: [integer]
[list each as: - "[exact quote from text]" — [reason it's a problem]]

NEEDS_CITATION: [integer]
[list each as: - "[exact quote from text]" — [what citation is needed]]

SOFT_OVERCLAIMS: [integer]
[list each as: - "[exact quote from text]" — [suggested revision]]

VERDICT: [PASS|WARN|BLOCKED]
(PASS = all zeros; WARN = NEEDS_CITATION or SOFT_OVERCLAIMS > 0 but OVER_PROMISES = 0; BLOCKED = OVER_PROMISES > 0)"""

def call_api(text, title, slug):
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("  ⚠  ANTHROPIC_API_KEY not set — truth check skipped (deploy continues)")
        print("     Add to ~/.zshrc: export ANTHROPIC_API_KEY=\"your-key\"")
        return None

    try:
        import anthropic
    except ImportError:
        print("  ⚠  anthropic SDK not found — run: pip3 install anthropic")
        print("     Truth check skipped (deploy continues)")
        return None

    client = anthropic.Anthropic(api_key=api_key)

    # Trim text to ~6000 chars — enough for the full prose, avoids token waste
    prose = text[:6000] + ("..." if len(text) > 6000 else "")

    try:
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1200,
            messages=[{
                "role": "user",
                "content": PROMPT_TEMPLATE.format(
                    title=title, slug=slug, text=prose
                )
            }]
        )
        return msg.content[0].text
    except Exception as e:
        print(f"  ⚠  API call failed: {type(e).__name__} — truth check skipped")
        return None

# ── Parse response ────────────────────────────────────────────────────────────

def parse_count(response, category):
    m = re.search(rf'{category}:\s*(\d+)', response)
    return int(m.group(1)) if m else 0

def parse_verdict(response):
    m = re.search(r'VERDICT:\s*(PASS|WARN|BLOCKED)', response)
    if not m:
        # Derive from counts if VERDICT line is missing
        if parse_count(response, 'OVER_PROMISES') > 0:
            return 'BLOCKED'
        if parse_count(response, 'NEEDS_CITATION') > 0 or parse_count(response, 'SOFT_OVERCLAIMS') > 0:
            return 'WARN'
        return 'PASS'
    return m.group(1)

# ── Write report ──────────────────────────────────────────────────────────────

def write_report(repo_root, response, verdict, title, slug, date_str):
    staging_dir = repo_root / '_engine' / 'staging'
    staging_dir.mkdir(parents=True, exist_ok=True)
    report_path = staging_dir / f"{date_str}-{slug}-truth-check.md"

    op  = parse_count(response, 'OVER_PROMISES')
    nc  = parse_count(response, 'NEEDS_CITATION')
    so  = parse_count(response, 'SOFT_OVERCLAIMS')

    report = f"""# Truth Check — {title}
*Run: {datetime.now().strftime('%Y-%m-%d %H:%M')} · Verdict: {verdict}*

## Summary
| Category | Count | Blocks deploy? |
|----------|-------|----------------|
| Over-promises | {op} | {'YES' if op > 0 else 'no'} |
| Needs citation | {nc} | no |
| Soft overclaims | {so} | no |

## Full Report

{response}

---
*Generated by `_engine/truth_agent.py` · Meliorism2 pre-publish gate*
"""
    report_path.write_text(report, encoding='utf-8')
    return report_path

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 _engine/truth_agent.py archive/YYYY-MM-DD-slug.html")
        sys.exit(2)

    html_path = Path(sys.argv[1]).resolve()
    if not html_path.exists():
        print(f"  ✗ File not found: {sys.argv[1]}")
        sys.exit(2)

    html_content = html_path.read_text(encoding='utf-8')
    meta = extract_metadata(html_content)

    slug     = meta.get('slug', html_path.stem)
    date_str = meta.get('date', html_path.stem[:10])
    title    = slug.replace('-', ' ').title()

    # Repo root = directory containing _engine/
    repo_root = html_path.parent.parent

    print(f"\n  TRUTH AGENT · {slug}")
    print(f"  {'─' * 48}")

    text = extract_text(html_content)
    response = call_api(text, title, slug)

    if response is None:
        sys.exit(0)  # Graceful skip — key missing or API unreachable

    verdict  = parse_verdict(response)
    op_count = parse_count(response, 'OVER_PROMISES')
    nc_count = parse_count(response, 'NEEDS_CITATION')
    so_count = parse_count(response, 'SOFT_OVERCLAIMS')

    report_path = write_report(repo_root, response, verdict, title, slug, date_str)

    # ── Print results ─────────────────────────────────────────────────────────
    if op_count > 0:
        print(f"  ✗ OVER-PROMISES ({op_count}) — deploy BLOCKED")
        # Print each flag
        for line in response.split('\n'):
            if line.strip().startswith('-') and 'NEEDS_CITATION' not in line and 'SOFT_OVERCLAIMS' not in line:
                # Only print lines between OVER_PROMISES and the next category
                pass
        # Print the over-promise lines from the full response
        in_op = False
        for line in response.split('\n'):
            if line.startswith('OVER_PROMISES:'):
                in_op = True
                continue
            if in_op and (line.startswith('NEEDS_CITATION:') or line.startswith('SOFT_OVERCLAIMS:') or line.startswith('VERDICT:')):
                in_op = False
            if in_op and line.strip().startswith('-'):
                print(f"    {line.strip()}")
    else:
        print(f"  ✓ No over-promises")

    if nc_count > 0:
        print(f"  ⚠  Needs citation ({nc_count}) — review recommended")
    if so_count > 0:
        print(f"  ⚠  Soft overclaims ({so_count}) — review recommended")

    print(f"\n  Verdict: {verdict}")
    print(f"  Report:  {report_path.relative_to(repo_root)}")

    if verdict == 'BLOCKED':
        print(f"\n  ✗ DEPLOY BLOCKED — resolve over-promises above before publishing.\n")
        sys.exit(1)
    elif verdict == 'WARN':
        print(f"  ⚠  Warnings noted — check report before publishing (deploy not blocked).\n")
        sys.exit(0)
    else:
        print(f"  ✓ PASS — no issues found.\n")
        sys.exit(0)

if __name__ == '__main__':
    main()
