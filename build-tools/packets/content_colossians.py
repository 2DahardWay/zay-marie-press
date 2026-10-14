# DRAFT for publisher approval.
BOOK = "Colossians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "The Preeminent Christ, the Mystery, and Completeness in Him"
SECTIONS = []
def S(n, t, *blocks): SECTIONS.append((n, t, list(blocks)))
P = lambda x: ("p", x)
L = lambda *xs: ("ul", list(xs))
H = lambda x: ("h3", x)
TBL = lambda head, rows, widths: ("table", head, rows, widths)
OL = lambda *xs: ("ol", list(xs))
OLR = lambda *xs: ("olr", list(xs))
BOX = lambda lead, text: ("box", lead, text)

S(1, "Book Overview (Program-Aware)",
  P("Colossians is a letter from “Paul, an apostle of Jesus Christ by the will of God, and Timotheus our brother, to the saints and faithful brethren in Christ which are at Colosse” (Col. 1:1–2). Paul writes from bonds (Col. 4:3, 18) to warn the believers against philosophy, tradition, and ordinances that would take them from Christ, and to show them what they have in Him (Col. 2:8, 16–17)."),
  BOX("Program Identity:", "Colossians belongs to the Mystery Program: it speaks of the mystery hid from ages and generations and now made manifest to the saints, and addresses believers in Christ at Colosse (Col. 1:26–27; 1:2)."))

S(2, "Narrative Flow of Colossians",
  H("Movement 1 — Thanksgiving and Prayer (Ch. 1:1–14)"),
  P("Paul thanks God for the believers’ faith and love, and prays that they be filled with the knowledge of His will (Col. 1:3–14)."),
  H("Movement 2 — The Preeminence of Christ and the Mystery (1:15–2:7)"),
  P("Christ is the image of the invisible God and head of the body, and the mystery is “Christ in you, the hope of glory” (Col. 1:15–20, 26–27)."),
  H("Movement 3 — Complete in Christ (2:8–23)"),
  P("Believers are complete in Him, and Paul warns against philosophy, ordinances, and the shadow of things to come (Col. 2:9–10, 16–17)."),
  H("Movement 4 — The Walk Above (3:1–4:6)"),
  P("Paul calls believers to set their affections above, to put off the old man and put on the new, and to order home and speech (Col. 3:1–4, 9–10, 18–4:1; 4:2–6)."),
  H("Movement 5 — Greetings and Closing (4:7–18)"),
  P("Paul names his fellow workers, sends greetings, and closes with “Remember my bonds. Grace be with you” (Col. 4:7–18)."))

S(3, "Mystery-Program Themes in Colossians",
  H("1. The Mystery Made Manifest"),
  P("The mystery which hath been hid from ages and from generations is made manifest to His saints (Col. 1:26)."),
  H("2. Christ in You"),
  P("The riches of the glory of this mystery among the Gentiles is “Christ in you, the hope of glory” (Col. 1:27)."),
  H("3. Complete in Christ"),
  P("In Christ dwells all the fulness of the Godhead bodily, and believers are complete in Him (Col. 2:9–10)."),
  H("4. Risen with Christ"),
  P("Believers are risen with Christ, their life is hid with Christ in God, and they are to seek things above (Col. 3:1–3)."),
  H("5. Appearing in Glory"),
  P("When Christ, who is our life, shall appear, they also shall appear with Him in glory (Col. 3:4)."))

S(4, "Christ in Colossians: Fulfillment and Revelation",
  H("1. Image of the Invisible God"),
  P("Christ is the image of the invisible God, the firstborn of every creature (Col. 1:15)."),
  H("2. Creator and Sustainer"),
  P("By Him were all things created, and by Him all things consist (Col. 1:16–17)."),
  H("3. Head of the Body"),
  P("He is the head of the body, the church, the beginning, the firstborn from the dead (Col. 1:18)."),
  H("4. Reconciler by the Blood of His Cross"),
  P("God reconciled all things to Himself by Him, having made peace through the blood of His cross (Col. 1:20–22)."),
  H("5. Head of All Principality and Power"),
  P("Christ is the head of all principality and power, and He triumphed over them in His cross (Col. 2:10, 15)."))

S(5, "Israel and the Body in Colossians",
  P("Colossians speaks to believers about circumcision and Jewish observances without calling the readers Israel:"),
  L("Believers are circumcised with “the circumcision made without hands” in the putting off of the body of the sins of the flesh (Col. 2:11).",
    "Paul warns against being judged in meat, drink, a holyday, the new moon, or the sabbath days, “which are a shadow of things to come; but the body is of Christ” (Col. 2:16–17).",
    "“There is neither Greek nor Jew, circumcision nor uncircumcision” in the new man where Christ is all and in all (Col. 3:11).",
    "The letter does not list Israel’s covenants or kingdom promises as the readers’ own."),
  P("This reading rests on the passage’s own audience markers and setting."))

S(6, "Body-of-Christ Distinctions",
  P("Colossians teaches the Body’s standing in Christ:"),
  L("Christ as head of the body, the church", "the mystery of Christ in you, the hope of glory", "completeness in Christ and risen life with Him", "the new man in whom there is neither Greek nor Jew", "a walk above, in the things of Christ"),
  P("It does not give Israel’s covenants, earthly kingdom, or Temple worship to the Body."))

S(7, "Body-Specific Truths Table (Program-Specific)",
  TBL(["Category", "Truth Revealed in Colossians", "Program Identity", "Scripture"], [
    ["The Mystery", "The mystery hid from ages is now made manifest to His saints.", "Body-Specific", "Col. 1:26"],
    ["Christ in You", "Christ in you, the hope of glory.", "Body-Specific", "Col. 1:27"],
    ["Head of the Body", "Christ is head of the body, the church.", "Body-Specific", "Col. 1:18"],
    ["Completeness", "Believers are complete in Christ.", "Body-Specific", "Col. 2:10"],
    ["Circumcision Without Hands", "The putting off of the body of the sins of the flesh.", "Body-Specific", "Col. 2:11"],
    ["Risen with Christ", "Believers are risen with Christ and their life is hid with Him in God.", "Body-Specific", "Col. 3:1–3"],
    ["Appearing in Glory", "Believers shall appear with Christ in glory.", "Body-Specific", "Col. 3:4"],
    ["The New Man", "Neither Greek nor Jew, circumcision nor uncircumcision.", "Body-Specific", "Col. 3:10–11"],
    ["Paul’s Stewardship", "Paul was made a minister according to the dispensation given to him.", "Body-Specific", "Col. 1:25"],
  ], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["Christ the Creator", "All things were created by Him and for Him.", "Col. 1:16"],
    ["God’s Forgiveness", "Forgiving one another, even as Christ forgave you.", "Col. 3:13"],
    ["Love as the Bond", "Above all, put on charity, the bond of perfectness.", "Col. 3:14"],
    ["Thankfulness", "Be ye thankful.", "Col. 3:15"],
    ["The Word Dwelling Richly", "Let the word of Christ dwell in you richly.", "Col. 3:16"],
    ["Working Heartily", "Whatsoever ye do, do it heartily, as to the Lord.", "Col. 3:23"],
    ["Fair Treatment", "Masters, give that which is just and equal.", "Col. 4:1"],
    ["Gracious Speech", "Let your speech be alway with grace, seasoned with salt.", "Col. 4:6"],
  ], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 separate what Colossians reveals about the Body’s calling from truths that hold for all people. Because Colossians is addressed to the Body, its conduct instructions apply to the Body directly. They do not turn Israel’s covenant commands into the Body’s obligations."),
  P("Drawn from Colossians’ own instructions to believers and from universal truths. The Body of Christ should:"),
  OL("<b>Keep Christ first</b> — Let Him have the preeminence in all things (Col. 1:18).",
     "<b>Know its completeness</b> — Do not return to philosophy or ordinances (Col. 2:8–10).",
     "<b>Seek things above</b> — Set the affections on things above (Col. 3:1–2).",
     "<b>Put off and put on</b> — Lay aside the old man and put on the new (Col. 3:9–10).",
     "<b>Forgive and love</b> — Forgive as Christ forgave; put on charity (Col. 3:13–14).",
     "<b>Be thankful</b> — Let the word of Christ dwell richly (Col. 3:15–16).",
     "<b>Work heartily</b> — Do it as to the Lord (Col. 3:23).",
     "<b>Speak with grace</b> — Season speech with salt (Col. 4:6)."))

S(10, "Teaching Outline for Colossians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Thanksgiving and Prayer (1:1–14) — Faith, love, and knowledge of God’s will. <i>(Col. 1:3–14)</i>",
     "The Preeminent Christ (1:15–23) — Image, Creator, head of the body, and reconciler. <i>(Col. 1:15–22)</i>",
     "The Mystery and Paul’s Stewardship (1:24–2:7) — Christ in you, the hope of glory. <i>(Col. 1:25–27)</i>",
     "Complete in Him (2:8–23) — Warnings against philosophy, ordinances, and shadows. <i>(Col. 2:8–10, 16–17)</i>",
     "Risen with Christ (3:1–4) — Seek things above. <i>(Col. 3:1–4)</i>",
     "The New Man and the Walk (3:5–4:1) — Putting off, putting on, and the household. <i>(Col. 3:9–17; 3:18–4:1)</i>",
     "Prayer, Wisdom, and Greetings (4:2–18) — Speech, fellow workers, and closing words. <i>(Col. 4:2–6, 18)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Colossians, helping you see both the letter’s own setting and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications will guide your heart toward completeness in Christ, thankfulness, and a walk above, drawn from what Colossians itself says to believers."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Colossians simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter says to its readers and what holds for all people, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Colossians stands in the mystery revealed through Paul and speaks directly to the Body of Christ. This Companion shows you how to honor the book’s own setting while drawing out the principles that apply to all believers in every age."))
