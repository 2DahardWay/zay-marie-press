# DRAFT for publisher approval.
BOOK = "Amos"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Herdman’s Warning, the Roaring LORD, and David’s Tabernacle Raised"
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
  P('Amos is “the words of Amos, who was among the herdmen of Tekoa, which he saw concerning Israel” (Amos 1:1). He begins with the LORD roaring from Zion, speaks judgment over the nations and over Israel, is sent to “my people Israel,” and closes with visions of the end and the promise to raise up the tabernacle of David and plant Israel upon their land (Amos 1:2; 7:15; 9:11, 14–15).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to the house of Israel about judgment, a famine of hearing, and a restoration to the land under the raised tabernacle of David (Amos 3:2; 5:4; 8:11; 9:11, 15).'))

S(2, "Narrative Flow of Amos",
  H('Movement 1 — Judgment on the Nations (Chs. 1–2)'),
  P('The LORD roars from Zion and pronounces judgment on the nations round about and on Israel (Amos 1:2).'),
  H('Movement 2 — Hear This Word (Chs. 3–6)'),
  P('The only family the LORD has known is told to prepare to meet its God, and is told to seek good and let judgment run down (Amos 3:2–3, 7; 4:12; 5:4, 14, 18, 24).'),
  H('Movement 3 — The Visions and the Herdman (Chs. 7–8)'),
  P('Amos answers Amaziah and is told to prophesy to Israel; the end is come, and a famine of hearing is promised (Amos 7:14–15; 8:2, 11).'),
  H('Movement 4 — The Restoration (Ch. 9)'),
  P('The LORD will raise up David’s tabernacle, bring again the captivity of Israel, and plant them on their land (Amos 9:11, 14–15).'))

S(3, "Prophecy-Program Themes in Amos",
  H('1. The Only Family Known'),
  P('“You only have I known of all the families of the earth: therefore I will punish you for all your iniquities” (Amos 3:2).'),
  H('2. Walking Together'),
  P('“Can two walk together, except they be agreed?” (Amos 3:3).'),
  H('3. Prepare to Meet Thy God'),
  P('“Prepare to meet thy God, O Israel” (Amos 4:12).'),
  H('4. Seek Good'),
  P('“Seek good, and not evil, that ye may live” (Amos 5:14).'),
  H('5. Justice Like Waters'),
  P('“Let judgment run down as waters, and righteousness as a mighty stream” (Amos 5:24).'),
  H('6. A Famine of Hearing'),
  P('“A famine in the land, not a famine of bread, nor a thirst for water, but of hearing the words of the LORD” (Amos 8:11).'),
  H('7. David’s Tabernacle'),
  P('“In that day will I raise up the tabernacle of David that is fallen” (Amos 9:11).'))

S(4, "Christ in Amos: The Prophetic Trajectory",
  H('1. The Tabernacle of David'),
  P('“In that day will I raise up the tabernacle of David that is fallen” (Amos 9:11) is quoted in Acts at the council at Jerusalem (Acts 15:16–17); both passages are reported as written.'),
  H('2. The Herdman Sent'),
  P('Amos says, “the LORD took me as I followed the flock” (Amos 7:15).'),
  H('3. The Restored Land'),
  P('“I will plant them upon their land” (Amos 9:15).'))

S(5, "Israel’s Identity in Amos",
  P("Amos reinforces Israel’s:"),
  L('Israel as the people the LORD has known (Amos 3:2)', 'the house of Israel told to seek the LORD (Amos 5:4)', 'a famine of hearing in the land (Amos 8:11)', 'the tabernacle of David raised and the captivity brought again (Amos 9:11, 14)', 'Israel planted upon the land the LORD gave them (Amos 9:15)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Amos does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its judgment on Israel, the famine of hearing, the tabernacle of David and the planting on the land belong exclusively to Israel; its words on justice and on the LORD’s word are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Amos", "Program Identity", "Scripture"], [
    ['Concerning Israel', '“which he saw concerning Israel.”', ISR, 'Amos 1:1'],
    ['The LORD Roars From Zion', '“The LORD will roar from Zion, and utter his voice from Jerusalem.”', ISR, 'Amos 1:2'],
    ['The Only Family', '“You only have I known of all the families of the earth.”', ISR, 'Amos 3:2'],
    ['Prepare to Meet Thy God', '“prepare to meet thy God, O Israel.”', ISR, 'Amos 4:12'],
    ['Seek Ye Me', '“thus saith the LORD unto the house of Israel, Seek ye me, and ye shall live.”', ISR, 'Amos 5:4'],
    ['Sent to My People', '“Go, prophesy unto my people Israel.”', ISR, 'Amos 7:15'],
    ['The End Is Come', '“The end is come upon my people of Israel.”', ISR, 'Amos 8:2'],
    ['A Famine of Hearing', '“not a famine of bread, nor a thirst for water, but of hearing the words of the LORD.”', ISR, 'Amos 8:11'],
    ['David’s Tabernacle', '“will I raise up the tabernacle of David that is fallen.”', ISR, 'Amos 9:11'],
    ['The Captivity Brought Again', '“I will bring again the captivity of my people of Israel.”', ISR, 'Amos 9:14'],
    ['Planted on Their Land', '“I will plant them upon their land.”', ISR, 'Amos 9:15'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Walking Together', '“Can two walk together, except they be agreed?”', 'Amos 3:3'],
    ['The Prophets Told', '“the Lord GOD will do nothing, but he revealeth his secret unto his servants the prophets.”', 'Amos 3:7'],
    ['Seek Good', '“Seek good, and not evil, that ye may live.”', 'Amos 5:14'],
    ['Justice Like Waters', '“let judgment run down as waters, and righteousness as a mighty stream.”', 'Amos 5:24'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant judgments or David’s tabernacle; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Walk in agreement</b> — Two walk together if agreed (Amos 3:3).', '<b>Receive what He reveals</b> — He tells His servants the prophets (Amos 3:7).', '<b>Seek good</b> — And not evil (Amos 5:14).', '<b>Let justice run</b> — Like waters and a mighty stream (Amos 5:24).'))

S(10, "Teaching Outline for Amos",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Judgment on the Nations (Chs. 1–2) — The roaring LORD. <i>(Amos 1:2)</i>', 'Hear This Word (Chs. 3–6) — The only family known. <i>(Amos 3:2–3, 7; 4:12; 5:4, 14, 24)</i>', 'The Visions and the Herdman (Chs. 7–8) — A famine of hearing. <i>(Amos 7:14–15; 8:2, 11)</i>', 'The Restoration (Ch. 9) — David’s tabernacle and the land. <i>(Amos 9:11, 14–15)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Amos, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward justice, humility, and attention to the word of the LORD without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Amos simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Amos stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
