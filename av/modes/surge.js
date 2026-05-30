// av/modes/surge.js — placeholder for "something about to happen"
export function draw(ctx, t, w, h) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, "#1a0f2e");
    g.addColorStop(1, "#1a0838");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
}
export function drawStatic(ctx, w, h) { draw(ctx, 0, w, h); }
