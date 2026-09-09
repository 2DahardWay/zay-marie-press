
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.primary-nav');
if (toggle && nav) {
  /* Approved site-wide navigation architecture: place Digital Studies between Series and About. */
  if (!nav.querySelector('a[href="digital-studies.html"]')) {
    const seriesLink = nav.querySelector('a[href="series.html"]');
    const digitalStudiesLink = document.createElement('a');
    digitalStudiesLink.href = 'digital-studies.html';
    digitalStudiesLink.textContent = 'DIGITAL STUDIES';
    if (seriesLink) {
      seriesLink.insertAdjacentElement('afterend', digitalStudiesLink);
    } else {
      nav.appendChild(digitalStudiesLink);
    }
  }

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

  /* Site-wide current-page navigation indicator. */
  const normalizePage = (value) => {
    const clean = (value || '').split('?')[0].split('#')[0].replace(/^.*\//, '').toLowerCase();
    if (!clean || clean === 'index.html' || clean === 'index') return 'home';
    return clean.replace(/\.html$/, '');
  };

  const currentPage = normalizePage(window.location.pathname);
  const navSectionByPage = {
    home: 'home',
    books: 'books',
    'full-framework': 'books',
    'diagnostic-manual': 'books',
    series: 'series',
    'digital-studies': 'digital-studies',
    about: 'about',
    resources: 'resources',
    'acts-overlap-visual-guide': 'resources',
    contact: 'contact'
  };
  const activeSection = navSectionByPage[currentPage];

  if (activeSection) {
    nav.querySelectorAll('a').forEach((link) => {
      const linkPage = normalizePage(link.getAttribute('href'));
      const linkSection = navSectionByPage[linkPage] || linkPage;
      if (linkSection === activeSection) {
        link.classList.add('current-page');
        link.setAttribute('aria-current', 'page');
      } else {
        link.classList.remove('current-page');
        link.removeAttribute('aria-current');
      }
    });

    const currentNavStyle = document.createElement('style');
    currentNavStyle.textContent = `
      .primary-nav a.current-page{color:#8a918d!important;border-bottom:2px solid #8a918d;padding-bottom:5px}
    `;
    document.head.appendChild(currentNavStyle);
  }
}

const coverTriggers = document.querySelectorAll('.cover-enlarge');
const coverLightbox = document.querySelector('#cover-lightbox');
if (coverTriggers.length && coverLightbox) {
  const closeButton = coverLightbox.querySelector('.cover-lightbox-close');
  const lightboxImage = coverLightbox.querySelector('img');
  let activeCoverTrigger = null;

  const openCover = (trigger) => {
    activeCoverTrigger = trigger;
    if (lightboxImage) {
      const triggerImage = trigger.querySelector('img');
      lightboxImage.src = trigger.dataset.coverSrc || triggerImage?.src || lightboxImage.src;
      lightboxImage.alt = trigger.dataset.coverAlt || triggerImage?.alt || 'Enlarged book cover';
    }
    coverLightbox.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('lightbox-open');
    closeButton?.focus();
  };

  const closeCover = () => {
    coverLightbox.hidden = true;
    document.body.classList.remove('lightbox-open');
    if (activeCoverTrigger) {
      activeCoverTrigger.setAttribute('aria-expanded', 'false');
      activeCoverTrigger.focus();
    }
  };

  coverTriggers.forEach((trigger) => trigger.addEventListener('click', () => openCover(trigger)));
  closeButton?.addEventListener('click', closeCover);
  coverLightbox.addEventListener('click', (event) => {
    if (event.target === coverLightbox) closeCover();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !coverLightbox.hidden) closeCover();
  });
}

/* Resource Library behavior */
const resourceSearch = document.querySelector('#resource-search');
const resourceCategory = document.querySelector('#resource-category');
const resourceCards = Array.from(document.querySelectorAll('[data-resource-card]'));
const resourceEmpty = document.querySelector('#resource-empty');

if (resourceCards.length && (resourceSearch || resourceCategory)) {
  const normalize = (value) => (value || '').toLowerCase().trim();
  const filterResources = () => {
    const searchTerm = normalize(resourceSearch?.value);
    const category = normalize(resourceCategory?.value);
    let visibleCount = 0;

    resourceCards.forEach((card) => {
      const haystack = normalize(card.dataset.search || card.textContent);
      const cardCategory = normalize(card.dataset.category);
      const matchesSearch = !searchTerm || haystack.includes(searchTerm);
      const matchesCategory = !category || category === 'all' || cardCategory === category;
      const visible = matchesSearch && matchesCategory;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    if (resourceEmpty) resourceEmpty.hidden = visibleCount !== 0;
  };

  resourceSearch?.addEventListener('input', filterResources);
  resourceCategory?.addEventListener('change', filterResources);
  filterResources();
}

/* Resource modal behavior */
const resourceModal = document.querySelector('#resource-modal');
const resourceModalTitle = resourceModal?.querySelector('[data-modal-title]');
const resourceModalDescription = resourceModal?.querySelector('[data-modal-description]');
const resourceModalLink = resourceModal?.querySelector('[data-modal-link]');
const resourceModalClose = resourceModal?.querySelector('[data-modal-close]');
const resourceModalTriggers = document.querySelectorAll('[data-resource-open]');
let lastResourceTrigger = null;

if (resourceModal && resourceModalTriggers.length) {
  const closeResourceModal = () => {
    resourceModal.hidden = true;
    document.body.classList.remove('resource-modal-open');
    lastResourceTrigger?.focus();
  };

  resourceModalTriggers.forEach((trigger) => {
    trigger.addEventListener('click', () => {
      lastResourceTrigger = trigger;
      if (resourceModalTitle) resourceModalTitle.textContent = trigger.dataset.title || 'Resource';
      if (resourceModalDescription) resourceModalDescription.textContent = trigger.dataset.description || '';
      if (resourceModalLink) {
        resourceModalLink.href = trigger.dataset.href || '#';
        resourceModalLink.textContent = trigger.dataset.linkText || 'OPEN RESOURCE';
      }
      resourceModal.hidden = false;
      document.body.classList.add('resource-modal-open');
      resourceModalClose?.focus();
    });
  });

  resourceModalClose?.addEventListener('click', closeResourceModal);
  resourceModal.addEventListener('click', (event) => {
    if (event.target === resourceModal) closeResourceModal();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !resourceModal.hidden) closeResourceModal();
  });
}
