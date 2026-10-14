# DRAFT for publisher approval.
BOOK = "Ezra"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Return from Babylon, the House Rebuilt, and the Law Taught"
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
  P('Ezra opens with the decree of Cyrus and follows the first return of the people to Jerusalem under Zerubbabel and Jeshua. It records the altar and foundation of the temple, the opposition, the dedication of the house, and the later coming of Ezra the scribe, his prayer of confession, and the separation of the people from the strange wives (Ezra 1:1–3; 3:2, 10–11; 6:16; 7:6, 10; 9:6, 15; 10:11).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where a remnant of Israel returns to the land to rebuild the house of the LORD under the law of Moses (Ezra 1:3; 7:6).'))

S(2, "Narrative Flow of Ezra",
  H('Movement 1 — The Return Under Cyrus (Chs. 1–2)'),
  P('The LORD stirs up Cyrus, who says, “Who is there among you of all his people? his God be with him, and let him go up to Jerusalem” (Ezra 1:1–3).'),
  H('Movement 2 — The Altar, the Foundation, and the Opposition (Chs. 3–6)'),
  P('The altar is built as written in the law of Moses, the foundation is laid with praise, and the house is dedicated with joy (Ezra 3:2, 10–11; 4:3; 6:16, 22).'),
  H('Movement 3 — Ezra Goes Up (Chs. 7–8)'),
  P('Ezra is a ready scribe in the law of Moses, prepares his heart to seek the law of the LORD, and trusts the hand of God for the way (Ezra 7:6, 10, 27; 8:22).'),
  H('Movement 4 — Confession and Separation (Chs. 9–10)'),
  P('Ezra prays, “O LORD God of Israel, thou art righteous,” the people weep, and they are told to separate from the people of the land (Ezra 9:6, 15; 10:1, 11).'))

S(3, "Prophecy-Program Themes in Ezra",
  H('1. The LORD Stirs Cyrus'),
  P('“The LORD stirred up the spirit of Cyrus king of Persia” (Ezra 1:1).'),
  H('2. The House of the LORD God of Israel'),
  P('“Build the house of the LORD God of Israel, (he is the God,) which is in Jerusalem” (Ezra 1:3).'),
  H('3. As Written in the Law'),
  P('“As it is written in the law of Moses the man of God” (Ezra 3:2).'),
  H('4. A Heart Prepared'),
  P('“Ezra had prepared his heart to seek the law of the LORD, and to do it, and to teach in Israel statutes and judgments” (Ezra 7:10).'),
  H('5. Righteous Before Him'),
  P('“O LORD God of Israel, thou art righteous” (Ezra 9:15).'))

S(4, "Christ in Ezra: The Prophetic Trajectory",
  H('1. The Return of a Remnant'),
  P('The book records a return to the land under Cyrus’s decree (Ezra 1:1–3), reported as written within Israel’s program.'),
  H('2. The House Rebuilt'),
  P('The house of the LORD is rebuilt and dedicated (Ezra 3:10–11; 6:16).'),
  H('3. The Scribe and the Law'),
  P('Ezra teaches the law of Moses in Israel (Ezra 7:6, 10).'))

S(5, "Israel’s Identity in Ezra",
  P("Ezra reinforces Israel’s:"),
  L('the return to the land after exile (Ezra 1:3)', 'altar and house of the LORD (Ezra 3:2; 6:16)', 'the law of Moses (Ezra 7:6, 10)', 'separation from the people of the land (Ezra 10:11)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Ezra does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its return, temple, law and separation commands belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Ezra", "Program Identity", "Scripture"], [
    ['The Decree to Go Up', '“his God be with him, and let him go up to Jerusalem, which is in Judah.”', ISR, 'Ezra 1:3'],
    ['The Altar Built', '“builded the altar of the God of Israel, to offer burnt offerings thereon.”', ISR, 'Ezra 3:2'],
    ['The Foundation Laid', '“the foundation of the house of the LORD was laid.”', ISR, 'Ezra 3:11'],
    ['The House Dedicated', '“kept the dedication of this house of God with joy.”', ISR, 'Ezra 6:16'],
    ['A Ready Scribe', '“he was a ready scribe in the law of Moses.”', ISR, 'Ezra 7:6'],
    ['Teaching Israel', '“to teach in Israel statutes and judgments.”', ISR, 'Ezra 7:10'],
    ['Separation', '“separate yourselves from the people of the land, and from the strange wives.”', ISR, 'Ezra 10:11'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The LORD Moves Kings', '“Blessed be the LORD God of our fathers, which hath put such a thing as this in the king’s heart.”', 'Ezra 7:27'],
    ['His Hand on Those Who Seek', '“The hand of our God is upon all them for good that seek him.”', 'Ezra 8:22'],
    ['The LORD Is Righteous', '“O LORD God of Israel, thou art righteous.”', 'Ezra 9:15'],
    ['His Mercy Endures', '“for his mercy endureth for ever toward Israel.”', 'Ezra 3:11'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s return, temple or separation commands; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Give thanks</b> — His mercy endures (Ezra 3:11).', '<b>Thank Him for ruling over rulers</b> (Ezra 7:27).', '<b>Seek Him</b> — His hand is for good on those who do (Ezra 8:22).', '<b>Confess that He is righteous</b> (Ezra 9:15).'))

S(10, "Teaching Outline for Ezra",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Return Under Cyrus (Chs. 1–2) — The decree. <i>(Ezra 1:1–3)</i>', 'The Altar and the House (Chs. 3–6) — Foundation and dedication. <i>(Ezra 3:2, 10–11; 6:16)</i>', 'Ezra Goes Up (Chs. 7–8) — The law prepared and taught. <i>(Ezra 7:6, 10, 27; 8:22)</i>', 'Confession and Separation (Chs. 9–10) — Righteous before Him. <i>(Ezra 9:15; 10:11)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Ezra, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward repentance, humility, and prayer without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Ezra simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Ezra stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
