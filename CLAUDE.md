# Zay-Marie Press website — instructions for Claude

This repository is the production site for zaymariepress.com. Pushing to `main` deploys automatically through Cloudflare Workers & Pages. Commit and push directly to `main`; no pull requests. The publisher is Hakeem (GitHub: 2DahardWay).

## Controlling documents (ask the publisher to attach them if not provided)

- **Framework Control Document — Acts Overlap Theology.** Governs all doctrinal content. It overrides mainstream dispensationalism.
- **Zay-Marie Press Digital Studies Master Standard (v1.13 or later).** Governs study structure, cover, PDF assembly, website package and publication.
- `Digital_Studies_Relationship_Map` (Markdown). Records each study's distinct subject and its related studies. Check a proposed topic against it before recommending or writing a new study.

## Approval checkpoints (do not skip)

1. Topic and overlap check against the relationship map and the neighbouring study PDFs.
2. Interior draft (PDF review copy).
3. Cover. The publisher generates the artwork in his own image tool. Claude removes any "Made with AI" badge, sets the typography (upper-right category, centred bold sans-serif title and subtitle, bottom "DIGITAL STUDIES SERIES"), and shows 1600×2400 and 320×480 proofs. The cover must be approved before integration.
4. Website changes. Show a rendered preview before pushing.

## Publishing a new study (Study N)

Files to add:

- `study-NN-slug.html`: copy the most recent study page (e.g. `study-42-one-baptism.html`) and replace everything inside `<main>`. Sections in order: hero (cover, eyebrow `STUDY N · DIGITAL STUDY`, title, subtitle, kicker, two copy paragraphs, buyline `$5.99 · Digital PDF · NN Pages · Checkout Coming Soon`), About This Study with "How These Studies Relate" (**at most three** related-study links, then the connection-guide link), What You'll Study (6 points), Key Scriptures (8 cards), From the Study quote, A Look Inside (4 preview pages, one of which must be the "What You Will Learn" page, never the TOC), What's Included (8 items), final buy panel, and the course bridge.
- `assets/study-NN-cover.jpg` and `assets/study-NN-cover.webp`: 1024×1536, made from the approved 1600×2400 cover.
- `assets/study-NN-page-P.jpg`: four preview pages at 1041×1347, rendered from the **final** PDF. P is the interior page number, i.e. the PDF page minus 1 for the cover.

Files to update:

- `digital-studies.html`:
  - Add the catalog card (`Study N · Digital Study`, or `Study N · Biblical Doctrine` in that section) to the correct browse section, in number order.
  - Update the counts: "Currently featuring N Digital Studies", "guide to all N studies", meta description "Explore N …", and in the Library Edition "all <N in words> studies", `<li>N Digital Studies</li>`, value = N × $5.99, and "Save $<value − 89.99> · More than 50%". The price stays $89.99 unless the publisher says otherwise.
  - Card copy varies its opening. Do not begin every card with "Trace".
- `site.js`: add `N:<pages>` to `digitalStudyPageCounts`, where pages is the complete final-PDF count including the cover.
- `sitemap.xml`: add the page URL after the previous study.
- `study-connections.html`: add a `<details class="guide-entry" id="study-NN">` entry in the right theme after its closest neighbour, add the number-index link, update the theme's study count in both places, and update "all N studies" and "Browse all N studies".
- Reciprocal link: add a link back to the new study on one related study's page, and in that study's connections entry, only if that page has fewer than three related links.

Catalog browse sections (subject, not date):

- **Foundations of Right Division**: foundational distinctions and interpretive systems.
- **Prophecy, Israel & the Covenants**: Israel's program, covenants, identity claims about Israel.
- **The Body of Christ & Grace**: the Body's calling, identity, standing.
- **Difficult Passages & Apostolic Distinctions**: single disputed passages, Acts events, commissions.
- **Biblical Doctrine**: one doctrine traced across both programs (judgments, crowns, baptism, resurrections).

The priced study-path bundles are separate from the browse sections. Do not change bundles or prices without approval.

## Verification after every push

- Fetch `origin/main` and confirm it matches the intended commit.
- Confirm there are no files at the wrong path: HTML only at the repository root, media only in `assets/`, never `assets/assets`.
- Render the new page and the catalog locally with Playwright (Chromium is preinstalled), and check that every image and link resolves.
- The live site may require a sign-in in Claude's browser; if it cannot be checked, say so and ask the publisher to confirm visually.

## Other controls

- Blue text is always the established dark navy; light blue is never used for text.
- Keep temporary experiments and rejected covers out of the repository.
- Never claim a live result that was not observed.
