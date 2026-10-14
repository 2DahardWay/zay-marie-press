# DRAFT for publisher approval.
BOOK = "Habakkuk"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Prophet’s Question, the Vision That Tarries, and Joy in the God of Salvation"
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
  P('Habakkuk is “the burden which Habakkuk the prophet did see” (Hab. 1:1). It opens with the prophet’s complaint, the LORD’s answer that He is raising up the Chaldeans, a second complaint, the vision to be written, five woes, and a prayer that ends in rejoicing though the fig tree does not blossom (Hab. 1:5, 13; 2:2–4; 3:17–19).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the prophet speaks for the LORD’s people and the LORD answers with a vision for an appointed time (Hab. 2:2–3). Its words on faith and on God’s glory are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Habakkuk",
  H('Movement 1 — The Prophet’s Complaint and the LORD’s Answer (Ch. 1)'),
  P('The LORD says He will work a work in their days, and the prophet asks how a God of purer eyes can look on the treacherous (Hab. 1:5, 13).'),
  H('Movement 2 — The Vision and the Woes (Ch. 2)'),
  P('The prophet stands on his watch, is told to write the vision, and hears that the just shall live by his faith (Hab. 2:1–4, 14, 20).'),
  H('Movement 3 — The Prayer of Habakkuk (Ch. 3)'),
  P('The prophet prays for mercy in wrath and ends with rejoicing in the LORD (Hab. 3:2, 17–19).'))

S(3, "Prophecy-Program Themes in Habakkuk",
  H('1. A Work in Their Days'),
  P('“I will work a work in your days, which ye will not believe, though it be told you” (Hab. 1:5).'),
  H('2. Standing on the Watch'),
  P('“I will stand upon my watch, and set me upon the tower” (Hab. 2:1).'),
  H('3. The Vision Written'),
  P('“Write the vision, and make it plain upon tables, that he may run that readeth it” (Hab. 2:2).'),
  H('4. The Appointed Time'),
  P('“The vision is yet for an appointed time, but at the end it shall speak, and not lie” (Hab. 2:3).'),
  H('5. The Just Shall Live'),
  P('“The just shall live by his faith” (Hab. 2:4).'),
  H('6. The Earth Filled'),
  P('“The earth shall be filled with the knowledge of the glory of the LORD, as the waters cover the sea” (Hab. 2:14).'),
  H('7. Joy in the God of Salvation'),
  P('“Yet I will rejoice in the LORD, I will joy in the God of my salvation” (Hab. 3:18).'))

S(4, "Christ in Habakkuk: The Prophetic Trajectory",
  H('1. The Just Shall Live by His Faith'),
  P('The words of Habakkuk 2:4 are quoted in the New Testament (Rom. 1:17; Gal. 3:11; Heb. 10:38); each quotation is read in its own letter, and none is read into Habakkuk.'),
  H('2. Though It Tarry'),
  P('“Though it tarry, wait for it; because it will surely come” (Hab. 2:3) is reported as written; Hebrews 10:37 has similar words and is read in its own chapter.'),
  H('3. The Earth Filled With Glory'),
  P('The earth filled with the knowledge of the glory of the LORD (Hab. 2:14) is reported within Israel’s prophetic hope.'))

S(5, "Israel’s Identity in Habakkuk",
  P("Habakkuk reinforces Israel’s:"),
  L('the LORD’s people for whom the vision is written (Hab. 2:2–3)', 'the chief singer and the prayer of the prophet (Hab. 3:19)', 'the work the LORD works in their days (Hab. 1:5)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Habakkuk does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its vision for an appointed time and its prophecy of the Chaldeans belong exclusively to Israel’s prophetic setting; its words on faith, patience and the glory of the LORD are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Habakkuk", "Program Identity", "Scripture"], [
    ['A Work in Their Days', '“I will work a work in your days, which ye will not believe, though it be told you.”', ISR, 'Hab. 1:5'],
    ['The Vision Written', '“Write the vision, and make it plain upon tables.”', ISR, 'Hab. 2:2'],
    ['The Appointed Time', '“the vision is yet for an appointed time, but at the end it shall speak, and not lie.”', ISR, 'Hab. 2:3'],
    ['The Just Shall Live', '“the just shall live by his faith.”', ISR, 'Hab. 2:4'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Purer Eyes', '“Thou art of purer eyes than to behold evil, and canst not look on iniquity.”', 'Hab. 1:13'],
    ['The Just Live by Faith', '“the just shall live by his faith.”', 'Hab. 2:4'],
    ['The Earth Filled', '“the earth shall be filled with the knowledge of the glory of the LORD, as the waters cover the sea.”', 'Hab. 2:14'],
    ['Silence Before Him', '“the LORD is in his holy temple: let all the earth keep silence before him.”', 'Hab. 2:20'],
    ['Mercy in Wrath', '“in wrath remember mercy.”', 'Hab. 3:2'],
    ['Rejoicing Though Empty', '“Yet I will rejoice in the LORD, I will joy in the God of my salvation.”', 'Hab. 3:18'],
    ['My Strength', '“The LORD God is my strength.”', 'Hab. 3:19'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the Chaldeans, the vision or the woes; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Wait for what He has said</b> — Though it tarry, wait (Hab. 2:3).', '<b>Live by faith</b> — The just shall live by his faith (Hab. 2:4).', '<b>Look for His glory</b> — The earth shall be filled with the knowledge of it (Hab. 2:14).', '<b>Be silent before Him</b> — The LORD is in His holy temple (Hab. 2:20).', '<b>Ask mercy in wrath</b> — In wrath remember mercy (Hab. 3:2).', '<b>Rejoice in the LORD</b> — The God of my salvation (Hab. 3:18).', '<b>Find strength in Him</b> — The LORD God is my strength (Hab. 3:19).'))

S(10, "Teaching Outline for Habakkuk",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Complaint and the Answer (Ch. 1) — A work in their days. <i>(Hab. 1:5, 13)</i>', 'The Vision and the Woes (Ch. 2) — The just shall live by his faith. <i>(Hab. 2:1–4, 14, 20)</i>', 'The Prayer of Habakkuk (Ch. 3) — Joy in the God of salvation. <i>(Hab. 3:2, 17–19)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Habakkuk, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward faith, patience, and rejoicing in the LORD in hard times without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Habakkuk simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Habakkuk stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
