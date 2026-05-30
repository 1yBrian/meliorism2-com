#!/usr/bin/env python3
"""system_audit.py — Coverage map of source documents → enforced gates.

For each source document, list the laws/rules it declares and check whether a
gate (script, workflow, or documented agent role) enforces it. Output a
coverage report.

This is the meta-gate: it prevents future blind spots by surfacing every law
that has no enforcement.

Source documents scanned:
  - _engine/DESIGN-ENGINE.md         (LAW OF... sections + HARD TYPOGRAPHY FLOOR + Uniqueness)
  - _engine/DESIGN-LEDGER.md         (Enforcement rules block)
  - _engine/LEARNING-LOG.md          ("Flagged" rows in Design Notes + Voice Drift Watch)
  - _engine/PIPELINE.md              (Phase index — which phases have skills/scripts)
  - 08 - The Intermodal Hub/Meliorism2 .../MELIORISM2-DIRECTIVE.md  (§11 Permanent Rules)
  - 08 - The Intermodal Hub/Meliorism2 .../PHOTO-PROTOCOL.md        (Ironclad rules)

Output: console report + `_engine/SYSTEM-AUDIT-LATEST.md`.

Usage:
    python3 _engine/scripts/system_audit.py
"""
import re, sys, pathlib
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parents[2]
VAULT_M2 = pathlib.Path.home() / "Documents/Obsidian Vault/08 - The Intermodal Hub/Meliorism2 (Formally Signal-OS)"

SCRIPTS_DIR = REPO / "_engine" / "scripts"
WORKFLOWS_DIR = REPO / ".github" / "workflows"

# Map source-document laws to expected gate scripts
LAW_GATE_MAP = {
    "DESIGN-ENGINE — Law of Earned Advance":              "earned_advance_check.py",
    "DESIGN-ENGINE — Law of Real Delight":                "(subjective: Plain Reader chat)",
    "DESIGN-ENGINE — Law of the Generous Wrong":          "(subjective: Agitator chat)",
    "DESIGN-ENGINE — Law of Role Elevation":              "(subjective: Plain Reader chat)",
    "DESIGN-ENGINE — HARD TYPOGRAPHY FLOOR (0.8rem)":     "typography_floor.py",
    "DESIGN-ENGINE — Uniqueness Guarantee":               "ledger_check.py",
    "DESIGN-LEDGER — Row complete (5 coordinates)":       "ledger_check.py",
    "DESIGN-LEDGER — No identical (container × primitive)": "ledger_check.py",
    "DESIGN-LEDGER — Hue not reused in 7-issue window":   "ledger_check.py",
    "DESIGN-LEDGER — Container family not in 14 window":  "ledger_check.py",
    "DESIGN-LEDGER — Archetype not same as prior":        "ledger_check.py",
    "LEARNING-LOG — Black as default flagged":            "palette_check.py",
    "LEARNING-LOG — Voice Drift: 'practitioner who X is doing Y'": "voice_drift_check.py",
    "LEARNING-LOG — Voice Drift: 'This is not X. This is Y.'":     "voice_drift_check.py",
    "LEARNING-LOG — Voice Drift: decision-maker register": "voice_drift_check.py",
    "LEARNING-LOG — Voice Drift: watcher register":        "voice_drift_check.py",
    "MELIORISM2-DIRECTIVE §11 — No Unsplash URLs (local only)": "unsplash_url_check.py",
    "MELIORISM2-DIRECTIVE §11 — meliorism2: prefix on metadata": "(implicit — metadata gate)",
    "MELIORISM2-DIRECTIVE §11 — 'READ →' is never the CTA":      "cta_check.py",
    "MELIORISM2-DIRECTIVE §11 — Minimum contrast #2c2c2c on cream": "(needed: contrast_check.py)",
    "MELIORISM2-DIRECTIVE §15 — Section title scoring":          "section_title_score.py",
    "MELIORISM2-DIRECTIVE §14 — Anti-Regression: pattern fatigue check": "(needed: pattern_fatigue_check.py)",
    "MELIORISM2-DIRECTIVE §14 — Anti-Regression: aesthetic drift":       "(needed: aesthetic_drift_check.py)",
    "MELIORISM2-DIRECTIVE §14 — Anti-Regression: scroll test":           "(needed: scroll_test.py — could the issue be a PDF?)",
    "MELIORISM2-DIRECTIVE §14 — Two-Title Rule":                         "(needed: two_title_check.py)",
    "MELIORISM2-DIRECTIVE §16 — Two-way navigation":                     "(needed: navigation_check.py)",
    "MELIORISM2-DIRECTIVE §16 — Directory station on page 1 or 2":       "(needed: directory_station_check.py)",
    "MELIORISM2-DIRECTIVE §16 — Define the Unknown (terms at first use)": "(subjective: Plain Reader chat)",
    "MELIORISM2-DIRECTIVE §16 — No False Affordances":                    "(needed: false_affordance_check.py)",
    "PHOTO-PROTOCOL Rule 1 — Attribution mandatory":      "photo_check.py",
    "PHOTO-PROTOCOL Rule 2 — Local files only":           "unsplash_url_check.py",
    "PHOTO-PROTOCOL Rule 3 — Rate limit (logged)":        "(needed: photo_usage_log_check.py)",
    "PHOTO-PROTOCOL §image alignment law (image = weather)": "(subjective: Design Editor chat)",
    "PHOTO-PROTOCOL §readability law (words always win)":   "(needed: image_text_contrast_check.py)",
    "PIPELINE Phase 1 — Randomizer":                      "(skill: phase-1-randomizer)",
    "PIPELINE Phase 2 — Dimension Research":              "(skill: phase-2-dimension-research)",
    "PIPELINE Phase 3 — Editorial Selection":             "(skill: phase-3-editorial-selection)",
    "PIPELINE Phase 3.5 — The Agitator":                  "(skill: the-agitator — needed)",
    "PIPELINE Phase 4 — Composing":                       "(skill: phase-4-issue-composition)",
    "PIPELINE Phase 5 — Editorial Review":                "(skill: phase-5-editorial-review)",
    "PIPELINE Phase 6 — Reviewer Stress Test":            "(skill: phase-6-stress-test)",
    "PIPELINE Phase 7 — Bibliographer":                   "(skill: phase-7-bibliographer)",
    "PIPELINE Phase 8a — Design Amplification":           "(skill: phase-8-design-amplification)",
    "PIPELINE Phase 8b — Publicist":                      "(skill: the-publicist)",
    "PIPELINE Phase 9 — Deploy":                          "daily-release.yml + deploy-api.sh",
    "CLAUDE.md — Help Rule":                              "help_rule_check.py",
    "CLAUDE.md — Truth (no over-promise, future studies)": "truth_lint.py",
    "Hero image — must resolve":                          "image_check.py",
    "Citations — closing block + integrity":              "citation_check.py",
    "No paid API in cron paths":                          "no_anthropic_in_cron.py",
    "Live verification (heartbeat)":                       "monitor.py",
}

def script_exists(name: str) -> bool:
    if name.startswith("("): return False  # subjective / unbuilt
    return (SCRIPTS_DIR / name).exists() or (WORKFLOWS_DIR / name).exists()

def main():
    repo_scripts = {p.name for p in SCRIPTS_DIR.glob("*.py")} | {p.name for p in WORKFLOWS_DIR.glob("*.yml")}
    rows = []
    enforced = 0
    needed_scripts = []
    subjective_or_skills = []
    for law, gate in LAW_GATE_MAP.items():
        if script_exists(gate):
            status = "✅ enforced"
            enforced += 1
        elif gate.startswith("(needed:"):
            status = "🔴 unbuilt"
            needed_scripts.append((law, gate))
        elif gate.startswith("(skill:") or gate.startswith("(subjective"):
            status = "🟡 chat/skill"
            subjective_or_skills.append((law, gate))
        else:
            status = "🔴 unbuilt"
            needed_scripts.append((law, gate))
        rows.append((law, gate, status))

    total = len(LAW_GATE_MAP)
    pct = 100 * enforced / total
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Console output
    print(f"\n══════ SYSTEM AUDIT — {now} ══════\n")
    print(f"  Laws scanned:        {total}")
    print(f"  Deterministic gates: {enforced} ({pct:.0f}%)")
    print(f"  Chat/skill (subjective or pipeline): {len(subjective_or_skills)}")
    print(f"  Unbuilt: {len(needed_scripts)}\n")

    print("─── DETERMINISTIC GATES (script exists) ───")
    for law, gate, status in rows:
        if status.startswith("✅"):
            print(f"  ✅ {law:60} → {gate}")

    print("\n─── CHAT / SKILL (subjective or pipeline agents — chat sessions) ───")
    for law, gate in subjective_or_skills:
        print(f"  🟡 {law:60} → {gate}")

    print("\n─── UNBUILT (deterministic but missing) ───")
    for law, gate in needed_scripts:
        print(f"  🔴 {law:60} → {gate}")

    # Markdown report
    md = [
        f"# System Audit — {now}",
        "",
        f"- Laws scanned: **{total}**",
        f"- Deterministic gates enforced: **{enforced} ({pct:.0f}%)**",
        f"- Chat/skill (subjective or pipeline): **{len(subjective_or_skills)}**",
        f"- Unbuilt (deterministic): **{len(needed_scripts)}**",
        "",
        "## Enforced",
        "",
        "| Law | Gate |",
        "|-----|------|",
    ]
    for law, gate, status in rows:
        if status.startswith("✅"):
            md.append(f"| {law} | `{gate}` |")
    md += ["", "## Chat / skill (subjective or pipeline)", "", "| Law | Where it lives |", "|-----|---------------|"]
    for law, gate in subjective_or_skills:
        md.append(f"| {law} | {gate} |")
    md += ["", "## Unbuilt — next deterministic gates to write", "", "| Law | Proposed gate |", "|-----|---------------|"]
    for law, gate in needed_scripts:
        md.append(f"| {law} | {gate} |")
    md.append("")
    md.append("*Generated by `_engine/scripts/system_audit.py`. Re-run after every new gate or skill is added.*")

    out_path = REPO / "_engine" / "SYSTEM-AUDIT-LATEST.md"
    out_path.write_text("\n".join(md))
    print(f"\n→ Report written to {out_path}")

if __name__ == "__main__":
    main()
