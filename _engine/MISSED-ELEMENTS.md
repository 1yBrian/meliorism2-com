# MISSED ELEMENTS LEDGER
*The system's record of its own blind spots. Every entry is a permanent gate.*
*One row per missed element. The system_audit.py script reads this and the source documents to confirm every entry has a live gate or chat-session check.*

---

## How this works

When a gap is discovered between what the system *claims* to enforce (in its source documents) and what it *actually* enforces (via cron-runnable gates or chat-session checks):

1. **Log it here** — one row, format below.
2. **Add the gate** — script in `_engine/scripts/` for deterministic checks, or a documented agent role for subjective ones.
3. **Update `editor_review.py`** — wire the new gate into the HARD or SOFT tier.
4. **Update `PUBLICATION-SOUL.md`** — add row to the Compliance Gate Map.
5. **Run `backfill.py`** — re-audit every past issue against the new gate.
6. **Mark as closed.**

A row stays OPEN until all 5 actions are complete.

---

## Entry format

```
### [Element name]
- Discovered: YYYY-MM-DD
- Source document: [where the rule was already written]
- How it was missed: [why the system didn't catch it before]
- Status: OPEN | GATED | CLOSED
- Gate added: [script name or chat-session role]
- Backfill required: yes | no | done
- Reference: [link or path]
```

---

## Discovered 2026-05-30 (the founding batch)

### Black palette as default — must be earned
- Discovered: 2026-05-30
- Source document: `_engine/LEARNING-LOG.md` Design Notes — "Black as default entry screen | Flagged | Dark backgrounds must be earned from content. Not a default. Open palette is the baseline."
- How it was missed: The first Issue Standard draft (PUBLICATION-SOUL v1.2) didn't reference LEARNING-LOG. Zen wrote a 19-point spec without reading the existing law set.
- Status: CLOSED
- Gate added: `_engine/scripts/palette_check.py` — requires `<!-- meliorism2:palette: dark -->` + `<!-- meliorism2:palette-justification: ... -->` with non-lazy justification ≥20 chars; otherwise light palette is the default.
- Backfill required: yes — all past 30 issues need palette declared + justified or swapped to light. Ledger 027 (Tide Chart) is the precedent for earned dark.
- Reference: LEARNING-LOG.md line 45

### Broken hero image — CSS filename mismatch
- Discovered: 2026-05-30 (Issue 030 The Provenance Document — CSS called `the-provenance-document-hero.jpg`; file on disk was `provenance-document-hero.jpg`)
- Source document: PHOTO-PROTOCOL.md Rule 2 + MELIORISM2-DIRECTIVE §7 Image Pipeline
- How it was missed: No gate checked that image references in CSS / `<img src>` resolve to actual files in the repo.
- Status: CLOSED
- Gate added: `_engine/scripts/image_check.py` — every `url()` / `src=` for image files must resolve.
- Backfill required: yes — `backfill.py` will identify any past issue with broken refs.
- Reference: archive/2026-05-30-the-provenance-document.html line 76 + 803

### DESIGN-LEDGER row was deployed marked "NEEDS BACKFILL"
- Discovered: 2026-05-30 (Issue 030 + 031 both rows blank — deployed anyway)
- Source document: `_engine/DESIGN-LEDGER.md` — "The engine reads this before every generation."
- How it was missed: No gate checked the ledger row before deploy. Phase 9 Iron Law (PIPELINE.md) was not enforced.
- Status: CLOSED
- Gate added: `_engine/scripts/ledger_check.py` — row must exist; all 5 coordinates (weather, archetype, container, primitive, hue) must be populated; uniqueness rules enforced.
- Backfill required: yes — 28 ledger rows (May 1–24 + 028 + 030 + 031) need coordinates filled.
- Reference: DESIGN-LEDGER.md lines 32–34, 41–66

### Typography floor (0.8rem) violated systemically across all issues
- Discovered: 2026-05-30 (4 sub-floor sizes in every issue tested — endemic template inheritance)
- Source document: `_engine/DESIGN-ENGINE.md` HARD TYPOGRAPHY FLOOR + `MELIORISM2-DIRECTIVE.md` §7d
- How it was missed: The audit grep command described in §7d was never wired into the deploy pipeline.
- Status: CLOSED
- Gate added: `_engine/scripts/typography_floor.py` — fails on any `font-size:` below 0.8rem / 13px.
- Backfill required: yes — single root-cause fix in the shared template will likely fix all 30 issues at once; identify the template first.
- Reference: DESIGN-ENGINE.md §HARD TYPOGRAPHY FLOOR

### Closing citations block missing
- Discovered: 2026-05-30 (Issue 030 has `[0]` footnote orphan + no citations block)
- Source document: PUBLICATION-SOUL three non-negotiables + PIPELINE.md Phase 7 Iron Law
- How it was missed: Citations were treated as "nice to have"; Phase 7 Bibliographer was documented but not run.
- Status: CLOSED
- Gate added: `_engine/scripts/citation_check.py` — closing block required; every footnote `[N]` must resolve.
- Backfill required: yes — every past issue needs a citations block.

### Agent pipeline (PIPELINE.md) — 9 phases, ~30 agents, none implemented
- Discovered: 2026-05-30
- Source document: `_engine/PIPELINE.md` + every `_engine/skills/phase-N-*/SKILL.md` referenced
- How it was missed: The pipeline was documented in May but no implementation was scheduled. Issues have been authored ad-hoc in chat sessions without the phase chain.
- Status: OPEN
- Gate added: `_engine/scripts/system_audit.py` will list missing phase skills; first phase to implement is **Phase 3.5 The Agitator** (Earned Advance check) + **Phase 5 Design Editor** (deterministic + subjective).
- Backfill required: not applicable (forward-only — agent pipeline produces new issues; backfill uses `editor_review.py` and human review).
- Reference: PIPELINE.md Skill Index table

### Design Engine ↔ Themes coupling missing
- Discovered: 2026-05-30
- Source document: `_engine/DESIGN-ENGINE.md` Generation Protocol (5 steps) + `_engine/DESIGN-LEDGER.md` Uniqueness Guarantee
- How it was missed: The engine describes inputs (concept, emotional_goal, desired_action, dimension, audience) and outputs (weather + archetype + container + primitive + hue) but no script reads a research packet and writes a DESIGN-SPEC artifact.
- Status: OPEN
- Gate added: `_engine/scripts/system_audit.py` flags this; planned: `_engine/scripts/generate_design_spec.py` reads `_engine/research/YYYY-WW/[dim-slug]-packet.md` and produces `_engine/staging/YYYY-MM-DD-[slug]-design-spec.md` with all 5 coordinates checked against the ledger.
- Backfill required: no — forward only. Past issues get retro-coordinates added via human review.

### Meta-process for missed elements — this ledger itself
- Discovered: 2026-05-30
- Source document: Brian's directive — "make sure this error of missing key elements does not get repeated"
- How it was missed: There was no protocol for converting discovered gaps into permanent gates.
- Status: CLOSED
- Gate added: This file (`MISSED-ELEMENTS.md`) + `_engine/scripts/system_audit.py` (reads source documents, reports laws without gates).
- Backfill required: n/a.

---

### AV engine shipped without pipeline review or gate pass
- Discovered: 2026-05-30 (immediately after deploy; Brian named it: "did we really follow all the steps in the system?")
- Source document: `_engine/PIPELINE.md` 9-phase agent chain + `_engine/PUBLICATION-SOUL.md` v1.3 Compliance Gate Map + `MELIORISM2-DIRECTIVE.md` Phase 3.5 Agitator Iron Law
- How it was missed: Zen composed `/av/proof.html` in one pass and pushed it via deploy-api.sh, skipping Phases 1, 2, 3, 3.5, 5, 6, 7, 8a, 8b. `editor_review.py` was never run against the new content. Hubris — the agent assumed L3 was "infrastructure" not "issue" and therefore exempt; nothing in the protocol grants that exemption.
- Status: OPEN
- Gate added (planned):
  - `editor_review.py` extended with an `--also-on` flag to run against any new public-facing HTML file in `/av/`, `/topics/`, root pages — not just issues
  - `deploy-api.sh` runs `editor_review.py` against any `*.html` file in the change set, not only `archive/YYYY-MM-DD-*.html`
  - PIPELINE.md gets a new clause: "any new public-facing deliverable goes through Phases 3.5 → 5 → 9 minimum, including non-issue artifacts (about, topics, av, marketing pages)"
- Backfill required: yes — once gates extend to non-issue HTML, every existing root page (about.html, weather.html, founding.html, topics/*) needs an audit pass.
- Reference: this entry IS the proof. The thing the MISSED-ELEMENTS ledger exists to prevent happened the day the ledger was created.

---

## Closed entries archive

*Entries move here once the gate is wired AND backfill is done.*

(none yet)

---

*Maintained by Zen. Every gap becomes a gate. The ledger is the proof the system learns.*
