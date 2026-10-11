# Pauline Doctrine Series Standard

Version 1.1 — Approved by the publisher, 2026-10-11 ("i approve"); pricing ruled the same day ("same pricing as the commentary series"). Recorded in Master Standard v1.124 §20 Rule 29 and CLAUDE.md in the same pass; the Framework §XX wording is supplied to the publisher for his copy. Version 1.0 — draft, 2026-10-11. Volume theses, outlines and rulings are still to be approved one volume at a time. Nothing is on the website yet.

Governs the Pauline Doctrine Series (each title a "Volume"; the shared working term "Commentary Volume" is used for build tooling only), written in Mode 2 (canonical identity synthesis) under Framework §XX and Master Standard §20 Rule 29. Modelled on the Acts Commentary Series Standard (v1.10) and the Gospel Commentary Series Standard (v1.19) and sharing their layout, quotation and citation rules. The Digital Studies stay under Mode 1 and are never changed by this series.

## Ruled by the publisher (2026-10-11)
- **Why a topic series:** Paul's epistles do not fit a commentary series organised by letter. It would be thin, and it would collide with the Acts Commentary Series (Galatians 1–2 against Acts Volumes 3 and 4; Thessalonians against Studies 7 and 8; Ephesians and Colossians on the Mystery against Prophecy & Mystery Volume 2; Galatians 3 against Covenantal Volume 2; Romans 11 against Prophetic Identity Volume 4).
- **Shape (Option 3):** a topic-based series for the large synthesis subjects, plus individual Digital Studies (Mode 1) for the single-term gaps.
- **Name:** Pauline Doctrine Series (not "commentary").
- **Placement:** the Commentary Collection page (`commentary.html#pauline`) as the **eighth** series, outside the Digital Studies catalog, bundles and Library Edition. No separate series page. Volume slugs: `commentary-pauline-0N-<slug>.html`.
- **Order:** the five volumes first; the individual Digital Studies afterwards.

## Approved wording (2026-10-11; built from the sibling Standards)
- **Scope:** five volumes on Paul's letters, each built around one narrower question on a large synthesis subject, not a walk through a letter. Where a volume enters ground already argued in another series or in a Digital Study, it cites that work as a neighbour and does not repeat the argument.
- **Length:** 50–70 pages including the cover. **Imprint:** Zay-Marie Press. **Translation:** KJV only. **Typeface:** Roboto.
- **Price:** $14.99 per volume unless the publisher says otherwise. Series bundle $54.99; Complete Commentary Library for 40 volumes $364.99 (see Pricing).
- **Footer:** "ZAY-MARIE PRESS PAULINE DOCTRINE SERIES, VOLUME V • N" (V the volume number within the series, N the page number, restarting at 1 on the Table of Contents page).
- **Cover:** "VOLUME V" upper right, the title, and "PAULINE DOCTRINE SERIES" at the bottom; 1600 × 2400 px artwork (2:3), 1024 × 1536 px website covers (.jpg and .webp), full-bleed interior cover page. Artwork supplied by the publisher; Claude removes any badge, sets any missing lettering and shows proofs before the cover is approved.
- **Citation and sources:** passage citation (book, chapter, verse or section); modern sources only (twentieth century and later; no author from before 1900 is cited, quoted or listed in a bibliography); a page number is printed only where the text was read in full; a writer is quoted only from a free full text read, otherwise described in Claude's own words without quotation marks; verse-level index "Where the Passages Are Read" as the last appendix before the Bibliography (Master Standard §20 Rule 29).
- **Preview pages:** four, as Master Standard §20 Rule 29 (v1.81) fixes: Table of Contents, Preface, one page of the argument at work and one page of objections and replies, rendered from the final PDF at 1041 × 1560 px and labelled by interior page number; shown to the publisher and approved before any push.
- **Binding rules:** Rules 7, 11 and 13–19 bind; Rules 8, 12 and 20–28 and 30 do not. **Rule 32** (Romans 9–11 and the Romans 10:9–10 formula) binds all modes and therefore every volume. Standing sentences are carried wherever the passage is touched: Galatians 3 ("The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant."); Rule 17 (the remnant and the Body); Rule 18 (Paul's synagogue ministry); Rule 19 (ground of salvation and content of faith); the Romans 11 triad ("Participation is not identity. Blessing is not covenant. Standing is not program membership.").
- **Reader-facing text:** a volume opens with a plain statement that it argues a position. The mode label, the Framework, rule numbers and every other working term never appear in anything the reader sees (Rule 14), including text inside diagrams, covers and preview images (OCR pass).
- **Objections chapter:** the Covenantal pattern (two to four modern writers who fortify the thesis beside named modern writers who hold the opposite view, each objection in the opponent's own words, short extracts checked against a free full text, answered from Scripture, closing table).
- **Build toolkit:** `build-tools/commentary/` (build.py, content.py, kjvlib.py, kjvcheck.py, tocmap.py, mkcover.py, mk.sh). KJV text is verified from a source and checked by hash with `kjvcheck.py` before publication.

## Overlap check (2026-10-11)
A text search of the study, volume, packet and parable pages found no commentary volume or parable that treats any of the nine gaps. The full study PDFs are not in the repo, so **the first job of each volume is a closer check of the neighbouring study PDFs** before the thesis is proposed. Neighbours to cite and keep clear of:

| Subject | Existing work | What it carries |
|---|---|---|
| Adam and Christ | incidental mentions only | no study or volume is built on Romans 5:12–21 or 1 Corinthians 15:21–22, 45–49 |
| The Cross in Paul's letters | Study 53 (Redemption); Study 54 (Justification); Study 55 (Reconciled to God) | the price and bondage; the righteous verdict and its ground (Romans 4:25); enmity, reconciliation and the ambassadors' appeal |
| The Person of Christ | Study 52 (Sonship and Adoption); Study 55 (light) | the two sonships by adoption; Christ's person touched only in passing |
| The Assembly in Order | Study 72 (The Lord's Supper); Study 81 (Praying in the Spirit); Study 33 (Crowns); Doctrinal Packets on 1 Corinthians, 1 and 2 Timothy and Titus | the Supper and 1 Corinthians 10–11; the tongues and prayer passages of 1 Corinthians 12–14; Paul's letters taken as key passages in five pages |
| Liberty, Conscience and the Walk | Studies 36, 77, 78 | 1 Corinthians 10:32 and corporate standing; Romans 13:1–7; the Sabbath passages including Romans 14:5–6 and Colossians 2:16–17 |
| Romans 6–7, old man and new (Digital Study afterwards) | Studies 37, 45, 42 | new creation; the three senses of sanctification; the one baptism |
| Romans 1–3 (Digital Study afterwards) | Studies 54, 43, 35 | justification; the gospel of the grace of God; the identity labels |

**Neighbours Claude adds beyond the handoff list, to be confirmed in each volume's closer check (not yet read in full):** Prophecy & Mystery Volume 4 (1 Corinthians 15:23 read narrowly as the Body's own order) for Volume 1; Covenantal Volume 2 (Galatians 3) and Study 12 (the New Covenant's ratifying blood) for Volume 2; Prophecy & Mystery Volume 3 (Colossians 1:13) for Volume 3; Acts Commentary Volume 2 and Studies 38 and 42 (tongues, Acts as non-manual, the one baptism of Ephesians 4:5) for Volume 4; Study 44 (Walking in the Spirit) and Study 59 (the Law's jurisdiction) for Volume 5.

Closest overlaps: Volume 2 with Studies 53, 54 and 55 (three words, three studies; this volume asks about the Cross itself, not the vocabulary of its benefits); Volume 4 with Studies 72 and 81 and the three Packets; Volume 5 with Studies 36, 77 and 78. Each volume answers the narrower question below.

## The volumes (provisional titles; the publisher approves title, subtitle, thesis, outline and rulings one volume at a time)
1. **Adam and Christ** — two heads, two humanities. Romans 5:12–21; 1 Corinthians 15:21–22, 45–49. Narrower question: what does Paul say each head does for those who are in him, and how do the two passages differ in what they answer (death and righteousness in Romans; resurrection and the body in 1 Corinthians)?
2. **The Cross in Paul's Letters** — blood, propitiation, the curse, dying with Christ. Romans 3:25; Galatians 3:13; Romans 6; 2 Corinthians 5:21; Colossians 2:14–15. Narrower question: what does Paul say the Cross itself did, passage by passage, as distinct from the benefits Studies 53, 54 and 55 trace?
3. **The Person of Christ in Paul** — pre-existence, fullness, "firstborn". Philippians 2:5–11; Colossians 1:15–20; 1 Timothy 3:16; Titus 2:13. Narrower question: what does each passage say about who Christ is, before and apart from what he did?
4. **The Assembly in Order** — gifts, offices, discipline, men and women. 1 Corinthians 5, 11–14; Ephesians 4; 1 and 2 Timothy; Titus. Narrower question: what does Paul say about how the gathered Body is ordered, and what does each instruction say it rests on, apart from the Supper (Study 72) and the prayer and tongues passages (Study 81)?
5. **Liberty, Conscience and the Walk** — Romans 14–15; 1 Corinthians 8–10; Colossians 2; Galatians 5. Narrower question: what does Paul say governs the believer's conduct where there is no command, and how does he set liberty against the weaker brother's conscience?

Volumes are numbered 1–5 within the series. Each volume's thesis, outline and rulings are approved before drafting.

## Individual Digital Studies afterwards (Mode 1; would be Studies 83–86; not started and not to be started until the five volumes are done)
- **Marriage and Singleness** (1 Corinthians 7) — incidental mentions only elsewhere.
- **Suffering and Glory** (Romans 8:17–39; 2 Corinthians 4) — incidental mentions only elsewhere.
- **The Sin of the World and the Conscience** (Romans 1–3) — keep clear of Studies 54 and 43 (and 35).
- **The Old Man and the New** (Romans 6–7; Ephesians 4; Colossians 3) — needs a narrower question to stay off Studies 37 and 45 (and 42); Volume 2's treatment of Romans 6 is a further neighbour.

These are built by the Master Standard and the Digital Studies workflow, not by this Standard; each is classified by the Category Standard's decision procedure at the time.

## Drafting cautions
- Mode 2 permits argument and identification; every identification follows the Identity Synthesis Protocol. Nothing in this series is read back into a Digital Study.
- Paul's letters are addressed to the Body, but a volume that touches Romans 9–11 reads it as addressed to Israel (Rule 32); Romans 10:9–10 is not used as a Body salvation passage; Romans 11 carries the standing triad. **Romans 5:12–21** and **Romans 6** are Body passages; Israel's covenant language is not imported into them.
- Galatians 3 appears wherever touched (Volume 2 on Galatians 3:13) with the standing sentence; the seed, the Abrahamic blessing and Israel's covenants are left to Covenantal Volume 2 and cited, not restated.
- Rule 19 applies wherever faith and its content are discussed: salvation is by faith, the content is what God revealed within each program, and no shared saving ground is stated; Adam and Christ (Volume 1) and the Cross (Volume 2) are the volumes where this is most easily broken.
- Rule 18 applies wherever Paul's synagogue reasoning or his customs are mentioned; Rule 17 wherever the remnant and the Body are set side by side; Rule 11 wherever Acts 9–28 fillings or signs are touched (Volume 4).
- Volume 4 stays consistent with the Acts Commentary Series rulings on tongues (reported as written; no timing for "cease"; Acts and 1 Corinthians not reconciled by assertion) unless the publisher rules otherwise at that volume's thesis stage; the Supper and its New Covenant sentence stay with Study 72 and are cited.
- Volume 3 argues who Christ is from the passages Paul wrote and does not read later creeds back into them; no author from before 1900 is cited.
- No internal working term appears in anything the reader sees (Rule 14).

## Points for the publisher's ruling at each volume's thesis stage (questions, not decisions)
- **Volume 1:** how 1 Corinthians 15:22–23 and 15:45–49 sit beside Prophecy & Mystery Volume 4's narrow reading of 15:23 (the Body's own order); whether "all" in Romans 5:18 is argued as Paul's own scope within the passage and left there.
- **Volume 2:** how Colossians 2:14–15 and the "handwriting of ordinances" sit beside the Law's jurisdiction (Study 59); whether Galatians 3:13 is read inside Galatians 3's standing sentence only.
- **Volume 3:** how Colossians 1:15–20 and Colossians 1:13 sit beside Prophecy & Mystery Volume 3; the reading of Titus 2:13 and 1 Timothy 3:16 as the passages' own audience markers allow.
- **Volume 4:** what is said of men and women in the assembly (1 Corinthians 11, 14; 1 Timothy 2) and of offices and discipline, reported from the letters' own setting.
- **Volume 5:** how Romans 14:5–6 and Colossians 2:16–17 sit beside Study 78 (no passage addressed to the Body commands a day, as a report of the text); where the volume stops on matters of conscience that Paul leaves open.

## Pricing (ruled 2026-10-11)
$14.99 per volume, the same as the other commentary series. Series bundle $54.99 (individually $74.95; save $19.96). The Complete Commentary Library of all 40 volumes in eight series is $364.99 (individually $599.60; save $234.61, about 39%; $74.93 less than the eight series bundles), following the +$45.00 per added series pattern ($229.99, $274.99, $319.99, $364.99). The $364.99 price takes effect on the Commentary Collection page when the Pauline Doctrine Series is added to it; until then the page keeps $319.99 for 35 volumes. Prices may change; a change is made on the Collection page (series strip, bundle card, Library box and note, cover strip), in the Master Standard §20 Rule 29 pricing paragraph and in CLAUDE.md in the same pass.

## Rule-sync (done 2026-10-11)
Rule 29 amendment written into CLAUDE.md and Master Standard v1.124 (DOCX and PDF, logged in §22). The Framework §XX wording is supplied to the publisher for his copy. Website work for each volume follows the Gospel pattern: volume page, eighth series block (`#pauline`), series strip, bundle card, Library box (price $364.99 when the series is added), four preview pages, Related Reading box (v1.89), sitemap, and neighbouring study pages checked for the volume (up to three per box).

## Version history
- v1.1, 2026-10-11: approved by the publisher; pricing ruled (bundle $54.99; 40-volume Library $364.99); rule recorded in Master Standard v1.124 and CLAUDE.md.
- v1.0, 2026-10-11: series created as a draft after the handoff rulings (name, placement, order, topic-based shape); scope wording, five volumes with narrower questions, overlap table, drafting cautions and rulings-to-ask proposed by Claude for approval; pricing left unruled; no rule recorded yet.
