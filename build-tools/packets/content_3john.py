# DRAFT for publisher approval.
BOOK = "3 John"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Walking in the Truth and Receiving the Brethren"
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
  P('3 John is a short personal letter from “The elder unto the wellbeloved Gaius” (3 John 1). It speaks about walking in the truth, faithful service to the brethren and to strangers, Diotrephes, “who loveth to have the preeminence among them” (3 John 9), and Demetrius, who “hath good report of all men” (3 John 12). It closes with the hope to see Gaius shortly and speak face to face.'),
  BOX("Program Identity:", '3 John is addressed to “the wellbeloved Gaius” (3 John 1) and speaks of “the church” (3 John 6, 9, 10). It is read on its own audience markers and setting. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 3 John',
  H('Movement 1 — Gaius Commended (vv. 1–8)'),
  P('The elder greets Gaius, rejoices that he walks in the truth, commends his faithfulness to the brethren and to strangers, and says that such are to be received, that they might be fellowhelpers to the truth (3 John 1–8).'),
  H('Movement 2 — Diotrephes (vv. 9–10)'),
  P('The elder writes of Diotrephes, who receiveth not the brethren, prates against the elder with malicious words, and casteth them out of the church (3 John 9–10).'),
  H('Movement 3 — Follow Good; Demetrius (vv. 11–12)'),
  P('The elder calls Gaius to follow that which is good and reports the good witness given to Demetrius (3 John 11–12).'),
  H('Movement 4 — Closing (vv. 13–14)'),
  P('The elder has many things to write, hopes to see Gaius shortly, and closes with peace and greetings from friends (3 John 13–14).'))

S(3, 'Program Themes in 3 John',
  H('1. Truth'),
  P('“I have no greater joy than to hear that my children walk in truth” (3 John 4).'),
  H('2. Faithful Service'),
  P('“Thou doest faithfully whatsoever thou doest to the brethren, and to strangers” (3 John 5).'),
  H('3. Fellowhelpers'),
  P('“We therefore ought to receive such, that we might be fellowhelpers to the truth” (3 John 8).'),
  H('4. Pre-eminence'),
  P('Diotrephes is one “who loveth to have the preeminence among them” (3 John 9).'),
  H('5. Good and Evil'),
  P('“He that doeth good is of God: but he that doeth evil hath not seen God” (3 John 11).'),
  H('6. A Good Report'),
  P('“Demetrius hath good report of all men, and of the truth itself” (3 John 12).'))

S(4, 'Christ in 3 John',
  P('3 John does not use the name of the Lord Jesus Christ. It speaks of a name once, and of God:'),
  H('1. For His Name’s Sake'),
  P('Of the brethren and strangers, the letter says “for his name’s sake they went forth, taking nothing of the Gentiles” (3 John 7). The letter itself does not say whose name is meant; this Companion reports the text as written.'),
  H('2. Of God'),
  P('“He that doeth good is of God: but he that doeth evil hath not seen God” (3 John 11).'),
  H('3. The Truth'),
  P('The elder’s joy is that his children walk “in truth” (3 John 4), and he speaks of “the truth itself” (3 John 12).'))

S(5, 'Israel and the Body in 3 John',
  P('The letter is a personal letter and names no program:'),
  L('The letter does not name Israel, does not mention a covenant, and does not use the name the Body of Christ.', 'It names Gaius, Diotrephes, and Demetrius, and speaks of “the church” (3 John 1, 9, 12, 6).', 'It speaks of strangers who went forth “taking nothing of the Gentiles” (3 John 5, 7).', 'It does not state how its readers relate to other programs.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('3 John shows fellowship among believers in practice:'),
  L('faithful service to the brethren and to strangers (3 John 5–6)', 'support for those who went forth “for his name’s sake” (3 John 7–8)', 'a warning about one who loves to have the preeminence (3 John 9–10)', 'a good report and an example to follow (3 John 11–12)'),
  P('It does not give a full account of church order and does not use the name the Body of Christ. It is read on the letter’s own audience markers and setting.'))

S(7, 'Truths Table: What 3 John Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter. “Universal Truth” marks truth that applies to all people, in all time, regardless of program.'),
  TBL(['Category', 'Truth Revealed in 3 John', 'Program Identity', 'Scripture'], [['The Address', 'The elder writes to the wellbeloved Gaius, whom he loves in the truth.', 'Israel / Kingdom / Prophecy Explicit Truth', '3 John 1'], ['Walking in Truth', '“I have no greater joy than to hear that my children walk in truth.”', 'Israel / Kingdom / Prophecy Explicit Truth', '3 John 3–4'], ['Faithful Service', 'Faithful work for the brethren and for strangers, and sending them forward after a godly sort.', 'Israel / Kingdom / Prophecy Explicit Truth', '3 John 5–6'], ['Fellowhelpers', '“We therefore ought to receive such, that we might be fellowhelpers to the truth.”', 'Israel / Kingdom / Prophecy Explicit Truth', '3 John 7–8'], ['Diotrephes', 'One who “loveth to have the preeminence” receiveth not the brethren and casteth them out of the church.', 'Israel / Kingdom / Prophecy Explicit Truth', '3 John 9–10'], ['Follow Good', '“follow not that which is evil, but that which is good.”', 'Universal Truth', '3 John 11'], ['Demetrius', '“Demetrius hath good report of all men, and of the truth itself.”', 'Israel / Kingdom / Prophecy Explicit Truth', '3 John 12'], ['Closing', 'Many things to write; a hope to see him shortly and speak face to face.', 'Israel / Kingdom / Prophecy Explicit Truth', '3 John 13–14']], [18, 32, 27, 23]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Joy in Truth', '“I have no greater joy than to hear that my children walk in truth.”', '3 John 4'], ['Faithful Doing', '“thou doest faithfully whatsoever thou doest.”', '3 John 5'], ['Fellowhelpers', '“fellowhelpers to the truth.”', '3 John 8'], ['Good and Evil', '“He that doeth good is of God: but he that doeth evil hath not seen God.”', '3 John 11'], ['A True Record', '“ye know that our record is true.”', '3 John 12']], [28, 50, 22]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 3 John says to believers, what it reports about Diotrephes and Demetrius, and what holds for all people. It is a personal letter and its instructions are read in that setting.'),
  P('Drawn from 3 John’s instructions and from universal truths. Believers can:'),
  OL('<b>Walk in truth</b> — Let your walk be the joy of those who teach you (3 John 4).', '<b>Serve faithfully</b> — Do well by the brethren and by strangers (3 John 5).', '<b>Help others on their way</b> — Send them forward after a godly sort (3 John 6).', '<b>Be fellowhelpers to the truth</b> — Receive those who go forth (3 John 8).', '<b>Beware the love of pre-eminence</b> — Do not seek first place (3 John 9–10).', '<b>Follow what is good</b> — Turn from what is evil (3 John 11).', '<b>Honour a good report</b> — Value those who have it (3 John 12).', '<b>Meet face to face</b> — Share what ink and pen cannot (3 John 13–14).'))

S(10, "Teaching Outline for 3 John",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Greeting and Wish (vv. 1–2) — The elder and the wellbeloved Gaius. <i>(3 John 1–2)</i>', 'Walking in Truth (vv. 3–4) — The elder’s joy. <i>(3 John 3–4)</i>', 'Faithfulness to the Brethren (vv. 5–8) — Receiving those who go forth. <i>(3 John 5–8)</i>', 'Diotrephes (vv. 9–10) — Pre-eminence and its works. <i>(3 John 9–10)</i>', 'Follow Good (vv. 11–12) — Demetrius and a true record. <i>(3 John 11–12)</i>', 'Closing (vv. 13–14) — Face to face and peace. <i>(3 John 13–14)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 3 John, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, verse by verse, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw on what 3 John itself says to believers and on the truths it states for all people, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 3 John simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for a single lesson. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 3 John is read on the letter’s own audience markers and setting. This Companion shows you how to read the letter in its own setting while drawing out the principles that apply to all believers."))
