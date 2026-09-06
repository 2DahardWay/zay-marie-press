
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
    activeCoverTrigger?.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('lightbox-open');
    activeCoverTrigger?.focus();
    activeCoverTrigger = null;
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

const processFlow = document.querySelector('.process-section .process-flow');
if (processFlow) {
  processFlow.innerHTML = '<img src="assets/about-conviction-to-craft.png" alt="Doctrine, editorial process, publication, and reader impact shown with warm photographic imagery" loading="lazy" style="display:block;width:100%;height:auto;" />';
  processFlow.style.display = 'block';
  processFlow.style.maxWidth = '960px';
  processFlow.style.border = '0';
  processFlow.style.boxShadow = 'none';
}

const libraryMark = document.querySelector('.library-section .library-mark');
if (libraryMark) {
  libraryMark.innerHTML = '<img src="assets/about-growing-theological-library.png" alt="Warm theological library with shelves of books" loading="lazy" style="display:block;width:100%;height:auto;" />';
  libraryMark.removeAttribute('aria-hidden');
  libraryMark.style.width = '640px';
  libraryMark.style.maxWidth = '90vw';
}

const orientation = document.querySelector('.orientation-section');
if (orientation) {
  const orientationWrap = orientation.querySelector('.wrap');
  if (orientationWrap) {
    orientationWrap.innerHTML = `
      <div class="orientation-title-mark" aria-hidden="true">
        <span></span>
        <svg viewBox="0 0 76 58"><path d="M12 18c9-3 18-2 26 4v27c-8-6-17-7-26-4z"/><path d="M64 18c-9-3-18-2-26 4v27c8-6 17-7 26-4z"/><path d="M38 22v27"/><path d="M38 4c4 5 6 8 6 12a6 6 0 0 1-12 0c0-3 2-6 6-12z"/></svg>
        <span></span>
      </div>
      <div class="about-heading orientation-heading">
        <h2>Our Orientation</h2>
        <p class="orientation-intro">Four convictions that shape the work of Zay-Marie Press</p>
      </div>
      <div class="orientation-principles" aria-label="Zay-Marie Press orientation principles">
        <div class="orientation-principle">
          <div class="orientation-mark" aria-hidden="true"><svg viewBox="0 0 64 52"><path d="M6 10c9-3 18-2 26 4v30c-8-6-17-7-26-4z"/><path d="M58 10c-9-3-18-2-26 4v30c8-6 17-7 26-4z"/><path d="M32 14v30"/></svg></div>
          <strong>Faithful to<br>Scripture</strong>
          <p>Biblical fidelity and text-driven interpretation.</p>
        </div>
        <div class="orientation-principle">
          <div class="orientation-mark" aria-hidden="true"><svg viewBox="0 0 64 52"><path d="M32 5c7 10 12 16 12 24a12 12 0 0 1-24 0c0-6 4-12 9-18 0 7 3 10 6 12 1-7-1-12-3-18z"/><path d="M27 36c2 4 8 5 11 1"/></svg></div>
          <strong>Led by<br>the Spirit</strong>
          <p>Illumination, dependence, and submission to the Spirit’s guidance.</p>
        </div>
        <div class="orientation-principle">
          <div class="orientation-mark" aria-hidden="true"><svg viewBox="0 0 64 52"><path d="M32 46V18"/><path d="M32 29c-9 0-15-5-17-13 9-1 15 3 17 13z"/><path d="M32 22c8 0 14-5 17-13-9-1-15 3-17 13z"/><path d="M24 46h16"/></svg></div>
          <strong>Life-Giving<br>Truth</strong>
          <p>Doctrine that strengthens, nourishes, and builds up.</p>
        </div>
        <div class="orientation-principle">
          <div class="orientation-mark" aria-hidden="true"><svg viewBox="0 0 64 52"><path d="M10 38h44"/><path d="M16 38c4-10 10-15 16-15s12 5 16 15"/><path d="M32 8v9M20 13l5 7M44 13l-5 7"/></svg></div>
          <strong>Eternal<br>Purpose</strong>
          <p>God’s promises, our heavenly calling, and future hope.</p>
        </div>
      </div>
      <div class="orientation-signoff"><strong>Zay-Marie Press</strong><em>Where the Bible Means What It Says</em></div>
    `;

    const orientationStyle = document.createElement('style');
    orientationStyle.textContent = `
      .orientation-section{background:linear-gradient(135deg,#f8f5ec 0%,#edf2e7 100%)!important}
      .orientation-section .wrap{max-width:1060px;padding:30px 50px 34px;background:radial-gradient(ellipse at center,#fffdf8 0%,#fffdf8 46%,#eef1e3 70%,#d9e6d4 100%);border:1px solid #d8d1bd;border-top:4px solid #b98519;box-shadow:inset 0 0 70px rgba(23,101,54,.10)}
      .orientation-section .wrap::after{margin-top:27px}
      .orientation-title-mark{display:grid;grid-template-columns:1fr 76px 1fr;align-items:center;gap:16px;max-width:900px;margin:0 auto 4px;color:#b98519}
      .orientation-title-mark span{height:1px;background:#b98519;opacity:.78}
      .orientation-title-mark svg{display:block;width:76px;height:58px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
      .orientation-heading{margin-bottom:28px}
      .orientation-heading h2{margin:0 0 9px;color:#176536}
      .orientation-intro{margin:0 auto!important;font-size:1.12rem!important;font-style:italic;color:#303d35}
      .orientation-principles{display:grid;grid-template-columns:repeat(4,1fr);max-width:900px;margin:0 auto;padding:4px 0 27px;border-bottom:1px solid rgba(185,133,25,.7)}
      .orientation-principle{position:relative;padding:0 20px;text-align:center}
      .orientation-principle+ .orientation-principle{border-left:1px solid #d9cfb7}
      .orientation-mark{width:58px;height:52px;margin:0 auto 12px;color:#b98519}
      .orientation-principle:nth-child(3) .orientation-mark{color:#176536}
      .orientation-mark svg{display:block;width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
      .orientation-principle strong{display:block;font-family:'Montserrat',Arial,sans-serif;font-size:.94rem;line-height:1.35;letter-spacing:.035em;text-transform:uppercase;color:#176536;padding-bottom:10px;border-bottom:1px solid rgba(185,133,25,.42)}
      .orientation-principle p{font-size:1rem!important;line-height:1.32;margin:10px auto 0!important;max-width:185px!important;font-style:italic;color:#303d35}
      .orientation-signoff{margin-top:23px;font-size:1.42rem;color:#176536}
      .orientation-signoff em{color:#0b4278}
      @media(max-width:700px){.orientation-section .wrap{padding:28px 22px 30px}.orientation-title-mark{grid-template-columns:1fr 68px 1fr}.orientation-title-mark svg{width:68px}.orientation-principles{grid-template-columns:1fr 1fr;gap:30px 0}.orientation-principle:nth-child(3){border-left:0}.orientation-principle{padding:0 14px}}
      @media(max-width:420px){.orientation-title-mark{grid-template-columns:1fr 60px 1fr;gap:10px}.orientation-title-mark svg{width:60px}.orientation-principles{grid-template-columns:1fr;gap:25px}.orientation-principle+ .orientation-principle{border-left:0}.orientation-principle{padding:0 8px 5px}.orientation-principle p{max-width:240px!important}}
    `;
    document.head.appendChild(orientationStyle);
  }
}

/* Diagnostic Manual — approved protocol spine hierarchy refinement. */
const diagnosticProtocol = document.querySelector('.protocol-instrument .protocol-spine');
if (diagnosticProtocol) {
  diagnosticProtocol.querySelectorAll('.protocol-step:not(:last-child)').forEach((step) => {
    const direction = document.createElement('span');
    direction.className = 'protocol-direction';
    direction.setAttribute('aria-hidden', 'true');
    direction.textContent = '▾';
    step.appendChild(direction);
  });

  const protocolRefinementStyle = document.createElement('style');
  protocolRefinementStyle.textContent = `
    .protocol-spine:before{width:3px!important;box-shadow:0 0 0 1px rgba(185,133,25,.08)}
    .protocol-step{padding-bottom:54px!important}
    .protocol-step:last-child{padding-bottom:0!important}
    .protocol-direction{position:absolute;z-index:2;left:26px;bottom:15px;width:20px;height:20px;display:flex;align-items:center;justify-content:center;background:#fcfdf9;color:#b98519;font:700 14px/1 Arial,sans-serif}
    @media(max-width:820px){.protocol-step{padding-bottom:48px!important}.protocol-direction{left:19px;bottom:13px}}
    @media(max-width:600px){.protocol-step{padding-bottom:44px!important}.protocol-direction{left:13px;bottom:12px;width:20px;height:20px}}
  `;
  document.head.appendChild(protocolRefinementStyle);
}

/* Diagnostic Manual — approved chronology palette refinement. */
const diagnosticChronology = document.querySelector('.dm-features + .series.model-section');
if (diagnosticChronology) {
  const chronologyStyle = document.createElement('style');
  chronologyStyle.textContent = `
    .dm-features + .series.model-section{background:radial-gradient(circle at 88% 18%,rgba(11,66,120,.055),transparent 30%),linear-gradient(135deg,#f8f5ec 0%,#f6f2e8 48%,#e3ece2 100%);color:#1d2520;border-top:0;border-bottom:2px solid #3b1110}
    .dm-features + .series.model-section h2{color:#143823}
    .dm-features + .series.model-section .eyebrow{color:#b98519}
    .dm-features + .series.model-section .model-lead{color:#1d2520;max-width:920px}
    .dm-features + .series.model-section .sequence-item{background:rgba(255,255,255,.78);border:1px solid #cbd5cc;box-shadow:0 5px 18px rgba(20,40,25,.035)}
    .dm-features + .series.model-section .sequence-item.prophecy{border-top:4px solid #b98519}
    .dm-features + .series.model-section .sequence-item.mystery{border-top:4px solid #0b4278}
    .dm-features + .series.model-section .sequence-item.overlap{border-top:4px solid #176536;background:rgba(227,236,226,.72)}
    .dm-features + .series.model-section .sequence-item.prophecy-end{border-top:4px solid #b98519}
    .dm-features + .series.model-section .sequence-item strong{color:#143823}
    .dm-features + .series.model-section .sequence-item.prophecy strong,.dm-features + .series.model-section .sequence-item.prophecy-end strong{color:#9b6d0f}
    .dm-features + .series.model-section .sequence-item.mystery strong{color:#0b4278}
    .dm-features + .series.model-section .sequence-item.overlap strong{color:#176536}
    .dm-features + .series.model-section .sequence-item small{color:#303d35;opacity:1}
    .dm-features + .series.model-section .sequence-kicker{color:#59645e}
    .dm-features + .series.model-section .sequence-item.prophecy .sequence-kicker,.dm-features + .series.model-section .sequence-item.prophecy-end .sequence-kicker{color:#b98519}
    .dm-features + .series.model-section .sequence-item.mystery .sequence-kicker{color:#0b4278}
    .dm-features + .series.model-section .sequence-item.overlap .sequence-kicker{color:#176536}
    .dm-features + .series.model-section .sequence-arrow{color:#b98519}
    .dm-features + .series.model-section .model-copy{margin-top:22px;border-left:3px solid #b98519;padding-left:18px;max-width:960px}
    .dm-features + .series.model-section .model-copy p{margin:0}
  `;
  document.head.appendChild(chronologyStyle);

  const diagnosticConclusion = diagnosticChronology.querySelector('.model-copy');
  if (diagnosticConclusion) {
    diagnosticConclusion.innerHTML = '<p><strong>Why the chronology matters diagnostically:</strong> A passage cannot be classified by subject matter alone. Its place within the Acts chronology helps determine which divine program, audience, and doctrinal context governs the passage. The Acts 9–28 overlap therefore becomes an essential coordinate in the diagnostic process.</p>';
  }
}
