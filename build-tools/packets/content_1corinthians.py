# DRAFT for publisher approval.
BOOK = "1 Corinthians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Order, Love, and the Gospel Received"
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
  P('1 Corinthians is a letter from “Paul called to be an apostle of Jesus Christ through the will of God” to “the church of God which is at Corinth” (1 Cor. 1:1–2). Paul writes in answer to reports of divisions and to questions the Corinthians had sent him (1 Cor. 1:11; 7:1). He takes up factions, discipline, lawsuits, marriage, food offered to idols, worship, spiritual gifts, the resurrection, and the collection for the saints.'),
  BOX("Program Identity:", '1 Corinthians is Paul’s letter to a Gentile church during the Acts 9–28 overlap. It belongs to his ministry in the Mystery Program, and a dispensation of the gospel is committed to him (1 Cor. 9:17). The letter is read for what it says to the Body, and it is not read as Israel’s program.'))

S(2, 'Narrative Flow of 1 Corinthians',
  H('Movement 1 — Divisions and the Cross (Chs. 1–4)'),
  P('Paul answers the factions, sets Christ crucified before them, and names himself and Apollos as ministers and stewards of the mysteries of God (1 Cor. 1:10–13, 23; 3:5–11; 4:1).'),
  H('Movement 2 — Discipline, Marriage, and Conscience (Chs. 5–10)'),
  P('Paul deals with immorality and lawsuits, answers their questions on marriage, and works through food offered to idols, his own rights as an apostle, and the warnings drawn from Israel in the wilderness (1 Cor. 5:1–5; 6:1–11, 19–20; 7:1–2; 8:1–13; 9:1–27; 10:1–13).'),
  H('Movement 3 — Worship, Gifts, and Love (Chs. 11–14)'),
  P('Paul addresses head coverings, the Lord’s supper, the gifts of the Spirit as one body with many members, love, and order in the assembly (1 Cor. 11:2–34; 12:12–31; 13:1–13; 14:26–40).'),
  H('Movement 4 — The Resurrection and the Collection (Chs. 15–16)'),
  P('Paul restates the gospel he preached, sets out Christ’s resurrection and the resurrection of those in Christ, speaks of a mystery and a change, and gives directions for the collection (1 Cor. 15:1–4, 20–23, 51–52; 16:1–2).'))

S(3, 'Program Themes in 1 Corinthians',
  H('1. Christ Crucified'),
  P('Paul determined to know nothing among them “save Jesus Christ, and him crucified” (1 Cor. 2:2).'),
  H('2. One Foundation'),
  P('“Other foundation can no man lay than that is laid, which is Jesus Christ” (1 Cor. 3:11).'),
  H('3. The Body’s Members'),
  P('As the body is one and has many members, so also is Christ (1 Cor. 12:12).'),
  H('4. Love Above the Gifts'),
  P('“The greatest of these is charity” (1 Cor. 13:13).'),
  H('5. The Gospel and the Resurrection'),
  P('Paul restates the gospel he preached and what Christ’s resurrection secures (1 Cor. 15:1–4, 20, 58).'))

S(4, 'Christ in 1 Corinthians',
  H('1. The Crucified One'),
  P('Paul preached “Christ crucified” (1 Cor. 1:23; 2:2).'),
  H('2. The Foundation'),
  P('Jesus Christ is the foundation laid (1 Cor. 3:11).'),
  H('3. Our Passover'),
  P('“Christ our passover is sacrificed for us” (1 Cor. 5:7).'),
  H('4. The Rock'),
  P('Israel drank of that spiritual Rock, “and that Rock was Christ” (1 Cor. 10:4).'),
  H('5. The Firstfruits'),
  P('Christ is risen from the dead, “the firstfruits of them that slept” (1 Cor. 15:20).'))

S(5, 'Israel and the Body in 1 Corinthians',
  P('The letter speaks of Israel in the wilderness and names the Lord’s supper without placing the Body inside Israel’s covenants:'),
  L('Paul writes of “our fathers” under the cloud and through the sea, and says these things “happened unto them for ensamples” written “for our admonition” (1 Cor. 10:1–11). The study reports the text and does not turn Israel’s wilderness history into the Body’s covenant.', 'The cup carries the blood on which the New Covenant rests. The Body of Christ remembers that blood and proclaims the Lord’s death without becoming a party to Israel’s New Covenant (1 Cor. 11:25–26).', '“Till he come” (1 Cor. 11:26) is reported as written, and the study does not specify which coming it names.', 'The gifts and signs of chapters 12–14 are reported as written in the setting of Corinth; the study does not build a doctrine of a prayer language or settle questions of present practice from them.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('1 Corinthians states the Body’s standing and order in Christ:'),
  L('one body, baptized by one Spirit, with many members (1 Cor. 12:12–13)', 'Christ crucified as the one foundation', 'the gospel Paul preached, received and stood in (1 Cor. 15:1–4)', 'love as the more excellent way', 'order and edification in the assembly (1 Cor. 14:26, 40)'),
  P('It does not make the Body a party to Israel’s covenants, and it does not state when or how the gifts pass away beyond what chapter 13 says.'))

S(7, 'Program-Specific Truths Table',
  P('Program Identity shows where a truth belongs. “Text Only” marks a passage the companion reports as written, without assigning it to a program.'),
  TBL(['Category', 'Truth Revealed in 1 Corinthians', 'Program Identity', 'Scripture'], [['The Gospel Preached', 'Christ died for our sins, was buried, and rose again the third day according to the Scriptures.', 'Body-Specific', '1 Cor. 15:1–4'], ['One Body', 'By one Spirit we are all baptized into one body.', 'Body-Specific', '1 Cor. 12:12–13'], ['The Stewardship', 'A dispensation of the gospel is committed to Paul.', 'Body-Specific', '1 Cor. 9:17'], ['The Foundation', 'The foundation laid is Jesus Christ.', 'Body-Specific', '1 Cor. 3:11'], ['The Temple of the Spirit', 'The believer’s body is the temple of the Holy Ghost.', 'Body-Specific', '1 Cor. 6:19'], ['A Mystery and a Change', '“We shall not all sleep, but we shall all be changed.”', 'Body-Specific', '1 Cor. 15:51–52'], ['Israel’s Examples', 'Israel’s wilderness history was written for admonition.', 'Addressed to Believers (warnings / corrections)', '1 Cor. 10:1–11'], ['The Lord’s Supper', 'The cup carries the blood on which the New Covenant rests; the Body remembers it.', 'Body-Specific', '1 Cor. 11:23–26']], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['God Is Faithful', 'God will not suffer you to be tempted above what you are able.', '1 Cor. 10:13'], ['Do All to God’s Glory', 'Whether ye eat or drink, do all to the glory of God.', '1 Cor. 10:31'], ['Love Never Fails', 'Charity suffereth long, and is kind; charity never faileth.', '1 Cor. 13:4–8'], ['Order in Worship', 'Let all things be done decently and in order.', '1 Cor. 14:40'], ['Stand Fast', 'Be stedfast, unmoveable, always abounding in the work of the Lord.', '1 Cor. 15:58'], ['Watch and Stand', 'Watch ye, stand fast in the faith, quit you like men, be strong.', '1 Cor. 16:13'], ['Let All Be in Love', 'Let all your things be done with charity.', '1 Cor. 16:14'], ['Flee Idolatry', 'Flee from idolatry.', '1 Cor. 10:14']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 1 Corinthians says to the Body, what it reports about Israel, and what holds for all people. Because the letter is addressed to a church of believers, its instructions apply to the Body directly. They do not make Israel’s covenants the Body’s.'),
  P('Drawn from 1 Corinthians’ instructions to believers and from universal truths. The Body of Christ should:'),
  OL('<b>Hold to the gospel received</b> — Stand in the gospel Paul preached (1 Cor. 15:1–4).', '<b>Build on the one foundation</b> — Take heed how you build on Jesus Christ (1 Cor. 3:10–11).', '<b>Seek unity</b> — Avoid factions and be joined in the same mind (1 Cor. 1:10).', '<b>Honor the body as God’s temple</b> — Glorify God in body and spirit (1 Cor. 6:19–20).', '<b>Remember the Lord</b> — Take the supper with self-examination (1 Cor. 11:23–28).', '<b>Use gifts to edify</b> — Seek the building up of the church (1 Cor. 14:12, 26).', '<b>Put love first</b> — Let all things be done with charity (1 Cor. 13:13; 16:14).', '<b>Stand fast</b> — Be stedfast, unmoveable, abounding in the Lord’s work (1 Cor. 15:58).'))

S(10, "Teaching Outline for 1 Corinthians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Divisions Answered (1:1–4:21) — Paul sets Christ crucified before the factions. <i>(1 Cor. 1:10–13, 23; 3:11)</i>', 'Discipline and Marriage (Chs. 5–7) — Immorality, lawsuits, and the questions on marriage. <i>(1 Cor. 5:1–5; 6:19–20; 7:1–2)</i>', 'Liberty and Idols (Chs. 8–10) — Knowledge, love, Paul’s rights, and Israel’s examples. <i>(1 Cor. 8:1–13; 9:17; 10:1–13)</i>', 'Worship and the Supper (Ch. 11) — Order and remembrance. <i>(1 Cor. 11:23–26)</i>', 'One Body, Many Members (Ch. 12) — The Spirit’s gifts and the body’s unity. <i>(1 Cor. 12:12–13)</i>', 'The More Excellent Way (Chs. 13–14) — Love and order in the assembly. <i>(1 Cor. 13:13; 14:40)</i>', 'The Gospel and the Resurrection (Chs. 15–16) — Christ the firstfruits, the change, and the collection. <i>(1 Cor. 15:1–4, 20, 51–58; 16:1–2)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 Corinthians, helping you see both what the letter says to believers and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what 1 Corinthians itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 Corinthians simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, 1 Corinthians was written during the overlap to a Gentile church and states what the Body is to hold and how it is to live. This Companion shows you how to keep what the letter reports about Israel in its place while drawing out the principles that apply to all believers."))
