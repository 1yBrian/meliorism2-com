---
name: the-plain-reader
description: Use when a research block in an issue draft contains two or more named neurological structures, coined theoretical terms used without prior experiential grounding, or mechanistic descriptions a practitioner without specialist training would need to parse twice before the concept lands.
---

# The Plain Reader

**Announce at start:** "I am running the plain-reader skill."

## Overview

The Plain Reader is not a simplifier — it is a translator of register. **It finds the concrete analog: the scene, the sensation, the practitioner moment the reader has already lived in which the research concept was already operating, before they had a name for it.**

## When to Use

**Always:**
- A research block contains two or more named neurological structures
- A coined theoretical term appears without prior experiential grounding
- A mechanistic description requires two passes to land for a practitioner without specialist training

**Exceptions:**
- Short bridging sentences between research blocks (no standalone concept to anchor)
- Research blocks already written in practitioner register with no jargon present

## Input

The issue draft file in `_engine/staging/`. The Plain Reader reads the full draft and identifies every research block that triggers the conditions above.

## Process

### Step 1: Identify Qualifying Research Blocks

Scan the draft. Mark each block containing two or more named neurological structures, coined terms without experiential grounding, or mechanistic language a non-specialist would parse twice. List them before writing any output.

### Step 2: Write the Three-Part Room Version

For each qualifying block, produce THE ROOM VERSION — the version that lands when you are standing in a room with people. Three parts, maximum 120 words across all three:

**Part 1 — The Scene (2–3 sentences)**
Put the reader inside their own experience. Second person. A specific sensory moment they have already lived. The first sentence must land in the body before it lands in the head. Present tense.

**Part 2 — The Turn (1–2 sentences)**
The pivot: what was actually operating in that scene, stated as plain mechanism. No jargon. This is the moment the reader connects: "that scene — that was this concept." Past tense.

**Part 3 — The Bridge (1 sentence)**
Return the reader to the research: "The research calls this [concept] — [Researcher], [year]. The full account is above." An invitation, not a conclusion.

### Step 3: Apply the Two Tests

Before placing any Room Version, run both tests:

- **16-Year-Old Test:** Could a sharp 16-year-old with no psychology background read Parts 1 and 2 and explain the concept to a friend?
- **PhD Test:** Would the researcher who spent their career on this concept feel the Plain Reading was faithful — that nothing essential was lost?

If either test fails, rewrite. Do not place until both pass.

### Step 4: Place in Draft

Insert each Room Version directly below its research block, directly above the pull-quote cite.

Sequence: `RESEARCH BLOCK → THE ROOM VERSION → PULL-QUOTE CITE`

Wrap in HTML:

```html
<div class="room-version">
  <span class="rv-label">THE ROOM VERSION</span>
  <p class="rv-body">[Parts 1 and 2]</p>
  <p class="rv-bridge">[Part 3]</p>
</div>
```

## Output

Inline HTML blocks inserted into the issue draft. Room Versions are part of the issue file — not a separate output file. The modified draft is the deliverable.

## Voice Rules

- Second person throughout ("you" — not "practitioners" or "the facilitator")
- No jargon in Parts 1 and 2. If the concept requires a technical term, the analog is not specific enough yet
- Sensory and specific — name the sensation, the room, the specific body response
- Present tense in Part 1; past tense in Part 2
- Shorter than the research block it accompanies. Always. Maximum 120 words across all three parts
- No condescension. The label "The Room Version" carries no apology and no hierarchy — it is a different register, not a lower one. One practitioner to another across different backgrounds

## Common Mistakes

**Writing a summary instead of a scene**
- Problem: The output describes what happened rather than making the reader feel the concept as if discovering it themselves
- Fix: Start from a specific body sensation or environmental detail — one the reader has had — then build out

**Using a metaphor more memorable than the concept**
- Problem: The analogy becomes the takeaway; the technical content disappears behind it
- Fix: The analog must unlock the technical content, not replace it. If the reader remembers the scene but not the concept, the analog is wrong

**Exceeding 120 words**
- Problem: The Room Version becomes as dense as the research block
- Fix: Cut until the scene is the minimum number of words needed for the reader to feel it. If longer, the analog is doing too much work

## Red Flags — STOP

- Any technical term in Parts 1 or 2 — stop, find a more concrete analog before continuing
- First sentence that opens with an abstract statement rather than a sensory scene — rewrite from the body up, not the head down
- Room Version longer than the research block it accompanies — cut

## Iron Law

> **THE ROOM VERSION IS A DIFFERENT REGISTER, NOT A LOWER ONE. IT DOES NOT APOLOGIZE FOR EXISTING.**
