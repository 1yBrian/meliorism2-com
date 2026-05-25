---
name: phase-3-editorial-selection
description: Use when all active dimension research packets for the week are present in _engine/research/YYYY-WW/. The Editor selects 7 themes for the week's publish schedule and rejects a minimum of 2 packets. Zero rejections is a gate failure.
---

# Phase 3: Editorial Selection

**Announce at start:** "I am running the phase-3-editorial-selection skill."

## Overview

The Editor receives all active packets and the 33 factors, selects exactly 7 themes (one per publish day, Monday through Sunday), and rejects a minimum of 2. **Minimum 2 rejections every week is non-negotiable. Zero rejections means the standard has slipped, not that all the work was excellent.**

## When to Use

**Always:**
- All active dimension packets for the week are present in `_engine/research/YYYY-WW/`
- `00-factors.md` is present and contains 33 items
- `EDITORIAL-DECISIONS.md` does not yet exist for this week

**Exceptions:**
- If fewer than 9 packets are present, stop. Report which dimensions are missing. Do not run a partial selection.
- If `EDITORIAL-DECISIONS.md` already exists, stop. Do not overwrite. Report to Brian.

## Input

- All active `[dim-slug]-packet.md` files in `_engine/research/YYYY-WW/`
- `_engine/research/YYYY-WW/00-factors.md`
- Last 4 published issues (dimension coverage map — do not repeat a dimension in consecutive weeks without editorial justification)

## Process

### Step 1: Read Everything

Read all packets and the 33 factors before making any selection decision. Do not select while reading. Complete the full read first.

Stop if any packet is missing a confidence rating, a WWYD scenario, or a suggested format. Flag the incomplete packet and do not proceed until it is filed correctly.

### Step 2: Apply the Six Selection Tests

For each packet, run all six tests. A packet must pass all six to be eligible for selection.

1. **Room test** — Does the concept land in a practitioner's physical room this week? Not someday. This week.
2. **Format test** — Is the suggested format genuinely new and environmental? Does it create a space, not a label?
3. **Scenario test** — Does the WWYD scenario feel specific and real? Does it name a setting, a friction, a decision point?
4. **Image test** — Does the image brief make you see the environment? Would a practitioner stop scrolling for it?
5. **Dimension balance test** — Does selecting this packet add a dimension not already covered this week?
6. **Random factor test** — Is there visible evidence that at least one factor from the random pool shaped this theme?

A packet that fails any test is a rejection candidate.

### Step 3: Select 7 Themes

Select exactly 7 packets. Assign each a publish date (Monday through Sunday). Distribution guidance:
- No two packets from adjacent dimensions on consecutive days if it can be avoided
- Spread confidence ratings — do not load all Strong packets into Monday–Wednesday
- At least one Weak-rated packet may be selected if it passes all six tests AND the editorial note explains why the concept is worth the development investment

### Step 4: Reject Minimum 2 Packets

Reject at least 2 of the active packets. This is not optional. For each rejected packet, assign a disposition:

- **Revise with notes** — strong concept, specific fixable problem, return to Phase 2
- **Archive as future issue** — concept is sound, timing is wrong, file for a future week
- **Archive as research report** — concept is too dense for an issue, develop as standalone PDF
- **Develop as standalone PDF** — concept warrants deeper treatment outside the issue format

### Step 5: Write EDITORIAL-DECISIONS.md

For each of the 7 selected themes, write one entry:

```
## [Dimension Name]

- **Format:** [format name]
- **Theme headline:** [one sentence]
- **Publish date:** [YYYY-MM-DD]
- **Why selected:** [2–3 sentences. Specific. Name the practitioner context and the week's relevance.]
- **Random factor influence:** [which of the 33 and how it shaped the selection]
```

### Step 6: Write REJECTED-THEMES.md

For each rejected packet, write one entry:

```
## [Dimension Name]

- **Proposed theme:** [the packet's theme headline]
- **Rejection reason:** [one professional paragraph. Name the specific editorial standard that failed. Not "not strong enough" — name the test.]
- **Editorial standard failed:** [Room test / Format test / Scenario test / Image test / Dimension balance test / Random factor test]
- **Disposition:** [one of the four options from Step 4]
```

### Step 7: Write the Files

Write both files to `_engine/research/YYYY-WW/`.

## Output

- `_engine/research/YYYY-WW/EDITORIAL-DECISIONS.md` — 7 selected themes with full editorial rationale
- `_engine/research/YYYY-WW/REJECTED-THEMES.md` — minimum 2 rejected packets with specific rejection reasons and dispositions

Both files are required. Phase 4 does not proceed without both.

## Common Mistakes

**Zero or one rejection**
- Problem: All packets selected, or only one cut because "they were all strong this week."
- Fix: The minimum is 2. If all packets appear strong, apply the six tests more rigorously. At least 2 will fail at least one test. The standard hasn't been applied hard enough.

**Vague rejection reason**
- Problem: "This theme wasn't strong enough for this week."
- Fix: Name the test. "This packet fails the Room test — the concept is relevant to the field broadly but does not land in a practitioner's physical context this week."

**No random factor influence documented**
- Problem: The EDITORIAL-DECISIONS.md entries contain no reference to any of the 33 factors.
- Fix: Every selected theme must name a specific factor and explain how it shaped the selection. If you cannot find one, the selection failed the Random factor test and should be reconsidered.

**Selecting a packet with a missing element**
- Problem: A packet without a confidence rating or WWYD scenario gets selected.
- Fix: Flag the incomplete packet before selection begins. Do not select it until it is complete.

## Red Flags — STOP

- Fewer than 9 packets present — report missing dimensions, do not run partial selection
- Zero rejections filed — gate failure, re-apply the six tests
- One rejection filed — insufficient, minimum is 2
- `EDITORIAL-DECISIONS.md` already exists — stop, report to Brian
- Any rejection reason uses only the phrase "not strong enough" without naming a specific test — rewrite

## Iron Law

> **MINIMUM 2 REJECTIONS EVERY WEEK. ZERO REJECTIONS IS A GATE FAILURE — THE STANDARD HAS SLIPPED.**
