---
name: phase-2-dimension-research
description: Use when the week's 00-factors.md exists and a dimension agent has been assigned an active slot for this week. Each dimension agent produces one research packet. Nine of eleven dimensions run per week; two rotate out and neither may be skipped twice in a row.
---

# Phase 2: Dimension Research

**Announce at start:** "I am running the phase-2-dimension-research skill."

## Overview

Each of the nine active dimension agents reads the week's 33 factors and produces a single research packet — a proposed theme, core concept, sources, scenario, format, and image brief. **A theme headline that doesn't work as a standalone practitioner-usable idea today fails before anything else is evaluated.**

## When to Use

**Always:**
- `_engine/research/YYYY-WW/00-factors.md` exists
- This dimension is in the active slot for the week
- The dimension's packet does not yet exist

**Exceptions:**
- If this dimension was skipped last week, it cannot be skipped again this week. If the rotation would skip it twice, override and include it.
- If the packet file already exists, stop. Do not overwrite. Report path to Brian.

## Input

- `_engine/research/YYYY-WW/00-factors.md` — the 33 factors for this week
- The dimension brief for this agent's dimension (see Eleven Dimensions below)
- Last 4 published issues — for no-repetition compliance on themes, formats, and WWYD scenarios
- 25-retired formats list (see Retired Formats below)

## Process

### Step 1: Confirm Active Status

Verify this dimension is in the active rotation for this week. Verify its packet does not already exist. Verify `00-factors.md` is present and contains 33 items.

Stop if the packet already exists. Do not proceed.

### Step 2: Read the Factors

Read all 33 factors without filtering. Do not pre-select factors that "obviously" connect to this dimension. The connection that earns its place in the packet should be non-obvious — a factor from the random pool or an unexpected seasonal item is preferable to the most direct calendar match.

### Step 3: Draft the Theme Headline

Write one sentence. It must:
- Be practitioner-usable today — a busy practitioner should be able to act on this idea this week
- Name the concept without requiring the full issue to understand it
- Not be a question
- Not use the dimension name as a noun

Apply the "could I use this today" test before moving on. If the answer is no, rewrite. Do not proceed to Step 4 with a failing headline.

Stop if the headline cannot pass the test after three rewrites. Flag as BLOCKED.

### Step 4: Build the Research Packet

Produce each element in order:

**Theme headline** — one sentence, practitioner-usable today (from Step 3)

**Core concept** — 2–3 paragraphs, research-grounded. Practitioner register, not academic. No jargon without immediate plain-language follow-through. Must connect to at least one of the 33 factors — name which one and how at the end of this section.

**Cited sources** — 3–5 sources. Format: Author, Title, Year. Must be real, verifiable citations. No invented sources. No sources older than 20 years unless the age itself is the point (historical anchor).

**WWYD scenario** — "What Would You Do?" A role-specific practitioner scenario, 2–4 sentences. It must feel specific and real — a named setting, a named friction, a moment of decision. It must not have appeared in any of the last 4 published issues. It must not be generic ("a client comes to you feeling stuck").

**Suggested format** — one format name from the active list. Must not appear in the 25-retired list. Must not have been used by this dimension in the last 4 issues.

**Suggested image environment** — one sentence, photographic scene. Write it as a DALL-E brief. Palette reference: warm cream tones (#faf8f5 / #8b6f47 / #1a1714). The scene must place a person or space inside an environment — not a symbolic object on a white background.

**Influence factor used** — state which of the 33 factors shaped this packet and write 1–2 sentences on the connection.

**Confidence rating** — one of: Strong / Solid / Weak. Mandatory. Omitting it is hiding uncertainty.

### Step 5: Write the File

Write to `_engine/research/YYYY-WW/[dim-slug]-packet.md`. Use the dimension slug from the list below.

## Output

`_engine/research/YYYY-WW/[dim-slug]-packet.md`

One file per dimension per week. Contains all eight elements from Step 4 in order.

## The Eleven Dimensions

| Dimension | Slug |
|---|---|
| Living Income | living-income |
| Brave Spaces | brave-spaces |
| In-Person Presence | in-person-presence |
| Witnessing Authentic Humanity | witnessing-authentic-humanity |
| Gender & Generational Difference | gender-generational |
| Witnessing | witnessing |
| Critical Consciousness | critical-consciousness |
| Adventure | adventure |
| Out of the Box | out-of-the-box |
| Becoming Adaptable | becoming-adaptable |
| Somatic / Body Intelligence | somatic-body |

Nine run per week. Two rotate out. Neither skipped dimension may be skipped again the following week.

## Retired Formats (do not suggest these)

The composing agent will reject any format from this list. Fix it here, before the packet reaches Phase 3.

The 25-retired list lives at `_engine/research/retired-formats.md`. Check it before filing. If that file does not exist, flag BLOCKED — do not guess.

## Common Mistakes

**Theme headline that fails the "could I use this today" test**
- Problem: The headline describes an interesting concept but doesn't give a practitioner anything actionable.
- Fix: Rewrite until it names a usable idea, not a topic. "The role of silence in supervision" fails. "Three ways to use intentional silence in your next supervision session" passes.

**Generic WWYD scenario**
- Problem: "A client comes to you feeling disconnected from their community." No setting. No friction. No decision point.
- Fix: Name the room, the relationship, the specific moment. "You're co-facilitating a group debrief after a community incident. Two participants are doing the emotional labor for the others. At the 40-minute mark, you have a choice."

**Omitting the confidence rating**
- Problem: Packet looks complete but the rating field is blank.
- Fix: Rate it. If you are uncertain, that is what Weak is for. Omitting the rating is a filing error — the editorial agent needs it.

**Format in the retired list**
- Problem: Suggested format gets rejected at Phase 3, sending the packet back.
- Fix: Check `retired-formats.md` before filing. One check, zero rework.

## Red Flags — STOP

- Fewer than 3 cited sources — filing incomplete research
- Theme headline is a question — rewrite before filing
- WWYD scenario matches a scenario from the last 4 issues — flag and rewrite
- `retired-formats.md` does not exist — flag BLOCKED, do not guess at the retired list
- Confidence rating is missing — do not file

## Iron Law

> **A THEME HEADLINE THAT DOESN'T PASS THE "COULD I USE THIS TODAY" TEST FAILS BEFORE ANYTHING ELSE IS EVALUATED. DO NOT FILE IT.**
