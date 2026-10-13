# DRAFT for publisher approval.
BOOK = "Romans"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Sin, Grace, Israel’s Future, and the Walk of the Body"
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
  P("Romans is Paul’s letter “to all that be in Rome, beloved of God, called to be saints” (Rom. 1:7). He writes as “an apostle, separated unto the gospel of God,” to set out the gospel he preaches, the condition of Jew and Gentile alike, righteousness by faith, and the walk that follows (Rom. 1:1, 16–17; 3:9, 22). The letter was written during the Acts 9–28 overlap, and Paul addresses Israel directly in chapters 9–11 (Rom. 9:3–4; 10:1; 11:1)."),
  BOX("Program Identity:", "Romans carries both programs. Chapters 1–8 and 12–16 speak to the Body in the Mystery Program (Rom. 16:25–26), while chapters 9–11 are addressed to Israel and concern Israel’s election and future in the Prophecy Program."))

S(2, "Narrative Flow of Romans",
  H("Movement 1 — The Gospel and the Guilt of the World (1:1–3:20)"),
  P("Paul announces the gospel as the power of God unto salvation, then shows Gentile and Jew alike under sin (Rom. 1:16–17; 3:9–19)."),
  H("Movement 2 — Righteousness by Faith (3:21–5:21)"),
  P("Righteousness comes by faith in Jesus Christ, illustrated by Abraham, with peace with God and the contrast of Adam and Christ (Rom. 3:21–26; 4:1–5; 5:1, 12–21)."),
  H("Movement 3 — Life in Christ and the Spirit (Chs. 6–8)"),
  P("Believers are baptized into Christ, freed from sin’s dominion, and led by the Spirit, with no condemnation and no separation from the love of God (Rom. 6:3–4; 8:1, 14, 38–39)."),
  H("Movement 4 — Israel’s Election, Stumbling, and Future (Chs. 9–11)"),
  P("Paul addresses Israel’s privileges, its present unbelief, the remnant, the olive tree, and the promise that all Israel shall be saved (Rom. 9:3–5; 10:1; 11:5, 17–24, 26)."),
  H("Movement 5 — The Walk of Believers (12:1–16:27)"),
  P("Paul calls for a renewed mind, love, order, and mutual acceptance, and closes with the revelation of the mystery (Rom. 12:1–2; 13:8–10; 14:1; 16:25–26)."))

S(3, "Program Themes in Romans",
  H("1. The Gospel Paul Preaches"),
  P("The gospel is the power of God unto salvation to every one that believeth (Rom. 1:16; 16:25)."),
  H("2. Universal Guilt and Justification by Faith"),
  P("All have sinned and are justified freely by His grace through the redemption that is in Christ Jesus (Rom. 3:23–24)."),
  H("3. Union with Christ"),
  P("Believers are baptized into Jesus Christ and walk in newness of life (Rom. 6:3–4)."),
  H("4. Israel’s Election and Future"),
  P("Israel’s adoption, covenants, and promises remain, and God has not cast away His people (Rom. 9:4–5; 11:1–2, 29)."),
  H("5. The Mystery Revealed"),
  P("The closing doxology speaks of the revelation of the mystery kept secret since the world began (Rom. 16:25–26)."))

S(4, "Christ in Romans: Fulfillment and Revelation",
  H("1. The Seed of David, Declared the Son of God"),
  P("Christ is made of the seed of David according to the flesh and declared the Son of God by the resurrection from the dead (Rom. 1:3–4)."),
  H("2. The Propitiation"),
  P("God set forth Christ as a propitiation through faith in His blood (Rom. 3:25)."),
  H("3. The Second Adam"),
  P("As by one man sin entered, so by the obedience of one many are made righteous (Rom. 5:12, 19)."),
  H("4. Risen and Interceding"),
  P("Christ died, rose again, and is at the right hand of God making intercession (Rom. 8:34)."),
  H("5. The End of the Law for Righteousness"),
  P("Christ is the end of the law for righteousness to every one that believeth (Rom. 10:4)."))

S(5, "Israel in Romans",
  P("Romans 9–11 is addressed to Israel and concerns Israel. It is read in that setting and not as a passage on how the Body is saved:"),
  L("Israel’s privileges: the adoption, the glory, the covenants, the law, the service, and the promises (Rom. 9:4–5).",
    "A remnant according to the election of grace in the present time (Rom. 11:5).",
    "The olive tree is prophetic blessing and not the Body of Christ. Participation is not identity. Blessing is not covenant. Standing is not program membership (Rom. 11:17–24).",
    "Israel’s future restoration: “all Israel shall be saved” (Rom. 11:26).",
    "Romans 10:9–10 is Israel’s covenantal formula drawn from Deuteronomy 30:14 (Rom. 10:8); the Body is saved by belief in the gospel Paul preached (1 Cor. 15:1–4; Eph. 2:8–9)."),
  P("Concurrency is operational, not transformational."))

S(6, "Body-of-Christ Distinctions",
  P("Romans teaches the Body’s standing in Christ in chapters 1–8 and 12–16:"),
  L("justification by faith apart from works of the law", "baptism into Christ by the Spirit, not water baptism", "life in the Spirit and no condemnation", "the revelation of the mystery through Paul’s gospel", "the believer’s walk of love, order, and mutual acceptance"),
  P("It does not make the Body Israel, place the Body in Israel’s covenants, or turn Romans 9–11 into the Body’s calling."))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Romans", "Program Identity", "Scripture"], [
    ["Justification by Faith", "Righteousness comes by faith in Christ, apart from the works of the law.", "Body-Specific", "Rom. 3:21–28"],
    ["Baptism into Christ", "Believers are baptized into Jesus Christ by the Spirit.", "Body-Specific", "Rom. 6:3–4"],
    ["The Mystery", "The mystery kept secret since the world began is now made manifest.", "Body-Specific", "Rom. 16:25–26"],
    ["Israel’s Privileges", "Adoption, glory, covenants, law, service, and promises belong to Israel.", "Israel-Specific", "Rom. 9:4–5"],
    ["The Remnant", "A remnant according to the election of grace.", "Israel-Specific", "Rom. 11:5"],
    ["Israel’s Restoration", "All Israel shall be saved when the Deliverer comes out of Sion.", "Israel-Specific", "Rom. 11:26–27"],
    ["Israel’s Covenantal Formula", "Confession and belief drawn from Deuteronomy 30:14.", "Israel-Specific", "Rom. 10:8–10"],
    ["The Olive Tree", "Prophetic blessing in which Gentiles participate without becoming Israel.", "Israel-Specific", "Rom. 11:17–24"],
  ], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["Universal Sin", "All have sinned and come short of the glory of God.", "Rom. 3:23"],
    ["Adam and Christ", "Death passed upon all through Adam, and grace abounds through Christ.", "Rom. 5:12–21"],
    ["God’s Love", "God commended His love toward us in that Christ died for us.", "Rom. 5:8"],
    ["God’s Righteous Judgment", "God will render to every man according to his deeds.", "Rom. 2:6"],
    ["God’s Goodness", "The goodness of God leads to repentance.", "Rom. 2:4"],
    ["God’s Sovereign Mercy", "God has mercy on whom He will have mercy.", "Rom. 9:15–16"],
    ["Overcoming Evil with Good", "Be not overcome of evil, but overcome evil with good.", "Rom. 12:21"],
    ["Love Fulfils the Law’s Duty to Neighbour", "Love worketh no ill to his neighbour.", "Rom. 13:8–10"],
  ], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 separate what Romans says to the Body, what it says to Israel, and what holds for all people. This section applies the Body’s own instructions and the universal truths. It does not apply Israel’s covenant formula or kingdom promises to the Body."),
  P("Drawn from Romans’ instructions to believers and from universal truths. The Body of Christ should:"),
  OL("<b>Trust the gospel</b> — It is the power of God unto salvation (Rom. 1:16).",
     "<b>Rest in justification by faith</b> — Righteousness is received, not earned (Rom. 3:24; 4:5).",
     "<b>Know its freedom</b> — There is no condemnation to those in Christ (Rom. 8:1).",
     "<b>Walk in newness of life</b> — Reckon yourselves dead to sin and alive to God (Rom. 6:4, 11).",
     "<b>Be transformed</b> — Renew the mind rather than conform to the world (Rom. 12:1–2).",
     "<b>Overcome evil with good</b> — Live peaceably with all men (Rom. 12:18–21).",
     "<b>Love one another</b> — Love is the fulfilling of the law’s duty to neighbour (Rom. 13:8–10).",
     "<b>Receive one another</b> — Accept the weak in faith without quarrelling (Rom. 14:1; 15:7)."))

S(10, "Teaching Outline for Romans",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("The Gospel and Human Guilt (1:1–3:20) — Paul’s gospel and the condition of Gentile and Jew. <i>(Rom. 1:16–17; 3:9–19)</i>",
     "Righteousness by Faith (3:21–5:21) — Justification, Abraham, peace with God, and Adam and Christ. <i>(Rom. 3:21–26; 4:1–5; 5:1, 12–21)</i>",
     "Freedom in Christ and the Spirit (Chs. 6–8) — Baptism into Christ, sin’s dominion broken, no condemnation. <i>(Rom. 6:3–4; 8:1, 14, 38–39)</i>",
     "Israel’s Election and Stumbling (Chs. 9–10) — Privileges, unbelief, and Israel’s covenantal setting. <i>(Rom. 9:3–5; 10:1–10)</i>",
     "The Remnant, the Olive Tree, and Israel’s Future (Ch. 11) — God has not cast away His people. <i>(Rom. 11:1–5, 17–26)</i>",
     "The Renewed Walk (12:1–15:13) — Transformation, love, order, and mutual acceptance. <i>(Rom. 12:1–2; 13:8–10; 14:1)</i>",
     "Closing Greetings and the Mystery (15:14–16:27) — Paul’s ministry and the doxology. <i>(Rom. 16:25–26)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Romans, helping you see both the way the letter carries two programs and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications will guide your heart toward faith, freedom in Christ, and love, drawn from what Romans says to believers and from universal truths, without turning Israel’s covenant formula into the Body’s calling."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Romans simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the table to help your group see which truths speak to the Body, which belong to Israel in chapters 9–11, and which hold for all people, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Romans was written during the overlap and carries both: the Body’s standing in Christ and Israel’s election and future. This Companion shows you how to keep each in its place while drawing out the truths that apply to all believers in every age."))
