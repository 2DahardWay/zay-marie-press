# DRAFT for publisher approval.
BOOK = "Psalms"
TESTAMENT = "Old Testament"
GENRE = "poetry"
SUBTITLE = "Israel’s Songbook of Praise, Lament, and the Coming King"
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
  P('Psalms is the songbook of Israel in five books of prayer, praise, lament and trust. It opens with the blessed man who delights “in the law of the LORD” (Ps. 1:2), speaks of the king set “upon my holy hill of Zion” (Ps. 2:6), carries the songs of David, the songs of the temple and of the exile, and closes in praise (Ps. 89:3; 137:1; 145:3).'),
  BOX("Program Identity:", 'This book is Israel’s songbook, built around Zion, David’s throne, the covenant, the law and the land, and it also speaks of God to all who hear it (Ps. 2:6; 89:3; 147:19).'))

S(2, "Narrative Flow of Psalms",
  H('Movement 1 — The Blessed Man and the King (Pss. 1–41)'),
  P('The way of the righteous and the way of the wicked is set out, and the LORD sets His king upon Zion (Ps. 1:1–2; 2:6; 23:1; 32:1).'),
  H('Movement 2 — Songs of Zion and Lament (Pss. 42–72)'),
  P('Songs of the sanctuary and of the king, and a prayer that his dominion be from sea to sea (Ps. 46:1; 51:10; 72:8).'),
  H('Movement 3 — The Covenant and the Hard Questions (Pss. 73–89)'),
  P('The testimony in Jacob is recalled and the covenant with David is sworn (Ps. 78:5; 87:2; 89:3, 34).'),
  H('Movement 4 — The LORD Reigns (Pss. 90–106)'),
  P('The LORD is God from everlasting, and the nations are told that He reigns (Ps. 90:2; 96:10; 102:13; 105:8).'),
  H('Movement 5 — Praise and the Word (Pss. 107–150)'),
  P('The LORD sits at the right hand, the word is a lamp, Zion is remembered, and the book closes in praise (Ps. 110:1; 119:105; 137:1; 145:3; 147:2; 149:2).'))

S(3, "Prophecy-Program Themes in Psalms",
  H('1. The Law of the LORD'),
  P('“His delight is in the law of the LORD; and in his law doth he meditate day and night” (Ps. 1:2).'),
  H('2. The King on Zion'),
  P('“Yet have I set my king upon my holy hill of Zion” (Ps. 2:6).'),
  H('3. The Covenant with David'),
  P('“I have made a covenant with my chosen, I have sworn unto David my servant” (Ps. 89:3).'),
  H('4. The Throne Sworn'),
  P('“The LORD hath sworn in truth unto David; he will not turn from it” (Ps. 132:11).'),
  H('5. Zion Favoured'),
  P('“Thou shalt arise, and have mercy upon Zion: for the time to favour her, yea, the set time, is come” (Ps. 102:13).'),
  H('6. The Outcasts Gathered'),
  P('“The LORD doth build up Jerusalem: he gathereth together the outcasts of Israel” (Ps. 147:2).'),
  H('7. His Word to Jacob'),
  P('“He sheweth his word unto Jacob, his statutes and his judgments unto Israel” (Ps. 147:19).'))

S(4, "Christ in Psalms: The Prophetic Trajectory",
  H('1. The Son'),
  P('“Thou art my Son; this day have I begotten thee” (Ps. 2:7) is quoted in the New Testament (Acts 13:33; Heb. 1:5).'),
  H('2. The Forsaken One'),
  P('“My God, my God, why hast thou forsaken me?” (Ps. 22:1) is quoted by the Lord on the cross (Matt. 27:46).'),
  H('3. The Holy One'),
  P('“Thou wilt not leave my soul in hell; neither wilt thou suffer thine Holy One to see corruption” (Ps. 16:10) is quoted in Acts (Acts 2:27; 13:35).'),
  H('4. The Right Hand'),
  P('“The LORD said unto my Lord, Sit thou at my right hand” (Ps. 110:1) is quoted by the Lord and in the New Testament (Matt. 22:44; Heb. 1:13).'),
  H('5. The Stone'),
  P('“The stone which the builders refused is become the head stone of the corner” (Ps. 118:22) is quoted by the Lord (Matt. 21:42).'))

S(5, "Israel’s Identity in Psalms",
  P("Psalms reinforces Israel’s:"),
  L('the covenant sworn to David (Ps. 89:3; 132:11)', 'Zion as the place of the LORD’s king and favour (Ps. 2:6; 102:13)', 'the testimony and law given to Jacob (Ps. 78:5; 147:19)', 'the outcasts of Israel gathered (Ps. 147:2)', 'the LORD’s choice of Jacob and Israel (Ps. 135:4)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Psalms does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its covenant with David, its law, its Zion and its temple worship belong exclusively to Israel; its songs of praise and trust are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Psalms", "Program Identity", "Scripture"], [
    ['The King on Zion', '“Yet have I set my king upon my holy hill of Zion.”', ISR, 'Ps. 2:6'],
    ['The Son', '“Thou art my Son; this day have I begotten thee.”', ISR, 'Ps. 2:7'],
    ['The King’s Dominion', '“He shall have dominion also from sea to sea.”', ISR, 'Ps. 72:8'],
    ['The Testimony in Jacob', '“he established a testimony in Jacob, and appointed a law in Israel.”', ISR, 'Ps. 78:5'],
    ['The Gates of Zion', '“The LORD loveth the gates of Zion more than all the dwellings of Jacob.”', ISR, 'Ps. 87:2'],
    ['The Covenant with David', '“I have made a covenant with my chosen, I have sworn unto David my servant.”', ISR, 'Ps. 89:3'],
    ['The Covenant Unbroken', '“My covenant will I not break, nor alter the thing that is gone out of my lips.”', ISR, 'Ps. 89:34'],
    ['The Set Time for Zion', '“Thou shalt arise, and have mercy upon Zion.”', ISR, 'Ps. 102:13'],
    ['The Chosen People', '“the LORD hath chosen Jacob unto himself, and Israel for his peculiar treasure.”', ISR, 'Ps. 135:4'],
    ['The Throne Sworn', '“The LORD hath sworn in truth unto David; he will not turn from it.”', ISR, 'Ps. 132:11'],
    ['The Outcasts Gathered', '“he gathereth together the outcasts of Israel.”', ISR, 'Ps. 147:2'],
    ['Word to Jacob', '“He sheweth his word unto Jacob, his statutes and his judgments unto Israel.”', ISR, 'Ps. 147:19'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The Blessed Man', '“Blessed is the man that walketh not in the counsel of the ungodly.”', 'Ps. 1:1'],
    ['The Heavens Declare', '“The heavens declare the glory of God; and the firmament sheweth his handywork.”', 'Ps. 19:1'],
    ['The Shepherd', '“The LORD is my shepherd; I shall not want.”', 'Ps. 23:1'],
    ['The Earth Is the LORD’s', '“The earth is the LORD’s, and the fulness thereof.”', 'Ps. 24:1'],
    ['A Present Help', '“God is our refuge and strength, a very present help in trouble.”', 'Ps. 46:1'],
    ['A Clean Heart', '“Create in me a clean heart, O God; and renew a right spirit within me.”', 'Ps. 51:10'],
    ['From Everlasting', '“from everlasting to everlasting, thou art God.”', 'Ps. 90:2'],
    ['Merciful and Gracious', '“The LORD is merciful and gracious, slow to anger, and plenteous in mercy.”', 'Ps. 103:8'],
    ['Forgiveness', '“there is forgiveness with thee, that thou mayest be feared.”', 'Ps. 130:4'],
    ['A Lamp', '“Thy word is a lamp unto my feet, and a light unto my path.”', 'Ps. 119:105'],
    ['Fearfully Made', '“I am fearfully and wonderfully made.”', 'Ps. 139:14'],
    ['Great Is the LORD', '“Great is the LORD, and greatly to be praised; and his greatness is unsearchable.”', 'Ps. 145:3'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant with David, law or Zion; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Delight in His word</b> — A lamp unto my feet (Ps. 119:105).', '<b>See the Creator in creation</b> — The heavens declare His glory (Ps. 19:1).', '<b>Rest in His care</b> — The LORD is my shepherd (Ps. 23:1).', '<b>Run to Him in trouble</b> — A very present help (Ps. 46:1).', '<b>Pray for a clean heart</b> — Create in me a clean heart (Ps. 51:10).', '<b>Rely on His mercy</b> — Merciful, gracious and slow to anger (Ps. 103:8).', '<b>Take forgiveness seriously</b> — With thee is forgiveness (Ps. 130:4).', '<b>Praise the greatness of the LORD</b> — His greatness is unsearchable (Ps. 145:3).'))

S(10, "Teaching Outline for Psalms",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Blessed Man and the King (Pss. 1–41) — Two ways and the king on Zion. <i>(Ps. 1:1–2; 2:6; 23:1)</i>', 'Songs of Zion and Lament (Pss. 42–72) — Refuge, repentance and the king’s dominion. <i>(Ps. 46:1; 51:10; 72:8)</i>', 'The Covenant and the Hard Questions (Pss. 73–89) — Jacob’s testimony and David’s covenant. <i>(Ps. 78:5; 89:3, 34)</i>', 'The LORD Reigns (Pss. 90–106) — From everlasting to everlasting. <i>(Ps. 90:2; 102:13)</i>', 'Praise and the Word (Pss. 107–150) — The word, Zion remembered, and the closing praise. <i>(Ps. 119:105; 137:1; 145:3; 147:2)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Psalms, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward worship, trust, and honest prayer without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Psalms simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Psalms stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
