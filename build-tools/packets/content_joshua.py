# DRAFT for publisher approval.
BOOK = "Joshua"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Crossing the Jordan, the Conquest, and the Land Divided by Lot"
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
  P('Joshua follows Israel after the death of Moses, when the LORD says, “Moses my servant is dead; now therefore arise, go over this Jordan” (Josh. 1:2). It records the crossing of the Jordan, the fall of Jericho, the battles of the conquest, the division of the land among the tribes, the cities of refuge, and Joshua’s last words and the covenant renewed at Shechem (Josh. 3:17; 6:20; 11:23; 20:2; 24:15).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel is God’s covenant nation brought into the land sworn to its fathers and given to it by tribe (Josh. 1:6; 11:23).'))

S(2, "Narrative Flow of Joshua",
  H('Movement 1 — Preparing to Enter (Chs. 1–5)'),
  P('The LORD commissions Joshua, Rahab hides the spies, Israel crosses the Jordan on dry ground, and the captain of the host of the LORD appears (Josh. 1:2, 9; 2:11; 3:17; 5:14).'),
  H('Movement 2 — The Conquest (Chs. 6–12)'),
  P('Jericho falls, Israel is judged and restored at Ai, and the land is taken in the south and the north (Josh. 6:20; 10:14; 11:23).'),
  H('Movement 3 — The Land Divided (Chs. 13–21)'),
  P('The land that remains is named, the inheritance is divided by tribe, and cities of refuge are appointed (Josh. 13:1; 14:12; 20:2; 21:45).'),
  H('Movement 4 — Joshua’s Farewell (Chs. 22–24)'),
  P('Joshua charges Israel to keep the law of Moses, rehearses what the LORD has done, and the people renew their covenant (Josh. 23:6, 14; 24:2, 13, 15).'))

S(3, "Prophecy-Program Themes in Joshua",
  H('1. The Land Given'),
  P('“Every place that the sole of your foot shall tread upon, that have I given unto you, as I said unto Moses” (Josh. 1:3).'),
  H('2. The Book of the Law'),
  P('“This book of the law shall not depart out of thy mouth” (Josh. 1:8).'),
  H('3. The LORD Fights for Israel'),
  P('“There was no day like that before it or after it, that the LORD hearkened unto the voice of a man: for the LORD fought for Israel” (Josh. 10:14).'),
  H('4. Rest from War'),
  P('“Joshua gave it for an inheritance unto Israel according to their divisions by their tribes. And the land rested from war” (Josh. 11:23).'),
  H('5. Every Promise Kept'),
  P('“There failed not ought of any good thing which the LORD had spoken unto the house of Israel; all came to pass” (Josh. 21:45).'),
  H('6. Choose Whom to Serve'),
  P('“Choose you this day whom ye will serve… but as for me and my house, we will serve the LORD” (Josh. 24:15).'))

S(4, "Christ in Joshua: The Prophetic Trajectory",
  H('1. Joshua the Deliverer'),
  P('Joshua leads Israel into the land and divides the inheritance (Josh. 11:23). His name is the Old Testament form of the name Jesus, and the book reads as Israel’s own deliverance within the Prophecy Program.'),
  H('2. The Captain of the Host'),
  P('Joshua meets one who says, “as captain of the host of the LORD am I now come,” and Joshua worships (Josh. 5:14). The verse is reported as written.'),
  H('3. The Cities of Refuge'),
  P('The LORD tells Joshua to appoint cities of refuge (Josh. 20:2), part of Israel’s covenant provision in the land.'),
  H('4. The Promise Kept'),
  P('“Not one thing hath failed” of the good things the LORD spoke to Israel (Josh. 23:14).'))

S(5, "Israel’s Identity in Joshua",
  P("Joshua reinforces Israel’s:"),
  L('crossing into the land sworn to its fathers (Josh. 1:6; 3:17)', 'conquest and rest from war (Josh. 11:23)', 'inheritance divided by tribe (Josh. 13:1; 14:12)', 'cities of refuge (Josh. 20:2)', 'covenant renewed at Shechem (Josh. 24:15)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Joshua does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its conquest, land division, law and covenant renewal belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Joshua", "Program Identity", "Scripture"], [
    ['Commissioned for the Land', '“Moses my servant is dead; now therefore arise, go over this Jordan.”', ISR, 'Josh. 1:2'],
    ['The Land Sworn', '“unto this people shalt thou divide for an inheritance the land, which I sware unto their fathers to give them.”', ISR, 'Josh. 1:6'],
    ['The Book of the Law', '“This book of the law shall not depart out of thy mouth.”', ISR, 'Josh. 1:8'],
    ['The Jordan Crossed', '“all the Israelites passed over on dry ground.”', ISR, 'Josh. 3:17'],
    ['Jericho Falls', '“the wall fell down flat, so that the people went up into the city.”', ISR, 'Josh. 6:20'],
    ['The LORD Fought for Israel', '“the LORD fought for Israel.”', ISR, 'Josh. 10:14'],
    ['The Land Divided', '“Joshua gave it for an inheritance unto Israel according to their divisions by their tribes.”', ISR, 'Josh. 11:23'],
    ['Cities of Refuge', '“Appoint out for you cities of refuge.”', ISR, 'Josh. 20:2'],
    ['Every Word Fulfilled', '“There failed not ought of any good thing which the LORD had spoken unto the house of Israel.”', ISR, 'Josh. 21:45'],
    ['The Law of Moses Kept', '“to keep and to do all that is written in the book of the law of Moses.”', ISR, 'Josh. 23:6'],
    ['The Covenant Renewed', '“choose you this day whom ye will serve.”', ISR, 'Josh. 24:15'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The LORD Is With You', '“the LORD thy God is with thee whithersoever thou goest.”', 'Josh. 1:9'],
    ['The LORD Is God', '“the LORD your God, he is God in heaven above, and in earth beneath.”', 'Josh. 2:11'],
    ['Faithful to His Word', '“not one thing hath failed of all the good things which the LORD your God spake.”', 'Josh. 23:14'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s conquest, land division or covenant renewal; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Be strong and courageous</b> — The LORD is with you (Josh. 1:9).', '<b>Know who God is</b> — He is God in heaven above and earth beneath (Josh. 2:11).', '<b>Count on His faithfulness</b> — Not one thing hath failed (Josh. 23:14).'))

S(10, "Teaching Outline for Joshua",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Preparing to Enter (Chs. 1–5) — The commission and the crossing. <i>(Josh. 1:2, 9; 3:17)</i>', 'The Conquest (Chs. 6–12) — Jericho and the battles. <i>(Josh. 6:20; 10:14; 11:23)</i>', 'The Land Divided (Chs. 13–21) — Inheritance and refuge. <i>(Josh. 14:12; 20:2; 21:45)</i>', 'Joshua’s Farewell (Chs. 22–24) — The covenant renewed. <i>(Josh. 23:6, 14; 24:15)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Joshua, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward courage, trust, and faithfulness without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Joshua simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Joshua stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
