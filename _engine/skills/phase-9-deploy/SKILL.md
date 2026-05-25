---
name: phase-9-deploy
description: Use when the final HTML is approved after amplification pass, all five review files exist at their designated paths (copy-review.md, design-review.md, marketing-review.md, stress-test.md, bibliography.md), and the bibliographer has confirmed citation count. Last gate before the issue goes live. Runs pre-flight verification on all conditions, deploys to archive/YYYY-MM-DD-[slug].html (never index.html), updates Supabase, and writes the Obsidian stub.
---

# Phase 9 — Deploy

**Announce at start:** "I am running the phase-9-deploy skill."

## Overview

The final gate before an issue goes live. No deploy happens until all five review files exist, all metadata is correct, and the deploy target is confirmed as the archive path — never index.html. If any pre-flight check fails, the deploy is BLOCKED and the specific failure is named.

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

**Library check (open `archive/index.html` and verify):**
- [ ] BRIEFINGS array entry for this slug exists with correct date, title, format, dimension, and sources count
- [ ] Sources count in BRIEFINGS entry matches `<!-- meliorism2:sources: N -->` in the issue HTML

### Step 2: Deploy the issue

```bash
./deploy-api.sh "Issue: [title] — [dimension] — full pipeline complete" archive/YYYY-MM-DD-[slug].html
```

Confirm deploy succeeds before proceeding to Step 3.

### Step 3: Deploy library update if sources count was stale

If the BRIEFINGS array in `archive/index.html` required a sources count correction:

```bash
./deploy-api.sh "Library: update sources count for [slug]" archive/index.html
```

### Step 4: Supabase update

Insert row into the `issues` table:
- `slug`: YYYY-MM-DD-[slug]
- `title`: issue title
- `dimension`: dimension value from metadata
- `sources`: verified citation count
- `published_at`: today's date
- `status`: live

Update the matching `editorial_calendar` row:
- Set `status` → `live`

### Step 5: Obsidian stub

Write stub file:
`08 - The Intermodal Hub/Signal-OS/Issues/YYYY-MM-DD-[slug].md`

Stub content:
```markdown
# [Issue Title]

- Date: YYYY-MM-DD
- Slug: [slug]
- Dimension: [dimension]
- Sources: N
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

## Red Flags — STOP

- Deploy target contains `index.html` without the `archive/` path prefix — STOP immediately; this is a homepage-destroying error
- Any review file is absent — do not deploy; report BLOCKED and name which files are missing; a deploy without complete review is a trust failure, not a shortcut

## Iron Law

> **NO DEPLOY WITHOUT CONFIRMING TARGET IS `archive/YYYY-MM-DD-[slug].html` — NEVER `index.html`.**
>
> `index.html` IS THE PERMANENT LANDING PAGE. OVERWRITING IT DESTROYS THE HOMEPAGE. CONFIRM THE SLUG. CONFIRM THE PATH. THEN DEPLOY.

> **NO DEPLOY WITHOUT ALL FIVE REVIEW FILES PRESENT AT THEIR DESIGNATED PATHS.**
>
> A DEPLOY WITHOUT COMPLETE REVIEW IS A TRUST FAILURE. THE REVIEW FILES ARE THE PROOF THAT THE PIPELINE RAN. CHECK THEY EXIST BEFORE THE API CALL.
