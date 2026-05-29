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

- **`_engine/LEARNING-LOG.md`** — read the last 7 Hall of Fame entries FIRST, before anything else. Let them set the standard. Do not imitate — let them remind you what excellence feels like in this voice.
- `_engine/CHANGE-LOG.md` — read for post-publish fixes on recent issues. These are corrections already made to live issues. The next issue inherits every fix automatically — you do not need to be told twice.
- `_engine/research/YYYY-WW/EDITORIAL-DECISIONS.md` — editorial selection and rationale for this theme. **Contains the energy archetype assignment.**
- `_engine/research/YYYY-WW/[dim-slug]-packet.md` — full research packet
- `_engine/research/YYYY-WW/00-factors.md` — 33 factors
- Design template: §7b of the editorial directive
- Agitator's brief for this issue (interaction element specification)
- `PUBLICATION-SOUL.md` §Energy Archetypes — the full archetype definitions. Read the assigned archetype before writing a single word.

## Process

### Step 0: Read the Learning Log and Change Log

Open `_engine/LEARNING-LOG.md`. Read the last 7 Hall of Fame entries. Read the full Rewrite Queue and Voice Drift Watch. These are not suggestions — they are the accumulated intelligence of this publication. A composing agent that skips this step is writing blind.

Open `_engine/CHANGE-LOG.md`. Read every entry marked `CARRIES FORWARD`. These are corrections to published issues that must be inherited. If the change log says "clock should show PT not UTC," every future issue uses PT. You do not need to rediscover this.

Only then proceed to Step 1.

### Step 1: Read the Energy Archetype and the Agitator's Brief

**Energy archetype first.** Find the `energy_archetype` field in `EDITORIAL-DECISIONS.md` for this issue. Look it up in `PUBLICATION-SOUL.md` §Energy Archetypes. Let the archetype set the tempo before you write anything — it shapes sentence rhythm, register, and where the wit or warmth lives. The Friend from the Field is always the ground state underneath.

If no archetype is assigned, default to **Friend from the Field**.

**Then read the Agitator's brief.** Identify the interaction element it specifies. That element must appear in the draft. If the brief names a reflection prompt, a drag-ranking exercise, a polling moment, or any other interaction — it is required, not optional.

Stop if the Agitator's brief has not been received. Do not proceed.

### Step 2: Draft the Entry Screen (Card 1)

The entry screen places the reader inside the environment before a word of content appears. It must:
- Use the image brief from the research packet as the background environment
- Include a CTA that is contextually specific to this issue's concept — never "READ →" or "ENTER →"
- Make the reader feel they are already inside the space before committing to reading
- Include the **Emotional Weather Report** — low visual weight, fine-print register, near the bottom of the entry screen. One short phrase naming the emotional vibe of this issue. Not a judgment of the reader — a reading of the issue's own atmosphere. The practitioner uses it as a lens for their room: *which of my clients are in this weather right now?*

Examples of correct register: *"Emotional weather: quiet defiance."* / *"Emotional weather: the good kind of unsettled."* / *"Emotional weather: solidarity in a long week."*

**Emotional Weather placement rules:**

1. **Card 1 (Cover/Entry screen)** — place the chip here with a **"learn more → /weather"** link. No inline onboarding copy — the link carries readers to the full explainer. The chip is low visual weight: emoji + label + link, one line.

— **or** —

2. **Card 2 (Phenomenon)** — place the chip at the bottom of card 2 with the inline onboarding paragraph: what the frequency means, how to check your own weather, how to use it as a room lens, that the library holds issues for other weathers. No "learn more" link needed — the copy is already there.

3. **Bibliography section before Etymology (Card 6: Roots)** — fallback only, when both card 1 and card 2 are too immersive to interrupt (rare: video-first issues, full-bleed interactive openers). Chip only, no copy, no link. Readers who reach card 6 are committed — they will know what it means.

**The chip always carries:** emoji · label · (link to /weather, if on card 1)

Write the CTA last. Write the Emotional Weather Report last. Test both: would a practitioner who only sees the entry screen understand what kind of space they are entering, and what emotional register awaits them?

### Step 3: Build the 8-Card Structure

Eight cards. Each card is a section in the `sections-rail`. Cards advance via `goTo(index)` function — horizontal swipe, not vertical scroll.

Required sections (all 8 mandatory):

| Card | Section | Notes |
|---|---|---|
| 1 | Entry screen | Image-driven environment, contextual CTA, Emotional Weather Report |
| 2 | The Phenomenon | What is happening in practice right now |
| 3 | The Evidence | Research-grounded, cited sources from the packet |
| 4 | The Concept | The core idea, practitioner register |
| 5 | Edge Cases | Where the concept breaks down or gets complicated |
| 6 | Etymology / Roots | Historical or linguistic grounding |
| 7 | Application / WWYD | The scenario from the packet, practitioner decision point |
| 8 | The Delight Card | Off-brief. No practitioner framing. No mechanism. Something genuinely surprising, funny, beautiful, or worth knowing that has nothing to do with professional development. A place to visit. A recipe. A strange fact. A short story. A thing worth noticing. The reader earned this by walking through the craft content — it's waiting for them at the end. |

**The Delight Card is mandatory. Every issue. No exceptions.** It is the reason to open the paper. If it reads like professional development content with the jargon removed, rewrite it. It should make someone sigh with appreciation, laugh quietly, or want to go somewhere.

### Step 4: Wire the Required Navigation Elements

Every interior card (cards 2–8) must include:
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

### Step 7: Add the Staging-Only Review Button

Every draft gets a `📝 Leave a note` floating button that lets Brian annotate the issue during phone review. This button must be invisible on the live site — only Brian is on staging; any reader on the live site could otherwise submit notes that appear to come from him.

Wire it with a hostname gate immediately after the button tag:

```html
<button class="review-btn" id="review-btn" onclick="openReview()">📝 Leave a note</button>
<script>
// Staging-only — hide on live site to prevent reader impersonation
(function(){
  if(window.location.hostname==='meliorism2.com'){
    var btn=document.getElementById('review-btn');
    if(btn)btn.style.display='none';
  }
})();
</script>
```

The review overlay writes to Supabase `captures` (tag: `review`) with the issue slug, issue number, and date in the content prefix. The anon key is safe in frontend HTML. Do not send to Telegram — Supabase is the readable queue.

### Step 8: Write the File

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

> **HORIZONTAL-SWIPE 8-CARD SECTIONS-RAIL. A VERTICAL SCROLL ARTICLE IS THE WRONG STRUCTURE — STOP AND REBUILD. THE DELIGHT CARD AND EMOTIONAL WEATHER REPORT ARE NOT OPTIONAL.**
