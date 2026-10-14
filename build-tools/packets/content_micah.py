# DRAFT for publisher approval.
BOOK = "Micah"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "Judgment on Samaria and Jerusalem, and the Mountain of the LORD’s House"
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
  P('Micah is “the word of the LORD that came to Micah the Morasthite in the days of Jotham, Ahaz, and Hezekiah, kings of Judah, which he saw concerning Samaria and Jerusalem” (Mic. 1:1). It speaks judgment on Samaria and Jerusalem, promises that “in the last days” the mountain of the house of the LORD shall be established, names the ruler to come from Bethlehem, and closes with a prayer to the God who pardons iniquity (Mic. 3:12; 4:1; 5:2; 7:18).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to Jacob and Israel, to Zion and Jerusalem, about judgment, the remnant, the ruler from Bethlehem and the last days (Mic. 3:8; 4:1–2; 5:3; 7:20).'))

S(2, "Narrative Flow of Micah",
  H('Movement 1 — Judgment on Samaria and Jerusalem (Chs. 1–3)'),
  P('The LORD comes against Samaria and Jerusalem, and Zion is plowed as a field (Mic. 1:1; 3:8, 12).'),
  H('Movement 2 — The Last Days (Ch. 4)'),
  P('The mountain of the LORD’s house is established, the nations go up, and every man sits under his vine and fig tree (Mic. 4:1–4).'),
  H('Movement 3 — The Ruler From Bethlehem (Ch. 5)'),
  P('A ruler comes forth out of Bethlehem Ephratah, and the remnant of his brethren return (Mic. 5:3–5).'),
  H('Movement 4 — The LORD’s Controversy (Ch. 6)'),
  P('The LORD pleads with His people and shows what He requires (Mic. 6:8).'),
  H('Movement 5 — Waiting and Pardon (Ch. 7)'),
  P('The prophet waits for the God of his salvation and closes with the God who pardons (Mic. 7:7, 9, 18–20).'))

S(3, "Prophecy-Program Themes in Micah",
  H('1. Judgment Declared'),
  P('The LORD’s word is “concerning Samaria and Jerusalem” (Mic. 1:1).'),
  H('2. Zion Plowed'),
  P('“Zion for your sake be plowed as a field, and Jerusalem shall become heaps” (Mic. 3:12).'),
  H('3. The Last Days'),
  P('“In the last days it shall come to pass, that the mountain of the house of the LORD shall be established” (Mic. 4:1).'),
  H('4. The Law From Zion'),
  P('“The law shall go forth of Zion, and the word of the LORD from Jerusalem” (Mic. 4:2).'),
  H('5. War No More'),
  P('“Nation shall not lift up a sword against nation, neither shall they learn war any more” (Mic. 4:3).'),
  H('6. The Remnant Return'),
  P('“The remnant of his brethren shall return unto the children of Israel” (Mic. 5:3).'),
  H('7. The Oath to the Fathers'),
  P('“Thou wilt perform the truth to Jacob, and the mercy to Abraham” (Mic. 7:20).'))

S(4, "Christ in Micah: The Prophetic Trajectory",
  H('1. The Ruler From Bethlehem'),
  P('The ruler whose goings forth are from of old comes out of Bethlehem Ephratah (Mic. 5:2); the chief priests and scribes quote the place in Matthew 2:5–6.'),
  H('2. He Shall Be the Peace'),
  P('“This man shall be the peace” (Mic. 5:5), and “he shall stand and feed in the strength of the LORD” (Mic. 5:4).'),
  H('3. A Kingdom Without War'),
  P('The nations’ swords are beaten into plowshares in the last days (Mic. 4:3), reported within Israel’s kingdom hope.'))

S(5, "Israel’s Identity in Micah",
  P("Micah reinforces Israel’s:"),
  L('Jacob and Israel told their transgression (Mic. 3:8)', 'Zion and Jerusalem, and the mountain of the LORD’s house (Mic. 3:12; 4:1–2)', 'the remnant of his brethren returning to the children of Israel (Mic. 5:3)', 'the truth to Jacob and the mercy to Abraham sworn to the fathers (Mic. 7:20)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Micah does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its judgment on Samaria and Jerusalem, the last-days mountain, the ruler from Bethlehem and the oath to Jacob belong exclusively to Israel; its words on justice, mercy and humility are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Micah", "Program Identity", "Scripture"], [
    ['The Word Concerning Samaria', '“which he saw concerning Samaria and Jerusalem.”', ISR, 'Mic. 1:1'],
    ['Jacob Told His Sin', '“to declare unto Jacob his transgression, and to Israel his sin.”', ISR, 'Mic. 3:8'],
    ['Zion Plowed', '“Zion for your sake be plowed as a field.”', ISR, 'Mic. 3:12'],
    ['The Mountain Established', '“the mountain of the house of the LORD shall be established in the top of the mountains.”', ISR, 'Mic. 4:1'],
    ['The Law From Zion', '“the law shall go forth of Zion, and the word of the LORD from Jerusalem.”', ISR, 'Mic. 4:2'],
    ['War No More', '“nation shall not lift up a sword against nation, neither shall they learn war any more.”', ISR, 'Mic. 4:3'],
    ['Vine and Fig Tree', '“they shall sit every man under his vine and under his fig tree.”', ISR, 'Mic. 4:4'],
    ['The Remnant Return', '“the remnant of his brethren shall return unto the children of Israel.”', ISR, 'Mic. 5:3'],
    ['He Shall Feed', '“he shall stand and feed in the strength of the LORD.”', ISR, 'Mic. 5:4'],
    ['The Truth to Jacob', '“Thou wilt perform the truth to Jacob, and the mercy to Abraham.”', ISR, 'Mic. 7:20'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['What the LORD Requires', '“to do justly, and to love mercy, and to walk humbly with thy God.”', 'Mic. 6:8'],
    ['Waiting on God', '“I will wait for the God of my salvation: my God will hear me.”', 'Mic. 7:7'],
    ['Bearing Discipline', '“I will bear the indignation of the LORD, because I have sinned against him.”', 'Mic. 7:9'],
    ['A God Like No Other', '“Who is a God like unto thee, that pardoneth iniquity.”', 'Mic. 7:18'],
    ['Sins Cast Away', '“thou wilt cast all their sins into the depths of the sea.”', 'Mic. 7:19'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the last days, Zion or the ruler from Bethlehem; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Do justly</b> — Love mercy and walk humbly (Mic. 6:8).', '<b>Wait on God</b> — The God of my salvation will hear (Mic. 7:7).', '<b>Bear His discipline humbly</b> — Until He pleads my cause (Mic. 7:9).', '<b>Marvel at His pardon</b> — Who is a God like unto thee (Mic. 7:18).', '<b>Rest in His forgiveness</b> — Sins cast into the depths of the sea (Mic. 7:19).'))

S(10, "Teaching Outline for Micah",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Judgment on Samaria and Jerusalem (Chs. 1–3) — Zion plowed. <i>(Mic. 1:1; 3:8, 12)</i>', 'The Last Days (Ch. 4) — The mountain of the LORD’s house. <i>(Mic. 4:1–4)</i>', 'The Ruler From Bethlehem (Ch. 5) — The remnant return. <i>(Mic. 5:3–5)</i>', 'The LORD’s Controversy (Ch. 6) — What He requires. <i>(Mic. 6:8)</i>', 'Waiting and Pardon (Ch. 7) — A God who pardons. <i>(Mic. 7:7, 9, 18–20)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Micah, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward justice, mercy, humility, and hope in the LORD without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Micah simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Micah stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
