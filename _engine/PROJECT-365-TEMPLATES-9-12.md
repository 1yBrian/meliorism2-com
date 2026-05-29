Now I have the full picture. This agent (me, `top-templates-9-12`) was called with only the first 3000 chars of synthesis and 2000 chars of design system. The synthesis truncates mid-template #5 in the prompt, meaning templates #9-12 were **not defined in the truncated synthesis passed to this agent** — they need to be constructed consistent with the taxonomy.

I now have everything I need to write authoritative specs for templates #9-12. Based on the synthesis taxonomy, the templates are ranked by: newsletter-impossible rating (5/5 prioritized), emotional weather coverage, build complexity (low first), and dimension fit coverage. Templates #1-4 cover: Living Income (2x Clarity), Practitioner Wisdom/Clarity, and Practitioner Wisdom/Clarity. I need to continue the taxonomy with templates that cover different weather states, dimensions, and interaction types not yet used.

Let me now write the complete build specs.

---

# PROJECT 365 — COMPLETE BUILD SPECS: TEMPLATES #9-12
## Plus: The Quick Win Sprint Plan (30-Day Schedule for Templates #1-12)

---

# TEMPLATE #9 — THE BURDEN MAP

---

**1. Template name:** The Burden Map

**2. Emotional weather and energy archetype**
- Emotional weather: Threshold (the moment before something becomes unsustainable)
- Energy archetype: The Witness — still, observant, not urgent; creates space for the reader to see something clearly for the first time

---

**3. Gradient palette spec**

```css
:root {
  --bg: #0f0e17;
  --surface: #1a1826;
  --surface-raised: #221f34;
  --accent: #c77dff;
  --accent-warm: #e0aaff;
  --accent-danger: #ff6b6b;
  --text-primary: #fffffe;
  --text-secondary: #a7a9be;
  --text-muted: #6c6f8a;
  --gradient: linear-gradient(135deg, #0f0e17 0%, #1a1033 50%, #2d1b4e 100%);
  --gradient-accent: linear-gradient(90deg, #c77dff 0%, #e0aaff 100%);
  --border: rgba(199, 125, 255, 0.15);
  --glow: 0 0 24px rgba(199, 125, 255, 0.12);
}
```

Visual effect: Deep violet-black with cool purple undertone. The reader feels they are in a late-night audit of themselves — private, honest, slightly heavy. Not alarming. Clarifying.

---

**4. The interaction — what the reader does**

The reader sees a blank canvas with the prompt: *"List everything you are currently holding."* Below it: a simple text input with an Add button and a category selector (Work commitments / Client relationships / Unfinished admin / Things I said I'd do / Things I'm waiting on).

As they add items, each one appears as a weighted card on a visual map. Weight is set by a single slider on each card: 1 (light) to 5 (heavy). The cards self-arrange on the canvas by weight — heavier items drift toward the center. When the total weight score crosses predefined thresholds (8, 16, 24), a faint colored ring appears around the center with a quiet label: *Manageable → Loaded → Unsustainable*.

There is a second layer: the reader can tag each item *Mine to carry* or *Carrying for someone else.* When they toggle this, the card moves to one of two columns. A running ratio updates at the top: *X% is yours. Y% belongs to someone else.*

A final button: *Show me the invisible labor* — toggles a calculated view showing the estimated mental overhead (in hours/week) if each item at weight 3+ demands at least 20 minutes of background cognitive churn daily.

---

**5. The aha moment**

The reader sees, for the first time, the ratio of burden they are holding for others versus themselves — and the total mental overhead as a number of hours per week, not a vague sense of overwhelm. The weight map makes visible what the mind holds diffusely.

---

**6. HTML structure**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Burden Map</title>
  <style>
    /* CSS custom properties from palette spec above */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text-primary);
      font-family: 'Inter', system-ui, sans-serif;
      min-height: 100vh;
      padding: 2rem 1.5rem;
    }

    .issue-header {
      max-width: 680px;
      margin: 0 auto 3rem;
    }
    .issue-header .weather-tag {
      font-size: 0.75rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 0.75rem;
    }
    .issue-header h1 {
      font-size: clamp(2.4rem, 6vw, 4.8rem);
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -0.03em;
      color: var(--text-primary);
      margin-bottom: 1rem;
    }
    .issue-header .lede {
      font-size: 1.15rem;
      line-height: 1.65;
      color: var(--text-secondary);
      max-width: 540px;
    }

    /* Input zone */
    .add-zone {
      max-width: 680px;
      margin: 0 auto 2rem;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      display: flex;
      gap: 0.75rem;
      align-items: center;
      flex-wrap: wrap;
    }
    .add-zone input[type="text"] {
      flex: 1;
      min-width: 200px;
      background: transparent;
      border: none;
      color: var(--text-primary);
      font-size: 1rem;
      outline: none;
      padding: 0.25rem 0;
    }
    .add-zone input::placeholder { color: var(--text-muted); }
    .add-zone select {
      background: var(--surface-raised);
      border: 1px solid var(--border);
      color: var(--text-secondary);
      border-radius: 6px;
      padding: 0.4rem 0.75rem;
      font-size: 0.85rem;
    }
    .add-zone button {
      background: var(--gradient-accent);
      border: none;
      border-radius: 6px;
      color: #0f0e17;
      font-weight: 700;
      font-size: 0.9rem;
      padding: 0.5rem 1.25rem;
      cursor: pointer;
      white-space: nowrap;
    }

    /* Stats bar */
    .stats-bar {
      max-width: 680px;
      margin: 0 auto 1.5rem;
      display: flex;
      gap: 2rem;
      align-items: center;
      font-size: 0.9rem;
      color: var(--text-muted);
    }
    .stats-bar .ratio-label {
      font-size: 0.95rem;
      color: var(--text-primary);
      font-weight: 600;
    }
    .stats-bar .threshold-indicator {
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }
    .threshold-manageable { background: rgba(100, 220, 150, 0.15); color: #64dc96; }
    .threshold-loaded     { background: rgba(255, 200, 80,  0.15); color: #ffc850; }
    .threshold-crisis     { background: rgba(255, 107, 107, 0.15); color: #ff6b6b; }

    /* Card grid */
    .burden-grid {
      max-width: 680px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .burden-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1rem 1.25rem;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .burden-card[data-weight="4"],
    .burden-card[data-weight="5"] {
      border-color: rgba(199, 125, 255, 0.35);
      box-shadow: var(--glow);
    }
    .burden-card .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.75rem;
    }
    .burden-card .item-text {
      font-size: 1rem;
      color: var(--text-primary);
      line-height: 1.4;
      flex: 1;
      margin-right: 1rem;
    }
    .burden-card .item-category {
      font-size: 0.75rem;
      color: var(--text-muted);
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .burden-card .weight-row {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .burden-card .weight-label {
      font-size: 0.8rem;
      color: var(--text-muted);
      width: 60px;
    }
    .burden-card input[type="range"] {
      flex: 1;
      accent-color: var(--accent);
      cursor: pointer;
    }
    .burden-card .weight-value {
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      width: 1.5rem;
      text-align: right;
    }
    .burden-card .ownership-toggle {
      margin-top: 0.75rem;
      display: flex;
      gap: 0.5rem;
    }
    .ownership-btn {
      font-size: 0.75rem;
      padding: 0.3rem 0.7rem;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s;
    }
    .ownership-btn.active {
      background: rgba(199, 125, 255, 0.15);
      border-color: var(--accent);
      color: var(--accent);
    }
    .burden-card .delete-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1rem;
      padding: 0.2rem;
      opacity: 0.5;
      transition: opacity 0.15s;
    }
    .burden-card .delete-btn:hover { opacity: 1; }

    /* Invisible labor reveal */
    .invisible-labor-btn {
      max-width: 680px;
      margin: 2rem auto 0;
      display: block;
      width: 100%;
      padding: 1rem;
      background: transparent;
      border: 1px dashed var(--border);
      border-radius: 10px;
      color: var(--text-muted);
      font-size: 0.95rem;
      cursor: pointer;
      transition: all 0.2s;
    }
    .invisible-labor-btn:hover {
      border-color: var(--accent);
      color: var(--accent);
    }

    .labor-reveal {
      max-width: 680px;
      margin: 1.5rem auto 0;
      background: var(--surface);
      border: 1px solid rgba(199, 125, 255, 0.3);
      border-radius: 12px;
      padding: 1.5rem;
      display: none;
    }
    .labor-reveal.visible { display: block; }
    .labor-reveal h3 {
      font-size: 0.85rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 1rem;
    }
    .labor-number {
      font-size: clamp(2.5rem, 7vw, 5rem);
      font-weight: 800;
      color: var(--text-primary);
      letter-spacing: -0.04em;
      line-height: 1;
    }
    .labor-unit {
      font-size: 1rem;
      color: var(--text-secondary);
      margin-top: 0.5rem;
    }
  </style>
</head>
<body>
  <div class="issue-header">
    <div class="weather-tag">Threshold · The Witness</div>
    <h1>The Burden Map</h1>
    <p class="lede">List everything you are currently holding. Every commitment, every waiting item, every thing you said yes to. Then watch it take shape.</p>
  </div>

  <div class="add-zone">
    <input type="text" id="item-input" placeholder="What are you carrying right now?" />
    <select id="category-select">
      <option value="work">Work commitments</option>
      <option value="client">Client relationships</option>
      <option value="admin">Unfinished admin</option>
      <option value="promised">Things I said I'd do</option>
      <option value="waiting">Things I'm waiting on</option>
    </select>
    <button id="add-btn">Add</button>
  </div>

  <div class="stats-bar">
    <span class="ratio-label" id="ratio-display">Add items to see your ratio</span>
    <span class="threshold-indicator threshold-manageable" id="threshold-display" style="display:none"></span>
  </div>

  <div class="burden-grid" id="burden-grid"></div>

  <button class="invisible-labor-btn" id="reveal-btn" style="display:none">
    Show me the invisible labor →
  </button>

  <div class="labor-reveal" id="labor-reveal">
    <h3>Estimated cognitive overhead per week</h3>
    <div class="labor-number" id="labor-hours">0</div>
    <div class="labor-unit">hours per week spent thinking about items at weight 3 or above</div>
    <p style="margin-top:1rem; color: var(--text-muted); font-size:0.9rem; line-height:1.6;">
      Each item at weight 3+ demands an estimated 20 minutes of background cognitive churn per day — the planning, the dread, the circling. This is work. It is just invisible.
    </p>
  </div>

  <script src="burden-map.js"></script>
</body>
</html>
```

---

**7. JS logic**

```javascript
// burden-map.js

const items = [];
let laborRevealed = false;

const grid = document.getElementById('burden-grid');
const input = document.getElementById('item-input');
const categorySelect = document.getElementById('category-select');
const addBtn = document.getElementById('add-btn');
const ratioDisplay = document.getElementById('ratio-display');
const thresholdDisplay = document.getElementById('threshold-display');
const revealBtn = document.getElementById('reveal-btn');
const laborReveal = document.getElementById('labor-reveal');
const laborHours = document.getElementById('labor-hours');

addBtn.addEventListener('click', addItem);
input.addEventListener('keydown', e => { if (e.key === 'Enter') addItem(); });

function addItem() {
  const text = input.value.trim();
  if (!text) return;
  const item = {
    id: Date.now(),
    text,
    category: categorySelect.value,
    weight: 3,
    ownership: 'mine' // 'mine' | 'others'
  };
  items.push(item);
  input.value = '';
  renderAll();
}

function renderAll() {
  grid.innerHTML = '';
  items.forEach(item => grid.appendChild(renderCard(item)));
  updateStats();
  revealBtn.style.display = items.length > 0 ? 'block' : 'none';
  if (laborRevealed) updateLaborReveal();
}

function renderCard(item) {
  const card = document.createElement('div');
  card.className = 'burden-card';
  card.dataset.weight = item.weight;
  card.innerHTML = `
    <div class="card-top">
      <div>
        <div class="item-text">${escapeHtml(item.text)}</div>
        <div class="item-category">${categoryLabel(item.category)}</div>
      </div>
      <button class="delete-btn" data-id="${item.id}" aria-label="Remove">✕</button>
    </div>
    <div class="weight-row">
      <span class="weight-label">Weight</span>
      <input type="range" min="1" max="5" value="${item.weight}" data-id="${item.id}" class="weight-slider">
      <span class="weight-value" id="wv-${item.id}">${item.weight}</span>
    </div>
    <div class="ownership-toggle">
      <button class="ownership-btn ${item.ownership === 'mine' ? 'active' : ''}" 
        data-id="${item.id}" data-own="mine">Mine to carry</button>
      <button class="ownership-btn ${item.ownership === 'others' ? 'active' : ''}" 
        data-id="${item.id}" data-own="others">Carrying for someone else</button>
    </div>
  `;

  // Weight slider
  card.querySelector('.weight-slider').addEventListener('input', e => {
    const id = parseInt(e.target.dataset.id);
    const val = parseInt(e.target.value);
    const itemRef = items.find(i => i.id === id);
    if (itemRef) { itemRef.weight = val; }
    document.getElementById('wv-' + id).textContent = val;
    e.target.closest('.burden-card').dataset.weight = val;
    updateStats();
    if (laborRevealed) updateLaborReveal();
  });

  // Ownership toggle
  card.querySelectorAll('.ownership-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      const id = parseInt(e.target.dataset.id);
      const own = e.target.dataset.own;
      const itemRef = items.find(i => i.id === id);
      if (itemRef) itemRef.ownership = own;
      renderAll();
    });
  });

  // Delete
  card.querySelector('.delete-btn').addEventListener('click', e => {
    const id = parseInt(e.target.dataset.id);
    const idx = items.findIndex(i => i.id === id);
    if (idx > -1) items.splice(idx, 1);
    renderAll();
  });

  return card;
}

function updateStats() {
  if (items.length === 0) {
    ratioDisplay.textContent = 'Add items to see your ratio';
    thresholdDisplay.style.display = 'none';
    return;
  }
  const mine = items.filter(i => i.ownership === 'mine').length;
  const others = items.filter(i => i.ownership === 'others').length;
  const total = items.length;
  const minePercent = Math.round((mine / total) * 100);
  const othersPercent = 100 - minePercent;

  ratioDisplay.innerHTML = `<strong style="color:var(--text-primary)">${minePercent}% yours</strong> · 
    <strong style="color:var(--accent)">${othersPercent}% belongs to someone else</strong>`;

  const totalWeight = items.reduce((sum, i) => sum + i.weight, 0);
  thresholdDisplay.style.display = 'inline-block';
  if (totalWeight <= 8) {
    thresholdDisplay.className = 'threshold-indicator threshold-manageable';
    thresholdDisplay.textContent = 'Manageable';
  } else if (totalWeight <= 16) {
    thresholdDisplay.className = 'threshold-indicator threshold-loaded';
    thresholdDisplay.textContent = 'Loaded';
  } else {
    thresholdDisplay.className = 'threshold-indicator threshold-crisis';
    thresholdDisplay.textContent = 'Unsustainable';
  }
}

revealBtn.addEventListener('click', () => {
  laborRevealed = true;
  updateLaborReveal();
  laborReveal.classList.add('visible');
  revealBtn.style.display = 'none';
});

function updateLaborReveal() {
  const heavyItems = items.filter(i => i.weight >= 3);
  // 20 min/day × 7 days = 140 min per heavy item per week = 2.33 hours
  const hoursPerWeek = Math.round((heavyItems.length * 140) / 60 * 10) / 10;
  laborHours.textContent = hoursPerWeek;
}

function categoryLabel(cat) {
  const map = {
    work: 'Work commitment', client: 'Client relationship',
    admin: 'Unfinished admin', promised: 'Said I\'d do',
    waiting: 'Waiting on'
  };
  return map[cat] || cat;
}

function escapeHtml(str) {
  return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
```

---

**8. Cover Agent brief**

```
COVER BRIEF — Template #9: The Burden Map

Weather state: Threshold
Energy archetype: The Witness
Gradient: linear-gradient(135deg, #0f0e17 0%, #1a1033 50%, #2d1b4e 100%)
Typography register: Light weight body (300–400), heavy display (800), generous line-height
Hero image character: Aerial or deep-space — something that makes scale visible. 
  A single figure seen from above. Empty space with a few objects. 
  Nothing urgent. Something that makes the reader feel observed from a distance.
Accent color: #c77dff
Surface treatment: Dark with violet undertone — the depth of midnight deliberation
One new element: A faint concentric ring illustration behind the canvas (CSS only) 
  that pulses gently as total weight increases
Headline: "The Burden Map"
Subhead: "Everything you are holding, made visible."
```

---

**9. Newsletter-impossible element**

The interactive canvas where items added by the reader self-arrange by weight, and the ownership ratio updates live with each toggle. A newsletter can list examples of burdens. It cannot show the reader their specific ratio, their specific total weight score, or calculate their personal invisible labor overhead in hours. The number the reader sees is their number — not an illustration.

---

**10. Style guide entry**

```
TEMPLATE #9 — THE BURDEN MAP
ID: M2-T009
Interaction type: Reactive document + live calculation
Learning mechanism: Personal data mirror + ratio reveal
Newsletter-impossible rating: 5/5
Build complexity: Low
Emotional weather: Threshold
Energy archetype: The Witness
Gradient: #0f0e17 → #1a1033 → #2d1b4e (135deg)
Accent: #c77dff
Primary dimension: Practitioner Wisdom
Secondary dimension: Somatic Intelligence
Aha moment: The reader discovers their ownership ratio and 
  invisible labor hours as a specific number for the first time.
Design signature: Deep violet-black. Soft glow on heavy items. 
  Dashed-border reveal button. No alarm — only clarity.
Mobile-first: Yes. Single column. Full-width cards. Touch-friendly sliders.
Reuse potential: High — any issue about load, capacity, and invisible work.
```

---
---

# TEMPLATE #10 — COMMIT BEFORE YOU SEE IT

---

**1. Template name:** Commit Before You See It

**2. Emotional weather and energy archetype**
- Emotional weather: Threshold (the moment before something becomes known)
- Energy archetype: The Challenger — sharp, confrontational in the best sense; it forces the reader to stake a position before seeing the answer, which is where learning lives

---

**3. Gradient palette spec**

```css
:root {
  --bg: #0d1117;
  --surface: #161b22;
  --surface-raised: #21262d;
  --accent: #f7c948;
  --accent-warm: #ffd97d;
  --accent-cool: #58a6ff;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --text-muted: #484f58;
  --gradient: linear-gradient(160deg, #0d1117 0%, #0f1923 55%, #161028 100%);
  --gradient-accent: linear-gradient(90deg, #f7c948 0%, #ffd97d 100%);
  --border: rgba(247, 201, 72, 0.15);
  --glow: 0 0 20px rgba(247, 201, 72, 0.10);
  --correct: #3fb950;
  --wrong: #f85149;
}
```

Visual effect: Near-black with a cool blue undertone. The amber accent creates the feeling of something under a spotlight. This is a laboratory or a courtroom — a place where you commit to a statement and then find out if it holds.

---

**4. The interaction — what the reader does**

The reader sees a chart — but only the axes and a blank grid. The title says: *"Before you see the data, draw what you expect."*

A freehand drawing tool (canvas element, finger or mouse) lets them sketch a prediction line or indicate a region on the blank chart. A confirm button locks their drawing. Then the actual data curve appears, overlaid in amber on the reader's drawn prediction in blue. A gap calculation appears: *"Your prediction was X% higher/lower than reality at the peak."*

Below the chart, a brief explanation of what the data shows and why practitioners consistently predict in the direction the reader just did. The reader's specific deviation becomes the entry point — not a general claim about human bias.

A second round: the reader is shown a new blank chart with a different variable. They can try again, this time knowing their calibration bias from round 1.

---

**5. The aha moment**

The reader sees the exact direction and magnitude of their own wrong assumption as a percentage. Not "practitioners tend to underestimate X" — but "you predicted 34% higher than reality." The gap between their line and the actual data is their learning.

---

**6. HTML structure**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Commit Before You See It</title>
  <style>
    :root { /* palette from above */ }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text-primary);
      font-family: 'Inter', system-ui, sans-serif;
      min-height: 100vh;
      padding: 2rem 1.5rem;
    }

    .issue-header {
      max-width: 680px;
      margin: 0 auto 2.5rem;
    }
    .weather-tag {
      font-size: 0.75rem; letter-spacing: 0.12em;
      text-transform: uppercase; color: var(--accent); margin-bottom: 0.75rem;
    }
    h1 {
      font-size: clamp(2.4rem, 6vw, 4.8rem);
      font-weight: 800; line-height: 1.05;
      letter-spacing: -0.03em; margin-bottom: 1rem;
    }
    .lede {
      font-size: 1.1rem; line-height: 1.65;
      color: var(--text-secondary); max-width: 560px;
    }

    /* Round indicator */
    .round-indicator {
      max-width: 680px; margin: 0 auto 1.5rem;
      display: flex; gap: 0.5rem; align-items: center;
    }
    .round-dot {
      width: 8px; height: 8px; border-radius: 50%;
      background: var(--surface-raised); border: 1px solid var(--border);
      transition: background 0.3s;
    }
    .round-dot.active { background: var(--accent); }
    .round-dot.done { background: var(--correct); }

    /* Chart area */
    .chart-container {
      max-width: 680px; margin: 0 auto 1.5rem;
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; overflow: hidden;
      position: relative;
    }
    .chart-prompt {
      padding: 1.25rem 1.5rem;
      font-size: 0.9rem; color: var(--text-secondary);
      border-bottom: 1px solid var(--border);
    }
    .chart-prompt strong { color: var(--text-primary); }
    canvas#prediction-canvas {
      display: block; width: 100%;
      cursor: crosshair; touch-action: none;
    }
    .chart-axes {
      position: absolute; pointer-events: none;
      top: 0; left: 0; width: 100%; height: 100%;
    }

    /* Controls */
    .controls {
      max-width: 680px; margin: 0 auto 2rem;
      display: flex; gap: 0.75rem; flex-wrap: wrap;
    }
    .btn-primary {
      background: var(--gradient-accent); border: none;
      border-radius: 8px; color: #0d1117;
      font-weight: 700; font-size: 0.95rem;
      padding: 0.7rem 1.5rem; cursor: pointer;
    }
    .btn-secondary {
      background: transparent; border: 1px solid var(--border);
      border-radius: 8px; color: var(--text-secondary);
      font-size: 0.95rem; padding: 0.7rem 1.25rem; cursor: pointer;
    }
    .btn-secondary:hover { border-color: var(--accent); color: var(--accent); }

    /* Result panel */
    .result-panel {
      max-width: 680px; margin: 0 auto 2rem;
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 1.5rem;
      display: none;
    }
    .result-panel.visible { display: block; }
    .gap-stat {
      font-size: clamp(2.5rem, 7vw, 5rem);
      font-weight: 800; line-height: 1;
      letter-spacing: -0.04em; margin-bottom: 0.5rem;
    }
    .gap-stat.over { color: var(--wrong); }
    .gap-stat.under { color: var(--accent-cool); }
    .gap-label {
      font-size: 0.9rem; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: 0.08em;
      margin-bottom: 1.25rem;
    }
    .insight-text {
      font-size: 1rem; line-height: 1.7;
      color: var(--text-secondary);
    }

    /* Legend */
    .chart-legend {
      display: flex; gap: 1.5rem; margin-top: 0.75rem;
      font-size: 0.8rem; color: var(--text-muted);
    }
    .legend-item { display: flex; align-items: center; gap: 0.4rem; }
    .legend-swatch {
      width: 20px; height: 3px; border-radius: 2px; display: inline-block;
    }
  </style>
</head>
<body>
  <div class="issue-header">
    <div class="weather-tag">Threshold · The Challenger</div>
    <h1>Commit Before You See It</h1>
    <p class="lede">Draw your prediction on a blank chart before the data appears. Your miscalibration is the lesson — not a statistic about other practitioners. You.</p>
  </div>

  <div class="round-indicator" id="round-indicator">
    <span style="font-size:0.8rem; color:var(--text-muted); margin-right:0.5rem;">Round</span>
    <div class="round-dot active" id="dot-1"></div>
    <div class="round-dot" id="dot-2"></div>
  </div>

  <div class="chart-container" id="chart-container">
    <div class="chart-prompt" id="chart-prompt">
      <strong>Round 1:</strong> How do you think session engagement changes over a typical 90-minute workshop?
      Draw your prediction line from left to right, then tap "Lock my prediction."
    </div>
    <canvas id="prediction-canvas" width="680" height="300"></canvas>
  </div>

  <div class="chart-legend">
    <div class="legend-item">
      <span class="legend-swatch" style="background:#58a6ff;"></span>
      Your prediction
    </div>
    <div class="legend-item">
      <span class="legend-swatch" style="background:#f7c948;"></span>
      Actual data (revealed after commit)
    </div>
  </div>

  <div class="controls" style="margin-top:1rem;">
    <button class="btn-primary" id="lock-btn">Lock my prediction</button>
    <button class="btn-secondary" id="clear-btn">Clear and redraw</button>
  </div>

  <div class="result-panel" id="result-panel">
    <div class="gap-stat" id="gap-number"></div>
    <div class="gap-label" id="gap-label-text"></div>
    <p class="insight-text" id="insight-text"></p>
    <button class="btn-primary" id="next-round-btn" style="margin-top:1.5rem;">Try round 2 →</button>
  </div>

  <script src="commit-before.js"></script>
</body>
</html>
```

---

**7. JS logic**

```javascript
// commit-before.js

const canvas = document.getElementById('prediction-canvas');
const ctx = canvas.getContext('2d');
const lockBtn = document.getElementById('lock-btn');
const clearBtn = document.getElementById('clear-btn');
const resultPanel = document.getElementById('result-panel');
const gapNumber = document.getElementById('gap-number');
const gapLabelText = document.getElementById('gap-label-text');
const insightText = document.getElementById('insight-text');
const nextRoundBtn = document.getElementById('next-round-btn');

// Two rounds of data
const rounds = [
  {
    prompt: '<strong>Round 1:</strong> How do you think session engagement changes over a typical 90-minute workshop? Draw your prediction line, then lock it.',
    // Actual data: array of {x: 0-1, y: 0-1} normalized points
    // Typical workshop: starts high, drops at 40min, recovers slightly, drops again at end
    actual: [
      {x:0, y:0.82}, {x:0.1, y:0.78}, {x:0.2, y:0.70}, {x:0.3, y:0.62},
      {x:0.4, y:0.50}, {x:0.5, y:0.54}, {x:0.6, y:0.58}, {x:0.7, y:0.55},
      {x:0.8, y:0.45}, {x:0.9, y:0.40}, {x:1.0, y:0.35}
    ],
    insight: 'Most practitioners predict a more gradual decline with a stronger recovery at the close. In observed data, engagement drops faster in the first third and the end-of-session recovery is typically shallower than expected. The implication: the first 30 minutes and the transition out of content (not into it) are where design decisions matter most.',
    axisLabels: { x: 'Time (0 → 90 min)', y: 'Engagement' }
  },
  {
    prompt: '<strong>Round 2:</strong> How much does average compensation change when a practitioner moves from employee to independent consultant? Draw the percentage change you expect.',
    actual: [
      {x:0, y:0.50}, {x:0.2, y:0.52}, {x:0.4, y:0.48}, {x:0.6, y:0.53},
      {x:0.8, y:0.51}, {x:1.0, y:0.50}
    ],
    insight: 'The majority of practitioners predict a significant income increase (30–60%) when going independent. Longitudinal data shows that in the first two years, total compensation — including benefits, paid time off, retirement contributions, and stability — is flat or negative for most practitioners. The increase in gross rate obscures the increase in uncovered costs.',
    axisLabels: { x: 'Years 1-3 independent', y: 'Total compensation (vs. employed)' }
  }
];

let currentRound = 0;
let drawing = false;
let userPoints = []; // [{x, y}] in canvas coordinates
let locked = false;

function setupCanvas() {
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  canvas.width = rect.width * dpr;
  canvas.height = 300 * dpr;
  ctx.scale(dpr, dpr);
  canvas.style.height = '300px';
  redraw();
}

function redraw() {
  const W = canvas.getBoundingClientRect().width;
  const H = 300;
  ctx.clearRect(0, 0, W, H);

  // Grid
  ctx.strokeStyle = 'rgba(255,255,255,0.05)';
  ctx.lineWidth = 1;
  for (let i = 0; i <= 10; i++) {
    const x = (i / 10) * (W - 80) + 40;
    ctx.beginPath(); ctx.moveTo(x, 20); ctx.lineTo(x, H - 40); ctx.stroke();
  }
  for (let j = 0; j <= 4; j++) {
    const y = 20 + (j / 4) * (H - 60);
    ctx.beginPath(); ctx.moveTo(40, y); ctx.lineTo(W - 40, y); ctx.stroke();
  }

  // Axes labels
  ctx.fillStyle = 'rgba(139,148,158,0.7)';
  ctx.font = '11px Inter, system-ui';
  ctx.fillText(rounds[currentRound].axisLabels.x, W / 2 - 40, H - 8);

  // User's drawn line (blue)
  if (userPoints.length > 1) {
    ctx.strokeStyle = '#58a6ff';
    ctx.lineWidth = 2.5;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.beginPath();
    userPoints.forEach((p, i) => {
      i === 0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y);
    });
    ctx.stroke();
  }

  // Actual data line (amber, only after locked)
  if (locked) {
    const data = rounds[currentRound].actual;
    const plotW = W - 80; const plotH = H - 60;
    ctx.strokeStyle = '#f7c948';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    data.forEach((p, i) => {
      const px = 40 + p.x * plotW;
      const py = 20 + (1 - p.y) * plotH;
      i === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py);
    });
    ctx.stroke();
  }
}

// Drawing handlers
function getPos(e) {
  const rect = canvas.getBoundingClientRect();
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  return { x: clientX - rect.left, y: clientY - rect.top };
}

canvas.addEventListener('mousedown', e => { if (locked) return; drawing = true; userPoints = []; userPoints.push(getPos(e)); });
canvas.addEventListener('mousemove', e => { if (!drawing || locked) return; userPoints.push(getPos(e)); redraw(); });
canvas.addEventListener('mouseup', () => { drawing = false; });
canvas.addEventListener('touchstart', e => { if (locked) return; e.preventDefault(); drawing = true; userPoints = []; userPoints.push(getPos(e)); }, {passive:false});
canvas.addEventListener('touchmove', e => { if (!drawing || locked) return; e.preventDefault(); userPoints.push(getPos(e)); redraw(); }, {passive:false});
canvas.addEventListener('touchend', () => { drawing = false; });

clearBtn.addEventListener('click', () => {
  if (locked) return;
  userPoints = [];
  redraw();
});

lockBtn.addEventListener('click', () => {
  if (userPoints.length < 5) { alert('Draw a prediction line first.'); return; }
  locked = true;
  lockBtn.disabled = true;
  lockBtn.textContent = 'Prediction locked';
  redraw();
  showResult();
});

function showResult() {
  // Compare: sample actual at same x-positions as user points
  // Calculate average deviation
  const W = canvas.getBoundingClientRect().width;
  const plotW = W - 80; const plotH = 300 - 60;
  const data = rounds[currentRound].actual;

  // Get user's average y (normalized 0-1)
  const userAvgY = 1 - (userPoints.reduce((s, p) => s + p.y, 0) / userPoints.length - 20) / plotH;
  const actualAvgY = data.reduce((s, p) => s + p.y, 0) / data.length;
  const diff = Math.round((userAvgY - actualAvgY) * 100);
  const absDiff = Math.abs(diff);
  const direction = diff > 0 ? 'over' : 'under';

  gapNumber.textContent = (diff > 0 ? '+' : '') + diff + '%';
  gapNumber.className = 'gap-stat ' + direction;
  gapLabelText.textContent = direction === 'over'
    ? `You predicted ${absDiff}% above the actual average`
    : `You predicted ${absDiff}% below the actual average`;
  insightText.textContent = rounds[currentRound].insight;
  resultPanel.classList.add('visible');

  if (currentRound === 1) {
    nextRoundBtn.textContent = 'See your calibration summary →';
    nextRoundBtn.addEventListener('click', showSummary);
  }
}

nextRoundBtn.addEventListener('click', () => {
  if (currentRound >= 1) return;
  currentRound = 1;
  locked = false; userPoints = [];
  document.getElementById('dot-1').className = 'round-dot done';
  document.getElementById('dot-2').className = 'round-dot active';
  document.getElementById('chart-prompt').innerHTML = rounds[1].prompt;
  lockBtn.disabled = false; lockBtn.textContent = 'Lock my prediction';
  resultPanel.classList.remove('visible');
  redraw();
});

function showSummary() {
  insightText.innerHTML += '<br><br><strong style="color:var(--accent)">Two rounds complete.</strong> You now know the direction of your calibration bias. Most practitioners overcorrect in round 2 — but the direction is yours to work with.';
  nextRoundBtn.style.display = 'none';
}

window.addEventListener('resize', setupCanvas);
setupCanvas();
```

---

**8. Cover Agent brief**

```
COVER BRIEF — Template #10: Commit Before You See It

Weather state: Threshold
Energy archetype: The Challenger
Gradient: linear-gradient(160deg, #0d1117 0%, #0f1923 55%, #161028 100%)
Typography register: Heavy display (800), tight tracking on headline, 
  generous body line-height for instructions
Hero image character: A crosshair. A blank target. An empty graph with axes only.
  Something that invites projection — negative space where the reader's 
  expectation should sit. Dark blue-black tones.
Accent: #f7c948 (amber spotlight)
One new element: The prediction line in the hero image should be partially drawn —
  just enough to imply the reader's hand, not enough to commit to a direction.
  This is the only template where the hero image is incomplete by design.
Headline: "Commit Before You See It"
Subhead: "Draw your prediction. Then find out where you were wrong."
```

---

**9. Newsletter-impossible element**

The act of drawing a freehand prediction on a blank chart, having it locked and frozen, then watching the actual data appear overlaid — and receiving a personal deviation percentage. No newsletter can require a commitment before showing information. The commitment is the mechanism. The gap between the reader's drawn line and the actual curve is not illustrative — it is their exact miscalibration, in pixels and percentage.

---

**10. Style guide entry**

```
TEMPLATE #10 — COMMIT BEFORE YOU SEE IT
ID: M2-T010
Interaction type: Prediction tap + freehand draw + reveal
Learning mechanism: Prediction confrontation — miscalibration as data
Newsletter-impossible rating: 5/5
Build complexity: Medium (canvas drawing API)
Emotional weather: Threshold
Energy archetype: The Challenger
Gradient: #0d1117 → #0f1923 → #161028 (160deg)
Accent: #f7c948
Primary dimension: Practitioner Wisdom
Secondary dimension: Living Income
Aha moment: The reader's deviation from actual data — as a named percentage, 
  their direction, their number.
Design signature: Near-black with cool blue undertone. Amber data line 
  as spotlight. Blue prediction line as the reader's voice. 
  Incomplete hero image — by design.
Mobile-first: Yes. Canvas resizes responsively. Touch drawing supported.
Reuse potential: Very high — any issue grounded in data that contradicts 
  practitioner intuition.
```

---
---

# TEMPLATE #11 — THE RATE NEGOTIATION SIMULATOR

---

**1. Template name:** The Rate Negotiation Simulator

**2. Emotional weather and energy archetype**
- Emotional weather: Pressure (controlled friction for growth; not threat, not comfort)
- Energy archetype: The Practitioner — competent, grounded, does not flinch; this template does not theorize about negotiation, it simulates it

---

**3. Gradient palette spec**

```css
:root {
  --bg: #0a0f1e;
  --surface: #111827;
  --surface-raised: #1f2937;
  --accent: #34d399;
  --accent-warm: #6ee7b7;
  --accent-alert: #fbbf24;
  --text-primary: #f9fafb;
  --text-secondary: #9ca3af;
  --text-muted: #4b5563;
  --gradient: linear-gradient(145deg, #0a0f1e 0%, #0f172a 40%, #0c1a14 100%);
  --gradient-accent: linear-gradient(90deg, #34d399 0%, #6ee7b7 100%);
  --border: rgba(52, 211, 153, 0.15);
  --glow: 0 0 20px rgba(52, 211, 153, 0.10);
  --client-bg: #1a1f2e;
  --practitioner-bg: #0e1a14;
}
```

Visual effect: Deep navy into dark teal — the feeling of a negotiation room at close of day. Professional pressure. The green accent reads as money, forward motion, go. Not alarm. Confidence under constraint.

---

**4. The interaction — what the reader does**

The reader is placed in a simulated negotiation conversation. A client message appears: *"We love your proposal but our budget is $X. Can you work with that?"* — where $X is a figure below their stated rate, populated from a value they entered at the start (their current rate) or defaulted to a realistic example.

The reader sees four response options — not as abstract principles but as actual phrases they could say. Each is labeled with a negotiation strategy (Hold / Anchor Higher / Offer Structure / Exit Gracefully). They choose one. The client responds based on their choice — the response is realistic, sometimes pushing back, sometimes yielding partially. Two to three exchanges deep, the simulation ends and shows: the rate they would have landed, the gap from their floor, and a short annotation on what strategy produced what outcome and why.

A reset button lets them try a different path. The key design decision: the phrases given are not obviously "right" — all four are legitimate approaches with different outcomes, so the reader experiences the tradeoff rather than selecting the correct answer.

---

**5. The aha moment**

The reader discovers that the outcome of a rate negotiation is not about confidence or personality — it is about which specific exchange pattern they use in the first two responses. The simulation makes the mechanism visible: "Offering a payment structure in message 2 when the client said budget was the issue" is not the same as "holding the rate with a yes-and." Both work. Neither is wrong. But they produce different outcomes for different clients, and the reader can feel the difference in 90 seconds.

---

**6. HTML structure**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Rate Negotiation Simulator</title>
  <style>
    :root { /* palette from above */ }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text-primary);
      font-family: 'Inter', system-ui, sans-serif;
      min-height: 100vh; padding: 2rem 1.5rem;
    }

    .issue-header { max-width: 680px; margin: 0 auto 2.5rem; }
    .weather-tag {
      font-size: 0.75rem; letter-spacing: 0.12em;
      text-transform: uppercase; color: var(--accent); margin-bottom: 0.75rem;
    }
    h1 {
      font-size: clamp(2.4rem, 6vw, 4.8rem); font-weight: 800;
      line-height: 1.05; letter-spacing: -0.03em; margin-bottom: 1rem;
    }
    .lede { font-size: 1.1rem; line-height: 1.65; color: var(--text-secondary); }

    /* Rate input */
    .rate-setup {
      max-width: 680px; margin: 0 auto 2rem;
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 1.5rem;
    }
    .rate-setup label {
      display: block; font-size: 0.85rem; color: var(--text-muted);
      letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.5rem;
    }
    .rate-row { display: flex; gap: 0.75rem; align-items: center; }
    .rate-row span { color: var(--accent); font-size: 1.1rem; font-weight: 600; }
    .rate-row input[type="number"] {
      background: var(--surface-raised); border: 1px solid var(--border);
      color: var(--text-primary); border-radius: 8px;
      padding: 0.5rem 0.75rem; font-size: 1rem; width: 120px;
    }
    .btn-start {
      background: var(--gradient-accent); border: none;
      border-radius: 8px; color: #0a0f1e; font-weight: 700;
      padding: 0.65rem 1.5rem; cursor: pointer; font-size: 0.95rem;
    }

    /* Conversation */
    .conversation {
      max-width: 680px; margin: 0 auto;
      display: flex; flex-direction: column; gap: 1rem;
    }
    .message {
      padding: 1rem 1.25rem; border-radius: 10px;
      line-height: 1.6; font-size: 0.95rem; max-width: 90%;
      animation: fadeUp 0.3s ease;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(8px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .message.client {
      background: var(--client-bg); border: 1px solid rgba(255,255,255,0.07);
      align-self: flex-start;
    }
    .message.practitioner {
      background: var(--practitioner-bg);
      border: 1px solid rgba(52, 211, 153, 0.2);
      align-self: flex-end;
    }
    .message .role-label {
      font-size: 0.72rem; letter-spacing: 0.1em;
      text-transform: uppercase; color: var(--text-muted);
      margin-bottom: 0.4rem;
    }

    /* Response options */
    .response-options {
      max-width: 680px; margin: 0.5rem auto 0;
      display: flex; flex-direction: column; gap: 0.6rem;
    }
    .response-btn {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 10px; padding: 1rem 1.25rem;
      cursor: pointer; text-align: left; transition: all 0.15s;
      display: flex; flex-direction: column; gap: 0.3rem;
    }
    .response-btn:hover {
      border-color: var(--accent); background: rgba(52, 211, 153, 0.05);
    }
    .response-btn .strategy-tag {
      font-size: 0.72rem; letter-spacing: 0.1em;
      text-transform: uppercase; color: var(--accent); font-weight: 600;
    }
    .response-btn .phrase {
      font-size: 0.95rem; color: var(--text-primary); line-height: 1.5;
      font-style: italic;
    }

    /* Result panel */
    .result-panel {
      max-width: 680px; margin: 2rem auto 0;
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 1.5rem; display: none;
    }
    .result-panel.visible { display: block; }
    .result-rate {
      font-size: clamp(2.5rem, 7vw, 4.5rem); font-weight: 800;
      letter-spacing: -0.04em; line-height: 1;
      color: var(--accent); margin-bottom: 0.5rem;
    }
    .result-label { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.25rem; }
    .outcome-annotation {
      font-size: 0.95rem; line-height: 1.7; color: var(--text-secondary);
      margin-bottom: 1.5rem;
    }
    .btn-reset {
      background: transparent; border: 1px solid var(--border);
      color: var(--text-secondary); border-radius: 8px;
      padding: 0.65rem 1.25rem; cursor: pointer; font-size: 0.9rem;
    }
    .btn-reset:hover { border-color: var(--accent); color: var(--accent); }
  </style>
</head>
<body>
  <div class="issue-header">
    <div class="weather-tag">Pressure · The Practitioner</div>
    <h1>The Rate Negotiation Simulator</h1>
    <p class="lede">You get two moves. The client has pushed back on your rate. What you say in the next 90 seconds determines the outcome. This is not theory.</p>
  </div>

  <div class="rate-setup" id="rate-setup">
    <label>Your day rate (or hourly — whatever you charge)</label>
    <div class="rate-row">
      <span>$</span>
      <input type="number" id="rate-input" value="1500" min="50" max="50000" />
      <button class="btn-start" id="start-btn">Start the simulation</button>
    </div>
  </div>

  <div class="conversation" id="conversation"></div>
  <div class="response-options" id="response-options"></div>

  <div class="result-panel" id="result-panel">
    <div class="result-rate" id="result-rate"></div>
    <div class="result-label" id="result-label"></div>
    <p class="outcome-annotation" id="outcome-annotation"></p>
    <button class="btn-reset" id="reset-btn">Try a different path →</button>
  </div>

  <script src="negotiation-sim.js"></script>
</body>
</html>
```

---

**7. JS logic**

```javascript
// negotiation-sim.js

let rateFloor, clientOffer, choiceLog = [], exchangeCount = 0;

const conversation = document.getElementById('conversation');
const responseOptions = document.getElementById('response-options');
const resultPanel = document.getElementById('result-panel');
const resultRate = document.getElementById('result-rate');
const resultLabel = document.getElementById('result-label');
const outcomeAnnotation = document.getElementById('outcome-annotation');
const rateSetup = document.getElementById('rate-setup');

document.getElementById('start-btn').addEventListener('click', startSim);
document.getElementById('reset-btn').addEventListener('click', resetSim);

function startSim() {
  const rate = parseInt(document.getElementById('rate-input').value) || 1500;
  rateFloor = rate;
  clientOffer = Math.round(rate * 0.72); // Client comes in at 72% of stated rate
  rateSetup.style.display = 'none';
  conversation.innerHTML = '';
  choiceLog = []; exchangeCount = 0;
  resultPanel.classList.remove('visible');

  addMessage('client',
    `We've reviewed your proposal and we love what you bring. Our budget for this engagement is $${clientOffer.toLocaleString()}. We know that's below your stated rate of $${rate.toLocaleString()} — is there any flexibility on your end?`
  );
  showRound1Options();
}

function addMessage(role, text) {
  const msg = document.createElement('div');
  msg.className = 'message ' + role;
  msg.innerHTML = `<div class="role-label">${role === 'client' ? 'Client' : 'You'}</div>${text}`;
  conversation.appendChild(msg);
  msg.scrollIntoView({behavior:'smooth', block:'nearest'});
}

function showRound1Options() {
  const rate = rateFloor;
  renderOptions([
    {
      strategy: 'Hold',
      phrase: `"I appreciate that — and I want to make this work. My rate is $${rate.toLocaleString()} because [value reason]. What I can offer is to scope the engagement so it fits within your budget at that rate."`,
      id: 'hold'
    },
    {
      strategy: 'Anchor Higher',
      phrase: `"Thank you for being direct. To be honest, for a project of this scope I typically charge $${Math.round(rate*1.15).toLocaleString()}. At $${rate.toLocaleString()} I'm already at the lower end. Can we talk about what's driving the budget cap?"`,
      id: 'anchor'
    },
    {
      strategy: 'Offer Structure',
      phrase: `"I can work within $${clientOffer.toLocaleString()} if we structure this in two phases — I'd want to confirm scope clarity before phase 2 starts. Would a phased approach work on your end?"`,
      id: 'structure'
    },
    {
      strategy: 'Exit Gracefully',
      phrase: `"I really appreciate the opportunity. At $${clientOffer.toLocaleString()} I wouldn't be able to give this the attention it deserves. If budget opens up, I'd love to revisit."`,
      id: 'exit'
    }
  ], handleRound1);
}

function renderOptions(options, handler) {
  responseOptions.innerHTML = '';
  options.forEach(opt => {
    const btn = document.createElement('button');
    btn.className = 'response-btn';
    btn.innerHTML = `<span class="strategy-tag">${opt.strategy}</span><span class="phrase">${opt.phrase}</span>`;
    btn.addEventListener('click', () => handler(opt));
    responseOptions.appendChild(btn);
  });
}

function handleRound1(choice) {
  choiceLog.push(choice.id);
  responseOptions.innerHTML = '';
  addMessage('practitioner', choice.phrase.replace(/^"|"$/g, ''));
  exchangeCount++;

  setTimeout(() => {
    if (choice.id === 'exit') {
      addMessage('client', "I understand. I'll keep you in mind if things change. Thank you for your time.");
      showResult('exit');
      return;
    }
    const clientResponses = {
      hold: "That makes sense. If we narrow the scope, we could potentially work within your rate. What would you remove from the original proposal?",
      anchor: "I didn't realize the full scope commanded that kind of investment. Let me go back to my team about the budget — can we reconnect Thursday?",
      structure: "A phased approach could work. What would phase 1 deliver and what's the cost?"
    };
    addMessage('client', clientResponses[choice.id]);
    showRound2Options(choice.id);
  }, 600);
}

function showRound2Options(round1Choice) {
  const rate = rateFloor;
  const optionSets = {
    hold: [
      { strategy: 'Hold and Scope', phrase: `"I'd take out the facilitation design component — that's about 20% of the scope. We'd deliver the core program at $${rate.toLocaleString()}."`, id: 'scope-cut', outcome: rate },
      { strategy: 'Soften', phrase: `"If we can agree on timeline flexibility, I can come down to $${Math.round(rate*0.9).toLocaleString()}."`, id: 'soften', outcome: Math.round(rate*0.9) }
    ],
    anchor: [
      { strategy: 'Wait', phrase: `"Thursday works. I want to make sure we're aligned on the value before we finalize the number."`, id: 'wait', outcome: Math.round(rate*1.05) },
      { strategy: 'Bridge', phrase: `"Thursday works. In the meantime — if you come back at $${Math.round(rate*0.95).toLocaleString()}, I can make that work without scope changes."`, id: 'bridge', outcome: Math.round(rate*0.95) }
    ],
    structure: [
      { strategy: 'Commit to Structure', phrase: `"Phase 1 would be discovery and design — $${Math.round(clientOffer*0.55).toLocaleString()}. Phase 2 delivery and follow-through — $${Math.round(clientOffer*0.5).toLocaleString()}. Total: $${clientOffer.toLocaleString()} with a clear gate between phases."`, id: 'commit-structure', outcome: clientOffer },
      { strategy: 'Trade for Rate', phrase: `"If we go phased, I'd need phase 1 at my full rate — $${rate.toLocaleString()} — with phase 2 conditional on outcomes. Keeps quality high for both of us."`, id: 'trade-rate', outcome: rate }
    ]
  };
  renderOptions(optionSets[round1Choice], (choice) => handleRound2(choice));
}

function handleRound2(choice) {
  choiceLog.push(choice.id);
  responseOptions.innerHTML = '';
  addMessage('practitioner', choice.phrase.replace(/^"|"$/g, ''));
  setTimeout(() => {
    addMessage('client', "That works for us. Let's move forward.");
    showResult(choice.id, choice.outcome);
  }, 600);
}

const annotations = {
  'exit': `Exiting gracefully preserved your positioning and left a professional impression. No revenue this time — but no rate erosion either. This is the correct move when a client's budget signals a fundamental mismatch with your scope of work.`,
  'scope-cut': `Protecting the rate by cutting scope is the most defensible move when you have a clear floor. The client gets the core of what they need. You maintained your rate integrity. The risk: scope cuts can signal flexibility that invites future negotiation.`,
  'soften': `A 10% concession with a stated reason (timeline flexibility) is more defensible than a straight discount. It keeps the door open without collapsing the floor. The risk: you've now established a new reference point for this client.`,
  'wait': `Letting the client return with a number after you've stated a higher anchor frequently produces an offer above your original floor — sometimes significantly. This requires comfort with silence and a willingness to lose the engagement.`,
  'bridge': `Giving the client a specific number to bring back (${ '' }) — slightly below your anchor, above your floor — compresses the negotiation to one exchange. Efficient. Slightly lower ceiling than waiting, but faster resolution.`,
  'commit-structure': `Accepting the original budget in a phased structure protects future revenue (phase 2) while managing risk. The client feels heard. You retain the right to re-scope at the phase gate. This works when you believe the engagement will grow.`,
  'trade-rate': `Holding your rate on phase 1 while making phase 2 conditional on outcomes is the highest-integrity move in a structure conversation. It signals confidence in your work. Clients who accept this are typically better long-term clients.`
};

function showResult(id, landedRate) {
  const landed = landedRate !== undefined ? landedRate : 0;
  resultRate.textContent = landed > 0 ? '$' + landed.toLocaleString() : 'No deal';
  resultLabel.textContent = landed > 0
    ? `landed vs. your floor of $${rateFloor.toLocaleString()} — ${Math.round((landed/rateFloor)*100)}% of your stated rate`
    : 'You exited with your positioning intact';
  outcomeAnnotation.textContent = annotations[id] || '';
  resultPanel.classList.add('visible');
  resultPanel.scrollIntoView({behavior:'smooth'});
}

function resetSim() {
  rateSetup.style.display = 'block';
  conversation.innerHTML = '';
  responseOptions.innerHTML = '';
  resultPanel.classList.remove('visible');
}
```

---

**8. Cover Agent brief**

```
COVER BRIEF — Template #11: The Rate Negotiation Simulator

Weather state: Pressure
Energy archetype: The Practitioner
Gradient: linear-gradient(145deg, #0a0f1e 0%, #0f172a 40%, #0c1a14 100%)
Typography register: Confident and spare. Nothing decorative. 
  Heavy display, normal body weight, generous white space between elements.
Hero image character: Two chairs facing each other across a table. 
  Or a single email thread on a screen. Something that establishes 
  a conversation — one party about to respond.
Accent: #34d399 (green — money, permission, forward motion)
Surface treatment: Deep navy-to-teal. Professional pressure, not threat.
One new element: Conversation bubbles in the hero — two visible, 
  content redacted with thin lines. The scene is set before a word is read.
Headline: "The Rate Negotiation Simulator"
Subhead: "Two moves. One outcome. Let's find out what happens when you say that."
```

---

**9. Newsletter-impossible element**

The branching dialogue where the client responds differently based on which phrase the reader chose — and the final landed rate is calculated from the reader's specific choices, not a generic example. A newsletter can describe negotiation strategies. It cannot put the reader in the conversation and show them, 90 seconds later, what rate they would have landed and why.

---

**10. Style guide entry**

```
TEMPLATE #11 — THE RATE NEGOTIATION SIMULATOR
ID: M2-T011
Interaction type: Branching choice dialogue + calculated outcome
Learning mechanism: Decision tree — reader experiences the consequence 
  of each exchange pattern, not a description of it
Newsletter-impossible rating: 5/5
Build complexity: Low-Medium (no canvas; branching logic in plain JS)
Emotional weather: Pressure
Energy archetype: The Practitioner
Gradient: #0a0f1e → #0f172a → #0c1a14 (145deg)
Accent: #34d399
Primary dimension: Living Income
Secondary dimension: Practitioner Wisdom
Aha moment: The reader discovers that outcome = exchange pattern, 
  not confidence or personality. Two moves produce a specific number.
Design signature: Deep navy-to-teal. Conversation bubble layout. 
  Green accent reads as money and forward motion. 
  No decorative elements — every pixel is functional.
Mobile-first: Yes. Conversation layout is naturally vertical. 
  Response buttons are full-width touch targets.
Reuse potential: Very high — any issue about pricing, client dynamics, 
  scope conversations, or boundaries.
```

---
---

# TEMPLATE #12 — THE ACCUMULATION CLOCK

---

**1. Template name:** The Accumulation Clock

**2. Emotional weather and energy archetype**
- Emotional weather: Clarity (the moment after something becomes undeniable)
- Energy archetype: The Accountant — precise, relentless, does not editorialize; lets the numbers do the work; the design is a ledger, not a lesson

---

**3. Gradient palette spec**

```css
:root {
  --bg: #07090f;
  --surface: #0f1219;
  --surface-raised: #161b26;
  --accent: #60a5fa;
  --accent-warm: #93c5fd;
  --accent-alert: #f87171;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted: #475569;
  --gradient: linear-gradient(160deg, #07090f 0%, #0a0f1c 50%, #0c1018 100%);
  --gradient-accent: linear-gradient(90deg, #60a5fa 0%, #93c5fd 100%);
  --border: rgba(96, 165, 250, 0.12);
  --glow: 0 0 24px rgba(96, 165, 250, 0.08);
  --tick-color: rgba(96, 165, 250, 0.6);
}
```

Visual effect: Near-black with a cool blue undertone — the color of data at midnight. Not ominous. Precise. A Bloomberg terminal or a Bloomberg terminal at the moment you realize something.

---

**4. The interaction — what the reader does**

The reader sees a blank interface with a single prompt: *"What is one hour of your time worth, in dollars?"* They enter a number. A second prompt: *"How many hours per week do you spend on work you are not being paid for?"*

When they submit, a clock starts. Not a countdown. A forward-running accumulation. Every second, a dollar amount ticks upward — the value of unpaid time accumulating in real time, in front of the reader, while they sit there reading.

The clock runs throughout the issue. At the end, a summary shows:
- Unpaid time accumulated during this reading session (usually 8-15 minutes)
- Unpaid time per week at their rate
- Unpaid time per year
- The cumulative total over 5 years
- A comparison: what that same figure would look like if invested or charged as a retainer

The reader can adjust their inputs and watch the clock recalculate instantly.

---

**5. The aha moment**

The reader watches money — their money — tick away while they are reading. Not a statistic. Not "practitioners lose an average of X." Their specific hourly rate, their specific unpaid hours, ticking upward right now. When the 5-year figure appears, the abstraction collapses. The number is specific enough to be uncomfortable.

---

**6. HTML structure**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Accumulation Clock</title>
  <style>
    :root { /* palette from above */ }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text-primary);
      font-family: 'Inter', system-ui, sans-serif;
      min-height: 100vh; padding: 2rem 1.5rem;
    }

    .issue-header { max-width: 680px; margin: 0 auto 2.5rem; }
    .weather-tag {
      font-size: 0.75rem; letter-spacing: 0.12em;
      text-transform: uppercase; color: var(--accent); margin-bottom: 0.75rem;
    }
    h1 {
      font-size: clamp(2.4rem, 6vw, 4.8rem); font-weight: 800;
      line-height: 1.05; letter-spacing: -0.03em; margin-bottom: 1rem;
    }
    .lede { font-size: 1.1rem; line-height: 1.65; color: var(--text-secondary); }

    /* Setup */
    .setup-panel {
      max-width: 680px; margin: 0 auto 2rem;
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 1.5rem;
    }
    .setup-row {
      display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1.25rem;
    }
    .setup-row label {
      font-size: 0.82rem; color: var(--text-muted);
      letter-spacing: 0.08em; text-transform: uppercase;
    }
    .setup-row .input-wrap {
      display: flex; align-items: center; gap: 0.5rem;
    }
    .setup-row .input-wrap span { color: var(--accent); font-weight: 600; }
    .setup-row input[type="number"] {
      background: var(--surface-raised); border: 1px solid var(--border);
      color: var(--text-primary); border-radius: 8px;
      padding: 0.5rem 0.75rem; font-size: 1rem; width: 140px;
    }
    .btn-start-clock {
      background: var(--gradient-accent); border: none;
      border-radius: 8px; color: #07090f; font-weight: 700;
      padding: 0.7rem 1.5rem; cursor: pointer; font-size: 0.95rem;
      width: 100%; margin-top: 0.5rem;
    }

    /* Live clock */
    .clock-panel {
      max-width: 680px; margin: 0 auto 2rem; display: none;
    }
    .clock-panel.active { display: block; }

    .live-row {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 1.5rem 2rem;
      display: flex; align-items: baseline; gap: 0.75rem;
      margin-bottom: 1rem; position: relative; overflow: hidden;
    }
    .live-row::before {
      content: '';
      position: absolute; top: 0; left: 0; right: 0; height: 1px;
      background: var(--gradient-accent); opacity: 0.4;
    }
    .live-amount {
      font-size: clamp(3rem, 9vw, 6rem); font-weight: 800;
      letter-spacing: -0.05em; color: var(--text-primary);
      font-variant-numeric: tabular-nums;
      line-height: 1; font-feature-settings: "tnum";
    }
    .live-label {
      font-size: 0.85rem; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: 0.08em;
      align-self: flex-end; padding-bottom: 0.4rem;
    }

    /* Stats grid */
    .stats-grid {
      display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;
      max-width: 680px; margin: 0 auto 2rem;
    }
    @media (max-width: 480px) { .stats-grid { grid-template-columns: 1fr; } }
    .stat-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 10px; padding: 1.25rem;
    }
    .stat-card .stat-label {
      font-size: 0.78rem; color: var(--text-muted);
      letter-spacing: 0.09em; text-transform: uppercase; margin-bottom: 0.5rem;
    }
    .stat-card .stat-value {
      font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 800;
      letter-spacing: -0.03em; color: var(--accent);
      font-variant-numeric: tabular-nums; font-feature-settings: "tnum";
    }
    .stat-card.highlight .stat-value { color: var(--accent-alert); }
    .stat-card .stat-sub {
      font-size: 0.8rem; color: var(--text-muted); margin-top: 0.3rem;
    }

    /* Adjust inputs */
    .adjust-row {
      max-width: 680px; margin: 0 auto 1.5rem;
      display: flex; gap: 1rem; flex-wrap: wrap; align-items: center;
      font-size: 0.85rem; color: var(--text-muted);
    }
    .adjust-row label { white-space: nowrap; }
    .adjust-row input[type="number"] {
      background: var(--surface-raised); border: 1px solid var(--border);
      color: var(--text-primary); border-radius: 6px;
      padding: 0.3rem 0.6rem; font-size: 0.9rem; width: 90px;
    }

    /* Comparison note */
    .comparison-note {
      max-width: 680px; margin: 0 auto;
      background: var(--surface); border: 1px solid rgba(96, 165, 250, 0.2);
      border-radius: 12px; padding: 1.5rem;
    }
    .comparison-note h3 {
      font-size: 0.82rem; letter-spacing: 0.1em;
      text-transform: uppercase; color: var(--accent); margin-bottom: 0.75rem;
    }
    .comparison-note p {
      font-size: 0.95rem; line-height: 1.7; color: var(--text-secondary);
    }
  </style>
</head>
<body>
  <div class="issue-header">
    <div class="weather-tag">Clarity · The Accountant</div>
    <h1>The Accumulation Clock</h1>
    <p class="lede">The money is already gone. You just haven't seen it as a number yet. Enter your rate and unpaid hours, then watch the clock.</p>
  </div>

  <div class="setup-panel" id="setup-panel">
    <div class="setup-row">
      <label>Your hourly rate (what one hour of your time is worth)</label>
      <div class="input-wrap"><span>$</span><input type="number" id="hourly-rate" value="150" min="10" max="5000" /></div>
    </div>
    <div class="setup-row">
      <label>Hours per week you work but don't bill</label>
      <div class="input-wrap"><input type="number" id="unpaid-hours" value="12" min="0" max="80" /><span>hrs/wk</span></div>
    </div>
    <button class="btn-start-clock" id="start-clock-btn">Start the clock</button>
  </div>

  <div class="clock-panel" id="clock-panel">
    <div class="live-row">
      <div class="live-amount" id="live-amount">$0</div>
      <div class="live-label">unpaid time accumulated this session</div>
    </div>

    <div class="adjust-row">
      <label>Rate: $<input type="number" id="rate-adjust" min="10" max="5000" /></label>
      <label>Unpaid hrs/wk: <input type="number" id="hours-adjust" min="0" max="80" /></label>
    </div>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-label">Per week</div>
        <div class="stat-value" id="stat-week">$0</div>
        <div class="stat-sub">at your current rate</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Per year</div>
        <div class="stat-value" id="stat-year">$0</div>
        <div class="stat-sub">50 working weeks</div>
      </div>
      <div class="stat-card highlight">
        <div class="stat-label">5-year total</div>
        <div class="stat-value" id="stat-5yr">$0</div>
        <div class="stat-sub">at constant rate, no adjustment</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">If charged as retainer</div>
        <div class="stat-value" id="stat-retainer">$0</div>
        <div class="stat-sub">annual retainer equivalent</div>
      </div>
    </div>

    <div class="comparison-note" id="comparison-note">
      <h3>What this looks like as a different decision</h3>
      <p id="comparison-text"></p>
    </div>
  </div>

  <script src="accumulation-clock.js"></script>
</body>
</html>
```

---

**7. JS logic**

```javascript
// accumulation-clock.js

let hourlyRate = 150;
let unpaidHoursPerWeek = 12;
let sessionStartTime = null;
let clockInterval = null;

const setupPanel = document.getElementById('setup-panel');
const clockPanel = document.getElementById('clock-panel');
const liveAmount = document.getElementById('live-amount');
const statWeek = document.getElementById('stat-week');
const statYear = document.getElementById('stat-year');
const stat5yr = document.getElementById('stat-5yr');
const statRetainer = document.getElementById('stat-retainer');
const comparisonText = document.getElementById('comparison-text');
const rateAdjust = document.getElementById('rate-adjust');
const hoursAdjust = document.getElementById('hours-adjust');

document.getElementById('start-clock-btn').addEventListener('click', () => {
  hourlyRate = parseFloat(document.getElementById('hourly-rate').value) || 150;
  unpaidHoursPerWeek = parseFloat(document.getElementById('unpaid-hours').value) || 12;
  rateAdjust.value = hourlyRate;
  hoursAdjust.value = unpaidHoursPerWeek;
  setupPanel.style.display = 'none';
  clockPanel.classList.add('active');
  sessionStartTime = Date.now();
  updateStats();
  clockInterval = setInterval(tick, 100);
});

rateAdjust.addEventListener('input', () => {
  hourlyRate = parseFloat(rateAdjust.value) || 150;
  updateStats();
});
hoursAdjust.addEventListener('input', () => {
  unpaidHoursPerWeek = parseFloat(hoursAdjust.value) || 0;
  updateStats();
});

function tick() {
  const elapsedSeconds = (Date.now() - sessionStartTime) / 1000;
  // unpaid hours/week → per second
  const unpaidPerSecond = (hourlyRate * unpaidHoursPerWeek) / (5 * 8 * 3600);
  const accumulated = elapsedSeconds * unpaidPerSecond;
  liveAmount.textContent = '$' + accumulated.toFixed(2);
}

function updateStats() {
  const weekTotal = hourlyRate * unpaidHoursPerWeek;
  const yearTotal = weekTotal * 50;
  const fiveYearTotal = yearTotal * 5;
  const retainerEquiv = weekTotal * 4.33; // monthly

  statWeek.textContent = '$' + Math.round(weekTotal).toLocaleString();
  statYear.textContent = '$' + Math.round(yearTotal).toLocaleString();
  stat5yr.textContent = '$' + Math.round(fiveYearTotal).toLocaleString();
  statRetainer.textContent = '$' + Math.round(retainerEquiv).toLocaleString() + '/mo';

  comparisonText.textContent = `At $${hourlyRate}/hr with ${unpaidHoursPerWeek} unpaid hours per week, 
    your annual uncaptured time is worth $${Math.round(yearTotal).toLocaleString()}. 
    As a standing retainer — one client, one engagement — that same work captured would cost 
    $${Math.round(retainerEquiv).toLocaleString()} per month. 
    Over 5 years: $${Math.round(fiveYearTotal).toLocaleString()}. 
    ${yearTotal >= 50000
      ? 'That is a salary. It is currently being donated.'
      : yearTotal >= 20000
      ? 'That is a significant annual figure going unrecognized.'
      : 'Even at this rate, the pattern compounds significantly over time.'}`;
}
```

---

**8. Cover Agent brief**

```
COVER BRIEF — Template #12: The Accumulation Clock

Weather state: Clarity
Energy archetype: The Accountant
Gradient: linear-gradient(160deg, #07090f 0%, #0a0f1c 50%, #0c1018 100%)
Typography register: Monospaced display for the live number (tabular nums). 
  System sans for everything else. Heavy weight on the ticking amount.
Hero image character: A digital counter — any analog that reads as 
  something accumulating: a meter, a stock ticker, a fuel gauge.
  The hero image should feel like a dashboard — functional, not decorative.
Accent: #60a5fa (cool blue — Bloomberg terminal, financial data, precision)
Surface treatment: Near-black with blue. Data at midnight.
One new element: The live counter in the hero image should appear to be running — 
  use a CSS animation to simulate ticking digits in the cover art itself.
  The reader sees a number changing before they even click in.
Headline: "The Accumulation Clock"
Subhead: "The money is already gone. You just haven't seen the number yet."
```

---

**9. Newsletter-impossible element**

The clock runs in real time throughout the reading session. The reader's specific dollar amount ticks upward while they sit there. Every second they spend on the issue is another fraction of a cent lost — calculated from their own rate, their own unpaid hours. A newsletter can show a table of annual losses. It cannot show the money leaving in real time, calibrated to the reader's specific situation, while they read.

---

**10. Style guide entry**

```
TEMPLATE #12 — THE ACCUMULATION CLOCK
ID: M2-T012
Interaction type: Live calculation + real-time counter
Learning mechanism: Personal data mirror + temporal immediacy
Newsletter-impossible rating: 5/5
Build complexity: Low
Emotional weather: Clarity
Energy archetype: The Accountant
Gradient: #07090f → #0a0f1c → #0c1018 (160deg)
Accent: #60a5fa
Primary dimension: Living Income
Secondary dimension: Practitioner Wisdom
Aha moment: The reader sees their unpaid time accumulating in dollars, 
  per second, in real time — while they are reading. The 5-year total 
  converts abstraction into a specific, uncomfortable number.
Design signature: Near-black with cool blue. Tabular numerals on the 
  live counter. Bloomberg-terminal precision aesthetic. 
  Nothing decorative — every element is a data point.
Mobile-first: Yes. Single column. Live counter full-width. 
  Stats grid collapses to single column on small screens.
Reuse potential: Extremely high — any Living Income issue about pricing, 
  invisible labor, rates, or the cost of undercharging.
```

---
---

# THE QUICK WIN SPRINT PLAN
## 30-Day Build Schedule: Templates #1-12

---

### SPRINT LOGIC

Sequencing is governed by three rules:

**Rule 1 — Low complexity first.** Build confidence and shipping rhythm before tackling canvas and multi-round interactions.

**Rule 2 — Cover all 3 emotional weather states in the first two weeks.** Clarity, Threshold, and Pressure should each be represented before the sprint is half done — this validates the gradient language in production.

**Rule 3 — Pair a Living Income template with a Practitioner Wisdom template in every week.** The library needs dimensional balance, not a run of pricing issues.

---

### TEMPLATE COMPLEXITY INDEX

| # | Template | Complexity | Weather | Build Days |
|---|----------|-----------|---------|-----------|
| 1 | The Price You're Actually Charging | Low | Clarity | 2 |
| 3 | What Your Week Is Actually Costing You | Low | Clarity | 1.5 |
| 9 | The Burden Map | Low | Threshold | 2 |
| 12 | The Accumulation Clock | Low | Clarity | 1.5 |
| 4 | The Cascade | Low | Clarity | 2 |
| 11 | The Rate Negotiation Simulator | Low-Med | Pressure | 2.5 |
| 8 | (from prior spec) | Low-Med | TBD | 2.5 |
| 7 | (from prior spec) | Med | TBD | 3 |
| 10 | Commit Before You See It | Medium | Threshold | 3 |
| 5 | Commit Before (full) | Medium | TBD | 3 |
| 2 | Draw the Curve Before You See It | Medium | Threshold | 3.5 |
| 6 | (from prior spec) | Medium | TBD | 3 |

---

### WEEK 1 (Days 1-7): FOUNDATION THREE

Build these three first. They are the lowest complexity, they validate the reactive-document pattern, and they cover two emotional weather states.

**Build 1 — Template #3: What Your Week Is Actually Costing You** *(Days 1-2)*
- Lowest complexity in the entire library — two inputs, three outputs, no canvas
- Validates the reactive-document pattern before anything else is built
- First test of the Clarity gradient palette in production
- Deliverable: live HTML/CSS/JS file, fully mobile-responsive, deployed

**Build 2 — Template #1: The Price You're Actually Charging** *(Days 3-4)*
- Four sliders, one live calculation — highest emotional impact for complexity invested
- The reader's floor rate as a personal discovery moment
- Proves the slider-reactive pattern works across screen sizes
- Deliverable: live file, tested on mobile, deployed

**Build 3 — Template #12: The Accumulation Clock** *(Days 5-7)*
- Low complexity, highest emotional immediacy
- Introduces the real-time counter pattern — a new primitive not in builds 1-2
- First Clarity archetype that runs throughout the issue rather than waiting for input
- Deliverable: live file, real-time tick validated at multiple screen sizes, deployed

**Week 1 minimum viable outcome:** Three live issues that prove reactive documents can be built in 2 days or less. The Living Income dimension is established with three distinct interaction patterns.

---

### WEEK 2 (Days 8-14): WEATHER EXPANSION

Introduce Threshold and Pressure. Validate that the gradient language works across all three weather states. Build the first branching interaction.

**Build 4 — Template #9: The Burden Map** *(Days 8-10)*
- First Threshold-weather issue — validates the violet-black palette in production
- Introduces a new primitive: weighted cards with live ratio calculation
- First issue that asks the reader to input qualitative (not just numerical) data
- Deliverable: live file, drag/touch interactions tested, deployed

**Build 5 — Template #11: The Rate Negotiation Simulator** *(Days 11-13)*
- First Pressure-weather issue — validates the navy-to-teal gradient
- Introduces the branching dialogue pattern — new primitive
- Highest immediate practitioner utility in the entire library
- Deliverable: live file, all dialogue paths tested, deployed

**Build 6 — Template #4: The Cascade** *(Days 13-14)*
- Low complexity branching without the dialogue overhead
- Reader makes 3-4 binary choices; content narrows accordingly
- Fast build because the pattern is simpler than the Negotiation Simulator
- Deliverable: live file, all 4 branch paths functional, deployed

**Week 2 minimum viable outcome:** All three emotional weather states represented in the live library. The palette language is proven in production. Six issues live and deployed.

---

### WEEK 3 (Days 15-21): CANVAS AND COMPLEXITY

Introduce the canvas-drawing pattern. The highest-complexity builds in the library. These take longer — build them before the final sprint so there's recovery time.

**Build 7 — Template #2: Draw the Curve Before You See It** *(Days 15-18)*
- First canvas-drawing interaction — the most technically demanding primitive
- Introduces freehand prediction + overlay reveal
- Build canvas drawing first as a standalone component, then wrap in the issue template
- Deliverable: canvas drawing works on mouse and touch; reveal animation smooth

**Build 8 — Template #10: Commit Before You See It** *(Days 18-21)*
- Second canvas template — builds on the drawing infrastructure from Build 7
- Adds the two-round structure and the personal deviation percentage calculation
- Reuses the canvas component from Build 7 — faster than building from scratch
- Deliverable: two-round flow complete, deviation calculation accurate

**Week 3 minimum viable outcome:** The canvas-drawing pattern is in production. Builds 7 and 8 together form a linked pair — the library now has a prediction-confrontation series.

---

### WEEK 4 (Days 22-30): LIBRARY COMPLETION

Complete templates #5, #6, #7, #8 (built from the prior spec in this workflow). Polish all 12 for the first quarterly template deck. Write the style guide archive.

**Days 22-26 — Builds 9-12:**
Complete the remaining four templates from the #5-8 spec in their order of complexity. Target: one per day for the two low-complexity ones, two days for each medium-complexity build.

**Days 27-29 — QA Sprint:**
- Mobile test every template on a real device (not just browser emulation)
- Test every template with real practitioner inputs — edge cases at the extremes (rate = $10, rate = $5000; unpaid hours = 0, unpaid hours = 40)
- Verify all gradient palettes render correctly across dark/light system themes
- Accessibility pass: keyboard navigation on all interactive elements, contrast ratios

**Day 30 — Style Guide Archive Entry:**
- Compile the 10-point style guide entry for each of the 12 templates
- Write the introductory note: what this library is, what it proves, how to license a deck
- First quarterly template deck is complete

**Week 4 minimum viable outcome:** 12 templates live, tested, and documented. The first quarterly deck is ready to package.

---

### SPRINT SUMMARY

| Week | Builds | Pattern unlocked | Dimensions covered |
|------|--------|------------------|--------------------|
| 1 | #3, #1, #12 | Reactive document, slider, real-time counter | Living Income |
| 2 | #9, #11, #4 | Weighted cards, branching dialogue, binary cascade | Living Income + Practitioner Wisdom |
| 3 | #2, #10 | Canvas freehand draw, prediction confrontation | Practitioner Wisdom |
| 4 | #5-#8 + QA | All remaining patterns | All dimensions |

**Total: 12 templates in 30 days. Eight distinct interaction primitives proven in production.**