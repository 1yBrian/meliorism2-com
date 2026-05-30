// av/modes/friction.js
// Weather: 🌧️ Friction — "pressure about to release"
// Palette: amber accent on warm-dark base (#1a1410 → #1a1208)
//
// Visual grammar:
//   - Base: vertical gradient, warm-dark to slightly cooler-dark
//   - 4 slow-drifting heat blobs (radial gradients), low opacity, ~30s orbit period
//   - Occasional pressure pulse — a slow brightening of one blob over 2.4s,
//     repeating every 32–48s (never sudden, never bright enough to startle)
//   - No strobing. No high-contrast flashes. Designed for ADHD nervous systems.
//
// Performance: 4 radial gradients + 1 base = 5 draw calls. ~1ms per frame on modern hardware.

const BLOBS = [
    { hue: 32,  sat: 78,  ax: 0.22, ay: 0.30, rx: 0.18, ry: 0.22, periodA: 47, periodB: 38, baseR: 0.42 },
    { hue: 22,  sat: 70,  ax: 0.72, ay: 0.20, rx: 0.16, ry: 0.20, periodA: 53, periodB: 41, baseR: 0.36 },
    { hue: 38,  sat: 82,  ax: 0.40, ay: 0.72, rx: 0.20, ry: 0.18, periodA: 61, periodB: 49, baseR: 0.46 },
    { hue: 18,  sat: 65,  ax: 0.85, ay: 0.78, rx: 0.14, ry: 0.16, periodA: 43, periodB: 37, baseR: 0.32 },
];

const PULSE_PERIOD = 38; // seconds between pulse starts (per-blob jittered)
const PULSE_DURATION = 2.4;

function basePaint(ctx, w, h) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0,    "#1a1410");
    g.addColorStop(0.55, "#15100a");
    g.addColorStop(1,    "#1a1208");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
}

function blobAt(ctx, w, h, blob, t) {
    // Slow orbital drift via sin/cos with distinct A/B periods (Lissajous)
    const cx = (blob.ax + Math.sin(t / blob.periodA * Math.PI * 2) * blob.rx) * w;
    const cy = (blob.ay + Math.cos(t / blob.periodB * Math.PI * 2) * blob.ry) * h;
    const baseRadius = Math.min(w, h) * blob.baseR;

    // Pressure pulse — slow brightening (cosine ease) at jittered intervals
    const phase = (t + blob.ax * PULSE_PERIOD) % PULSE_PERIOD;
    let pulse = 0;
    if (phase < PULSE_DURATION) {
        pulse = 0.5 - 0.5 * Math.cos((phase / PULSE_DURATION) * Math.PI * 2);
    }

    const radius = baseRadius * (1 + pulse * 0.18);
    const alpha = 0.16 + pulse * 0.10;
    const innerLight = 30 + pulse * 18;

    const g = ctx.createRadialGradient(cx, cy, 0, cx, cy, radius);
    g.addColorStop(0,    `hsla(${blob.hue}, ${blob.sat}%, ${innerLight}%, ${alpha})`);
    g.addColorStop(0.55, `hsla(${blob.hue}, ${blob.sat}%, 22%, ${alpha * 0.55})`);
    g.addColorStop(1,    "hsla(0, 0%, 0%, 0)");
    ctx.fillStyle = g;
    ctx.globalCompositeOperation = "screen";
    ctx.fillRect(0, 0, w, h);
}

export function draw(ctx, t, w, h /*, meta */) {
    ctx.globalCompositeOperation = "source-over";
    basePaint(ctx, w, h);
    for (const blob of BLOBS) {
        blobAt(ctx, w, h, blob, t);
    }
    ctx.globalCompositeOperation = "source-over";
}

// For reduced-motion users — a single static frame at t=0 so the page still has atmosphere
export function drawStatic(ctx, w, h /*, meta */) {
    draw(ctx, 14.7, w, h);  // arbitrary frozen moment that looks balanced
}
