---
name: day-before-publish-review
description: Run the evening before publish date. Activates the Calendar Hook — weaves today's world (news, events, global happenings) into the completed draft to make it timely. Also runs the tone-deafness gate and a mandatory elements gate that blocks deployment if any required structural element is missing. Runs after Phase 8, before Phase 9 (Deploy).
---

# Day-Before-Publish Review

**Announce at start:** "I am running the day-before-publish-review skill."

## Overview

The issue was researched and composed days or weeks ahead of publish date. That is the right order — research and drafting should never be rushed by proximity to deadline. But the world changes daily. This review activates the Calendar Hook at the last possible moment, weaving today's world into a completed draft without rebuilding it.

This is not a redesign. It is a precision weave. The structure stays. The thesis stays. One to three timely threads are added, or the existing content is re-framed to land against today's backdrop.

This review also runs the Mandatory Elements Gate before any timeliness work begins. If any element in the gate fails, deployment is blocked. The gate must fully pass before the Calendar Hook runs.

## When to Use

**Always:**
- The draft has passed Phase 8 (Design Amplification + Publicist)
- Publish date is tomorrow
- Phase 9 (Deploy) has not yet run

**Exceptions:**
- Do not run if the draft has not passed Phase 8 — the order is not optional
- If no timely threads can be found that genuinely connect, document that and proceed without forcing one

## Input

- Completed draft HTML at `_engine/staging/YYYY-MM-DD-[slug]-draft.html`
- `_engine/CHANGE-LOG.md` — read in full before opening the draft HTML
- Today's date and tomorrow's publish date
- Live signal scan: what is happening in the world today

---

## MANDATORY ELEMENTS GATE

**Run this gate before any other step. Each check is PASS or FAIL. One FAIL blocks the entire deployment. Report all failures together — do not stop at the first one.**

Open the draft HTML at `_engine/staging/YYYY-MM-DD-[slug]-draft.html` and evaluate each gate in order.

---

### Gate 1 — Eight Cards

**What to check:** The `.sections-rail` element has a width of exactly `800%` or `calc(100% * 8)`, and exactly 8 `.card` or `.card-panel` elements are present in the DOM.

**PASS:** 8 cards confirmed in the sections-rail.

**FAIL:** Fewer or more than 8 cards. Report: "GATE 1 FAIL — Card count is [N], expected 8. Sections-rail width does not match an 8-card layout."

---

### Gate 2 — Delight Card Present and Off-Brief

**What to check:** The final card (Card 8, index 7) exists and contains content that is genuinely off-brief — no practitioner framing, no clinical language, no skill-building structure. It is a surprise. It delights. It exists for no reason except that it is worth existing.

**PASS:** Card 8 is present. Its content is not framed as professional development. It could not be mistaken for any other card in the issue.

**FAIL — Card absent:** "GATE 2 FAIL — No Delight Card found. Card 8 is missing from the sections-rail."

**FAIL — Card present but on-brief:** "GATE 2 FAIL — Card 8 exists but reads as practitioner content. Delight Card must be genuinely off-brief — no professional framing, no skill arc, no clinical register."

---

### Gate 3 — Emotional Weather Chip

**What to check:** An Emotional Weather chip is present on Card 1 (entry screen) or Card 2. It must contain: an emoji, a weather label, and a link to `/weather`. Accepted formats: `[emoji] [label] · learn more →` linking to `/weather`, or a `.weather-chip` or `.weather-block` element with equivalent content.

**PASS:** Chip found with emoji, label, and /weather link on Card 1 or Card 2.

**FAIL:** "GATE 3 FAIL — Emotional Weather chip missing. Required: [emoji] [label] · learn more → /weather on Card 1 or Card 2. Neither a .weather-chip element nor equivalent inline markup was found."

---

### Gate 4 — Energy Archetype Assigned

**What to check:** The HTML metadata comments include `<!-- meliorism2:energy: [archetype] -->` with a populated value, OR the EDITORIAL-DECISIONS.md file for this issue names a specific energy archetype.

**PASS:** Energy archetype is named in metadata comments or EDITORIAL-DECISIONS.md.

**FAIL:** "GATE 4 FAIL — Energy archetype not assigned. Add `<!-- meliorism2:energy: [archetype] -->` to the HTML metadata block or confirm assignment in EDITORIAL-DECISIONS.md before deploying."

---

### Gate 5 — Etymology Section Present

**What to check:** An etymology block is present in the HTML. It must appear before the bibliography. Accepted locations: Card 6, Card 7, or any card labeled Roots, Application, or equivalent. The block must contain a Latin or Greek root with 2–3 sentences of context. Look for `<h3>Etymology</h3>` or equivalent heading.

**PASS:** Etymology heading and body found before the bibliography section.

**FAIL:** "GATE 5 FAIL — Etymology section missing. Required: Latin or Greek root with 2–3 sentences, positioned before the bibliography, on Card 6 or Card 7 (Roots or Application)."

---

### Gate 6 — PT Clock (Not UTC)

**What to check:** The JavaScript clock implementation uses `Intl.DateTimeFormat` with `timeZone: 'America/Los_Angeles'`. The clock label reads `HH:MM:SS PT` or equivalent Pacific Time label. No UTC display is present anywhere in the HTML.

**PASS:** Clock uses America/Los_Angeles timezone. Label confirms PT. No UTC reference found.

**FAIL:** "GATE 6 FAIL — Clock is not PT. Clock must use `Intl.DateTimeFormat` with `timeZone: 'America/Los_Angeles'` and display a PT label. UTC display is not acceptable."

---

### Gate 7 — Mobile Font Floor

**What to check:** A `@media (max-width: 640px)` block is present in the CSS that sets `font-size: 1rem !important` (or equivalent 16px floor) on all utility text elements. Required selectors to cover: `.date-tag`, `.issue-format-badge`, `.section-number`, and all stamp/label/utility text elements.

**PASS:** Mobile breakpoint block found. All required selectors confirmed with 1rem floor.

**FAIL:** "GATE 7 FAIL — Mobile font floor missing or incomplete. Required: `@media (max-width: 640px)` block with `font-size: 1rem !important` covering `.date-tag`, `.issue-format-badge`, `.section-number`, and all utility text. Missing selectors: [list them]."

---

### Gate 8 — Footer Bar

**What to check:** The footer contains exactly three navigation links: LIBRARY (linking to `/archive/index.html` or `/archive/`), WEATHER (linking to `/weather`), and HOME (linking to `/` or `index.html`). No static text labels in place of links. All three must be anchor elements.

**PASS:** Footer contains all three links — LIBRARY, WEATHER, HOME — as anchor elements.

**FAIL:** "GATE 8 FAIL — Footer bar incomplete. Required: three anchor links labeled LIBRARY · WEATHER · HOME. Missing or non-linked: [list what is absent or broken]."

---

### Gate 9 — Last Card Navigation

**What to check:** The `goTo()` function (or equivalent navigation handler) redirects to `/archive/index.html` when the navigation index reaches or exceeds `CARDS.length`. The nav-next button on the final card is labeled `← LIBRARY` in amber styling. It is never disabled — it always routes to the library.

**PASS:** Final card nav-next routes to `/archive/index.html`. Label is `← LIBRARY`. Button is never disabled.

**FAIL:** "GATE 9 FAIL — Last card navigation broken. `goTo()` must redirect to `/archive/index.html` at `index >= CARDS.length`. Nav-next on final card must be labeled `← LIBRARY` in amber. It must never be disabled. Current state: [describe what was found]."

---

### Gate 10 — Hero Image Position on Card 0

**What to check:** Card 0 (The Signal / entry screen) opens with the hero image as the first child of `.card-inner`. The metadata block (date, dimension, format badge, etc.) follows the hero image in DOM order. The hero image is full-bleed or full-width above the metadata.

**PASS:** Hero image is first child of `.card-inner` on Card 0. Metadata follows.

**FAIL:** "GATE 10 FAIL — Hero image position wrong on Card 0. Hero image must appear as the first child of `.card-inner`, above all metadata. Current DOM order has [describe what was found] before the image."

---

### Gate 11 — Anti-Discount Framing

**What to check:** If the issue covers pricing, rates, income, fees, or value negotiation in any card — search for the phrases "accept at a loss," "reduce the rate," "discount," "lower your price," "work for less," or any equivalent framing that positions the practitioner as surrendering value. None of these may appear.

Valid pricing register: add value to justify the rate, adjust scope to fit the budget, or decline the engagement. These are the only three options the issue may present.

**PASS:** No discount framing found. OR: Issue contains no pricing content — gate passes by non-applicability (document this).

**FAIL:** "GATE 11 FAIL — Discount framing detected. The phrase '[exact phrase found]' appears on Card [N]. Replace with add-value, adjust-scope, or decline framing. Practitioners do not reduce rates — they negotiate scope or walk."

---

### Gate 12 — CHANGE-LOG Carries Forward Applied

**What to check:** Open `_engine/CHANGE-LOG.md`. Read every entry marked `CARRIES FORWARD`. For each carry-forward entry, confirm that the current draft HTML reflects the rule it codifies. This gate does not check every CHANGE-LOG entry — only those explicitly marked as carries-forward standing rules.

**PASS:** Every CARRIES FORWARD entry has been read. Each rule is reflected in the current draft. Document which entries were checked.

**FAIL:** "GATE 12 FAIL — CHANGE-LOG carry-forward not applied. The following CARRIES FORWARD rules are not reflected in the current draft: [list entry titles and what is missing]. Resolve before proceeding."

---

### Gate Report

After running all 12 gates, produce a gate report in this format before continuing:

```
MANDATORY ELEMENTS GATE — [issue slug] — [date]

Gate 1 — Eight Cards:          [PASS / FAIL]
Gate 2 — Delight Card:         [PASS / FAIL]
Gate 3 — Emotional Weather:    [PASS / FAIL]
Gate 4 — Energy Archetype:     [PASS / FAIL]
Gate 5 — Etymology:            [PASS / FAIL]
Gate 6 — PT Clock:             [PASS / FAIL]
Gate 7 — Mobile Font Floor:    [PASS / FAIL]
Gate 8 — Footer Bar:           [PASS / FAIL]
Gate 9 — Last Card Nav:        [PASS / FAIL]
Gate 10 — Hero Image Position: [PASS / FAIL]
Gate 11 — Anti-Discount:       [PASS / FAIL]
Gate 12 — CHANGE-LOG CF:       [PASS / FAIL]

OVERALL: [ALL PASS — proceed to Calendar Hook] / [BLOCKED — [N] gates failed]
```

If any gate fails: **STOP. Do not proceed to the Calendar Hook or any subsequent step. Report all failures. Fix them. Re-run the gate before continuing.**

If all gates pass: proceed to Step 1 below.

---

## Process

### Step 1: The Calendar Hook Scan

Scan for:
- **Exact-date anchors** — Is today or tomorrow a holiday, anniversary, cultural moment, or observance anywhere in the world?
- **Active news** — What stories are practitioners likely to have seen, heard, or felt this week? Not the news cycle for its own sake — the signal that is already inside the practitioner's head when they open the issue.
- **Global events** — What is happening beyond the practitioner's home country that their clients might be carrying? A ceasefire. An election result. A climate event. A major death or celebration. The practitioner holds the room; the room holds the world.
- **Field events** — Any conference concluding, credential deadline, professional moment landing this week?
- **Seasonal / atmospheric** — What is the body registering right now? Late afternoon light in the Northern Hemisphere. First real heat in the South. The smell after rain.

Document findings in a brief list before touching the draft.

### Step 2: The Tone-Deafness Gate

Ask: **Is there anything happening in the world today that makes the current draft's tone wrong?**

This is a different question from timeliness. It is a harm-avoidance check.

If a mass casualty event occurred in the last 48 hours:
- The issue does not lead with the usual energy
- Add one line of acknowledgment in the entry screen: spare, human, not performative
- The practitioner who reads this is also holding that in their room

If the draft's tone is actively discordant with the day's weight — an upbeat aquatic survey on the morning after a significant loss — adjust the entry screen register before deploying.

**The test:** Would a thoughtful practitioner reading this at 6 AM, already aware of what happened in the world, feel that this issue noticed? Not that it dwelled — that it noticed.

### Step 3: Weave, Don't Rebuild

Find one to three places in the existing draft where a timely thread can be woven in without restructuring. Options:

- **Entry screen copy** — A line in the pull quote, subtitle, or CTA that anchors the issue to today
- **The Phenomenon card** — "This week, as [event] unfolds..." frames the phenomenon as live, not archival
- **Application/WWYD card** — The scenario can reference what practitioners are navigating in their rooms right now because of what is happening outside
- **A single inline callout** — A bracketed observation, set apart visually: *"This week: [one sentence on world context]."* Not a paragraph — a sentence.

Do not add a card. Do not restructure the navigation. Do not rewrite the thesis. The draft is finished — this step sharpens its edge.

### Step 4: Global Awareness Check

Read the final draft and ask: does this issue exist only in one country? The readership holds rooms on every continent. If every reference is US-centric, add one international anchor — a happening, a practitioner context, a cultural moment from elsewhere.

This is not tokenism. It is accuracy. The work these practitioners do is not American. The science they use was not discovered in one place. The problems they face are not unique to one economy.

### Step 5: Run the Three Simultaneous Criteria

Before filing:

1. **Working knowledge expands** — Does the practitioner gain a usable mechanism? Still true after the weave?
2. **Visual environment genuinely surprises** — Did the weave preserve the format's distinctiveness or blur it with generic news peg?
3. **Covert curriculum advances** — Which of the five capacities (agency, systems thinking, emotional intelligence, somatic literacy, economic discernment) does today's version plant? Name it.

If criterion 3 cannot be named, the weave was decorative. Either name it or remove it.

### Step 6: File the Review Note

Write one paragraph to `_engine/staging/YYYY-MM-DD-[slug]-day-before-review.md`:
- Gate report summary (all 12 gates — PASS/FAIL counts, any fixes applied)
- What timely threads were found
- What was woven in (or why nothing was added)
- Whether the tone-deafness gate passed
- Which covert curriculum capacity the issue plants today

## Output

- Modified draft HTML (in place — same file, Phase 9 reads from the same path)
- `_engine/staging/YYYY-MM-DD-[slug]-day-before-review.md` (includes gate report)

## Common Mistakes

**Running the Calendar Hook before the Mandatory Elements Gate**
- Problem: Timeliness work begins before structural integrity is confirmed.
- Fix: The gate runs first. Every time. The Calendar Hook does not start until all 12 gates pass.

**Treating gate failures as suggestions**
- Problem: Noting a gate failure and continuing anyway.
- Fix: One FAIL blocks everything. Stop. Fix. Re-run the gate. Then proceed.

**Forcing a news peg that doesn't fit**
- Problem: Adding a reference to a world event because it happened, not because it connects.
- Fix: If the connection requires explaining, it is not a connection. Remove it and document that no genuine thread was found.

**Rewriting the thesis under cover of "timeliness"**
- Problem: Using the calendar hook as an excuse to revisit editorial decisions.
- Fix: The thesis is locked. The weave is a thread, not a reframe. If the draft's thesis feels wrong against today's world, that is a Phase 3 failure — escalate to Brian rather than patching it here.

**Ignoring the global dimension**
- Problem: Every timely reference is US-centric.
- Fix: Practitioners hold rooms on every continent. Name one international happening, context, or anchor.

**Treating the tone-deafness gate as optional**
- Problem: Skipping it because "nothing major happened."
- Fix: Run it every time. The check takes 30 seconds. The cost of deploying a tone-deaf issue is not 30 seconds.

**Skimming CHANGE-LOG for carries-forward**
- Problem: Reading only recent entries or assuming prior sessions applied all rules.
- Fix: Read CHANGE-LOG in full before opening the draft. Every CARRIES FORWARD entry must be verified against the current draft. Not assumed. Verified.

## Red Flags — STOP

- The draft has not passed Phase 8 — do not run this review, return it to the correct phase
- Any of the 12 Mandatory Elements Gates fails — stop, fix all failures, re-run the gate before proceeding
- A major world event in the last 48 hours has not been addressed in the tone-deafness check — stop, address it
- The covert curriculum capacity cannot be named after the weave — the weave was decorative, remove it or find the real connection

## Iron Laws

> **THE MANDATORY ELEMENTS GATE RUNS BEFORE THE CALENDAR HOOK. ALL 12 GATES MUST PASS. ONE FAIL BLOCKS THE DEPLOYMENT.**

> **THE ISSUE WAS BUILT AHEAD. THIS STEP MAKES IT TODAY'S. ONE TO THREE THREADS. THE STRUCTURE DOES NOT MOVE.**
