# DRAFT for publisher approval.
BOOK = "Proverbs"
TESTAMENT = "Old Testament"
GENRE = "poetry"
SUBTITLE = "The Fear of the LORD, Wisdom for Daily Life, and the Counsel of a Father"
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
  P('Proverbs opens with “The proverbs of Solomon the son of David, king of Israel” (Prov. 1:1), gathers counsel on wisdom, the heart, speech, money, friendship and family, and adds proverbs “which the men of Hezekiah king of Judah copied out” (Prov. 25:1). It closes with a portrait of the virtuous woman (Prov. 31:10, 30).'),
  BOX("Program Identity:", 'The book is introduced as the proverbs of Solomon, king of Israel, and of the men of Hezekiah king of Judah (Prov. 1:1; 25:1). Its sayings are rooted in the fear of the LORD and are placed in the Universal Truths Table except where a verse names the Israelite setting.'))

S(2, "Narrative Flow of Proverbs",
  H('Movement 1 — A Father’s Call to Wisdom (Chs. 1–9)'),
  P('The purpose of the book is stated and wisdom is set before the young: “The fear of the LORD is the beginning of knowledge” (Prov. 1:7; 3:5–6; 4:23; 9:10).'),
  H('Movement 2 — The Proverbs of Solomon (Chs. 10–22:16)'),
  P('Short sayings on the wise son, the soft answer, honest weights, the way that seems right and the training of a child (Prov. 10:1; 11:1; 14:12; 15:1; 22:6).'),
  H('Movement 3 — Sayings of the Wise (Chs. 22:17–24)'),
  P('Counsel on friends, the fear of man and the pursuit of wisdom (Prov. 13:20; 17:17; 24:3).'),
  H('Movement 4 — Hezekiah’s Collection (Chs. 25–29)'),
  P('Further proverbs of Solomon copied out by the men of Hezekiah king of Judah (Prov. 25:1; 27:17; 28:13; 29:25).'),
  H('Movement 5 — Agur, Lemuel, and the Virtuous Woman (Chs. 30–31)'),
  P('Agur’s words, a king’s mother’s teaching, and the portrait of the woman who feareth the LORD (Prov. 30:5; 31:10, 30).'))

S(3, "Prophecy-Program Themes in Proverbs",
  H('1. The Fear of the LORD'),
  P('“The fear of the LORD is the beginning of knowledge: but fools despise wisdom and instruction” (Prov. 1:7).'),
  H('2. Trust and Direction'),
  P('“Trust in the LORD with all thine heart; and lean not unto thine own understanding” (Prov. 3:5).'),
  H('3. Guarding the Heart'),
  P('“Keep thy heart with all diligence; for out of it are the issues of life” (Prov. 4:23).'),
  H('4. The Way That Seems Right'),
  P('“There is a way which seemeth right unto a man, but the end thereof are the ways of death” (Prov. 14:12).'),
  H('5. The Soft Answer'),
  P('“A soft answer turneth away wrath: but grievous words stir up anger” (Prov. 15:1).'),
  H('6. The LORD Directs'),
  P('“A man’s heart deviseth his way: but the LORD directeth his steps” (Prov. 16:9).'),
  H('7. The Word of God Pure'),
  P('“Every word of God is pure: he is a shield unto them that put their trust in him” (Prov. 30:5).'))

S(4, "Christ in Proverbs: The Prophetic Trajectory",
  H('1. Wisdom Personified'),
  P('Wisdom speaks of being with the LORD “before his works of old” (Prov. 8:22), reported as written.'),
  H('2. A Word That Shields'),
  P('“Every word of God is pure” (Prov. 30:5).'),
  H('3. The Greater Than Solomon'),
  P('Solomon is the king named at the head of the book (Prov. 1:1); the Lord speaks of one greater than Solomon (Matt. 12:42).'))

S(5, "Israel’s Identity in Proverbs",
  P("Proverbs reinforces Israel’s:"),
  L(),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Proverbs does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its sayings are rooted in the fear of the LORD and are given to the reader as counsel for daily life; the book’s Israelite setting is named only in its headings, and none of its sayings is taught as the Body of Christ’s calling.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Proverbs", "Program Identity", "Scripture"], [
    ['The Proverbs of Solomon', '“The proverbs of Solomon the son of David, king of Israel.”', ISR, 'Prov. 1:1'],
    ['A Wise Son', '“The proverbs of Solomon. A wise son maketh a glad father.”', ISR, 'Prov. 10:1'],
    ['Hezekiah’s Men', '“proverbs of Solomon, which the men of Hezekiah king of Judah copied out.”', ISR, 'Prov. 25:1'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The Fear of the LORD', '“The fear of the LORD is the beginning of knowledge.”', 'Prov. 1:7'],
    ['Trust the LORD', '“Trust in the LORD with all thine heart; and lean not unto thine own understanding.”', 'Prov. 3:5'],
    ['He Directs the Paths', '“In all thy ways acknowledge him, and he shall direct thy paths.”', 'Prov. 3:6'],
    ['Keep the Heart', '“Keep thy heart with all diligence; for out of it are the issues of life.”', 'Prov. 4:23'],
    ['Honest Weights', '“A false balance is abomination to the LORD: but a just weight is his delight.”', 'Prov. 11:1'],
    ['The Way That Seems Right', '“There is a way which seemeth right unto a man.”', 'Prov. 14:12'],
    ['A Soft Answer', '“A soft answer turneth away wrath.”', 'Prov. 15:1'],
    ['The LORD Directs', '“A man’s heart deviseth his way: but the LORD directeth his steps.”', 'Prov. 16:9'],
    ['A Strong Tower', '“The name of the LORD is a strong tower: the righteous runneth into it, and is safe.”', 'Prov. 18:10'],
    ['The Counsel of the LORD', '“the counsel of the LORD, that shall stand.”', 'Prov. 19:21'],
    ['Confession', '“whoso confesseth and forsaketh them shall have mercy.”', 'Prov. 28:13'],
    ['Every Word Pure', '“Every word of God is pure: he is a shield unto them that put their trust in him.”', 'Prov. 30:5'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s courts of Israel or the throne of Solomon; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Begin with the fear of the LORD</b> — The beginning of knowledge (Prov. 1:7).', '<b>Trust Him with the whole heart</b> — Lean not on your own understanding (Prov. 3:5).', '<b>Guard the heart</b> — Out of it are the issues of life (Prov. 4:23).', '<b>Deal honestly</b> — A just weight is His delight (Prov. 11:1).', '<b>Answer softly</b> — A soft answer turneth away wrath (Prov. 15:1).', '<b>Let the LORD direct your steps</b> — The heart devises, the LORD directs (Prov. 16:9).', '<b>Run to His name</b> — A strong tower (Prov. 18:10).', '<b>Confess and forsake</b> — Mercy follows (Prov. 28:13).'))

S(10, "Teaching Outline for Proverbs",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('A Father’s Call to Wisdom (Chs. 1–9) — The fear of the LORD. <i>(Prov. 1:1, 7; 3:5–6; 4:23)</i>', 'The Proverbs of Solomon (Chs. 10–22) — Sayings on daily life. <i>(Prov. 10:1; 11:1; 14:12; 15:1; 16:9)</i>', 'Sayings of the Wise (Chs. 22–24) — Friends and the heart. <i>(Prov. 19:21)</i>', 'Hezekiah’s Collection (Chs. 25–29) — More of Solomon’s sayings. <i>(Prov. 25:1; 28:13)</i>', 'Agur and Lemuel (Chs. 30–31) — The pure word and the virtuous woman. <i>(Prov. 30:5; 31:10, 30)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Proverbs, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward wisdom, humility, and the fear of the LORD without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Proverbs simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Proverbs stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
