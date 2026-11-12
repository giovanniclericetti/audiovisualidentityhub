// A short azure pixel trail; the native pointer remains available everywhere.
(() => {
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const finePointer = matchMedia('(any-pointer: fine)');
  const forcedColors = matchMedia('(forced-colors: active)');
  const pixels = new Map();
  const size = 7;
  const lifetime = 420;
  let canvas, context, frame = 0;
  let color = '#009fe3';
  const clear = () => {
    cancelAnimationFrame(frame);
    frame = 0;
    pixels.clear();
    if (context) context.clearRect(0, 0, innerWidth, innerHeight);
  };
  const resize = () => {
    clear();
    if (!canvas) return;
    const ratio = Math.min(devicePixelRatio || 1, 2);
    canvas.width = Math.round(innerWidth * ratio);
    canvas.height = Math.round(innerHeight * ratio);
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
  };
  const prepare = () => {
    if (canvas) return true;
    canvas = document.createElement('canvas');
    context = canvas.getContext('2d');
    if (!context) { canvas = null; return false; }
    canvas.className = 'azure-pixel-trail';
    canvas.setAttribute('aria-hidden', 'true');
    document.body.append(canvas);
    color = getComputedStyle(document.documentElement).getPropertyValue('--blue').trim() || color;
    resize();
    return true;
  };
  const paint = time => {
    context.clearRect(0, 0, innerWidth, innerHeight);
    context.fillStyle = color;
    for (const [key, pixel] of pixels) {
      const age = (time - pixel.born) / lifetime;
      if (age >= 1) { pixels.delete(key); continue; }
      context.globalAlpha = .28 * (1 - age) ** 1.5;
      context.fillRect(pixel.x, pixel.y, size, size);
    }
    context.globalAlpha = 1;
    frame = pixels.size ? requestAnimationFrame(paint) : 0;
  };
  document.addEventListener('pointermove', event => {
    if (event.pointerType !== 'mouse' || reducedMotion.matches || !finePointer.matches || forcedColors.matches) return clear();
    if (event.target.closest('input,textarea,select,[contenteditable],iframe,video')) return clear();
    if (!prepare()) return;
    const x = Math.floor(event.clientX / size) * size;
    const y = Math.floor(event.clientY / size) * size;
    const key = `${x}:${y}`;
    pixels.delete(key);
    pixels.set(key, {x, y, born:performance.now()});
    if (pixels.size > 72) pixels.delete(pixels.keys().next().value);
    if (!frame) frame = requestAnimationFrame(paint);
  }, {passive:true});
  document.documentElement.addEventListener('pointerleave', clear);
  document.addEventListener('pointerdown', event => { if (event.pointerType !== 'mouse') clear(); }, {passive:true});
  document.addEventListener('keydown', event => { if (event.key === 'Tab') clear(); });
  document.addEventListener('visibilitychange', () => { if (document.hidden) clear(); });
  window.addEventListener('blur', clear);
  window.addEventListener('scroll', clear, {passive:true});
  window.addEventListener('resize', resize, {passive:true});
  for (const preference of [reducedMotion, finePointer, forcedColors]) preference.addEventListener('change', clear);
})();
