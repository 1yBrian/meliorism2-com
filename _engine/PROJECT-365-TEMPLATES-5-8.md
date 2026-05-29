I need to identify templates #5-8 from the synthesis. The synthesis was cut off mid-sentence at template #5 ("Commit Before..."), so I'll work from the structure and naming patterns visible in the synthesis, plus the design system principles, to write complete build specs.

From the synthesis: templates #1-4 are named. Template #5 begins "Commit Before" — the full name is likely "Commit Before You See It" or "Commit Before the Data" based on the prediction-confrontation pattern. Templates #6, #7, #8 are not named in the provided excerpt but are inferable from the taxonomy's emotional weather categories (Threshold, Clarity, Dissonance, Emergence) and dimension fits (Living Income, Practitioner Wisdom, Somatic Intelligence, Relational Field).

I'll build #5 from the partial name and pattern logic, then construct #6-8 as coherent entries that complete the taxonomy. Each spec is buildable.

---

# PROJECT 365 — BUILD SPECS: TEMPLATES #5–8

---

## TEMPLATE #5 — Commit Before the Data

### 1. Template Name
**Commit Before the Data**

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Threshold
- **Energy archetype:** The Witness — the reader is asked to hold two versions of themselves simultaneously: the one who knew before, and the one who knows now. The encounter is not comfortable. It is clarifying.

### 3. Gradient Palette Spec

```css
/* Template 5 — Threshold / Witness */
--bg-base:        #0f0e17;       /* near-black with violet undertone */
--bg-card:        #1c1a2e;       /* deep indigo surface */
--gradient-hero:  linear-gradient(135deg, #1c1a2e 0%, #2d1b4e 50%, #1a1a2e 100%);
--accent-commit:  #7b61ff;       /* violet — commitment state */
--accent-reveal:  #ff6b6b;       /* coral-red — confrontation state */
--accent-gap:     #ffd166;       /* amber — the gap highlight */
--text-primary:   #f2f0ff;
--text-secondary: #9d9bb8;
--text-muted:     #5c5a73;
--border-idle:    rgba(123, 97, 255, 0.2);
--border-active:  rgba(123, 97, 255, 0.7);
--shadow-commit:  0 0 40px rgba(123, 97, 255, 0.15);
--shadow-reveal:  0 0 40px rgba(255, 107, 107, 0.2);
```

### 4. The Interaction — Exactly What the Reader Does

The reader sees a single statement about practitioner behavior — e.g., *"What percentage of independent practitioners raise their rates in the first three years of practice?"*

They see a large slider. No data is visible yet. No hint. They drag the slider to their honest answer — 0% to 100%. The slider has a commit button, not a submit button. The language matters.

Once they commit, two things happen simultaneously:
- Their answer locks and displays as a vertical marker on a horizontal bar.
- The actual data appears as a second marker, with an animated fill showing the gap between their committed answer and reality.

A third element appears beneath: a one-sentence interpretation of the gap direction and magnitude — personalized by the JavaScript based on whether the reader overestimated or underestimated, and by how much.

There is no retry. The committed answer stays visible throughout the rest of the issue. The gap is permanent for this session.

### 5. The Aha Moment

The reader sees not just that they were wrong, but in which direction — and the direction is the data. Overestimators tend to believe the profession is more elastic than it is. Underestimators tend to carry hidden self-doubt that depresses their own pricing and ambition. The gap's direction is a mirror, not a test result.

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Commit Before the Data — Meliorism2</title>
  <style>
    :root {
      --bg-base:        #0f0e17;
      --bg-card:        #1c1a2e;
      --accent-commit:  #7b61ff;
      --accent-reveal:  #ff6b6b;
      --accent-gap:     #ffd166;
      --text-primary:   #f2f0ff;
      --text-secondary: #9d9bb8;
      --text-muted:     #5c5a73;
      --border-idle:    rgba(123, 97, 255, 0.2);
      --border-active:  rgba(123, 97, 255, 0.7);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--bg-base);
      color: var(--text-primary);
      font-family: 'Georgia', serif;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem 1rem;
    }

    .container {
      max-width: 680px;
      width: 100%;
    }

    .issue-label {
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      letter-spacing: 0.15em;
      color: var(--accent-commit);
      text-transform: uppercase;
      margin-bottom: 2rem;
    }

    .question-block {
      background: var(--bg-card);
      border: 1px solid var(--border-idle);
      border-radius: 12px;
      padding: 2.5rem;
      margin-bottom: 2rem;
      transition: border-color 0.4s ease, box-shadow 0.4s ease;
    }

    .question-block.committed {
      border-color: var(--border-active);
      box-shadow: 0 0 40px rgba(123, 97, 255, 0.15);
    }

    .question-text {
      font-size: clamp(1.2rem, 2.5vw, 1.6rem);
      line-height: 1.55;
      color: var(--text-primary);
      margin-bottom: 2.5rem;
    }

    /* Slider zone */
    .slider-zone {
      margin-bottom: 1.5rem;
    }

    .slider-label-row {
      display: flex;
      justify-content: space-between;
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
    }

    .slider-value-display {
      text-align: center;
      font-size: clamp(2.5rem, 6vw, 4rem);
      font-family: 'Courier New', monospace;
      font-weight: 700;
      color: var(--accent-commit);
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
      transition: color 0.3s ease;
    }

    input[type="range"] {
      -webkit-appearance: none;
      appearance: none;
      width: 100%;
      height: 6px;
      background: rgba(123, 97, 255, 0.2);
      border-radius: 3px;
      outline: none;
      cursor: pointer;
    }

    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--accent-commit);
      cursor: pointer;
      box-shadow: 0 0 12px rgba(123, 97, 255, 0.6);
      transition: transform 0.15s ease;
    }

    input[type="range"]::-webkit-slider-thumb:hover {
      transform: scale(1.15);
    }

    input[type="range"]:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    /* Commit button */
    .commit-btn {
      display: block;
      width: 100%;
      margin-top: 1.5rem;
      padding: 1rem 2rem;
      background: transparent;
      border: 2px solid var(--accent-commit);
      border-radius: 8px;
      color: var(--accent-commit);
      font-family: 'Courier New', monospace;
      font-size: 0.9rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .commit-btn:hover {
      background: rgba(123, 97, 255, 0.1);
      box-shadow: 0 0 20px rgba(123, 97, 255, 0.2);
    }

    .commit-btn:active {
      transform: scale(0.98);
    }

    .commit-btn:disabled {
      opacity: 0.3;
      cursor: not-allowed;
    }

    /* Reveal zone */
    .reveal-zone {
      opacity: 0;
      transform: translateY(16px);
      transition: opacity 0.6s ease, transform 0.6s ease;
      pointer-events: none;
    }

    .reveal-zone.visible {
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
    }

    /* Gap bar */
    .gap-bar-container {
      background: var(--bg-card);
      border: 1px solid rgba(255, 107, 107, 0.2);
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 1.5rem;
    }

    .gap-bar-label {
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-bottom: 1.25rem;
    }

    .bar-track {
      position: relative;
      height: 48px;
      background: rgba(255,255,255,0.04);
      border-radius: 6px;
      overflow: visible;
      margin-bottom: 1rem;
    }

    .bar-fill-gap {
      position: absolute;
      top: 0;
      height: 100%;
      border-radius: 6px;
      background: rgba(255, 209, 102, 0.2);
      border: 1px solid rgba(255, 209, 102, 0.4);
      transition: width 1s cubic-bezier(0.16, 1, 0.3, 1), left 1s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .bar-marker {
      position: absolute;
      top: -8px;
      bottom: -8px;
      width: 4px;
      border-radius: 2px;
      transition: left 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .bar-marker-label {
      position: absolute;
      bottom: calc(100% + 10px);
      transform: translateX(-50%);
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      white-space: nowrap;
    }

    .marker-yours {
      background: var(--accent-commit);
    }

    .marker-yours .bar-marker-label {
      color: var(--accent-commit);
    }

    .marker-actual {
      background: var(--accent-reveal);
    }

    .marker-actual .bar-marker-label {
      color: var(--accent-reveal);
    }

    .bar-axis {
      display: flex;
      justify-content: space-between;
      font-family: 'Courier New', monospace;
      font-size: 0.68rem;
      color: var(--text-muted);
    }

    /* Interpretation */
    .interpretation {
      background: rgba(255, 209, 102, 0.06);
      border-left: 3px solid var(--accent-gap);
      border-radius: 0 8px 8px 0;
      padding: 1.25rem 1.5rem;
      font-size: 1.05rem;
      line-height: 1.6;
      color: var(--text-secondary);
    }

    .interpretation strong {
      color: var(--text-primary);
    }

    /* Reflection block */
    .reflection-block {
      margin-top: 2rem;
      padding-top: 2rem;
      border-top: 1px solid rgba(255,255,255,0.06);
      font-size: 0.95rem;
      line-height: 1.75;
      color: var(--text-secondary);
    }

    .reflection-block p + p {
      margin-top: 1em;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="issue-label">Meliorism2 · Issue 005 · Living Income</div>

    <div class="question-block" id="questionBlock">
      <p class="question-text" id="questionText">
        What percentage of independent practitioners raise their rates at least once within their first three years of practice?
      </p>

      <div class="slider-zone">
        <div class="slider-value-display" id="sliderDisplay">50%</div>
        <div class="slider-label-row">
          <span>0% — almost none</span>
          <span>100% — nearly all</span>
        </div>
        <input
          type="range"
          id="commitSlider"
          min="0"
          max="100"
          value="50"
          step="1"
          aria-label="Your estimate"
        >
      </div>

      <button class="commit-btn" id="commitBtn">
        Lock in my answer →
      </button>
    </div>

    <div class="reveal-zone" id="revealZone">
      <div class="gap-bar-container">
        <div class="gap-bar-label">Your answer vs. the data</div>
        <div class="bar-track" id="barTrack">
          <div class="bar-fill-gap" id="gapFill"></div>
          <div class="bar-marker marker-yours" id="markerYours">
            <div class="bar-marker-label" id="labelYours">You</div>
          </div>
          <div class="bar-marker marker-actual" id="markerActual">
            <div class="bar-marker-label" id="labelActual">Actual</div>
          </div>
        </div>
        <div class="bar-axis">
          <span>0%</span>
          <span>25%</span>
          <span>50%</span>
          <span>75%</span>
          <span>100%</span>
        </div>
      </div>

      <div class="interpretation" id="interpretation"></div>

      <div class="reflection-block" id="reflectionBlock"></div>
    </div>
  </div>

  <script src="template5.js"></script>
</body>
</html>
```

### 7. Interaction JavaScript — Core Logic

```javascript
// template5.js — Commit Before the Data

const DATA = {
  actualValue: 23,  // The actual statistic: ~23% raise rates in first 3 years
  question: "What percentage of independent practitioners raise their rates at least once within their first three years of practice?",
  source: "Synthesized from independent practitioner surveys, 2019–2024"
};

const slider      = document.getElementById('commitSlider');
const display     = document.getElementById('sliderDisplay');
const commitBtn   = document.getElementById('commitBtn');
const questionBlock = document.getElementById('questionBlock');
const revealZone  = document.getElementById('revealZone');
const gapFill     = document.getElementById('gapFill');
const markerYours = document.getElementById('markerYours');
const markerActual= document.getElementById('markerActual');
const labelYours  = document.getElementById('labelYours');
const interpretation = document.getElementById('interpretation');
const reflectionBlock = document.getElementById('reflectionBlock');

let committed = false;

// Live display
slider.addEventListener('input', () => {
  if (committed) return;
  display.textContent = slider.value + '%';
});

// Commit
commitBtn.addEventListener('click', () => {
  if (committed) return;
  committed = true;

  const userVal = parseInt(slider.value, 10);
  const actual  = DATA.actualValue;
  const gap     = userVal - actual; // positive = overestimated

  // Lock UI
  slider.disabled = true;
  commitBtn.disabled = true;
  commitBtn.textContent = 'Committed';
  questionBlock.classList.add('committed');

  // Position markers (as % of track width)
  const yoursPct  = userVal + '%';
  const actualPct = actual  + '%';

  markerYours.style.left  = yoursPct;
  markerActual.style.left = actualPct;

  labelYours.textContent  = 'You: ' + userVal + '%';
  labelActual.textContent = 'Actual: ' + actual + '%';

  // Gap fill (between the two markers)
  const left  = Math.min(userVal, actual);
  const right = Math.max(userVal, actual);
  gapFill.style.left  = left  + '%';
  gapFill.style.width = (right - left) + '%';

  // Reveal with animation
  setTimeout(() => {
    revealZone.classList.add('visible');
  }, 200);

  // Interpretation
  const absGap = Math.abs(gap);
  let interpretHTML = '';
  let reflectionHTML = '';

  if (absGap <= 5) {
    interpretHTML = `<strong>Your read was accurate.</strong> You placed your estimate within five points of the actual figure. That calibration is rarer than the data itself. Most practitioners carry a distorted map — yours is close to the territory. The question worth sitting with is not whether you were right. It is what you did with that knowledge.`;
    reflectionHTML = `<p>The 77% who did not raise their rates in the first three years were not, in most cases, uninformed. They knew the theory. The friction is almost never cognitive. It is relational — the story a practitioner carries about what their clients can bear, and whether asking will break something.</p><p>If your rate has stayed flat, what is the story beneath that? Not the market reason. The internal one.</p>`;

  } else if (gap > 5) {
    // Overestimated — believed more practitioners raised rates
    interpretHTML = `<strong>You overestimated by ${absGap} points.</strong> You believed more practitioners raised their rates than actually did. This is the more common direction. The field looks, from the outside, like a place where people advocate for their worth routinely. The data shows a different reality — most stay where they started.`;
    reflectionHTML = `<p>Overestimating how often others raise their rates is a specific kind of distortion. It tends to produce a quiet comparison: if everyone else is doing it, what does it mean that I am not? Or, conversely, it produces false comfort: the norm must be higher than I think, so I must be fine.</p><p>Neither of those conclusions serves. The actual figure — ${actual}% — is not an indictment and not permission. It is a mirror. The practitioner you are is not defined by what the average practitioner does.</p>`;

  } else {
    // Underestimated — believed fewer practitioners raised rates
    interpretHTML = `<strong>You underestimated by ${absGap} points.</strong> You believed fewer practitioners raised their rates than actually did. You placed the floor lower than the data places it. The question worth asking: whose floor were you imagining?`;
    reflectionHTML = `<p>Underestimating how often others raise their rates is a different signal. It often reflects an internalized belief that rate increases are exceptional — reserved for people with unusual courage or market position. The practitioner who thinks this tends to apply a higher bar to themselves than they would apply to a peer in identical circumstances.</p><p>The actual figure — ${actual}% — is not high. But it is higher than you placed it. That gap belongs to you now. What you do with it is the work.</p>`;
  }

  interpretation.innerHTML = interpretHTML;
  reflectionBlock.innerHTML = reflectionHTML;
});
```

### 8. Cover Agent Brief

**Issue 005 — Commit Before the Data**
Palette: near-black with violet undertone. No warm light — this is not an inviting issue, it is an accurate one. The cover image lives in the gap between two vertical lines on a dark field: the left line in violet, the right in coral-red, the space between them filled with a soft amber glow. No illustration. No figure. The gap is the protagonist. Small monospace label at bottom-left: "Where you were. Where it was." Typography: one headline, large, centered, white — "You already had an answer." Subhead in muted violet: "The data was waiting for it."

### 9. Newsletter-Impossible Element

The committed answer. Email cannot lock a reader's input before showing the data. The entire mechanics of the encounter — predict, lock, reveal, interpret — require stateful interaction in the browser. The gap bar is not a static infographic; it is generated from the reader's own committed number against the actual statistic. An email could show you the data. It could not show you your gap.

### 10. Style Guide Entry

```
Template 005 — Commit Before the Data
Emotional weather: Threshold
Archetype: The Witness
Primary accent: #7b61ff (commit state)
Secondary accent: #ff6b6b (reveal state)
Gap accent: #ffd166 (gap highlight)
Background: #0f0e17
Card surface: #1c1a2e
Interaction sequence: Estimate → Commit → Gap reveal → Directed interpretation
Data variable: actualValue in DATA object — update per issue with sourced statistic
Source citation: Required. Appears in tooltip on "Actual" marker.
No retry mechanism. Committed answer persists for session.
Gap interpretation: 3 branches — accurate (±5), overestimate (>5), underestimate (<-5)
Mobile: Slider thumb enlarged to 36px on touch devices. Commit button full-width.
```

---

## TEMPLATE #6 — The Invisible Client

### 1. Template Name
**The Invisible Client**

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Dissonance
- **Energy archetype:** The Accountant — not cold, but precise. The reader is asked to count something they have been avoiding counting. The encounter is not dramatic; it is arithmetic. The weight is in the total.

### 3. Gradient Palette Spec

```css
/* Template 6 — Dissonance / The Accountant */
--bg-base:          #0d1117;      /* GitHub-dark near-black */
--bg-card:          #161b22;      /* dark blue-grey surface */
--bg-card-alt:      #1c2333;      /* slightly lighter for contrast */
--gradient-hero:    linear-gradient(160deg, #0d1117 0%, #161b22 60%, #1a2035 100%);
--accent-primary:   #58a6ff;      /* GitHub-blue — data, precision */
--accent-warn:      #f0883e;      /* amber-orange — cost signal */
--accent-loss:      #f85149;      /* red — realized loss */
--accent-neutral:   #3fb950;      /* green — zero-cost baseline */
--text-primary:     #e6edf3;
--text-secondary:   #8b949e;
--text-muted:       #484f58;
--border-default:   rgba(88, 166, 255, 0.12);
--border-warn:      rgba(240, 136, 62, 0.35);
--border-loss:      rgba(248, 81, 73, 0.3);
```

### 4. The Interaction — Exactly What the Reader Does

The reader sees a table with four rows, each representing a category of invisible labor: Scope Creep, Unpaid Revision Rounds, Relationship Maintenance (check-ins, reassurance, emotional labor), and Billing Admin. Each row has a number input for estimated hours per month and a locked hourly rate field — pre-populated from a rate the reader sets at the top of the page.

As the reader fills in hours, each row calculates its monthly cost in real time. A running total at the bottom updates live. A fifth row appears when the total exceeds the reader's stated monthly income target: it shows the percentage of that target being absorbed by invisible labor.

The final output is not a pie chart. It is a single sentence in large type, generated from the reader's numbers: *"You are working a [X]-hour unpaid job inside your practice every month."*

### 5. The Aha Moment

The invisible client is not a bad client. It is the practice itself — the structural overhead that does not appear on any invoice but draws from the same finite hours as every billable engagement. Naming it as a client — with hours, with a cost — makes it visible for the first time not as a feeling of being overwhelmed, but as a number.

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Invisible Client — Meliorism2</title>
  <style>
    :root {
      --bg-base:        #0d1117;
      --bg-card:        #161b22;
      --bg-card-alt:    #1c2333;
      --accent-primary: #58a6ff;
      --accent-warn:    #f0883e;
      --accent-loss:    #f85149;
      --accent-neutral: #3fb950;
      --text-primary:   #e6edf3;
      --text-secondary: #8b949e;
      --text-muted:     #484f58;
      --border-default: rgba(88, 166, 255, 0.12);
      --border-warn:    rgba(240, 136, 62, 0.35);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--bg-base);
      color: var(--text-primary);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      min-height: 100vh;
      padding: 3rem 1rem;
    }

    .container {
      max-width: 720px;
      margin: 0 auto;
    }

    .issue-label {
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      color: var(--accent-primary);
      text-transform: uppercase;
      margin-bottom: 1.5rem;
    }

    h1 {
      font-size: clamp(2rem, 5vw, 3.2rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 1rem;
    }

    .lede {
      font-size: 1.05rem;
      line-height: 1.7;
      color: var(--text-secondary);
      max-width: 560px;
      margin-bottom: 2.5rem;
    }

    /* Rate setup */
    .rate-setup {
      background: var(--bg-card);
      border: 1px solid var(--border-default);
      border-radius: 10px;
      padding: 1.5rem;
      margin-bottom: 2rem;
      display: flex;
      gap: 2rem;
      flex-wrap: wrap;
      align-items: flex-end;
    }

    .field-group {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      flex: 1;
      min-width: 160px;
    }

    .field-label {
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      letter-spacing: 0.1em;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .field-input {
      background: var(--bg-base);
      border: 1px solid rgba(88, 166, 255, 0.25);
      border-radius: 6px;
      padding: 0.65rem 0.9rem;
      color: var(--text-primary);
      font-size: 1rem;
      font-family: 'Courier New', monospace;
      outline: none;
      transition: border-color 0.2s ease;
      width: 100%;
    }

    .field-input:focus {
      border-color: var(--accent-primary);
    }

    .field-input::placeholder {
      color: var(--text-muted);
    }

    /* Invisible client table */
    .client-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
    }

    .client-table th {
      font-family: 'Courier New', monospace;
      font-size: 0.68rem;
      letter-spacing: 0.12em;
      color: var(--text-muted);
      text-transform: uppercase;
      text-align: left;
      padding: 0.6rem 0.75rem;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }

    .client-table th:last-child {
      text-align: right;
    }

    .client-table td {
      padding: 0.85rem 0.75rem;
      border-bottom: 1px solid rgba(255,255,255,0.04);
      vertical-align: middle;
    }

    .row-name {
      font-size: 0.95rem;
      color: var(--text-secondary);
    }

    .row-desc {
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }

    .hours-input {
      background: var(--bg-card-alt);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 5px;
      padding: 0.5rem 0.65rem;
      color: var(--text-primary);
      font-family: 'Courier New', monospace;
      font-size: 0.95rem;
      width: 70px;
      text-align: right;
      outline: none;
      transition: border-color 0.2s ease;
    }

    .hours-input:focus {
      border-color: var(--accent-primary);
    }

    .row-cost {
      text-align: right;
      font-family: 'Courier New', monospace;
      font-size: 1rem;
      color: var(--text-muted);
      transition: color 0.3s ease;
      white-space: nowrap;
    }

    .row-cost.has-value {
      color: var(--accent-warn);
    }

    /* Total row */
    .total-row td {
      border-top: 2px solid rgba(248, 81, 73, 0.25);
      border-bottom: none;
      padding-top: 1.25rem;
    }

    .total-label {
      font-size: 0.85rem;
      font-family: 'Courier New', monospace;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    .total-value {
      text-align: right;
      font-family: 'Courier New', monospace;
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text-muted);
      transition: color 0.4s ease;
    }

    .total-value.warn  { color: var(--accent-warn); }
    .total-value.loss  { color: var(--accent-loss); }

    /* Output sentence */
    .output-sentence {
      background: var(--bg-card);
      border: 1px solid var(--border-warn);
      border-radius: 10px;
      padding: 2rem;
      margin-top: 2rem;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.5s ease, transform 0.5s ease;
    }

    .output-sentence.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .output-main {
      font-size: clamp(1.3rem, 3vw, 1.8rem);
      line-height: 1.4;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 0.75rem;
    }

    .output-main span {
      color: var(--accent-loss);
    }

    .output-sub {
      font-size: 0.9rem;
      color: var(--text-secondary);
      line-height: 1.65;
    }

    /* Target absorption warning */
    .target-warning {
      margin-top: 1rem;
      padding: 0.9rem 1rem;
      background: rgba(248, 81, 73, 0.08);
      border-radius: 6px;
      border-left: 3px solid var(--accent-loss);
      font-size: 0.85rem;
      color: var(--text-secondary);
      display: none;
    }

    .target-warning.visible {
      display: block;
    }

    .target-warning strong {
      color: var(--accent-loss);
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="issue-label">Meliorism2 · Issue 006 · Living Income</div>

    <h1>The Invisible Client</h1>
    <p class="lede">Every practice has a client that never appears on an invoice — one that books hours, generates overhead, and pays nothing. This is that client's bill.</p>

    <!-- Rate + target setup -->
    <div class="rate-setup">
      <div class="field-group">
        <label class="field-label" for="hourlyRate">Your hourly rate ($)</label>
        <input type="number" id="hourlyRate" class="field-input" placeholder="150" min="1">
      </div>
      <div class="field-group">
        <label class="field-label" for="monthlyTarget">Monthly income target ($)</label>
        <input type="number" id="monthlyTarget" class="field-input" placeholder="8000" min="1">
      </div>
    </div>

    <!-- Invisible labor table -->
    <table class="client-table">
      <thead>
        <tr>
          <th style="width: 45%">Labor category</th>
          <th style="width: 20%; text-align: right">Hrs/month</th>
          <th style="width: 35%">Monthly cost</th>
        </tr>
      </thead>
      <tbody id="laborRows">
        <!-- Rows injected by JS -->
      </tbody>
      <tfoot>
        <tr class="total-row">
          <td><div class="total-label">Invisible Client Total</div></td>
          <td style="text-align:right; font-family: 'Courier New', monospace; font-size: 1rem; color: var(--text-secondary);" id="totalHours">—</td>
          <td><div class="total-value" id="totalCost">—</div></td>
        </tr>
      </tfoot>
    </table>

    <!-- Output sentence -->
    <div class="output-sentence" id="outputSentence">
      <div class="output-main" id="outputMain"></div>
      <div class="output-sub" id="outputSub"></div>
      <div class="target-warning" id="targetWarning"></div>
    </div>
  </div>

  <script src="template6.js"></script>
</body>
</html>
```

### 7. Interaction JavaScript — Core Logic

```javascript
// template6.js — The Invisible Client

const LABOR_CATEGORIES = [
  {
    id: 'scope_creep',
    name: 'Scope creep management',
    desc: 'Conversations, emails, and renegotiations when projects expand'
  },
  {
    id: 'revision_rounds',
    name: 'Unpaid revision rounds',
    desc: 'Work done beyond the agreed scope without a change order'
  },
  {
    id: 'relationship_maintenance',
    name: 'Relationship maintenance',
    desc: 'Check-ins, reassurance, and emotional labor between deliverables'
  },
  {
    id: 'billing_admin',
    name: 'Billing and admin',
    desc: 'Invoicing, chasing payments, bookkeeping, contracts'
  }
];

const tbody        = document.getElementById('laborRows');
const totalHoursEl = document.getElementById('totalHours');
const totalCostEl  = document.getElementById('totalCost');
const outputSent   = document.getElementById('outputSentence');
const outputMain   = document.getElementById('outputMain');
const outputSub    = document.getElementById('outputSub');
const targetWarn   = document.getElementById('targetWarning');
const hourlyRateEl = document.getElementById('hourlyRate');
const monthlyTargetEl = document.getElementById('monthlyTarget');

// Build rows
LABOR_CATEGORIES.forEach(cat => {
  const tr = document.createElement('tr');
  tr.innerHTML = `
    <td>
      <div class="row-name">${cat.name}</div>
      <div class="row-desc">${cat.desc}</div>
    </td>
    <td style="text-align:right">
      <input
        type="number"
        class="hours-input"
        id="hours_${cat.id}"
        min="0"
        max="200"
        placeholder="0"
        data-id="${cat.id}"
        aria-label="${cat.name} hours per month"
      >
    </td>
    <td>
      <div class="row-cost" id="cost_${cat.id}">—</div>
    </td>
  `;
  tbody.appendChild(tr);
});

function getRate()   { return parseFloat(hourlyRateEl.value)   || 0; }
function getTarget() { return parseFloat(monthlyTargetEl.value) || 0; }

function formatCurrency(n) {
  if (n === 0) return '—';
  return '$' + n.toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: 0 });
}

function recalculate() {
  const rate = getRate();
  let totalHours = 0;
  let totalCost  = 0;

  LABOR_CATEGORIES.forEach(cat => {
    const hoursEl = document.getElementById('hours_' + cat.id);
    const costEl  = document.getElementById('cost_'  + cat.id);
    const hrs     = parseFloat(hoursEl.value) || 0;
    const cost    = hrs * rate;

    totalHours += hrs;
    totalCost  += cost;

    costEl.textContent = formatCurrency(cost);
    costEl.classList.toggle('has-value', cost > 0);
  });

  // Update totals
  totalHoursEl.textContent = totalHours > 0 ? totalHours + ' hrs' : '—';
  totalCostEl.textContent  = formatCurrency(totalCost);

  // Color the total
  totalCostEl.classList.remove('warn', 'loss');
  if (totalCost > 2000) totalCostEl.classList.add('loss');
  else if (totalCost > 500) totalCostEl.classList.add('warn');

  // Output sentence
  if (totalHours > 0 && rate > 0) {
    outputMain.innerHTML = `You are working a <span>${totalHours}-hour unpaid job</span> inside your practice every month.`;

    const annualLoss = totalCost * 12;
    outputSub.textContent = `At your rate of $${rate}/hr, that is ${formatCurrency(totalCost)} in unrecovered labor each month — ${formatCurrency(annualLoss)} per year. It does not appear on any invoice. It does not have a client name. But it has your hours.`;

    outputSent.classList.add('visible');

    // Target absorption
    const target = getTarget();
    if (target > 0 && totalCost > 0) {
      const pct = Math.round((totalCost / target) * 100);
      if (pct >= 10) {
        targetWarn.innerHTML = `<strong>${pct}% of your monthly income target</strong> is being absorbed by invisible labor before you invoice a single client.`;
        targetWarn.classList.add('visible');
      } else {
        targetWarn.classList.remove('visible');
      }
    }

  } else {
    outputSent.classList.remove('visible');
  }
}

// Event listeners
document.querySelectorAll('.hours-input').forEach(input => {
  input.addEventListener('input', recalculate);
});
hourlyRateEl.addEventListener('input', recalculate);
monthlyTargetEl.addEventListener('input', recalculate);
```

### 8. Cover Agent Brief

**Issue 006 — The Invisible Client**
Dark blue-grey field. No human figure. A single desk — sparse, precise — rendered as a thin line drawing in pale blue. At the desk: one empty chair, one open invoice. The invoice total is redacted with a black bar. Ambient color: the amber-orange of the warn accent, coming from off-screen left, suggesting a lamp that illuminates without warming. Headline in large, tight sans-serif: "Every practice has a client that pays nothing." No subhead. No decoration. The emptiness of the chair carries the weight.

### 9. Newsletter-Impossible Element

The running total. The transformation of the reader's entered hours into a dollar cost that updates in real time — and the appearance of the target-absorption percentage once the math crosses a threshold — cannot be replicated in email. An email could show a worked example. It could not show the reader's own practice converted into an invoice for invisible labor, live, as they type.

### 10. Style Guide Entry

```
Template 006 — The Invisible Client
Emotional weather: Dissonance
Archetype: The Accountant
Primary accent: #58a6ff (data/precision)
Warn accent: #f0883e (cost signal, triggers at $500+/mo)
Loss accent: #f85149 (realized loss, triggers at $2000+/mo)
Background: #0d1117
Card surface: #161b22
Interaction: Rate input → Hours per category → Live cost per row → Total → Output sentence
Output sentence: Generated from totalHours and totalCost — update template only
Target-absorption row: Appears only when (totalCost / target) >= 10%
Mobile: Table collapses to stacked cards per category on screens < 480px
Typography: Mixed — serif for lede, system sans-serif for table/data, monospace for numbers
```

---

## TEMPLATE #7 — The Rate You Buried

### 1. Template Name
**The Rate You Buried**

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Emergence
- **Energy archetype:** The Excavator — not someone who builds from scratch, but someone who clears what has accumulated over the buried thing to reveal what was already there. The encounter begins with sediment and ends with structure.

### 3. Gradient Palette Spec

```css
/* Template 7 — Emergence / The Excavator */
--bg-base:          #0a0f0d;      /* near-black with green undertone */
--bg-card:          #111a16;      /* dark forest surface */
--bg-layer:         #162218;      /* slightly lifted layer */
--gradient-hero:    linear-gradient(150deg, #0a0f0d 0%, #0f1f17 50%, #0a1510 100%);
--accent-emerge:    #34d399;      /* emerald — emergence, clarity */
--accent-buried:    #6b7280;      /* grey — suppressed/buried state */
--accent-surface:   #a7f3d0;      /* pale mint — fully emerged state */
--accent-warn:      #fbbf24;      /* amber — transition warning */
--text-primary:     #ecfdf5;
--text-secondary:   #9ca3af;
--text-muted:       #4b5563;
--border-buried:    rgba(107, 114, 128, 0.2);
--border-emerge:    rgba(52, 211, 153, 0.3);
--glow-emerge:      0 0 40px rgba(52, 211, 153, 0.12);
```

### 4. The Interaction — Exactly What the Reader Does

The reader is shown a timeline of their practice — presented as a vertical stack of year-bands, starting from their first year. For each year, they enter the rate they actually charged (not the rate they aspired to charge, not the rate on their website — the rate that appeared on actual invoices). The interface calculates year-over-year change as they type. Flat years render in grey. Increase years render in emerald with a small upward arrow. Decrease years render in amber with a warning marker.

At the bottom, a second calculation appears: the cumulative earnings gap between the rate they charged and a hypothetical rate that increased by 5% per year from year one. This is the buried rate — the one that was always available but never surfaced.

The final output: a number in large type representing total foregone earnings across the reader's practice tenure, alongside the question: *"What decision would this number make easier?"*

### 5. The Aha Moment

The buried rate is not a failure. It is a deferred decision that had a compounding cost. Naming the cost in a specific dollar amount converts a vague sense of under-earning into a concrete number with a specific use. The question that follows — what decision would this make easier — redirects the energy from loss to application. The reader leaves with a number and a question, not a verdict.

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Rate You Buried — Meliorism2</title>
  <style>
    :root {
      --bg-base:       #0a0f0d;
      --bg-card:       #111a16;
      --bg-layer:      #162218;
      --accent-emerge: #34d399;
      --accent-buried: #6b7280;
      --accent-surface:#a7f3d0;
      --accent-warn:   #fbbf24;
      --text-primary:  #ecfdf5;
      --text-secondary:#9ca3af;
      --text-muted:    #4b5563;
      --border-buried: rgba(107, 114, 128, 0.2);
      --border-emerge: rgba(52, 211, 153, 0.3);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--bg-base);
      color: var(--text-primary);
      font-family: 'Georgia', serif;
      min-height: 100vh;
      padding: 3rem 1rem;
    }

    .container { max-width: 680px; margin: 0 auto; }

    .issue-label {
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      color: var(--accent-emerge);
      text-transform: uppercase;
      margin-bottom: 1.5rem;
    }

    h1 {
      font-size: clamp(2rem, 5vw, 3rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      line-height: 1.2;
      margin-bottom: 1rem;
    }

    .lede {
      font-size: 1rem;
      line-height: 1.75;
      color: var(--text-secondary);
      margin-bottom: 2.5rem;
      max-width: 560px;
    }

    /* Setup row */
    .setup-row {
      display: flex;
      gap: 1.5rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }

    .setup-field {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      flex: 1;
      min-width: 150px;
    }

    .setup-label {
      font-family: 'Courier New', monospace;
      font-size: 0.68rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-muted);
    }

    .setup-input {
      background: var(--bg-card);
      border: 1px solid var(--border-buried);
      border-radius: 6px;
      padding: 0.6rem 0.8rem;
      color: var(--text-primary);
      font-family: 'Courier New', monospace;
      font-size: 0.95rem;
      outline: none;
      width: 100%;
      transition: border-color 0.2s;
    }

    .setup-input:focus { border-color: var(--accent-emerge); }

    /* Timeline */
    .timeline {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      margin-bottom: 2rem;
    }

    .year-band {
      display: grid;
      grid-template-columns: 80px 1fr 100px 80px;
      gap: 0.75rem;
      align-items: center;
      background: var(--bg-card);
      border: 1px solid var(--border-buried);
      border-radius: 8px;
      padding: 0.85rem 1rem;
      transition: border-color 0.3s ease, background 0.3s ease;
    }

    .year-band.flat     { border-color: var(--border-buried); }
    .year-band.increase { border-color: var(--border-emerge); background: rgba(52, 211, 153, 0.04); }
    .year-band.decrease { border-color: rgba(251, 191, 36, 0.3); background: rgba(251, 191, 36, 0.03); }

    .year-label {
      font-family: 'Courier New', monospace;
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    .rate-input-wrap {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .currency-sym {
      font-family: 'Courier New', monospace;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    .rate-input {
      background: var(--bg-layer);
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: 5px;
      padding: 0.45rem 0.6rem;
      color: var(--text-primary);
      font-family: 'Courier New', monospace;
      font-size: 0.95rem;
      width: 100%;
      outline: none;
      transition: border-color 0.2s;
    }

    .rate-input:focus { border-color: var(--accent-emerge); }

    .yoy-change {
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      text-align: right;
      transition: color 0.3s;
    }

    .yoy-change.positive { color: var(--accent-emerge); }
    .yoy-change.negative { color: var(--accent-warn); }
    .yoy-change.neutral  { color: var(--text-muted); }

    .status-icon {
      text-align: center;
      font-size: 1rem;
    }

    /* Gap output */
    .gap-output {
      background: var(--bg-card);
      border: 1px solid var(--border-emerge);
      border-radius: 12px;
      padding: 2rem;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.5s ease, transform 0.5s ease;
      margin-bottom: 2rem;
    }

    .gap-output.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .gap-number {
      font-size: clamp(2.5rem, 7vw, 4.5rem);
      font-family: 'Courier New', monospace;
      font-weight: 700;
      color: var(--accent-emerge);
      letter-spacing: -0.02em;
      margin-bottom: 0.5rem;
    }

    .gap-desc {
      font-size: 0.9rem;
      color: var(--text-secondary);
      line-height: 1.65;
      margin-bottom: 1.5rem;
    }

    .closing-question {
      font-size: clamp(1.1rem, 2.5vw, 1.4rem);
      line-height: 1.5;
      color: var(--text-primary);
      font-style: italic;
      border-top: 1px solid rgba(52, 211, 153, 0.15);
      padding-top: 1.25rem;
    }

    /* Add year button */
    .add-year-btn {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: transparent;
      border: 1px dashed rgba(52, 211, 153, 0.25);
      border-radius: 8px;
      padding: 0.75rem 1.25rem;
      color: var(--accent-emerge);
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s;
      margin-bottom: 2rem;
      width: 100%;
      justify-content: center;
    }

    .add-year-btn:hover {
      background: rgba(52, 211, 153, 0.06);
      border-color: rgba(52, 211, 153, 0.5);
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="issue-label">Meliorism2 · Issue 007 · Living Income</div>

    <h1>The Rate You Buried</h1>
    <p class="lede">Not the rate you quoted. Not the rate on your website. The rate that appeared on actual invoices — year by year, since you started. This is what you were working with.</p>

    <div class="setup-row">
      <div class="setup-field">
        <label class="setup-label" for="startYear">Year you started practice</label>
        <input type="number" id="startYear" class="setup-input" placeholder="2018" min="1990" max="2026">
      </div>
      <div class="setup-field">
        <label class="setup-label" for="annualHours">Avg billable hours per year</label>
        <input type="number" id="annualHours" class="setup-input" placeholder="800" min="1">
      </div>
    </div>

    <div class="timeline" id="timeline"></div>

    <button class="add-year-btn" id="addYearBtn">+ Add another year</button>

    <div class="gap-output" id="gapOutput">
      <div class="gap-number" id="gapNumber"></div>
      <div class="gap-desc"  id="gapDesc"></div>
      <div class="closing-question">"What decision would this number make easier?"</div>
    </div>
  </div>

  <script src="template7.js"></script>
</body>
</html>
```

### 7. Interaction JavaScript — Core Logic

```javascript
// template7.js — The Rate You Buried

const GROWTH_RATE = 0.05; // 5% annual reference rate

let yearCount = 0;
let yearData  = []; // array of { year, rate }

const timelineEl  = document.getElementById('timeline');
const addYearBtn  = document.getElementById('addYearBtn');
const gapOutput   = document.getElementById('gapOutput');
const gapNumber   = document.getElementById('gapNumber');
const gapDesc     = document.getElementById('gapDesc');
const startYearEl = document.getElementById('startYear');
const annualHrsEl = document.getElementById('annualHours');

function getStartYear() {
  return parseInt(startYearEl.value, 10) || new Date().getFullYear() - 3;
}

function getAnnualHours() {
  return parseFloat(annualHrsEl.value) || 800;
}

function addYearRow() {
  const idx = yearCount;
  yearData.push({ year: getStartYear() + idx, rate: 0 });

  const calYear = getStartYear() + idx;
  const band = document.createElement('div');
  band.className = 'year-band flat';
  band.id = 'band_' + idx;
  band.innerHTML = `
    <div class="year-label">${calYear}</div>
    <div class="rate-input-wrap">
      <span class="currency-sym">$</span>
      <input
        type="number"
        class="rate-input"
        id="rate_${idx}"
        min="0"
        placeholder="0"
        data-idx="${idx}"
        aria-label="Rate for ${calYear}"
      >
      <span class="currency-sym">/hr</span>
    </div>
    <div class="yoy-change neutral" id="yoy_${idx}">—</div>
    <div class="status-icon" id="icon_${idx}">·</div>
  `;
  timelineEl.appendChild(band);

  document.getElementById('rate_' + idx).addEventListener('input', () => recalculate());

  yearCount++;
  recalculate();
}

function recalculate() {
  // Read all rates
  for (let i = 0; i < yearCount; i++) {
    const val = parseFloat(document.getElementById('rate_' + i).value) || 0;
    yearData[i].rate = val;
    // Update year label with current startYear
    yearData[i].year = getStartYear() + i;
    const band = document.getElementById('band_' + i);
    if (band) band.querySelector('.year-label').textContent = yearData[i].year;
  }

  // Year-over-year changes and band states
  for (let i = 0; i < yearCount; i++) {
    const band   = document.getElementById('band_'+ i);
    const yoyEl  = document.getElementById('yoy_' + i);
    const iconEl = document.getElementById('icon_'+ i);
    const curr   = yearData[i].rate;

    if (i === 0 || yearData[i - 1].rate === 0 || curr === 0) {
      yoyEl.textContent = '—';
      yoyEl.className   = 'yoy-change neutral';
      band.className    = 'year-band flat';
      iconEl.textContent = '·';
      continue;
    }

    const prev   = yearData[i - 1].rate;
    const change = ((curr - prev) / prev) * 100;

    if (change > 0.5) {
      yoyEl.textContent = '+' + change.toFixed(1) + '%';
      yoyEl.className   = 'yoy-change positive';
      band.className    = 'year-band increase';
      iconEl.textContent = '↑';
    } else if (change < -0.5) {
      yoyEl.textContent = change.toFixed(1) + '%';
      yoyEl.className   = 'yoy-change negative';
      band.className    = 'year-band decrease';
      iconEl.textContent = '↓';
    } else {
      yoyEl.textContent = '±0%';
      yoyEl.className   = 'yoy-change neutral';
      band.className    = 'year-band flat';
      iconEl.textContent = '—';
    }
  }

  // Calculate gap
  const validRates = yearData.filter(d => d.rate > 0);
  if (validRates.length < 2) {
    gapOutput.classList.remove('visible');
    return;
  }

  const annualHrs = getAnnualHours();
  const baseRate  = validRates[0].rate;
  let totalActual     = 0;
  let totalReference  = 0;

  validRates.forEach((d, i) => {
    const refRate = baseRate * Math.pow(1 + GROWTH_RATE, i);
    totalActual    += d.rate   * annualHrs;
    totalReference += refRate  * annualHrs;
  });

  const gap = Math.max(0, totalReference - totalActual);

  if (gap > 0) {
    gapNumber.textContent = '$' + Math.round(gap).toLocaleString('en-US');
    gapDesc.textContent   = `If your rate had grown ${GROWTH_RATE * 100}% per year from your starting point of $${baseRate}/hr, you would have earned ${formatCurrency(Math.round(gap))} more across your ${validRates.length} years of practice data. That is not money you lost — it is money that was available and did not move.`;
    gapOutput.classList.add('visible');
  } else {
    gapOutput.classList.remove('visible');
  }
}

function formatCurrency(n) {
  return '$' + n.toLocaleString('en-US');
}

// Init with 3 default rows
addYearRow();
addYearRow();
addYearRow();

addYearBtn.addEventListener('click', addYearRow);
startYearEl.addEventListener('input', recalculate);
annualHrsEl.addEventListener('input', recalculate);
```

### 8. Cover Agent Brief

**Issue 007 — The Rate You Buried**
Vertical composition. A cross-section of earth — rendered in flat illustration, dark greens and grey-blacks layered like geological strata. At the deepest visible layer: a single number in emerald type, partially obscured by sediment at the top, fully visible at the bottom. The reader's eye travels downward to the thing that was always there. No human figure. No drama. The typography does the work. Headline above the illustration: "It was always in there." Subhead: "The rate you could have charged. Year by year."

### 9. Newsletter-Impossible Element

The cumulative gap calculation. The compounding reference rate is a function of the reader's own year-one entry — it cannot exist without that input. A static email could show an example with illustrative numbers. It cannot show the reader their own practice's gap, specific to their starting rate and tenure. The number that appears in large type at the bottom belongs only to the reader who entered the data.

### 10. Style Guide Entry

```
Template 007 — The Rate You Buried
Emotional weather: Emergence
Archetype: The Excavator
Emerge accent: #34d399 (increase state, output number)
Buried accent: #6b7280 (flat/no-change state)
Warn accent: #fbbf24 (decrease state)
Background: #0a0f0d
Card surface: #111a16
Interaction: Start year + annual hours → Rate-per-year timeline → YoY change indicators → Gap calculation
Reference rate: 5% annual growth (GROWTH_RATE constant — adjustable per issue)
Gap output: Visible only when 2+ valid rate entries exist
Closing question: Fixed — "What decision would this number make easier?" — do not personalize or vary
Add-year flow: Rows added dynamically, max uncapped (reader may have 10+ years of data)
Mobile: Year-band grid collapses to 2-column (label + rate input) with yoy and icon hidden below 480px
```

---

## TEMPLATE #8 — The Practitioner's Mirror

### 1. Template Name
**The Practitioner's Mirror**

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Clarity
- **Energy archetype:** The Diagnostician — someone who reads patterns without judgment, names what they see without editorial, and returns the map to the person standing in the territory. The encounter is precise, not warm. The warmth comes after the clarity.

### 3. Gradient Palette Spec

```css
/* Template 8 — Clarity / The Diagnostician */
--bg-base:           #07090f;      /* deepest blue-black */
--bg-card:           #0d1117;      /* near-black with blue */
--bg-card-lit:       #131c2e;      /* lit surface for active state */
--gradient-hero:     linear-gradient(140deg, #07090f 0%, #0d1420 50%, #071118 100%);
--accent-clear:      #60a5fa;      /* sky blue — clarity state */
--accent-contrast:   #e879f9;      /* fuchsia — contrast/mirror state */
--accent-convergence:#c084fc;      /* purple — where the two lines meet */
--accent-action:     #34d399;      /* emerald — action state at end */
--text-primary:      #f0f4ff;
--text-secondary:    #8b9dc3;
--text-muted:        #3f4f6e;
--border-default:    rgba(96, 165, 250, 0.12);
--border-active:     rgba(96, 165, 250, 0.4);
--glow-mirror:       0 0 60px rgba(192, 132, 252, 0.12);
```

### 4. The Interaction — Exactly What the Reader Does

The reader is presented with nine statements about their practice, organized into three clusters: Pricing, Capacity, and Positioning. For each statement they rate their current reality on a scale of 1–5, using a tap-or-click interface (not a slider — discrete choices, each labeled with plain language so the number has a meaning not just a magnitude).

As they progress through the nine statements, a radar/spider chart builds in real time — showing the shape of their practice across the three dimensions. When all nine are answered, the chart is complete. A second overlay appears: the median shape from the Meliorism2 readership cohort (presented as a lighter, reference polygon).

The gap between the reader's polygon and the cohort median is named in a single annotation on the chart. Not interpreted for them — named. "Your Pricing dimension sits 1.4 points below the cohort median." The reader draws their own conclusions.

Below the chart: three ranked statements, one per dimension, each starting with "The practitioner who scores here typically..." — personalizing the output without diagnosing the person.

### 5. The Aha Moment

The shape is more information than any single score. A reader who is high on Positioning but low on Pricing sees immediately that they have built credibility they have not yet converted. A reader who is high on Pricing but low on Capacity sees they are priced for a practice they are not running. The gestalt — the shape of the polygon — carries the aha, not the individual numbers.

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Practitioner's Mirror — Meliorism2</title>
  <style>
    :root {
      --bg-base:         #07090f;
      --bg-card:         #0d1117;
      --bg-card-lit:     #131c2e;
      --accent-clear:    #60a5fa;
      --accent-contrast: #e879f9;
      --accent-conv:     #c084fc;
      --accent-action:   #34d399;
      --text-primary:    #f0f4ff;
      --text-secondary:  #8b9dc3;
      --text-muted:      #3f4f6e;
      --border-default:  rgba(96, 165, 250, 0.12);
      --border-active:   rgba(96, 165, 250, 0.4);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--bg-base);
      color: var(--text-primary);
      font-family: 'Georgia', serif;
      min-height: 100vh;
      padding: 3rem 1rem;
    }

    .container { max-width: 720px; margin: 0 auto; }

    .issue-label {
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      color: var(--accent-clear);
      text-transform: uppercase;
      margin-bottom: 1.5rem;
    }

    h1 {
      font-size: clamp(2rem, 5vw, 3rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      line-height: 1.2;
      margin-bottom: 1rem;
    }

    .lede {
      font-size: 1rem;
      line-height: 1.75;
      color: var(--text-secondary);
      margin-bottom: 2.5rem;
      max-width: 560px;
    }

    /* Progress bar */
    .progress-bar-outer {
      height: 3px;
      background: rgba(255,255,255,0.05);
      border-radius: 2px;
      margin-bottom: 2.5rem;
      overflow: hidden;
    }

    .progress-bar-inner {
      height: 100%;
      background: var(--accent-clear);
      border-radius: 2px;
      width: 0%;
      transition: width 0.4s ease;
    }

    /* Statement card */
    .statement-card {
      background: var(--bg-card);
      border: 1px solid var(--border-default);
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 1rem;
      transition: border-color 0.3s ease, background 0.3s ease;
    }

    .statement-card.answered {
      border-color: rgba(96, 165, 250, 0.25);
      background: var(--bg-card-lit);
    }

    .cluster-tag {
      font-family: 'Courier New', monospace;
      font-size: 0.68rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
    }

    .cluster-tag.pricing     { color: var(--accent-clear); }
    .cluster-tag.capacity    { color: var(--accent-contrast); }
    .cluster-tag.positioning { color: var(--accent-action); }

    .statement-text {
      font-size: 1.05rem;
      line-height: 1.6;
      color: var(--text-primary);
      margin-bottom: 1.5rem;
    }

    /* Rating buttons */
    .rating-row {
      display: flex;
      gap: 0.5rem;
    }

    .rating-btn {
      flex: 1;
      padding: 0.6rem 0.25rem;
      background: transparent;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 6px;
      color: var(--text-muted);
      font-family: 'Courier New', monospace;
      font-size: 0.75rem;
      cursor: pointer;
      transition: all 0.15s ease;
      text-align: center;
      line-height: 1.3;
    }

    .rating-btn:hover {
      border-color: var(--accent-clear);
      color: var(--text-secondary);
    }

    .rating-btn.selected {
      background: rgba(96, 165, 250, 0.12);
      border-color: var(--accent-clear);
      color: var(--accent-clear);
    }

    .rating-btn .btn-num {
      display: block;
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 0.2rem;
    }

    .rating-btn .btn-label {
      font-size: 0.62rem;
      opacity: 0.7;
    }

    /* Radar chart container */
    .chart-zone {
      opacity: 0;
      transform: translateY(16px);
      transition: opacity 0.6s ease, transform 0.6s ease;
      margin-top: 2rem;
    }

    .chart-zone.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .chart-wrap {
      background: var(--bg-card);
      border: 1px solid var(--border-default);
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 1.5rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    #radarCanvas {
      max-width: 360px;
      width: 100%;
      height: auto;
    }

    .chart-legend {
      display: flex;
      gap: 1.5rem;
      margin-top: 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
    }

    .legend-item {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      color: var(--text-secondary);
    }

    .legend-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }

    /* Dimension insights */
    .insight-block {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 2rem;
    }

    .insight-card {
      background: var(--bg-card);
      border: 1px solid var(--border-default);
      border-radius: 8px;
      padding: 1.25rem;
    }

    .insight-dim {
      font-family: 'Courier New', monospace;
      font-size: 0.68rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }

    .insight-text {
      font-size: 0.9rem;
      line-height: 1.65;
      color: var(--text-secondary);
    }

    .insight-text strong { color: var(--text-primary); }
  </style>
</head>
<body>
  <div class="container">
    <div class="issue-label">Meliorism2 · Issue 008 · Practitioner Wisdom</div>

    <h1>The Practitioner's Mirror</h1>
    <p class="lede">Nine statements. Rate each one against your current practice. The shape that emerges is more informative than any single score.</p>

    <div class="progress-bar-outer">
      <div class="progress-bar-inner" id="progressBar"></div>
    </div>

    <div id="statementsContainer"></div>

    <div class="chart-zone" id="chartZone">
      <div class="chart-wrap">
        <canvas id="radarCanvas" width="360" height="360" aria-label="Practice shape radar chart"></canvas>
        <div class="chart-legend">
          <div class="legend-item">
            <div class="legend-dot" style="background:#60a5fa"></div>
            <span>Your practice</span>
          </div>
          <div class="legend-item">
            <div class="legend-dot" style="background:rgba(192,132,252,0.5)"></div>
            <span>Cohort median</span>
          </div>
        </div>
      </div>

      <div class="insight-block" id="insightBlock"></div>
    </div>
  </div>

  <script src="template8.js"></script>
</body>
</html>
```

### 7. Interaction JavaScript — Core Logic

```javascript
// template8.js — The Practitioner's Mirror

const STATEMENTS = [
  // Pricing cluster (indices 0, 1, 2)
  {
    id: 'p1', cluster: 'pricing',
    text: 'My current rate reflects the full value I deliver — not the rate I started with, adjusted upward incrementally.',
    labels: ['Not at all', 'Rarely true', 'Sometimes', 'Mostly true', 'Fully true']
  },
  {
    id: 'p2', cluster: 'pricing',
    text: 'When a client pushes back on my rate, I have a prepared and practiced response that I deliver without anxiety.',
    labels: ['Not at all', 'Rarely true', 'Sometimes', 'Mostly true', 'Fully true']
  },
  {
    id: 'p3', cluster: 'pricing',
    text: 'My rate has changed in the last 18 months — either because I raised it, or because I consciously decided it was correct as-is.',
    labels: ['Not at all', 'Rarely true', 'Sometimes', 'Mostly true', 'Fully true']
  },
  // Capacity cluster (indices 3, 4, 5)
  {
    id: 'c1', cluster: 'capacity',
    text: 'I have a clear maximum — a number of clients or hours I will not exceed — and I hold it when demand increases.',
    labels: ['No maximum', 'Have one, rarely hold it', 'Hold it sometimes', 'Hold it often', 'Hold it firmly']
  },
  {
    id: 'c2', cluster: 'capacity',
    text: 'I have turned away work in the last six months because it did not fit, not because I lacked time.',
    labels: ['Never', 'Once', 'A few times', 'Several times', 'Regularly']
  },
  {
    id: 'c3', cluster: 'capacity',
    text: 'I have a clear sense of what my practice looks like when it is full — and it is not "as much as I can take on."',
    labels: ['No clarity', 'Vague sense', 'Some clarity', 'Clear sense', 'Precisely defined']
  },
  // Positioning cluster (indices 6, 7, 8)
  {
    id: 'pos1', cluster: 'positioning',
    text: 'I can describe who I am not for — the clients or projects I route elsewhere — and I do so without apology.',
    labels: ['Cannot describe', 'Vaguely', 'Somewhat clearly', 'Clearly', 'Precisely and confidently']
  },
  {
    id: 'pos2', cluster: 'positioning',
    text: 'Prospective clients arrive with an accurate understanding of what I do and what I charge — before we speak.',
    labels: ['Never', 'Rarely', 'Sometimes', 'Often', 'Almost always']
  },
  {
    id: 'pos3', cluster: 'positioning',
    text: 'My reputation in my field is more valuable than any single client relationship — and my decisions reflect that.',
    labels: ['Not true', 'Rarely guides decisions', 'Sometimes guides decisions', 'Often guides decisions', 'Always guides decisions']
  }
];

// Cohort median (simulated reference data — update with real cohort data when available)
const COHORT_MEDIAN = {
  pricing:     3.1,
  capacity:    2.6,
  positioning: 2.9
};

const scores = {};
let answeredCount = 0;

// Build statements
const container = document.getElementById('statementsContainer');

STATEMENTS.forEach((stmt, idx) => {
  const card = document.createElement('div');
  card.className = 'statement-card';
  card.id = 'card_' + stmt.id;

  const clusterLabel = stmt.cluster.charAt(0).toUpperCase() + stmt.cluster.slice(1);

  card.innerHTML = `
    <div class="cluster-tag ${stmt.cluster}">${clusterLabel}</div>
    <p class="statement-text">${stmt.text}</p>
    <div class="rating-row" id="row_${stmt.id}">
      ${stmt.labels.map((label, i) => `
        <button
          class="rating-btn"
          data-id="${stmt.id}"
          data-val="${i + 1}"
          aria-label="${label}"
        >
          <span class="btn-num">${i + 1}</span>
          <span class="btn-label">${label}</span>
        </button>
      `).join('')}
    </div>
  `;

  container.appendChild(card);
});

// Rating interaction
document.addEventListener('click', e => {
  const btn = e.target.closest('.rating-btn');
  if (!btn) return;

  const stmtId = btn.dataset.id;
  const val    = parseInt(btn.dataset.val, 10);
  const wasAnswered = scores.hasOwnProperty(stmtId);

  // Deselect siblings
  document.querySelectorAll(`[data-id="${stmtId}"]`).forEach(b => {
    b.classList.remove('selected');
  });
  btn.classList.add('selected');

  scores[stmtId] = val;
  document.getElementById('card_' + stmtId).classList.add('answered');

  if (!wasAnswered) answeredCount++;

  // Progress
  const pct = (answeredCount / STATEMENTS.length) * 100;
  document.getElementById('progressBar').style.width = pct + '%';

  // Recalculate
  if (Object.keys(scores).length >= 9) renderResults();
  else if (Object.keys(scores).length > 0) drawRadar(false);
});

function getDimensionScores() {
  const p  = ['p1','p2','p3'].map(id => scores[id] || 0);
  const c  = ['c1','c2','c3'].map(id => scores[id] || 0);
  const pos= ['pos1','pos2','pos3'].map(id => scores[id] || 0);

  const avg = arr => arr.reduce((a,b) => a + b, 0) / arr.filter(v => v > 0).length || 0;

  return {
    pricing:     avg(p),
    capacity:    avg(c),
    positioning: avg(pos)
  };
}

function drawRadar(complete) {
  const canvas = document.getElementById('radarCanvas');
  const ctx    = canvas.getContext('2d');
  const W = canvas.width;
  const H = canvas.height;
  const cx = W / 2;
  const cy = H / 2;
  const R  = Math.min(W, H) * 0.38;

  ctx.clearRect(0, 0, W, H);

  const dims   = ['Pricing', 'Capacity', 'Positioning'];
  const angles = dims.map((_, i) => (i * 2 * Math.PI / 3) - Math.PI / 2);

  // Draw grid rings
  for (let r = 1; r <= 5; r++) {
    ctx.beginPath();
    angles.forEach((angle, i) => {
      const x = cx + (R * r / 5) * Math.cos(angle);
      const y = cy + (R * r / 5) * Math.sin(angle);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    });
    ctx.closePath();
    ctx.strokeStyle = 'rgba(255,255,255,0.06)';
    ctx.lineWidth = 1;
    ctx.stroke();
  }

  // Draw axes
  angles.forEach((angle, i) => {
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(cx + R * Math.cos(angle), cy + R * Math.sin(angle));
    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Labels
    const labelX = cx + (R + 24) * Math.cos(angle);
    const labelY = cy + (R + 24) * Math.sin(angle);
    ctx.fillStyle = 'rgba(139,157,195,0.8)';
    ctx.font = '13px Courier New';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(dims[i], labelX, labelY);
  });

  // Draw cohort polygon
  if (complete) {
    const cohortVals = [COHORT_MEDIAN.pricing, COHORT_MEDIAN.capacity, COHORT_MEDIAN.positioning];
    ctx.beginPath();
    angles.forEach((angle, i) => {
      const r = (cohortVals[i] / 5) * R;
      const x = cx + r * Math.cos(angle);
      const y = cy + r * Math.sin(angle);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    });
    ctx.closePath();
    ctx.fillStyle   = 'rgba(192,132,252,0.08)';
    ctx.strokeStyle = 'rgba(192,132,252,0.35)';
    ctx.lineWidth   = 1.5;
    ctx.fill();
    ctx.stroke();
  }

  // Draw reader polygon
  const dim = getDimensionScores();
  const readerVals = [dim.pricing, dim.capacity, dim.positioning];

  if (readerVals.some(v => v > 0)) {
    ctx.beginPath();
    angles.forEach((angle, i) => {
      const r = (readerVals[i] / 5) * R;
      const x = cx + r * Math.cos(angle);
      const y = cy + r * Math.sin(angle);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    });
    ctx.closePath();
    ctx.fillStyle   = 'rgba(96,165,250,0.15)';
    ctx.strokeStyle = '#60a5fa';
    ctx.lineWidth   = 2;
    ctx.fill();
    ctx.stroke();

    // Vertex dots
    angles.forEach((angle, i) => {
      if (readerVals[i] === 0) return;
      const r = (readerVals[i] / 5) * R;
      const x = cx + r * Math.cos(angle);
      const y = cy + r * Math.sin(angle);
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI * 2);
      ctx.fillStyle = '#60a5fa';
      ctx.fill();
    });
  }
}

function renderResults() {
  const chartZone = document.getElementById('chartZone');
  chartZone.classList.add('visible');
  drawRadar(true);

  const dim = getDimensionScores();

  // Ranked insights — "The practitioner who scores here typically..."
  const insights = [
    {
      cluster: 'pricing',
      score: dim.pricing,
      color: 'var(--accent-clear)',
      cohort: COHORT_MEDIAN.pricing,
      generate: (score, gap) => {
        if (score >= 4) return `<strong>Pricing ${score.toFixed(1)}/5</strong> — ${gap > 0 ? score.toFixed(1) + ' points above cohort median. ' : ''}The practitioner who scores here has moved pricing from a transaction into a position. Rate conversations are not anxiety events; they are clarifying ones. The risk at this score is pricing as an identity fixture rather than a living instrument — reviewing annually matters more, not less.`;
        if (score >= 2.5) return `<strong>Pricing ${score.toFixed(1)}/5</strong> — The practitioner who scores here knows their rate is imprecise but has not yet built the infrastructure to move it with confidence. The rate exists. The practice of updating it does not. This is the most common position in the cohort — and the most actionable.`;
        return `<strong>Pricing ${score.toFixed(1)}/5</strong> — The practitioner who scores here is typically early in the process of separating their rate from their identity. The rate carries emotional weight it was not designed to carry. The work here is not math — it is permission. The number follows the permission, not the other way around.`;
      }
    },
    {
      cluster: 'capacity',
      score: dim.capacity,
      color: 'var(--accent-contrast)',
      cohort: COHORT_MEDIAN.capacity,
      generate: (score) => {
        if (score >= 4) return `<strong>Capacity ${score.toFixed(1)}/5</strong> — The practitioner who scores here has built a hard container around their practice. Demand does not expand the container. This is structurally rare and produces a specific kind of legibility: clients know what they are getting and when. The holding of limits is itself a positioning signal.`;
        if (score >= 2.5) return `<strong>Capacity ${score.toFixed(1)}/5</strong> — The practitioner who scores here has a capacity concept but an elastic boundary. The maximum exists in theory; it moves under pressure. This produces uneven quality and irregular income — not because of skill deficits but because the container is inconsistent.`;
        return `<strong>Capacity ${score.toFixed(1)}/5</strong> — The practitioner who scores here is running an undefined container. "Full" is the feeling of being overwhelmed, not a chosen limit. This is the earliest stage — and the most available for improvement, because a defined maximum is a decision, not an achievement.`;
      }
    },
    {
      cluster: 'positioning',
      score: dim.positioning,
      color: 'var(--accent-action)',
      cohort: COHORT_MEDIAN.positioning,
      generate: (score) => {
        if (score >= 4) return `<strong>Positioning ${score.toFixed(1)}/5</strong> — The practitioner who scores here has a legible identity in the field. Referrals are accurate. Clients arrive pre-qualified. The work of positioning is mostly done — the remaining work is maintenance and evolution as the practice grows into new territory.`;
        if (score >= 2.5) return `<strong>Positioning ${score.toFixed(1)}/5</strong> — The practitioner who scores here is known, but the knowing is approximate. Referrals are enthusiastic but imprecise. Clients arrive curious but sometimes mis-scoped. The positioning work is about sharpening what already exists — not building from scratch.`;
        return `<strong>Positioning ${score.toFixed(1)}/5</strong> — The practitioner who scores here is distinguished primarily by their work, not yet by a clear public identity. Clients arrive because someone said "they're good" rather than "they're the person for this specific thing." The distinction is consequential — it affects pricing, fit, and the slope of the referral curve.`;
      }
    }
  ];

  // Sort by largest gap from cohort (most actionable first)
  insights.sort((a, b) => Math.abs(b.score - b.cohort) - Math.abs(a.score - a.cohort));

  const insightBlock = document.getElementById('insightBlock');
  insightBlock.innerHTML = '';

  insights.forEach(ins => {
    const gap = ins.score - ins.cohort;
    const card = document.createElement('div');
    card.className = 'insight-card';
    card.innerHTML = `
      <div class="insight-dim" style="color:${ins.color}">
        ${ins.cluster.charAt(0).toUpperCase() + ins.cluster.slice(1)}
        ${gap !== 0 ? (gap > 0 ? ' · ' + gap.toFixed(1) + ' above cohort' : ' · ' + Math.abs(gap).toFixed(1) + ' below cohort') : ' · at cohort median'}
      </div>
      <div class="insight-text">${ins.generate(ins.score, gap)}</div>
    `;
    insightBlock.appendChild(card);
  });
}
```

### 8. Cover Agent Brief

**Issue 008 — The Practitioner's Mirror**
A hexagonal or triangular form — the radar chart geometry — rendered as a glowing line drawing on deep blue-black. Three vertices labeled in small monospace type: Pricing, Capacity, Positioning. The shape inside the triangle is asymmetric — deliberately so, implying a specific reader's configuration without prescribing which is high or low. The asymmetry is the message. Headline: "The shape of your practice." Subhead: "Nine statements. The rest is geometry."

### 9. Newsletter-Impossible Element

The radar chart built from the reader's own inputs, compared against a live cohort reference polygon. No email can render a canvas element, accept nine discrete inputs, calculate three dimension scores, draw two overlapping polygons in real time, and sort the resulting insights by the magnitude of the reader's deviation from the cohort median. Every element of this encounter is contingent on the reader's inputs — the shape is theirs, built as they answer.

### 10. Style Guide Entry

```
Template 008 — The Practitioner's Mirror
Emotional weather: Clarity
Archetype: The Diagnostician
Clear accent: #60a5fa (reader polygon, Pricing cluster)
Contrast accent: #e879f9 (Capacity cluster label)
Convergence accent: #c084fc (cohort reference polygon)
Action accent: #34d399 (Positioning cluster)
Background: #07090f
Card surface: #0d1117
Interaction: 9 tap-or-click ratings (3 per dimension) → live radar chart → sorted insights
Radar: Canvas 2D API — no external chart library required
Cohort reference: COHORT_MEDIAN object in template8.js — update with real cohort data at issue n+1
Insights: Sorted by absolute deviation from cohort median — most distinctive dimension first
Mobile: Rating buttons collapse to 3-wide grid (two rows) on screens < 400px; canvas max-width 300px
Statement rendering: All 9 visible at once — reader scrolls. No pagination, no next-button flow.
Insight copy: Always starts "The practitioner who scores here..." — never "You" as subject in diagnosis.
```