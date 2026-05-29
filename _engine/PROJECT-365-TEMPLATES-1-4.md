# PROJECT 365 — TOP 4 TEMPLATE BUILD SPECS

---

## TEMPLATE 01 — THE PRICE YOU'RE ACTUALLY CHARGING

---

### 1. Template Name
**The Price You're Actually Charging**
*Slug:* `template-price-floor`

---

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Clarity
- **Energy archetype:** The Mirror — not a teacher delivering a lesson, but a surface that shows you something you already contain but have not yet seen clearly.
- **Reader state on entry:** Mild unease. The reader suspects their rate is wrong but has not done the arithmetic.
- **Reader state on exit:** Grounded certainty. The number is no longer a guess.

---

### 3. Gradient Palette Spec

```css
/* Template 01 — Clarity / Living Income */
--gradient-bg: linear-gradient(160deg, #0f1923 0%, #1a2e3b 60%, #0d2233 100%);
--gradient-card: linear-gradient(135deg, #162535 0%, #1e3347 100%);
--accent-primary: #4fc3a1;      /* teal — the number that matters */
--accent-secondary: #e8b86d;    /* amber — warning zone / below floor */
--accent-confirm: #6fcf97;      /* green — above floor */
--accent-danger: #eb5757;       /* red — deep below floor */
--text-primary: #f0f4f8;
--text-secondary: #8fa8be;
--text-muted: #4a6278;
--border-subtle: rgba(79, 195, 161, 0.12);
--border-active: rgba(79, 195, 161, 0.45);
--slider-track: #1e3347;
--slider-fill: #4fc3a1;
--glow-floor: 0 0 32px rgba(79, 195, 161, 0.18);
```

---

### 4. The Interaction — Step by Step

**Step 0 — Entry / State Gate**
Reader sees a single screen: a large typographic question — *"Do you know the lowest rate you can charge and still keep your life intact?"* — with two buttons: `Yes, I know it` / `Not really`. Both proceed; the `Not really` path surfaces a brief orienting sentence before the calculator.

**Step 1 — Personal Expenses (Monthly)**
Four labeled number inputs with placeholder values:
- Housing (rent/mortgage, utilities)
- Food + transport
- Healthcare + insurance
- Everything else

A soft `+Add a line` link allows custom rows. A running subtotal updates in real time at the bottom of this group.

**Step 2 — Business Overhead (Monthly)**
Three inputs:
- Software, tools, subscriptions
- Professional development, dues
- Everything else business

Running subtotal updates.

**Step 3 — Tax Reserve**
A single slider: `What % do you set aside for taxes?` — range 0–45%, default 28%. A one-line tooltip: *"If you're not sure, 30% is a reasonable floor for US self-employed."* The slider shows the monthly dollar amount in real time as it moves.

**Step 4 — Billable Hours**
Two inputs:
- Hours per week you actually bill (not work — bill)
- Weeks per year you work

A soft note beneath: *"If you take 3 weeks off and have 1 week of unbillable time per month, your working weeks are roughly 44."*

**Step 5 — The Reveal**
Full-screen result. A large animated number: **Your floor rate: $XX/hr**

Below it, a comparison input: *"What are you currently charging?"*

The screen responds:
- If current rate > floor: teal glow, confirmation text
- If current rate = floor ± 10%: amber, caution text
- If current rate < floor: red, specific dollar deficit per month

A horizontal bar shows **floor vs current** as a ratio.

**Step 6 — The Takeaway**
One sentence, generated from their inputs, that is specific: *"At your current rate of $X and Y billable hours, you are earning $Z/month before taxes — $W below your stated floor."* No generic advice. Numbers only.

An optional share mechanic: `Get this as a PDF` (generates a clean summary page using the browser's print API, no server needed).

---

### 5. The Aha Moment
The reader has known roughly what they charge. They have not known, precisely, what they need. The reveal is not a judgment — it is arithmetic. The gap between the two numbers is their answer, and it is specific to them down to the dollar. Most readers will see, for the first time, that their floor is higher than they assumed and their rate is closer to or below it than they admitted.

---

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en" data-template="price-floor" data-state="entry">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Price You're Actually Charging — Meliorism2</title>
  <link rel="stylesheet" href="/assets/css/template-base.css">
  <link rel="stylesheet" href="/assets/css/template-price-floor.css">
</head>
<body class="t-price-floor">

  <!-- SCREEN 0: ENTRY -->
  <section class="screen screen--entry" id="screen-entry" aria-label="Entry">
    <div class="screen__inner screen__inner--centered">
      <span class="entry__eyebrow">Living Income · Issue [N]</span>
      <h1 class="entry__headline">
        Do you know the lowest rate<br>you can charge and still<br>keep your life intact?
      </h1>
      <div class="entry__cta-group">
        <button class="btn btn--primary" data-answer="yes" id="btn-yes">
          Yes, I know it
        </button>
        <button class="btn btn--ghost" data-answer="no" id="btn-no">
          Not really
        </button>
      </div>
    </div>
  </section>

  <!-- SCREEN 0b: ORIENT (shown only if "Not really") -->
  <section class="screen screen--orient screen--hidden" id="screen-orient">
    <div class="screen__inner screen__inner--narrow">
      <p class="orient__body">
        Your floor rate is the number your life requires — not the number
        you feel comfortable asking for. Most practitioners have never
        calculated it. This takes four minutes.
      </p>
      <button class="btn btn--primary" id="btn-orient-continue">
        Calculate mine
      </button>
    </div>
  </section>

  <!-- MAIN CALCULATOR FORM -->
  <section class="screen screen--calc screen--hidden" id="screen-calc">
    <div class="screen__inner">

      <!-- PROGRESS BAR -->
      <div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemax="4">
        <div class="progress-bar__fill" id="progress-fill"></div>
        <span class="progress-bar__label" id="progress-label">Step 1 of 4</span>
      </div>

      <!-- STEP 1: PERSONAL EXPENSES -->
      <fieldset class="calc-step" id="step-1" data-step="1">
        <legend class="calc-step__legend">
          <span class="step-number">01</span>
          Personal expenses — monthly
        </legend>
        <p class="calc-step__sub">What does your life actually cost each month?</p>

        <div class="input-group" id="personal-inputs">
          <div class="input-row">
            <label class="input-label" for="housing">Housing</label>
            <div class="input-wrap">
              <span class="input-prefix">$</span>
              <input class="input-field" type="number" id="housing"
                     name="housing" min="0" step="50" placeholder="0"
                     data-category="personal">
            </div>
          </div>
          <div class="input-row">
            <label class="input-label" for="food-transport">Food + transport</label>
            <div class="input-wrap">
              <span class="input-prefix">$</span>
              <input class="input-field" type="number" id="food-transport"
                     name="food-transport" min="0" step="50" placeholder="0"
                     data-category="personal">
            </div>
          </div>
          <div class="input-row">
            <label class="input-label" for="healthcare">Healthcare + insurance</label>
            <div class="input-wrap">
              <span class="input-prefix">$</span>
              <input class="input-field" type="number" id="healthcare"
                     name="healthcare" min="0" step="50" placeholder="0"
                     data-category="personal">
            </div>
          </div>
          <div class="input-row">
            <label class="input-label" for="personal-other">Everything else</label>
            <div class="input-wrap">
              <span class="input-prefix">$</span>
              <input class="input-field" type="number" id="personal-other"
                     name="personal-other" min="0" step="50" placeholder="0"
                     data-category="personal">
            </div>
          </div>

          <!-- Dynamic custom rows inserted here by JS -->
          <div id="personal-custom-rows"></div>

          <button type="button" class="btn btn--add-row" id="btn-add-personal">
            + Add a line
          </button>
        </div>

        <div class="step-subtotal">
          <span class="step-subtotal__label">Monthly personal total</span>
          <span class="step-subtotal__value" id="subtotal-personal">$0</span>
        </div>

        <button class="btn btn--primary btn--next" data-next="2">Next</button>
      </fieldset>

      <!-- STEP 2: BUSINESS OVERHEAD -->
      <fieldset class="calc-step calc-step--hidden" id="step-2" data-step="2">
        <legend class="calc-step__legend">
          <span class="step-number">02</span>
          Business overhead — monthly
        </legend>
        <p class="calc-step__sub">What does your practice cost to run?</p>

        <div class="input-group">
          <div class="input-row">
            <label class="input-label" for="software">Software + tools + subscriptions</label>
            <div class="input-wrap">
              <span class="input-prefix">$</span>
              <input class="input-field" type="number" id="software"
                     name="software" min="0" step="10" placeholder="0"
                     data-category="business">
            </div>
          </div>
          <div class="input-row">
            <label class="input-label" for="prodev">Professional development + dues</label>
            <div class="input-wrap">
              <span class="input-prefix">$</span>
              <input class="input-field" type="number" id="prodev"
                     name="prodev" min="0" step="10" placeholder="0"
                     data-category="business">
            </div>
          </div>
          <div class="input-row">
            <label class="input-label" for="business-other">Everything else</label>
            <div class="input-wrap">
              <span class="input-prefix">$</span>
              <input class="input-field" type="number" id="business-other"
                     name="business-other" min="0" step="10" placeholder="0"
                     data-category="business">
            </div>
          </div>

          <div id="business-custom-rows"></div>
          <button type="button" class="btn btn--add-row" id="btn-add-business">
            + Add a line
          </button>
        </div>

        <div class="step-subtotal">
          <span class="step-subtotal__label">Monthly business total</span>
          <span class="step-subtotal__value" id="subtotal-business">$0</span>
        </div>

        <div class="step-nav">
          <button class="btn btn--ghost btn--back" data-back="1">Back</button>
          <button class="btn btn--primary btn--next" data-next="3">Next</button>
        </div>
      </fieldset>

      <!-- STEP 3: TAX RESERVE -->
      <fieldset class="calc-step calc-step--hidden" id="step-3" data-step="3">
        <legend class="calc-step__legend">
          <span class="step-number">03</span>
          Tax reserve
        </legend>
        <p class="calc-step__sub">
          What percentage of gross income do you set aside for taxes?
        </p>

        <div class="slider-group">
          <div class="slider-labels">
            <span>0%</span>
            <span id="tax-pct-display" class="slider-current-value">28%</span>
            <span>45%</span>
          </div>
          <input class="slider" type="range" id="tax-rate"
                 min="0" max="45" value="28" step="1">
          <p class="slider-hint">
            <span class="hint-icon">→</span>
            At this rate, your monthly tax reserve on a $X gross is
            <strong id="tax-monthly-amount">$0</strong>.
          </p>
          <p class="slider-note">
            Not sure? 30% is a reasonable floor for US self-employed.
          </p>
        </div>

        <div class="step-nav">
          <button class="btn btn--ghost btn--back" data-back="2">Back</button>
          <button class="btn btn--primary btn--next" data-next="4">Next</button>
        </div>
      </fieldset>

      <!-- STEP 4: BILLABLE HOURS -->
      <fieldset class="calc-step calc-step--hidden" id="step-4" data-step="4">
        <legend class="calc-step__legend">
          <span class="step-number">04</span>
          Billable hours
        </legend>
        <p class="calc-step__sub">
          Not hours you work — hours you bill.
        </p>

        <div class="input-group">
          <div class="input-row">
            <label class="input-label" for="hours-per-week">
              Billable hours per week
            </label>
            <div class="input-wrap">
              <input class="input-field input-field--short" type="number"
                     id="hours-per-week" name="hours-per-week"
                     min="1" max="80" step="1" placeholder="20">
              <span class="input-suffix">hrs</span>
            </div>
          </div>
          <div class="input-row">
            <label class="input-label" for="weeks-per-year">
              Working weeks per year
            </label>
            <div class="input-wrap">
              <input class="input-field input-field--short" type="number"
                     id="weeks-per-year" name="weeks-per-year"
                     min="1" max="52" step="1" placeholder="46">
              <span class="input-suffix">wks</span>
            </div>
          </div>
        </div>

        <p class="input-hint">
          If you take 3 weeks off and have roughly 1 unbillable week per month,
          your working weeks are around 44–46.
        </p>

        <div class="live-preview" id="hours-preview">
          Annual billable hours: <strong id="annual-hours">--</strong>
        </div>

        <div class="step-nav">
          <button class="btn btn--ghost btn--back" data-back="3">Back</button>
          <button class="btn btn--primary" id="btn-calculate">
            Show my floor
          </button>
        </div>
      </fieldset>

    </div>
  </section>

  <!-- SCREEN: REVEAL -->
  <section class="screen screen--reveal screen--hidden" id="screen-reveal">
    <div class="screen__inner screen__inner--reveal">

      <p class="reveal__eyebrow">Your floor rate</p>
      <div class="reveal__number-wrap">
        <span class="reveal__currency">$</span>
        <span class="reveal__number" id="floor-rate-display">--</span>
        <span class="reveal__unit">/hr</span>
      </div>
      <p class="reveal__sub" id="reveal-sub">per hour to cover your life and practice</p>

      <!-- COMPARISON INPUT -->
      <div class="comparison-block" id="comparison-block">
        <label class="comparison-label" for="current-rate">
          What are you currently charging?
        </label>
        <div class="comparison-input-wrap">
          <span class="input-prefix">$</span>
          <input class="input-field input-field--large" type="number"
                 id="current-rate" name="current-rate"
                 min="0" step="5" placeholder="0">
          <span class="input-suffix">/hr</span>
        </div>
      </div>

      <!-- DELTA DISPLAY — shown after current-rate is entered -->
      <div class="delta-block delta-block--hidden" id="delta-block">
        <div class="delta-bar-wrap">
          <div class="delta-bar" id="delta-bar">
            <div class="delta-bar__floor" id="delta-bar-floor"></div>
            <div class="delta-bar__current" id="delta-bar-current"></div>
          </div>
          <div class="delta-bar-labels">
            <span id="delta-label-floor">Floor</span>
            <span id="delta-label-current">Current</span>
          </div>
        </div>
        <p class="delta-verdict" id="delta-verdict"></p>
        <p class="delta-sentence" id="delta-sentence"></p>
      </div>

      <!-- ACTIONS -->
      <div class="reveal__actions">
        <button class="btn btn--ghost" id="btn-recalculate">
          Recalculate
        </button>
        <button class="btn btn--primary" id="btn-save-pdf"
                onclick="window.print()">
          Save as PDF
        </button>
      </div>

    </div>
  </section>

  <script src="/assets/js/template-price-floor.js"></script>
</body>
</html>
```

---

### 7. Interaction JavaScript

```javascript
// template-price-floor.js
// Template 01 — The Price You're Actually Charging

(function () {
  'use strict';

  // ── STATE ─────────────────────────────────────────────────────────────────
  const state = {
    personal: 0,
    business: 0,
    taxRate: 28,        // percent
    hoursPerWeek: 0,
    weeksPerYear: 0,
    floorRate: 0,
    currentRate: null,
  };

  // ── ELEMENT REFS ──────────────────────────────────────────────────────────
  const $ = (id) => document.getElementById(id);

  // ── FORMATTING ────────────────────────────────────────────────────────────
  function formatMoney(n) {
    return '$' + Math.round(n).toLocaleString('en-US');
  }

  function formatRate(n) {
    return Math.ceil(n).toLocaleString('en-US');
  }

  // ── SCREEN MANAGEMENT ─────────────────────────────────────────────────────
  function showScreen(id) {
    document.querySelectorAll('.screen').forEach((s) => {
      s.classList.add('screen--hidden');
      s.setAttribute('aria-hidden', 'true');
    });
    const target = $(id);
    target.classList.remove('screen--hidden');
    target.removeAttribute('aria-hidden');
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function showStep(n) {
    document.querySelectorAll('.calc-step').forEach((s) => {
      s.classList.add('calc-step--hidden');
    });
    $('step-' + n).classList.remove('calc-step--hidden');
    updateProgress(n);
  }

  function updateProgress(step) {
    const pct = ((step - 1) / 4) * 100;
    $('progress-fill').style.width = pct + '%';
    $('progress-label').textContent = 'Step ' + step + ' of 4';
    document.querySelector('.progress-bar')
      .setAttribute('aria-valuenow', step);
  }

  // ── SUBTOTAL CALCULATOR ───────────────────────────────────────────────────
  function sumCategory(category) {
    const inputs = document.querySelectorAll(
      `input[data-category="${category}"]`
    );
    let total = 0;
    inputs.forEach((inp) => {
      total += parseFloat(inp.value) || 0;
    });
    return total;
  }

  function updateSubtotals() {
    state.personal = sumCategory('personal');
    state.business = sumCategory('business');
    $('subtotal-personal').textContent = formatMoney(state.personal);
    $('subtotal-business').textContent = formatMoney(state.business);
    updateTaxHint();
  }

  // ── TAX SLIDER ────────────────────────────────────────────────────────────
  function updateTaxHint() {
    const grossNeeded = state.personal + state.business;
    const taxMonthly = grossNeeded * (state.taxRate / 100);
    $('tax-monthly-amount').textContent = formatMoney(taxMonthly);
    $('tax-pct-display').textContent = state.taxRate + '%';
  }

  // ── FLOOR CALCULATION ─────────────────────────────────────────────────────
  // Formula:
  //   Monthly need = personal + business
  //   Gross monthly needed = monthly need / (1 - taxRate/100)
  //   Annual gross needed = gross monthly * 12
  //   Annual billable hours = hoursPerWeek * weeksPerYear
  //   Floor rate = annualGrossNeeded / annualBillableHours
  function calculateFloor() {
    const monthlyNet = state.personal + state.business;
    const grossMonthly = monthlyNet / (1 - state.taxRate / 100);
    const grossAnnual = grossMonthly * 12;
    const annualHours = state.hoursPerWeek * state.weeksPerYear;

    if (annualHours === 0) return 0;
    return grossAnnual / annualHours;
  }

  // ── REVEAL SCREEN ─────────────────────────────────────────────────────────
  function showReveal() {
    state.floorRate = calculateFloor();
    $('floor-rate-display').textContent = formatRate(state.floorRate);

    // Animate the number counting up
    animateNumber($('floor-rate-display'), 0, state.floorRate, 800);

    showScreen('screen-reveal');
  }

  function animateNumber(el, from, to, duration) {
    const start = performance.now();
    const diff = to - from;
    function step(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.ceil(from + diff * eased).toLocaleString('en-US');
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  // ── COMPARISON / DELTA ────────────────────────────────────────────────────
  function updateDelta(currentRate) {
    state.currentRate = currentRate;
    const floor = state.floorRate;
    const delta = currentRate - floor;
    const deltaBlock = $('delta-block');
    deltaBlock.classList.remove('delta-block--hidden');

    // Bar widths — normalize to wider of the two = 100%
    const max = Math.max(floor, currentRate, 1);
    const floorPct = (floor / max) * 100;
    const currentPct = (currentRate / max) * 100;
    $('delta-bar-floor').style.width = floorPct + '%';
    $('delta-bar-current').style.width = currentPct + '%';
    $('delta-label-floor').textContent =
      'Floor ' + formatMoney(floor) + '/hr';
    $('delta-label-current').textContent =
      'Yours ' + formatMoney(currentRate) + '/hr';

    // Verdict class + text
    const verdict = $('delta-verdict');
    const sentence = $('delta-sentence');

    // Clear existing state classes
    deltaBlock.classList.remove(
      'delta--above', 'delta--close', 'delta--below'
    );

    const pctDiff = ((currentRate - floor) / floor) * 100;
    const monthlyShortfall = (floor - currentRate) * state.hoursPerWeek * 4;
    const monthlyHoursWorked = state.hoursPerWeek * 4;

    if (pctDiff > 10) {
      deltaBlock.classList.add('delta--above');
      verdict.textContent = 'Above your floor.';
      sentence.textContent =
        `At ${formatMoney(currentRate)}/hr and ` +
        `${state.hoursPerWeek} billable hours per week, ` +
        `you are earning ${formatMoney(currentRate * monthlyHoursWorked)}/month gross — ` +
        `${formatMoney(delta * monthlyHoursWorked)} above your floor.`;
    } else if (pctDiff >= -10) {
      deltaBlock.classList.add('delta--close');
      verdict.textContent = 'Within 10% of your floor. Worth watching.';
      sentence.textContent =
        `At ${formatMoney(currentRate)}/hr you have a margin of ` +
        `${formatMoney(Math.abs(delta * monthlyHoursWorked))}/month. ` +
        `A single slow month puts you below the line.`;
    } else {
      deltaBlock.classList.add('delta--below');
      verdict.textContent = 'Below your floor.';
      sentence.textContent =
        `At ${formatMoney(currentRate)}/hr you are running ` +
        `${formatMoney(Math.abs(monthlyShortfall))}/month short of what ` +
        `your life requires — before a single unexpected expense.`;
    }
  }

  // ── ADD ROW ───────────────────────────────────────────────────────────────
  let customRowCount = 0;
  function addCustomRow(containerId, category) {
    customRowCount++;
    const id = `custom-${category}-${customRowCount}`;
    const row = document.createElement('div');
    row.className = 'input-row input-row--custom';
    row.innerHTML = `
      <input class="input-label input-label--editable"
             type="text" placeholder="Label"
             aria-label="Custom line item label">
      <div class="input-wrap">
        <span class="input-prefix">$</span>
        <input class="input-field" type="number" id="${id}"
               name="${id}" min="0" step="10" placeholder="0"
               data-category="${category}">
        <button type="button" class="btn btn--remove-row"
                aria-label="Remove this row">×</button>
      </div>
    `;
    row.querySelector('.btn--remove-row').addEventListener('click', () => {
      row.remove();
      updateSubtotals();
    });
    row.querySelector('.input-field').addEventListener('input', updateSubtotals);
    $(containerId).appendChild(row);
  }

  // ── EVENT LISTENERS ───────────────────────────────────────────────────────
  function init() {

    // Entry buttons
    $('btn-yes').addEventListener('click', () => {
      showScreen('screen-calc');
      showStep(1);
    });
    $('btn-no').addEventListener('click', () => {
      showScreen('screen-orient');
    });
    $('btn-orient-continue').addEventListener('click', () => {
      showScreen('screen-calc');
      showStep(1);
    });

    // Step navigation — delegated on calc screen
    $('screen-calc').addEventListener('click', (e) => {
      if (e.target.matches('.btn--next')) {
        const nextStep = parseInt(e.target.dataset.next, 10);
        showStep(nextStep);
      }
      if (e.target.matches('.btn--back')) {
        const prevStep = parseInt(e.target.dataset.back, 10);
        showStep(prevStep);
      }
    });

    // Live subtotals
    document.querySelectorAll('input[data-category]').forEach((inp) => {
      inp.addEventListener('input', updateSubtotals);
    });

    // Add row buttons
    $('btn-add-personal').addEventListener('click', () => {
      addCustomRow('personal-custom-rows', 'personal');
    });
    $('btn-add-business').addEventListener('click', () => {
      addCustomRow('business-custom-rows', 'business');
    });

    // Tax slider
    $('tax-rate').addEventListener('input', (e) => {
      state.taxRate = parseInt(e.target.value, 10);
      updateTaxHint();
    });

    // Hours preview
    function updateHoursPreview() {
      const h = parseInt($('hours-per-week').value, 10) || 0;
      const w = parseInt($('weeks-per-year').value, 10) || 0;
      state.hoursPerWeek = h;
      state.weeksPerYear = w;
      $('annual-hours').textContent =
        (h * w).toLocaleString('en-US') + ' hours';
    }
    $('hours-per-week').addEventListener('input', updateHoursPreview);
    $('weeks-per-year').addEventListener('input', updateHoursPreview);

    // Calculate button
    $('btn-calculate').addEventListener('click', () => {
      state.hoursPerWeek =
        parseInt($('hours-per-week').value, 10) || 0;
      state.weeksPerYear =
        parseInt($('weeks-per-year').value, 10) || 0;
      showReveal();
    });

    // Current rate comparison
    $('current-rate').addEventListener('input', (e) => {
      const val = parseFloat(e.target.value);
      if (!isNaN(val) && val > 0) {
        updateDelta(val);
      }
    });

    // Recalculate
    $('btn-recalculate').addEventListener('click', () => {
      showScreen('screen-calc');
      showStep(1);
    });

    // Init display
    updateSubtotals();
    updateTaxHint();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
```

---

### 8. Entry Screen Design

The Cover Agent builds a full-bleed dark screen with the gradient background. Centered vertically and horizontally:

- Small all-caps eyebrow in `--text-muted`: `LIVING INCOME · ISSUE [N]`
- A single headline in `--text-primary`, large (clamp 2.4rem–4.8rem), line breaks for rhythm: `Do you know the lowest rate / you can charge and still / keep your life intact?`
- A 48px gap
- Two buttons side by side: `Yes, I know it` (teal fill, `--accent-primary`) and `Not really` (ghost/outline, `--border-active`)
- No decorative images. No background illustration. The only visual weight is the type.
- A soft ambient glow effect — a radial gradient in the background at 30% opacity, centered behind the headline, using `--accent-primary` at 8% alpha.

---

### 9. Newsletter-Impossible Element

The live floor rate calculation that responds to the reader's own numbers in real time. No email client renders a live calculating form that takes four personal inputs, applies a formula, and surfaces a specific dollar figure contingent on the reader's life. The letter version could give the formula. Only the interactive version gives the number. The aha is not the formula — it is the number.

---

### 10. Style Guide Entry

```
TEMPLATE-01 — THE PRICE YOU'RE ACTUALLY CHARGING
─────────────────────────────────────────────────
Slug:            template-price-floor
Dimension:       Living Income
Emotional weather: Clarity
Interaction type: Reactive document (multi-step calculator)
NI rating:       5/5
Build complexity: Low

Palette:
  bg             #0f1923 → #0d2233
  card           #162535 → #1e3347
  accent         #4fc3a1 (teal)
  warning        #e8b86d (amber)
  confirm        #6fcf97 (green)
  danger         #eb5757 (red)

Core formula:
  floor = (monthlyNet / (1 - taxRate)) * 12 / annualBillableHours

Screens:   entry → [orient] → calc(4 steps) → reveal
State:     5 fields: personal, business, taxRate, hoursPerWeek, weeksPerYear

Critical UX rules:
  · Running subtotals visible at all times within their step
  · Reveal animates number from 0 to floor (800ms ease-out cubic)
  · Delta block hidden until current-rate is entered
  · Bar chart normalizes to max(floor, current) = 100%
  · PDF save uses window.print() — no server, no tracking

Files:
  /assets/css/template-price-floor.css
  /assets/js/template-price-floor.js
  /templates/price-floor/index.html
```

---
---

## TEMPLATE 02 — DRAW THE CURVE BEFORE YOU SEE IT

---

### 1. Template Name
**Draw the Curve Before You See It**
*Slug:* `template-draw-the-curve`

---

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Threshold
- **Energy archetype:** The Confrontation — not hostile, but honest. The reader's own hand draws the line that proves their assumption wrong.
- **Reader state on entry:** Confident. They think they know what the data looks like.
- **Reader state on exit:** Recalibrated. The gap between their line and the real line is not an accusation — it is information.

---

### 3. Gradient Palette Spec

```css
/* Template 02 — Threshold / Prediction Confrontation */
--gradient-bg: linear-gradient(150deg, #12101e 0%, #1c1630 55%, #110e1c 100%);
--gradient-card: linear-gradient(135deg, #1a1730 0%, #221e40 100%);
--accent-primary: #8b7ffa;      /* violet — the reader's prediction */
--accent-data: #f5a623;         /* amber — the real data curve */
--accent-gap: rgba(245,166,35,0.15); /* gap fill between curves */
--accent-confirm: #6fcf97;      /* green — for calibrated predictions */
--text-primary: #ede9ff;
--text-secondary: #9e96c8;
--text-muted: #584f82;
--border-subtle: rgba(139, 127, 250, 0.12);
--border-active: rgba(139, 127, 250, 0.4);
--canvas-bg: #0e0c1a;
--canvas-grid: rgba(255,255,255,0.04);
--prediction-line: #8b7ffa;
--data-line: #f5a623;
--glow-prediction: 0 0 24px rgba(139, 127, 250, 0.25);
```

---

### 4. The Interaction — Step by Step

**Step 0 — Entry**
Full-bleed screen. The question: *"What does the relationship between practitioner years of experience and hourly rate actually look like?"* Two small sub-questions primed below: *"Does it flatten? Accelerate? Plateau early?"* A single button: `Draw your prediction`.

**Step 1 — The Drawing Canvas**
A blank chart appears. X-axis: `Years in practice (0–25)`. Y-axis: `Hourly rate ($0–$500)`. Light grid lines only. No data points yet.

Instructions: *"Use your mouse or finger to draw what you think the curve looks like. Start anywhere."*

A crosshair cursor on the canvas. As the reader clicks and drags (or taps and drags on mobile), a violet line traces their prediction. They can redraw at any time before confirming. A `Clear` button resets the canvas.

When the reader lifts the finger/mouse: the line is rendered as a smooth SVG path, slightly glowing.

A `That's my prediction` button appears below the canvas.

**Step 2 — The Reveal**
The reader confirms. The real data curve animates in over 1.2 seconds in amber (`--accent-data`). The gap between the two curves fills with a soft amber wash.

A subtle annotation appears at the divergence point: *"Your line"* (violet) and *"Peer data"* (amber).

**Step 3 — The Reading**
Below the chart, a generated reading based on two measurements: (a) the direction of the reader's prediction vs. the real curve, and (b) the magnitude of the gap.

Four possible readings:
- **Overestimate, early plateau** — *"You predicted steeper early gains than practitioners report. The real curve rises more slowly through year 5."*
- **Underestimate, strong mid-career** — *"You drew a flatter curve than the data. Mid-career (years 7–14) shows larger gains than most practitioners expect."*
- **Overestimate, late-career** — *"Your prediction steepened past year 15. Real data shows a plateau — ceiling effects, market saturation, or a deliberate choice to stop raising."*
- **Calibrated** — *"Your prediction tracked the real curve within a 12% margin. That's unusual. Most practitioners draw their own wishful version."*

**Step 4 — The Question**
One line below the reading: *"Where does your current trajectory put you on that curve?"* A single button: `Calculate mine →` (links to Template 01 if not already completed, or surfaces a simplified rate-vs-years comparison if Template 01 data is available in sessionStorage).

---

### 5. The Aha Moment
The reader's hand drew the evidence. They cannot externalize the mistake as "something someone told them" — they made it themselves, in public (to themselves), on a chart. The gap between their violet line and the amber data is the specific shape of their miscalibration. The reading names it without judgment. This is what prediction confrontation produces: the gap is the lesson.

---

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en" data-template="draw-the-curve" data-state="entry">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Draw the Curve Before You See It — Meliorism2</title>
  <link rel="stylesheet" href="/assets/css/template-base.css">
  <link rel="stylesheet" href="/assets/css/template-draw-the-curve.css">
</head>
<body class="t-draw-curve">

  <!-- SCREEN 0: ENTRY -->
  <section class="screen screen--entry" id="screen-entry">
    <div class="screen__inner screen__inner--centered">
      <span class="entry__eyebrow">Practitioner Wisdom · Issue [N]</span>
      <h1 class="entry__headline">
        What does the relationship between<br>
        practitioner experience and hourly rate<br>
        actually look like?
      </h1>
      <p class="entry__body">
        Does it flatten? Accelerate? Plateau early?<br>
        Draw what you think — before you see it.
      </p>
      <button class="btn btn--primary" id="btn-start-drawing">
        Draw my prediction
      </button>
    </div>
  </section>

  <!-- SCREEN 1: DRAWING CANVAS -->
  <section class="screen screen--canvas screen--hidden" id="screen-canvas">
    <div class="screen__inner">

      <div class="canvas-header">
        <h2 class="canvas-title">Draw the curve</h2>
        <p class="canvas-instructions">
          Click and drag (or touch and drag) to draw what you think
          the curve looks like. You can redraw as many times as you want.
        </p>
      </div>

      <div class="chart-container" id="chart-container">

        <!-- Y-axis label -->
        <div class="axis-label axis-label--y">Hourly rate ($)</div>

        <!-- Y-axis ticks -->
        <div class="y-ticks" id="y-ticks" aria-hidden="true"></div>

        <!-- Main SVG chart area -->
        <svg class="chart-svg" id="chart-svg"
             viewBox="0 0 800 400" preserveAspectRatio="xMidYMid meet"
             role="img" aria-label="Chart for drawing prediction">

          <!-- Grid lines -->
          <g class="chart-grid" id="chart-grid"></g>

          <!-- Axis lines -->
          <line class="axis-line" x1="60" y1="20" x2="60" y2="360"/>
          <line class="axis-line" x1="60" y1="360" x2="780" y2="360"/>

          <!-- X-axis labels -->
          <g class="x-labels" id="x-labels"></g>

          <!-- Y-axis labels -->
          <g class="y-labels" id="y-labels"></g>

          <!-- Gap fill between prediction and real (hidden until reveal) -->
          <path class="gap-fill gap-fill--hidden" id="gap-fill" d=""/>

          <!-- Real data path (hidden until reveal) -->
          <path class="data-curve data-curve--hidden" id="data-curve" d=""/>

          <!-- Prediction path (drawn by reader) -->
          <path class="prediction-curve" id="prediction-curve" d=""/>

          <!-- Drawing capture overlay -->
          <rect class="draw-overlay" id="draw-overlay"
                x="60" y="20" width="720" height="340"
                fill="transparent" style="cursor:crosshair"/>

          <!-- Annotations (hidden until reveal) -->
          <g class="annotations annotations--hidden" id="annotations"></g>

        </svg>

        <!-- X-axis label -->
        <div class="axis-label axis-label--x">Years in practice</div>

      </div>

      <div class="canvas-controls">
        <button class="btn btn--ghost btn--sm" id="btn-clear-drawing">
          Clear
        </button>
        <button class="btn btn--primary btn--confirm"
                id="btn-confirm-prediction" disabled>
          That's my prediction
        </button>
      </div>

    </div>
  </section>

  <!-- SCREEN 2+3: REVEAL + READING -->
  <section class="screen screen--reveal screen--hidden" id="screen-reveal">
    <div class="screen__inner">

      <div class="reveal-header">
        <h2 class="reveal-title">Here's what the data shows.</h2>
      </div>

      <!-- Replay of chart with both curves -->
      <div class="chart-container chart-container--reveal" id="chart-reveal-container">
        <div class="axis-label axis-label--y">Hourly rate ($)</div>
        <svg class="chart-svg" id="chart-svg-reveal"
             viewBox="0 0 800 400" preserveAspectRatio="xMidYMid meet"
             role="img" aria-label="Prediction vs real data comparison">
          <g class="chart-grid" id="reveal-grid"></g>
          <line class="axis-line" x1="60" y1="20" x2="60" y2="360"/>
          <line class="axis-line" x1="60" y1="360" x2="780" y2="360"/>
          <g class="x-labels" id="reveal-x-labels"></g>
          <g class="y-labels" id="reveal-y-labels"></g>

          <!-- Gap fill -->
          <path class="gap-fill" id="reveal-gap-fill" d=""/>

          <!-- Real data curve (animates in) -->
          <path class="data-curve" id="reveal-data-curve" d=""/>

          <!-- Reader's prediction (static copy) -->
          <path class="prediction-curve prediction-curve--frozen"
                id="reveal-prediction-curve" d=""/>

          <!-- Legend labels -->
          <g id="reveal-annotations"></g>
        </svg>
        <div class="axis-label axis-label--x">Years in practice</div>

        <!-- Legend -->
        <div class="chart-legend">
          <div class="legend-item">
            <span class="legend-swatch legend-swatch--prediction"></span>
            Your prediction
          </div>
          <div class="legend-item">
            <span class="legend-swatch legend-swatch--data"></span>
            Peer data
          </div>
        </div>
      </div>

      <!-- Generated reading -->
      <div class="reading-block" id="reading-block">
        <p class="reading-text" id="reading-text"></p>
      </div>

      <!-- Pivot question -->
      <div class="pivot-block">
        <p class="pivot-question">
          Where does your current trajectory put you on that curve?
        </p>
        <button class="btn btn--primary" id="btn-pivot">
          Calculate mine →
        </button>
      </div>

    </div>
  </section>

  <script src="/assets/js/template-draw-the-curve.js"></script>
</body>
</html>
```

---

### 7. Interaction JavaScript

```javascript
// template-draw-the-curve.js
// Template 02 — Draw the Curve Before You See It

(function () {
  'use strict';

  // ── CHART GEOMETRY ────────────────────────────────────────────────────────
  // SVG viewBox: 0 0 800 400
  // Plot area: x 60–780, y 20–360  →  width 720, height 340
  const PLOT = { x0: 60, y0: 20, x1: 780, y1: 360 };
  const X_RANGE = [0, 25];    // years
  const Y_RANGE = [0, 500];   // dollars

  // Actual peer data — normalized array of [year, rate] pairs
  // This is the "real curve" the reader's prediction will be compared against.
  // Source: synthesized from practitioner survey data referenced in issue copy.
  const REAL_DATA = [
    [0, 55], [1, 65], [2, 80], [3, 95], [4, 112],
    [5, 130], [7, 158], [9, 185], [11, 210], [13, 232],
    [15, 248], [17, 260], [19, 268], [21, 272], [23, 274], [25, 275]
  ];

  // ── COORDINATE TRANSFORMS ─────────────────────────────────────────────────
  function xToSvg(year) {
    const pct = (year - X_RANGE[0]) / (X_RANGE[1] - X_RANGE[0]);
    return PLOT.x0 + pct * (PLOT.x1 - PLOT.x0);
  }

  function yToSvg(rate) {
    const pct = (rate - Y_RANGE[0]) / (Y_RANGE[1] - Y_RANGE[0]);
    return PLOT.y1 - pct * (PLOT.y1 - PLOT.y0);  // inverted: high rate = low y
  }

  function svgToData(svgX, svgY) {
    const year = X_RANGE[0] +
      ((svgX - PLOT.x0) / (PLOT.x1 - PLOT.x0)) * (X_RANGE[1] - X_RANGE[0]);
    const rate = Y_RANGE[0] +
      ((PLOT.y1 - svgY) / (PLOT.y1 - PLOT.y0)) * (Y_RANGE[1] - Y_RANGE[0]);
    return { year, rate };
  }

  // ── SVG HELPERS ───────────────────────────────────────────────────────────
  function makePath(points) {
    if (points.length === 0) return '';
    return 'M ' + points.map((p) => `${p.x},${p.y}`).join(' L ');
  }

  function smoothPath(points) {
    // Catmull-Rom spline approximation via cubic bezier
    if (points.length < 2) return makePath(points);
    let d = `M ${points[0].x},${points[0].y}`;
    for (let i = 0; i < points.length - 1; i++) {
      const p0 = points[Math.max(0, i - 1)];
      const p1 = points[i];
      const p2 = points[i + 1];
      const p3 = points[Math.min(points.length - 1, i + 2)];
      const cp1x = p1.x + (p2.x - p0.x) / 6;
      const cp1y = p1.y + (p2.y - p0.y) / 6;
      const cp2x = p2.x - (p3.x - p1.x) / 6;
      const cp2y = p2.y - (p3.y - p1.y) / 6;
      d += ` C ${cp1x},${cp1y} ${cp2x},${cp2y} ${p2.x},${p2.y}`;
    }
    return d;
  }

  // ── GRID SETUP ────────────────────────────────────────────────────────────
  function buildGrid(svgId, gridId, xLabelsId, yLabelsId) {
    const svg = document.getElementById(svgId);
    const grid = document.getElementById(gridId);
    const xLabels = document.getElementById(xLabelsId);
    const yLabels = document.getElementById(yLabelsId);

    const xTicks = [0, 5, 10, 15, 20, 25];
    const yTicks = [0, 100, 200, 300, 400, 500];

    xTicks.forEach((yr) => {
      const x = xToSvg(yr);
      const line = document.createElementNS(
        'http://www.w3.org/2000/svg', 'line'
      );
      line.setAttribute('x1', x); line.setAttribute('y1', PLOT.y0);
      line.setAttribute('x2', x); line.setAttribute('y2', PLOT.y1);
      line.setAttribute('class', 'grid-line');
      grid.appendChild(line);

      const text = document.createElementNS(
        'http://www.w3.org/2000/svg', 'text'
      );
      text.setAttribute('x', x);
      text.setAttribute('y', PLOT.y1 + 20);
      text.setAttribute('class', 'axis-tick-label');
      text.textContent = yr;
      xLabels.appendChild(text);
    });

    yTicks.forEach((rate) => {
      const y = yToSvg(rate);
      const line = document.createElementNS(
        'http://www.w3.org/2000/svg', 'line'
      );
      line.setAttribute('x1', PLOT.x0); line.setAttribute('y1', y);
      line.setAttribute('x2', PLOT.x1); line.setAttribute('y2', y);
      line.setAttribute('class', 'grid-line');
      grid.appendChild(line);

      const text = document.createElementNS(
        'http://www.w3.org/2000/svg', 'text'
      );
      text.setAttribute('x', PLOT.x0 - 8);
      text.setAttribute('y', y + 4);
      text.setAttribute('class', 'axis-tick-label axis-tick-label--y');
      text.textContent = '$' + rate;
      yLabels.appendChild(text);
    });
  }

  // ── DRAWING ENGINE ────────────────────────────────────────────────────────
  let isDrawing = false;
  let rawPoints = [];       // [{x, y}] in SVG coords
  let sampledPoints = [];   // decimated for smooth path

  function getSvgPoint(event, svg) {
    const rect = svg.getBoundingClientRect();
    const clientX = event.touches ? event.touches[0].clientX : event.clientX;
    const clientY = event.touches ? event.touches[0].clientY : event.clientY;
    // Map from screen coords to SVG viewBox coords
    const scaleX = 800 / rect.width;
    const scaleY = 400 / rect.height;
    return {
      x: (clientX - rect.left) * scaleX,
      y: (clientY - rect.top) * scaleY
    };
  }

  function clampToPlot(pt) {
    return {
      x: Math.max(PLOT.x0, Math.min(PLOT.x1, pt.x)),
      y: Math.max(PLOT.y0, Math.min(PLOT.y1, pt.y))
    };
  }

  function startDraw(event) {
    event.preventDefault();
    isDrawing = true;
    rawPoints = [];
    const svg = document.getElementById('chart-svg');
    const pt = clampToPlot(getSvgPoint(event, svg));
    rawPoints.push(pt);
    updatePredictionPath();
  }

  function continueDraw(event) {
    if (!isDrawing) return;
    event.preventDefault();
    const svg = document.getElementById('chart-svg');
    const pt = clampToPlot(getSvgPoint(event, svg));
    // Decimate: only add if moved > 8px
    const last = rawPoints[rawPoints.length - 1];
    const dist = Math.hypot(pt.x - last.x, pt.y - last.y);
    if (dist > 8) {
      rawPoints.push(pt);
      updatePredictionPath();
    }
  }

  function endDraw() {
    if (!isDrawing) return;
    isDrawing = false;
    sampledPoints = [...rawPoints];
    const confirmBtn = document.getElementById('btn-confirm-prediction');
    if (sampledPoints.length >= 3) {
      confirmBtn.removeAttribute('disabled');
    }
  }

  function updatePredictionPath() {
    const path = document.getElementById('prediction-curve');
    path.setAttribute('d', smoothPath(rawPoints));
  }

  function clearDrawing() {
    rawPoints = [];
    sampledPoints = [];
    document.getElementById('prediction-curve').setAttribute('d', '');
    document.getElementById('btn-confirm-prediction')
      .setAttribute('disabled', '');
  }

  // ── REAL DATA PATH ────────────────────────────────────────────────────────
  function getRealDataPoints() {
    return REAL_DATA.map(([yr, rate]) => ({
      x: xToSvg(yr),
      y: yToSvg(rate)
    }));
  }

  // ── REVEAL ANIMATION ──────────────────────────────────────────────────────
  function revealDataCurve() {
    const realPts = getRealDataPoints();
    const pathEl = document.getElementById('reveal-data-curve');
    const fullD = smoothPath(realPts);
    pathEl.setAttribute('d', fullD);

    // Animate using SVG stroke-dashoffset
    const length = pathEl.getTotalLength();
    pathEl.style.strokeDasharray = length;
    pathEl.style.strokeDashoffset = length;
    // Force reflow
    pathEl.getBoundingClientRect();
    pathEl.style.transition = 'stroke-dashoffset 1.2s cubic-bezier(0.4,0,0.2,1)';
    pathEl.style.strokeDashoffset = 0;
  }

  function buildGapFill(predPoints, realPoints) {
    // Build a closed polygon: prediction forward, real backward
    if (predPoints.length < 2) return;

    // Normalize prediction to same x domain as real data
    // by sampling the prediction path at each real data x
    const pathEl = document.getElementById('reveal-prediction-curve');

    const gapPoints = [];

    // Forward: real data points
    realPoints.forEach((pt) => gapPoints.push(pt));

    // Find y on prediction path for each real x
    // Approximation: walk sampled prediction points
    const predYAtX = (targetX) => {
      let closest = predPoints[0];
      let minDist = Math.abs(predPoints[0].x - targetX);
      predPoints.forEach((pt) => {
        const d = Math.abs(pt.x - targetX);
        if (d < minDist) { minDist = d; closest = pt; }
      });
      return closest.y;
    };

    // Backward: prediction at same x positions (reversed)
    const reversed = [...realPoints].reverse().map((pt) => ({
      x: pt.x,
      y: predYAtX(pt.x)
    }));
    reversed.forEach((pt) => gapPoints.push(pt));

    const gapPath = document.getElementById('reveal-gap-fill');
    gapPath.setAttribute(
      'd',
      'M ' + gapPoints.map((p) => `${p.x},${p.y}`).join(' L ') + ' Z'
    );
  }

  // ── PREDICTION ANALYSIS ───────────────────────────────────────────────────
  function analyzePrediction(predPoints) {
    if (predPoints.length < 3) {
      return 'Your prediction did not have enough data points to analyze.';
    }

    const realPts = getRealDataPoints();

    // Sample prediction at 5 x checkpoints: years 3, 8, 13, 18, 23
    const checkYears = [3, 8, 13, 18, 23];
    const checkXs = checkYears.map(xToSvg);

    function yAtX(points, targetX) {
      let best = points[0];
      let bestDist = Infinity;
      points.forEach((p) => {
        const d = Math.abs(p.x - targetX);
        if (d < bestDist) { bestDist = d; best = p; }
      });
      return best.y;  // SVG y (lower = higher rate)
    }

    // Compare SVG y values: prediction vs real
    // Lower SVG y = higher rate = prediction overestimates
    const diffs = checkXs.map((x, i) => {
      const predY = yAtX(predPoints, x);
      const realY = yAtX(realPts, x);
      return realY - predY;  // positive = real is lower SVG y = real is higher rate
    });

    const earlyDiff = (diffs[0] + diffs[1]) / 2;   // years 3–8
    const midDiff   = (diffs[1] + diffs[2]) / 2;   // years 8–13
    const lateDiff  = (diffs[2] + diffs[3] + diffs[4]) / 3; // years 13–23

    const threshold = 20; // SVG units = ~30% of y range / 5 ticks

    // Positive diff means real > pred (pred underestimated)
    // Negative diff means real < pred (pred overestimated)

    const totalAbsDiff =
      diffs.reduce((sum, d) => sum + Math.abs(d), 0) / diffs.length;

    if (totalAbsDiff < threshold) {
      return `Your prediction tracked the real curve within a tight margin. ` +
        `That's unusual. Most practitioners draw their own wishful version — ` +
        `you drew something closer to the actual data.`;
    }

    if (earlyDiff < -threshold && midDiff < -threshold) {
      return `You predicted steeper early gains than practitioners report. ` +
        `The real curve rises more slowly through years 3–8. ` +
        `The leap you drew happens — but it comes later, ` +
        `and it requires the kind of positioning most practitioners skip.`;
    }

    if (earlyDiff > threshold && midDiff > threshold) {
      return `You drew a flatter curve than the data shows. ` +
        `Mid-career — years 8 through 14 — shows larger rate gains ` +
        `than most practitioners expect or plan for. ` +
        `That window does not stay open indefinitely.`;
    }

    if (lateDiff < -threshold && (earlyDiff > -threshold || midDiff > -threshold)) {
      return `Your prediction steepened past year 15. ` +
        `The real data shows a plateau — ` +
        `ceiling effects, market saturation, or a deliberate choice ` +
        `to stop raising. Late-career rate growth is not automatic.`;
    }

    // Default: mixed
    return `Your prediction diverged from the data in both directions ` +
      `across different career stages. The real curve is less linear ` +
      `than most people draw it — steeper in the middle, ` +
      `slower at the start and end.`;
  }

  // ── SCREENS ───────────────────────────────────────────────────────────────
  function showScreen(id) {
    document.querySelectorAll('.screen').forEach((s) => {
      s.classList.add('screen--hidden');
    });
    document.getElementById(id).classList.remove('screen--hidden');
  }

  // ── PIVOT BUTTON ──────────────────────────────────────────────────────────
  function handlePivot() {
    // If Template 01 data exists in sessionStorage, jump to comparison
    const floorRate = sessionStorage.getItem('m2_floor_rate');
    if (floorRate) {
      window.location.href = '/issues/[N]/rate-floor#comparison';
    } else {
      window.location.href = '/issues/[N-1]/price-floor';
    }
  }

  // ── INIT ──────────────────────────────────────────────────────────────────
  function init() {
    // Build grids for both canvases
    buildGrid('chart-svg', 'chart-grid', 'x-labels', 'y-labels');
    buildGrid('chart-svg-reveal', 'reveal-grid',
              'reveal-x-labels', 'reveal-y-labels');

    // Entry button
    document.getElementById('btn-start-drawing')
      .addEventListener('click', () => {
        showScreen('screen-canvas');
      });

    // Drawing events
    const overlay = document.getElementById('draw-overlay');
    overlay.addEventListener('mousedown', startDraw);
    overlay.addEventListener('mousemove', continueDraw);
    overlay.addEventListener('mouseup', endDraw);
    overlay.addEventListener('mouseleave', endDraw);
    overlay.addEventListener('touchstart', startDraw, { passive: false });
    overlay.addEventListener('touchmove', continueDraw, { passive: false });
    overlay.addEventListener('touchend', endDraw);

    // Clear
    document.getElementById('btn-clear-drawing')
      .addEventListener('click', clearDrawing);

    // Confirm prediction → show reveal
    document.getElementById('btn-confirm-prediction')
      .addEventListener('click', () => {
        // Copy prediction path to reveal canvas
        const frozenPath = document.getElementById('reveal-prediction-curve');
        frozenPath.setAttribute('d', smoothPath(sampledPoints));

        showScreen('screen-reveal');

        // Short delay then animate real data in
        setTimeout(() => {
          revealDataCurve();
          const realPts = getRealDataPoints();
          buildGapFill(sampledPoints, realPts);
        }, 300);

        // Generate reading
        const reading = analyzePrediction(sampledPoints);
        document.getElementById('reading-text').textContent = reading;

        // Store prediction summary in sessionStorage for cross-template use
        sessionStorage.setItem(
          'm2_prediction_divergence',
          JSON.stringify({ analyzed: true, reading })
        );
      });

    // Pivot button
    document.getElementById('btn-pivot')
      .addEventListener('click', handlePivot);
  }

  document.addEventListener('DOMContentLoaded', init);
})();
```

---

### 8. Entry Screen Design

Full-bleed dark screen, deep violet gradient. Centered:

- Eyebrow in `--text-muted`, all-caps: `PRACTITIONER WISDOM · ISSUE [N]`
- Headline in `--text-primary`, large: three lines, each on its own line, max width 680px
- Two lines of body copy beneath in `--text-secondary`, smaller size (1.1rem): the priming questions about shape
- One button: `Draw my prediction` in `--accent-primary` background (violet fill), white text
- No chart visible yet. The blank canvas is the reveal, not the entry. Entry is all about framing the question before the reader sees the tool.

---

### 9. Newsletter-Impossible Element

The reader draws with their own hand on a live SVG canvas. The act of drawing is the mechanism of miscalibration — the reader's belief becomes a physical mark, and then the real data renders on top of it. No email can accept freehand drawing input and compare it to a data set. The gap between what the reader drew and what exists is the entire lesson. In a newsletter, you can describe the shape of the data. Here, the reader's own prior belief is in the picture.

---

### 10. Style Guide Entry

```
TEMPLATE-02 — DRAW THE CURVE BEFORE YOU SEE IT
────────────────────────────────────────────────
Slug:            template-draw-the-curve
Dimension:       Practitioner Wisdom
Emotional weather: Threshold
Interaction type: Prediction confrontation (freehand SVG draw + reveal)
NI rating:       5/5
Build complexity: Medium

Palette:
  bg             #12101e → #110e1c
  card           #1a1730 → #221e40
  prediction     #8b7ffa (violet) — reader's drawn line
  data           #f5a623 (amber) — real data curve
  gap fill       rgba(245,166,35,0.15)

Data source:
  REAL_DATA array in JS — update from issue research before publish
  Source must be cited in issue body copy

SVG chart bounds:
  viewBox 0 0 800 400
  Plot area: x 60–780, y 20–360

Screens:   entry → canvas(draw) → reveal(animate + reading)
Analysis:  5-checkpoint comparison; 4 reading variants + calibrated

Critical UX rules:
  · Drawing capture uses transparent SVG rect overlay
  · Catmull-Rom smoothing on prediction path
  · Real data animates via stroke-dashoffset (1.2s ease)
  · Gap fill renders AFTER animation completes (300ms delay)
  · Mobile: touchstart/touchmove/touchend with preventDefault
  · Confirm button disabled until ≥3 points drawn

Cross-template hook:
  Reads: sessionStorage 'm2_floor_rate' (from Template 01)
  Writes: sessionStorage 'm2_prediction_divergence'

Files:
  /assets/css/template-draw-the-curve.css
  /assets/js/template-draw-the-curve.js
  /templates/draw-the-curve/index.html
```

---
---

## TEMPLATE 03 — WHAT YOUR WEEK IS ACTUALLY COSTING YOU

---

### 1. Template Name
**What Your Week Is Actually Costing You**
*Slug:* `template-week-cost`

---

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Clarity
- **Energy archetype:** The Ledger — not a judgment, a record. Every hour has an entry. The reader discovers the account balance has been running negative in a column they never named.
- **Reader state on entry:** Low-grade awareness that "admin takes a lot of time." Not quantified.
- **Reader state on exit:** Specific dollar figure. The unnamed cost now has a number.

---

### 3. Gradient Palette Spec

```css
/* Template 03 — Clarity / The Ledger */
--gradient-bg: linear-gradient(155deg, #111820 0%, #18262f 55%, #0e1e28 100%);
--gradient-card: linear-gradient(135deg, #152030 0%, #1c2d3e 100%);
--accent-primary: #56c0e8;      /* sky blue — billable / earned */
--accent-cost: #e05c7a;         /* rose — cost / lost */
--accent-neutral: #7fb8cc;      /* soft blue — neutral hours */
--accent-confirm: #6fcf97;
--text-primary: #eef4f8;
--text-secondary: #7eabc0;
--text-muted: #3f6070;
--border-subtle: rgba(86, 192, 232, 0.1);
--border-active: rgba(86, 192, 232, 0.4);
--bar-bg: #1a2f3e;
--bar-billable: #56c0e8;
--bar-admin: #e05c7a;
--bar-other: #4a6a7a;
--glow-cost: 0 0 28px rgba(224, 92, 122, 0.2);
```

---

### 4. The Interaction — Step by Step

**Step 0 — Entry**
One question: *"How much does your admin load cost you each week — in dollars?"* A sub-line: *"Most practitioners say 'too much.' Almost none have a number."* One button: `Find my number`.

**Step 1 — Rate Input**
Single large input: `What do you charge per hour?` with a soft helper: *"If you use a package rate, divide your package fee by the hours you actually work for that client."* A `$` prefix, number input.

**Step 2 — Time Allocation**
Three slider groups, each with a real-time hour display:

- **Billable hours** — time you charge for directly
- **Administrative hours** — email, scheduling, invoicing, record-keeping
- **Other non-billable** — learning, networking, breaks, personal

A constraint: the three groups sum to a fixed total work-week input (default 40 hours, editable). If they exceed the total, the sliders auto-constrain; if they fall short, a "Remaining hours" counter shows in neutral blue.

**Step 3 — The Reactive Document**
As the reader adjusts any slider, the document below the sliders recalculates live:

```
This week you are billing [X] hours at $[rate]/hr.
That earns you $[billable-income] this week.

Your [admin] hours of administration and [other] hours of other
non-billable work cost you $[lost-income] — at your current rate,
that is money you could have earned, or time you could have stopped working.

Your effective hourly rate this week: $[effective-rate]/hr.
Your stated rate: $[stated-rate]/hr.
```

Every bracketed value is `--accent-primary` or `--accent-cost` colored text — billable numbers in sky blue, cost numbers in rose.

**Step 4 — The Bar**
A single horizontal stacked bar:
- Sky blue segment: billable hours
- Rose segment: admin hours
- Dark gray segment: other non-billable

Below the bar: one line — *"[X]% of your working time is generating revenue."*

**Step 5 — The Question**
*"If you reclaimed half your admin hours to billable work, your weekly income would change by $[delta]."* A button: `What would it take to reclaim them?` — links to an issue on delegation or systemization (not built in this template, but the hook is here).

---

### 5. The Aha Moment
The reader has called admin hours "a lot of time" for years. They have never seen it rendered as `$[X]/week`. The reactive document does not editorialize. It does arithmetic. The number — specific to their rate and their hours — is the moment. For most readers it will be between $200 and $800 per week. That is not abstract. That is a subscription they never signed up for.

---

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en" data-template="week-cost">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>What Your Week Is Actually Costing You — Meliorism2</title>
  <link rel="stylesheet" href="/assets/css/template-base.css">
  <link rel="stylesheet" href="/assets/css/template-week-cost.css">
</head>
<body class="t-week-cost">

  <!-- SCREEN 0: ENTRY -->
  <section class="screen screen--entry" id="screen-entry">
    <div class="screen__inner screen__inner--centered">
      <span class="entry__eyebrow">Living Income · Issue [N]</span>
      <h1 class="entry__headline">
        How much does your admin load<br>cost you each week — in dollars?
      </h1>
      <p class="entry__body">
        Most practitioners say "too much."<br>
        Almost none have a number.
      </p>
      <button class="btn btn--primary" id="btn-start">
        Find my number
      </button>
    </div>
  </section>

  <!-- SCREEN 1: CALCULATOR -->
  <section class="screen screen--calc screen--hidden" id="screen-calc">
    <div class="screen__inner">

      <!-- RATE INPUT -->
      <div class="input-section" id="rate-section">
        <label class="input-section__label" for="hourly-rate">
          What do you charge per hour?
        </label>
        <p class="input-section__hint">
          If you use a package rate, divide your fee by the hours
          you actually work for that client.
        </p>
        <div class="input-wrap input-wrap--large">
          <span class="input-prefix">$</span>
          <input class="input-field input-field--xl" type="number"
                 id="hourly-rate" name="hourly-rate"
                 min="1" step="5" placeholder="150">
          <span class="input-suffix">/hr</span>
        </div>
      </div>

      <!-- TOTAL HOURS CONTROL -->
      <div class="input-section input-section--inline">
        <label class="input-section__label" for="total-hours">
          Total working hours this week
        </label>
        <div class="input-wrap">
          <input class="input-field input-field--short" type="number"
                 id="total-hours" name="total-hours"
                 min="1" max="80" step="1" value="40">
          <span class="input-suffix">hrs</span>
        </div>
        <span class="remaining-label">
          Remaining: <strong id="hours-remaining">0</strong> hrs
        </span>
      </div>

      <!-- TIME SLIDERS -->
      <div class="sliders-section">

        <div class="slider-group">
          <div class="slider-group__header">
            <span class="slider-group__label">
              <span class="swatch swatch--billable"></span>
              Billable hours
            </span>
            <span class="slider-group__value" id="billable-display">
              0 hrs
            </span>
          </div>
          <input class="slider slider--billable" type="range"
                 id="billable-hours" name="billable-hours"
                 min="0" max="80" step="1" value="20">
          <p class="slider-group__hint">
            Time you charge for directly
          </p>
        </div>

        <div class="slider-group">
          <div class="slider-group__header">
            <span class="slider-group__label">
              <span class="swatch swatch--admin"></span>
              Administrative hours
            </span>
            <span class="slider-group__value" id="admin-display">
              0 hrs
            </span>
          </div>
          <input class="slider slider--admin" type="range"
                 id="admin-hours" name="admin-hours"
                 min="0" max="80" step="1" value="10">
          <p class="slider-group__hint">
            Email, scheduling, invoicing, record-keeping
          </p>
        </div>

        <div class="slider-group">
          <div class="slider-group__header">
            <span class="slider-group__label">
              <span class="swatch swatch--other"></span>
              Other non-billable
            </span>
            <span class="slider-group__value" id="other-display">
              0 hrs
            </span>
          </div>
          <input class="slider slider--other" type="range"
                 id="other-hours" name="other-hours"
                 min="0" max="80" step="1" value="10">
          <p class="slider-group__hint">
            Learning, networking, personal, breaks
          </p>
        </div>

      </div>

      <!-- STACKED BAR -->
      <div class="stacked-bar-wrap">
        <div class="stacked-bar" id="stacked-bar" role="img"
             aria-label="Time allocation bar">
          <div class="stacked-bar__segment stacked-bar__segment--billable"
               id="bar-billable"></div>
          <div class="stacked-bar__segment stacked-bar__segment--admin"
               id="bar-admin"></div>
          <div class="stacked-bar__segment stacked-bar__segment--other"
               id="bar-other"></div>
        </div>
        <p class="bar-summary" id="bar-summary">
          — % of your working time is generating revenue.
        </p>
      </div>

      <!-- REACTIVE DOCUMENT -->
      <div class="reactive-doc" id="reactive-doc">

        <div class="rdoc-line rdoc-line--primary">
          This week you are billing
          <span class="rdoc-val rdoc-val--earn" id="rdoc-billable-hrs">0</span>
          hours at
          <span class="rdoc-val rdoc-val--earn" id="rdoc-rate">$0</span>/hr.
          That earns you
          <span class="rdoc-val rdoc-val--earn rdoc-val--large"
                id="rdoc-earned">$0</span>
          this week.
        </div>

        <div class="rdoc-line rdoc-line--cost">
          Your
          <span class="rdoc-val rdoc-val--cost" id="rdoc-admin-hrs">0</span>
          hours of administration and
          <span class="rdoc-val rdoc-val--cost" id="rdoc-other-hrs">0</span>
          hours of other non-billable work cost you
          <span class="rdoc-val rdoc-val--cost rdoc-val--large"
                id="rdoc-cost">$0</span>
          — at your current rate, that is money you could have earned,
          or time you could have stopped working.
        </div>

        <div class="rdoc-line rdoc-line--rates">
          <div class="rate-compare">
            <div class="rate-compare__item">
              <span class="rate-compare__label">Effective rate</span>
              <span class="rate-compare__val rdoc-val--cost"
                    id="rdoc-effective-rate">$0/hr</span>
            </div>
            <div class="rate-compare__divider">vs.</div>
            <div class="rate-compare__item">
              <span class="rate-compare__label">Stated rate</span>
              <span class="rate-compare__val rdoc-val--earn"
                    id="rdoc-stated-rate">$0/hr</span>
            </div>
          </div>
        </div>

      </div>

      <!-- PIVOT QUESTION -->
      <div class="pivot-block" id="pivot-block">
        <p class="pivot-question" id="pivot-question">
          If you reclaimed half your admin hours to billable work,
          your weekly income would change by
          <span class="rdoc-val rdoc-val--earn" id="pivot-delta">$0</span>.
        </p>
        <button class="btn btn--ghost" id="btn-reclaim">
          What would it take to reclaim them? →
        </button>
      </div>

    </div>
  </section>

  <script src="/assets/js/template-week-cost.js"></script>
</body>
</html>
```

---

### 7. Interaction JavaScript

```javascript
// template-week-cost.js
// Template 03 — What Your Week Is Actually Costing You

(function () {
  'use strict';

  // ── STATE ─────────────────────────────────────────────────────────────────
  const state = {
    rate: 0,
    totalHours: 40,
    billable: 20,
    admin: 10,
    other: 10,
  };

  const $ = (id) => document.getElementById(id);

  function fmt(n) { return '$' + Math.round(n).toLocaleString('en-US'); }
  function fmtHr(n) { return '$' + Math.round(n).toLocaleString('en-US') + '/hr'; }

  // ── SHOW SCREEN ───────────────────────────────────────────────────────────
  function showScreen(id) {
    document.querySelectorAll('.screen').forEach((s) =>
      s.classList.add('screen--hidden')
    );
    $(id).classList.remove('screen--hidden');
  }

  // ── CONSTRAINT: sliders cannot exceed totalHours combined ─────────────────
  function constrainSliders(changed) {
    const total = state.totalHours;
    // Priority: the slider just changed keeps its value;
    // the others split the remainder proportionally.
    const others = ['billable', 'admin', 'other'].filter((k) => k !== changed);
    const changedVal = state[changed];
    const remaining = total - changedVal;

    if (remaining < 0) {
      // Clamp changed value itself
      state[changed] = total;
      others.forEach((k) => { state[k] = 0; });
    } else {
      const otherSum = others.reduce((s, k) => s + state[k], 0);
      if (otherSum > remaining) {
        // Scale others down proportionally
        others.forEach((k) => {
          state[k] = otherSum === 0
            ? 0
            : Math.floor((state[k] / otherSum) * remaining);
        });
      }
    }

    // Sync slider elements
    ['billable', 'admin', 'other'].forEach((k) => {
      $(`${k}-hours`).value = state[k];
    });
  }

  // ── UPDATE ALL DISPLAYS ───────────────────────────────────────────────────
  function update() {
    const { rate, totalHours, billable, admin, other } = state;

    const used = billable + admin + other;
    const remaining = Math.max(0, totalHours - used);

    // Slider labels
    $('billable-display').textContent = billable + ' hrs';
    $('admin-display').textContent = admin + ' hrs';
    $('other-display').textContent = other + ' hrs';
    $('hours-remaining').textContent = remaining;

    // Stacked bar
    const total = Math.max(totalHours, 1);
    $('bar-billable').style.width = (billable / total * 100) + '%';
    $('bar-admin').style.width = (admin / total * 100) + '%';
    $('bar-other').style.width = (other / total * 100) + '%';

    const billablePct = Math.round((billable / total) * 100);
    $('bar-summary').textContent =
      `${billablePct}% of your working time is generating revenue.`;

    // Calculations
    const earned = rate * billable;
    const cost = rate * (admin + other);
    const effectiveRate = totalHours > 0 ? (earned / totalHours) : 0;
    const reclaimDelta = rate * Math.floor(admin / 2);

    // Reactive document
    $('rdoc-billable-hrs').textContent = billable;
    $('rdoc-rate').textContent = fmt(rate);
    $('rdoc-earned').textContent = fmt(earned);
    $('rdoc-admin-hrs').textContent = admin;
    $('rdoc-other-hrs').textContent = other;
    $('rdoc-cost').textContent = fmt(cost);
    $('rdoc-effective-rate').textContent = fmtHr(effectiveRate);
    $('rdoc-stated-rate').textContent = fmtHr(rate);

    // Pivot
    $('pivot-delta').textContent = fmt(reclaimDelta);

    // Persist to sessionStorage for cross-template use
    sessionStorage.setItem('m2_week_cost', JSON.stringify({
      rate, billable, admin, other, cost, earned, effectiveRate
    }));
  }

  // ── INIT ──────────────────────────────────────────────────────────────────
  function init() {

    $('btn-start').addEventListener('click', () => {
      showScreen('screen-calc');
    });

    // Rate input
    $('hourly-rate').addEventListener('input', (e) => {
      state.rate = parseFloat(e.target.value) || 0;
      update();
    });

    // Total hours
    $('total-hours').addEventListener('input', (e) => {
      state.totalHours = parseInt(e.target.value, 10) || 40;
      $('billable-hours').max = state.totalHours;
      $('admin-hours').max = state.totalHours;
      $('other-hours').max = state.totalHours;
      constrainSliders('billable');
      update();
    });

    // Sliders
    ['billable', 'admin', 'other'].forEach((key) => {
      $(`${key}-hours`).addEventListener('input', (e) => {
        state[key] = parseInt(e.target.value, 10) || 0;
        constrainSliders(key);
        update();
      });
    });

    // Reclaim button — links to a delegation/systemization issue
    $('btn-reclaim').addEventListener('click', () => {
      window.location.href = '/issues/delegation-systems';
    });

    // Initial display state
    update();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
```

---

### 8. Entry Screen Design

Dark background, sky blue gradient undertone. Centered:

- Eyebrow: `LIVING INCOME · ISSUE [N]` in muted teal
- Headline: two lines, large type (clamp 2.8–5rem): `How much does your admin load / cost you each week — in dollars?`
- Body: two lines in secondary color, smaller weight: `Most practitioners say "too much."` / `Almost none have a number.`
- One button: `Find my number`
- No chart, no preview. The absence of a number on the entry screen is the point — it creates the lack that the tool fills.

---

### 9. Newsletter-Impossible Element

The reactive document — every sentence in the document recalculates every time a slider moves. The text is not static. The dollar amounts in the paragraph are live. `$312` becomes `$468` the moment the admin slider moves. The paragraph does not reload. The numbers inside it change. That is not possible in email. The letter version can show a formula. Only the interactive version shows the reader's own number inside a sentence written directly to them.

---

### 10. Style Guide Entry

```
TEMPLATE-03 — WHAT YOUR WEEK IS ACTUALLY COSTING YOU
──────────────────────────────────────────────────────
Slug:            template-week-cost
Dimension:       Living Income
Emotional weather: Clarity
Interaction type: Reactive document (sliders → live paragraph)
NI rating:       5/5
Build complexity: Low

Palette:
  bg             #111820 → #0e1e28
  card           #152030 → #1c2d3e
  billable       #56c0e8 (sky blue) — earning
  cost           #e05c7a (rose) — cost / loss

Key formula:
  earned         = rate × billable
  cost           = rate × (admin + other)
  effectiveRate  = earned / totalHours
  reclaimDelta   = rate × floor(admin / 2)

Slider constraint:
  billable + admin + other ≤ totalHours
  Changed slider keeps value; others scale proportionally

Screens:   entry → calc (single screen, all live)

Critical UX rules:
  · Reactive document updates on every input event, no debounce
  · Color-coded inline values: sky blue = earn, rose = cost
  · Bar updates simultaneously with document
  · Slider max dynamically tied to totalHours input
  · Remaining hours shown as positive incentive, not error

Cross-template hook:
  Writes: sessionStorage 'm2_week_cost'

Files:
  /assets/css/template-week-cost.css
  /assets/js/template-week-cost.js
  /templates/week-cost/index.html
```

---
---

## TEMPLATE 04 — THE CASCADE

---

### 1. Template Name
**The Cascade**
*Slug:* `template-cascade`

---

### 2. Emotional Weather and Energy Archetype
- **Emotional weather:** Clarity
- **Energy archetype:** The Navigator — the reader does not read a map, they choose a route. Every choice narrows the territory. The destination is theirs because they walked to it.
- **Reader state on entry:** Mild overwhelm. The principle has multiple applications and the reader is not sure which part applies to them.
- **Reader state on exit:** Specific traction. One insight that matches their situation, not a list of possibilities.

---

### 3. Gradient Palette Spec

```css
/* Template 04 — Clarity / The Navigator */
--gradient-bg: linear-gradient(158deg, #0d1f18 0%, #172b22 55%, #0b1c14 100%);
--gradient-card: linear-gradient(135deg, #122018 0%, #1b2e22 100%);
--accent-primary: #52d68a;      /* forest green — active choice / selected path */
--accent-secondary: #a8e6c2;    /* pale green — available options */
--accent-path: #3bb87a;         /* darker green — confirmed path line */
--accent-inactive: #2a4036;     /* very dark green — unselected / faded */
--text-primary: #e8f5ef;
--text-secondary: #7db898;
--text-muted: #355045;
--border-subtle: rgba(82, 214, 138, 0.1);
--border-active: rgba(82, 214, 138, 0.45);
--choice-bg: #142219;
--choice-bg-hover: #1e3328;
--choice-bg-selected: #1f3d2b;
--choice-border-selected: #52d68a;
--path-line: rgba(82, 214, 138, 0.3);
--glow-path: 0 0 20px rgba(82, 214, 138, 0.15);
```

---

### 4. The Interaction — Step by Step

**Step 0 — Entry**
The issue topic is stated as a question. Example (adaptable to any principle): *"You know what you need to charge. Something is making it hard to ask for it. What's closest to what's true right now?"* One button: `Map my situation`.

**Step 1 — Branch A: The First Choice**
Three options appear as large tap-cards (not small radio buttons — full-width cards, readable at a glance):

```
A1 · I don't believe my rate is justified
A2 · I believe it, but I can't say it without hesitation
A3 · I say it, but I discount when pushed
```

The reader taps one. It highlights in forest green. The others fade to `--accent-inactive`. A brief pause (300ms), then the next layer cascades in below.

**Step 2 — Branch B: Second Choice (contingent on A)**

If A1 selected:
```
B1a · I compare myself to practitioners who charge more and feel behind
B1b · I haven't put together a clear case for my rate — not even for myself
```

If A2 selected:
```
B2a · The hesitation is in my body — voice, posture, eye contact
B2b · The hesitation is in the framing — I hedge or over-explain
```

If A3 selected:
```
B3a · I discount to close — I'd rather have the client than hold the rate
B3b · I discount when I sense disapproval — even before they ask
```

**Step 3 — Branch C: Third Choice (contingent on B, optional)**

Not all paths require a third branch. A3 → B3a, for example, is specific enough to land directly. The cascade ends when the insight is specific. Forcing a third branch when it is not needed dilutes the effect.

Example of a path that takes a third branch — A2 → B2b:
```
C1 · The over-explanation starts before they react — I preempt their objection
C2 · The over-explanation starts after a pause — I fill silence
```

**Step 4 — The Insight**
The terminal node renders a full paragraph — the insight for this specific path. It is not generic advice about pricing. It is a named, specific observation about what is happening at this exact intersection.

Example insight for A2 → B2b → C2:
```
Silence tolerance.

You are filling a pause that has not yet meant anything. The client's
pause after hearing your rate is processing time — not rejection.
You are answering an objection they have not made.

The work here is not on your rate. It is on your relationship to
the 4-second pause. That is the specific thing.
```

**Step 5 — The Path Display**
A visual breadcrumb of the three choices appears above the insight — `A2 → B2b → C2` — so the reader can see the exact route they took. A soft `Start over` button beneath the insight resets the cascade.

**Step 6 — Cross-Template Awareness**
If `sessionStorage` contains Template 01 data (their floor rate), and the path ends at an insight about rate hesitation, append: *"Your calculated floor is $[X]/hr. What you are hesitating to say has a specific number."*

---

### 5. The Aha Moment
The reader did not receive a general principle about rate hesitation. They received a paragraph that describes what is happening specifically to them, at a specific intersection — because they chose the route. The insight cannot be received as generic because the reader's own choices generated it. The navigation is the personalization.

---

### 6. Complete HTML Structure

```html
<!DOCTYPE html>
<html lang="en" data-template="cascade">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Cascade — Meliorism2</title>
  <link rel="stylesheet" href="/assets/css/template-base.css">
  <link rel="stylesheet" href="/assets/css/template-cascade.css">
</head>
<body class="t-cascade">

  <!-- SCREEN 0: ENTRY -->
  <section class="screen screen--entry" id="screen-entry">
    <div class="screen__inner screen__inner--centered">
      <span class="entry__eyebrow">Practitioner Wisdom · Issue [N]</span>
      <h1 class="entry__headline">
        You know what you need to charge.<br>
        Something is making it hard to ask for it.<br>
        What's closest to what's true right now?
      </h1>
      <button class="btn btn--primary" id="btn-start-cascade">
        Map my situation
      </button>
    </div>
  </section>

  <!-- SCREEN 1: CASCADE -->
  <section class="screen screen--cascade screen--hidden" id="screen-cascade">
    <div class="screen__inner screen__inner--cascade">

      <!-- BREADCRUMB PATH -->
      <nav class="cascade-path" id="cascade-path" aria-label="Your path">
        <!-- Populated by JS as choices are made -->
      </nav>

      <!-- CHOICE LAYERS — stacked, each slides in below the previous -->
      <div class="cascade-layers" id="cascade-layers">
        <!-- Layer 0 is injected by JS on start -->
      </div>

      <!-- INSIGHT BLOCK — hidden until terminal node -->
      <div class="insight-block insight-block--hidden" id="insight-block">

        <div class="insight-path-label" id="insight-path-label">
          <!-- e.g. "A2 → B2b → C2" -->
        </div>

        <div class="insight-content" id="insight-content">
          <!-- Populated by JS -->
        </div>

        <div class="insight-floor-hook insight-floor-hook--hidden"
             id="insight-floor-hook">
          <!-- Populated by JS if floor rate data exists -->
        </div>

        <div class="insight-actions">
          <button class="btn btn--ghost" id="btn-reset-cascade">
            Start over
          </button>
          <button class="btn btn--primary" id="btn-share-insight"
                  onclick="window.print()">
            Save this
          </button>
        </div>

      </div>

    </div>
  </section>

  <script src="/assets/js/template-cascade.js"></script>
</body>
</html>
```

---

### 7. Interaction JavaScript

```javascript
// template-cascade.js
// Template 04 — The Cascade

(function () {
  'use strict';

  // ── CASCADE DATA STRUCTURE ────────────────────────────────────────────────
  // Each node: { id, label, prompt, options: [{id, label, next}] | null }
  // null options = terminal node → show insight

  const CASCADE = {
    root: {
      id: 'root',
      prompt: null,  // No prompt at root — first layer is the first question
      options: ['A1', 'A2', 'A3']
    },

    // ── LAYER A ──────────────────────────────────────────────────────────────
    A1: {
      id: 'A1',
      label: "I don't believe my rate is justified",
      options: ['B1a', 'B1b']
    },
    A2: {
      id: 'A2',
      label: "I believe it, but I can't say it without hesitation",
      options: ['B2a', 'B2b']
    },
    A3: {
      id: 'A3',
      label: "I say it, but I discount when pushed",
      options: ['B3a', 'B3b']
    },

    // ── LAYER B ──────────────────────────────────────────────────────────────
    B1a: {
      id: 'B1a',
      label: "I compare myself to practitioners who charge more and feel behind",
      options: null  // terminal
    },
    B1b: {
      id: 'B1b',
      label: "I haven't put together a clear case for my rate — not even for myself",
      options: null  // terminal
    },
    B2a: {
      id: 'B2a',
      label: "The hesitation is in my body — voice, posture, eye contact",
      options: null  // terminal
    },
    B2b: {
      id: 'B2b',
      label: "The hesitation is in the framing — I hedge or over-explain",
      options: ['C2a', 'C2b']  // this branch takes a third step
    },
    B3a: {
      id: 'B3a',
      label: "I discount to close — I'd rather have the client than hold the rate",
      options: null  // terminal
    },
    B3b: {
      id: 'B3b',
      label: "I discount when I sense disapproval — even before they ask",
      options: null  // terminal
    },

    // ── LAYER C (only B2b path) ───────────────────────────────────────────
    C2a: {
      id: 'C2a',
      label: "The over-explanation starts before they react — I preempt their objection",
      options: null
    },
    C2b: {
      id: 'C2b',
      label: "The over-explanation starts after a pause — I fill silence",
      options: null
    },
  };

  // ── INSIGHT COPY ──────────────────────────────────────────────────────────
  // Keyed by terminal node ID. Written as specific, named observations.

  const INSIGHTS = {
    B1a: {
      title: 'Comparison drift.',
      body: `You are measuring your rate against practitioners whose context
you don't fully know — their client base, their positioning, how long it took
them to get there, and what they gave up to do it.

The comparison is not neutral data. It is a story you are using as evidence
against yourself.

Your rate is not a statement about where you rank. It is a reflection of
what the work requires to sustain. Those are different questions.
Return to the second one.`
    },

    B1b: {
      title: 'The unbuilt case.',
      body: `You have not yet assembled the argument for your own rate.
Not for a client — for yourself.

That argument exists. It is built from: the transformation you have
produced, the preparation that work required, the results you can point to,
and the alternatives your clients would face without you.

The hesitation is not about the number. It is about the absence of a brief
you have not yet written. Write the brief. One page. Once.
After that, the number stops being a question.`
    },

    B2a: {
      title: 'The body knows first.',
      body: `Your rate is not the problem. Your nervous system is running
a threat response in what should be a neutral transaction.

The hesitation in your voice, the shift in your posture — these are
not signs of dishonesty. They are signals that part of you is expecting
a consequence for asking.

The work here is somatic rehearsal, not mindset. Say the number out loud,
alone, until it stops activating the response. The number is correct.
The body needs repetition to believe it.`
    },

    B2b: {
      // This node routes to C — should not render as terminal
      // Safety fallback only
      title: 'Framing hesitation.',
      body: `The words around your rate are doing work you haven't assigned them.
Choose the one that fits — it will lead to something more specific.`
    },

    B3a: {
      title: 'The closing discount.',
      body: `You are treating a closed deal at a lower rate as better
than a lost deal at the right rate.

Run the actual arithmetic. A client at 70% of your rate who stays six months
earns you less than a client at full rate who stays three. The discount
is not a business decision — it is an anxiety management strategy that
looks like a business decision.

Your rate is not a take-it-or-leave-it stance against the client.
It is the condition under which you can do the work at full capacity.
Discounted rates produce discounted practitioners.`
    },

    B3b: {
      title: 'The preemptive discount.',
      body: `You are discounting in response to a signal — a tone, a pause,
a raised eyebrow — that you have interpreted as rejection.

That interpretation may be wrong. And even if it is right, you have now
moved without being asked. The client did not negotiate. You negotiated
against yourself.

The practice here is waiting for a sentence. Not a look. Not a pause.
A sentence. Until they say a sentence, your rate stands.`
    },

    C2a: {
      title: 'Preemptive objection handling.',
      body: `You are answering a question the client has not asked.

The justification you offer before their reaction is information to them:
it signals that you expect to be challenged, which makes a challenge
more likely.

State the rate. Stop. Let them respond. The explanation, if it is ever
needed, lands with more weight when it comes after a real question —
not before an imagined one.

Silence after stating a price is not awkward. It is professional.`
    },

    C2b: {
      title: 'Silence tolerance.',
      body: `You are filling a pause that has not yet meant anything.

The client's silence after hearing your rate is processing time — not rejection.
You are answering an objection they have not made.

The work here is not on your rate. It is on your relationship to
the 4-second pause.

Count to four. Every time. The client who was going to say yes
is still going to say yes after four seconds. The client who was going
to object will say so — and then you will have a real conversation
instead of a preemptive apology.

That is the specific thing.`
    },
  };

  // ── STATE ─────────────────────────────────────────────────────────────────
  let chosenPath = [];  // array of chosen node IDs, e.g. ['A2', 'B2b', 'C2b']

  const $ = (id) => document.getElementById(id);

  // ── SHOW SCREEN ───────────────────────────────────────────────────────────
  function showScreen(id) {
    document.querySelectorAll('.screen').forEach((s) =>
      s.classList.add('screen--hidden')
    );
    $(id).classList.remove('screen--hidden');
  }

  // ── BUILD BREADCRUMB ──────────────────────────────────────────────────────
  function updateBreadcrumb() {
    const nav = $('cascade-path');
    nav.innerHTML = '';
    chosenPath.forEach((id, i) => {
      const span = document.createElement('span');
      span.className = 'crumb';
      span.textContent = id;
      nav.appendChild(span);
      if (i < chosenPath.length - 1) {
        const arrow = document.createElement('span');
        arrow.className = 'crumb-arrow';
        arrow.textContent = '→';
        nav.appendChild(arrow);
      }
    });
  }

  // ── BUILD A CHOICE LAYER ──────────────────────────────────────────────────
  function buildLayer(nodeIds, layerIndex) {
    const layer = document.createElement('div');
    layer.className = 'cascade-layer';
    layer.dataset.layer = layerIndex;

    const layerLabel = document.createElement('p');
    layerLabel.className = 'cascade-layer__prompt';
    layerLabel.textContent = getLayerPrompt(layerIndex);
    layer.appendChild(layerLabel);

    const cardGroup = document.createElement('div');
    cardGroup.className = 'cascade-card-group';

    nodeIds.forEach((nodeId) => {
      const node = CASCADE[nodeId];
      const card = document.createElement('button');
      card.className = 'cascade-card';
      card.dataset.nodeId = nodeId;
      card.setAttribute('type', 'button');
      card.innerHTML = `
        <span class="cascade-card__id">${nodeId}</span>
        <span class="cascade-card__label">${node.label}</span>
      `;
      card.addEventListener('click', () => handleChoice(nodeId, layerIndex));
      cardGroup.appendChild(card);
    });

    layer.appendChild(cardGroup);
    return layer;
  }

  function getLayerPrompt(index) {
    const prompts = [
      'What is closest to what is true right now?',
      'Which of these fits more precisely?',
      'Which version of this is yours?',
    ];
    return prompts[index] || 'Which is closer?';
  }

  // ── HANDLE A CHOICE ───────────────────────────────────────────────────────
  function handleChoice(nodeId, layerIndex) {
    const node = CASCADE[nodeId];

    // Update path
    chosenPath = chosenPath.slice(0, layerIndex);
    chosenPath.push(nodeId);
    updateBreadcrumb();

    // Mark cards in this layer
    const layer = document.querySelector(
      `.cascade-layer[data-layer="${layerIndex}"]`
    );
    layer.querySelectorAll('.cascade-card').forEach((card) => {
      card.classList.remove('cascade-card--selected', 'cascade-card--faded');
      if (card.dataset.nodeId === nodeId) {
        card.classList.add('cascade-card--selected');
      } else {
        card.classList.add('cascade-card--faded');
      }
    });

    // Disable further interaction on this layer
    layer.querySelectorAll('.cascade-card').forEach((c) =>
      c.setAttribute('disabled', '')
    );

    // Remove any layers below this one (user changed mind / branched)
    const layersContainer = $('cascade-layers');
    const existingLayers = layersContainer.querySelectorAll('.cascade-layer');
    existingLayers.forEach((l) => {
      if (parseInt(l.dataset.layer, 10) > layerIndex) l.remove();
    });

    // Hide insight block while navigating
    $('insight-block').classList.add('insight-block--hidden');

    // Short animation pause then cascade next layer or show insight
    setTimeout(() => {
      if (node.options && node.options.length > 0) {
        // Build and append next layer
        const nextLayer = buildLayer(node.options, layerIndex + 1);
        nextLayer.classList.add('cascade-layer--entering');
        layersContainer.appendChild(nextLayer);
        nextLayer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        setTimeout(() => nextLayer.classList.remove('cascade-layer--entering'), 50);
      } else {
        // Terminal — show insight
        showInsight(nodeId);
      }
    }, 320);
  }

  // ── SHOW INSIGHT ──────────────────────────────────────────────────────────
  function showInsight(terminalId) {
    const insight = INSIGHTS[terminalId];
    if (!insight) return;

    $('insight-path-label').textContent = chosenPath.join(' → ');

    $('insight-content').innerHTML = `
      <h2 class="insight-title">${insight.title}</h2>
      <p class="insight-body">${insight.body.replace(/\n\n/g, '</p><p class="insight-body">')}</p>
    `;

    // Cross-template hook: floor rate
    const floorData = sessionStorage.getItem('m2_floor_rate');
    const hookEl = $('insight-floor-hook');
    if (floorData && parseFloat(floorData) > 0) {
      hookEl.classList.remove('insight-floor-hook--hidden');
      hookEl.textContent =
        `Your calculated floor is $${parseFloat(floorData).toFixed(0)}/hr. ` +
        `What you are hesitating to say has a specific number.`;
    } else {
      hookEl.classList.add('insight-floor-hook--hidden');
    }

    const insightBlock = $('insight-block');
    insightBlock.classList.remove('insight-block--hidden');
    insightBlock.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // ── RESET ─────────────────────────────────────────────────────────────────
  function resetCascade() {
    chosenPath = [];
    updateBreadcrumb();
    $('cascade-layers').innerHTML = '';
    $('insight-block').classList.add('insight-block--hidden');

    // Re-inject layer 0
    const firstLayer = buildLayer(['A1', 'A2', 'A3'], 0);
    $('cascade-layers').appendChild(firstLayer);
  }

  // ── INIT ──────────────────────────────────────────────────────────────────
  function init() {
    $('btn-start-cascade').addEventListener('click', () => {
      showScreen('screen-cascade');
      resetCascade();
    });

    $('btn-reset-cascade').addEventListener('click', resetCascade);
  }

  document.addEventListener('DOMContentLoaded', init);
})();
```

---

### 8. Entry Screen Design

Deep forest green gradient, dark and saturated. Centered:

- Eyebrow: `PRACTITIONER WISDOM · ISSUE [N]` in muted green
- Headline: three lines, each on its own line. Medium weight, large (clamp 2.4–4.4rem). The three lines build a logical sequence — each line answers a condition of the previous.
- One button: `Map my situation` — forest green fill, white text
- No preview of the cards. The cards appear only after the button is pressed. The entry is not a menu — it is a question.

---

### 9. Newsletter-Impossible Element

The conditional logic of the cascade. A newsletter can ask a question. It cannot route the reader down one of six paths based on their answer, deliver a unique paragraph at the terminal node of their specific path, and then hook that paragraph to personal data from a prior interactive tool. The insight the reader receives exists nowhere in the issue as a readable section — it was generated by their own choices. The branching is not editorial variation. It is a machine that the reader drives.

---

### 10. Style Guide Entry

```
TEMPLATE-04 — THE CASCADE
──────────────────────────
Slug:            template-cascade
Dimension:       Practitioner Wisdom (adaptable to any dimension)
Emotional weather: Clarity
Interaction type: Branching choice (sequential tap-cards → terminal insight)
NI rating:       4/5
Build complexity: Low

Palette:
  bg             #0d1f18 → #0b1c14
  card           #122018 → #1b2e22
  active         #52d68a (forest green)
  inactive       #2a4036 (faded)

Data structure:
  CASCADE object — tree of nodes; null options = terminal
  INSIGHTS object — keyed by terminal node ID
  Add/edit nodes and insights per issue topic — no JS changes needed

Screens:   entry → cascade (single screen, layers append dynamically)

Critical UX rules:
  · Cards are full-width tap targets — minimum 64px height
  · Selected card highlighted; others faded and disabled
  · New layers append below (do not replace), user sees full path
  · Insight scrolls into view after terminal node
  · Reset clears all layers and re-injects layer 0
  · Third layer is optional — only used when the B node warrants it

Cross-template hook:
  Reads: sessionStorage 'm2_floor_rate' (appended to relevant insights)
  Designed to chain with Templates 01 and 03

Content update protocol:
  Per-issue: update CASCADE nodes, INSIGHTS copy, entry headline
  JS architecture unchanged between issues
  Insight copy is the editorial labor — allow 2–3 hours per issue

Files:
  /assets/css/template-cascade.css
  /assets/js/template-cascade.js
  /templates/cascade/index.html
```

---

## CROSS-TEMPLATE INTEGRATION MAP

```
Template 01 (Price Floor)
  └─ writes: sessionStorage 'm2_floor_rate'
  └─ reads: nothing

Template 02 (Draw the Curve)
  └─ writes: sessionStorage 'm2_prediction_divergence'
  └─ reads: 'm2_floor_rate' → pivot button routes to T01 if no data

Template 03 (Week Cost)
  └─ writes: sessionStorage 'm2_week_cost'
  └─ reads: nothing (standalone)

Template 04 (The Cascade)
  └─ writes: nothing
  └─ reads: 'm2_floor_rate' → appends floor number to relevant insights
```

All four templates share:
- `/assets/css/template-base.css` — reset, typography scale, button system, screen management utilities
- `/assets/js/template-utils.js` — formatMoney, showScreen, sessionStorage helpers
- Font stack: `'Inter', system-ui, sans-serif` — no external font dependency for performance
- Print stylesheet: all four templates include `@media print` rules for clean PDF output via `window.print()`