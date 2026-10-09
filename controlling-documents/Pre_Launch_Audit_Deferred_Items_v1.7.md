# Pre-Launch Audit — Deferred Items (v1.6, 2026-10-07)

Working list for the one full website audit before the site opens to the public (Master Standard v1.72, Section 14, Stage 9). While the site is not public, each push gets the light per-integration check; items below are noticed but not yet fixed, or fixed only in part, and wait for the audit. Add to this list as items are found; bump the version and rename the file as it changes. Working record, not a rule.

## The audit itself (final site, all pages)
- Section-by-section screenshot walk of every page at 390, 360 and 320 px, plus desktop; report only what was observed.
- Image, link, sitemap and redirect check across the site.
- Count, label and series-name consistency across catalog, hub, connections guide and Library Edition pages.
- OCR pass over preview images for working terms (Master Standard Section 20, Rule 14).

## Known items
1. (Closed 2026-10-07, accepted by the publisher) Prophetic Identity Commentary Series Volumes 1–5 covers stay at the supplied 687 × 1024 px, enlarged to 1600 × 2400 and 1024 × 1536. On the site they render at about 387 css px wide (a 1.13× stretch on a 2× screen); only a 3× phone or a printed cover would show softness. Replace only if larger originals are ever generated.
2. (Closed 2026-10-07) The series name returned to Prophetic Commentary Series, so the existing covers and footers need no re-lettering.
3. (Closed 2026-10-07) Pre-1900 authors removed from Prophetic Commentary Series Volumes 1, 3, 4 and 5 (Volume 1 is now 65 pages); see the Series Standard v1.10.
4. (Mostly closed 2026-10-09) Commentary Collection hub ideas: sticky series bar with a Pricing link, pricing button, aligned tile footers and shorter tile blurbs, lighter 400×600 card images, and a notify-me mailto link (via `site.js`) are done; still open: an “Available now” row and a fit-to-screen option in the preview lightbox.
5. Prophetic Identity Commentary Series is complete (Volumes 1–5 all on the Collection page). Volumes 3 and 4 interiors were corrected for a duplicated KJV-table header row, and their preview images replaced; the previously delivered Volume 3 and 4 PDFs are superseded by the corrected files.
6. Identity Volume 1 page: Related Reading does not yet link to Volume 2 (optional).
7. CLAUDE.md: some series-standard bullets carry stale version text; tidy in one pass.
8. Built-in browser notes: the narrow-viewport screenshot sometimes tiles one image four times (a capture artifact, confirmed against the page's own element count); each page load needs a fresh access approval.
9. (Closed 2026-10-07, mechanical part) Local phone-width sweep of every root page at 390, 360 and 320 px for sideways overflow; results recorded in the 2026-10-07 audit note below. Visual and wording polish remain for the single pre-launch audit.
10. Framework §XX still says Mode 2 governs “the Prophetic Commentary Series” and points to the series Standard at v1.3; the Covenantal Commentary Series (and the Prophetic Identity series) are not named there. Claude supplies the wording and the publisher updates the Framework by his copy (Covenantal Standard v1.0, Master Standard v1.75).
11. Build toolkit: `build-tools/commentary/appg.py` is the old chapter-level static table; the verse-level “Where the Passages Are Read” index (Master Standard v1.73) is generated per volume by a script written for that volume. Fold the generator into the shared toolkit in a later tidy pass.
12. Covenantal Commentary Series: full-KJV checking is done through the publisher's built-in browser (Project Gutenberg eBook 10, parsed in the page; each page load needs a fresh access approval). This is one copy; a second independent copy for the "two copies compared" check is still to be done at the pre-launch audit. The existing `kjv_all.txt` covers only the chapters the first two series cited.
13. Covenantal Volume 1, Chapter 9 names seven modern writers (supporting: Harris, Fruchtenbaum, S. Lewis Johnson; opposing: Wright, Piper, Kline, Horton), each quoted only from a free full text read in the browser and verified quote by quote. R. C. Sproul and O. Palmer Robertson were on the publisher's list but no free full text of their words on the land could be found (the Ligonier devotional on the promised land carries no author), so neither is quoted. Add them if the publisher supplies the text.
14. Covenantal Volume 1: the Kline extract (Kingdom Prologue) was read on a third-party site that reproduces it as a block, so it is cited by section, not by page, as the series Standard requires. Check against the printed book and confirm the site's permission before launch. Horton's essay is dated 18 August 2026 and its opening is political; only its exegetical lines are quoted. Re-read all seven sources once at the audit in case a page has changed.

## 2026-10-07 phone-width sweep (local, Playwright Chromium)
All 283 root HTML pages loaded at 390, 360 and 320 px: 0 pages with sideways overflow, 0 load errors (scrollWidth equal to viewport width, and no visible element extending past it). This covers overflow only; section-by-section visual and wording polish remain for the single pre-launch audit.

## 2026-10-09 improvement pass
- Phone-width sweep re-run: all 303 root HTML pages at 390, 360 and 320 px, 0 pages with sideways overflow (local Playwright, external requests blocked).
- Social-preview audit: 272 of 303 pages (every Digital Study, the summaries, the main pages) had no og/twitter tags; 269 now carry og:title, og:description, og:url, og:image (1200×630) and twitter:card, canonicals were added to 195 pages that lacked one, and 80 study share images plus `assets/share-site-default.jpg` were made. 404 and the two redirect pages are skipped on purpose. Not yet tested on a live link-card checker (the shell cannot reach the live site).
- Notify-me link: appears under the Checkout Coming Soon buttons on pages that load `site.js` (5 study pages do not load it). It is a mailto to info@zaymariepress.com, not a form; a real list needs a mail-service account.
- Collection tile blurbs were shortened to the first sentence or two; the full text stays on each volume page. Series names were left as the Standards fix them.
- Still for the pre-launch audit: Lighthouse run on the live site; alignment and wording polish; a link-card check of a few share images.

- v1.7, 2026-10-09: improvement pass recorded in the 2026-10-09 section below.
