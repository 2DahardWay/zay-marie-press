# DRAFT for publisher approval.
BOOK = "2 Chronicles"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Solomon’s Temple, the Kings of Judah, and the Decree of Cyrus"
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
  P('2 Chronicles retells the history of Judah from Solomon to the exile. It records the dedication of the temple and the glory that fills it, the LORD’s answer to Solomon, the reigns of Judah’s kings, the reforms of Hezekiah and Josiah, the sending of the LORD’s messengers, the fall of Jerusalem, and the decree of Cyrus (2 Chr. 6:14; 7:1, 14; 29:36; 34:33; 36:15–16, 22–23).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the temple, the house of David and Judah’s kings stand within Israel’s covenant (2 Chr. 7:16; 13:5).'))

S(2, "Narrative Flow of 2 Chronicles",
  H('Movement 1 — Solomon and the Temple (Chs. 1–9)'),
  P('Solomon is strengthened by the LORD his God, the singers praise Him, Solomon prays at the dedication, and the glory of the LORD fills the house (2 Chr. 1:1; 5:13; 6:14, 18; 7:1).'),
  H('Movement 2 — The Divided Kingdom (Chs. 10–20)'),
  P('Abijah speaks of the covenant of salt, Asa is told that the LORD is with him while he is with Him, and Jehoshaphat calls Judah to believe the LORD (2 Chr. 13:5; 15:2; 16:9; 19:7; 20:15, 20–21).'),
  H('Movement 3 — Reform and Decline (Chs. 21–35)'),
  P('Hezekiah and Josiah turn Judah back to the LORD (2 Chr. 29:36; 30:9; 34:33).'),
  H('Movement 4 — Exile and Return Promised (Ch. 36)'),
  P('The LORD sends messengers, Judah mocks them, Jerusalem falls, and Cyrus is stirred up to let the people go up (2 Chr. 36:15–16, 22–23).'))

S(3, "Prophecy-Program Themes in 2 Chronicles",
  H('1. The Glory in the House'),
  P('“The fire came down from heaven, and consumed the burnt offering and the sacrifices; and the glory of the LORD filled the house” (2 Chr. 7:1).'),
  H('2. Humble, Pray, Seek, Turn'),
  P('“If my people, which are called by my name, shall humble themselves, and pray, and seek my face, and turn from their wicked ways; then will I hear from heaven, and will forgive their sin, and will heal their land” (2 Chr. 7:14).'),
  H('3. The Name Placed in the House'),
  P('“Now have I chosen and sanctified this house, that my name may be there for ever” (2 Chr. 7:16).'),
  H('4. The Kingdom Given to David'),
  P('“The LORD God of Israel gave the kingdom over Israel to David for ever, even to him and to his sons by a covenant of salt” (2 Chr. 13:5).'),
  H('5. No Remedy'),
  P('“Until the wrath of the LORD arose against his people, till there was no remedy” (2 Chr. 36:16).'))

S(4, "Christ in 2 Chronicles: The Prophetic Trajectory",
  H('1. The House and the Glory'),
  P('The glory of the LORD fills the house (2 Chr. 7:1), reported as written within Israel’s temple worship.'),
  H('2. The Son of David'),
  P('The kingdom is given to David and his sons by a covenant of salt (2 Chr. 13:5), within Israel’s kingdom hope.'),
  H('3. The Decree of Cyrus'),
  P('The book ends with Cyrus’s decree, “Who is there among you of all his people? The LORD his God be with him, and let him go up” (2 Chr. 36:23).'))

S(5, "Israel’s Identity in 2 Chronicles",
  P("2 Chronicles reinforces Israel’s:"),
  L('temple and glory of the LORD (2 Chr. 7:1)', 'a people called by His name (2 Chr. 7:14)', 'the kingdom given to David (2 Chr. 13:5)', 'warning by messengers and prophets (2 Chr. 36:15–16)', 'the decree to go up (2 Chr. 36:23)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("2 Chronicles does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its temple, throne, covenant conditions and exile belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in 2 Chronicles", "Program Identity", "Scripture"], [
    ['The Glory Fills the House', '“the glory of the LORD filled the house.”', ISR, '2 Chr. 7:1'],
    ['My People Called by My Name', '“If my people, which are called by my name, shall humble themselves.”', ISR, '2 Chr. 7:14'],
    ['The Land Healed', '“will forgive their sin, and will heal their land.”', ISR, '2 Chr. 7:14'],
    ['The Name There for Ever', '“that my name may be there for ever.”', ISR, '2 Chr. 7:16'],
    ['The Covenant of Salt', '“gave the kingdom over Israel to David for ever.”', ISR, '2 Chr. 13:5'],
    ['Believe His Prophets', '“Believe in the LORD your God, so shall ye be established; believe his prophets, so shall ye prosper.”', ISR, '2 Chr. 20:20'],
    ['The Return Promised', '“for if ye turn again unto the LORD, your brethren and your children shall find compassion before them that lead them captive.”', ISR, '2 Chr. 30:9'],
    ['Messengers Despised', '“they mocked the messengers of God, and despised his words, and misused his prophets.”', ISR, '2 Chr. 36:16'],
    ['Cyrus Stirred Up', '“the LORD stirred up the spirit of Cyrus king of Persia.”', ISR, '2 Chr. 36:22'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['No God Like Him', '“O LORD God of Israel, there is no God like thee in the heaven, nor in the earth.”', '2 Chr. 6:14'],
    ['His Eyes Run to and Fro', '“the eyes of the LORD run to and fro throughout the whole earth, to shew himself strong in the behalf of them whose heart is perfect toward him.”', '2 Chr. 16:9'],
    ['No Respect of Persons', '“there is no iniquity with the LORD our God, nor respect of persons, nor taking of gifts.”', '2 Chr. 19:7'],
    ['The Battle Is God’s', '“the battle is not yours, but God’s.”', '2 Chr. 20:15'],
    ['His Mercy Endures', '“his mercy endureth for ever.”', '2 Chr. 20:21'],
    ['Gracious and Merciful', '“the LORD your God is gracious and merciful.”', '2 Chr. 30:9'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s temple, throne or exile; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Honour the God who has no equal</b> (2 Chr. 6:14).', '<b>Trust Him to strengthen the wholehearted</b> (2 Chr. 16:9).', '<b>Practice fairness</b> — There is no respect of persons with Him (2 Chr. 19:7).', '<b>Rest in His battle</b> (2 Chr. 20:15).', '<b>Praise Him</b> — His mercy endures for ever (2 Chr. 20:21).'))

S(10, "Teaching Outline for 2 Chronicles",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Solomon and the Temple (Chs. 1–9) — The glory fills the house. <i>(2 Chr. 5:13; 6:14; 7:1, 14, 16)</i>', 'The Divided Kingdom (Chs. 10–20) — The covenant of salt. <i>(2 Chr. 13:5; 16:9; 19:7; 20:15, 20–21)</i>', 'Reform and Decline (Chs. 21–35) — Hezekiah and Josiah. <i>(2 Chr. 30:9; 34:33)</i>', 'Exile and Return (Ch. 36) — Cyrus’s decree. <i>(2 Chr. 36:15–16, 22–23)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 Chronicles, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward humility, prayer, and trust without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 Chronicles simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 2 Chronicles stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
