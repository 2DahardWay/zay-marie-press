# DRAFT for publisher approval.
BOOK = "Zephaniah"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Day of the LORD, the Meek Remnant, and the King in Their Midst"
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
  P('Zephaniah is “the word of the LORD which came unto Zephaniah… in the days of Josiah the son of Amon, king of Judah” (Zeph. 1:1). It speaks of the great day of the LORD, calls the meek to seek the LORD, promises a pure language and an afflicted and poor people who trust in His name, and closes with the song of the daughter of Zion (Zeph. 1:14; 2:3; 3:9, 12, 14–17).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to Judah and Jerusalem about the day of the LORD, the remnant of Israel and the king of Israel in their midst (Zeph. 1:1; 3:13–15).'))

S(2, "Narrative Flow of Zephaniah",
  H('Movement 1 — The Great Day of the LORD (Ch. 1)'),
  P('The LORD prepares a sacrifice, and the great day is near (Zeph. 1:1, 7, 14).'),
  H('Movement 2 — Seek the LORD (Ch. 2)'),
  P('The meek of the earth are called to seek righteousness and meekness (Zeph. 2:1, 3).'),
  H('Movement 3 — Nations Gathered, a Remnant Left (Ch. 3:1–13)'),
  P('The LORD gathers the nations, gives a pure language, and leaves an afflicted and poor people (Zeph. 3:8, 9, 12–13).'),
  H('Movement 4 — The Song of Zion (Ch. 3:14–20)'),
  P('The king of Israel is in the midst of Zion, and the captivity is turned back (Zeph. 3:14–15, 17, 20).'))

S(3, "Prophecy-Program Themes in Zephaniah",
  H('1. The Day at Hand'),
  P('“The day of the LORD is at hand” (Zeph. 1:7).'),
  H('2. Seek the LORD'),
  P('“Seek ye the LORD, all ye meek of the earth… it may be ye shall be hid in the day of the LORD’s anger” (Zeph. 2:3).'),
  H('3. Nations Gathered'),
  P('“My determination is to gather the nations, that I may assemble the kingdoms” (Zeph. 3:8).'),
  H('4. A Pure Language'),
  P('“Then will I turn to the people a pure language, that they may all call upon the name of the LORD” (Zeph. 3:9).'),
  H('5. The Remnant of Israel'),
  P('“The remnant of Israel shall not do iniquity, nor speak lies” (Zeph. 3:13).'),
  H('6. The King in Their Midst'),
  P('“The king of Israel, even the LORD, is in the midst of thee” (Zeph. 3:15).'),
  H('7. Captivity Turned Back'),
  P('“I turn back your captivity before your eyes, saith the LORD” (Zeph. 3:20).'))

S(4, "Christ in Zephaniah: The Prophetic Trajectory",
  H('1. The King of Israel'),
  P('The LORD is “the king of Israel” in the midst of the daughter of Zion (Zeph. 3:15).'),
  H('2. He Will Save'),
  P('“He will save, he will rejoice over thee with joy” (Zeph. 3:17).'),
  H('3. The Day of the LORD'),
  P('The great day of the LORD is described in Zeph. 1:14 and read beside Joel 1:15 and Obadiah 1:15 as written.'))

S(5, "Israel’s Identity in Zephaniah",
  P("Zephaniah reinforces Israel’s:"),
  L('Judah and Jerusalem addressed in the days of Josiah (Zeph. 1:1)', 'the remnant of Israel and the daughter of Zion (Zeph. 3:13–14)', 'the king of Israel in the midst of Zion (Zeph. 3:15)', 'the captivity turned back (Zeph. 3:20)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Zephaniah does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its day of the LORD, its nations gathered, its remnant and its king in Zion belong exclusively to Israel; its words on seeking the LORD and on His rejoicing over His people are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Zephaniah", "Program Identity", "Scripture"], [
    ['The Day at Hand', '“the day of the LORD is at hand.”', ISR, 'Zeph. 1:7'],
    ['The Great Day Near', '“The great day of the LORD is near, it is near, and hasteth greatly.”', ISR, 'Zeph. 1:14'],
    ['Nations Gathered', '“my determination is to gather the nations, that I may assemble the kingdoms.”', ISR, 'Zeph. 3:8'],
    ['A Pure Language', '“I turn to the people a pure language.”', ISR, 'Zeph. 3:9'],
    ['The Remnant of Israel', '“The remnant of Israel shall not do iniquity, nor speak lies.”', ISR, 'Zeph. 3:13'],
    ['The King in the Midst', '“the king of Israel, even the LORD, is in the midst of thee.”', ISR, 'Zeph. 3:15'],
    ['Captivity Turned Back', '“when I turn back your captivity before your eyes, saith the LORD.”', ISR, 'Zeph. 3:20'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Seek the LORD', '“Seek ye the LORD, all ye meek of the earth.”', 'Zeph. 2:3'],
    ['Trust in His Name', '“they shall trust in the name of the LORD.”', 'Zeph. 3:12'],
    ['Mighty to Save', '“The LORD thy God in the midst of thee is mighty; he will save.”', 'Zeph. 3:17'],
    ['Rejoicing in Love', '“he will rest in his love, he will joy over thee with singing.”', 'Zeph. 3:17'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the day of the LORD, the remnant or Zion’s king; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Seek the LORD</b> — Seek righteousness and meekness (Zeph. 2:3).', '<b>Trust in His name</b> — An afflicted and poor people may trust (Zeph. 3:12).', '<b>Rest on His strength</b> — He is mighty and will save (Zeph. 3:17).', '<b>Know His delight</b> — He will rest in His love (Zeph. 3:17).'))

S(10, "Teaching Outline for Zephaniah",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Great Day of the LORD (Ch. 1) — The day at hand. <i>(Zeph. 1:1, 7, 14)</i>', 'Seek the LORD (Ch. 2) — The meek hid in the day. <i>(Zeph. 2:3)</i>', 'Nations Gathered, a Remnant Left (Ch. 3:1–13) — A pure language. <i>(Zeph. 3:8–9, 12–13)</i>', 'The Song of Zion (Ch. 3:14–20) — The king in their midst. <i>(Zeph. 3:14–15, 17, 20)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Zephaniah, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward seeking the LORD, humility, and rejoicing in His salvation without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Zephaniah simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Zephaniah stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
