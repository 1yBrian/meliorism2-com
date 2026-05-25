---
name: phase-4-issue-composition
description: Use when EDITORIAL-DECISIONS.md contains an approved theme for this dimension and publish date, and the research packet for that theme exists. Builds the full HTML issue in horizontal-swipe 7-card architecture. One composing agent per dimension.
---

# Phase 4: Issue Composition

**Announce at start:** "I am running the phase-4-issue-composition skill."

## Overview

One composing agent per dimension builds deep expertise in their dimension's voice, sources, and practitioner context over time. Each issue is a horizontal-swipe, 7-card HTML structure using the `sections-rail` architecture. **A vertical scroll article is the wrong structure — stop and rebuild before proceeding.**

## When to Use

**Always:**
- `EDITORIAL-DECISIONS.md` contains an approved entry for this dimension and publish date
- The research packet for that theme exists at `_engine/research/YYYY-WW/[dim-slug]-packet.md`
- The Agitator's brief has been received for this issue
- The draft file does not yet exist at the output path

**Exceptions:**
- If the draft file already exists, stop. Do not overwrite. Report to Brian.
- If the Agitator's brief has not been received, stop. The interaction element named in the brief must be present in the HTML — building without the brief produces an incomplete draft.

## Input

- `_engine/research/YYYY-WW/EDITORIAL-DECISIONS.md` — editorial selection and rationale for this theme
- `_engine/research/YYYY-WW/[dim-slug]-packet.md` — full research packet
- `_engine/research/YYYY-WW/00-factors.md` — 33 factors
- Design template: §7b of the editorial directive
- Trust-biology issue as ceiling reference (the structural and tonal benchmark)
- Agitator's brief for this issue (interaction element specification)

## Process

### Step 1: Read the Agitator's Brief

Read the Agitator's brief before writing a single line of HTML. Identify the interaction element it specifies. That element must appear in the draft. If the brief names a reflection prompt, a drag-ranking exercise, a polling moment, or any other interaction — it is required, not optional.

Stop if the brief has not been received. Do not proceed.

### Step 2: Draft the Entry Screen (Card 1)

The entry screen places the reader inside the environment before a word of content appears. It must:
- Use the image brief from the research packet as the background environment
- Include a CTA that is contextually specific to this issue's concept — never "READ →" or "ENTER →"
- Make the reader feel they are already inside the space before committing to reading

Write the CTA last. Test it: would a practitioner who only sees the entry screen understand what kind of space they are entering?

### Step 3: Build the 7-Card Structure

Seven cards minimum. Each card is a section in the `sections-rail`. Cards advance via `goTo(index)` function — horizontal swipe, not vertical scroll.

Required sections (6 mandatory, 1 optional):

| Card | Section | Notes |
|---|---|---|
| 1 | Entry screen | Image-driven environment, contextual CTA |
| 2 | The Phenomenon | What is happening in practice right now |
| 3 | The Evidence | Research-grounded, cited sources from the packet |
| 4 | The Concept | The core idea, practitioner register |
| 5 | Edge Cases | Where the concept breaks down or gets complicated |
| 6 | Etymology / Roots | Historical or linguistic grounding |
| 7 | Application / WWYD | The scenario from the packet, practitioner decision point |

Optional 8th card: The 90-Second Signal. A standalone shareable unit — a single insight, a single action, a single sentence worth forwarding. If included, it must read as complete without the rest of the issue.

### Step 4: Wire the Required Navigation Elements

Every interior card (cards 2–7) must include:
- Reading progress bar (position in the 7-card sequence)
- ↩ Contents button (returns to card 1 or a contents card)
- Forward prompt to the next section (contextually labeled — not "NEXT →")

### Step 5: Wire the Agitator's Interaction Element

Place the interaction element named in the Agitator's brief on the card where it fits the reader's journey. It must be functional — not a placeholder comment. If it is a reflection prompt, the prompt text must be written. If it is a drag-ranking exercise, the items must be present.

### Step 6: Produce Supporting Assets

In the same draft file or as inline comments, include:

**Entry screen CTA** — the final text used (for review reference)

**Image brief** — one sentence, photographic scene, palette #faf8f5 / #8b6f47 / #1a1714. The scene must place a person or space inside an environment. Not a symbolic object on a white background.

**DALL-E prompt** — a complete prompt derived from the image brief, ready to submit.

### Step 7: Write the File

Write to `_engine/staging/YYYY-MM-DD-[slug]-draft.html`. Use the publish date from EDITORIAL-DECISIONS.md and the dimension slug.

## Output

`_engine/staging/YYYY-MM-DD-[slug]-draft.html`

A complete HTML file with the `sections-rail` architecture, all 7 cards, the Agitator's interaction element, navigation elements on every interior card, and inline supporting assets.

## Architecture Reference

```html
<div class="sections-rail">
  <section class="card" id="card-1"><!-- Entry screen --></section>
  <section class="card" id="card-2"><!-- The Phenomenon --></section>
  <!-- ... -->
</div>

<script>
  function goTo(index) {
    // horizontal scroll to card at index
  }
</script>
```

Dark section-break bands separate major sections. Ken Burns effect + gradient overlay on entry screen image. Refer to §7b of the editorial directive for full CSS and JS specifications.

## Common Mistakes

**Vertical scroll structure**
- Problem: Building a standard single-page HTML article instead of the horizontal-swipe `sections-rail`.
- Fix: Stop. Rebuild from the architecture reference. This is not a layout preference — it is the format.

**Generic entry screen CTA**
- Problem: CTA reads "READ →" or "ENTER →" or "EXPLORE →".
- Fix: Write the CTA last, after building the full issue. It should name the specific space the reader is entering — something only true of this issue's concept.

**Agitator's interaction element absent**
- Problem: Draft submitted without the interaction element from the Agitator's brief.
- Fix: Do not submit. Add the element. The draft goes back if it's missing — build it in from the start.

**Placeholder WWYD scenario**
- Problem: "WWYD scenario goes here" or a generic scenario written fresh instead of using the packet's scenario.
- Fix: Use the WWYD scenario from the research packet. It has already passed no-repetition compliance. Do not substitute.

**Forward prompts labeled "NEXT →"**
- Problem: Navigation labels are generic.
- Fix: Label each forward prompt with the name of the next section, contextually phrased. "Into the evidence →" not "NEXT →".

## Red Flags — STOP

- Draft is a single vertical-scroll HTML page — stop, rebuild in `sections-rail` architecture
- No WWYD scenario on card 7 — content is incomplete, do not submit
- Agitator's interaction element is absent or is a placeholder comment — do not submit
- Agitator's brief has not been received — stop, do not build without it
- Entry screen CTA is "READ →", "ENTER →", or any generic verb — rewrite before filing

## Iron Law

> **HORIZONTAL-SWIPE 7-CARD SECTIONS-RAIL. A VERTICAL SCROLL ARTICLE IS THE WRONG STRUCTURE — STOP AND REBUILD.**
