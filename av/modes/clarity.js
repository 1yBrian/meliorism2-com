// av/modes/clarity.js — placeholder
// Weather: ☀️ Clarity — "morning intelligence briefing"
// Full implementation pending. Current fallback: light blue-green wash, no motion.
export function draw(ctx, t, w, h) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, "#0f1923");
    g.addColorStop(1, "#0d4a3a");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = "rgba(79, 195, 161, 0.06)";
    const cx = w * (0.5 + Math.sin(t / 73) * 0.06);
    const cy = h * (0.40 + Math.cos(t / 89) * 0.04);
    ctx.beginPath();
    ctx.arc(cx, cy, Math.min(w, h) * 0.42, 0, Math.PI * 2);
    ctx.fill();
}
export function drawStatic(ctx, w, h) { draw(ctx, 0, w, h); }
