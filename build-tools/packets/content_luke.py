# DRAFT for publisher approval.
BOOK = "Luke"
TESTAMENT = "New Testament"
GENRE = "gospels"
SUBTITLE = "The Son of David, Good Tidings to Israel, and the Things Written Concerning Him"
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
  P('Luke is written “in order” that the reader “mightest know the certainty of those things, wherein thou hast been instructed” (Luke 1:1, 4). It tells of the promise that the Lord God shall give the Son “the throne of his father David,” the good tidings of a Saviour born in the city of David, the Lord’s preaching “the acceptable year of the Lord,” the road to Jerusalem, the cup of the new testament, and the risen Lord opening the things written “in the law of Moses, and in the prophets, and in the psalms, concerning me” (Luke 1:32–33; 2:10–11; 4:18–19; 22:20; 24:44).'),
  BOX("Program Identity:", 'The portions of Luke treated here belong to the Prophecy Program: the promise to Mary speaks of the throne of David and the house of Jacob, and the Lord promises the Twelve thrones judging the twelve tribes of Israel (Luke 1:32–33; 22:29–30). Its words on mercy and love are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Luke",
  H('Movement 1 — The Promise and the Birth (Chs. 1–2)'),
  P('The promise of the throne of David and the house of Jacob, and the good tidings to the shepherds (Luke 1:32–33, 68; 2:10–11).'),
  H('Movement 2 — The Anointed Preacher (Chs. 3–4)'),
  P('The Lord reads from the prophet and preaches the acceptable year of the Lord and the kingdom of God (Luke 4:18–19, 43).'),
  H('Movement 3 — Teaching and Mercy (Chs. 5–9)'),
  P('The Lord teaches love of enemies and mercy toward the unthankful (Luke 6:27, 31, 35–37).'),
  H('Movement 4 — The Road to Jerusalem (Chs. 10–19)'),
  P('The lawyer’s question, the good Samaritan, the little flock and the Son of man come to seek and to save that which was lost (Luke 10:25–27, 37; 12:15, 32; 19:10).'),
  H('Movement 5 — The Supper and the Cross (Chs. 20–23)'),
  P('The cup of the new testament and the kingdom appointed to the Twelve (Luke 22:20, 29–30).'),
  H('Movement 6 — The Risen Lord (Ch. 24)'),
  P('The Lord expounds in all the scriptures the things concerning himself and opens the repentance and remission to be preached beginning at Jerusalem (Luke 24:25–27, 44, 47).'))

S(3, "Prophecy-Program Themes in Luke",
  H('1. The Throne of David'),
  P('“The Lord God shall give unto him the throne of his father David” (Luke 1:32).'),
  H('2. He Shall Reign Over the House of Jacob'),
  P('“He shall reign over the house of Jacob for ever; and of his kingdom there shall be no end” (Luke 1:33).'),
  H('3. The Lord God of Israel'),
  P('“Blessed be the Lord God of Israel; for he hath visited and redeemed his people” (Luke 1:68).'),
  H('4. The Acceptable Year'),
  P('“To preach the acceptable year of the Lord” (Luke 4:19).'),
  H('5. The Little Flock'),
  P('“Fear not, little flock; for it is your Father’s good pleasure to give you the kingdom” (Luke 12:32).'),
  H('6. A Kingdom Appointed'),
  P('“I appoint unto you a kingdom… and sit on thrones judging the twelve tribes of Israel” (Luke 22:29–30).'))

S(4, "Christ in Luke: The Prophetic Trajectory",
  H('1. A Saviour, Christ the Lord'),
  P('“Unto you is born this day in the city of David a Saviour, which is Christ the Lord” (Luke 2:11).'),
  H('2. Seeking the Lost'),
  P('“The Son of man is come to seek and to save that which was lost” (Luke 19:10).'),
  H('3. The Cup of the New Testament'),
  P('“This cup is the new testament in my blood, which is shed for you” (Luke 22:20), reported as written, at the table with the Twelve.'),
  H('4. Concerning Himself'),
  P('“Beginning at Moses and all the prophets, he expounded unto them in all the scriptures the things concerning himself” (Luke 24:27).'))

S(5, "Israel’s Identity in Luke",
  P("Luke reinforces Israel’s:"),
  L('the throne of David and the house of Jacob (Luke 1:32–33)', 'the Lord God of Israel who visited and redeemed his people (Luke 1:68)', 'the little flock given the kingdom (Luke 12:32)', 'the twelve tribes of Israel judged from thrones (Luke 22:30)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Luke does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its throne of David, its kingdom for the little flock, its thrones for the Twelve and its repentance and remission preached beginning at Jerusalem belong exclusively to Israel’s program; its words on mercy, humility and love of neighbour are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Luke", "Program Identity", "Scripture"], [
    ['The Throne of David', '“the Lord God shall give unto him the throne of his father David.”', ISR, 'Luke 1:32'],
    ['The House of Jacob', '“he shall reign over the house of Jacob for ever.”', ISR, 'Luke 1:33'],
    ['Redeemed His People', '“Blessed be the Lord God of Israel; for he hath visited and redeemed his people.”', ISR, 'Luke 1:68'],
    ['The City of David', '“unto you is born this day in the city of David a Saviour, which is Christ the Lord.”', ISR, 'Luke 2:11'],
    ['The Acceptable Year', '“To preach the acceptable year of the Lord.”', ISR, 'Luke 4:19'],
    ['The Kingdom to the Little Flock', '“it is your Father’s good pleasure to give you the kingdom.”', ISR, 'Luke 12:32'],
    ['Seeking the Lost', '“the Son of man is come to seek and to save that which was lost.”', ISR, 'Luke 19:10'],
    ['The Cup', '“This cup is the new testament in my blood, which is shed for you.”', ISR, 'Luke 22:20'],
    ['A Kingdom Appointed', '“I appoint unto you a kingdom.”', ISR, 'Luke 22:29'],
    ['Twelve Tribes Judged', '“sit on thrones judging the twelve tribes of Israel.”', ISR, 'Luke 22:30'],
    ['The Things Written', '“all things must be fulfilled, which were written in the law of Moses, and in the prophets, and in the psalms, concerning me.”', ISR, 'Luke 24:44'],
    ['Beginning at Jerusalem', '“that repentance and remission of sins should be preached in his name among all nations, beginning at Jerusalem.”', ISR, 'Luke 24:47'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Love Your Enemies', '“Love your enemies, do good to them which hate you.”', 'Luke 6:27'],
    ['As You Would Be Treated', '“as ye would that men should do to you, do ye also to them likewise.”', 'Luke 6:31'],
    ['Merciful as the Father', '“Be ye therefore merciful, as your Father also is merciful.”', 'Luke 6:36'],
    ['Love of God and Neighbour', '“Thou shalt love the Lord thy God with all thy heart… and thy neighbour as thyself.”', 'Luke 10:27'],
    ['Go and Do Likewise', '“Go, and do thou likewise.”', 'Luke 10:37'],
    ['Beware Covetousness', '“a man’s life consisteth not in the abundance of the things which he possesseth.”', 'Luke 12:15'],
    ['Humility', '“whosoever exalteth himself shall be abased; and he that humbleth himself shall be exalted.”', 'Luke 14:11'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the throne of David, the little flock or the Twelve; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Love your enemies</b> — Do good to them that hate you (Luke 6:27).', '<b>Be merciful</b> — As your Father is merciful (Luke 6:36).', '<b>Love God and neighbour</b> — With heart, soul, strength and mind (Luke 10:27).', '<b>Show mercy</b> — Go, and do likewise (Luke 10:37).', '<b>Beware covetousness</b> — Life is more than possessions (Luke 12:15).', '<b>Humble yourself</b> — He that humbleth himself shall be exalted (Luke 14:11).'))

S(10, "Teaching Outline for Luke",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Promise and the Birth (Chs. 1–2) — The throne of David. <i>(Luke 1:32–33, 68; 2:10–11)</i>', 'The Anointed Preacher (Chs. 3–4) — The acceptable year. <i>(Luke 4:18–19, 43)</i>', 'Teaching and Mercy (Chs. 5–9) — Love your enemies. <i>(Luke 6:27, 31, 36)</i>', 'The Road to Jerusalem (Chs. 10–19) — Seeking the lost. <i>(Luke 10:27, 37; 12:15, 32; 14:11; 19:10)</i>', 'The Supper and the Cross (Chs. 20–23) — A kingdom appointed. <i>(Luke 22:20, 29–30)</i>', 'The Risen Lord (Ch. 24) — The things concerning himself. <i>(Luke 24:25–27, 44, 47)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Luke, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward mercy, humility, and love of neighbour without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Luke simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Luke stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
