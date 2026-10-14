# DRAFT for publisher approval.
BOOK = "Galatians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "One Gospel, Justified by Faith, and Liberty in the Spirit"
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
  P("Galatians is a letter from “Paul, an apostle, (not of men, neither by man, but by Jesus Christ, and God the Father, who raised him from the dead)” to “the churches of Galatia” (Gal. 1:1–2). Paul wrote because the believers were turning to “another gospel” (Gal. 1:6–7). He insists that the gospel he preached was not received from man but came “by the revelation of Jesus Christ” (Gal. 1:11–12)."),
  BOX("Program Identity:", "Galatians is Paul’s defense of the gospel committed to him, written to believers in the Gentile churches of Galatia during the Acts 9–28 overlap. It belongs to Paul’s ministry in the Mystery Program and is read with the standing boundaries between Israel’s prophetic program and the Body (Gal. 2:7–9; 6:16)."))

S(2, "Narrative Flow of Galatians",
  H("Movement 1 — Paul’s Gospel and Apostleship Defended (Chs. 1–2)"),
  P("Paul rebukes the turn to another gospel, recounts how he received his gospel by revelation, reports his meeting at Jerusalem, and confronts Peter at Antioch (Gal. 1:6–12; 2:1–10, 11–14)."),
  H("Movement 2 — Faith, the Law, and the Seed (Chs. 3–4)"),
  P("Paul asks whether the Spirit came by works of the law or by the hearing of faith, sets the law’s purpose beside the promise, and shows believers as sons through faith in Christ Jesus (Gal. 3:2, 19, 24–26; 4:4–7)."),
  H("Movement 3 — Liberty and the Walk in the Spirit (Chs. 5–6)"),
  P("Paul calls believers to stand fast in liberty, to walk in the Spirit, to bear one another’s burdens, and to count a new creature as what matters (Gal. 5:1, 16, 22–23; 6:2, 15)."))

S(3, "Program Themes in Galatians",
  H("1. One Gospel by Revelation"),
  P("Paul’s gospel came by the revelation of Jesus Christ, and no other gospel is to be received (Gal. 1:8–12)."),
  H("2. Justification by Faith"),
  P("A man is not justified by the works of the law but by the faith of Jesus Christ (Gal. 2:16)."),
  H("3. The Purpose of the Law"),
  P("The law was added because of transgressions and was our schoolmaster to bring us to Christ (Gal. 3:19, 24)."),
  H("4. Sons Through Faith"),
  P("Believers are children of God by faith in Christ Jesus, and God sent the Spirit of His Son into their hearts (Gal. 3:26; 4:6)."),
  H("5. Liberty and the Spirit’s Walk"),
  P("Christ has made believers free, and they are to walk in the Spirit (Gal. 5:1, 16)."))

S(4, "Christ in Galatians: Fulfillment and Revelation",
  H("1. The One Who Gave Himself"),
  P("Christ “gave himself for our sins, that he might deliver us from this present evil world” (Gal. 1:4)."),
  H("2. The Crucified One"),
  P("Christ was set forth crucified, and Paul is crucified with Christ so that Christ lives in him (Gal. 2:20; 3:1)."),
  H("3. The One Made a Curse"),
  P("Christ redeemed from the curse of the law, being made a curse for us (Gal. 3:13)."),
  H("4. The Seed"),
  P("The promises were made to Abraham and his seed, “which is Christ” (Gal. 3:16)."),
  H("5. Sent Forth, Made Under the Law"),
  P("When the fulness of the time was come, God sent forth His Son, made of a woman, made under the law (Gal. 4:4)."))

S(5, "Israel and the Body in Galatians",
  P("Galatians mentions Israel’s promises and Israel’s apostles without placing the Body inside Israel’s covenants:"),
  L("The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant (Gal. 3:16, 29).",
    "Paul reports that the gospel of the uncircumcision was committed to him and the gospel of the circumcision to Peter, and the study records the text and assigns nothing further (Gal. 2:7–9).",
    "“The Israel of God” (Gal. 6:16) names believing Jews within Israel’s prophetic identity, not members of the Body.",
    "The law’s jurisdiction and the believer’s liberty are stated in Galatians 3–5; the letter never places the Body under Israel’s covenant obligations."),
  P("This reading rests on the passage’s own audience markers and setting."))

S(6, "Body-of-Christ Distinctions",
  P("Galatians teaches the Body’s standing in Christ:"),
  L("justification by faith, not works of the law", "crucifixion with Christ and Christ living in the believer", "sonship through faith and the Spirit of His Son in the heart", "liberty and the walk in the Spirit", "a new creature as what counts"),
  P("It does not place the Body under the law, make circumcision or special days a requirement, or give the Body a share in Israel’s covenants."))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Galatians", "Program Identity", "Scripture"], [
    ["Paul’s Gospel", "The gospel came to Paul by the revelation of Jesus Christ.", "Body of Christ (Pauline) Truth", "Gal. 1:11–12"],
    ["Justification by Faith", "A man is justified by the faith of Jesus Christ, not by works of the law.", "Body of Christ (Pauline) Truth", "Gal. 2:16"],
    ["Crucified with Christ", "Christ lives in the believer.", "Body of Christ (Pauline) Truth", "Gal. 2:20"],
    ["Sons Through Faith", "Believers are children of God by faith in Christ Jesus.", "Body of Christ (Pauline) Truth", "Gal. 3:26; 4:6"],
    ["Liberty in Christ", "Believers stand fast in the liberty Christ gave.", "Body of Christ (Pauline) Truth", "Gal. 5:1"],
    ["A New Creature", "Neither circumcision nor uncircumcision counts; a new creature does.", "Body of Christ (Pauline) Truth", "Gal. 6:15"],
    ["The Seed", "The promise to Abraham’s seed is fulfilled in Christ.", "Israel / Kingdom / Prophecy Explicit Truth", "Gal. 3:16"],
    ["The Israel of God", "Believing Jews within Israel’s prophetic identity, not members of the Body.", "Israel / Kingdom / Prophecy Explicit Truth", "Gal. 6:16"],
  ], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["All Under Sin", "The scripture hath concluded all under sin.", "Gal. 3:22"],
    ["Love Your Neighbour", "Love your neighbour as yourself.", "Gal. 5:14"],
    ["The Fruit of the Spirit", "Love, joy, peace, longsuffering, gentleness, goodness, faith, meekness, temperance.", "Gal. 5:22–23"],
    ["Restoring Gently", "Restore the one overtaken in a fault in the spirit of meekness.", "Gal. 6:1"],
    ["Bearing Burdens", "Bear one another’s burdens.", "Gal. 6:2"],
    ["Sowing and Reaping", "Whatsoever a man soweth, that shall he also reap.", "Gal. 6:7"],
    ["Not Weary in Well-Doing", "Do not grow weary in well-doing.", "Gal. 6:9"],
    ["Doing Good to All", "Do good unto all men as there is opportunity.", "Gal. 6:10"],
  ], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 separate what Galatians says to the Body, what it says about Israel, and what holds for all people. Because Galatians is addressed to believers in Christ, its instructions apply to the Body directly. They do not turn Israel’s covenant obligations into the Body’s requirements."),
  P("Drawn from Galatians’ instructions to believers and from universal truths. The Body of Christ should:"),
  OL("<b>Hold to one gospel</b> — Receive no other gospel than the one Paul preached (Gal. 1:8–9).",
     "<b>Rest in justification by faith</b> — Righteousness is not earned by works (Gal. 2:16).",
     "<b>Live by Christ’s life</b> — Christ lives in the believer (Gal. 2:20).",
     "<b>Stand fast in liberty</b> — Do not be entangled again with a yoke of bondage (Gal. 5:1).",
     "<b>Walk in the Spirit</b> — Let the Spirit’s fruit show in daily life (Gal. 5:16, 22–23).",
     "<b>Restore gently</b> — Help the one who falls in a spirit of meekness (Gal. 6:1).",
     "<b>Bear one another’s burdens</b> — Care for one another in practical ways (Gal. 6:2).",
     "<b>Do good to all</b> — Sow well and do not grow weary (Gal. 6:7–10)."))

S(10, "Teaching Outline for Galatians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Another Gospel Rebuked (1:1–10) — Paul’s greeting, astonishment, and the curse on any other gospel. <i>(Gal. 1:1–9)</i>",
     "The Gospel by Revelation (1:11–2:10) — How Paul received his gospel and what he reports of Jerusalem. <i>(Gal. 1:11–12; 2:7–9)</i>",
     "Peter Confronted and Faith Defended (2:11–21) — Justified by faith and crucified with Christ. <i>(Gal. 2:11–21)</i>",
     "The Spirit, the Seed, and the Promise (Ch. 3) — Hearing of faith, the law’s purpose, and sons by faith. <i>(Gal. 3:2, 16, 24–29)</i>",
     "Sons and Heirs (4:1–31) — Redeemed from under the law and free in Christ. <i>(Gal. 4:4–7)</i>",
     "Liberty and the Walk in the Spirit (Ch. 5) — Stand fast, walk in the Spirit, bear its fruit. <i>(Gal. 5:1, 16, 22–23)</i>",
     "Bearing, Sowing, and the New Creature (Ch. 6) — Burdens, harvest, and the final word on circumcision and the cross. <i>(Gal. 6:1–2, 7–10, 14–16)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Galatians, helping you see both Paul’s defense of the gospel and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications will guide your heart toward faith, liberty, and the Spirit’s walk, drawn from what Galatians says to believers without turning Israel’s covenant obligations into the Body’s requirements."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Galatians simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the table to help your group see what Galatians says to the Body, what it says about Israel, and what holds for all people, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Galatians was written during the overlap and defends the gospel Paul preached to the Gentiles. This Companion shows you how to keep Israel’s promises and the Body’s standing each in its place while drawing out the principles that apply to all believers."))
