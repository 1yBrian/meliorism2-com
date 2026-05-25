---
name: phase-6-stress-test
description: Use when all three editorial review files exist for a draft (copy-review.md, design-review.md, marketing-review.md). Runs four independent reviewers in parallel — each reads the draft without seeing the others' feedback. Reviewers: (1) Native American woman presenter — cultural integrity lens; (2) High-profile TED talk speaker — stage-worthiness and idea clarity; (3) K–12 school teacher — pedagogical soundness and teachability; (4) Out-of-work aspiring trainer — accessibility and practical utility. Each returns a structured 5-item feedback note. All four compile to a single output file.
---

# Phase 6 — Stress Test

**Announce at start:** "I am running the phase-6-stress-test skill."

## Overview

Four independent reviewers read the draft in parallel. Each reviewer holds a distinct lens. No reviewer sees another's feedback before completing their own. Independence is the entire point of this phase — a reviewer who reads ahead loses their lens and the phase must restart.

## When to Use

When all three of the following files exist for the current draft:
- `_engine/reviews/copy-review.md`
- `_engine/reviews/design-review.md`
- `_engine/reviews/marketing-review.md`

Do not run this phase if any review file is absent or marked incomplete.

## Input

- Draft HTML file (full read — do not accept a summary)
- Confirmed paths to all three review files

## Process

### Step 1: Confirm prerequisites

Verify all three review files exist and are marked complete. If any is missing, STOP and report BLOCKED with the missing file named.

### Step 2: Load the draft

Read the full draft HTML file. Do not accept a summary or excerpt from the composing agent.

### Step 3: Run all four reviewers in parallel

Each reviewer reads the draft independently. Each returns a structured 5-item feedback note. No reviewer sees another's output before completing their own.

---

**Reviewer 1 — Native American Woman Presenter**
Lens: cultural integrity, representation, whose knowledge is centered, what is erased.

Questions this reviewer answers:
- Are cited sources culturally diverse?
- Does the content center Western or white frameworks without acknowledging it?
- Is any cultural content used appropriately — not extracted, not flattened?
- Is the practitioner world depicted inclusive of practitioners who are not white, not Western, not neurotypical?

Returns: 5 specific observations with proposed adjustments where warranted.

---

**Reviewer 2 — High-Profile TED Talk Speaker**
Lens: stage-worthiness, opening power, idea clarity, memorability.

Questions this reviewer answers:
- Does this concept have a single clear idea worth spreading?
- Is the opening sentence a hook?
- Would a TED audience remember the core concept after 30 days?
- Is the vocabulary accessible without being dumbed down?

Returns: 5 specific observations with proposed adjustments where warranted.

---

**Reviewer 3 — K–12 School Teacher**
Lens: pedagogical soundness, accessibility, teachability.

Questions this reviewer answers:
- Is the concept teachable? Can a practitioner explain it in 60 seconds?
- Is there a clear learning arc — what changes in the reader?
- Is the What Would You Do (WWYD) scenario realistic in a classroom or training room context?
- Is any jargon used that would confuse a smart non-specialist?

Returns: 5 specific observations with proposed adjustments where warranted.

---

**Reviewer 4 — Out-of-Work Aspiring Trainer**
Lens: inspiration, accessibility, practical utility — "this is for me too."

Questions this reviewer answers:
- Does this feel for the already-credentialed elite, or for someone still building?
- Is there something actionable to try this week even without a full client roster?
- Does this make the reader feel more capable or more behind?
- Would they share this with someone just starting?

Returns: 5 specific observations with proposed adjustments where warranted.

---

### Step 4: Compile all four outputs

Assemble all four reviewer notes into a single compiled file. Preserve reviewer attribution. Do not merge or summarize across lenses — keep each reviewer's voice intact.

## Output

`_engine/staging/YYYY-MM-DD-[slug]-stress-test.md`

Structure:
```
# Stress Test — [slug] — [date]

## Reviewer 1: Native American Woman Presenter
[5 items]

## Reviewer 2: TED Talk Speaker
[5 items]

## Reviewer 3: K–12 School Teacher
[5 items]

## Reviewer 4: Aspiring Trainer
[5 items]
```

## Common Mistakes

- Any reviewer reading another's feedback before completing their own — independence is the entire point; if this happens, that reviewer's output is invalid and must be regenerated
- Summarizing or merging feedback across lenses — each lens must remain intact and attributed
- Running this phase before all three review files exist — stress test depends on prior phases being complete

## Red Flags — STOP

- Any reviewer using the word "interesting" as feedback — it means nothing; require specific observations before continuing
- Any reviewer output with fewer than 5 items — incomplete; regenerate before compiling
- Draft has changed since review files were written — confirm draft version matches what was reviewed
