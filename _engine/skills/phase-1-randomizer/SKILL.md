---
name: phase-1-randomizer
description: Use when beginning the Sunday production cycle for a new issue week and no factors file yet exists for that week. Produces the 33 influence factors that seed all downstream dimension agents.
---

# Phase 1: Randomizer

**Announce at start:** "I am running the phase-1-randomizer skill."

## Overview

Produces 33 influence factors for the week — a numbered, category-free list drawn from seven source pools. **The cross-domain pattern is the value; category headers destroy it.**

## When to Use

**Always:**
- Sunday of the production week
- `_engine/research/YYYY-WW/00-factors.md` does not yet exist

**Exceptions:**
- If `00-factors.md` already exists for the target week, stop immediately. Do not overwrite. Report the path and ask Brian to confirm before proceeding.

## Input

- Current calendar week (ISO week number)
- Live signal scan: news, field events, seasonal data, pop culture
- No prior file dependency — this is the root of the pipeline

## Process

### Step 1: Identify the Week

Confirm the ISO week number and year (format: `YYYY-WW`). Confirm the output path: `_engine/research/YYYY-WW/00-factors.md`. If the directory does not exist, create it.

Stop if the file already exists. Do not proceed.

### Step 2: Pull from Seven Source Pools

Draw factors from all seven pools every week. Minimum coverage per pool:

| Pool | Minimum draws | Examples |
|---|---|---|
| Calendar | 3 | holidays, full moons, sports finals, award seasons |
| News | 3 | what practitioners are reading and sharing this week |
| Field events | 3 | conference season, certification cycles, retreat season, back-to-school |
| Geographic | 2 | what is happening where practitioners physically work |
| Seasonal | 3 | body rhythms, daylight changes, temperature inflection points |
| Pop culture | 3 | film, music, viral moments, cultural memes with traction |
| Completely random | 3 | a 16th-century practice, a deep-sea discovery, a forgotten word, a mathematical curiosity — anything with zero obvious practitioner relevance |

Remaining factors (up to 33) can draw from any pool. The random pool should contribute at least 3 factors that have no obvious connection to social work or human services practice.

### Step 3: Assemble the List

Write all 33 factors as a numbered list, 1 through 33, one line each. No categories. No headers between items. No grouping by pool. The ordering should be non-obvious — do not cluster related items.

Each factor is a brief, specific phrase — not a sentence, not a question. Examples of correct format:
- `14. Summer solstice in the Northern Hemisphere`
- `22. "Petrichor" — smell of rain on dry earth`
- `31. FIFA Club World Cup group stage begins`

### Step 4: Write the File

Write to `_engine/research/YYYY-WW/00-factors.md`. No preamble. No metadata block. The file begins at `1.` and ends at `33.`

## Output

`_engine/research/YYYY-WW/00-factors.md`

A numbered list, 1–33, no categories, no headers, no prose. The file is complete when it contains exactly 33 items.

## Common Mistakes

**Adding category headers**
- Problem: Breaking the list into "Calendar," "News," "Seasonal" sections destroys the cross-domain signal. Dimension agents are supposed to see connections across pools, not within them.
- Fix: Remove all headers. Reorder items so items from the same pool are not adjacent.

**Fewer than 33 factors**
- Problem: Stopping at 25 or 28 because the list "feels complete."
- Fix: Count before filing. The number is not decorative — downstream agents use the full palette of 33. A short list creates blind spots in the week's coverage.

**Random factors that aren't random**
- Problem: Choosing "random" items that still relate to therapy, coaching, or human development.
- Fix: The random pool must include at least 3 items with zero obvious relevance to practice. A medieval salt tax. A species of jellyfish. A 1940s radio format. The value is the friction of forcing unexpected connections.

**Over-explaining a factor**
- Problem: Writing `14. Summer solstice (the longest day of the year, when practitioners may experience X…)` — the parenthetical kills the openness.
- Fix: One phrase. Let the dimension agent make the connection.

## Red Flags — STOP

- Fewer than 33 factors in the output file — report count and rebuild before filing
- `00-factors.md` already exists for the target week — stop, do not overwrite, report to Brian
- All 33 factors are drawn from calendar and news — no random pool items — report and re-pull

## Iron Law

> **33 FACTORS, NO CATEGORIES, EVERY WEEK. THE COUNT IS NOT DECORATIVE.**
