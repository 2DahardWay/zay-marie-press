# DRAFT for publisher approval.
BOOK = "Philippians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Joy in Christ, the Mind of Christ, and the Prize of the Calling"
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
  P("Philippians is a letter from “Paul and Timotheus, the servants of Jesus Christ, to all the saints in Christ Jesus which are at Philippi, with the bishops and deacons” (Phil. 1:1). Paul writes from imprisonment (Phil. 1:7, 13) to thank the believers for their gift, to report on his circumstances, and to urge them to stand fast in one spirit and to have the mind of Christ (Phil. 1:27; 2:5; 4:10–18)."),
  BOX("Program Identity:", "Philippians is a letter from Paul to believers at Philippi, written from prison. This reading rests on the letter’s own audience markers and setting."))

S(2, "Narrative Flow of Philippians",
  H("Movement 1 — Thanksgiving and Paul’s Circumstances (Ch. 1)"),
  P("Paul gives thanks, prays for the believers’ love to abound, and reports that his bonds have furthered the gospel (Phil. 1:3–11, 12–14)."),
  H("Movement 2 — The Mind of Christ (Ch. 2)"),
  P("Paul urges lowliness of mind, sets Christ’s humbling and exaltation before them, and commends Timothy and Epaphroditus (Phil. 2:3–11, 19–30)."),
  H("Movement 3 — Knowing Christ and Pressing On (Ch. 3)"),
  P("Paul counts his former standing as loss for the knowledge of Christ and presses toward the mark, noting that “our conversation is in heaven” (Phil. 3:4–14, 20)."),
  H("Movement 4 — Peace, Contentment, and Thanks (Ch. 4)"),
  P("Paul calls for rejoicing and prayer, describes what to think on, speaks of contentment, and acknowledges the Philippians’ gift (Phil. 4:4–9, 11–13, 15–18)."))

S(3, "Program Themes in Philippians",
  H("1. Joy in Christ"),
  P("Paul rejoices in the gospel’s progress and calls the believers to “rejoice in the Lord alway” (Phil. 1:18; 4:4)."),
  H("2. The Mind of Christ"),
  P("“Let this mind be in you, which was also in Christ Jesus,” who humbled Himself and was exalted (Phil. 2:5–11)."),
  H("3. Knowing Christ"),
  P("Paul counts all things loss for the excellency of the knowledge of Christ Jesus his Lord (Phil. 3:7–10)."),
  H("4. A Heavenly Citizenship"),
  P("“Our conversation is in heaven; from whence also we look for the Saviour” (Phil. 3:20)."),
  H("5. Peace and Contentment"),
  P("The peace of God keeps hearts and minds, and Paul has learned in whatsoever state he is to be content (Phil. 4:7, 11)."))

S(4, "Christ in Philippians: Fulfillment and Revelation",
  H("1. Christ the Servant"),
  P("Christ took upon Himself the form of a servant and became obedient unto death, even the death of the cross (Phil. 2:7–8)."),
  H("2. Christ Exalted"),
  P("God has highly exalted Him and given Him a name above every name, so that every knee shall bow (Phil. 2:9–11)."),
  H("3. Christ Our Righteousness"),
  P("Paul desires to be found in Christ, having the righteousness which is of God by faith (Phil. 3:9)."),
  H("4. Christ the Saviour from Heaven"),
  P("Believers look for the Saviour, the Lord Jesus Christ, who shall change their vile body (Phil. 3:20–21)."))

S(5, "Paul’s Jewish Background in Philippians",
  P("Philippians records Paul’s own Jewish background and what he counts of it:"),
  L("Paul lists his credentials: circumcised the eighth day, of the stock of Israel, of the tribe of Benjamin, an Hebrew of the Hebrews (Phil. 3:5).",
    "He counts what was gain to him as loss for Christ (Phil. 3:7–8).",
    "He desires the righteousness which is of God by faith, not his own righteousness of the law (Phil. 3:9).",
    "The letter does not address the readers as Israel and does not list Israel’s covenants as their own."),
  P("This reading rests on the letter’s own audience markers and setting."))

S(6, "Distinctions in Philippians",
  P("Philippians teaches believers:"),
  L("to stand fast in one spirit and to have the mind of Christ", "to count all things loss for the knowledge of Christ", "to await the Saviour from heaven", "to be anxious for nothing and to pray with thanksgiving"),
  P("It does not mention Israel’s covenants, kingdom promises, or Temple worship as the readers’ own."))

S(7, "Truths Table: What Philippians Says",
  TBL(["Category", "Truth Revealed in Philippians", "Program Identity", "Scripture"], [
    ["Heavenly Citizenship", "Believers’ conversation is in heaven, and they look for the Saviour.", "Addressed to Believers", "Phil. 3:20"],
    ["Righteousness by Faith", "The righteousness which is of God by faith, not of the law.", "Addressed to Believers", "Phil. 3:9"],
    ["Change at Christ’s Coming", "The Lord Jesus Christ shall change our vile body.", "Addressed to Believers", "Phil. 3:21"],
    ["Bishops and Deacons", "The letter greets the saints with the bishops and deacons.", "Addressed to Believers", "Phil. 1:1"],
    ["Partnership in the Gospel", "The Philippians’ fellowship in the gospel and their gift.", "Addressed to Believers", "Phil. 1:5; 4:15–16"],
    ["Paul’s Imprisonment", "Paul’s bonds are in Christ and have furthered the gospel.", "Report", "Phil. 1:12–14"],
    ["Paul’s Hebrew Credentials", "Paul’s background is reported and counted as loss.", "Report", "Phil. 3:4–8"],
    ["Names Written in the Book of Life", "Paul’s fellow labourers have their names in the book of life.", "Report", "Phil. 4:3"],
  ], [24, 41, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["Every Knee Shall Bow", "At the name of Jesus every knee shall bow.", "Phil. 2:10–11"],
    ["Humility", "In lowliness of mind let each esteem others better than themselves.", "Phil. 2:3"],
    ["God at Work in Us", "God worketh in you both to will and to do of his good pleasure.", "Phil. 2:13"],
    ["Pressing On", "Forgetting what is behind, press toward the mark.", "Phil. 3:13–14"],
    ["Prayer Without Anxiety", "Be careful for nothing; make requests known with thanksgiving.", "Phil. 4:6"],
    ["The Peace of God", "The peace of God shall keep hearts and minds.", "Phil. 4:7"],
    ["Things to Think On", "Whatsoever things are true, honest, just, pure, lovely, of good report.", "Phil. 4:8"],
    ["Contentment", "In whatsoever state, to be content.", "Phil. 4:11"],
  ], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 separate what Philippians says to its readers from truths that hold for all people. Because the letter is addressed to believers, its own instructions apply to them directly. They do not turn Israel’s covenant commands into the readers’ obligations."),
  P("Drawn from Philippians’ instructions to believers and from universal truths. Believers should:"),
  OL("<b>Rejoice in the Lord</b> — Joy does not wait for easy circumstances (Phil. 4:4).",
     "<b>Have the mind of Christ</b> — Walk in humility and service (Phil. 2:3–5).",
     "<b>Stand fast in one spirit</b> — Strive together for the faith of the gospel (Phil. 1:27).",
     "<b>Count Christ above all</b> — Let knowing Him outweigh every earthly gain (Phil. 3:8).",
     "<b>Press toward the mark</b> — Forget what is behind and reach forward (Phil. 3:13–14).",
     "<b>Pray without anxiety</b> — Bring every request with thanksgiving (Phil. 4:6).",
     "<b>Think on what is good</b> — Fill the mind with what is true and lovely (Phil. 4:8).",
     "<b>Learn contentment</b> — Rest in the Lord’s supply (Phil. 4:11–13, 19)."))

S(10, "Teaching Outline for Philippians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Partners in the Gospel (1:1–11) — Greeting, thanksgiving, and prayer. <i>(Phil. 1:1–11)</i>",
     "Bonds That Advance the Gospel (1:12–30) — Paul’s circumstances and the call to stand fast. <i>(Phil. 1:12–14, 27)</i>",
     "The Mind of Christ (2:1–18) — Humility, Christ’s humbling and exaltation, and shining as lights. <i>(Phil. 2:3–11, 15)</i>",
     "Timothy and Epaphroditus (2:19–30) — Two faithful servants. <i>(Phil. 2:19–30)</i>",
     "Knowing Christ (Ch. 3) — Paul’s loss and gain, the mark, and the heavenly citizenship. <i>(Phil. 3:7–14, 20–21)</i>",
     "Peace and Right Thinking (4:1–9) — Rejoice, pray, and think on what is good. <i>(Phil. 4:4–9)</i>",
     "Contentment and Thanks (4:10–23) — The gift, contentment, and God’s supply. <i>(Phil. 4:11–13, 18–19)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Philippians, helping you see both the letter’s own setting and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications will guide your heart toward joy, humility, and contentment, drawn from what Philippians itself says to believers."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Philippians simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter says to its readers and what holds for all people, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Philippians is a letter from Paul to believers at Philippi, read on its own audience markers and setting. This Companion shows you how to honor the book’s own setting while drawing out the principles that apply to all believers in every age."))
