# The New Testament's Use of the Old Testament: Explanation Series (PAUSED)

Status: **PAUSED by the publisher, 2026-10-18.** Nothing is approved for building. This is a working note, not a rule; no controlling document, Standard or website page was changed for it. Version 1.0.

The publisher paused the project to think it through. Resume only when he says so; do not draft further entries, write a series Standard or touch the website until then.

## The goal (publisher, 2026-10-18)

"My end goal is to be able to explain why and how the NT writer is quoting the OT and explain that to the reader in its proper context."

The search database (`ot-in-nt-quotations.html`, 439 references) stays what it is: a neutral lookup. The explanations are a separate product that takes and defends positions (commentary-style, Mode 2 in method, with the Readers Question habit of arguing first from the writer's own chapter and the Old Testament passage's own setting). The 87 Digital Studies stay Mode 1 and are untouched.

## What was found

- Of the 439 references, 387 sit in passages some non-companion product treats (key, argued or reported); 52 have no treating product (clusters in Mark 10, John 6, 1 Cor 6, Matthew 5, Luke 4, 2 Cor 4, Jude, 1 Peter and the Thessalonians).
- No product asks the question "how does the New Testament writer use the Old Testament here?" Passage coverage is not coverage of that question.
- Fit Check on Matthew 1–2: **overlap (crowded)**. The famous uses (Isaiah 7:14, Micah 5:2, Hosea 11:1, Jeremiah 31:15) are already treated: Study 63, Typology Volumes 4 and 5, Study 52 and Reader Question 3-02 (Hosea 11:1 is the closest to a duplicate). A new series adds most where the reference is not already treated.
- Counts by writer (database rows): Paul 124, John (Gospel, letters, Revelation) 69, Luke and Acts 67, Matthew 62, Hebrews 54, Mark 24, Peter 23, James 10, Jude 6.

## The unit (approved by the publisher as the right shape, 2026-10-18)

One reference per unit, about 600 words, about a page and a half with the KJV table: the question; the Old Testament passage in its own setting; a KJV table (Verse / KJV text / What to observe); what the writer does; why he uses it at that point; what he is not claiming; a closing list sorting each claim by how firmly the text supports it.

## Decisions already reached

- Reader-facing wording: the words "entry", "what carries the weight", "pilot", "shape", "tag" and "mode" never appear to the reader. A unit carries its title (for example "Jude 9 and Zechariah 3:2"); in the running text use "this passage" or "reference". The closing section is headed in plain words (proposed: "What the text says, and what this book concludes"), with a one-line key under the heading and the marks explained once in a "How to read this book" section at the front of each volume. Proposed plain mark names: **Stated** (a verse says it), **Clear from the context** (the surrounding verses show it), **Our reading** (a conclusion this book draws). Not yet applied to the pilot draft.
- Pilot set of seven (Fit Check verdicts, 2026-10-18): Jude 9 / Zechariah 3:2 (clear); Jude 14–15 / Genesis 5:18–24 (fit by narrower question); 1 Cor 6:16 / Genesis 2:24 (clear); Mark 10:6–8 / Genesis 1:27, 2:24 (fit by narrower question; Study 83 reports it); 2 Cor 4:13 / Psalm 116:10 (fit by narrower question; Study 84 argues the passage); John 6:31 / Psalm 78:24, Exodus 16:15 (fit by narrower question; Typology Volume 4 reports the manna); John 6:45 / Isaiah 54:13 (clear).
- The pilot draft (about 4,700 words, with a publisher-notes section) is in `build-tools/nt-use-of-ot/explanations-pilot/` (`pilot_draft.md`, source of the `.docx`). Quoted KJV text in it was checked against the repo KJV corpus; the one paraphrase in quotation marks was corrected. It has not been read and approved by the publisher beyond the shape.

## Open questions for the publisher

1. **Depth.** Full explanation of all 439 references (about 16 volumes of about 27 references, about 260,000 words) or full depth on the roughly 150 places readers ask "why" with the rest grouped by pattern (6 to 8 volumes)? Not decided; the publisher wants to settle it after more thought.
2. **Structure.** By writer (Matthew 2 volumes; Mark and Luke 2; John's Gospel and letters 1; Acts 1; Romans 2; Corinthians 1; Galatians through the Pastoral Letters 1–2; Hebrews 2; Peter, James, Jude 1; Revelation 2) or by pattern? Not decided.
3. **Series name and form.** New commentary series (Mode 2) or a series borrowing the Readers Question entry form (Mode 3)? Not decided; needs a series Standard, a Master Standard rule and Framework wording (rule-sync rule applies) before any volume.
4. **Positions needing a ruling** (marked "needs your eye" in the pilot draft): Jude 9 (source of the dispute over Moses' body); Jude 14–15 (the saying and 1 Enoch, which Claude has not read in a free full text); Jude 14 (reliance on Deuteronomy 33:2 and Zechariah 14:5); 1 Cor 6:16 ("saith he"; a pre-law creation statement reaching Gentiles); Mark 10:6–8 (Genesis 1 and 2 as one account; Matthew 19:9 held for a separate entry); John 6:31 (source of the crowd's line); John 6:44–45 ("draw" and election, no position stated); John 6:45 (Isaiah 54:13 identified from the wording).
5. **How the database and the explanations link** (each row to its explanation, each explanation back to the full list of uses), and whether the explanations are a free resource or a priced series (Readers Question volumes are free; commentary volumes are $14.99). Not decided.

## To resume

1. Publisher says to resume and answers questions 1–3.
2. Run the Fit Check Map (`python3 -I build-tools/fit-check/fitcheck.py "<passage>"`) on the first volume's passages and state the one narrower question and verdict for each (Approval Checkpoint 1).
3. Apply the reader-facing wording decisions above to the pilot draft and send a revised review copy.
4. Only after approval of the shape, depth and structure: draft a series Standard, the Master Standard rule and the Framework wording together (rule-sync rule), then volumes one at a time under the usual checkpoints.
