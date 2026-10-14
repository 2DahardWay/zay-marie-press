# DRAFT for publisher approval.
BOOK = "2 Kings"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Elijah Taken Up, the Fall of Israel and Judah, and the Exile to Babylon"
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
  P('2 Kings follows Elijah’s going up by a whirlwind and Elisha’s ministry, then the fall of the northern kingdom to Assyria and the fall of Jerusalem to Babylon. It gives the reasons the book itself states, the prayer of Hezekiah, the finding of the book of the law under Josiah, and the carrying away of Judah, with a closing note on Jehoiachin (2 Kgs. 2:11; 17:7, 18, 23; 19:15; 22:8; 25:1, 7).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel and Judah answer to the LORD’s covenant, are carried away from the land, and the house of David is still remembered (2 Kgs. 13:23; 17:23; 19:34).'))

S(2, "Narrative Flow of 2 Kings",
  H('Movement 1 — Elijah and Elisha (Chs. 1–8)'),
  P('Elijah goes up by a whirlwind, Naaman confesses there is no God but in Israel, and Elisha says, “they that be with us are more than they that be with them” (2 Kgs. 2:11; 5:15; 6:16).'),
  H('Movement 2 — The Fall of Israel (Chs. 9–17)'),
  P('The LORD is gracious for His covenant with Abraham, Isaac and Jacob, yet Israel sins, is removed out of His sight and carried to Assyria (2 Kgs. 13:23; 17:7, 14, 18, 23).'),
  H('Movement 3 — Hezekiah and Josiah (Chs. 18–23)'),
  P('Hezekiah trusts the LORD and prays, the LORD defends the city, and Josiah turns to the LORD after the book of the law is found (2 Kgs. 18:5; 19:15, 19, 34; 20:6; 22:8, 19; 23:25).'),
  H('Movement 4 — The Fall of Judah (Chs. 24–25)'),
  P('Nebuchadnezzar comes against Jerusalem, Zedekiah is bound and carried to Babylon, and the book closes with Jehoiachin’s allowance (2 Kgs. 25:1, 7, 30).'))

S(3, "Prophecy-Program Themes in 2 Kings",
  H('1. Why Israel Fell'),
  P('“The children of Israel had sinned against the LORD their God, which had brought them up out of the land of Egypt” (2 Kgs. 17:7).'),
  H('2. Removed as the Prophets Said'),
  P('“Until the LORD removed Israel out of his sight, as he had said by all his servants the prophets” (2 Kgs. 17:23).'),
  H('3. The Covenant Remembered'),
  P('“The LORD was gracious unto them… because of his covenant with Abraham, Isaac, and Jacob” (2 Kgs. 13:23).'),
  H('4. A Remnant'),
  P('“Out of Jerusalem shall go forth a remnant, and they that escape out of mount Zion” (2 Kgs. 19:31).'),
  H('5. For David’s Sake'),
  P('“I will defend this city, to save it, for mine own sake, and for my servant David’s sake” (2 Kgs. 19:34).'),
  H('6. The Book of the Law Found'),
  P('“I have found the book of the law in the house of the LORD” (2 Kgs. 22:8).'))

S(4, "Christ in 2 Kings: The Prophetic Trajectory",
  H('1. The Remnant and David'),
  P('The LORD defends Jerusalem for David’s sake and speaks of a remnant going out of Zion (2 Kgs. 19:31, 34), within Israel’s prophetic hope.'),
  H('2. The Prophet Taken Up'),
  P('Elijah goes up by a whirlwind into heaven (2 Kgs. 2:11); the book reports this as written.'),
  H('3. Exile and Hope'),
  P('The book closes on Jehoiachin’s continual allowance (2 Kgs. 25:30), reported as written.'))

S(5, "Israel’s Identity in 2 Kings",
  P("2 Kings reinforces Israel’s:"),
  L('covenant with Abraham, Isaac and Jacob (2 Kgs. 13:23)', 'removal from the land for sin (2 Kgs. 17:18, 23)', 'the remnant out of Jerusalem (2 Kgs. 19:31)', 'the house of David remembered (2 Kgs. 19:34; 20:6)', 'the book of the law (2 Kgs. 22:8)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("2 Kings does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its prophets, kings, covenant warnings and exile belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in 2 Kings", "Program Identity", "Scripture"], [
    ['Israel Sinned', '“the children of Israel had sinned against the LORD their God.”', ISR, '2 Kgs. 17:7'],
    ['Removed Out of His Sight', '“the LORD was very angry with Israel, and removed them out of his sight.”', ISR, '2 Kgs. 17:18'],
    ['As the Prophets Said', '“as he had said by all his servants the prophets.”', ISR, '2 Kgs. 17:23'],
    ['The Covenant With the Fathers', '“because of his covenant with Abraham, Isaac, and Jacob.”', ISR, '2 Kgs. 13:23'],
    ['The Remnant', '“out of Jerusalem shall go forth a remnant.”', ISR, '2 Kgs. 19:31'],
    ['For David’s Sake', '“for my servant David’s sake.”', ISR, '2 Kgs. 19:34'],
    ['The Book of the Law', '“I have found the book of the law in the house of the LORD.”', ISR, '2 Kgs. 22:8'],
    ['Josiah Turned', '“that turned to the LORD with all his heart, and with all his soul, and with all his might.”', ISR, '2 Kgs. 23:25'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['No God Like Him', '“thou art the God, even thou alone, of all the kingdoms of the earth; thou hast made heaven and earth.”', '2 Kgs. 19:15'],
    ['That All May Know', '“that all the kingdoms of the earth may know that thou art the LORD God, even thou only.”', '2 Kgs. 19:19'],
    ['The LORD Hears', '“I have heard thy prayer, I have seen thy tears.”', '2 Kgs. 20:5'],
    ['A Humble Heart Heard', '“thou hast humbled thyself before the LORD… I also have heard thee, saith the LORD.”', '2 Kgs. 22:19'],
    ['Those With Us Are More', '“they that be with us are more than they that be with them.”', '2 Kgs. 6:16'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant warnings, kings or exile; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Pray as Hezekiah did</b> — To the God who made heaven and earth (2 Kgs. 19:15).', '<b>Desire that all know the LORD</b> (2 Kgs. 19:19).', '<b>Trust that He hears</b> (2 Kgs. 20:5).', '<b>Humble yourself before Him</b> (2 Kgs. 22:19).', '<b>Take courage</b> — Those with us are more (2 Kgs. 6:16).'))

S(10, "Teaching Outline for 2 Kings",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Elijah and Elisha (Chs. 1–8) — The prophets. <i>(2 Kgs. 2:11; 5:15; 6:16)</i>', 'The Fall of Israel (Chs. 9–17) — Removed as the prophets said. <i>(2 Kgs. 13:23; 17:7, 18, 23)</i>', 'Hezekiah and Josiah (Chs. 18–23) — Prayer and the book of the law. <i>(2 Kgs. 19:15, 31, 34; 22:8; 23:25)</i>', 'The Fall of Judah (Chs. 24–25) — Exile to Babylon. <i>(2 Kgs. 25:1, 7, 30)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 Kings, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward humility, prayer, and trust without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 Kings simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 2 Kings stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
