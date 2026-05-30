// av/modes/fog.js — placeholder for "uncertainty worth sitting with"
export function draw(ctx, t, w, h) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, "#141824");
    g.addColorStop(1, "#141620");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
}
export function drawStatic(ctx, w, h) { draw(ctx, 0, w, h); }
