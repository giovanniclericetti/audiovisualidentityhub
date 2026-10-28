// Independent of the galleries: cursor initialization cannot be blocked by them.
(() => {
  const root = document.documentElement;
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const dot = document.createElement('div');
  const ring = document.createElement('div');
  dot.className = 'azure-cursor azure-cursor__dot';
  ring.className = 'azure-cursor azure-cursor__ring';
  for (const element of [ring, dot]) {
    element.setAttribute('aria-hidden', 'true');
    document.body.append(element);
  }
  let active = false, frame = 0, x = 0, y = 0, targetX = 0, targetY = 0, lastTime = 0;
  const place = (element, left, top) => {
    element.style.transform = `translate3d(${left}px,${top}px,0)`;
  };
  const hide = () => {
    active = false;
    cancelAnimationFrame(frame);
    frame = 0;
    root.classList.remove('azure-cursor-active');
    ring.classList.remove('is-link', 'is-pressed');
  };
  const tick = time => {
    const dt = Math.min(time - lastTime, 64);
    lastTime = time;
    const follow = reducedMotion.matches ? 1 : 1 - Math.exp(-dt / 65);
    x += (targetX - x) * follow;
    y += (targetY - y) * follow;
    place(ring, x, y);
    if (Math.abs(targetX - x) + Math.abs(targetY - y) > .05) {
      frame = requestAnimationFrame(tick);
    } else {
      place(ring, targetX, targetY);
      frame = 0;
    }
  };
  document.addEventListener('pointermove', event => {
    if (event.pointerType !== 'mouse') return hide();
    if (event.target.closest('input,textarea,[contenteditable],iframe,video,:disabled,[aria-disabled="true"]')) return hide();
    targetX = event.clientX;
    targetY = event.clientY;
    if (!active) {
      x = targetX;
      y = targetY;
      place(ring, x, y);
    }
    active = true;
    place(dot, targetX, targetY);
    root.classList.add('azure-cursor-active');
    ring.classList.toggle('is-link', !!event.target.closest('a,button,summary,[role="button"]'));
    if (!frame) {
      lastTime = performance.now();
      frame = requestAnimationFrame(tick);
    }
  }, {passive:true});
  document.addEventListener('pointerdown', event => {
    if (event.pointerType !== 'mouse') return hide();
    if (active) ring.classList.add('is-pressed');
  });
  window.addEventListener('pointerup', () => ring.classList.remove('is-pressed'));
  root.addEventListener('pointerleave', hide);
  window.addEventListener('blur', hide);
  document.addEventListener('visibilitychange', () => { if (document.hidden) hide(); });
  document.addEventListener('keydown', event => { if (event.key === 'Tab') hide(); });
})();
