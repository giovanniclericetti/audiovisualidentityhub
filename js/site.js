document.documentElement.classList.add('js');
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#site-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
    toggle.textContent = open ? 'Chiudi' : 'Menu';
  });
  const closeMenu = () => {
    if (toggle.getAttribute('aria-expanded') === 'true') toggle.click();
  };
  nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('click', event => {
    if (!nav.contains(event.target) && !toggle.contains(event.target)) closeMenu();
  });
  document.addEventListener('focusin', event => {
    if (!nav.contains(event.target) && !toggle.contains(event.target)) closeMenu();
  });
  matchMedia('(min-width:768px)').addEventListener('change', event => {
    if (event.matches) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('open')) {
      toggle.click();
      toggle.focus();
    }
  });
}
for (const link of document.querySelectorAll('#site-nav a')) {
  const path = location.pathname === '/' ? '/index.html' : location.pathname;
  const destination = new URL(link.href).pathname;
  const sameSection = ['/documentazione/', '/case-studies/'].some(section =>
    path.startsWith(section) && destination.startsWith(section));
  if (path === destination || sameSection) {
    link.setAttribute('aria-current', path === destination ? 'page' : 'location');
  } else {
    link.removeAttribute('aria-current');
  }
}
// Duplicate complete groups and measure the exact repeat distance on resize.
function continuousStrip(viewport, track, group, speed) {
  const originals = [...group.children];
  viewport.addEventListener('focusin', event => {
    if (event.target.closest('a,button')) {
      event.target.scrollIntoView({block:'nearest', inline:'nearest', behavior:'instant'});
    }
  });
  viewport.addEventListener('focusout', event => {
    if (!viewport.contains(event.relatedTarget)) viewport.scrollLeft = 0;
  });
  const clone = node => {
    const copy = node.cloneNode(true);
    copy.setAttribute('aria-hidden', 'true');
    if (copy.matches('a, button')) copy.tabIndex = -1;
    copy.querySelectorAll('a, button, [tabindex]').forEach(item => item.tabIndex = -1);
    copy.querySelectorAll('[id]').forEach(item => item.removeAttribute('id'));
    return copy;
  };
  let lastWidth = -1;
  const measure = () => {
    const width = viewport.clientWidth;
    if (!width || width === lastWidth) return;
    lastWidth = width;
    track.querySelectorAll(':scope > [aria-hidden="true"]').forEach(item => item.remove());
    group.replaceChildren(...originals);
    // At very wide viewports a single source group may be shorter than the screen.
    while (group.getBoundingClientRect().width < width) originals.forEach(item => group.append(clone(item)));
    const distance = group.getBoundingClientRect().width;
    track.style.setProperty('--loop-distance', `${distance}px`);
    track.style.setProperty('--loop-duration', `${distance / speed}s`);
    track.append(clone(group));
  };
  new ResizeObserver(measure).observe(viewport);
  measure();
}
for (const track of document.querySelectorAll('.ribbon-track')) {
  continuousStrip(track.parentElement, track, track.firstElementChild, 35);
}
for (const viewport of document.querySelectorAll('.case-grid')) {
  const group = document.createElement('div');
  group.className = 'loop-group';
  group.append(...viewport.children);
  const track = document.createElement('div');
  track.className = 'loop-track';
  track.append(group);
  viewport.append(track);
  viewport.classList.add('is-loop');
  continuousStrip(viewport, track, group, 35);
}
const images = document.querySelectorAll('.research-image');
if (images.length) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      images.forEach((image, index) => image.classList.toggle('active', index === Number(entry.target.dataset.research)));
    }
  }, {rootMargin:'-35% 0px -35% 0px'});
  document.querySelectorAll('.research-step').forEach(step => observer.observe(step));
}
const chapterMenu = document.querySelector('.chapter-menu');
if (chapterMenu) {
  const mobileChapters = matchMedia('(max-width:1199px)');
  const syncChapters = () => { chapterMenu.open = !mobileChapters.matches; };
  syncChapters();
  mobileChapters.addEventListener('change', syncChapters);
}
// Testimonials form a continuous strip, like the moving brand galleries.
const testimonials = document.querySelector('.testimonials-grid');
if (testimonials) {
  const group = document.createElement('div');
  group.className = 'loop-group';
  group.append(...testimonials.children);
  const track = document.createElement('div');
  track.className = 'loop-track';
  track.append(group);
  testimonials.append(track);
  testimonials.classList.add('is-loop');
  continuousStrip(testimonials, track, group, 35);
}
