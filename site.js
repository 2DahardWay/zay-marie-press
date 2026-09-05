
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.primary-nav');
if (toggle && nav) {
  const closeMenu = () => {
    toggle.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
  };

  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('open', !open);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      toggle.focus();
    }
  });
}

const coverTrigger = document.querySelector('.cover-enlarge');
const coverLightbox = document.querySelector('#cover-lightbox');
if (coverTrigger && coverLightbox) {
  const closeButton = coverLightbox.querySelector('.cover-lightbox-close');

  const openCover = () => {
    coverLightbox.hidden = false;
    coverTrigger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('lightbox-open');
    closeButton?.focus();
  };

  const closeCover = () => {
    coverLightbox.hidden = true;
    coverTrigger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('lightbox-open');
    coverTrigger.focus();
  };

  coverTrigger.addEventListener('click', openCover);
  closeButton?.addEventListener('click', closeCover);
  coverLightbox.addEventListener('click', (event) => {
    if (event.target === coverLightbox) closeCover();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !coverLightbox.hidden) closeCover();
  });
}
