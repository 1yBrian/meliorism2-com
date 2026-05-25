# Meliorism2 Editorial Pipeline
*Master artifact chain · obra/superpowers-style · 2026-05-25*

---

## Core Principle

**Every stage produces a file. No stage completes without one.**

No agent claims completion with a verbal summary. The output artifact must exist at its designated path and be readable by the next stage before that stage begins. Reviewers do not trust prior agents' reports — they read the actual output file.

**Announce at start:** Every agent announces "I am running the [phase-name] skill" before doing anything.

---

## Artifact Chain

| Phase | Agent | Input | Output file | Path pattern |
|-------|-------|-------|-------------|--------------|
| 1 | Randomizer | Date, season, calendar | 33 influence factors | `_engine/research/YYYY-WW/00-factors.md` |
| 2 | Dimension Research ×9 | factors.md + dimension brief + last 4 issues | Research packet | `_engine/research/YYYY-WW/[dim-slug]-packet.md` |
| 3 | Editor | All packets + factors.md | Editorial decisions + rejections | `_engine/research/YYYY-WW/EDITORIAL-DECISIONS.md` + `REJECTED-THEMES.md` |
| 4 | Composing Agent ×7 | Editorial decision + packet | HTML draft | `_engine/staging/YYYY-MM-DD-[slug]-draft.html` |
| 5 | Review ×3 (parallel) | Draft HTML | Review notes | `_engine/staging/YYYY-MM-DD-[slug]-copy-review.md` + `-design-review.md` + `-marketing-review.md` |
| 6 | Stress Test ×4 (parallel) | Draft HTML + review notes | Stress test feedback | `_engine/staging/YYYY-MM-DD-[slug]-stress-test.md` |
| 7 | Bibliographer | Draft HTML + stress test | Citation-verified draft | `_engine/staging/YYYY-MM-DD-[slug]-bibliography.md` (annotates draft in place) |
| 8a | Design Amplification ×3 (parallel) | Citation-verified draft | Amplification notes | `_engine/staging/YYYY-MM-DD-[slug]-amplification.md` |
| 8b | Publicist (parallel to 8a) | Citation-verified draft | Social swipe file | `_engine/staging/YYYY-MM-DD-[slug]-swipe-file.md` |
| 9 | Deploy | Final HTML + all review files present | Live issue + Supabase row | `archive/YYYY-MM-DD-[slug].html` |

---

## Parallel vs Sequential

**Parallel (independent reads of same artifact — run simultaneously):**
- Phase 5: Copy Editor + Design Editor + Marketing Editor
- Phase 6: Reviewer 1 + Reviewer 2 + Reviewer 3 + Reviewer 4
- Phase 8a + 8b: Design Amplification + Publicist

**Sequential (next stage depends on prior output):**
- Phase 1 → Phase 2 (dimension agents need the factors file)
- Phase 3 → Phase 4 (composing agents need editorial selection)
- Phase 4 → Phase 5 (reviewers need the draft)
- Phase 5+6 resolved → Phase 7 (Bibliographer needs complete review notes)
- Phase 7 → Phase 8 (amplification works on citation-verified draft only)
- Phase 8 complete → Phase 9 (deploy requires all review files present)

**Decision criterion: dependency, not complexity.** If two agents read the same artifact without modifying it, they run in parallel. If one needs the other's output, they run in sequence.

---

## Gate Rules

### Phase 3 Gate — Rejection Standard
The Editor rejects a minimum of 2 packets every week. A week with zero rejections is a gate failure — the standard has slipped. Each rejection is documented in `REJECTED-THEMES.md` with a professional paragraph-length reason and a disposition (Revise / Archive / Develop as report).

### Phase 7 Gate — Citation Iron Law

> **NO CITATION IN THE FINAL HTML WITHOUT A VERIFIED SOURCE IN THE BIBLIOGRAPHY BLOCK.**
>
> The Bibliographer reads the actual HTML file. It does not trust the Composing Agent's claim that citations are present. It opens the file, counts the citations, checks each one against a named source, and flags any assertion without attribution.

### Phase 9 Gate — Deploy Iron Law

> **NO DEPLOY WITHOUT CONFIRMING TARGET IS `archive/YYYY-MM-DD-[slug].html`.**
>
> The deploy agent confirms the filename before the GitHub API call. `index.html` is the permanent landing page. Writing to it is a critical failure. Confirm the slug matches the editorial calendar entry. Confirm all review files are present at their designated paths before proceeding.

---

## Escalation Protocol

Any agent that cannot locate its required input file stops immediately and reports:

```
STATUS: BLOCKED
REASON: [input file] not found at [expected path]
REQUIRED: [what needs to exist before this agent can proceed]
DO NOT: guess, invent content, or proceed with a partial input
```

Guessing is worse than stopping. An agent that proceeds without its input produces output that poisons all downstream stages.

---

## File Naming Conventions

```
YYYY-WW    = ISO week (e.g., 2026-22 for week 22 of 2026)
YYYY-MM-DD = publish date (e.g., 2026-05-25)
[slug]     = kebab-case issue slug (e.g., the-barograph)
[dim-slug] = dimension kebab-case (e.g., somatic-body, brave-spaces, living-income)
```

---

## COOK's Weekly Check (3 questions)

1. Did any dimension agent produce a weak packet two weeks in a row? → Revise that agent's brief.
2. Did the design editor approve an entry screen that wouldn't pass the screenshot test? → Gate failure.
3. Did the bibliographer find uncited claims? → Trust failure. Trace to composing agent.

Logged at: `_engine/COOK-LOG.md` — weekly, 3 lines maximum.

---

## Skill Index

| Skill | File | Phase |
|-------|------|-------|
| phase-1-randomizer | `skills/phase-1-randomizer/SKILL.md` | 1 |
| phase-2-dimension-research | `skills/phase-2-dimension-research/SKILL.md` | 2 |
| phase-3-editorial-selection | `skills/phase-3-editorial-selection/SKILL.md` | 3 |
| phase-4-issue-composition | `skills/phase-4-issue-composition/SKILL.md` | 4 |
| phase-5-editorial-review | `skills/phase-5-editorial-review/SKILL.md` | 5 |
| phase-6-stress-test | `skills/phase-6-stress-test/SKILL.md` | 6 |
| phase-7-bibliographer | `skills/phase-7-bibliographer/SKILL.md` | 7 |
| phase-8-design-amplification | `skills/phase-8-design-amplification/SKILL.md` | 8a |
| phase-9-deploy | `skills/phase-9-deploy/SKILL.md` | 9 |
| the-plain-reader | `skills/the-plain-reader/SKILL.md` | Post-composition |
| the-publicist | `skills/the-publicist/SKILL.md` | 8b (parallel) |
| the-agitator | `skills/the-agitator/SKILL.md` | 3.5 + 5 |
