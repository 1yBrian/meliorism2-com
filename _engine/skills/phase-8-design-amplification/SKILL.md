---
name: phase-8-design-amplification
description: Use when the bibliographer has cleared a draft (bibliography.md exists and is complete). Runs three amplification agents in parallel — each reads the citation-verified draft looking for what is boring, expected, safe, or forgettable: (1) The OCD Detailer — micro-precision, word-level specificity, section headers; (2) The ADHD Reader — attention flow, where readers stop and where they re-engage; (3) The Kid — genuine interest, over-complexity, what could be said in a third of the words. The Publicist also runs simultaneously. All three amplification outputs compile to a single file. Composing agent makes a surgical amplification pass — not a full rewrite.
---

# Phase 8 — Design Amplification

**Announce at start:** "I am running the phase-8-design-amplification skill."

## Overview

Three amplification agents read the citation-verified draft and return specific moments that are weak, forgettable, or overcomplicated. The composing agent then makes a targeted amplification pass — not a structural rewrite. Simultaneously, the Publicist runs its own pass (see `skills/the-publicist/SKILL.md`).

Amplification is surgical. The structure of the issue is not being rebuilt. Specific moments are being sharpened.

## When to Use

When `_engine/staging/YYYY-MM-DD-[slug]-bibliography.md` exists and is marked complete.

Do not run if bibliography.md is absent, incomplete, or has unresolved uncited claims.

## Input

- Citation-verified draft HTML file (read in full)
- Confirmed path to bibliography.md

## Process

### Step 1: Confirm prerequisites

Verify bibliography.md exists and is marked complete with no unresolved uncited claims. If any uncited claims remain, STOP and report BLOCKED.

### Step 2: Load the draft

Read the full citation-verified draft HTML. Do not accept a summary.

### Step 3: Run all three amplification agents in parallel

Each agent reads the draft independently and returns their structured output. The Publicist also runs simultaneously — it does not block or wait on the amplification agents.

---

**The OCD Detailer**
Lens: micro-precision — the one pixel that's wrong, the one word that could be 40% more specific, the section header that describes what's there instead of making you feel something.

This agent does not look at structure. It looks at the grain of the writing. It finds:
- Words that are technically correct but imprecise — what is the more specific word?
- Section headers that are descriptive labels instead of evocative frames — what header would make a reader stop?
- Sentences that are doing two jobs and should do one

Returns: a list of micro-fixes. Each item is: location + current text + proposed replacement + one-line rationale.

---

**The ADHD Reader**
Lens: attention flow — reads the issue the way a distracted, overstimulated practitioner reads it. Quickly, partially, with tabs open.

This agent tracks where attention collapses and where it snaps back. It flags:
- Where they stopped reading (location + what caused the stop)
- What pulled them back in after stopping
- What they skipped entirely (section or paragraph + reason)
- Which sentence made them stop and read again

Returns: 5 moments that lost them + 3 moments that grabbed them. Each item is: location + what happened + what would change it.

---

**The Kid**
Lens: genuine interest — reads it like a curious 11-year-old with zero professional context.

This agent does not care about importance. It cares about what is actually interesting. It flags:
- 3 things that are genuinely interesting (not just important)
- 3 things that are trying too hard to sound smart and could be said in one-third the words
- Anything that is confusing when it does not need to be

Returns: 6 items total (3 interesting + 3 overcomplicated), each with location and a plain-language note.

---

### Step 4: Compile amplification notes

Assemble all three agent outputs into a single compiled file. Preserve agent attribution. Do not merge across lenses.

### Step 5: Composing agent amplification pass

The composing agent reads the compiled notes and makes targeted changes. This is not a rewrite. Each change must be traceable to a specific note in the amplification file. Changes that are not traceable to a note are out of scope for this phase.

## Output

`_engine/staging/YYYY-MM-DD-[slug]-amplification.md`

Structure:
```
# Amplification Notes — [slug] — [date]

## The OCD Detailer
[micro-fix list: location | current | proposed | rationale]

## The ADHD Reader
Lost moments (5):
[list]

Grabbed moments (3):
[list]

## The Kid
Actually interesting (3):
[list]

Overcomplicated (3):
[list]
```

## Common Mistakes

- The composing agent treating amplification notes as a full rewrite brief — amplification is surgical; the structure is not being rebuilt
- An amplification agent returning vague summary feedback instead of specific moments with specific proposed fixes — each item must have a location and a concrete alternative
- Running this phase before bibliography.md is complete — amplifying an uncited draft is wasted effort

## Red Flags — STOP

- Any amplification agent saying "this is mostly good" — that is not feedback; require specific moments with specific fixes before compiling
- Any amplification agent output with no location references — vague feedback cannot be acted on; regenerate before compiling
- Composing agent making structural changes during this pass — amplification is micro-level; structural changes require a separate editorial decision
