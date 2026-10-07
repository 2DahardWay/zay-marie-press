# Pre-Launch Audit — Deferred Items (v1.4, 2026-10-07)

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
4. Commentary Collection hub ideas offered, not approved: an “Available now” row; price and page count on live tiles; shorter placeholder titles; a notify-me link; a fit-to-screen option in the preview lightbox.
5. Prophetic Identity Commentary Series is complete (Volumes 1–5 all on the Collection page). Volumes 3 and 4 interiors were corrected for a duplicated KJV-table header row, and their preview images replaced; the previously delivered Volume 3 and 4 PDFs are superseded by the corrected files.
6. Identity Volume 1 page: Related Reading does not yet link to Volume 2 (optional).
7. CLAUDE.md: some series-standard bullets carry stale version text; tidy in one pass.
8. Built-in browser notes: the narrow-viewport screenshot sometimes tiles one image four times (a capture artifact, confirmed against the page's own element count); each page load needs a fresh access approval.
9. (Closed 2026-10-07, mechanical part) Local phone-width sweep of every root page at 390, 360 and 320 px for sideways overflow; results recorded in the 2026-10-07 audit note below. Visual and wording polish remain for the single pre-launch audit.

## 2026-10-07 phone-width sweep (local, Playwright Chromium)
All 283 root HTML pages loaded at 390, 360 and 320 px: 0 pages with sideways overflow, 0 load errors (scrollWidth equal to viewport width, and no visible element extending past it). This covers overflow only; section-by-section visual and wording polish remain for the single pre-launch audit.
