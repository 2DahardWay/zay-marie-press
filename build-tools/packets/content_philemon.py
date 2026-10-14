# DRAFT for publisher approval.
BOOK = "Philemon"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "A Brother Beloved, Received as Paul Himself"
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
  P('Philemon is a short letter from “Paul, a prisoner of Jesus Christ, and Timothy our brother” to “Philemon our dearly beloved, and fellowlabourer,” with Apphia, Archippus, and the church in his house (Philem. 1–2). Paul appeals for Onesimus, whom he calls his son begotten in his bonds, and asks Philemon to receive him as a brother beloved (Philem. 10, 16).'),
  BOX("Program Identity:", 'Philemon is a personal letter from Paul to a believer and his household church. It is read for what it says about love, reconciliation, and Christian fellowship. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of Philemon',
  H('Movement 1 — Greeting and Thanksgiving (vv. 1–7)'),
  P('Paul greets Philemon and the church in his house and gives thanks for his love and faith toward the Lord Jesus and toward all saints (Philem. 1–7).'),
  H('Movement 2 — The Appeal for Onesimus (vv. 8–16)'),
  P('Paul beseeches Philemon for love’s sake on behalf of Onesimus, now profitable, sent back, and to be received no longer merely as a servant but as a brother beloved (Philem. 8–16).'),
  H('Movement 3 — Receive Him as Myself (vv. 17–25)'),
  P('Paul asks Philemon to receive Onesimus as himself, offers to repay any loss, expresses confidence in him, and closes with grace (Philem. 17–25).'))

S(3, 'Program Themes in Philemon',
  H('1. Love and Faith Toward All'),
  P('Paul hears of Philemon’s love and faith toward the Lord Jesus and all saints (Philem. 5).'),
  H('2. An Appeal Rather Than a Command'),
  P('Paul, though bold enough to enjoin, rather beseeches for love’s sake (Philem. 8–9).'),
  H('3. A Brother Beloved'),
  P('Onesimus is to be received “not now as a servant, but above a servant, a brother beloved” (Philem. 16).'),
  H('4. Partnership'),
  P('“If thou count me therefore a partner, receive him as myself” (Philem. 17).'),
  H('5. Refreshed Hearts'),
  P('Paul wants Philemon to refresh his bowels in the Lord (Philem. 20).'))

S(4, 'Christ in Philemon',
  H('1. Our Lord Jesus Christ'),
  P('Grace and peace come from God our Father and the Lord Jesus Christ (Philem. 3).'),
  H('2. The Lord Jesus'),
  P('Philemon’s love and faith are toward the Lord Jesus (Philem. 5).'),
  H('3. In Christ'),
  P('Paul speaks of “much boldness in Christ” and of the good that is in them “in Christ Jesus” (Philem. 6, 8).'),
  H('4. In the Lord'),
  P('Paul appeals to Philemon to refresh his heart “in the Lord” (Philem. 20).'),
  H('5. The Grace of Our Lord'),
  P('The letter closes: “The grace of our Lord Jesus Christ be with your spirit” (Philem. 25).'))

S(5, 'Israel and the Body in Philemon',
  P('The letter is a personal appeal and speaks of no covenant or program:'),
  L('Paul calls himself “a prisoner of Jesus Christ” (Philem. 1, 9).', 'The letter names Philemon, Apphia, Archippus, and the church in his house (Philem. 1–2).', 'The letter does not mention Israel and does not place believers inside any covenant.', 'The letter does not make a doctrine of slavery; it reports Paul’s appeal for one man, Onesimus.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('Philemon shows the Body’s fellowship in Christ in practice:'),
  L('a church gathered in a house', 'love and faith toward the Lord Jesus and all saints', 'a brother received above a servant', 'partnership and substitution offered in love', 'grace closing the letter'),
  P('It does not give a general rule on household relations beyond what Paul writes here.'))

S(7, 'Truths Table: What Philemon Says',
  P('Program Identity shows how each passage is classified. “Addressed to Believers (Identity / Doctrine)” marks teaching for believers. “Addressed to Believers (Warnings / Corrections)” marks warnings, corrections, exhortations, and future conditions believers must prepare for. “Text Only” marks a passage with no instructional force, such as a greeting or a background statement.'),
  TBL(['Category', 'Truth Revealed in Philemon', 'Program Identity', 'Scripture'], [['Love and Faith', 'Love and faith toward the Lord Jesus and all saints.', 'Addressed to Believers (Identity / Doctrine)', 'Philem. 5'], ['Fellowship of Faith', 'The communication of thy faith becomes effectual.', 'Addressed to Believers (Identity / Doctrine)', 'Philem. 6'], ['Appeal for Love’s Sake', 'Paul beseeches rather than commands.', 'Addressed to Believers (Identity / Doctrine)', 'Philem. 8–9'], ['A Brother Beloved', 'Onesimus is more than a servant, a brother beloved.', 'Addressed to Believers (Identity / Doctrine)', 'Philem. 16'], ['Partnership', 'Receive him as myself.', 'Addressed to Believers (Identity / Doctrine)', 'Philem. 17'], ['Substitution Offered', 'Put that on mine account; I will repay it.', 'Addressed to Believers (Identity / Doctrine)', 'Philem. 18–19'], ['A House Church', 'The church in thy house.', 'Addressed to Believers (Identity / Doctrine)', 'Philem. 2'], ['Appeal as a Prisoner', 'Paul appeals as the aged and now a prisoner of Jesus Christ.', 'Addressed to Believers (Warnings / Corrections)', 'Philem. 9']], [20, 36, 26, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Thanksgiving in Prayer', 'I thank my God, making mention of thee always in my prayers.', 'Philem. 4'], ['Refresh the Saints', 'The bowels of the saints are refreshed by thee, brother.', 'Philem. 7'], ['Love’s Appeal', 'For love’s sake I rather beseech thee.', 'Philem. 9'], ['Willing Service', 'Do not let thy benefit be as it were of necessity, but willingly.', 'Philem. 14'], ['Receive as a Brother', 'Receive him forever, a brother beloved.', 'Philem. 15–16'], ['Bear a Debt', 'If he hath wronged thee, or oweth thee ought, put that on mine account.', 'Philem. 18'], ['Obedience', 'Having confidence in thy obedience I wrote unto thee.', 'Philem. 21'], ['Prayer and Hope', 'I trust that through your prayers I shall be given unto you.', 'Philem. 22']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what Philemon says to believers, what it reports about the house church and Paul’s imprisonment, and what holds for all people. It is a personal letter and its instructions are read in that setting.'),
  P('Drawn from Philemon’s appeal and from universal truths. The Body of Christ should:'),
  OL('<b>Love all the saints</b> — Show love and faith toward all (Philem. 5).', '<b>Share faith in practice</b> — Let fellowship become effectual (Philem. 6).', '<b>Appeal in love</b> — Persuade rather than command (Philem. 9).', '<b>Receive as a brother</b> — Welcome one who has been apart (Philem. 15–16).', '<b>Bear another’s debt</b> — Stand beside one who owes (Philem. 18–19).', '<b>Refresh one another</b> — Give joy in the Lord (Philem. 7, 20).', '<b>Give willingly</b> — Do good freely, not by compulsion (Philem. 14).', '<b>Pray for one another</b> — Hold hope together in prayer (Philem. 22).'))

S(10, "Teaching Outline for Philemon",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Thanksgiving (vv. 1–7) — Love and faith toward all. <i>(Philem. 4–7)</i>', 'Love’s Appeal (vv. 8–11) — Paul beseeches for Onesimus. <i>(Philem. 8–11)</i>', 'Sent Back (vv. 12–14) — Not by necessity, but willingly. <i>(Philem. 12–14)</i>', 'A Brother Beloved (vv. 15–16) — Received above a servant. <i>(Philem. 15–16)</i>', 'As Myself (vv. 17–19) — Partnership and substitution. <i>(Philem. 17–19)</i>', 'Refresh My Heart (vv. 20–22) — Confidence and a hope of visiting. <i>(Philem. 20–22)</i>', 'Greetings and Grace (vv. 23–25) — Fellowlabourers and the grace of our Lord. <i>(Philem. 23–25)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Philemon, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what Philemon itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Philemon simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Philemon was written during the overlap as a personal letter from Paul. This Companion shows you how to read the appeal in its own setting while drawing out the principles that apply to all believers."))
