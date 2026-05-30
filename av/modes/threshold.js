// av/modes/threshold.js — placeholder for "the moment before a belief changes"
export function draw(ctx, t, w, h) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, "#1a1624");
    g.addColorStop(1, "#1a1420");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
}
export function drawStatic(ctx, w, h) { draw(ctx, 0, w, h); }
