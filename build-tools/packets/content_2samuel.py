# DRAFT for publisher approval.
BOOK = "2 Samuel"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "David’s Reign, the Covenant Promise, and the Cost of His Sin"
SECTIONS = []
def S(n, t, *blocks): SECTIONS.append((n, t, list(blocks)))
P = lambda x: ("p", x)
L = lambda *xs: ("ul", list(xs))
H = lambda x: ("h3", x)
TBL = lambda head, rows, widths: ("table", head, rows, widths)
OL = lambda *xs: ("ol", list(xs))
OLR = lambda *xs: ("olr", list(xs))
BOX = lambda lead, text: ("box", lead, text)
ISR = 'Israel / Kingdom / Prophecy Explicit Truth'

S(1, "Book Overview (Program-Aware)",
  P('2 Samuel follows David from his anointing over Judah and then over all Israel, to the establishment of his kingdom and the promise of an enduring house. It records the LORD’s covenant with David through Nathan, David’s sin with Bathsheba and Nathan’s rebuke, the troubles of his house, David’s song of praise, and the numbering of the people and the purchase of the threshingfloor (2 Sam. 5:3; 7:12–16; 11:27; 12:7, 13; 22:2; 24:24).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD establishes David’s house and kingdom over Israel in the land (2 Sam. 5:12; 7:16).'))

S(2, "Narrative Flow of 2 Samuel",
  H('Movement 1 — David Becomes King (Chs. 1–5)'),
  P('The elders of Israel anoint David king in Hebron, he reigns forty years, and he perceives that the LORD has established him (2 Sam. 5:3–4, 12).'),
  H('Movement 2 — The Covenant with David (Chs. 6–10)'),
  P('The LORD tells David through Nathan that He will set up his seed, establish his kingdom and be his seed’s father (2 Sam. 7:8, 12–14, 16, 22, 28).'),
  H('Movement 3 — David’s Sin and Its Consequences (Chs. 11–20)'),
  P('David’s sin displeases the LORD, Nathan says, “Thou art the man,” and David says, “I have sinned against the LORD” (2 Sam. 11:27; 12:7, 13).'),
  H('Movement 4 — David’s Song and the Last Words (Chs. 21–24)'),
  P('David praises the LORD as his rock and speaks of an everlasting covenant, and buys the threshingfloor (2 Sam. 22:2, 31; 23:2, 5; 24:14, 24).'))

S(3, "Prophecy-Program Themes in 2 Samuel",
  H('1. The King Anointed'),
  P('“They anointed David king over Israel” (2 Sam. 5:3).'),
  H('2. The Kingdom Established'),
  P('“David perceived that the LORD had established him king over Israel, and that he had exalted his kingdom for his people Israel’s sake” (2 Sam. 5:12).'),
  H('3. An Enduring House'),
  P('“Thine house and thy kingdom shall be established for ever before thee: thy throne shall be established for ever” (2 Sam. 7:16).'),
  H('4. A Son of David'),
  P('“He shall build an house for my name, and I will stablish the throne of his kingdom for ever” (2 Sam. 7:13).'),
  H('5. An Everlasting Covenant'),
  P('“He hath made with me an everlasting covenant, ordered in all things, and sure” (2 Sam. 23:5).'))

S(4, "Christ in 2 Samuel: The Prophetic Trajectory",
  H('1. The Davidic Covenant'),
  P('The LORD’s promise of a seed, a house, a kingdom and a throne for ever (2 Sam. 7:12–16) belongs to Israel’s prophetic kingdom hope.'),
  H('2. The Son and the Father'),
  P('“I will be his father, and he shall be my son” (2 Sam. 7:14) is quoted in the New Testament and is reported here as written.'),
  H('3. David’s Last Words'),
  P('David says “the Spirit of the LORD spake by me, and his word was in my tongue” (2 Sam. 23:2).'))

S(5, "Israel’s Identity in 2 Samuel",
  P("2 Samuel reinforces Israel’s:"),
  L('the throne and house of David (2 Sam. 7:12–16)', 'kingdom over Israel in the land (2 Sam. 5:12)', 'the everlasting covenant (2 Sam. 23:5)', 'the altar at the threshingfloor (2 Sam. 24:24)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("2 Samuel does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its Davidic covenant, throne, kingdom and altar belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in 2 Samuel", "Program Identity", "Scripture"], [
    ['David Anointed King', '“they anointed David king over Israel.”', ISR, '2 Sam. 5:3'],
    ['The Kingdom Established', '“the LORD had established him king over Israel.”', ISR, '2 Sam. 5:12'],
    ['A Seed After Him', '“I will set up thy seed after thee… and I will establish his kingdom.”', ISR, '2 Sam. 7:12'],
    ['The Throne for Ever', '“I will stablish the throne of his kingdom for ever.”', ISR, '2 Sam. 7:13'],
    ['Father and Son', '“I will be his father, and he shall be my son.”', ISR, '2 Sam. 7:14'],
    ['House and Kingdom', '“thy throne shall be established for ever.”', ISR, '2 Sam. 7:16'],
    ['The Everlasting Covenant', '“he hath made with me an everlasting covenant, ordered in all things, and sure.”', ISR, '2 Sam. 23:5'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The LORD Is Incomparable', '“there is none like thee, neither is there any God beside thee.”', '2 Sam. 7:22'],
    ['His Words Are True', '“thou art that God, and thy words be true.”', '2 Sam. 7:28'],
    ['Sin Is Confessed and Put Away', '“I have sinned against the LORD. And Nathan said unto David, The LORD also hath put away thy sin.”', '2 Sam. 12:13'],
    ['The LORD Is a Refuge', '“The LORD is my rock, and my fortress, and my deliverer.”', '2 Sam. 22:2'],
    ['His Way Is Perfect', '“As for God, his way is perfect.”', '2 Sam. 22:31'],
    ['Great Mercies', '“for his mercies are great.”', '2 Sam. 24:14'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s throne, house or kingdom promises; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Confess sin</b> — David said, “I have sinned” (2 Sam. 12:13).', '<b>Trust the true word of God</b> — His words are true (2 Sam. 7:28).', '<b>Take refuge in the LORD</b> — He is a rock and a fortress (2 Sam. 22:2).', '<b>Rely on His perfect way</b> — His way is perfect (2 Sam. 22:31).', '<b>Fall on His mercies</b> — They are great (2 Sam. 24:14).'))

S(10, "Teaching Outline for 2 Samuel",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('David Becomes King (Chs. 1–5) — Anointed over Israel. <i>(2 Sam. 5:3–4, 12)</i>', 'The Covenant with David (Chs. 6–10) — House, kingdom and throne. <i>(2 Sam. 7:8, 12–14, 16)</i>', 'David’s Sin (Chs. 11–20) — Thou art the man. <i>(2 Sam. 11:27; 12:7, 13)</i>', 'Song and Last Words (Chs. 21–24) — The everlasting covenant. <i>(2 Sam. 22:2, 31; 23:5; 24:14, 24)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 Samuel, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward repentance, trust, and humility without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 Samuel simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 2 Samuel stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
