---
name: phase-5-editorial-review
description: Use when a draft HTML file exists at _engine/staging/YYYY-MM-DD-[slug]-draft.html. Three reviewers run in parallel — Copy Editor, Design Editor, and Marketing/Learning/Vocal Quality Editor — each with a single lens, each independent. Reviewers must not read each other's notes before filing.
---

# Phase 5: Editorial Review

**Announce at start:** "I am running the phase-5-editorial-review skill."

## Overview

Three parallel agents each receive the same draft independently and apply a single lens. Independence is the value — a reviewer who reads another reviewer's notes first loses their lens. **A design editor who passes an entry screen that wouldn't stop a practitioner scrolling past it has committed a gate failure, not filed a minor note.**

## When to Use

**Always:**
- `_engine/staging/YYYY-MM-DD-[slug]-draft.html` exists
- All three review output files do not yet exist for this slug
- The three reviewers operate simultaneously — do not sequence them

**Exceptions:**
- If any review file already exists for this slug, stop. Do not overwrite. Report to Brian.
- If the draft file does not exist, stop. Do not fabricate a review.

## Input

- `_engine/staging/YYYY-MM-DD-[slug]-draft.html` — the draft to review

Each reviewer reads the draft independently. No reviewer reads another reviewer's output file before filing their own.

## Process

Three agents run in parallel. Each follows only their lens.

---

### Copy Editor Lens

**Single lens:** Voice, language precision, accessibility standards, no prohibited content.

**Check list — flag every violation:**

1. **Meliorist 2.0 voice** — practitioner-to-practitioner register. Not academic. Not casual. Not corporate.
2. **Help Rule** — the word "help" must not appear unless Brian is making a genuine personal request. Flag every instance. Precise verb substitutes: support, build, execute, advise, deliver, act, solve, research.
3. **Acronyms** — every acronym must be spelled out on first use. Format: Full Name (Acronym), then acronym alone.
4. **Reader as agent** — no copy that implies something is wrong with the reader. The reader is the agent. Life creates friction. The work is removal, not repair. Flag any sentence that implies deficit.
5. **Minimum contrast** — body text must be minimum #2c2c2c on cream (#faf8f5). Flag any lighter value.
6. **Prohibited content** — no community sections, no newsletter prompts, no placeholder content (any text containing "goes here," "TBD," "placeholder," or inline HTML comments intended as content substitutes).

**Output format for copy-review.md:**

```
## Copy Review — YYYY-MM-DD-[slug]

### Voice Violations
[List each instance with card number and quoted text, or NONE]

### Help Rule Violations
[List each instance with card number and quoted text, or NONE]

### Acronym Violations
[List each instance, or NONE]

### Reader-as-Agent Violations
[List each instance with card number and quoted text, or NONE]

### Contrast Violations
[List each element and its color value, or NONE]

### Prohibited Content
[List each instance, or NONE]

### Overall Copy Verdict
PASS / REVISE — [one sentence summary]
```

---

### Design Editor Lens

**Single lens:** Entry screen stopping power, format metaphor quality, image brief quality, structural architecture compliance, visual hierarchy.

**Check list — flag every failure:**

1. **Entry screen test** — Does the entry screen place the reader inside the environment before a word of content appears? Would a busy practitioner stop scrolling for it? If the answer is no to either question, this is a gate failure, not a note.
2. **Format metaphor** — Does the format feel like a space, not a label? A "Field Report" should feel like the field. A "Debrief Protocol" should feel like a debrief room. If it feels like a content label, flag it.
3. **Image brief quality** — Is the image brief worth generating? Apply the screenshot test: if you ran the DALL-E prompt right now, would the result be an environment worth stepping into?
4. **Dark section-break bands** — Are dark bands present between major sections? If absent, flag.
5. **Ken Burns + gradient overlay** — Is the entry screen image wired with Ken Burns effect and gradient overlay? If absent or broken, flag.
6. **sections-rail architecture** — Is the draft horizontal-swipe with `sections-rail` and `goTo(index)`? If it is a vertical scroll article, this is a structural failure — flag immediately.

**Output format for design-review.md:**

```
## Design Review — YYYY-MM-DD-[slug]

### Entry Screen
PASS / GATE FAILURE — [specific note]

### Format Metaphor
PASS / FAIL — [specific note]

### Image Brief
PASS / FAIL — [specific note, include the brief text being evaluated]

### Section-Break Bands
PRESENT / ABSENT

### Ken Burns + Gradient Overlay
WIRED / MISSING

### sections-rail Architecture
CORRECT / STRUCTURAL FAILURE

### Overall Design Verdict
PASS / REVISE / REBUILD — [one sentence summary. REBUILD if sections-rail is missing or entry screen is a gate failure.]
```

---

### Marketing / Learning / Vocal Quality Editor Lens

**Single lens:** Practitioner utility, scenario quality, shareability, vocal consistency, the 90-Second Signal.

**Check list — score and flag:**

1. **Practitioner utility** — Is the concept practitioner-usable this week? Not "eventually useful." This week, in a real room.
2. **WWYD scenario specificity** — Does the scenario name a setting, a friction, a decision point? Would a practitioner recognize this room? Generic scenarios fail this test.
3. **90-Second Signal** — If present: does it read as a complete standalone shareable unit? Would a busy practitioner forward it to a colleague without the full issue? If absent: note the absence (not a failure unless the Agitator's brief required it).
4. **Vocal consistency** — Is the voice consistent across all 7 cards? Not academic on cards 2–3 and casual on card 7. Consistent practitioner register throughout.
5. **Forward test** — Would a busy practitioner forward this issue to a colleague this week? If the answer is uncertain, name what is blocking it.

**Engagement score:** Rate 1–10. 7+ is publish-ready. 5–6 requires specific improvement before submission. Below 5 is a rejection recommendation — name what would need to change.

**Output format for marketing-review.md:**

```
## Marketing / Learning / Vocal Quality Review — YYYY-MM-DD-[slug]

### Practitioner Utility
[Assessment — is it usable this week? Specific evidence.]

### WWYD Scenario
PASS / FAIL — [quote the scenario, note what passes or fails]

### 90-Second Signal
PRESENT AND PASSES / PRESENT AND FAILS / ABSENT — [one sentence]

### Vocal Consistency
CONSISTENT / INCONSISTENT — [if inconsistent, name the cards where it breaks]

### Forward Test
YES / UNCERTAIN / NO — [one sentence on what enables or blocks it]

### Engagement Score
[1–10] — [2–3 sentences of specific improvement notes if below 7]

### Overall Marketing Verdict
PUBLISH-READY / REVISE / REJECT — [one sentence summary]
```

---

### Step: File All Three Reviews

Write all three review files simultaneously. Reviewers do not read each other's files before or during their review.

## Output

- `_engine/staging/YYYY-MM-DD-[slug]-copy-review.md`
- `_engine/staging/YYYY-MM-DD-[slug]-design-review.md`
- `_engine/staging/YYYY-MM-DD-[slug]-marketing-review.md`

All three are required before Phase 6 may proceed.

## Common Mistakes

**Reviewers reading each other's notes**
- Problem: The Copy Editor reads the Design Editor's file first, then adjusts their findings to align.
- Fix: Each reviewer files independently. The value of three lenses is that they catch different things. A reviewer who reads another reviewer's notes first produces a less useful review, not a more coherent one.

**Design editor treating a gate failure as a note**
- Problem: Entry screen doesn't stop a scrolling practitioner. Design editor writes "consider strengthening the entry screen image."
- Fix: Gate failure is gate failure. The verdict is REBUILD, not REVISE. Name it plainly.

**Marketing reviewer giving a high score without naming what earns it**
- Problem: "Engagement score: 8. This is a strong issue."
- Fix: Score 7+ requires at least one sentence of specific evidence. What specific element makes this practitioner-usable this week?

**Copy reviewer flagging style preferences as violations**
- Problem: Flagging sentence length or paragraph structure as a Meliorist 2.0 voice violation.
- Fix: Voice violations are specific: the Help Rule, reader-as-deficit framing, academic register. Style preferences are not violations.

## Red Flags — STOP

- Draft file does not exist at the stated path — stop, do not fabricate a review
- Any review file already exists for this slug — stop, report to Brian
- Design verdict is PASS but sections-rail architecture is marked STRUCTURAL FAILURE — contradiction, re-examine
- All three verdicts are PASS but engagement score is below 5 — contradiction, re-examine

## Iron Law

> **THREE INDEPENDENT LENSES. A REVIEWER WHO READS ANOTHER REVIEWER'S NOTES BEFORE FILING HAS LOST THEIR LENS AND THEIR VALUE TO THIS PROCESS.**
