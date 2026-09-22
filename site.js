
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.primary-nav');
if (toggle && nav) {
  if (!nav.querySelector('a[href="digital-studies.html"]')) {
    const seriesLink = nav.querySelector('a[href="series.html"]');
    const digitalStudiesLink = document.createElement('a');
    digitalStudiesLink.href = 'digital-studies.html';
    digitalStudiesLink.textContent = 'DIGITAL STUDIES';
    if (seriesLink) seriesLink.insertAdjacentElement('afterend', digitalStudiesLink); else nav.appendChild(digitalStudiesLink);
  }
  if (!nav.querySelector('a[href="biblical-hermeneutics-course.html"]')) {
    const digitalStudiesLink = nav.querySelector('a[href="digital-studies.html"]');
    const seriesLink = nav.querySelector('a[href="series.html"]');
    const courseLink = document.createElement('a');
    courseLink.href = 'biblical-hermeneutics-course.html';
    courseLink.textContent = 'COURSE';
    if (digitalStudiesLink) digitalStudiesLink.insertAdjacentElement('afterend', courseLink);
    else if (seriesLink) seriesLink.insertAdjacentElement('afterend', courseLink);
    else nav.appendChild(courseLink);
  }
  const closeMenu = () => { toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); };
  toggle.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') === 'true'; toggle.setAttribute('aria-expanded', String(!open)); nav.classList.toggle('open', !open); });
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } });
  const normalizePage = (value) => { const clean = (value || '').split('?')[0].split('#')[0].replace(/^.*\//, '').toLowerCase(); if (!clean || clean === 'index.html' || clean === 'index') return 'home'; return clean.replace(/\.html$/, ''); };
  const currentPage = normalizePage(window.location.pathname);
  const navSectionByPage = {home:'home',books:'books','full-framework':'books','diagnostic-manual':'books',series:'series','digital-studies':'digital-studies','biblical-hermeneutics-course':'biblical-hermeneutics-course',about:'about',resources:'resources','acts-overlap-visual-guide':'resources',contact:'contact'};
  const activeSection = navSectionByPage[currentPage];
  if (activeSection) {
    nav.querySelectorAll('a').forEach((link) => { const linkPage = normalizePage(link.getAttribute('href')); const linkSection = navSectionByPage[linkPage] || linkPage; if (linkSection === activeSection) { link.classList.add('current-page'); link.setAttribute('aria-current','page'); } else { link.classList.remove('current-page'); link.removeAttribute('aria-current'); } });
    const currentNavStyle = document.createElement('style'); currentNavStyle.textContent = `.primary-nav a.current-page{color:#8a918d!important;border-bottom:2px solid #8a918d;padding-bottom:5px}`; document.head.appendChild(currentNavStyle);
  }
}

const coverTriggers = document.querySelectorAll('.cover-enlarge');
const coverLightbox = document.querySelector('#cover-lightbox');
const bookOnePreviewPages = [
  {src:'assets/full-framework-front-cover.png',alt:'The Full Framework front cover'},
  {src:'assets/book1-preview-02.png',alt:'The Full Framework preview — Chapter 2 opening'},
  {src:'assets/book1-preview-03.png',alt:'The Full Framework preview — Chapter 2 continuation'},
  {src:'assets/appendix A Acts Timeline for the website insert.png',alt:'The Full Framework preview — canonical four-marker Acts timeline'},
  {src:'assets/book1-preview-05.png',alt:'The Full Framework preview — canonical Two Programs chart'},
  {src:'assets/book1-preview-06.png',alt:'The Full Framework preview — Full Master Chart'},
  {src:'assets/book1-preview-07.png',alt:'The Full Framework preview — Full Master Chart continuation'},
  {src:'assets/book1-preview-08.png',alt:'The Full Framework preview — Overlap Zone Diagram'},
  {src:'assets/back cover mock for website2.png',alt:'The Full Framework — back cover'}
];
const previewModal = document.createElement('div'); previewModal.className='book-preview-modal'; previewModal.hidden=true; previewModal.setAttribute('role','dialog'); previewModal.setAttribute('aria-modal','true'); previewModal.setAttribute('aria-label','Preview The Full Framework'); previewModal.innerHTML=`<div class="book-preview-shell"><div class="book-preview-topbar"><div class="book-preview-titleblock"><span class="book-preview-kicker">BOOK PREVIEW</span><div class="book-preview-heading"><em>The Full Framework</em></div></div><button class="book-preview-close" type="button" aria-label="Close book preview">×</button></div><div class="book-preview-stage"><button class="book-preview-arrow book-preview-prev" type="button" aria-label="Previous preview page">‹</button><img class="book-preview-image" src="" alt=""/><button class="book-preview-arrow book-preview-next" type="button" aria-label="Next preview page">›</button></div><div class="book-preview-controls"><button class="book-preview-text-button book-preview-prev-bottom" type="button">‹ Previous</button><span class="book-preview-count" aria-live="polite"></span><button class="book-preview-text-button book-preview-next-bottom" type="button">Next ›</button></div></div>`; document.body.appendChild(previewModal);
const previewImage=previewModal.querySelector('.book-preview-image'), previewCount=previewModal.querySelector('.book-preview-count'), previewClose=previewModal.querySelector('.book-preview-close'), previewPrevButtons=previewModal.querySelectorAll('.book-preview-prev,.book-preview-prev-bottom'), previewNextButtons=previewModal.querySelectorAll('.book-preview-next,.book-preview-next-bottom'); let previewIndex=0, activePreviewTrigger=null;
const renderBookPreview=()=>{const page=bookOnePreviewPages[previewIndex]; previewImage.src=page.src; previewImage.alt=page.alt; previewImage.classList.toggle('book-preview-image--timeline',previewIndex===3); previewCount.textContent=`Preview ${previewIndex+1} of ${bookOnePreviewPages.length}`; previewPrevButtons.forEach(b=>b.disabled=previewIndex===0); previewNextButtons.forEach(b=>b.disabled=previewIndex===bookOnePreviewPages.length-1);};
const openBookPreview=(trigger)=>{activePreviewTrigger=trigger; previewIndex=0; renderBookPreview(); previewModal.hidden=false; trigger.setAttribute('aria-expanded','true'); document.body.classList.add('lightbox-open'); previewClose.focus();};
const closeBookPreview=()=>{previewModal.hidden=true; document.body.classList.remove('lightbox-open'); if(activePreviewTrigger){activePreviewTrigger.setAttribute('aria-expanded','false');activePreviewTrigger.focus();}};
previewPrevButtons.forEach(b=>b.addEventListener('click',()=>{if(previewIndex>0){previewIndex--;renderBookPreview();}})); previewNextButtons.forEach(b=>b.addEventListener('click',()=>{if(previewIndex<bookOnePreviewPages.length-1){previewIndex++;renderBookPreview();}})); previewClose.addEventListener('click',closeBookPreview); previewModal.addEventListener('click',e=>{if(e.target===previewModal)closeBookPreview();});
const isBookOneTrigger=(trigger)=>{const img=trigger.querySelector('img'); const src=trigger.dataset.coverSrc||img?.getAttribute('src')||''; return src.includes('full-framework-front-cover.png');};
if(coverTriggers.length){let activeCoverTrigger=null; const closeButton=coverLightbox?.querySelector('.cover-lightbox-close'), lightboxImage=coverLightbox?.querySelector('img'); const openCover=(trigger)=>{if(!coverLightbox)return; activeCoverTrigger=trigger; if(lightboxImage){const img=trigger.querySelector('img');lightboxImage.src=trigger.dataset.coverSrc||img?.src||lightboxImage.src;lightboxImage.alt=trigger.dataset.coverAlt||img?.alt||'Enlarged book cover';}coverLightbox.hidden=false;trigger.setAttribute('aria-expanded','true');document.body.classList.add('lightbox-open');closeButton?.focus();}; const closeCover=()=>{if(!coverLightbox)return;coverLightbox.hidden=true;document.body.classList.remove('lightbox-open');if(activeCoverTrigger){activeCoverTrigger.setAttribute('aria-expanded','false');activeCoverTrigger.focus();}}; coverTriggers.forEach(trigger=>trigger.addEventListener('click',()=>isBookOneTrigger(trigger)?openBookPreview(trigger):openCover(trigger))); closeButton?.addEventListener('click',closeCover); coverLightbox?.addEventListener('click',e=>{if(e.target===coverLightbox)closeCover();}); document.addEventListener('keydown',e=>{if(e.key==='Escape'){if(!previewModal.hidden)closeBookPreview();else if(coverLightbox&&!coverLightbox.hidden)closeCover();} if(!previewModal.hidden&&e.key==='ArrowLeft'&&previewIndex>0){previewIndex--;renderBookPreview();} if(!previewModal.hidden&&e.key==='ArrowRight'&&previewIndex<bookOnePreviewPages.length-1){previewIndex++;renderBookPreview();}});}

const resourceSearch=document.querySelector('#resource-search'), resourceCategory=document.querySelector('#resource-category'), resourceCards=Array.from(document.querySelectorAll('[data-resource-card]')), resourceEmpty=document.querySelector('#resource-empty');
if(resourceCards.length&&(resourceSearch||resourceCategory)){const normalize=v=>(v||'').toLowerCase().trim(); const filterResources=()=>{const searchTerm=normalize(resourceSearch?.value), category=normalize(resourceCategory?.value);let visibleCount=0;resourceCards.forEach(card=>{const haystack=normalize(card.dataset.search||card.textContent),cardCategory=normalize(card.dataset.category),visible=(!searchTerm||haystack.includes(searchTerm))&&(!category||category==='all'||cardCategory===category);card.hidden=!visible;if(visible)visibleCount++;});if(resourceEmpty)resourceEmpty.hidden=visibleCount!==0;};resourceSearch?.addEventListener('input',filterResources);resourceCategory?.addEventListener('change',filterResources);filterResources();}
const resourceModal=document.querySelector('#resource-modal'), resourceModalTitle=resourceModal?.querySelector('[data-modal-title]'), resourceModalDescription=resourceModal?.querySelector('[data-modal-description]'), resourceModalLink=resourceModal?.querySelector('[data-modal-link]'), resourceModalClose=resourceModal?.querySelector('[data-modal-close]'), resourceModalTriggers=document.querySelectorAll('[data-resource-open]');let lastResourceTrigger=null;
if(resourceModal&&resourceModalTriggers.length){const closeResourceModal=()=>{resourceModal.hidden=true;document.body.classList.remove('resource-modal-open');lastResourceTrigger?.focus();};resourceModalTriggers.forEach(trigger=>trigger.addEventListener('click',()=>{lastResourceTrigger=trigger;if(resourceModalTitle)resourceModalTitle.textContent=trigger.dataset.title||'Resource';if(resourceModalDescription)resourceModalDescription.textContent=trigger.dataset.description||'';if(resourceModalLink){resourceModalLink.href=trigger.dataset.href||'#';resourceModalLink.textContent=trigger.dataset.linkText||'OPEN RESOURCE';}resourceModal.hidden=false;document.body.classList.add('resource-modal-open');resourceModalClose?.focus();}));resourceModalClose?.addEventListener('click',closeResourceModal);resourceModal.addEventListener('click',e=>{if(e.target===resourceModal)closeResourceModal();});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!resourceModal.hidden)closeResourceModal();});}

/* Display the verified final-PDF page count at the primary purchase decision point. */
const digitalStudyPageCounts={1:14,2:15,3:20,4:20,5:16,6:16,7:17,8:15,9:15,10:23,11:13,12:13,13:15,14:13,15:13,16:14,17:14,18:13,19:13,20:13,21:14,22:15,23:15,24:13,25:13,26:17,27:15,28:14,29:13};
const digitalStudyMatch=window.location.pathname.match(/\/study-(\d+)-/i);
const digitalStudyFormat=document.querySelector('.detail-hero .detail-format');
if(digitalStudyMatch&&digitalStudyFormat){const studyNumber=Number(digitalStudyMatch[1]),pageCount=digitalStudyPageCounts[studyNumber];if(pageCount)digitalStudyFormat.textContent=`Digital PDF · ${pageCount} Pages`;}
if(digitalStudyMatch){document.querySelectorAll('.detail-button.pending').forEach(button=>{button.textContent='Checkout Coming Soon';button.setAttribute('aria-disabled','true');});}

/* Approved Digital Studies catalog: larger real covers, tighter cards, click-to-enlarge preview. */
if(document.body.classList.contains('digital-studies-page')){
  const studyCards=document.querySelectorAll('.individual-studies .study-card');
  const studyPreview=document.createElement('div'); studyPreview.className='study-cover-preview'; studyPreview.hidden=true; studyPreview.setAttribute('role','dialog'); studyPreview.setAttribute('aria-modal','true'); studyPreview.setAttribute('aria-label','Digital Study cover preview'); studyPreview.innerHTML='<button class="study-cover-preview-close" type="button" aria-label="Close cover preview">×</button><img src="" alt="">'; document.body.appendChild(studyPreview);
  const previewImg=studyPreview.querySelector('img'), previewCloseBtn=studyPreview.querySelector('.study-cover-preview-close'); let activeStudyCover=null;
  const closeStudyPreview=()=>{studyPreview.hidden=true;document.body.classList.remove('lightbox-open');activeStudyCover?.focus();};
  previewCloseBtn.addEventListener('click',closeStudyPreview); studyPreview.addEventListener('click',e=>{if(e.target===studyPreview)closeStudyPreview();}); document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!studyPreview.hidden)closeStudyPreview();});
  studyCards.forEach(card=>{const type=card.querySelector('.study-type'),match=type?.textContent.match(/Study\s+(\d+)/i);if(!match)return;const number=String(Number(match[1])).padStart(2,'0'),title=card.querySelector('h3')?.textContent.trim()||`Study ${Number(match[1])}`;const button=document.createElement('button');button.className='study-cover-button';button.type='button';button.setAttribute('aria-label',`Enlarge ${title} cover`);const image=document.createElement('img');image.className='study-cover-thumb';image.src=number==='01'?'assets/study-01-cover-final-v2.png':number==='29'?'assets/study-29-cover-v4.webp':number==='30'?'assets/study-30-cover-v2.webp':number==='35'?'assets/study-35-cover.webp':number==='36'?'assets/study-36-cover.webp':`assets/study-${number}-cover.jpg`;image.alt=`${title} cover`;image.loading='lazy';image.decoding='async';if(number==='03')card.classList.add('study-card-03');button.appendChild(image);button.addEventListener('click',()=>{activeStudyCover=button;previewImg.src=image.src;previewImg.alt=image.alt;studyPreview.hidden=false;document.body.classList.add('lightbox-open');previewCloseBtn.focus();});const content=document.createElement('div');content.className='study-card-content';while(card.firstChild)content.appendChild(card.firstChild);card.appendChild(button);card.appendChild(content);});
  const style=document.createElement('style');style.textContent=`
    .digital-studies-page .study-card{display:grid;grid-template-columns:185px minmax(0,1fr);gap:20px;align-items:stretch;padding:16px;min-height:0}
    .digital-studies-page .study-cover-button{display:block;width:185px;padding:0;border:0;background:transparent;cursor:zoom-in;align-self:start}
    .digital-studies-page .study-cover-thumb{display:block;width:185px;height:auto;aspect-ratio:2/3;object-fit:cover;border:1px solid #d8d1bf;box-shadow:0 5px 14px rgba(20,40,25,.12)}
    .digital-studies-page .study-cover-button:focus-visible{outline:3px solid #1d6b43;outline-offset:4px}
    .digital-studies-page .study-card-content{display:flex;flex-direction:column;min-width:0;height:100%}
    .digital-studies-page .study-card-content .study-meta{margin-top:auto}
    .digital-studies-page .study-card-03 h3{font-weight:700;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}
    .digital-studies-page .study-card-03 h3 + p{font-weight:500;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}
    .study-cover-preview[hidden]{display:none}.study-cover-preview{position:fixed;inset:0;z-index:10000;background:rgba(7,20,12,.86);display:flex;align-items:center;justify-content:center;padding:36px}
    .study-cover-preview img{display:block;max-height:88vh;max-width:min(92vw,680px);width:auto;height:auto;box-shadow:0 18px 55px rgba(0,0,0,.45)}
    .study-cover-preview-close{position:fixed;top:20px;right:26px;width:48px;height:48px;border:1px solid rgba(255,255,255,.7);border-radius:50%;background:#fff;color:#123d28;font-size:32px;line-height:1;cursor:pointer}
    @media(max-width:1100px){.digital-studies-page .study-card{grid-template-columns:155px minmax(0,1fr);gap:17px}.digital-studies-page .study-cover-button,.digital-studies-page .study-cover-thumb{width:155px}}
    @media(max-width:820px){.digital-studies-page .study-card{grid-template-columns:145px minmax(0,1fr);gap:16px}.digital-studies-page .study-cover-button,.digital-studies-page .study-cover-thumb{width:145px}}
    @media(max-width:520px){.digital-studies-page .study-card{grid-template-columns:112px minmax(0,1fr);gap:13px;padding:14px}.digital-studies-page .study-cover-button,.digital-studies-page .study-cover-thumb{width:112px}.digital-studies-page .study-card h3{font-size:1.25rem}.digital-studies-page .study-card p{font-size:.94rem}.study-cover-preview{padding:20px}.study-cover-preview img{max-height:84vh;max-width:92vw}}
  `;document.head.appendChild(style);
}
