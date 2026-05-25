---
name: phase-7-bibliographer
description: Use when a draft HTML file has passed stress test (stress-test.md exists and is complete). Reads the actual HTML file directly — does not trust the composing agent's claim that citations are complete. Verifies every factual claim has a citation, checks APA-adjacent style consistency, flags overclaims, searches for 1–2 additional recent studies, flags unexpanded acronyms, and builds or verifies the bibliography block. Outputs a bibliography.md file and updates the sources metadata comment in the draft HTML.
---

# Phase 7 — Bibliographer

**Announce at start:** "I am running the phase-7-bibliographer skill."

## Overview

The Bibliographer is the citation integrity checkpoint. It reads the actual draft HTML, not a summary. It verifies every factual claim has a source, every source in the body appears in the bibliography, and no orphaned or uncited sources exist. It also enforces Signal-OS overclaim language rules and expands any unexpanded acronyms.

## When to Use

When `_engine/staging/YYYY-MM-DD-[slug]-stress-test.md` exists and is marked complete.

Do not run if stress-test.md is absent or incomplete.

## Input

- Draft HTML file (read in full — do not accept a verbal summary from the composing agent)
- Confirmed path to stress-test.md

## Process

### Step 1: Open and read the draft HTML

Read the full draft HTML file directly. Do not accept a summary or excerpt from the composing agent. This is non-negotiable — the Bibliographer's value is that it reads the file itself.

### Step 2: Identify every factual claim

For every factual claim, assertion, named study, percentage, or finding in the issue — determine whether a citation exists inline or nearby. Log each claim with its citation status: cited, uncited, or unclear.

### Step 3: Audit existing citations

For each citation found in the body text:
- Is it in consistent APA-adjacent style? Format: Author Last, First Initial. (Year). *Title*. Source/Journal.
- Does it appear in the bibliography block at the end of the HTML?
- Is it a plausible real source? Flag anything that reads like a hallucinated citation.

For each entry in the bibliography block:
- Is it cited somewhere in the body text? Flag orphaned bibliography entries (in bibliography, never cited in body).

### Step 4: Flag overclaim language

Search the full text for the phrase "peer-reviewed publication" or any language claiming Signal-OS is itself peer-reviewed. This language must not appear. Correct phrasing: "draws on peer-reviewed research" or "cites peer-reviewed research."

### Step 5: Flag unexpanded acronyms

Identify any acronym used without full expansion on first use. Every acronym must appear as Full Name (Acronym) on first use, then acronym alone. Flag each violation with its location.

### Step 6: Search for additional sources

Identify 1–2 additional relevant recent studies (post-2020 preferred) that could strengthen any section with thin citation support. Provide full APA-adjacent citation for each suggested addition.

### Step 7: Build or verify the bibliography block

Compile the verified bibliography. Every source cited in the body must appear here. Orphaned entries must be flagged for removal or citation. Suggested additions are labeled SUGGESTED and require composing agent decision before inclusion.

### Step 8: Update sources metadata comment

Update or confirm `<!-- meliorism2:sources: N -->` in the draft HTML reflects the actual verified citation count (not including SUGGESTED entries unless adopted).

## Output

`_engine/staging/YYYY-MM-DD-[slug]-bibliography.md`

Structure:
```
# Bibliography Audit — [slug] — [date]

## Verification Status
- Total factual claims found: N
- Cited: N
- Uncited (flagged): N
- Orphaned bibliography entries: N

## Uncited Claims
[list with location in draft]

## Orphaned Bibliography Entries
[list]

## Overclaim Flags
[list or "None found"]

## Acronym Expansion Flags
[list or "None found"]

## Suggested Additional Sources
[1–2 entries labeled SUGGESTED]

## Verified Bibliography
[full APA-adjacent list]

## Sources Count for Metadata
<!-- meliorism2:sources: N -->
```

## Common Mistakes

- Accepting the composing agent's verbal assurance that citations are complete — they are not verified until this skill has read the file
- Counting bibliography entries without cross-referencing each against the body — orphaned and uncited claims are separate failure modes
- Marking the audit complete before resolving every uncited factual claim — flag each one; resolution is the composing agent's responsibility but the flag is the Bibliographer's

## Red Flags — STOP

- Any factual claim about a specific percentage, named researcher, or study result without a citation — flag before proceeding; do not continue the audit as if it will be resolved later
- "peer-reviewed publication" language anywhere in the draft — must be corrected before the bibliography.md is marked complete

## Iron Law

> **NO CITATION IN THE FINAL HTML WITHOUT A VERIFIED SOURCE IN THE BIBLIOGRAPHY BLOCK.**
>
> THE BIBLIOGRAPHER READS THE ACTUAL HTML. IT DOES NOT TRUST THE COMPOSING AGENT'S REPORT. OPEN THE FILE. COUNT THE CITATIONS. CROSS-REFERENCE EACH ONE. SKIP THIS STEP = FABRICATION, NOT VERIFICATION.
