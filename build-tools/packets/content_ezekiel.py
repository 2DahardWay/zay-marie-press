# DRAFT for publisher approval.
BOOK = "Ezekiel"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "Glory Departed, Bones Raised, and the Temple Seen"
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
  P('Ezekiel begins “among the captives by the river of Chebar,” where the heavens were opened and he saw visions of God (Ezek. 1:1). He is sent to “the children of Israel, to a rebellious nation” (Ezek. 2:3), is made a watchman, sees the glory depart from the house, speaks of the shepherd and the new heart, sees the valley of bones, and is shown a restored temple and land (Ezek. 3:17; 10:18; 34:23; 36:26; 37:1; 40:2; 43:7).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to the house of Israel in exile about judgment, a new heart and spirit, one shepherd, one nation in the land, and the dwelling of the LORD among them (Ezek. 2:3; 36:24–28; 37:22; 43:7).'))

S(2, "Narrative Flow of Ezekiel",
  H('Movement 1 — The Call and the Glory (Chs. 1–3)'),
  P('Ezekiel sees the likeness of a throne and is sent to a rebellious nation as a watchman (Ezek. 1:26; 2:3; 3:17).'),
  H('Movement 2 — Judgment on Jerusalem (Chs. 4–24)'),
  P('The LORD speaks of the sin of the house, the glory departs from the threshold, and a new heart is promised (Ezek. 10:18; 11:19–20, 23; 18:4, 23, 30).'),
  H('Movement 3 — The Nations (Chs. 25–32)'),
  P('Oracles on the nations that rejoiced at Jerusalem’s fall.'),
  H('Movement 4 — Shepherd, New Heart, and Bones (Chs. 33–37)'),
  P('The watchman is renewed, the LORD seeks His sheep, gathers Israel, gives a new heart, and raises the valley of bones into one nation under David (Ezek. 33:11; 34:11, 23; 36:24–28; 37:11, 21–27).'),
  H('Movement 5 — The Temple and the Land (Chs. 38–48)'),
  P('Gog is spoken of, and the prophet is brought into the land of Israel and shown the house, the glory returning, and the river (Ezek. 38:2; 40:2; 43:2, 7; 47:1, 9).'))

S(3, "Prophecy-Program Themes in Ezekiel",
  H('1. A Rebellious Nation'),
  P('“I send thee to the children of Israel, to a rebellious nation that hath rebelled against me” (Ezek. 2:3).'),
  H('2. The Watchman'),
  P('“I have made thee a watchman unto the house of Israel” (Ezek. 3:17).'),
  H('3. The Glory Departs'),
  P('“The glory of the LORD departed from off the threshold of the house” (Ezek. 10:18).'),
  H('4. A New Heart'),
  P('“A new heart also will I give you, and a new spirit will I put within you” (Ezek. 36:26).'),
  H('5. The Gathering'),
  P('“I will take you from among the heathen, and gather you out of all countries, and will bring you into your own land” (Ezek. 36:24).'),
  H('6. One Nation, One King'),
  P('“I will make them one nation in the land upon the mountains of Israel” (Ezek. 37:22).'),
  H('7. The Covenant of Peace'),
  P('“I will make a covenant of peace with them; it shall be an everlasting covenant with them” (Ezek. 37:26).'))

S(4, "Christ in Ezekiel: The Prophetic Trajectory",
  H('1. The One Shepherd'),
  P('“I will set up one shepherd over them, and he shall feed them, even my servant David” (Ezek. 34:23) is reported as written.'),
  H('2. The Spirit Within'),
  P('“I will put my spirit within you” (Ezek. 36:27) belongs to the new covenant promised to Israel.'),
  H('3. The Valley of Bones'),
  P('“These bones are the whole house of Israel” (Ezek. 37:11) is the LORD’s own explanation of the vision.'))

S(5, "Israel’s Identity in Ezekiel",
  P("Ezekiel reinforces Israel’s:"),
  L('the house of Israel as the exiles addressed (Ezek. 2:3; 3:17)', 'the gathering into their own land (Ezek. 36:24)', 'a new heart and spirit for Israel (Ezek. 36:26)', 'one nation under David in the land (Ezek. 37:22, 24)', 'the LORD dwelling among the children of Israel (Ezek. 43:7)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Ezekiel does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its exile, gathering, new heart, one nation, covenant of peace and temple belong exclusively to Israel; its words on the LORD’s justice and mercy toward the wicked are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Ezekiel", "Program Identity", "Scripture"], [
    ['The Rebellious Nation', '“I send thee to the children of Israel.”', ISR, 'Ezek. 2:3'],
    ['The Watchman', '“I have made thee a watchman unto the house of Israel.”', ISR, 'Ezek. 3:17'],
    ['One Heart', '“I will give them one heart, and I will put a new spirit within you.”', ISR, 'Ezek. 11:19'],
    ['The One Shepherd', '“I will set up one shepherd over them.”', ISR, 'Ezek. 34:23'],
    ['The Gathering', '“I will take you from among the heathen, and gather you out of all countries, and will bring you into your own land.”', ISR, 'Ezek. 36:24'],
    ['A New Heart', '“A new heart also will I give you, and a new spirit will I put within you.”', ISR, 'Ezek. 36:26'],
    ['The House of Israel', '“these bones are the whole house of Israel.”', ISR, 'Ezek. 37:11'],
    ['One Nation', '“I will make them one nation in the land upon the mountains of Israel.”', ISR, 'Ezek. 37:22'],
    ['David as King', '“David my servant shall be king over them.”', ISR, 'Ezek. 37:24'],
    ['A Covenant of Peace', '“I will make a covenant of peace with them.”', ISR, 'Ezek. 37:26'],
    ['The Place of His Throne', '“the place of my throne, and the place of the soles of my feet, where I will dwell in the midst of the children of Israel for ever.”', ISR, 'Ezek. 43:7'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['All Souls Are His', '“all souls are mine; as the soul of the father, so also the soul of the son is mine.”', 'Ezek. 18:4'],
    ['The Soul That Sinneth', '“the soul that sinneth, it shall die.”', 'Ezek. 18:4'],
    ['No Pleasure in Death', '“Have I any pleasure at all that the wicked should die?”', 'Ezek. 18:23'],
    ['Turn and Live', '“I have no pleasure in the death of the wicked; but that the wicked turn from his way and live.”', 'Ezek. 33:11'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s exile, new heart or temple; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Know all souls are His</b> — The LORD holds every life (Ezek. 18:4).', '<b>Take sin seriously</b> — The soul that sinneth shall die (Ezek. 18:4).', '<b>Trust His mercy toward the wicked</b> — He takes no pleasure in death (Ezek. 18:23).', '<b>Turn from wrong</b> — Turn from the way and live (Ezek. 33:11).'))

S(10, "Teaching Outline for Ezekiel",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Call and the Glory (Chs. 1–3) — The watchman sent. <i>(Ezek. 1:26; 2:3; 3:17)</i>', 'Judgment on Jerusalem (Chs. 4–24) — The glory departs. <i>(Ezek. 10:18; 11:19; 18:4, 23)</i>', 'The Nations (Chs. 25–32) — Oracles on the nations.', 'Shepherd, New Heart, and Bones (Chs. 33–37) — The gathering and the nation. <i>(Ezek. 33:11; 34:23; 36:24–28; 37:11, 22)</i>', 'The Temple and the Land (Chs. 38–48) — The house and the glory. <i>(Ezek. 40:2; 43:7; 47:1, 9)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Ezekiel, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward reverence, repentance, and trust in the LORD’s word without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Ezekiel simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Ezekiel stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
