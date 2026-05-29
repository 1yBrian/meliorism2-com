---
name: phase-9-deploy
description: Use when the final HTML is approved after amplification pass, all five review files exist at their designated paths (copy-review.md, design-review.md, marketing-review.md, stress-test.md, bibliography.md), and the bibliographer has confirmed citation count. Last gate before the issue goes live. Runs CHANGE-LOG carries-forward verification, pre-flight verification on all conditions, deploys to archive/YYYY-MM-DD-[slug].html (never index.html), updates Supabase, and writes the Obsidian stub.
---

# Phase 9 — Deploy

**Announce at start:** "I am running the phase-9-deploy skill."

## Overview

The final gate before an issue goes live. No deploy happens until all CHANGE-LOG carries-forward checks pass, all five review files exist, all metadata is correct, and the deploy target is confirmed as the archive path — never index.html. If any pre-flight check fails, the deploy is BLOCKED and the specific failure is named.

## When to Use

When all of the following are true:
- Amplification pass is complete (`_engine/staging/YYYY-MM-DD-[slug]-amplification.md` exists)
- All five review files exist at their designated paths
- Bibliographer has confirmed citation count and updated the sources metadata comment
- Brian has approved the final HTML

## Input

- Final approved HTML file
- Confirmed slug and date matching EDITORIAL-DECISIONS.md
- Supabase credentials (from `_engine/ZEN-DIRECTIVE.md`)

## Process

### Step 0: CHANGE-LOG Carries-Forward Verification

This step runs before any file check, any metadata check, and any deploy command. If any carries-forward check fails, the deploy is BLOCKED. Report which check failed and exactly what the issue HTML is missing. Do not proceed to Step 1 until all carries-forward checks pass.

**How to run it:**

1. Read `_engine/CHANGE-LOG.md` in full.
2. Extract every entry marked `Carries forward: YES`.
3. For each such entry, open the target issue HTML and verify the fix is present.
4. Document each check as PASS or FAIL with a one-line note.

**Example carries-forward checks drawn from known post-publish fixes (these are illustrative — always read the actual CHANGE-LOG for the current authoritative list):**

- [ ] Card count: `sections-rail` uses `width:800%` and `width:calc(100%/8)` — 8 cards present, not 7
- [ ] Emotional Weather chip present on Card 1 (entry screen) — `.weather-chip` or `.weather-block` element with emoji, label, and `/weather` link
- [ ] Etymology block present on Roots/Application card — `<h3>Etymology</h3>` or equivalent heading with Latin or Greek root, 2–3 sentences
- [ ] Footer bar contains exactly three links: `← LIBRARY · WEATHER · HOME` — no static labels, no missing WEATHER link
- [ ] Clock uses `Intl.DateTimeFormat` with `timeZone:'America/Los_Angeles'` — label reads `HH:MM:SS PT`, no UTC display anywhere
- [ ] `@media(max-width:640px)` block present with `font-size:1rem!important` on all stamp/label/utility text elements — covers `.date-tag`, `.issue-format-badge`, `.section-number`, and all utility text
- [ ] `goTo()` redirects to `/archive/index.html` when `index >= CARDS.length` — nav-next on final card labeled `← LIBRARY` in amber, never disabled
- [ ] Card 0 (The Signal): hero image is first child of `.card-inner`, metadata block follows in DOM order
- [ ] Any Living Income or pricing issue: no "accept at a loss" or "discount" language present — three valid options only (add value, adjust scope, decline)
- [ ] `<!-- meliorism2:energy: -->` comment present and populated with energy archetype value

**If the CHANGE-LOG has no entries marked `Carries forward: YES`:** document that explicitly — "CHANGE-LOG read. No carries-forward entries found. Proceeding." Do not skip this step silently.

### Step 1: Pre-flight verification

Run all checks before any deploy command. If any check fails, STOP immediately, report BLOCKED, and name the specific failure. Do not proceed past a failed check.

**File existence checks:**
- [ ] `_engine/reviews/copy-review.md` — exists and complete
- [ ] `_engine/reviews/design-review.md` — exists and complete
- [ ] `_engine/reviews/marketing-review.md` — exists and complete
- [ ] `_engine/staging/YYYY-MM-DD-[slug]-stress-test.md` — exists and complete
- [ ] `_engine/staging/YYYY-MM-DD-[slug]-bibliography.md` — exists and complete

**HTML metadata checks (open the file and verify each):**
- [ ] Final HTML filename matches slug in EDITORIAL-DECISIONS.md
- [ ] Deploy target path is `archive/YYYY-MM-DD-[slug].html` — confirm this is NOT `index.html`
- [ ] `<!-- meliorism2:sources: N -->` in HTML matches verified bibliography count
- [ ] `<!-- meliorism2:date: -->` present and correct
- [ ] `<!-- meliorism2:slug: -->` present and correct
- [ ] `<!-- meliorism2:dimension: -->` present and correct
- [ ] `<!-- meliorism2:energy: -->` present and populated

**Structural checks (open the file and verify each):**
- [ ] Card count: `sections-rail` width is `800%` and each card is `calc(100%/8)` — 8 cards, not 7
- [ ] `.weather-chip` or `.weather-block` element present on Card 1 (entry screen)
- [ ] `<h3>Etymology</h3>` or equivalent heading present in the Roots/Application card
- [ ] Footer bar contains three links: `← LIBRARY`, `WEATHER`, `HOME` — WEATHER link present, no static labels
- [ ] Clock implementation uses `timeZone:'America/Los_Angeles'` — no UTC display
- [ ] `@media(max-width:640px)` font floor block present in `<style>`
- [ ] `goTo()` function includes boundary redirect to `/archive/index.html` — final card nav-next labeled `← LIBRARY` in amber
- [ ] Card 0 hero image is first child of `.card-inner`

**Library check (open `archive/index.html` and verify):**
- [ ] BRIEFINGS array entry for this slug exists with correct date, title, format, dimension, and sources count
- [ ] Sources count in BRIEFINGS entry matches `<!-- meliorism2:sources: N -->` in the issue HTML

### Step 2: Deploy confirmation checklist

Print this checklist to output before issuing any deploy command. All boxes must be checked. If any box cannot be checked, STOP — report BLOCKED with the specific item.

```
PRE-DEPLOY CONFIRMATION — [YYYY-MM-DD-slug]

- [ ] All CHANGE-LOG carries-forward checks passed (Step 0)
- [ ] All five review files present at designated paths (Step 1)
- [ ] HTML metadata complete: sources, date, slug, dimension, energy all present (Step 1)
- [ ] Structural gates passed: 8 cards, weather chip, etymology, footer, clock, mobile font floor, goTo() boundary, Card 0 DOM order (Step 1)
- [ ] Library BRIEFINGS array entry verified and sources count matches (Step 1)
- [ ] Target file is archive/YYYY-MM-DD-[slug].html — NOT index.html (confirmed)
- [ ] Brian has approved the final HTML (pre-condition)

ALL CHECKS PASSED. Proceeding to deploy.
```

### Step 3: Deploy the issue

```bash
./deploy-api.sh "Issue: [title] — [dimension] — full pipeline complete" archive/YYYY-MM-DD-[slug].html
```

Confirm deploy succeeds before proceeding to Step 4.

### Step 4: Deploy library update if sources count was stale

If the BRIEFINGS array in `archive/index.html` required a sources count correction:

```bash
./deploy-api.sh "Library: update sources count for [slug]" archive/index.html
```

### Step 5: Supabase update

Insert row into the `issues` table:
- `slug`: YYYY-MM-DD-[slug]
- `title`: issue title
- `dimension`: dimension value from metadata
- `sources`: verified citation count
- `published_at`: today's date
- `status`: live

Update the matching `editorial_calendar` row:
- Set `status` → `live`

### Step 6: Obsidian stub

Write stub file:
`08 - The Intermodal Hub/Signal-OS/Issues/YYYY-MM-DD-[slug].md`

Stub content:
```markdown
# [Issue Title]

- Date: YYYY-MM-DD
- Slug: [slug]
- Dimension: [dimension]
- Sources: N
- Energy: [archetype]
- URL: https://meliorism2.com/archive/YYYY-MM-DD-[slug].html
- Status: live
```

## Output

Live issue at `https://meliorism2.com/archive/YYYY-MM-DD-[slug].html`

Supabase `issues` row inserted, `editorial_calendar` row updated to `live`.

Obsidian stub written.

## Common Mistakes

- Deploying to `index.html` instead of the archive path — this destroys the homepage; the fix is in the filename check, not the content
- Deploying with a stale sources count in `archive/index.html` — always verify the BRIEFINGS array entry matches the bibliography count before deploying the library
- Skipping the Supabase row update — the editorial calendar row must be set to `live` or the production state cannot be tracked in COOK
- Skipping the Obsidian stub — the vault is the record of record; every live issue must have a stub
- Skipping Step 0 (CHANGE-LOG verification) — carries-forward checks exist because a fix was hard-won after a live issue failed; skipping them means the same failure ships again
- Treating the carries-forward check list as illustrative rather than authoritative — always read the actual CHANGE-LOG; the list in Step 0 is a memory aid, not the source of truth

## Red Flags — STOP

- Deploy target contains `index.html` without the `archive/` path prefix — STOP immediately; this is a homepage-destroying error
- Any review file is absent — do not deploy; report BLOCKED and name which files are missing; a deploy without complete review is a trust failure, not a shortcut
- Any CHANGE-LOG carries-forward check fails — STOP; report BLOCKED with the check that failed and what the issue is missing; a carries-forward failure means a known defect is about to ship again

## Iron Law

> **NO DEPLOY WITHOUT CONFIRMING TARGET IS `archive/YYYY-MM-DD-[slug].html` — NEVER `index.html`.**
>
> `index.html` IS THE PERMANENT LANDING PAGE. OVERWRITING IT DESTROYS THE HOMEPAGE. CONFIRM THE SLUG. CONFIRM THE PATH. THEN DEPLOY.

> **NO DEPLOY WITHOUT ALL FIVE REVIEW FILES PRESENT AT THEIR DESIGNATED PATHS.**
>
> A DEPLOY WITHOUT COMPLETE REVIEW IS A TRUST FAILURE. THE REVIEW FILES ARE THE PROOF THAT THE PIPELINE RAN. CHECK THEY EXIST BEFORE THE API CALL.

> **NO DEPLOY WITHOUT READING THE CHANGE-LOG AND VERIFYING EVERY CARRIES-FORWARD ENTRY.**
>
> CARRIES-FORWARD FIXES EXIST BECAUSE A KNOWN DEFECT SHIPPED ONCE. THE CHANGE-LOG IS THE INSTITUTIONAL MEMORY OF EVERY POST-PUBLISH REPAIR. IF YOU SKIP STEP 0, YOU ARE CHOOSING TO IGNORE THAT MEMORY. EVERY ENTRY MARKED "CARRIES FORWARD: YES" IS A HARD GATE. PASS ALL OF THEM OR STOP.
