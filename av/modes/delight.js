// av/modes/delight.js — placeholder for "earned reward, beautiful for its own sake"
export function draw(ctx, t, w, h) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, "#1a1208");
    g.addColorStop(1, "#1a1005");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
}
export function drawStatic(ctx, w, h) { draw(ctx, 0, w, h); }
