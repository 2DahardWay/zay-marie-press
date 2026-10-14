# DRAFT for publisher approval.
BOOK = "Ruth"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "A Moabitess in Israel, the Kinsman’s Redemption, and the Line to David"
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
  P('Ruth is a short account set in the days of the judges. It follows Naomi and her daughter in law Ruth the Moabitess, Ruth’s vow to Naomi, her gleaning in the field of Boaz, his place as a near kinsman, his purchase of the inheritance, and the birth of Obed, who is “the father of Jesse, the father of David” (Ruth 1:16; 2:2; 3:9; 4:10, 17).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel’s land, inheritance and kinsman law shape every scene and the line runs to David (Ruth 4:10, 17, 22).'))

S(2, "Narrative Flow of Ruth",
  H('Movement 1 — Naomi and Ruth (Ch. 1)'),
  P('Ruth tells Naomi, “thy people shall be my people, and thy God my God,” and says she will be buried where Naomi dies (Ruth 1:16–17).'),
  H('Movement 2 — Gleaning in Boaz’s Field (Ch. 2)'),
  P('Ruth goes to glean, Boaz speaks a blessing over her, and Naomi names him as one of their next kinsmen (Ruth 2:2, 12, 20).'),
  H('Movement 3 — At the Threshing Floor (Ch. 3)'),
  P('Ruth asks Boaz to spread his skirt over her as a near kinsman, and he answers that the city knows she is a virtuous woman (Ruth 3:9, 11).'),
  H('Movement 4 — The Redemption and the Line to David (Ch. 4)'),
  P('Boaz purchases the inheritance, takes Ruth as his wife, and Obed is born, the father of Jesse, the father of David (Ruth 4:10, 13–14, 17, 22).'))

S(3, "Prophecy-Program Themes in Ruth",
  H('1. Loyalty to Naomi and Her God'),
  P('“Whither thou goest, I will go; and where thou lodgest, I will lodge: thy people shall be my people, and thy God my God” (Ruth 1:16).'),
  H('2. The LORD Recompenses'),
  P('“The LORD recompense thy work, and a full reward be given thee of the LORD God of Israel, under whose wings thou art come to trust” (Ruth 2:12).'),
  H('3. The Near Kinsman'),
  P('“I am Ruth thine handmaid: spread therefore thy skirt over thine handmaid; for thou art a near kinsman” (Ruth 3:9).'),
  H('4. The Inheritance Purchased'),
  P('“To raise up the name of the dead upon his inheritance, that the name of the dead be not cut off from among his brethren” (Ruth 4:10).'),
  H('5. The Line to David'),
  P('“They called his name Obed: he is the father of Jesse, the father of David” (Ruth 4:17).'))

S(4, "Christ in Ruth: The Prophetic Trajectory",
  H('1. The Kinsman'),
  P('Boaz acts as a near kinsman who purchases the inheritance (Ruth 3:9; 4:10).'),
  H('2. The Line to David'),
  P('The book closes with “Obed begat Jesse, and Jesse begat David” (Ruth 4:22).'),
  H('3. The Gentile in Israel’s Line'),
  P('A Moabitess comes under the wings of the LORD God of Israel and stands in David’s line (Ruth 2:12; 4:17); the book reports this as written and assigns it to the Prophecy Program.'))

S(5, "Israel’s Identity in Ruth",
  P("Ruth reinforces Israel’s:"),
  L('land and inheritance within the tribes (Ruth 4:10)', 'kinsman’s right to redeem (Ruth 3:9; 4:10)', 'the LORD God of Israel (Ruth 2:12)', 'the line to David (Ruth 4:17, 22)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Ruth does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its kinsman law, inheritance, gleaning and line to David belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Ruth", "Program Identity", "Scripture"], [
    ['Ruth Joins Israel’s People', '“thy people shall be my people, and thy God my God.”', ISR, 'Ruth 1:16'],
    ['Under the Wings of the LORD God of Israel', '“under whose wings thou art come to trust.”', ISR, 'Ruth 2:12'],
    ['The Near Kinsman', '“near of kin unto us, one of our next kinsmen.”', ISR, 'Ruth 2:20'],
    ['Asking the Kinsman', '“for thou art a near kinsman.”', ISR, 'Ruth 3:9'],
    ['The Inheritance Purchased', '“to raise up the name of the dead upon his inheritance.”', ISR, 'Ruth 4:10'],
    ['A Kinsman for Naomi', '“Blessed be the LORD, which hath not left thee this day without a kinsman.”', ISR, 'Ruth 4:14'],
    ['The Line to David', '“Obed begat Jesse, and Jesse begat David.”', ISR, 'Ruth 4:22'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Kindness Remembered', '“Blessed be he of the LORD, who hath not left off his kindness to the living and to the dead.”', 'Ruth 2:20'],
    ['A Virtuous Woman', '“all the city of my people doth know that thou art a virtuous woman.”', 'Ruth 3:11'],
    ['The LORD Gives Life', '“the LORD gave her conception, and she bare a son.”', 'Ruth 4:13'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s kinsman law or inheritance; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Show faithful kindness</b> — To the living and the dead (Ruth 2:20).', '<b>Pursue a good name</b> — A virtuous character is known (Ruth 3:11).', '<b>Thank the LORD for His gifts</b> — Life and children are from Him (Ruth 4:13).'))

S(10, "Teaching Outline for Ruth",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Naomi and Ruth (Ch. 1) — Loyalty and a vow. <i>(Ruth 1:16–17)</i>', 'Gleaning in Boaz’s Field (Ch. 2) — Blessing and kindness. <i>(Ruth 2:12, 20)</i>', 'At the Threshing Floor (Ch. 3) — The near kinsman. <i>(Ruth 3:9, 11)</i>', 'The Redemption (Ch. 4) — The line to David. <i>(Ruth 4:10, 13–14, 17, 22)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Ruth, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward kindness, loyalty, and trust without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Ruth simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Ruth stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
