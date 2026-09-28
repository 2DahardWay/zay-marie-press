# Preview-Page Spoiler Retrofit Audit — Studies 1–60

Tracks the publisher-directed retrofit of the preview-page conclusion-spoiler
standard (Master Standard §17 / CLAUDE.md "Preview-page conclusion-spoiler
standard") across the 60 studies published before Study 61. Study 61 was built
compliant from the start and needs no entry here.

Version 1.2 — created 2026-09-28, updated 2026-09-28, after Study 61 published, per the publisher's
confirmed sequencing ("do this only as its own scoped, approved task... after
Study 61 is complete and published"). Bump the version and log changes here as
the audit proceeds. Mirrors the Master Standard's `_vX.Y` filename convention.
As of v1.2, both halves of the audit (website and interior PDF) have been surveyed; see the
"Interior PDF Audit (v1.2)" section below for the interior-PDF pass. No interior-PDF fixes have
been made yet — that is a separate, not-yet-scoped follow-up (see that section for why).

## The rule being audited against (verbatim from CLAUDE.md)

> Applies to every "What You Will Learn in This Study" page inside the interior
> PDF, and to the website's "What You'll Study" (6 points) section on every study
> page — both are the same preview promise in two places.
>
> - The preview page states the **skills and interpretive outcomes** the reader
>   will gain. It is a value signal, not an answer key: it must promise mastery,
>   not deliver the solution.
> - It must never reveal the identity of a figure before the study presents it,
>   give away the doctrinal conclusion, state the interpretive answer outright,
>   collapse the discovery process, or pre-empt the study's narrative arc.
> - Instead, each point describes the *process* the reader will follow, names
>   the *textual markers* they will trace, and states the *interpretive
>   discipline* they will learn.

Model (compliant) example, Study 61 point 3: "Trace the identity of the male
child in 12:5 by following the chapter's own textual markers — including the
term 'caught up' (harpazō) and the later appearance of a sealed firstfruits
company in Revelation 14:1–5."

Flagged non-example of what this replaces: "Identify the male child of 12:5 as
the 144,000…" — states the conclusion before the reader begins.

## Scope and known blocker — READ BEFORE CONTINUING (historical; resolved as of v1.2)

**Update (v1.2): this blocker is resolved.** The publisher supplied Studies 1–60's interior
production PDFs and the interior-PDF half of the audit is now complete — see "Interior PDF Audit
(v1.2)" below for the findings. The section immediately below is kept as-written for history; read
the v1.2 section for current status instead of assuming the blocker below still applies.

Each study has **two** places to check, and they are not equally reachable from
this repo:

1. **Website — "What You'll Study" (6 points)`, on each `study-NN-*.html` page.**
   Fully auditable from this repo right now. The current text for all 60 studies
   is captured verbatim in the table below so the audit can start immediately.
2. **Interior PDF — "What You Will Learn in This Study" page.**
   The finished interior PDFs/DOCX for Studies 1–60 are **not stored in this
   git repo** (this repo is the website only; sold-study source files live
   with the publisher). A repo-wide search found exactly **one exception**:
   `assets/study-45-sanctification-under-grace.docx` — an orphaned file (not
   linked from any page) that appears to be a leftover source upload. Its
   "What You Will Learn" page is NOT compliant (see Study 45's row below for
   the actual quoted text) — flag this to the publisher both as a content fix
   and to ask whether the file itself should be removed from `assets/` per the
   "keep temporary experiments... out of the repository" rule, or whether it's
   there on purpose.

   **Before the interior-PDF half of this audit can proceed, ask the publisher
   to supply the current interior PDF (or source DOCX) for each of Studies
   1–60** — or confirm a place Claude can already read them from. Do not assume
   a study's interior page matches its website wording; audit each source
   directly once available.

## Suggested sequencing

1. Work the website side first (no blocker) — go study by study in catalog
   order, judge each of the 6 points against the rule above, and mark the
   Website columns below.
2. For any non-compliant point, draft replacement wording in the Study 61
   style (process + textual marker + interpretive discipline, no named
   conclusion), show the before/after to the publisher, and only edit the live
   HTML after approval — this is a doctrinal-content change, not a mechanical
   one, so treat it like any other content edit needing sign-off even though
   CLAUDE.md's four numbered checkpoints don't name this specific task.
3. In parallel, ask the publisher for Studies 1–60's interior PDFs/DOCX.
   Once supplied, audit each "What You Will Learn" page the same way, and ask
   the publisher how they want a corrected interior page distributed (silent
   page swap in the existing PDF vs. a versioned reissue) — that decision
   hasn't been made yet and shouldn't be assumed.
4. Log progress in this file (status columns + a short changelog at the
   bottom) so the audit survives across sessions, the same way the other
   controlling documents are kept current.

## Methodology used for the website-side pass (2026-09-28)

The publisher directed strict application: any point that gives away the specific answer to a
debated or argued-for question gets rewritten into process language, even in plain doctrinal
studies with no "hidden identity" to protect. Applying that, a point was flagged as a VIOLATION
only when it stated a study's own specific, resolved exegetical or doctrinal conclusion as settled
fact (e.g. "...describes an accomplished status, not a present moral report"). Two categories were
treated as compliant and left alone even though they use confident language:

- **Boilerplate framework restatement** — recurring lines like "Prophecy and Mystery operate
  distinctly and concurrently during Acts 9–28" or "does not automatically transfer an identity."
  This is the publishing house's already-public governing framework (from the Framework Control
  Document), not a specific study's own withheld twist, so restating it doesn't spoil anything.
- **Direct textual quotation/observation** — lines that describe what a passage itself explicitly
  says (e.g. Revelation 20 explicitly separates two resurrections by a thousand years; Ezekiel 37
  explicitly names the bones "the whole house of Israel"). Quoting the text's own plain statement
  isn't revealing an inferred conclusion the reader was supposed to trace toward.

22 points across 11 studies (41, 44, 45, 46, 48, 49, 50, 51, 52, 53, 54) were rewritten under this
standard; four headings that stated a conclusion outright were also renamed. All other studies'
"What You'll Study" text was reviewed and left as-is — already process-oriented, per this standard.

## Website "What You'll Study" — current text and status

Status legend: `PENDING` (not yet judged) · `COMPLIANT` · `VIOLATION` ·
`FIXED` (edited + pushed).

### Study 1 — The Bride of Christ
File: `study-01-the-bride-of-christ.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Israel’s Covenant-Marriage Relationship.** Trace the bridal framework through Israel’s covenant history and the prophetic promises of judgment, restoration, and future faithfulness.
2. **Zion, Jerusalem &amp; the Bride.** Follow the relationship among Zion, Jerusalem, restoration, Kingdom hope, and bridal imagery from Isaiah into Revelation.
3. **The Marriage of the Lamb.** Examine Revelation 19 and 21 in their prophetic setting and consider Revelation’s own identification of the Bride/Lamb’s wife.
4. **Ephesians 5 &amp; 2 Corinthians 11.** Work carefully through the major Pauline passages used to support the traditional identification of the Church as the Bride.
5. **Analogy vs. Programmatic Identity.** Learn why genuine marriage imagery does not automatically transfer an identity, covenant, promise, or inheritance from one revealed program to another.
6. **The Acts Overlap &amp; Non-Transfer Principle.** See how Prophecy and Mystery operate concurrently during Acts 9–28 while retaining their distinct identities, promises, callings, and destinies.

### Study 2 — The Gospel of the Kingdom
File: `study-02-the-gospel-of-the-kingdom.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Kingdom Promised Before Matthew.** Establish the prophetic background of Messiah, David’s throne, Israel’s restoration, righteous government, and God’s rule among the nations.
2. **John, Jesus &amp; the Twelve.** Follow the same “at hand” Kingdom announcement through John the Baptist, Jesus Christ, and the Twelve.
3. **Israel as the Covenantal Audience.** Examine why the initial Kingdom proclamation was directed to Israel and how covenant, Messiah, and Kingdom promises identify its setting.
4. **The Prophetic Appeal After the Cross.** Use Acts 1–3 to see why Israel’s Prophecy Program continued after the resurrection rather than ending at the Cross.
5. **Paul During the Acts Overlap.** Distinguish Paul’s one Mystery apostleship from Prophecy truth he could communicate to Israel while both programs operated concurrently.
6. **Kingdom Gospel &amp; Gospel of Grace.** Compare audience, revealed content, promises, commission, and program while preserving the finished work of Christ as the saving ground.

### Study 3 — The Body of Christ and the Tribulation
File: `study-03-the-body-of-christ-and-the-tribulation.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Israel’s Future Prophetic Tribulation.** Distinguish ordinary Christian suffering from Daniel’s seventieth week, Jacob’s Trouble, the Day of the Lord, and the great Tribulation.
2. **Daniel’s People &amp; Holy City.** Examine Daniel 9:24–27 and why “thy people” and “thy holy city” establish the national and prophetic setting of the seventy weeks.
3. **The Body Is Not Appointed to Wrath.** Follow Paul’s cumulative argument in 1 Thessalonians: waiting for the Son, gathering to Christ, the Day of the Lord, and deliverance from coming wrath.
4. **The Gathering of the Body.** Work through 1 Thessalonians 4 and 2 Thessalonians 2 carefully, distinguishing explicit statements from disputed interpretive details.
5. **Rapture &amp; Prophetic Second Coming.** Compare the Body’s gathering with prophetic Second Coming passages while preserving their distinct audiences, movements, purposes, and revelatory settings.
6. **Acts Overlap &amp; Prophetic Resumption.** See how Prophecy and Mystery operate distinctly and concurrently during Acts 9–28 and why suspension at Acts 28 allows Israel’s prophetic program to resume.

### Study 4 — Israel and the Body of Christ
File: `study-04-israel-and-the-body-of-christ.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Prophecy and Mystery.** Compare what God spoke through the prophets with the Mystery kept secret and subsequently revealed through Paul.
2. **Different Origins and Identities.** Trace Israel’s covenantal-prophetic history and distinguish it from the Body’s identity as one Body in Christ.
3. **Covenantal Relationships.** Identify the named recipients of Israel’s covenants and distinguish covenant identity from benefiting through Christ’s blood.
4. **Promises, Callings, and Destinies.** Separate what God pledged, purposed, and revealed concerning Israel from the Body’s Mystery calling in Christ.
5. **The Acts 9–28 Overlap.** See how Prophecy and Mystery operated distinctly and concurrently without merging into one program.
6. **Acts 28 and Interpretive Control.** Understand why suspension is not cancellation or transfer and why Israel’s promises remain Israel’s.

### Study 5 — The Heavenly Calling
File: `study-05-the-heavenly-calling.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Calling Begins in Christ.** Establish union with the exalted Christ as the source of the Body’s position and purpose.
2. **Position and Blessings.** Examine the Body’s present position and spiritual blessings in the heavenly places in Christ.
3. **Citizenship, Hope, and Transformation.** Follow Paul’s teaching from heavenly citizenship to Christ-centered hope, gathering, and future transformation.
4. **Spiritual Conflict and Future Purpose.** See how the heavenly calling shapes present spiritual warfare and God’s display of grace and wisdom.
5. **Israel and the Body: Distinct Callings.** Preserve Israel’s prophetic, national, and Kingdom calling alongside the Body’s distinct Mystery calling.
6. **Acts 9–28 and Acts 28.** Confirm concurrent callings during the overlap and explain why suspension does not cancel or transfer Israel’s calling.

### Study 6 — The Mystery Revealed Through Paul
File: `study-06-the-mystery-revealed-through-paul.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Hidden, Then Revealed.** Define Mystery by its revelatory history rather than by ordinary usage.
2. **Prophecy and Mystery.** Compare what God spoke through the prophets with what He kept secret before revealing it through Paul.
3. **Paul’s Reception and Stewardship.** Establish Paul’s direct reception and distinctive stewardship while preserving Ephesians 3:5.
4. **The One Body in Christ.** Examine how Jew and Gentile are united in one Body without turning Israel into an enlarged Church.
5. **Hope, Position, and Purpose.** Follow the Mystery’s connection to heavenly position, Christ in you, transformation, gathering, and future purpose.
6. **Acts 9–28 and Acts 28.** Place Mystery within the overlap and distinguish its beginning at Acts 9 from Israel’s suspension at Acts 28.

### Study 7 — The Day of the Lord
File: `study-07-the-day-of-the-lord.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Day Begins in Prophecy.** Establish its prophetic vocabulary, purpose, and extended character.
2. **Judgment, Wrath, and Return.** Follow the Day through judgment to its visible climax in Christ’s return.
3. **Israel’s Restoration and Kingdom Hope.** See why judgment belongs within Israel’s prophetic future and restoration.
4. **Why Paul Teaches the Body About the Day.** Learn how a Pauline epistle can address a prophetic subject without redefining its setting.
5. **THEY and YOU.** Work through Paul’s contrast in 1 Thessalonians 5 between those overtaken by the Day and believers identified differently.
6. **The Body’s Gathering and Hope.** Keep 1 Thessalonians 4 distinct from the Day of the Lord in chapter 5.

### Study 8 — The Day of Christ
File: `study-08-the-day-of-christ.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Begin With Paul’s Own Expressions.** Let the Day-of-Christ texts establish their own emphasis before related passages are brought alongside them.
2. **Completion, Sincerity, and Rejoicing.** Examine divine completion, blamelessness, and Paul’s joy in faithful labor.
3. **Gathering, Resurrection, and Transformation.** Study the Body’s future gathering to Christ and its promised change into incorruptibility.
4. **Glorification and Presentation.** See how the Body’s future is brought to its completed, presented, and glorified end in Christ.
5. **Judgment Seat: Reward Without Condemnation.** Distinguish service, reward, and loss from any question of sin or condemnation.
6. **Day of Christ and Day of the Lord.** Keep their distinct programmatic settings clear and approach 2 Thessalonians 2 with textual restraint.

### Study 9 — The Remnant
File: `study-09-the-remnant.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Biblical Pattern of Preservation.** See how God preserves through judgment without turning every example into the same remnant category.
2. **The Remnant Within Israel.** Follow the remnant from Elijah and the prophets into Paul’s argument in Romans 11.
3. **Messiah, the Kingdom, and Believing Israel.** Distinguish believing Israel and Kingdom apostleship from the Body of Christ.
4. **The Remnant During the Acts Overlap.** Place the continuing remnant alongside the Body of Christ without merging Prophecy and Mystery.
5. **Romans 11: Preservation Without Identity Transfer.** Work through Elijah, the remnant according to grace, and the olive tree without collapsing participation into identity.
6. **Two Distinct Destinies, One Faithful God.** Preserve Israel’s prophetic future and the Body’s heavenly calling in their distinct revealed settings.

### Study 10 — Daniel’s Seventieth Week
File: `study-10-daniels-seventieth-week.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Daniel’s People, Holy City, and Prophetic Setting.** Begin where Daniel begins: Israel, Jerusalem, and the objectives God determined for them.
2. **The Seventy-Week Framework.** Establish the completed sixty-nine weeks and the one remaining seven-year week.
3. **The Unfulfilled Week and the Acts Overlap.** Keep Daniel’s future week distinct while Prophecy and Mystery operate concurrently in Acts 9–28.
4. **The Week Begins and Reaches Its Midpoint.** Follow Daniel 9:27’s explicit markers for the covenant, sacrifice, offering, and midpoint.
5. **The Great Tribulation: The Final Half.** Distinguish the complete seven-year week from the latter period Jesus associates with the abomination.
6. **Israel, Preservation, and the Coming King.** Trace judgment, preservation, Messiah’s appearing, and the earthly Kingdom promised to Israel.

### Study 11 — The Beginning of the Body of Christ
File: `study-11-the-beginning-of-the-body-of-christ.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Question Scripture Must Answer.** Identify the Church which is Christ’s Body before deciding when it began historically.
2. **Pentecost in Its Prophetic Setting.** Read Acts 2 through Joel, Israel, David, and the promised Kingdom.
3. **Ekklesia Does Not Determine Identity.** See why an assembly word alone cannot establish program identity.
4. **Acts 9 and the Historical Beginning.** Follow Paul’s calling and the historical beginning of the Mystery Program.
5. **The Mystery Unfolded Through Paul.** Distinguish the Body’s historical beginning from the progressive unfolding of Body doctrine.
6. **Distinct and Concurrent Programs.** Keep the Prophecy and Mystery programs distinct throughout the Acts 9–28 overlap.

### Study 12 — The New Covenant
File: `study-12-the-new-covenant.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Covenant Story Before Jeremiah.** Set the New Covenant alongside the Abrahamic, Mosaic, and Davidic covenants without collapsing their functions.
2. **Israel’s Covenant Failure.** See why Israel’s history exposes the need for God’s transforming work within His covenant people.
3. **The Promise of Jeremiah 31.** Identify Israel and Judah as the named parties and follow the covenant’s promised provisions.
4. **Ezekiel’s Restoration Vision.** Examine cleansing, a new heart, the Spirit within, regathering, and restoration to the land.
5. **Christ’s Finished Work.** Understand the covenant’s redemptive basis without changing its covenant recipients.
6. **Israel’s Future Covenant Fulfillment.** Read Romans 11 and the Acts Overlap while preserving Israel’s future restoration and the Body’s distinct Mystery blessings.

### Study 13 — The Olive Tree and the Body of Christ
File: `study-13-the-olive-tree-and-the-body-of-christ.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Israel Has Not Been Cast Away.** Begin where Paul begins: God has not abandoned His people Israel.
2. **The Patriarchal Root.** Identify the Abrahamic source of prophetic blessing and privilege that supports the branches.
3. **Natural and Wild Branches.** Distinguish Israel’s natural relationship to the root from Gentile participation among the branches.
4. **Grafting and Standing.** See why breaking off and grafting in change standing without changing the branch’s identity.
5. **Israel’s Future Remains.** Read partial blindness, future reception, and the gifts and calling of God in their immediate context.
6. **The Olive Tree and the One Body.** Keep Romans 11’s prophetic participation distinct from the Mystery identity Paul explains in Ephesians 2.

### Study 14 — Acts 9 and the Beginning of Mystery
File: `study-14-acts-9-and-the-beginning-of-mystery.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Acts 1-8 Before Saul’s Calling.** Establish Israel’s Prophecy and Kingdom setting before the Mystery begins with Paul.
2. **Saul and the Damascus Road.** See the risen Christ confront and independently call Saul from heaven.
3. **What Begins at Acts 9.** Identify Paul’s distinctive apostleship, the Mystery Program, and its new revelatory stewardship.
4. **What Continues After Acts 9.** Follow Peter, Jerusalem, signs, Jewish audiences, and Kingdom testimony through the overlap.
5. **Distinct Apostolic Lines.** Keep Paul’s Mystery apostleship and Peter’s Kingdom apostleship distinct while they operate concurrently.
6. **Acts 28 and Suspension.** Recognize the later national judicial suspension point of Prophecy while Mystery continues beyond Acts.

### Study 15 — Faith and Works in James and Paul
File: `study-15-faith-and-works-in-james-and-paul.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **James’s Stated Audience.** Begin with the twelve tribes and the letter’s Israel-oriented covenantal setting.
2. **Dead Faith.** Examine James’s concern with a profession that remains barren and unexpressed.
3. **Abraham and Rahab.** Follow the examples James uses to describe living faith acting in response to God’s word.
4. **Paul’s Justification Teaching.** Read Romans, Galatians, and Ephesians on justification apart from works.
5. **Different Revelatory Settings.** Compare audience, authority, covenant setting, and the role of works without flattening either writer.
6. **One Finished Work of Christ.** Preserve distinct administrative expressions without creating independent redemptive accomplishments.

### Study 16 — The Believer's Identity in Christ
File: `study-16-the-believers-identity-in-christ.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Union With Christ.** Establish the believer’s God-given position in Christ’s death, life, and resurrection.
2. **A New Creation.** Distinguish the new identity God has established from former patterns and present experience.
3. **One Body Under One Head.** Understand belonging, function, unity, and responsibility under Christ the Head.
4. **Accepted and Complete.** Separate a complete standing in Christ from the ongoing work of spiritual maturity.
5. **Sealed by the Spirit.** Ground assurance in God’s ownership, promise, and present indwelling ministry.
6. **Position, Identity, and Walk.** Learn Paul’s order: divine accomplishment establishes identity, and identity governs conduct.

### Study 17 — The Abrahamic Covenant
File: `study-17-the-abrahamic-covenant.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Promise of Genesis 12.** Establish the covenant’s original promises of nation, land, descendants, and blessing.
2. **God’s Ratification in Genesis 15.** Examine the covenant scene in which God alone passes between the pieces.
3. **Nation, Land, Seed, and Blessing.** Keep the covenant’s coordinated dimensions clear without reducing them to one idea.
4. **The Covenant Line.** Follow Scripture’s own sequence: Abraham, Isaac, Jacob/Israel, the tribes, and the nation.
5. **Abrahamic and Mosaic Covenants.** Distinguish foundational promise from Sinai’s stipulations, blessings, curses, and sanctions.
6. **Covenant Identity During the Overlap.** Preserve Israel’s covenantal identity while recognizing the Body’s distinct Mystery calling.

### Study 18 — Peter and Paul: Distinct Apostolic Commissions
File: `study-18-peter-and-paul-distinct-apostolic-commissions.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Peter and the Twelve.** Examine Peter’s place among the Twelve and the Kingdom purpose entrusted to Israel’s apostles.
2. **Paul’s Distinct Calling.** Follow Paul’s calling by the risen Christ at Acts 9 and the Mystery revealed through him concerning the Body of Christ.
3. **Distinction Without Opposition.** See why distinct commissions do not place Peter and Paul in rivalry or deny their shared faithfulness to the same Lord.
4. **Galatians 2: Recognition Without Absorption.** Study the recognition of their ministries without making either apostleship an extension of the other.
5. **The Acts Overlap.** Identify how Prophecy and Mystery operate distinctly and concurrently during Acts 9–28.
6. **Acts 28 and the Suspension of Prophecy.** Understand the Acts 28 boundary: Prophecy is suspended while Mystery continues.

### Study 19 — The Jerusalem Council
File: `study-19-the-jerusalem-council.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Circumcision and Law Controversy.** Identify the precise demand that brought Paul and Barnabas to Jerusalem and why it required an answer.
2. **Peter’s Testimony.** Trace what Peter established about God’s acceptance of Gentiles apart from the Mosaic yoke.
3. **Paul and Barnabas’s Ministry.** See why their report presents a Gentile ministry already underway rather than one created by Jerusalem.
4. **James, Amos 9, and Prophecy.** Read James’s appeal in its prophetic setting without making the Mystery the fulfillment of Amos.
5. **The Jerusalem Decree.** Understand the practical instructions given to Gentile believers without treating them as Israel’s Mosaic administration.
6. **Recognition Without Absorption.** Learn how fellowship and practical agreement can remain genuine while distinct ministries retain their revealed purposes.

### Study 20 — Understanding Acts 2:38
File: `study-20-understanding-acts-2-38.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Pentecost and Prophecy.** See how Joel, David, the outpoured Spirit, and Israel’s Messiah establish the prophetic setting of Acts 2.
2. **Peter’s Audience.** Trace Peter’s direct address to Israel and the indictment that gives rise to the question in Acts 2:37.
3. **Repent and Be Baptized.** Examine Peter’s explicit commands without reducing water baptism to an optional afterthought.
4. **Remission and the Spirit.** Follow the remission and Holy Ghost language within the Pentecostal promise Peter has just explained.
5. **Acts 3 as a Companion.** Use Peter’s later call to repentance, restoration, and the prophets to clarify the setting of Acts 2:38.
6. **Water and Spirit Baptism.** Distinguish Peter’s commanded water baptism from Spirit incorporation into the one Body revealed through Paul.

### Study 21 — Israel’s Judicial Blinding
File: `study-21-israels-judicial-blinding.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Isaiah 6 and Judicial Hardening.** Begin with the prophetic vocabulary of seeing, hearing, resistance, and covenant responsibility.
2. **The Gospels and Recurring Resistance.** Read each use of Isaiah’s language in its own narrative setting without treating every citation as the final boundary.
3. **Romans 11: Partial and Bounded.** See why Paul’s “in part” and “until” language preserves both the reality and the limits of the judgment.
4. **The Believing Remnant.** Distinguish Israel’s national condition from the Jewish believers who remain according to the election of grace.
5. **Acts 28: The Judicial Boundary.** Examine Paul’s final recorded Israelward appeal and the Isaiah pronouncement at Rome.
6. **What Is Suspended and What Remains True.** Identify the suspension of Israel’s active national Prophecy administration while retaining covenant promises and future restoration.

### Study 22 — Prayer Under Grace
File: `study-22-prayer-under-grace.html` · **Website status: FIXED (2026-09-28) — see note below; was showing Study 21's content, now rewritten and confirmed compliant** · **Interior PDF status: PENDING (source not available in repo)**

Text below is what's now live (the old text was Study 21's, see the bug note further down):

1. **Prayer Across Scripture.** Trace prayer's presence across the Old Testament, the Gospels, and Acts, and ask which audience and setting each recorded promise actually addresses.
2. **Kingdom Prayer Promises in Their Setting.** Read Christ's upper-room prayer promises to His disciples in their own setting, before asking what a later audience may rightly claim from them.
3. **Acts 9 and the Acts Overlap.** Locate Paul's calling at Acts 9 alongside Israel's continuing Prophecy administration, and test what each program's own Scriptures establish about prayer.
4. **Paul's Commands for Prayer.** Examine Paul's own commands for prayer — what he directs the Body of Christ to bring to God, and on what ground he grounds the instruction.
5. **Requests, Peace, and the Spirit's Help.** Trace Philippians 4's pattern of request and thanksgiving alongside Romans 8's description of the Spirit's own intercession, and test what each actually promises.
6. **Sufficient Grace When Circumstances Remain.** Follow Paul's own thorn in 2 Corinthians 12 to identify what "sufficient grace" answers, and what it leaves unchanged.

Also rebuilt: Key Scriptures (8 cards, now actual prayer passages), What's Included (removed Israel/hardening-content items), and two mismatched preview-image alt texts.

### Study 23 — The 144,000
File: `study-23-the-144000.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Revelation’s Israelite Identification.** Start with Revelation 7:4, where the sealed company is identified in explicit Israelite and tribal language.
2. **Twelve Thousand From Twelve Tribes.** Follow the numbered tribal list and see why the text establishes a particular company, not an undefined symbol.
3. **The Seal and Its Prophetic Function.** Examine how the seal marks God’s servants before the further judgments described in Revelation proceed.
4. **The 144,000 and Israel’s Remnant.** Distinguish this selected company from the broader collective believing remnant within Israel.
5. **The Great Multitude as a Distinct Company.** Compare Revelation’s separate descriptions so that the great multitude is not assigned the 144,000’s identity.
6. **Revelation 14 and the Lamb on Mount Sion.** Trace the same numbered company as Revelation describes their worship, loyalty, firstfruits, and faultlessness.

### Study 24 — The Willful Sin Warning
File: `study-24-the-willful-sin-warning.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Begin Before Verse 26.** Follow Hebrews 10:19–25 to see why the warning begins with “For” and how it relates to holding fast rather than drawing back.
2. **What “Sin Wilfully” Describes.** Examine the threefold description in Hebrews 10:29 to distinguish deliberate apostasy from every conscious act of sin.
3. **No More Sacrifice for Sins.** Trace Hebrews’ once-for-all sacrifice argument and see why rejecting Christ leaves no alternate sacrificial provision.
4. **Moses, Judgment, and Covenant Responsibility.** Study Hebrews 10:28–31 alongside Deuteronomy 32 to identify the judicial and covenantal force of the warning.
5. **Hebrews’ Unified Warning Pattern.** Compare the warning passages throughout Hebrews and identify their recurring concern: rejecting God’s revealed provision.
6. **Hebrews and the Body of Christ.** Read Hebrews in its covenant and Prophecy setting while recognizing the secure standing revealed through Paul for the Body of Christ.

### Study 25 — The Signs That Followed
File: `study-25-the-signs-that-followed.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Read the Whole Commission.** Follow Mark 16:15–20 as one unit: commission, response, signs, mission, and confirmation.
2. **Belief, Baptism, and Salvation.** Examine why belief and water baptism stand together in the positive response of this Kingdom commission.
3. **The Purpose of the Signs.** See how Mark 16:20 explains casting out devils, tongues, protection, and healing as confirmation of the preached word.
4. **Signs in Early Acts.** Trace the Kingdom-apostolic witness through Acts 2–5, where signs accompany Peter’s proclamation to Israel.
5. **Signs During the Acts Overlap.** Understand why signs continue during Acts 9–28 while Prophecy and Mystery operate distinctly and concurrently.
6. **Paul’s Distinct Apostleship.** Distinguish Paul’s signs and direct calling from the Kingdom commission given to the Twelve.

### Study 26 — The Seven Churches of Revelation
File: `study-26-the-seven-churches-of-revelation.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Revelation’s Prophetic Setting.** Identify the audience, genre, kingdom language, coming judgment, and prophetic markers supplied by Revelation itself.
2. **Seven Historical Assemblies.** Examine the named cities and the real conditions Christ commends, exposes, corrects, and judges.
3. **Ekklesia and Identity.** Learn why the Greek word for assembly does not independently establish Body-of-Christ identity.
4. **Christ Among the Lampstands.** Interpret the lampstands, stars, and angels within Christ’s authority over the seven assemblies.
5. **Overcoming and Reward.** Trace repentance, endurance, promised rewards, and their connections with Revelation’s later chapters.
6. **The Church-Ages Theory.** Evaluate the seven-age interpretation without presenting a disputed historical construction as explicit Scripture.

### Study 27 — Israel’s Seven Appointed Feasts
File: `study-27-israels-seven-appointed-feasts.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Appointed Times.** Read Leviticus 23 as Israel’s covenant calendar and distinguish the weekly Sabbath from the seven annual observances.
2. **Spring Observances.** Examine Passover, Unleavened Bread, Firstfruits, and Weeks in their historical and agricultural settings.
3. **Seventh-Month Feasts.** Study Trumpets, the Day of Atonement, and Tabernacles with their commands, sacrifices, and national meaning.
4. **Explicit Fulfillment.** Trace the apostolic identification of Christ as our Passover and the Firstfruits of resurrection.
5. **Prophecy and Inference.** Separate explicit fulfillment from responsible inference, disputed calendar schemes, and unsupported date setting.
6. **The Body of Christ.** Explain why Pentecost belongs to Prophecy and why Israel’s feast calendar does not govern the Body.

### Study 28 — The Warning of Hebrews 6:4–6
File: `study-28-the-warning-of-hebrews-6-4-6.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Hebrews’ Audience.** Locate the warning within the book’s Israelite, covenantal, priestly, and prophetic setting.
2. **Dullness and Maturity.** Connect Hebrews 5:11–6:3 to the warning and the summons to go on unto perfection.
3. **Privileged Experience.** Examine enlightened, tasted, partakers, the good word, and powers of the coming age without weakening their force.
4. **Falling Away.** Define apostasy from the passage’s language of repudiation, public shame, and renewed repentance.
5. **Land and Fruit.** Use the rain, fruit, thorns, rejection, and burning illustration as the inspired explanation of the warning.
6. **Assignment Control.** Preserve the warning’s covenant force without making it govern the Body’s Pauline standing.

### Study 29 — One Taken and the Other Left
File: `study-29-one-taken-and-the-other-left.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Prophetic Setting.** Locate Matthew 24 within Israel’s Tribulation, Second Coming, and Kingdom framework.
2. **The Days of Noah.** Identify who was overtaken by the Flood and who remained under divine preservation.
3. **Noah and Lot.** Use Luke’s double comparison to trace ordinary life, sudden destruction, and deliverance.
4. **“Where, Lord?”.** Examine Christ’s answer concerning the body and gathered eagles as destination language.
5. **Kingdom Separation.** Compare Matthew 13 and 25 without forcing every prophetic judgment into one mechanism.
6. **Pauline Distinction.** Keep Christ’s earthly appearing distinct from the Body’s heavenly gathering revealed through Paul.

### Study 30 — Seated With Christ in Heavenly Places
File: `study-30-seated-with-christ-in-heavenly-places.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Christ Above Every Authority.** Begin with the exalted Head before interpreting the Body’s seated position.
2. **Made Alive, Raised, and Seated.** Follow Paul’s threefold grace progression in Ephesians 2:4–7.
3. **In Christ Jesus.** Let union with Christ govern the meaning and boundaries of the doctrine.
4. **Head and Body.** Preserve genuine union without confusing identity, rank, or headship.
5. **Principalities and Powers.** Distinguish divine display through the Church from present jurisdiction over spiritual beings.
6. **Position and Future Function.** Separate present standing from manifestation, service, inheritance, reward, judging, and reigning.

### Study 31 — The Judgments of Scripture
File: `study-31-the-judgments-of-scripture.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Subject.** Identify who or what is being judged before drawing conclusions from the passage.
2. **Timing.** Place each judgment within its stated historical, prophetic, or Mystery setting.
3. **Standard.** Determine the revealed measure by which the judgment is administered.
4. **Purpose.** Ask what God accomplishes through the judgment in its own context.
5. **Outcome.** Trace the sentence, reward, loss, discipline, exclusion, or final state that follows.
6. **Programmatic Setting.** Keep Prophecy and Mystery distinct wherever Scripture assigns different subjects and purposes.

### Study 32 — Covenant Theology and Dispensational Theology
File: `study-32-covenant-theology-and-dispensational-theology.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Biblical Unity.** Identify what each framework believes holds the canon together as one revelation.
2. **Covenants.** Compare theological covenant structures with the biblical covenants and their stated recipients.
3. **Israel and the Church.** Examine whether the two are identified, organically continuous, distinguishable, or programmatically distinct.
4. **Promise and Fulfillment.** Ask whether later fulfillment preserves the wording, recipient, and terms of earlier promises.
5. **Kingdom and Prophecy.** Compare present, future, earthly, heavenly, christological, and typological claims.
6. **Paul and Acts.** Evaluate progressive revelation, Paul’s stewardship, Acts chronology, and the Acts 9–28 overlap.

### Study 33 — The Crowns of Scripture
File: `study-33-the-crowns-of-scripture.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Language and Context.** Distinguish <em>stephanos</em>, <em>diadema</em>, metaphorical reward, and symbolic crown imagery.
2. **Recipients.** Identify whether Paul, members of the Body, elders, overcomers, heavenly elders, or Christ is in view.
3. **Basis and Condition.** Trace discipline, ministry fruit, faithful completion, endurance, shepherding, and overcoming.
4. **Timing.** Compare Christ’s appearing, the Judgment Seat of Christ, death, approval, Kingdom expectation, and throne visions.
5. **Purpose.** Separate reward, joy, honor, vindication, delegated authority, worship, and royal supremacy.
6. **Programmatic Setting.** Preserve Pauline Mystery passages and prophetic crown promises without unauthorized transfer.

### Study 34 — Filled Again
File: `study-34-filled-again.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Prophetic Promise.** Trace the promised outpouring behind Pentecost without importing later Pauline doctrine into the prophetic setting.
2. **Receiving and Filling.** Separate receiving the Spirit from renewed enablement for a named act of witness or service.
3. **Fullness as Character.** Recognize when “full of the Holy Spirit” describes an abiding qualification or spiritual characterization.
4. **Identification and Sealing.** Distinguish Spirit baptism, indwelling, and Pauline sealing from narrative manifestations in Acts.
5. **Signs During the Overlap.** Place tongues, visions, and apostolic signs within their immediate setting and assigned apostolic line.
6. **Present Application.** Read Ephesians 5:18 as an ongoing command for a Spirit-governed walk grounded in the Body’s accomplished standing.

### Study 35 — Who Is the Israel of God?
File: `study-35-who-is-the-israel-of-god.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Biblical Names.** Separate Scripture’s own expressions from later theological labels that can quietly assume the conclusion.
2. **The Galatian Argument.** Trace circumcision, new creation, apostolic spheres, and the rule governing Galatians 6:15–16.
3. **The Israel of God.** Evaluate the grammar and context without presuming that Paul renamed the Body as Israel.
4. **A Jew Inwardly.** Read Romans 2 within Paul’s direct address to the Jew, then use Romans 3:1 as the immediate control.
5. **The Faithful Remnant.** Recognize believing Israelites within Israel without turning every believer of every nation into Israel.
6. **Identity and Blessing.** Distinguish Gentile participation in spiritual blessing from transfer of covenant or corporate identity.

### Study 36 — Jews, Gentiles, and the Church of God
File: `study-36-jews-gentiles-and-the-church-of-god.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Immediate Context.** Place 1 Corinthians 10:32 within Paul’s teaching on liberty, conscience, idolatry, edification, and avoiding needless offense.
2. **Jews and Gentiles.** Define Israel’s continuing historical category and the nations outside Israel without making natural origin a basis of spiritual rank.
3. **The Church of God.** Identify the called corporate people addressed in Paul’s Mystery apostleship and their unity as one Body in Christ.
4. **Origin and Standing.** Distinguish Jewish or Gentile background from the believer’s new corporate standing without denying either truth.
5. **Equality Without Erasure.** Read Galatians 3 and Ephesians 2 without turning equal standing into the disappearance of every historical or programmatic distinction.
6. **The Acts Overlap.** Place the threefold identity within the concurrent Prophecy and Mystery programs and the distinct apostolic lines of Peter and Paul.

### Study 37 — What Does Paul Mean by “New Creation”?
File: `study-37-what-does-paul-mean-by-new-creation.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Paul’s Actual Language.** Begin with “new creature” and “new creation” in 2 Corinthians 5:17 and Galatians 6:15 before importing broader theological assumptions.
2. **In Christ.** Read new creation within union with Christ, reconciliation, changed standing, and God’s accomplished work.
3. **The One New Man.** Relate personal standing to the corporate creation of Jews and Gentiles in one Body without transferring either group into Israel.
4. **Continuing Renewal.** Distinguish the decisive creative act from the believer’s ongoing renewal in knowledge, thought, and conduct.
5. **Present and Future.** Hold present new-creation standing together with mortal weakness and the future glorification of the body.
6. **Programmatic Boundaries.** Compare Israel’s prophetic renewal and the Body’s Pauline new creation without assuming identity transfer.

### Study 38 — Why Acts Is Not a Universal Experience Manual
File: `study-38-why-acts-is-not-a-universal-experience-manual.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Description and Command.** Ask what Luke records and whether the passage gives its audience a repeatable instruction.
2. **Acts Overlap.** Follow Israel’s continuing Prophecy Program alongside the Mystery Program begun with Paul in Acts 9.
3. **Audience and Commission.** Keep Peter’s commission to Israel and Paul’s commission to the Body distinct even when their ministries appear in the same book.
4. **Signs and the Spirit.** Test tongues, healing, repeated filling, and Spirit reception against each event’s stated purpose and context.
5. **Paul’s Participation.** Read Paul’s visits, vows, and temple actions as history before assigning a present obligation.
6. **Present Doctrine.** Check proposed obligations against the instruction given to the Body through Paul.

### Study 39 — The Church’s Relationship to Israel’s Scriptures
File: `study-39-the-churchs-relationship-to-israels-scriptures.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **All Scripture Is Profitable.** Read Romans 15:4, 1 Corinthians 10, and 2 Timothy 3 for the particular benefits Paul draws from earlier writings.
2. **Original Audience and Genre.** Identify the people, covenant setting, literary form, and stated claim before moving to present application.
3. **Law and National Promise.** Examine Sabbath observance and Deuteronomy’s national blessings without assigning their covenant terms to the Body.
4. **Poetry and Prophetic Hope.** Learn from Psalm 23 and Jeremiah’s letter while respecting David’s voice and Judah’s promised return.
5. **Paul’s Use of Abraham.** Follow Romans 4 and Galatians 3 where Paul draws a point about faith and blessing from Genesis.
6. **Responsible Application.** State an original claim, valid lesson, governing present instruction, and excluded identity or promise transfer.

### Study 40 — Who Is Abraham’s Seed?
File: `study-40-who-is-abrahams-seed.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Genesis and the Selected Line.** Distinguish Abraham’s descendants, Isaac’s line, national promises, and blessing to the nations before tracing Paul’s citations.
2. **Romans 4 and Faith.** See why righteousness reckoned before circumcision matters for Abraham’s fatherhood and Gentile inclusion.
3. **Romans 9 and Promise.** Examine Isaac and Jacob within Paul’s account of Israel and God’s faithfulness to His word.
4. **Christ the Seed.** Read Galatians 3:16 in its argument without forcing a singular referent onto every use of “seed” in Genesis.
5. **Believers as Heirs.** Trace faith, the Spirit, adoption, and inheritance in Galatians 3–4 through belonging to Christ.
6. **The Circumcision Test.** Compare its historical place in Romans 4 with Paul’s refusal to make it a condition of Gentile standing in Galatians 5.

### Study 41 — Kingdom of God or Kingdom of Heaven?
File: `study-41-kingdom-of-god-or-kingdom-of-heaven.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **Where Each Phrase Appears.** See why “kingdom of heaven” is unique to Matthew and how often Matthew also says “kingdom of God.”
2. **One Kingdom, Two Names.** Compare the Synoptic parallels and Matthew 19:23–24, and test whether the two phrases name one kingdom or two.
3. **Daniel’s Kingdom From Heaven.** Trace Daniel’s own use of “of heaven” and test what it names — a location, or a source and authority.
4. **The Kingdom Promised to Israel.** Identify David’s throne, the house of Jacob, and the earthly kingdom still expected in Acts 1:6.
5. **God’s Universal Reign.** Distinguish God’s everlasting rule over all things from the particular kingdom promised to Israel.
6. **Paul’s Heavenly Kingdom.** Classify kingdom language during the Acts Overlap and read Paul’s “heavenly kingdom” within the Body’s heavenly calling.

### Study 42 — One Baptism
File: `study-42-one-baptism.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **What “Baptize” Means.** See why baptism means identification, including baptisms in which no water touches anyone.
2. **Water in Israel’s Program.** Trace priestly washing, the prophets’ promised cleansing, and John’s stated purpose for his baptism.
3. **Every Baptism in Acts.** Classify each recorded water baptism by audience, administrator, order, and stated purpose.
4. **The Difficult Texts.** Work through Acts 22:16, Acts 19:1–7, and Peter’s own comment on Cornelius in Acts 11:16.
5. **Not Sent to Baptize.** Read 1 Corinthians 1:13–17, and see why Paul baptized a few during the overlap without making it part of his commission.
6. **The One Baptism.** Follow 1 Corinthians 12:13, Galatians 3:27, Romans 6, and Colossians 2 to Ephesians 4:5.

### Study 43 — The Gospel of the Grace of God
File: `study-43-the-gospel-of-the-grace-of-god.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Names Paul Gives It.** See what “the gospel of God,” “the gospel of Christ,” “the gospel of the grace of God,” and “my gospel” each identify.
2. **Grace as Its Character.** Define grace by contrast with debt, and see why it excludes every earned addition.
3. **Its Content: 1 Corinthians 15.** State the three facts Paul names as of first importance: died, buried, rose again.
4. **Its Ground: Romans 3:21–26.** See how God is both just and the justifier through the propitiation in Christ’s blood.
5. **Its Audience and Its Faith.** Read why the gospel is addressed to all on the same terms, and what faith alone receives.
6. **The Gospel and the Mystery.** Relate the gospel to the Mystery revealed through Paul without merging the two.

### Study 44 — Walking in the Spirit
File: `study-44-walking-in-the-spirit.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **Two Natures in Conflict.** See what it means to walk by the Spirit, and why the flesh and Spirit are genuinely opposed within the believer.
2. **Whose Ministry This Is.** Distinguish the Body's settled ministry of the Spirit from Israel's Acts-era signs, wonders, and repeated fillings.
3. **The Works of the Flesh.** Read Galatians 5:19–21's list on its own terms, and test whether it describes a habitual life pattern or an isolated lapse.
4. **The Fruit of the Spirit.** Trace why Paul writes “fruit,” singular, and test what that grammar implies about how it comes about.
5. **No Condemnation.** Ground the daily walk in Romans 8:1's settled legal fact rather than making the walk the basis of acceptance.
6. **Debtors to the Spirit.** Follow Romans 8:12–14 to the identity the Spirit-led walk confirms: sons of God, not servants under wages.

### Study 45 — Sanctification Under Grace
File: `study-45-sanctification-under-grace.html` · **Website status: FIXED (2026-09-28) — 4 of 6 points rewritten to remove stated conclusions** · **Interior PDF status: SOURCE WAS FOUND at `assets/study-45-sanctification-under-grace.docx` (orphaned, not linked from any page) — REVIEWED, NOT COMPLIANT, but that file has since been removed from the repo per the publisher's instruction (see changelog); the interior PDF itself still needs the publisher's current source to fix**

**Interior PDF "What You Will Learn in This Study" page, quoted verbatim from the DOCX — every bullet states the conclusion outright:**

> What "sanctify" actually means in Scripture — set apart to God — and why that is a wider category than "made morally better." Why 1 Corinthians 1:2 and 1:30 call believers "sanctified" and "saints" as an already-accomplished fact, before any instruction to grow. What 1 Thessalonians 4:3–7 commands as God's will for the believer's conduct, and how that command rests on the position already given. What Romans 6 means when it says the believer's present fruit is "unto holiness" (6:19, 22) — a result, not a repeated achievement of standing. How 2 Corinthians 3:18 describes ongoing transformation "from glory to glory" by the Spirit — a third, distinct sense of sanctification. Why Israel's holiness under the Law (Leviticus 20:7–8) is not the Body's sanctification under grace, under the Acts Overlap framework. Why 2 Corinthians 3:18's ongoing transformation is not a claim to sinless perfection, and what 1 John 1:8–10 says about a believer who claims to have no sin. Why this is not a study of the believer's identity as a whole (Study 16) or of the flesh-and-Spirit walk (Study 44), and how those studies connect to this one.

This is the clearest concrete non-example found so far: every point states what a passage *means* or *commands* as settled fact, rather than naming the process/markers the reader will trace. Treat this as the first confirmed interior-PDF VIOLATION once the publisher confirms this DOCX is the live source (or supplies the current one).

Now live (points 2, 3, 4, 5 rewritten; 1 and 6 were already compliant):

1. **Three Distinct Senses.** Distinguish positional, practical, and progressive sanctification by the grammar Paul actually uses for each.
2. **Already Sanctified in Christ.** Trace what 1 Corinthians 1:2 and 6:11 call believers, and test whether the description is an accomplished status or a present moral report.
3. **God's Will Is Your Sanctification.** Read 1 Thessalonians 4:3–7's concrete, commanded conduct, and test what standing it assumes the reader already has.
4. **Fruit Unto Holiness.** Trace Romans 6:19, 22's picture of holiness, and test whether it names an outcome or a re-earned status.
5. **Beholding and Being Changed.** Trace 2 Corinthians 3:18's "are changed," and test whether the verb points to the Spirit's ongoing work or the believer's self-effort.
6. **Israel's Holiness, the Body's Grace.** Distinguish Leviticus 20:7–8's covenant holiness from the Body's sanctification under grace.

### Study 46 — Secure in Christ
File: `study-46-secure-in-christ.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **What Grounds the Believer's Acceptance.** Test whether the believer’s acceptance in Ephesians 1:6 rests on Christ’s work or on ongoing performance.
2. **Sealed Unto the Day of Redemption.** Read Ephesians 1:13–14 and 4:30’s stated terminus for the Spirit’s seal of ownership.
3. **The Earnest of the Spirit.** Examine what kind of guarantee an earnest actually is, and what Ephesians 1:14 says it obligates God to deliver.
4. **An Unbroken Chain.** Trace Romans 8:28–39’s chain of God’s own verbs, and its list of what cannot separate.
5. **Kept by His Faithfulness.** Read 2 Timothy 2:11–13’s distinction between a denied reward and God’s own unchanging character.
6. **Reward Lost, Standing Kept.** Follow 1 Corinthians 3:11–15’s tested work, and Paul’s verdict on the worker himself.

### Study 47 — Giving Under Grace
File: `study-47-giving-under-grace.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Macedonian Pattern.** See how 2 Corinthians 8:1–5 grounds giving in first yielding oneself to the Lord.
2. **A Willing Mind, Not a Command.** Read why 2 Corinthians 8:8 explicitly says Paul is "not by commandment."
3. **Equality, Not Equal Amounts.** See what the "principle of equality" in 2 Corinthians 8:13–15 actually asks for.
4. **Administered With Integrity.** Trace why Paul sends Titus and named brethren rather than handling the gift alone.
5. **The Cheerful Giver.** Follow 2 Corinthians 9:6–15 from sowing and reaping to the harvest of righteousness.
6. **Contentment and Israel's Tithe.** Read Philippians 4:10–19's contentment, then distinguish grace-giving from the Law's tithe.

### Study 48 — The Christian Household
File: `study-48-the-christian-household.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **Mutual Submission First.** See how Ephesians 5:21 governs every household pair that follows, before any is named.
2. **Christ and the Church.** Examine the standard Ephesians 5:25–33 sets for husbands, and test it against a standard of mere authority.
3. **Children and Parents.** Trace the obedience commanded in 6:1–3 alongside the limit placed on fathers in 6:4.
4. **Servants and Masters.** See how 6:5–9 binds both parties to the same Master in heaven, "no respect of persons."
5. **Providing for One's Own.** Read 1 Timothy 5:8 and test how seriously it treats providing for one's own household.
6. **Headship, Submission, and Worth.** Test whether headship and submission describe a difference in order and function, or a difference in worth (1 Cor. 11:3; Gal. 3:28).

### Study 49 — The Resurrections of Scripture
File: `study-49-the-resurrections-of-scripture.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **Firstfruits and What Follows.** Trace how Christ's own resurrection (1 Cor. 15:20–23) relates to the resurrections that follow it, and test whether the relationship is identity or pattern.
2. **Caught Up to Meet Him.** Read the Body's own resurrection hope in 1 Thessalonians 4:13–18 and trace its stated destination.
3. **A Revealed Mystery.** Trace 1 Corinthians 15:51–54's "we shall all be changed" as new revelation given through Paul.
4. **Two Resurrections, Not One.** See why Revelation 20 separates the resurrection of the just from the resurrection of the unjust by a thousand years.
5. **Ezekiel 37 Is National, Not Individual.** Read why the text itself names the dry bones "the whole house of Israel," not individual bodily resurrection.
6. **Concurrency Is Not Transfer.** See why shared resurrection vocabulary across Israel and the Body never means one program's hope has become the other's.

### Study 50 — Election
File: `study-50-election.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **One Word, Two Referents.** See why "chosen" alone never settles who is in view — the object, basis, timing, and destiny must come from each passage's own setting.
2. **Israel's National Election.** Trace God's unconditional choice of Israel in Deuteronomy 7, Romans 9's Isaac/Jacob argument, and Romans 11:28–29's "beloved for the fathers' sakes."
3. **Corporate Election and the Believing Remnant.** See how a nation can be elected as a whole while Romans 11:5's individual "election of grace" still operates within it.
4. **The Body's Election in Christ.** Read Ephesians 1's "chosen . . . before the foundation of the world" and test its ground against Israel's own national election.
5. **What the Two Elections Never Share.** Compare object, basis, covenant status, and destiny side by side without collapsing one election into the other.
6. **Guarding Against Two Opposite Errors.** Avoid merging Israel and the Body into one election, and avoid stretching Israel's election to answer a question about individual salvation it was not given to answer.

### Study 51 — Circumcision
File: `study-51-circumcision.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **One Word, Two Realities.** See why “circumcision” alone never settles what is in view — the covenant, the company, and whether a physical rite or a spiritual reality is meant must come from each passage's own setting.
2. **Israel's Covenant Sign.** Trace circumcision from its institution in Genesis 17 through its codification under the Law in Leviticus 12, and its renewal at Gilgal in Joshua 5.
3. **The Jerusalem Council's Test Case.** See how Timothy's circumcision and Titus's refusal to be circumcised draw the line between missionary accommodation and doctrinal requirement.
4. **Circumcision's Value for the Body.** Read Paul's argument in Romans 4 and Galatians 5–6 and test what circumcision does or doesn't establish for anyone in Christ.
5. **The Circumcision of Christ.** Examine Colossians 2:11–13's “circumcision made without hands” and trace what kind of reality it names for the Body.
6. **Guarding Against Two Opposite Errors.** Avoid requiring the fleshly sign of Gentile Body members, and avoid collapsing Israel's fleshly covenant sign into the Body's spiritual identity.

### Study 52 — Sonship and Adoption
File: `study-52-sonship-and-adoption.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **Adoption Defined.** Examine huiothesia's own legal background, and test how it differs from new birth's gift of a new nature (John 1:12–13).
2. **Israel's National Sonship.** Trace God's own claim on Israel as “my son, even my firstborn” (Exodus 4:22) through to Paul's naming of “the adoption” as Israel's own covenant possession in Romans 9:4.
3. **The Body's Adoption in Christ.** Read Galatians 4 and Ephesians 1 for the Body's own distinct adoption, grounded in God's own predestinating choice “before the foundation of the world.”
4. **The Spirit of Adoption.** Examine Romans 8:14–17 and the believer's own cry of “Abba, Father” as the Spirit's present witness to a sonship already received.
5. **The Future Adoption.** Trace Romans 8:23's “waiting for the adoption, to wit, the redemption of our body” as the same standing's full, still-future unveiling.
6. **Guarding Against Two Opposite Errors.** Avoid merging Israel's national adoption into the Body's own, and avoid denying the believer's already-settled present sonship.

### Study 53 — Redemption
File: `study-53-redemption.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **Redemption Defined.** Trace redemption's own vocabulary of a price paid to secure deliverance from bondage, and test how it differs from forgiveness and reconciliation.
2. **Israel's Historical Redemption.** Trace God's own redemption of Israel from Egypt “with a stretched out arm” (Exodus 6:6) through her still-awaited national redemption (Isaiah 59:20; Romans 11:26–27).
3. **The Body's Redemption in Christ.** Read Romans 3:24, Ephesians 1:7, and Colossians 1:14 for the Body's own redemption, and trace its stated ground in Christ's blood.
4. **Redemption's Stated Grounds.** Examine Galatians 3:13's redemption “from the curse of the law” and 1 Peter 1:18–19's redemption “with the precious blood of Christ” as the ground Scripture itself gives.
5. **The Future Redemption.** Trace Ephesians 1:14's “redemption of the purchased possession” and Romans 8:23's “redemption of our body” as the same redemption's still-future completion.
6. **Guarding Against Two Opposite Errors.** Avoid merging Israel's national redemption into the Body's own, and avoid treating the Body's redemption as incomplete because one part of it remains future.

### Study 54 — Justification
File: `study-54-justification.html` · **Website status: FIXED (2026-09-28) — see changelog for which points changed** · **Interior PDF status: PENDING (source not available in repo)**

1. **Justification Defined.** Trace justification's own legal vocabulary as a verdict declared by God, and distinguish it from regeneration and sanctification.
2. **Israel's Pursuit of a Law-Righteousness.** Trace Israel's own stumbling in Romans 9:30–10:4, seeking a righteousness of her own rather than submitting to God's.
3. **Justification by Faith Apart from Works.** Read Romans 3–5 for the righteousness of God, apart from the law, received by faith and resulting in peace with God.
4. **Galatians 2:16 and the Stated Ground.** Examine Paul's own confrontation at Antioch and his stated principle that no flesh is justified by the works of the law.
5. **Abraham, the Pattern Already Given.** Trace Genesis 15:6 and Romans 4 to see that faith-righteousness was never a new doctrine invented for the Body.
6. **Guarding Against Two Opposite Errors.** Avoid treating the law as though it were ever a valid means of justification, and avoid treating faith-righteousness as a Pauline innovation.

### Study 55 — Reconciled to God
File: `study-55-reconciled-to-god.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Former Enmity and Present Peace.** Read Romans 5:1–11 for the former condition, Christ’s initiative, the benefit received, and confidence amid hardship.
2. **God’s Initiative in Christ.** Trace the verbs in 2 Corinthians 5:18–21: God acts, entrusts a word, and speaks through ambassadors.
3. **The Appeal to Be Reconciled.** Distinguish Christ’s completed work from its proclamation and a hearer’s reception.
4. **Peace in One Body.** Follow Ephesians 2:11–18 without transferring Israel’s covenant identity to the Body.
5. **The Reach of “All Things”.** Honor Colossians 1:19–23’s breadth while reading its direct address and exhortation.
6. **Ministry and Conduct.** Explain what ambassadors announce and why the believer’s pursuit of interpersonal peace follows grace.

### Study 56 — Inheritance
File: `study-56-inheritance.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Inheritance Vocabulary.** Distinguish an heir from the inherited object, and read related Greek and Hebrew terms in their clauses.
2. **The Land Promise.** Compare Abraham’s grant, Israel’s tribal allotments, Mosaic tenure, historical possession, and return.
3. **Heirs in Christ.** Follow Galatians 3–4 and Romans 8 through faith, the Spirit, adoption, heirship, and future glory.
4. **The Spirit’s Earnest.** Read Ephesians 1:11–14 carefully and distinguish the present pledge from completed enjoyment.
5. **Peter’s Reserved Inheritance.** Ask what 1 Peter 1:4 says about secure custody without inventing a final geography.
6. **A Repeatable Reading Method.** Test claims by the giver, heir, named object, basis, timing, and what remains unstated.

### Study 57 — The Eternal Purpose of God
File: `study-57-the-eternal-purpose-of-god.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Purpose and Disclosure.** Distinguish God’s intention before the ages from the Mystery’s historical revelation.
2. **The Fullness of Times.** Read Ephesians 1:9–10 as a claim about Christ without erasing named recipients elsewhere.
3. **The Mystery Hidden in God.** Follow Paul’s account of its disclosure and stewardship in Ephesians 3.
4. **Wisdom Made Known.** Identify the Church as the stated agent of witness to heavenly authorities.
5. **Christ’s Headship.** Keep His comprehensive supremacy and the distinct programs of Scripture in view.
6. **Limits of the Text.** Separate stated future display from detailed offices and timelines the passages leave unstated.

### Study 58 — What Is a Dispensation?
File: `study-58-what-is-a-dispensation.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Meaning in Context.** Distinguish stewardship or administration from a bare period label.
2. **Gospel Responsibility.** Read Paul’s commissioned preaching and local practice in 1 Corinthians 9.
3. **Grace Stewardship.** Follow entrustment, revelation, recipients, and ministry in Ephesians 3.
4. **The Colossians Parallel.** Compare Paul’s service to the Church and the Mystery now manifest.
5. **Future Administration.** Keep Ephesians 1:10 distinct from Paul’s personal commission.
6. **Acts Overlap.** Test the concurrent assignments by narrative and apostolic evidence.

### Study 59 — The Law’s Jurisdiction and the Body of Christ
File: `study-59-the-laws-jurisdiction-and-the-body-of-christ.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **Named Addressees.** Identify the people, terms, and assent at Sinai.
2. **The Law’s Function.** Distinguish exposure of sin from justification and life.
3. **Release in Christ.** Read Romans 6–7 without turning grace into license.
4. **One New Body.** Follow Ephesians 2’s account of common access in Christ.
5. **Paul’s Commands.** Identify concrete instruction given by the Lord to the Body.
6. **Worked Applications.** Test circumcision, holiness, giving, and Romans 13.

### Study 60 — The Churches Named in Scripture
File: `study-60-the-churches-named-in-scripture.html` · **Website status: COMPLIANT (reviewed 2026-09-28) — process-oriented language already, no stated conclusions found** · **Interior PDF status: PENDING (source not available in repo)**

1. **The Identification Test.** Read speaker, audience, setting, commission, and stated corporate teaching.
2. **Matthew’s References.** Test what Matthew 16 and 18 say within their own Kingdom setting.
3. **Acts’ Assemblies.** Distinguish Stephen’s wilderness reference, Jerusalem, and Antioch.
4. **Saul’s Persecution.** Handle Paul’s retrospective “church of God” language without assuming a corporate starting date.
5. **Local and Corporate.** Distinguish a local congregation from Paul’s explicit one Body teaching.
6. **Worked Tests.** Apply the procedure to three disputed identifications.

## Unrelated bug found during this audit — Study 22 (fix separately, not a spoiler issue)

While reading through all 60 studies' "What You'll Study" text side by side, found that **Study
22's ("Prayer Under Grace") six points are not about prayer at all** — all six paragraph bodies
are byte-identical copies of Study 21's ("Israel's Judicial Blinding") points, with only the `<h3>`
titles changed to sound prayer-related. E.g. Study 22 point 1 is titled "Prayer Across Scripture"
but its text reads "Begin with the prophetic vocabulary of seeing, hearing, resistance, and
covenant responsibility" — Isaiah-6 hardening language, not prayer. Checked every study for this
pattern; it is isolated to Studies 21/22 only. This needs its own fix (six new, correct
descriptions for Study 22) independent of the spoiler retrofit, and should probably happen first
since it's a plain content error, not a judgment call.

## Preliminary pattern found in the spoiler audit — needs a scope decision before rewriting

A full line-by-line pass of all 60 studies' website text turned up a clear stylistic split:

- **Studies ~1–44** are written almost entirely in process language — "Trace," "Examine,"
  "Distinguish," "Compare," "Follow," "See how" — and generally do NOT state the study's
  conclusion outright. Spot-checking these against the rule, most already read as compliant or
  close to it.
- **Studies ~45–60** (and isolated earlier points) frequently use a different, declarative pattern
  — "See why X is Y, not Z" / "Read why X means Y" — that states the interpretive answer as
  settled fact rather than describing a process to trace. Representative confirmed examples:
  - **Study 45** (Sanctification), point 2: "See why 1 Corinthians 1:2 and 6:11 describe an
    accomplished status, not a present moral report." States the conclusion outright — matches
    the flagged bad-example pattern exactly. Points 4 and 5 do the same.
  - **Study 41** (Kingdom of God or Kingdom of Heaven?), point 2: "...where both phrases describe
    one entrance into one kingdom." and point 3: "...names the kingdom's source and authority
    rather than a kingdom located in heaven." Both hand over the study's actual interpretive
    answer before the reader traces it.
  - This same "See why X is Y, not Z" construction recurs across many of Studies 46–56 (Secure in
    Christ, Giving Under Grace, Election, Circumcision, Sonship and Adoption, Redemption,
    Justification, and others use it in at least one to three of their six points each).

**Open question for the publisher, before any rewriting starts:** the rule's own wording ("must
never... give away the doctrinal conclusion, state the interpretive answer outright") reads as
strict and universal, which would mean essentially all of Studies 45–60 (and scattered points
elsewhere) need rewriting — a large job. But the rule's origin (the flagged Study 61 example) was
specifically about *withholding a debated, argued-for identification* (who the male child is) —
not necessarily about softening every doctrinal-distinction description in an expository study
where there is no "mystery" being protected. Asked Claude (via chat) to get direction on how
strictly to apply this before doing the rewrite pass; see the conversation for the answer once
given, and log the decision here.

## Interior PDF Audit (v1.2)

Source: interior production PDFs for all 60 studies, supplied by the publisher outside this repo
and worked from a local extraction (first several pages of each PDF, pulled with pdfplumber).
Methodology is the **same strict standard** used for the website-side pass above (see
"Methodology used for the website-side pass"), applied by the publisher's confirmed strict
directive: a bullet is a VIOLATION when it states this study's own specific, resolved
interpretive/doctrinal conclusion as settled fact, rather than describing the process, textual
markers, or discipline the reader will use to reach it themselves. Boilerplate Acts
Overlap/Prophecy-Mystery/Non-Transfer framework restatement and direct textual
quotation/observation (the passage's own explicit wording) remain COMPLIANT even when
confident-sounding, per the same two exceptions used on the website side.

**This is a read-only survey.** No interior PDF has been edited. Editable source files (DOCX) for
Studies 1–60 are not available in this repo or session — only finished PDFs — so fixing any
violation found here is out of scope for this pass and is left as a separate, not-yet-scoped
follow-up task once the publisher decides how a corrected interior page should be distributed
(silent page swap vs. versioned reissue), per the original scope note above.

### Step 1 — Duplicate-file resolutions

Four studies had two candidate interior PDFs in the supplied source set. All four pairs turned out
to have **identical (or functionally identical) "What You Will Learn" bulleted content**, so the
choice of canonical file does not change any judgment below — it is recorded here for the record
only, using the naming hierarchy PRODUCTION_MASTER > FINAL_REVIEW/MASTER_STANDARD_AUDITED >
FINAL/INTERIOR_REVIEW > PASS1/plain draft names:

- **Study 25.** `Study_25_The_Signs_That_Followed_FINAL_CLEAN_COVER.pdf` vs.
  `..._BALANCED_FINAL_REVIEW (1).pdf` — bullet text is word-for-word identical between the two.
  Picked `FINAL_CLEAN_COVER.pdf` as canonical (reads as the cover-finalized production file).
- **Study 34.** `Study_34_Filled_Again_FINAL (1).pdf` vs.
  `..._MASTER_STANDARD_AUDITED (2).pdf` — bullet text is word-for-word identical between the two.
  Picked `MASTER_STANDARD_AUDITED (2).pdf` as canonical (outranks plain "FINAL" per the naming
  hierarchy; confirmed the content matches anyway).
- **Study 39.** `..._FINAL_REVIEW.pdf` vs. `..._INTERIOR_REVIEW (1).pdf` — bullet text is
  word-for-word identical between the two (only the content page number differs: 4 vs. 3, an
  artifact of a different page count earlier in each file). Picked `FINAL_REVIEW.pdf` as canonical
  (outranks "INTERIOR_REVIEW" per the naming hierarchy).
- **Study 51.** `Study_51_PASS1.pdf` vs. `Study_51_Circumcision_PRODUCTION_MASTER.pdf` — bullet
  text is word-for-word identical between the two. Picked `PRODUCTION_MASTER.pdf` as canonical,
  consistent with the task's own prior note that this file is "clearly canonical per naming and
  file size."

### Step 2 — Per-study status (interior PDF, all 60 studies)

Status legend: `COMPLIANT` (no stated conclusions found) · `VIOLATION` (specific bullet(s) quoted).
Studies not listed with quoted bullets below are COMPLIANT — the extracted "What You Will Learn"
bullets already use process/trace/distinguish/test language or restate the passage's own explicit
wording or the public Acts-Overlap/Prophecy-Mystery framework, with no study-specific conclusion
stated as settled fact.

Studies 1–36, 38–40, 42, 43, 44, 46, 50, 55–60: **COMPLIANT.** (Studies 44 and 46 are worth noting
specifically: their interior "What You Will Learn" text already reads almost identically to the
*post-fix* website wording recorded above — e.g. Study 44's "Ground the daily walk in Romans 8:1's
settled legal fact rather than making the walk the basis of acceptance" restates Romans 8:1's own
explicit "no condemnation" language rather than an inferred conclusion, so it was judged compliant
under the direct-textual-observation exception, consistent with how the equivalent website point
was treated.)

- **Study 37 — What Does Paul Mean by New Creation?** VIOLATION (1 of 8 points). Point: *"explain
  why 'new creation' describes God's accomplished work rather than the believer's attempt at moral
  self-reconstruction"* — states the study's interpretive conclusion outright rather than framing
  it as something to trace or test.

- **Study 41 — Kingdom of God or Kingdom of Heaven?** VIOLATION. This interior page is written as
  two paragraphs of prose rather than a bulleted list, but it states the same conclusions the
  website version stated before its 2026-09-28 fix (see Study 41's website row above): *"Matthew's
  'kingdom of heaven' and the other Gospels' 'kingdom of God' name the same promised kingdom"* and
  *"[the phrase] describes the kingdom's source and authority rather than its location."* Both hand
  over the study's actual interpretive answer before the reader traces it — the interior page was
  never given the same fix the website page received.

- **Study 45 — Sanctification Under Grace.** VIOLATION — all 8 points. **This interior PDF's "What
  You Will Learn" text is word-for-word identical to the orphaned `.docx` quoted in this tracker's
  earlier exhibit** (see the "Study 45" entry in the website section above, which quotes the DOCX
  verbatim). Every point states what a passage means or commands as settled fact rather than a
  process to trace — e.g. *"Why 1 Corinthians 1:2 and 1:30 call believers 'sanctified' and 'saints'
  as an already-accomplished fact, before any instruction to grow"* and *"What Romans 6 means when
  it says the believer's present fruit is 'unto holiness' (6:19, 22) — a result, not a repeated
  achievement of standing."* This confirms the DOCX was not a stray unrelated draft: it matches the
  study's actual production interior PDF content exactly, so this is a real, confirmed interior
  violation, not just a hypothetical one from an orphaned file.

- **Study 47 — Giving Under Grace.** VIOLATION (2 of 9 points). Points: *"What Paul means by 'grace
  giving' in 2 Corinthians 8–9 — giving that flows from God's grace already received, not from a
  command imposed"* and *"How 1 Corinthians 16:1–2 establishes an orderly weekly pattern of setting
  aside, without turning that pattern into a tithe."* Both assert the study's own interpretive
  conclusion ("not X") as settled fact rather than posing it as something to test or trace; neither
  is a direct quotation of what the cited verse itself says.

- **Study 48 — The Christian Household.** VIOLATION (1 of 7 points). Point: *"What Paul actually
  commands husbands in Ephesians 5:25–33 — a standard drawn from Christ's own self-giving love for
  the church, not a license to rule."* Compare the website's post-fix wording for the same point:
  "Examine the standard Ephesians 5:25–33 sets for husbands, and test it against a standard of mere
  authority" — process language that tests rather than asserts. The interior page still has the
  pre-fix, conclusion-stating wording.

- **Study 49 — The Resurrections of Scripture.** VIOLATION (2 of 7 points). Points: *"The Body of
  Christ's own resurrection and rapture hope in 1 Thessalonians 4:13–18 and 1 Corinthians
  15:51–54, revealed as a 'mystery' and tied to glorification in the heavens, not to an earthly
  kingdom"* and *"Why Ezekiel 37's valley of dry bones is Israel's national restoration typology,
  not a proof text for individual bodily resurrection, and why confusing the two produces error in
  both directions."* Compare the website's post-fix wording, which grounds the same points in the
  text's own language instead ("Revelation 20 separates the resurrection of the just from the
  resurrection of the unjust by a thousand years"; "the text itself names the dry bones 'the whole
  house of Israel'") — the interior page asserts the conclusion directly rather than pointing to
  what the text itself says.

- **Study 51 — Circumcision.** VIOLATION (2 of 6 points). Points: *"Read Paul's argument in Romans
  4 and Galatians 5–6 that circumcision neither justifies nor disqualifies anyone in Christ"* and
  *"Examine Colossians 2:11–13's 'circumcision made without hands' as the Body's own distinct,
  non-fleshly reality."* Compare the website's post-fix wording for the same two points — "test
  what circumcision does or doesn't establish for anyone in Christ" and "trace what kind of reality
  it names for the Body" — both turned into process language during the website fix; the interior
  page still states the answer outright.

- **Study 52 — Sonship and Adoption.** VIOLATION (1 of 6 points). Point: *"Adoption Defined — See
  huiothesia as a legal placing into the position, rights, and inheritance of a son, distinguished
  from new birth's gift of a new nature."* Compare the website's post-fix wording — "Examine
  huiothesia's own legal background, and test how it differs from new birth's gift of a new
  nature" — the interior page still states the definition and its distinction as settled fact
  rather than something to test.

- **Study 53 — Redemption.** VIOLATION (2 of 6 points). Points: *"Redemption Defined — See
  redemption as a price paid to secure a deliverance from bondage, distinguished from forgiveness
  (the removal of guilt) and from reconciliation (the restoring of relationship)"* and *"Read
  Romans 3:24, Ephesians 1:7, and Colossians 1:14 for the Body's own redemption, accomplished
  through Christ's blood, not a nation's deliverance."* Compare the website's post-fix wording for
  the same two points — "test how it differs from forgiveness and reconciliation" and "trace its
  stated ground in Christ's blood" — again turned into process language on the website but not in
  the interior PDF.

- **Study 54 — Justification.** VIOLATION (1 of 6 points). Point: *"Justification Defined — See
  justification as a legal verdict of righteousness declared by God, distinguished from
  regeneration (a new nature) and sanctification (a changed life)."* Compare the website's post-fix
  wording — "Trace justification's own legal vocabulary as a verdict declared by God, and
  distinguish it from regeneration and sanctification" — same pattern as Studies 52 and 53.

### Summary count

- **Studies with zero interior violations: 50** (Studies 1–36, 38–40, 42, 43, 44, 46, 50, 55–60).
- **Studies with at least one interior violation: 10** — Studies 37, 41, 45, 47, 48, 49, 51, 52, 53,
  54. Total individual violating bullets/points across those 10 studies: 14 (37: 1, 41: 2
  statements in prose form, 45: 8, 47: 2, 48: 1, 49: 2, 51: 2, 52: 1, 53: 2, 54: 1 — note 41 and 45
  are counted by statement/point above and 45's 8 is exact since every point in that study's list
  is a violation).
- Notably, **8 of these 10 studies (41, 45, 47, 48, 49, 51, 52, 53, 54 minus 47, i.e. 41/45/48/49/
  51/52/53/54) are studies whose *website* "What You'll Study" text was already identified and
  fixed in the v1.1 pass** — confirming the tracker's original suspicion that interior and website
  content were likely drafted together and share the same violation pattern. Study 37 and Study 47
  are the two exceptions: their website text was already judged COMPLIANT in v1.1, but their
  interior PDFs still carry a violation the website version does not (or no longer does) — so
  interior and website content are not perfectly mirrored, and each has to be checked on its own
  rather than assumed from the other's status.

### Study 45 DOCX-vs-PDF comparison

The orphaned `assets/study-45-sanctification-under-grace.docx` (reviewed in v1.0/v1.1, then
removed from the repo per the publisher's instruction) and the actual production interior PDF
supplied for this audit (`study-45-sanctification-under-grace.pdf`) contain **exactly the same
"What You Will Learn in This Study" text, word for word, bullet for bullet** (8 bullets,
identical wording and order in both). This resolves the open question the removal left behind:
the DOCX was not an unrelated or superseded draft — it matches the study's real, current interior
content exactly. Study 45's interior PDF is therefore a confirmed, not merely suspected,
violation, and needs the same fix eventually applied to its DOCX-quoted content.

## Changelog

- v1.0 (2026-09-28): File created. Website-side text extracted for all 60
  studies. No studies judged yet. Interior-PDF blocker identified. Study 45's
  orphaned source DOCX found, flagged, and removed from the repo. Full
  line-by-line pass completed for the website side of all 60 studies;
  found and flagged an unrelated Study 22 content bug (six points copied
  from Study 21), and found a stylistic split (Studies ~45-60 lean on a
  declarative "See why X is Y" pattern that likely violates the rule more
  often than Studies 1-44). Raised a scope question to the publisher before
  starting any rewrites.
- v1.1 (2026-09-28): Publisher chose strict application. Fixed Study 22's
  content bug (Key Scriptures, What's Included, What You'll Study, and two
  preview alt texts rewritten — pushed to `main`). Completed the website-side
  spoiler judgment pass for all 60 studies using the methodology documented
  above; rewrote 22 points (plus 4 headings) across Studies 41, 44, 45, 46,
  48, 49, 50, 51, 52, 53, and 54 — pushed to `main`. All other studies'
  website text reviewed and confirmed already compliant, no changes made.
  Website side of this audit is now COMPLETE. Interior-PDF side remains
  blocked on the publisher supplying Studies 1-60's source PDFs/DOCX.
- v1.2 (2026-09-28): Publisher supplied Studies 1–60's interior production
  PDFs. File renamed from v1.1 to v1.2. Resolved the 4 duplicate-file cases
  (Studies 25, 34, 39, 51) — in all four, the two candidates' bulleted
  content was identical, so canonical choice made no judgment difference;
  picked per the naming hierarchy (see Step 1 above). Completed the
  interior-PDF "What You Will Learn" audit for all 60 studies using the same
  strict methodology as the website pass: found 10 studies with at least one
  violation (37, 41, 45, 47, 48, 49, 51, 52, 53, 54; 14 individual violating
  points/statements total) and 50 studies fully compliant. Confirmed the
  orphaned `study-45-sanctification-under-grace.docx` (removed from the repo
  in v1.0) is word-for-word identical to the actual production interior
  PDF's "What You Will Learn" text — so Study 45's interior violation is
  confirmed, not hypothetical. This pass is READ-ONLY: no interior PDF was
  edited, since no editable DOCX/source files are available for any of the
  60 studies, only finished PDFs — fixing the 10 violating studies' interior
  pages is left as a separate, not-yet-scoped follow-up task pending the
  publisher's decision on editable sources and distribution method (silent
  page swap vs. versioned reissue). Both halves of the original
  Preview-Page Spoiler Retrofit Audit (website + interior) are now
  surveyed; only the interior fixes remain outstanding.
- v1.3 (2026-09-28): Publisher supplied editable DOCX sources for all 10
  violating studies (37, 41, 45, 47, 48, 49, 51, 52, 53, 54). All 15
  violating points rewritten directly in each DOCX (Study 45: all 8 points;
  the rest: 1-2 points each), applying the same process/textual-markers
  reframing used on the website side, and delivered to the publisher for
  review — approved. Along the way: found and fixed a second, independent
  defect in Studies 47 and 48 — their source DOCX still carried the
  "[APPROVED COVER TO BE INSERTED HERE AT FINAL ASSEMBLY]" placeholder
  instead of the actual approved cover art, even though both studies are
  long since published live with real covers on the website; corrected by
  inserting the existing approved cover image (already live in `assets/`)
  as the PDF's first page for both. Final PDFs were converted from the
  corrected DOCX files in this environment (LibreOffice); this required
  installing the studies' actual production fonts (EB Garamond, Noto Serif,
  Gelasio for Georgia, Liberation Serif/Sans) to avoid a font-substitution
  regression that was caught and fixed before anything was delivered or
  pushed. Six studies (37, 41, 51, 52, 53, 54) render one page shorter/
  longer than the publisher's recorded final page count — a LibreOffice
  reflow/line-wrap artifact from the corrected wording, not a content
  problem; flagged to the publisher, approval given to proceed. Website
  fix: regenerated and pushed the "What You Will Learn" preview image
  (`study-NN-page-3.jpg`) for all 10 studies from the corrected, correctly-
  fonted PDFs, matching the live site's existing visual style exactly
  (verified pixel-identical between the push and a fresh independent
  clone, no broken images/links, live-rendered and visually confirmed) —
  pushed to `main` (commit `cea1859`). **The website side of this audit
  (both the "What You'll Study" bullets and the "A Look Inside" preview
  image) is now fully compliant for all 60 studies.** Outstanding: the
  publisher's own purchasable interior PDFs (the $5.99 product files) —
  the corrected final PDFs have been delivered, but a decision on how a
  corrected interior page reaches anyone who already purchased the old
  version (silent page swap vs. versioned reissue) has not yet been made,
  and is a publisher decision, not a website change.
