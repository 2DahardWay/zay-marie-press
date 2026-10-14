# DRAFT for publisher approval.
BOOK = "Song of Solomon"
TESTAMENT = "Old Testament"
GENRE = "poetry"
SUBTITLE = "A Song of Love, Sought, Found, and Kept"
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
  P('The Song of Solomon opens, “The song of songs, which is Solomon’s” (Song 1:1). It is a poem of two lovers, with the daughters of Jerusalem as a chorus. It moves through longing and finding, spring and the seeking by night, the praise of the beloved, and ends with love set as a seal (Song 2:10; 5:16; 8:6–7).'),
  BOX("Program Identity:", 'The book is introduced as Solomon’s song and addresses the daughters of Jerusalem, so its setting is Israelite (Song 1:1; 8:4). Its celebration of faithful love is also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Song of Solomon",
  H('Movement 1 — Longing and Finding (Chs. 1–2)'),
  P('The two lovers speak of one another, and the beloved calls, “Rise up, my love, my fair one, and come away” (Song 1:2; 2:10–12).'),
  H('Movement 2 — Seeking and the Wedding (Chs. 3–4)'),
  P('The bride seeks her beloved, the wedding procession comes, and the bridegroom speaks of her (Song 4:9).'),
  H('Movement 3 — Absence and Praise (Chs. 5–6)'),
  P('The beloved is sought and then praised as “altogether lovely” (Song 5:16; 6:3).'),
  H('Movement 4 — Delight and Desire (Ch. 7)'),
  P('The beloved’s desire is toward her (Song 7:10).'),
  H('Movement 5 — Love as a Seal (Ch. 8)'),
  P('Love is set as a seal, strong as death, and many waters cannot quench it (Song 8:4, 6–7).'))

S(3, "Prophecy-Program Themes in Song of Solomon",
  H('1. A Song Within Israel'),
  P('“The song of songs, which is Solomon’s” (Song 1:1).'),
  H('2. Mutual Belonging'),
  P('“My beloved is mine, and I am his” (Song 2:16).'),
  H('3. The Call of the Beloved'),
  P('“Rise up, my love, my fair one, and come away” (Song 2:10).'),
  H('4. Praise'),
  P('“He is altogether lovely” (Song 5:16).'),
  H('5. Desire Returned'),
  P('“I am my beloved’s, and his desire is toward me” (Song 7:10).'),
  H('6. Love Stronger Than Death'),
  P('“Love is strong as death” (Song 8:6).'),
  H('7. Love Not Bought'),
  P('“Many waters cannot quench love, neither can the floods drown it” (Song 8:7).'))

S(4, "Christ in Song of Solomon: The Prophetic Trajectory",
  H('1. A Figure Not Named'),
  P('Some readers read the lovers as a figure of the LORD and Israel; the book does not say so, and it is reported as written.'),
  H('2. Solomon the King'),
  P('The song is Solomon’s (Song 1:1); the Lord speaks of one greater than Solomon (Matt. 12:42).'),
  H('3. No Quotation in the New Testament'),
  P('The New Testament does not quote the book, and no passage is built on it here.'))

S(5, "Israel’s Identity in Song of Solomon",
  P("Song of Solomon reinforces Israel’s:"),
  L('an Israelite setting and the daughters of Jerusalem (Song 1:1; 8:4)', 'the king’s song as part of Israel’s wisdom writings (Song 1:1)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Song of Solomon does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its setting is Israelite, and its poetry of marriage love is given as wisdom for all; none of it is taught as the Body of Christ’s calling.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Song of Solomon", "Program Identity", "Scripture"], [
    ['The Song of Songs', '“The song of songs, which is Solomon’s.”', ISR, 'Song 1:1'],
    ['The Daughters of Jerusalem', '“I charge you, O daughters of Jerusalem, that ye stir not up, nor awake my love, until he please.”', ISR, 'Song 8:4'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Love Declared', '“his banner over me was love.”', 'Song 2:4'],
    ['The Call', '“Rise up, my love, my fair one, and come away.”', 'Song 2:10'],
    ['Belonging', '“My beloved is mine, and I am his.”', 'Song 2:16'],
    ['The Heart Won', '“Thou hast ravished my heart, my sister, my spouse.”', 'Song 4:9'],
    ['Praise of the Beloved', '“he is altogether lovely.”', 'Song 5:16'],
    ['Desire Returned', '“I am my beloved’s, and his desire is toward me.”', 'Song 7:10'],
    ['Strong as Death', '“love is strong as death.”', 'Song 8:6'],
    ['Love Not Bought', '“Many waters cannot quench love, neither can the floods drown it.”', 'Song 8:7'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s courts, kingdom or land; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Honour faithful love</b> — Love is strong as death (Song 8:6).', '<b>Belong to one another</b> — My beloved is mine, and I am his (Song 2:16).', '<b>Speak praise to the beloved</b> — He is altogether lovely (Song 5:16).', '<b>Answer desire with desire</b> — His desire is toward me (Song 7:10).', '<b>Know love cannot be bought</b> — Many waters cannot quench it (Song 8:7).'))

S(10, "Teaching Outline for Song of Solomon",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Longing and Finding (Chs. 1–2) — The call of the beloved. <i>(Song 1:2; 2:10, 16)</i>', 'Seeking and the Wedding (Chs. 3–4) — The heart won. <i>(Song 4:9)</i>', 'Absence and Praise (Chs. 5–6) — Altogether lovely. <i>(Song 5:16)</i>', 'Delight and Desire (Ch. 7) — Desire returned. <i>(Song 7:10)</i>', 'Love as a Seal (Ch. 8) — Strong as death. <i>(Song 8:4, 6–7)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Song of Solomon, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward gratitude, faithfulness, and the worth of committed love without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Song of Solomon simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Song of Solomon stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
