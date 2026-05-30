// av/modes/solidarity.js — placeholder for "practitioner-to-practitioner recognition"
export function draw(ctx, t, w, h) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, "#0d1a14");
    g.addColorStop(1, "#0f2218");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
}
export function drawStatic(ctx, w, h) { draw(ctx, 0, w, h); }
