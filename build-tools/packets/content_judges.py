# DRAFT for publisher approval.
BOOK = "Judges"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Deliverers Raised Up, Israel’s Repeated Failure, and the Need of a King"
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
  P('Judges covers the time after Joshua, when “there arose another generation after them, which knew not the LORD” (Judg. 2:10). It records a repeating pattern: Israel does evil, the LORD gives them into the hand of enemies, they cry out, and the LORD raises up a deliverer (Judg. 2:11, 16; 3:9; 6:1). The book names Othniel, Deborah, Gideon, Jephthah and Samson, and closes with the words that “every man did that which was right in his own eyes” (Judg. 21:25).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel is God’s covenant nation in the land, its judges raised up by the LORD to deliver it (Judg. 2:1, 16).'))

S(2, "Narrative Flow of Judges",
  H('Movement 1 — Unfinished Conquest and Decline (Chs. 1–3)'),
  P('Israel asks who shall go up first, the angel of the LORD speaks at Bochim, the next generation does not know the LORD, and Othniel is raised up (Judg. 1:1; 2:1, 10–11; 3:9).'),
  H('Movement 2 — Deborah and Gideon (Chs. 4–8)'),
  P('Deborah judges Israel, the LORD sends Gideon against Midian, reduces his army, and Gideon refuses to rule (Judg. 4:4; 6:12, 14; 7:2, 7; 8:23).'),
  H('Movement 3 — Abimelech, Jephthah, and Samson (Chs. 9–16)'),
  P('The Spirit of the LORD comes on Jephthah and on Samson, who was to begin to deliver Israel from the Philistines (Judg. 11:29; 13:5; 14:6; 16:30).'),
  H('Movement 4 — Israel Without a King (Chs. 17–21)'),
  P('The book closes in idolatry and violence, with the verdict that there was no king in Israel (Judg. 17:6; 21:25).'))

S(3, "Prophecy-Program Themes in Judges",
  H('1. The Cycle'),
  P('“The children of Israel did evil in the sight of the LORD, and served Baalim” (Judg. 2:11).'),
  H('2. The LORD Raises Up Judges'),
  P('“The LORD raised up judges, which delivered them out of the hand of those that spoiled them” (Judg. 2:16).'),
  H('3. The Covenant Remembered'),
  P('“I will never break my covenant with you” (Judg. 2:1).'),
  H('4. The LORD Saves by Few'),
  P('“By the three hundred men that lapped will I save you” (Judg. 7:7).'),
  H('5. The LORD Rules'),
  P('“The LORD shall rule over you” (Judg. 8:23).'),
  H('6. No King in Israel'),
  P('“In those days there was no king in Israel, but every man did that which was right in his own eyes” (Judg. 17:6).'))

S(4, "Christ in Judges: The Prophetic Trajectory",
  H('1. The Deliverer Pattern'),
  P('The judges deliver Israel from enemies for a time (Judg. 2:16, 18), within Israel’s own history in the land.'),
  H('2. The Call for a King'),
  P('The closing verses state that there was no king in Israel (Judg. 21:25), and 1 Samuel takes up that question.'),
  H('3. The LORD as Israel’s Ruler'),
  P('Gideon’s answer, “the LORD shall rule over you” (Judg. 8:23), is reported as written.'))

S(5, "Israel’s Identity in Judges",
  P("Judges reinforces Israel’s:"),
  L('covenant with the LORD who will “never break” it (Judg. 2:1)', 'cycle of sin, oppression, cry and deliverance (Judg. 2:11, 16; 3:9)', 'judges raised up by the LORD (Judg. 2:16, 18)', 'call to be ruled by the LORD (Judg. 8:23)', 'life in the land without a king (Judg. 21:25)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Judges does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its judges, enemies, land and cycle of deliverance belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Judges", "Program Identity", "Scripture"], [
    ['The Covenant Held', '“I will never break my covenant with you.”', ISR, 'Judg. 2:1'],
    ['A Generation That Knew Not', '“another generation after them, which knew not the LORD.”', ISR, 'Judg. 2:10'],
    ['Judges Raised Up', '“the LORD raised up judges, which delivered them out of the hand of those that spoiled them.”', ISR, 'Judg. 2:16'],
    ['Othniel the Deliverer', '“the LORD raised up a deliverer to the children of Israel.”', ISR, 'Judg. 3:9'],
    ['Deborah the Prophetess', '“Deborah, a prophetess… she judged Israel at that time.”', ISR, 'Judg. 4:4'],
    ['Gideon Sent', '“Go in this thy might, and thou shalt save Israel from the hand of the Midianites.”', ISR, 'Judg. 6:14'],
    ['The LORD Ruling', '“the LORD shall rule over you.”', ISR, 'Judg. 8:23'],
    ['Samson Appointed', '“he shall begin to deliver Israel out of the hand of the Philistines.”', ISR, 'Judg. 13:5'],
    ['The Spirit on Jephthah', '“Then the Spirit of the LORD came upon Jephthah.”', ISR, 'Judg. 11:29'],
    ['No King in Israel', '“In those days there was no king in Israel.”', ISR, 'Judg. 21:25'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['God Hears Their Cry', '“when the children of Israel cried unto the LORD, the LORD raised up a deliverer.”', 'Judg. 3:9'],
    ['Salvation Is the LORD’s', '“lest Israel vaunt themselves against me, saying, Mine own hand hath saved me.”', 'Judg. 7:2'],
    ['The LORD Is With the Faithful', '“The LORD is with thee, thou mighty man of valour.”', 'Judg. 6:12'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant deliverance or the judges’ office; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Cry out to the LORD</b> — He hears (Judg. 3:9).', '<b>Give Him the credit for salvation</b> — It is not our own hand (Judg. 7:2).', '<b>Trust His presence</b> — The LORD is with His servants (Judg. 6:12).'))

S(10, "Teaching Outline for Judges",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Unfinished Conquest (Chs. 1–3) — The new generation. <i>(Judg. 2:1, 10–11; 3:9)</i>', 'Deborah and Gideon (Chs. 4–8) — Deliverers raised up. <i>(Judg. 4:4; 6:14; 7:2, 7; 8:23)</i>', 'Jephthah and Samson (Chs. 9–16) — The Spirit and the Philistines. <i>(Judg. 11:29; 13:5; 16:30)</i>', 'Without a King (Chs. 17–21) — Every man right in his own eyes. <i>(Judg. 17:6; 21:25)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Judges, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward humility, repentance, and trust without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Judges simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Judges stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
