// av/engine.js — Meliorism2 Immersive AV Engine
// Reads <!-- meliorism2:av-* --> metadata from the page, mounts a canvas
// behind the content, dispatches to a weather-keyed visual mode, and
// provides off-by-default audio.
//
// Design principles:
//   1. Neuro-spicy friendly — reduced-motion respected, audio off by default,
//      no sudden bright movement, no autoplay, no strobing.
//   2. Static-DOM-first — engine NEVER alters article prose. It paints behind.
//      AI crawlers and readers without JS see the full article.
//   3. Performance budget — < 5ms per frame, < 30KB total, pauses on hidden tab.
//   4. Earned advance — controls are visible, keyboard-reachable, ARIA-labeled.
//
// Source of laws: _engine/DESIGN-ENGINE.md (weather gradients, 4 layers, laws)

const META_RE = /<!--\s*meliorism2:([\w-]+):\s*([^>]+?)\s*-->/g;
const DEFAULTS = {
    "av-mode":      "friction",
    "av-intensity": "subtle",   // subtle | medium | strong
    "av-audio":     "off",      // off | drone (default off; user must enable)
    "av-palette":   "amber",
};

function readMeta() {
    const out = { ...DEFAULTS };
    const html = document.documentElement.outerHTML;
    let m;
    while ((m = META_RE.exec(html)) !== null) {
        if (m[1] in DEFAULTS || m[1].startsWith("av-")) out[m[1]] = m[2];
    }
    return out;
}

function prefersReducedMotion() {
    return window.matchMedia?.("(prefers-reduced-motion: reduce)").matches ?? false;
}

function mountCanvas() {
    // Clear html/body backgrounds so a z-index:-1 canvas can show through.
    // The engine owns the page background. Issue stylesheets that set a body
    // color get overridden here — by design — so the weather is what's seen.
    document.documentElement.style.background = "transparent";
    document.body.style.background = "transparent";
    const c = document.createElement("canvas");
    c.id = "av-canvas";
    c.setAttribute("aria-hidden", "true");
    c.style.cssText =
        "position:fixed;inset:0;width:100%;height:100%;z-index:-1;" +
        "pointer-events:none;display:block;";
    document.body.prepend(c);
    return c;
}

function mountControls(state) {
    const wrap = document.createElement("div");
    wrap.id = "av-controls";
    wrap.style.cssText =
        "position:fixed;right:14px;bottom:14px;z-index:9000;" +
        "display:flex;gap:8px;font:0.8rem/1 system-ui,sans-serif;";
    wrap.innerHTML = `
        <button id="av-toggle-motion" aria-label="Pause background motion"
                style="background:rgba(0,0,0,0.55);color:#f0e9d8;border:1px solid rgba(255,255,255,0.18);
                       border-radius:999px;padding:8px 12px;cursor:pointer;backdrop-filter:blur(6px);"
                >motion · on</button>
        <button id="av-toggle-audio" aria-label="Enable ambient audio"
                style="background:rgba(0,0,0,0.55);color:#f0e9d8;border:1px solid rgba(255,255,255,0.18);
                       border-radius:999px;padding:8px 12px;cursor:pointer;backdrop-filter:blur(6px);"
                >audio · off</button>
    `;
    document.body.appendChild(wrap);
    return wrap;
}

function setupCanvasResize(canvas) {
    function resize() {
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width  = Math.floor(window.innerWidth  * dpr);
        canvas.height = Math.floor(window.innerHeight * dpr);
        const ctx = canvas.getContext("2d");
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    window.addEventListener("resize", resize, { passive: true });
    resize();
}

async function loadMode(name) {
    try {
        const mod = await import(`./modes/${name}.js`);
        return mod;
    } catch (e) {
        console.warn(`[av] mode "${name}" not found — falling back to friction`);
        return await import(`./modes/friction.js`);
    }
}

let audioCtx = null;
let audioNodes = null;

function audioStart(weather) {
    if (audioCtx) return;
    try {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        // Single low-pass-filtered drone — frequency keyed to weather
        const FREQ = {
            clarity: 110, surge: 73, threshold: 65, solidarity: 98,
            friction: 82, fog: 87, delight: 130
        };
        const osc = audioCtx.createOscillator();
        osc.type = "sine";
        osc.frequency.value = FREQ[weather] ?? 82;
        const detune = audioCtx.createOscillator();
        detune.type = "sine";
        detune.frequency.value = (FREQ[weather] ?? 82) * 1.005;
        const filter = audioCtx.createBiquadFilter();
        filter.type = "lowpass";
        filter.frequency.value = 320;
        const gain = audioCtx.createGain();
        gain.gain.value = 0;
        osc.connect(filter); detune.connect(filter);
        filter.connect(gain).connect(audioCtx.destination);
        osc.start(); detune.start();
        // Slow fade-in (3s) — never sudden
        gain.gain.linearRampToValueAtTime(0.08, audioCtx.currentTime + 3);
        audioNodes = { osc, detune, filter, gain };
    } catch (e) {
        console.warn("[av] audio init failed:", e);
    }
}

function audioStop() {
    if (!audioCtx || !audioNodes) return;
    try {
        const t = audioCtx.currentTime;
        audioNodes.gain.gain.cancelScheduledValues(t);
        audioNodes.gain.gain.linearRampToValueAtTime(0, t + 1);
        setTimeout(() => {
            audioNodes.osc.stop(); audioNodes.detune.stop();
            audioCtx.close(); audioCtx = null; audioNodes = null;
        }, 1100);
    } catch (e) { /* ignore */ }
}

export async function boot() {
    const meta = readMeta();
    const reduced = prefersReducedMotion();
    const canvas = mountCanvas();
    setupCanvasResize(canvas);
    const ctx = canvas.getContext("2d");
    const controls = mountControls(meta);
    const mode = await loadMode(meta["av-mode"]);

    const state = {
        running: !reduced,           // honor reduced-motion at boot
        audio: false,
        reduced,
        meta,
        startedAt: performance.now(),
    };

    // If reduced motion, paint one static frame and stop
    if (reduced) {
        mode.drawStatic?.(ctx, canvas.width, canvas.height, meta);
        controls.querySelector("#av-toggle-motion").textContent = "motion · off (reduced)";
    }

    function tick(now) {
        if (!state.running) return;
        const t = (now - state.startedAt) / 1000;
        mode.draw(ctx, t, window.innerWidth, window.innerHeight, meta);
        requestAnimationFrame(tick);
    }
    if (state.running) requestAnimationFrame(tick);

    // Page Visibility — pause when tab hidden
    document.addEventListener("visibilitychange", () => {
        if (document.hidden && state.running) {
            state.running = false;
        } else if (!document.hidden && !document.querySelector("#av-toggle-motion").textContent.includes("off") && !reduced) {
            state.running = true;
            state.startedAt = performance.now() - (state.lastT || 0) * 1000;
            requestAnimationFrame(tick);
        }
    });

    // Motion toggle
    controls.querySelector("#av-toggle-motion").addEventListener("click", (e) => {
        const btn = e.currentTarget;
        if (state.running) {
            state.running = false;
            btn.textContent = "motion · paused";
            mode.drawStatic?.(ctx, canvas.width, canvas.height, meta);
        } else {
            state.running = true;
            state.startedAt = performance.now();
            btn.textContent = "motion · on";
            requestAnimationFrame(tick);
        }
    });

    // Audio toggle
    controls.querySelector("#av-toggle-audio").addEventListener("click", (e) => {
        const btn = e.currentTarget;
        if (!state.audio) {
            audioStart(meta["av-mode"]);
            state.audio = true;
            btn.textContent = "audio · on";
            btn.setAttribute("aria-label", "Mute ambient audio");
        } else {
            audioStop();
            state.audio = false;
            btn.textContent = "audio · off";
            btn.setAttribute("aria-label", "Enable ambient audio");
        }
    });
}

// Auto-boot when DOM ready
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
} else {
    boot();
}
