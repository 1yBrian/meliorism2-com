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

**What changed:** Clock changed from UTC to PT.
**Why:** UTC is not Brian's timezone. PT is.
**Carries forward:** YES
**Rule going forward:** All issue clocks show PT. Use `Intl.DateTimeFormat` with `timeZone:'America/Los_Angeles'`. Never UTC display in any issue. Label: `HH:MM:SS PT`.

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
**Rule going forward:** Every entry screen (Card 1) must include the emotional weather chip: `[emoji] [label] · learn more → /weather`. Low visual weight, fine-print register, positioned near the bottom of the entry overlay. Run emotional_weather_agent.py before Phase 8c to get the reading.

---

### 2026-05-29 — Issue 029: the-annotated-estimate

**What changed:** Delight Card (Card 8) missing — issue shipped with 7 cards.
**Why:** PUBLICATION-SOUL §Energy Archetypes and Delight Card spec were not in PUBLICATION-SOUL.md until today. Composing agent was building against v1.0 which did not include this requirement. SKILL.md had it but PUBLICATION-SOUL.md did not — contradiction caused the omission.
**Carries forward:** YES
**Rule going forward:** Every issue must have 8 cards. Card 8 is the Delight Card — no practitioner framing, no mechanism, something genuinely surprising, funny, beautiful, or worth knowing. Mandatory. An issue with 7 cards is incomplete. Do not deploy.

---

*Log grows downward. Never delete entries.*
