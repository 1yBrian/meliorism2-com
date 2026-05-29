# Meliorism2 Change Log
*Post-publish corrections to live issues. Every entry marked CARRIES FORWARD is inherited by all future issues automatically.*
*Composing agents read this at Step 0 before drafting.*
*Updated: 2026-05-29*

---

## How to Use

**Composing agents (Phase 4 Step 0):** Read every entry marked `CARRIES FORWARD`. These are non-negotiable. They represent corrections already paid for once — do not make the reader pay twice.

**After any post-publish fix:** Add an entry here before closing the session. Format below.

---

## Entry Format

```
### [DATE] — Issue [NNN]: [slug]
**What changed:** [one sentence]
**Why:** [one sentence — what was wrong]
**Carries forward:** YES / NO
**Rule going forward:** [if YES — the standing instruction]
```

---

## Log

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Clock changed from UTC to PT on Issue 029 (theme: time/labor documentation).
**Why:** UTC is not Brian's timezone. PT is. However: clocks should only appear in issues where time is part of the theme or format concept.
**Carries forward:** NO — corrected 2026-05-29
**Rule going forward:** Do NOT include a clock in every issue. A clock is a design element, not a mandatory structural element. Include it only when the issue's theme relates to time, timing, scheduling, or temporal awareness. When a clock IS included, it must show PT using `Intl.DateTimeFormat` with `timeZone:'America/Los_Angeles'`. Never UTC. The mandatory clock in Phase 8c gate is removed — see Phase 8c update.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Mobile font floor added — all stamp/label text set to minimum 1rem (18px) on mobile.
**Why:** 0.8rem elements at 14.4px violate PUBLICATION-SOUL mobile minimum of 16px.
**Carries forward:** YES
**Rule going forward:** All issues must include a mobile breakpoint block enforcing 1rem floor on `.date-tag`, `.issue-format-badge`, `.section-number`, `.highlight-label`, `.sb-label`, `.sb-clock`, `.sb-logo`, `.progress-label`, `.entry-stamp`, `.entry-enter`, `.citation`, and all utility/meta text. Copy the block from Issue 029.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Hero image moved above metadata on Card 0 — full-bleed, no border, flush to edges.
**Why:** Image buried below title/date/badge block made Card 0 look identical to other issues. Image-first creates immediate visual differentiation.
**Carries forward:** YES
**Rule going forward:** Card 0 (The Signal) always opens with the hero image full-bleed, then metadata. Image is the first thing the reader sees after the entry screen, not the title.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Last card `→` now navigates to archive instead of disabling. Label changes to "← LIBRARY" on final card.
**Why:** Disabling the forward button on the last card left the reader with no exit path. The forward momentum must always continue — into the archive if nowhere else.
**Carries forward:** YES
**Rule going forward:** In `goTo()`, when `index >= CARDS.length`, redirect to `/archive/index.html`. Final card `nav-next` shows "← LIBRARY" in amber. Never disabled.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Footer bar updated — added WEATHER link, HOME link, removed "TODAY'S BRIEFING ← CURRENT" static label.
**Why:** Weather page was built and never linked from any issue. The static label provided no navigation value.
**Carries forward:** YES
**Rule going forward:** Every issue footer bar contains: `← LIBRARY` · `WEATHER` · `HOME`. No static labels.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Etymology section added before bibliography on last card.
**Why:** Etymology was specified in Phase 4 SKILL.md (Card 6: Roots) but not built into this issue.
**Carries forward:** YES (already in SKILL.md — this was a composition failure, not a system gap)
**Rule going forward:** Card 6 (Roots/Application) always includes etymology before bibliography. Latin/Greek root of the core concept word. Connects the mechanism to its language origin. 2–3 sentences maximum.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** "Accept at a loss" framing removed from Edge Cases. Replaced with add-value/bonus approach.
**Why:** Brian's standing philosophy: never discount. Add value instead. The issue was contradicting its author's practice.
**Carries forward:** YES
**Rule going forward:** Any Living Income issue (or any issue that touches pricing/rate) must not include "accept at a loss" or "discount" as a legitimate option. The three options for a below-budget request are always: (1) add value/bonus to justify the existing rate, (2) adjust scope while holding rate per unit, (3) decline. Never reduce the rate for the same work.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Emotional Weather Report missing from entry screen.
**Why:** PUBLICATION-SOUL §Emotional Weather was not written until today (v1.2). Cannot retroactively fix a live issue.
**Carries forward:** YES
**Rule going forward:** Every entry screen (Card 1) must include the emotional weather chip: `[emoji] [label] · learn more → /weather`. Low visual weight, fine-print register, positioned near the bottom of the entry overlay. The composing agent sets it during Phase 4 — no separate script, no API call.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Delight Card (Card 8) missing — issue shipped with 7 cards.
**Why:** PUBLICATION-SOUL §Energy Archetypes and Delight Card spec were not in PUBLICATION-SOUL.md until today. Composing agent was building against v1.0 which did not include this requirement. SKILL.md had it but PUBLICATION-SOUL.md did not — contradiction caused the omission.
**Carries forward:** YES
**Rule going forward:** Every issue must have 8 cards. Card 8 is the Delight Card — no practitioner framing, no mechanism, something genuinely surprising, funny, beautiful, or worth knowing. Mandatory. An issue with 7 cards is incomplete. Do not deploy.

---

### 2026-05-29 — Issue 029: the-annotated-estimate (post-publish patch)

**What changed:** Added McKinsey November 2025 outcome-based pricing research to Card 3 (Evidence). Reframed Card 4 "Value-Based Pricing" section to lead with results-over-hours philosophy.
**Why:** The issue framed the practitioner's pricing problem as "how do I justify my hours." Brian's philosophy is that the question is "how do I create the results the client wants." McKinsey's shift to outcome-based fees (25% of global revenue, Nov 2025) provides external validation. The premium investment principle was absent.
**Carries forward:** YES
**Rule going forward:** Any issue touching pricing, rates, or income — particularly Living Income dimension — must include: (1) results-over-hours framing (what outcomes will you create?), (2) pricing principle: good price between real worth and client budget; best price is often a premium reach, (3) premium dividend: done right, on time, quality. Discounting is never framed as an option. McKinsey 2025 is a citeable source for any issue on professional service pricing.

---

### 2026-05-29 — SYSTEM: PUBLICATION-SOUL.md
**What changed:** §Energy Archetypes and §Emotional Weather added to PUBLICATION-SOUL.md (v1.2).
**Why:** v1.0 was missing these sections entirely — SKILL.md referenced them as requirements but the canonical spec document did not define them, creating an unresolvable contradiction for composing agents.
**Carries forward:** YES
**Rule going forward:** PUBLICATION-SOUL.md must carry a version header. Any time PUBLICATION-SOUL.md is updated, the Phase 4, Phase 5, and Phase 9 checklists must be reviewed and updated in the same session before closing. Phase 4 Step 0 must confirm the version header is present before drafting begins — if absent, stop and report to Brian.

---

### 2026-05-29 — Issue 028 + Issue 029: SYSTEM
**What changed:** Delight Card (Card 8) retroactively identified as missing from Issues 028 and 029.
**Why:** Phase 4 SKILL.md listed Card 8 in the card table but the Iron Law and Output section still declared "7 cards" — an internal contradiction that composing agents resolved in favor of the lower number.
**Carries forward:** YES
**Rule going forward:** Phase 4 SKILL.md Iron Law and Output section must read "8 cards." Phase 9 pre-flight must verify: `[ ] sections-rail CSS width is 800% and width:calc(100%/8) — confirming 8 cards in DOM`. An issue with 7 cards fails pre-flight and does not deploy.

---

### 2026-05-29 — Issue 028 + Issue 029: SYSTEM
**What changed:** Emotional Weather chip retroactively identified as missing from Issues 028 and 029.
**Why:** §Emotional Weather did not exist in PUBLICATION-SOUL.md until v1.2. Phase 4 SKILL.md listed it as mandatory but no phase had a checkable output criterion for its presence.
**Carries forward:** YES
**Rule going forward:** Phase 5 design-review checklist must include: `[ ] Emotional Weather chip present on entry screen — emoji + label + /weather link`. Phase 9 pre-flight must include: `[ ] .weather-chip or .weather-block element present on Card 1`. Run emotional_weather_agent.py before Phase 8c to obtain the reading.

---

### 2026-05-29 — Issue 028 + Issue 029: SYSTEM
**What changed:** Energy archetype metadata comment retroactively identified as missing from Issues 028 and 029.
**Why:** PUBLICATION-SOUL §Energy Archetypes did not exist until v1.2. No phase skill file listed `<!-- meliorism2:energy: -->` as a required metadata comment, and Phase 9 pre-flight metadata checklist did not include it.
**Carries forward:** YES
**Rule going forward:** Phase 4 SKILL.md metadata comment block must include `<!-- meliorism2:energy: [archetype] -->`. Phase 9 pre-flight metadata checklist must include: `[ ] meliorism2:energy: comment present and populated with a named archetype`.

---

### 2026-05-29 — SYSTEM: Phase 4 input list
**What changed:** LEARNING-LOG.md §Editorial Philosophy — Standing Principles added as a required Phase 4 Step 0 input.
**Why:** The Results Principle, Premium Principle, and Anti-Discount Rule existed in Brian's practice but were not a pipeline gate — composing agents had no instruction to read the Editorial Philosophy section before drafting, so pricing-register violations reached publication.
**Carries forward:** YES
**Rule going forward:** Phase 4 SKILL.md Step 0 must include: "Read LEARNING-LOG.md §Editorial Philosophy — Standing Principles. For any issue touching pricing, rates, income, or the Living Income dimension, the Results Principle, Premium Principle, and Anti-Discount Rule are mandatory. McKinsey 2025 (Birshan, Nov 2025) is a citable source for outcome-based pricing."

---

### 2026-05-29 — SYSTEM: CHANGE-LOG.md did not exist before Issue 029 session
**What changed:** CHANGE-LOG.md created. All post-publish corrections to Issues 027, 028, and 029 documented for the first time.
**Why:** No change log existed before tonight — post-publish fixes to Issue 027 and earlier could not carry forward to later issues because there was no record of them.
**Carries forward:** YES
**Rule going forward:** Phase 4 Step 0 must include CHANGE-LOG.md as a required input alongside LEARNING-LOG.md. Every composing agent reads all entries marked "Carries forward: YES" before drafting a single word. After any post-publish fix, an entry is added to CHANGE-LOG.md before the session closes.

---

### 2026-05-29 — SYSTEM: Phase 9 pre-flight checklist gaps
**What changed:** The following checks were absent from Phase 9 pre-flight and must be added: card count (8), energy archetype metadata, Emotional Weather chip, etymology block, footer link structure (LIBRARY · WEATHER · HOME), clock timezone (PT not UTC), mobile font floor block, goTo() library redirect on final card, Card 0 DOM order (image before metadata).
**Why:** Phase 9 pre-flight was not wired to PUBLICATION-SOUL.md as a dependency — when the spec changed, the pre-flight checklist was not updated, so every new requirement introduced after the checklist was written silently bypassed the final quality gate.
**Carries forward:** YES
**Rule going forward:** Phase 9 pre-flight must include all of the following before any deploy is permitted: `[ ] Card count: 8 cards in DOM (sections-rail width 800%)` · `[ ] meliorism2:energy: comment present and populated` · `[ ] Emotional Weather chip on Card 1` · `[ ] <h3>Etymology</h3> present on Roots/Application card` · `[ ] Footer bar: ← LIBRARY · WEATHER · HOME — no static labels` · `[ ] Clock uses Intl.DateTimeFormat timeZone:'America/Los_Angeles', label reads HH:MM:SS PT` · `[ ] @media(max-width:640px) mobile font floor block present` · `[ ] goTo() redirects to /archive/index.html at index >= CARDS.length, final nav-next labeled ← LIBRARY in amber` · `[ ] Card 0 DOM order: hero image is first child of .card-inner`.

---

*Log grows downward. Never delete entries.*
