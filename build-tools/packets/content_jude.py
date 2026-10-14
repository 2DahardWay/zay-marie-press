# DRAFT for publisher approval.
BOOK = "Jude"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Contending for the Faith and Kept in the Love of God"
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
  P('Jude is a short letter from “Jude, the servant of Jesus Christ, and brother of James” (Jude 1). He had set out to write of “the common salvation” and found it needful to exhort his readers to “earnestly contend for the faith which was once delivered unto the saints” (Jude 3). The letter speaks about certain men crept in unawares, examples of judgment, Michael and the devil, Enoch’s prophecy, the words of the apostles, keeping yourselves in the love of God, and the One who is able to keep from falling.'),
  BOX("Program Identity:", 'Jude is written “to them that are sanctified by God the Father, and preserved in Jesus Christ, and called” (Jude 1). It is read on the audience markers set out in Section 5. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of Jude',
  H('Movement 1 — Contend for the Faith (vv. 1–4)'),
  P('Jude greets his readers, says he was moved to exhort them to contend for the faith, and tells why: certain men have crept in unawares, ungodly men turning the grace of God into lasciviousness (Jude 1–4).'),
  H('Movement 2 — Examples of Judgment (vv. 5–7)'),
  P('Jude puts them in remembrance of the people saved out of Egypt and afterward destroyed, the angels that kept not their first estate, and Sodom and Gomorrha (Jude 5–7).'),
  H('Movement 3 — These Men (vv. 8–16)'),
  P('Jude describes the dreamers who defile the flesh, tells of Michael and the devil, speaks of the way of Cain, the error of Balaam and the gainsaying of Core, and records Enoch’s prophecy (Jude 8–16).'),
  H('Movement 4 — Remember the Apostles’ Words (vv. 17–19)'),
  P('Jude calls his readers to remember what the apostles told them: that there should be mockers in the last time (Jude 17–19).'),
  H('Movement 5 — Keep Yourselves; the Doxology (vv. 20–25)'),
  P('Jude calls his readers to build up themselves, to pray in the Holy Ghost, to keep themselves in the love of God, to have compassion on some and save others, and closes with praise to the One who is able to keep them from falling (Jude 20–25).'))

S(3, 'Program Themes in Jude',
  H('1. Contending for the Faith'),
  P('Jude exhorts his readers to “earnestly contend for the faith which was once delivered unto the saints” (Jude 3).'),
  H('2. Men Crept In'),
  P('“There are certain men crept in unawares” (Jude 4).'),
  H('3. Examples of Judgment'),
  P('The Lord “afterward destroyed them that believed not” (Jude 5), and the angels are “reserved in everlasting chains under darkness unto the judgment of the great day” (Jude 6).'),
  H('4. The Way of Cain'),
  P('“They have gone in the way of Cain, and ran greedily after the error of Balaam for reward” (Jude 11).'),
  H('5. Enoch’s Prophecy'),
  P('“Behold, the Lord cometh with ten thousands of his saints” (Jude 14).'),
  H('6. Mockers in the Last Time'),
  P('“There should be mockers in the last time” (Jude 18).'),
  H('7. Kept in the Love of God'),
  P('“Keep yourselves in the love of God” (Jude 21).'))

S(4, 'Christ in Jude',
  H('1. The Servant of Jesus Christ'),
  P('Jude calls himself “the servant of Jesus Christ” and writes to those “preserved in Jesus Christ” (Jude 1).'),
  H('2. Our Lord Jesus Christ Denied'),
  P('The men crept in are said to be “denying the only Lord God, and our Lord Jesus Christ” (Jude 4).'),
  H('3. The Words of the Apostles'),
  P('Jude calls his readers to remember “the words which were spoken before of the apostles of our Lord Jesus Christ” (Jude 17).'),
  H('4. The Mercy of Our Lord'),
  P('The readers are to keep themselves in the love of God, “looking for the mercy of our Lord Jesus Christ unto eternal life” (Jude 21).'),
  H('5. God Our Saviour'),
  P('“To the only wise God our Saviour, be glory and majesty, dominion and power, both now and ever” (Jude 25).'))

S(5, 'The Audience of Jude',
  P('The letter’s audience markers are read as written:'),
  L('Jude writes “to them that are sanctified by God the Father, and preserved in Jesus Christ, and called” (Jude 1).', 'Jude calls his readers “Beloved” (Jude 3, 17, 20) and speaks of “the faith which was once delivered unto the saints” (Jude 3).', 'Jude points his readers to what was “spoken before of the apostles of our Lord Jesus Christ” (Jude 17).', 'Jude sets before them the people saved out of the land of Egypt and Sodom and Gomorrha as examples (Jude 5, 7), and records Enoch’s prophecy (Jude 14–15).', 'The letter does not use the name the Body of Christ, and it does not state how its readers relate to other programs.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('Jude is read on its own audience markers. What it commands, warns and promises to its readers is not addressed to the Body of Christ and does not transfer to it. Truths about God that the letter states stand as written:'),
  L('God the Father sanctifies and Jesus Christ preserves (Jude 1)', 'the Lord’s judgment of those who believed not (Jude 5)', 'the Lord’s coming to execute judgment upon all (Jude 14–15)', 'the One who is able to keep from falling and to present faultless (Jude 24)', 'the only wise God our Saviour (Jude 25)'),
  P('Its warnings about the men crept in and its call to contend for the faith are reported as written and are not turned into instructions to the Body.'))

S(7, 'Truths Table: What Jude Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter.'),
  TBL(['Category', 'Truth Revealed in Jude', 'Program Identity', 'Scripture'], [['The Address', 'Jude writes to those “sanctified by God the Father, and preserved in Jesus Christ, and called.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 1'], ['Contend for the Faith', '“earnestly contend for the faith which was once delivered unto the saints.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 3'], ['Men Crept In', 'Certain ungodly men have crept in unawares, “denying the only Lord God, and our Lord Jesus Christ.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 4'], ['Examples of Judgment', 'The people out of Egypt, the angels, and Sodom and Gomorrha are set forth as examples.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 5–7'], ['Michael and the Devil', 'Michael “durst not bring against him a railing accusation, but said, The Lord rebuke thee.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 9'], ['Enoch’s Prophecy', '“Behold, the Lord cometh with ten thousands of his saints, to execute judgment upon all.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 14–15'], ['Mockers', 'The apostles told them that “there should be mockers in the last time.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 17–19'], ['Keep Yourselves', '“Keep yourselves in the love of God, looking for the mercy of our Lord Jesus Christ unto eternal life.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 20–21'], ['Able to Keep', 'He is “able to keep you from falling, and to present you faultless.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Jude 24–25']], [18, 32, 27, 23]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Mercy, Peace, and Love', '“Mercy unto you, and peace, and love, be multiplied.”', 'Jude 2'], ['The Lord Judges', '“to execute judgment upon all.”', 'Jude 15'], ['Able to Keep', '“able to keep you from falling.”', 'Jude 24'], ['The Only Wise God', '“the only wise God our Saviour.”', 'Jude 25'], ['Glory and Power', '“glory and majesty, dominion and power, both now and ever.”', 'Jude 25']], [28, 50, 22]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The table in Section 7 marks every row “Israel / Kingdom / Prophecy Explicit Truth” because Jude is read on its own audience markers. The tables separate what the letter says to its readers from what holds for all people. Its commands, warnings and promises to those readers are not turned into the Body’s. The applications below draw only on the universal truths in Section 8.'),
  P('Drawn from the universal truths of Jude. Readers can:'),
  OL('<b>Receive mercy, peace and love</b> — Let them be multiplied (Jude 2).', '<b>Remember that the Lord judges</b> — Judgment is upon all (Jude 15).', '<b>Rest in the One who keeps</b> — He is able to keep from falling (Jude 24).', '<b>Praise the only wise God</b> — He is our Saviour (Jude 25).', '<b>Give Him glory</b> — Glory and majesty, dominion and power are His (Jude 25).'))

S(10, "Teaching Outline for Jude",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Contend for the Faith (vv. 1–4) — The reason Jude writes. <i>(Jude 1–4)</i>', 'Examples of Judgment (vv. 5–7) — Egypt, the angels, and Sodom. <i>(Jude 5–7)</i>', 'These Men (vv. 8–16) — Michael, Cain, Balaam, Core and Enoch. <i>(Jude 8–16)</i>', 'Remember the Apostles’ Words (vv. 17–19) — Mockers in the last time. <i>(Jude 17–19)</i>', 'Keep Yourselves (vv. 20–23) — Build up, pray, keep, and have compassion. <i>(Jude 20–23)</i>', 'The Doxology (vv. 24–25) — Able to keep, and glory to God. <i>(Jude 24–25)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Jude, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, verse by verse, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on the universal truths Jude itself states, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Jude simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for a single lesson. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Jude is read on the letter’s own audience markers and setting. This Companion shows you how to read the letter in its own setting while drawing out the universal truths it states."))
