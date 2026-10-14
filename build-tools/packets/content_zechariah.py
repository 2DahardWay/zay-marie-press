# DRAFT for publisher approval.
BOOK = "Zechariah"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "Return to the LORD, the Coming King, and the LORD King Over All the Earth"
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
  P('Zechariah is “the word of the LORD unto Zechariah, the son of Berechiah, the son of Iddo the prophet” in the second year of Darius (Zech. 1:1). The book moves through night visions, the high priest and the BRANCH, the King who comes lowly on an ass, the house of David and the Spirit of grace, the fountain opened for sin, and the day when the LORD fights the nations, stands on the mount of Olives and is king over all the earth (Zech. 3:8; 9:9; 12:10; 13:1; 14:3–4, 9).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to Judah, Jerusalem, the house of David and the remnant about return, the King and the Kingdom (Zech. 2:10; 8:3; 12:10; 14:16).'))

S(2, "Narrative Flow of Zechariah",
  H('Movement 1 — Return to the LORD (Chs. 1–2)'),
  P('The people are told to turn to the LORD, and the LORD says He will dwell in the midst of the daughter of Zion (Zech. 1:1, 3; 2:10).'),
  H('Movement 2 — Joshua and the BRANCH (Chs. 3–6)'),
  P('Joshua the high priest stands before the LORD, and the BRANCH is promised, who shall build the temple and sit and rule upon his throne (Zech. 3:8; 4:6; 6:12–13).'),
  H('Movement 3 — Truth, Mercy, and Zion Restored (Chs. 7–8)'),
  P('The LORD says He is returned unto Zion, and the nations take hold of him that is a Jew (Zech. 7:9; 8:3, 16, 23).'),
  H('Movement 4 — The King Cometh (Chs. 9–11)'),
  P('The daughter of Zion is told that her King cometh, lowly and riding upon an ass (Zech. 9:9–10).'),
  H('Movement 5 — The Spirit, the Fountain, and the Day (Chs. 12–14)'),
  P('The LORD pours the spirit of grace on the house of David, opens a fountain for sin, and becomes king over all the earth (Zech. 12:10; 13:1; 14:3–4, 9, 16, 20).'))

S(3, "Prophecy-Program Themes in Zechariah",
  H('1. Turn Ye Unto Me'),
  P('“Turn ye unto me, saith the LORD of hosts, and I will turn unto you” (Zech. 1:3).'),
  H('2. Not by Might'),
  P('“Not by might, nor by power, but by my spirit, saith the LORD of hosts” (Zech. 4:6).'),
  H('3. The BRANCH'),
  P('“Behold the man whose name is The BRANCH; and he shall grow up out of his place, and he shall build the temple of the LORD” (Zech. 6:12).'),
  H('4. The LORD Dwells in Zion'),
  P('“I am returned unto Zion, and will dwell in the midst of Jerusalem” (Zech. 8:3).'),
  H('5. The King Cometh'),
  P('“Behold, thy King cometh unto thee: he is just, and having salvation” (Zech. 9:9).'),
  H('6. The Spirit of Grace'),
  P('“I will pour upon the house of David, and upon the inhabitants of Jerusalem, the spirit of grace and of supplications” (Zech. 12:10).'),
  H('7. King Over All the Earth'),
  P('“The LORD shall be king over all the earth: in that day shall there be one LORD, and his name one” (Zech. 14:9).'))

S(4, "Christ in Zechariah: The Prophetic Trajectory",
  H('1. The BRANCH'),
  P('The BRANCH who builds the temple and sits and rules upon his throne (Zech. 3:8; 6:12–13) is reported as written.'),
  H('2. The King on an Ass'),
  P('Zechariah 9:9 is quoted in Matthew 21:5; the New Testament quotation is read in its own chapter.'),
  H('3. They Shall Look on Me'),
  P('“They shall look upon me whom they have pierced” (Zech. 12:10) is reported as written, with the pouring of the spirit of grace on the house of David and Jerusalem.'))

S(5, "Israel’s Identity in Zechariah",
  P("Zechariah reinforces Israel’s:"),
  L('Joshua the high priest and the BRANCH (Zech. 3:8; 6:12–13)', 'the daughter of Zion, Jerusalem and the holy mountain (Zech. 2:10; 8:3)', 'the house of David and the inhabitants of Jerusalem (Zech. 12:10; 13:1)', 'the nations coming up to worship the King, the LORD of hosts (Zech. 14:16)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Zechariah does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its BRANCH, its King, its pouring out on the house of David and its day of the LORD belong exclusively to Israel; its words on truth and mercy toward a neighbour are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Zechariah", "Program Identity", "Scripture"], [
    ['The Word of the LORD', '“came the word of the LORD unto Zechariah.”', ISR, 'Zech. 1:1'],
    ['The BRANCH', '“I will bring forth my servant the BRANCH.”', ISR, 'Zech. 3:8'],
    ['The Temple Built', '“he shall build the temple of the LORD.”', ISR, 'Zech. 6:12'],
    ['Seated and Ruling', '“shall sit and rule upon his throne.”', ISR, 'Zech. 6:13'],
    ['Dwelling in Jerusalem', '“I am returned unto Zion, and will dwell in the midst of Jerusalem.”', ISR, 'Zech. 8:3'],
    ['The Nations and the Jew', '“ten men shall take hold out of all languages of the nations, even shall take hold of the skirt of him that is a Jew.”', ISR, 'Zech. 8:23'],
    ['The King Cometh', '“thy King cometh unto thee.”', ISR, 'Zech. 9:9'],
    ['Dominion Sea to Sea', '“his dominion shall be from sea even to sea.”', ISR, 'Zech. 9:10'],
    ['Spirit of Grace', '“I will pour upon the house of David, and upon the inhabitants of Jerusalem, the spirit of grace and of supplications.”', ISR, 'Zech. 12:10'],
    ['A Fountain Opened', '“there shall be a fountain opened to the house of David and to the inhabitants of Jerusalem for sin and for uncleanness.”', ISR, 'Zech. 13:1'],
    ['Feet on the Mount', '“his feet shall stand in that day upon the mount of Olives.”', ISR, 'Zech. 14:4'],
    ['King Over All', '“the LORD shall be king over all the earth.”', ISR, 'Zech. 14:9'],
    ['The Feast of Tabernacles', '“go up from year to year to worship the King, the LORD of hosts, and to keep the feast of tabernacles.”', ISR, 'Zech. 14:16'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Turn to Him', '“Turn ye unto me, saith the LORD of hosts, and I will turn unto you.”', 'Zech. 1:3'],
    ['By His Spirit', '“Not by might, nor by power, but by my spirit, saith the LORD of hosts.”', 'Zech. 4:6'],
    ['True Judgment and Mercy', '“Execute true judgment, and shew mercy and compassions every man to his brother.”', 'Zech. 7:9'],
    ['Speak the Truth', '“Speak ye every man the truth to his neighbour.”', 'Zech. 8:16'],
    ['No Evil in the Heart', '“let none of you imagine evil in your hearts against his neighbour.”', 'Zech. 8:17'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the BRANCH, the King or the day of the LORD; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Turn to the LORD</b> — He promises to turn to those who turn (Zech. 1:3).', '<b>Rely on His Spirit</b> — Not by might nor power (Zech. 4:6).', '<b>Execute true judgment and show mercy</b> — Every man to his brother (Zech. 7:9).', '<b>Speak the truth</b> — To your neighbour (Zech. 8:16).', '<b>Keep evil out of the heart</b> — Toward your neighbour (Zech. 8:17).'))

S(10, "Teaching Outline for Zechariah",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Return to the LORD (Chs. 1–2) — Turn ye unto me. <i>(Zech. 1:3; 2:10)</i>', 'Joshua and the BRANCH (Chs. 3–6) — Not by might. <i>(Zech. 3:8; 4:6; 6:12–13)</i>', 'Truth, Mercy, and Zion Restored (Chs. 7–8) — The LORD in Jerusalem. <i>(Zech. 7:9; 8:3, 16–17, 23)</i>', 'The King Cometh (Chs. 9–11) — Lowly on an ass. <i>(Zech. 9:9–10)</i>', 'The Spirit, the Fountain, and the Day (Chs. 12–14) — King over all the earth. <i>(Zech. 12:10; 13:1; 14:4, 9, 16)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Zechariah, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward truth, mercy, and dependence on the LORD’s Spirit without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Zechariah simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Zechariah stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
