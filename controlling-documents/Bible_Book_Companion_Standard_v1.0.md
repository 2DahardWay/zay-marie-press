# Zay-Marie Press Bible Book Companion Standard — v1.0

Status: working standard, approved piece by piece by the publisher on 2026-10-13. It replaces the Doctrinal Packet Standard (v0.4, five-page format). The Bible Book Companion Series is a separate product strand from the Digital Studies; this Standard governs companions only (Master Standard §16 and §17 govern studies).

## Name (publisher directive, 2026-10-13)
The series was called the Doctrinal Packets. On 2026-10-13 the publisher renamed it the **Bible Book Companion Series** (a single book is a **Bible Book Companion**). The name is used on the website, in the PDFs, in the controlling documents and in this folder. Earlier dated entries (Master Standard Version History, the CLAUDE.md entries, working trackers) keep the name in force when they were written. File names, URLs and CSS classes are unchanged: book pages are `packet-<slug>.html`, the hub is `doctrinal-packets.html`. The word "packet" may still appear in a URL or file name; it never appears in anything the reader sees. (An intermediate name, "Bible Companion", was in use for a few hours on 2026-10-13 and is retired.)

## 1. Purpose
A Bible Book Companion is the paid, interpretive companion to a book's free Bible Book Summary. The summary orients. The companion interprets: it gives the book's program identity, follows its movements, sets what belongs to a program apart from what holds for all people, applies the universal truths, and closes with a teaching outline and usage notes.

## 2. Product specification
- One companion per book of the Bible (66). $2.99, printable PDF, KJV only.
- Page size and margins as the Digital Studies (483.846 × 725.754 pt; margins 43.2 / 61.2 / 51.55 / 51.55 pt), Roboto only (Regular, Italic, Bold), body 10 pt black, headings 17 pt navy (#1B3350), table headers Slate Blue (#3B6E91).
- Length is whatever the eleven sections need, cover included (1 Chronicles 6 pages, Ephesians 7, Romans 6). The page count is one number everywhere: hero buyline, What's Included, buy panel, meta description.
- Naming: title "Bible Book Companion — [Book]"; a subtitle chosen per book.

## 3. Structure (publisher's template, 2026-10-13)
Interior page 1 opens with the kicker "ZAY-MARIE PRESS | BIBLE BOOK COMPANIONS", the title, the subtitle, a gold rule and a Table of Contents with real dot leaders aligned to the right edge. Then, in this order:
1. Book Overview (Program-Aware), with a boxed Program Identity statement.
2. Narrative Flow (three to seven movements).
3. Program Themes: "Prophecy-Program Themes" for Old Testament books; "Mystery-Program Themes" or "Program Themes" for New Testament books as the book requires.
4. Christ in [Book]: the prophetic trajectory (Old Testament) or fulfillment and revelation (New Testament).
5. Israel's Identity in [Book] (Old Testament); "Israel and the Body in [Book]" (New Testament, where the book addresses the question; Romans: "Israel in Romans").
6. Body-of-Christ Distinctions.
7. Program-Specific Truths Table (Israel-Specific rows for Old Testament books; Body-Specific and Israel-Specific rows as the book requires; Slate Blue header, four columns: Category, Truth, Program Identity, Scripture).
8. Universal Truths Table (All People, All Time): three columns.
9. Program-Safe Application Grid: a "Why This Section Exists" box and eight applications, each a bold lead-in and a short pastoral line. Old Testament books draw only from the universal truths. Where a book is addressed to the Body, the applications may also draw on the book's own instructions to believers, and the box says so in plain words; Israel's covenant commands or kingdom promises never become the Body's obligations.
10. Teaching Outline: five to eight movements in roman numerals with Scripture references, plain weight.
11. Companion Usage and Study Suggestions (placed last, closes the companion): three headings, each with one paragraph: How to Use This Companion in Personal Study; How to Use This Companion in Small Groups or Classes; How This Companion Fits Within the Acts Overlap Theology Series. For 1 Chronicles the paragraphs are the publisher's own text (with regular hyphens and the section name "Program-Safe Application Grid"); for other books they follow the same three-paragraph pattern, adapted to the book's program placement and approved with the book.

Bold is limited to headings, table headers, box titles and the lead-ins in section 9. Body text, item lines, the teaching outline and section 11 are regular weight.

## 3a. Governance
- Doctrine follows the Framework Control Document in full (Rules 7, 11 and 13–19 and the standing sentences). Where the program assignment manual assigns a book or passage, the companion follows it exactly. The reader-facing wording rule applies to every word the reader sees, including text in covers and preview images.
- Each companion is drafted by Claude and approved by the publisher before anything is pushed. Nothing is pushed without the publisher's explicit "i approve" after a rendered preview.
- Rollout: Ephesians, 1 Chronicles and Romans were built and published first (2026-10-13). The other 63 books keep their earlier pages until each is rebuilt in the new format, in batches approved by the publisher.

## 4. Scripture
KJV throughout. Verse text is checked against a KJV source, never quoted from memory. The cover carries no translation line (removed at the publisher's direction, 2026-10-13).

## 5. Cover and footer
- Cover is page 1: a genre photograph fades into a dark panel, deep blue for the Old Testament and deep green for the New Testament. Lettering: gold "BIBLE BOOK COMPANION SERIES", the testament line, the book title in white serif, a short gold rule, the italic subtitle, and "ZAY-MARIE PRESS" at the foot. Genre photographs: `assets/genre/packet-genre-<genre>.jpg` (gospels, history, law, letters, poetry, prophets, revelation).
- Interior footer, centered on one baseline, Roboto: "ZAY-MARIE PRESS BIBLE BOOK COMPANION SERIES • N".
- Website covers: `assets/companion-<slug>-cover.jpg` and `.webp`, 1024 × 1536.

## 6. Preview rule (publisher directive, 2026-10-13; replaces the 2026-09-29 two-view rule)
A book page shows one preview under "A Look Inside": interior page 1 (the title block, the full Table of Contents and the opening of the Book Overview and Narrative Flow), rendered whole, never cropped, from the final PDF at 1041 × 1560 px, labelled "Page 1", named `assets/companion-<slug>-page-1.jpg`, checked for working terms and approved before any push. It shows scope and method and none of the tables, applications or outline.

## 7. Website
Each book page (`packet-<slug>.html`): hero with the real cover and the buyline "$2.99 · Digital PDF · N Pages · Checkout Coming Soon"; About; Related Reading (Master Standard §18, v1.133 format; the Bible Book Companion Series list is capped at three); What You'll Study (six points); Key Scriptures; A Look Inside (§6); What's Included (eight items); buy panel. The hub is `doctrinal-packets.html` with the heading "Bible Book Companion Series". Nav and footer label: "BIBLE BOOK COMPANION SERIES". Checkout is closed; the price is $2.99 and bundles do not exist.

## 8. Build tools
`build-tools/packets/`: `build_packet.py` (cover, interior, two-pass contents page numbers, merge), `content_<book>.py` (the text), run as `python3 build_packet.py content_<book> <outdir>`. A text change is made in the content file and the PDF, previews and page are regenerated together.

## Version note
v1.0 (2026-10-13): created from the Doctrinal Packet Standard v0.4 at the publisher's direction: new name; the publisher's eleven-section structure replaces the five-page format; one-page preview; cover without the translation line; footer renamed. Sections of v0.4 that no longer apply (five pages, anchor texts, logic chain, cross-reference network, the two-view preview) stay in the repository history only.
