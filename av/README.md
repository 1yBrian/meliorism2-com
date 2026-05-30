# Meliorism2 Immersive AV Engine
*Lives at `/av/` so it's publicly served. Loaded by every issue via `<script type="module" src="/av/engine.js">`.*
*Source of design law: `_engine/DESIGN-ENGINE.md` (7 weather gradients, 4 generative layers, the three Laws).*

---

## What this is

The AV engine is what makes a Meliorism2 issue **not a blog**. Every issue declares a *weather* via metadata; the engine renders a quiet, deliberate, never-bombarding visual atmosphere (and optionally audio) that puts the reader inside an environment before they read a word.

This is not a frontend animation library. It is the **architectural layer** that distinguishes a Meliorism2 issue from any other thing on the open web. The engine + the prose are not separable — together they are the issue.

---

## What this is NOT

- Not a slideshow
- Not a parallax effect
- Not "delightful micro-interactions"
- Not autoplay video
- Not a music player

If any of the above describe what it's doing, it's wrong and needs to be redesigned.

---

## Neuro-spicy / accessibility commitments (non-negotiable)

These are the rules. Violations are gate failures.

1. **`prefers-reduced-motion: reduce` is respected at boot.** Engine paints exactly one static frame and stops. The reader can opt back in via the visible motion toggle.
2. **Audio is always OFF by default.** No exception. The audio toggle is visible but unlit; reader must explicitly enable.
3. **No sudden bright movement.** No flashes faster than 2 seconds. No high-contrast strobing. No element jumps from dark to bright in less than a 1.5s ease.
4. **All controls are visible, reachable by Tab, and ARIA-labeled.** Bottom-right pill cluster.
5. **Hidden tab pauses everything.** Page Visibility API. CPU is sacred.
6. **Engine never touches article prose.** Static-DOM-first: AI crawlers, screen readers, and JS-disabled visitors get the full article.
7. **Frame budget: < 5ms per frame on modern hardware.** Drop frames before introducing jank.
8. **Total engine + one mode + audio scaffold: < 30KB unminified.**

---

## File map

```
/av/
├── engine.js              — boot, metadata read, canvas mount, controls, audio
├── modes/
│   ├── friction.js        — ✅ live  (amber heat blobs, pulse every ~38s)
│   ├── clarity.js         — 🟡 placeholder (gradient only)
│   ├── surge.js           — 🟡 placeholder
│   ├── threshold.js       — 🟡 placeholder
│   ├── solidarity.js      — 🟡 placeholder
│   ├── fog.js             — 🟡 placeholder
│   └── delight.js         — 🟡 placeholder
├── proof.html             — standalone demo (switch modes, toggle audio)
└── README.md              — this file
```

---

## How an issue uses it

In the issue's HTML `<head>`:

```html
<!-- meliorism2:av-mode: friction -->
<!-- meliorism2:av-intensity: subtle -->
<!-- meliorism2:av-audio: drone -->
<!-- meliorism2:av-palette: amber -->
<script type="module" src="/av/engine.js" defer></script>
```

The engine mounts a `<canvas id="av-canvas">` with `position:fixed; z-index:-1` behind everything. The article HTML is unchanged.

No build step. No bundler. Modern browsers handle ES module imports natively.

---

## The 7 weather modes — what each one feels like

| Weather | Felt as | Visual grammar | Status |
|---------|---------|----------------|--------|
| ☀️ Clarity | morning intelligence briefing | cool teal-green, slow single light source rising | placeholder |
| ⚡ Surge | something about to happen | violet base, slow building tension lines | placeholder |
| 🌊 Threshold | the moment before a belief changes | violet-grey, held suspension, faint ripple | placeholder |
| 🌿 Solidarity | practitioner-to-practitioner recognition | warm green field, soft particles | placeholder |
| 🌧️ Friction | pressure about to release | amber heat blobs, slow pulses ✅ | **live** |
| 🌫️ Fog | uncertainty worth sitting with | blue-grey particulate, slow drift | placeholder |
| ✨ Delight | earned reward, beautiful for its own sake | gold sparks, gentle | placeholder |

Each mode is a self-contained ES module with two exports:

```js
export function draw(ctx, t, w, h, meta) { /* per-frame paint */ }
export function drawStatic(ctx, w, h, meta) { /* one frame for reduced-motion */ }
```

A mode file should be **under 200 lines** and **under 5ms per frame**. Compose with sin/cos and small numbers of `createRadialGradient` calls — avoid pixel-level manipulation.

---

## How to add a new mode

1. Drop a new file at `/av/modes/<weather>.js` with the two required exports
2. Set the weather palette anchors from `_engine/DESIGN-ENGINE.md` §7 Weather Gradients
3. Test in `/av/proof.html` — open `?mode=<weather>` to preview
4. Run `python3 _engine/scripts/system_audit.py` — it should report the new mode is live
5. Use the mode in an issue via `<!-- meliorism2:av-mode: <weather> -->`

---

## Audio scaffolding (minimal)

- Single low-pass-filtered sine oscillator + a slightly detuned partner for warmth
- Frequency keyed to weather (lower for Friction, higher for Delight)
- Gain ramps in over 3 seconds — never sudden
- Gain ramps out over 1 second when toggled off
- No melody, no chord changes, no rhythm — sustained drone only

The audio is intentionally simple. Music would compete with reading. The drone is room tone — felt, not noticed.

---

## Performance + audit hooks

- `python3 _engine/scripts/system_audit.py` knows about each weather mode and reports which are placeholders vs live
- A future check can measure per-mode frame time in CI via Playwright + Performance API

---

## What's queued next

In order of priority:
1. **Implement Solidarity** — needed for any Witnessing / Brave Spaces / In-Person Presence issue
2. **Implement Clarity** — needed for Living Income / Critical Consciousness
3. **Implement Threshold** — needed for the highest-impact issues
4. **Implement Delight** — for the delight-card screens
5. **Implement Fog, Surge** — round out the 7
6. **Optional 8th mode "Threshold-Earned-Dark"** — the precedent from Issue 027 (Tide Chart)
7. **Wire the engine into the daily-release pipeline** so every new issue picks up the engine by default
8. **Backfill the engine into past issues** as part of the no-grandfathering protocol

---

*The engine is what makes Meliorism2 a publication, not a blog. Updated by Zen at every milestone.*
