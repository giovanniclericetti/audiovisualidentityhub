const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#site-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
    toggle.querySelector('span').textContent = open ? '−' : '+';
  });
  const closeMenu = () => {
    if (toggle.getAttribute('aria-expanded') === 'true') toggle.click();
  };
  nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('click', event => {
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
  const path = location.pathname;
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
// Keep the archive's editorial column order without duplicating cards or links.
const archiveGrid = document.querySelector('.studies-grid');
if (archiveGrid) {
  const archiveCards = [...archiveGrid.querySelectorAll('.study-card')];
  let previousColumns = 0;
  const arrangeArchive = () => {
    const count = innerWidth >= 1536 ? 4 : innerWidth >= 1200 ? 3 : innerWidth >= 768 ? 2 : 1;
    if (count === previousColumns) return;
    previousColumns = count;
    const columns = Array.from({length:count}, () => {
      const column = document.createElement('div');
      column.className = 'study-column';
      return column;
    });
    const desktopGroups = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3];
    const mediumGroups = [0,0,0,0,1,1,1,1,2,2,2,1,0,2,2];
    archiveCards.forEach((card,index) => columns[count === 4 ? desktopGroups[index] : count === 3 ? mediumGroups[index] : count === 2 ? (index < 8 ? 0 : 1) : 0].append(card));
    archiveGrid.replaceChildren(...columns);
  };
  arrangeArchive();
  window.addEventListener('resize', arrangeArchive);
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
