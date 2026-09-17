
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

/* Approved Book 1 site-wide preview viewer */
const bookOnePreviewPages = [
  { src: 'assets/full-framework-front-cover.png', alt: 'The Full Framework front cover' },
  { src: 'assets/book1-preview-02.png', alt: 'The Full Framework preview — Chapter 2 opening' },
  { src: 'assets/book1-preview-03.png', alt: 'The Full Framework preview — Chapter 2 continuation' },
  { src: 'assets/appendix A Acts Timeline for the website insert.png', alt: 'The Full Framework preview — canonical four-marker Acts timeline' },
  { src: 'assets/book1-preview-05.png', alt: 'The Full Framework preview — canonical Two Programs chart' },
  { src: 'assets/book1-preview-06.png', alt: 'The Full Framework preview — Full Master Chart' },
  { src: 'assets/book1-preview-07.png', alt: 'The Full Framework preview — Full Master Chart continuation' },
  { src: 'assets/book1-preview-08.png', alt: 'The Full Framework preview — Overlap Zone Diagram' },
  { src: 'assets/back cover mock for website2.png', alt: 'The Full Framework — back cover' }
];

const previewModal = document.createElement('div');
previewModal.className = 'book-preview-modal';
previewModal.hidden = true;
previewModal.setAttribute('role', 'dialog');
previewModal.setAttribute('aria-modal', 'true');
previewModal.setAttribute('aria-label', 'Preview The Full Framework');
previewModal.innerHTML = `
  <div class="book-preview-shell">
    <div class="book-preview-topbar">
      <div class="book-preview-titleblock"><span class="book-preview-kicker">BOOK PREVIEW</span><div class="book-preview-heading"><em>The Full Framework</em></div></div>
      <button class="book-preview-close" type="button" aria-label="Close book preview">×</button>
    </div>
    <div class="book-preview-stage">
      <button class="book-preview-arrow book-preview-prev" type="button" aria-label="Previous preview page">‹</button>
      <img class="book-preview-image" src="" alt=""/>
      <button class="book-preview-arrow book-preview-next" type="button" aria-label="Next preview page">›</button>
    </div>
    <div class="book-preview-controls">
      <button class="book-preview-text-button book-preview-prev-bottom" type="button">‹ Previous</button>
      <span class="book-preview-count" aria-live="polite"></span>
      <button class="book-preview-text-button book-preview-next-bottom" type="button">Next ›</button>
    </div>
  </div>`;
document.body.appendChild(previewModal);

const previewImage = previewModal.querySelector('.book-preview-image');
const previewCount = previewModal.querySelector('.book-preview-count');
const previewClose = previewModal.querySelector('.book-preview-close');
const previewPrevButtons = previewModal.querySelectorAll('.book-preview-prev, .book-preview-prev-bottom');
const previewNextButtons = previewModal.querySelectorAll('.book-preview-next, .book-preview-next-bottom');
let previewIndex = 0;
let activePreviewTrigger = null;

const renderBookPreview = () => {
  const page = bookOnePreviewPages[previewIndex];
  previewImage.src = page.src;
  previewImage.alt = page.alt;
  previewImage.classList.toggle('book-preview-image--timeline', previewIndex === 3);
  previewCount.textContent = `Preview ${previewIndex + 1} of ${bookOnePreviewPages.length}`;
  previewPrevButtons.forEach((button) => { button.disabled = previewIndex === 0; });
  previewNextButtons.forEach((button) => { button.disabled = previewIndex === bookOnePreviewPages.length - 1; });
};

const openBookPreview = (trigger) => {
  activePreviewTrigger = trigger;
  previewIndex = 0;
  renderBookPreview();
  previewModal.hidden = false;
  trigger.setAttribute('aria-expanded', 'true');
  document.body.classList.add('lightbox-open');
  previewClose.focus();
};

const closeBookPreview = () => {
  previewModal.hidden = true;
  document.body.classList.remove('lightbox-open');
  if (activePreviewTrigger) {
    activePreviewTrigger.setAttribute('aria-expanded', 'false');
    activePreviewTrigger.focus();
  }
};

previewPrevButtons.forEach((button) => button.addEventListener('click', () => {
  if (previewIndex > 0) {
    previewIndex -= 1;
    renderBookPreview();
  }
}));
previewNextButtons.forEach((button) => button.addEventListener('click', () => {
  if (previewIndex < bookOnePreviewPages.length - 1) {
    previewIndex += 1;
    renderBookPreview();
  }
}));
previewClose.addEventListener('click', closeBookPreview);
previewModal.addEventListener('click', (event) => {
  if (event.target === previewModal) closeBookPreview();
});

const isBookOneTrigger = (trigger) => {
  const triggerImage = trigger.querySelector('img');
  const src = trigger.dataset.coverSrc || triggerImage?.getAttribute('src') || '';
  return src.includes('full-framework-front-cover.png');
};

if (coverTriggers.length) {
  let activeCoverTrigger = null;
  const closeButton = coverLightbox?.querySelector('.cover-lightbox-close');
  const lightboxImage = coverLightbox?.querySelector('img');

  const openCover = (trigger) => {
    if (!coverLightbox) return;
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
    if (!coverLightbox) return;
    coverLightbox.hidden = true;
    document.body.classList.remove('lightbox-open');
    if (activeCoverTrigger) {
      activeCoverTrigger.setAttribute('aria-expanded', 'false');
      activeCoverTrigger.focus();
    }
  };

  coverTriggers.forEach((trigger) => trigger.addEventListener('click', () => {
    if (isBookOneTrigger(trigger)) {
      openBookPreview(trigger);
    } else {
      openCover(trigger);
    }
  }));

  closeButton?.addEventListener('click', closeCover);
  coverLightbox?.addEventListener('click', (event) => {
    if (event.target === coverLightbox) closeCover();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      if (!previewModal.hidden) {
        closeBookPreview();
      } else if (coverLightbox && !coverLightbox.hidden) {
        closeCover();
      }
    }
    if (!previewModal.hidden && event.key === 'ArrowLeft' && previewIndex > 0) {
      previewIndex -= 1;
      renderBookPreview();
    }
    if (!previewModal.hidden && event.key === 'ArrowRight' && previewIndex < bookOnePreviewPages.length - 1) {
      previewIndex += 1;
      renderBookPreview();
    }
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

/* Approved Digital Studies catalog cover treatment */
if (document.body.classList.contains('digital-studies-page')) {
  const studyCards = document.querySelectorAll('.individual-studies .study-card');
  studyCards.forEach((card) => {
    const type = card.querySelector('.study-type');
    const match = type?.textContent.match(/Study\s+(\d+)/i);
    if (!match) return;
    const number = String(Number(match[1])).padStart(2, '0');
    const title = card.querySelector('h3')?.textContent.trim() || `Study ${Number(match[1])}`;
    const image = document.createElement('img');
    image.className = 'study-cover-thumb';
    image.src = `assets/study-${number}-cover.jpg`;
    image.alt = `${title} cover`;
    image.loading = 'lazy';
    image.decoding = 'async';
    const content = document.createElement('div');
    content.className = 'study-card-content';
    while (card.firstChild) content.appendChild(card.firstChild);
    card.appendChild(image);
    card.appendChild(content);
  });

  const studyCoverStyle = document.createElement('style');
  studyCoverStyle.textContent = `
    .digital-studies-page .study-card{display:grid;grid-template-columns:150px minmax(0,1fr);gap:22px;align-items:stretch;padding:20px;min-height:260px}
    .digital-studies-page .study-cover-thumb{display:block;width:150px;height:auto;aspect-ratio:2/3;object-fit:cover;align-self:start;border:1px solid #d8d1bf;box-shadow:0 5px 14px rgba(20,40,25,.12)}
    .digital-studies-page .study-card-content{display:flex;flex-direction:column;min-width:0;height:100%}
    .digital-studies-page .study-card-content .study-meta{margin-top:auto}
    @media(max-width:1100px){.digital-studies-page .study-card{grid-template-columns:125px minmax(0,1fr);gap:18px}.digital-studies-page .study-cover-thumb{width:125px}}
    @media(max-width:820px){.digital-studies-page .study-card{grid-template-columns:130px minmax(0,1fr);gap:18px}.digital-studies-page .study-cover-thumb{width:130px}}
    @media(max-width:520px){.digital-studies-page .study-card{grid-template-columns:96px minmax(0,1fr);gap:14px;padding:16px}.digital-studies-page .study-cover-thumb{width:96px}.digital-studies-page .study-card h3{font-size:1.25rem}.digital-studies-page .study-card p{font-size:.94rem}}
  `;
  document.head.appendChild(studyCoverStyle);
}
