# DRAFT for publisher approval.
BOOK = "Nehemiah"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "The Wall Rebuilt, the Law Read, and the Covenant Renewed"
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
  P('Nehemiah begins with the prayer of the cupbearer to the king of Persia and follows his return to Jerusalem. It records the rebuilding of the wall in fifty and two days, the reading of the book of the law, the confession of the people, the sure covenant and its oath, the dedication of the wall, and Nehemiah’s final reforms (Neh. 1:5; 2:17–18; 6:15; 8:1, 8; 9:17, 38; 10:29; 12:43; 13:14).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where a remnant of Israel rebuilds Jerusalem and renews the covenant under the law of Moses (Neh. 8:1; 10:29).'))

S(2, "Narrative Flow of Nehemiah",
  H('Movement 1 — Nehemiah’s Prayer and Commission (Chs. 1–2)'),
  P('Nehemiah prays to the LORD God of heaven and tells the people, “Let us rise up and build” (Neh. 1:5, 9; 2:17–18, 20).'),
  H('Movement 2 — The Wall Built (Chs. 3–7)'),
  P('The wall is built and finished in fifty and two days (Neh. 4:6; 6:15).'),
  H('Movement 3 — The Law Read and the Covenant Renewed (Chs. 8–10)'),
  P('Ezra reads the book of the law, they give the sense, the people confess, and they make a sure covenant (Neh. 8:1, 8, 12; 9:5–6, 17, 32, 38; 10:29).'),
  H('Movement 4 — Dedication and Reform (Chs. 11–13)'),
  P('The wall is dedicated with great joy, and Nehemiah prays, “Remember me, O my God, for good” (Neh. 12:43; 13:14, 31).'))

S(3, "Prophecy-Program Themes in Nehemiah",
  H('1. The Great and Terrible God'),
  P('“O LORD God of heaven, the great and terrible God, that keepeth covenant and mercy for them that love him and observe his commandments” (Neh. 1:5).'),
  H('2. The Place He Chose'),
  P('“Will I gather them from thence, and will bring them unto the place that I have chosen to set my name there” (Neh. 1:9).'),
  H('3. The Wall Finished'),
  P('“So the wall was finished in the twenty and fifth day of the month Elul, in fifty and two days” (Neh. 6:15).'),
  H('4. The Law Read and Understood'),
  P('“They read in the book in the law of God distinctly, and gave the sense, and caused them to understand the reading” (Neh. 8:8).'),
  H('5. A Sure Covenant'),
  P('“We make a sure covenant, and write it” (Neh. 9:38).'))

S(4, "Christ in Nehemiah: The Prophetic Trajectory",
  H('1. The Restored City'),
  P('Jerusalem’s wall is rebuilt by a returned remnant (Neh. 6:15), reported as written within Israel’s program.'),
  H('2. The Book of the Law'),
  P('The people ask for the book of the law of Moses, which the LORD had commanded to Israel (Neh. 8:1).'),
  H('3. The Covenant Oath'),
  P('They enter into an oath to walk in God’s law, which was given by Moses (Neh. 10:29).'))

S(5, "Israel’s Identity in Nehemiah",
  P("Nehemiah reinforces Israel’s:"),
  L('the rebuilt wall and city (Neh. 2:17; 6:15)', 'the book of the law of Moses (Neh. 8:1)', 'the sure covenant and oath (Neh. 9:38; 10:29)', 'the place the LORD chose for His name (Neh. 1:9)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Nehemiah does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its wall, city, law and covenant oath belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Nehemiah", "Program Identity", "Scripture"], [
    ['The Place Chosen', '“the place that I have chosen to set my name there.”', ISR, 'Neh. 1:9'],
    ['Rise Up and Build', '“Let us rise up and build.”', ISR, 'Neh. 2:18'],
    ['Wall Finished', '“in fifty and two days.”', ISR, 'Neh. 6:15'],
    ['The Book of the Law of Moses', '“the book of the law of Moses, which the LORD had commanded to Israel.”', ISR, 'Neh. 8:1'],
    ['A Sure Covenant', '“we make a sure covenant, and write it.”', ISR, 'Neh. 9:38'],
    ['The Oath', '“to walk in God’s law, which was given by Moses the servant of God.”', ISR, 'Neh. 10:29'],
    ['The Wall Dedicated', '“God had made them rejoice with great joy.”', ISR, 'Neh. 12:43'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['God Keeps Covenant', '“the great and terrible God, that keepeth covenant and mercy for them that love him.”', 'Neh. 1:5'],
    ['The LORD Alone', '“Thou, even thou, art LORD alone; thou hast made heaven, the heaven of heavens.”', 'Neh. 9:6'],
    ['Ready to Pardon', '“thou art a God ready to pardon, gracious and merciful, slow to anger, and of great kindness.”', 'Neh. 9:17'],
    ['Understanding the Word', '“they had understood the words that were declared unto them.”', 'Neh. 8:12'],
    ['Remember Me for Good', '“Remember me, O my God, for good.”', 'Neh. 13:31'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s wall, city or covenant oath; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Pray with confidence in His covenant mercy</b> (Neh. 1:5).', '<b>Confess the LORD alone as Creator</b> (Neh. 9:6).', '<b>Trust that He is ready to pardon</b> (Neh. 9:17).', '<b>Read the Word until it is understood</b> (Neh. 8:8, 12).'))

S(10, "Teaching Outline for Nehemiah",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Prayer and Commission (Chs. 1–2) — Rise up and build. <i>(Neh. 1:5, 9; 2:17–18)</i>', 'The Wall Built (Chs. 3–7) — Fifty and two days. <i>(Neh. 4:6; 6:15)</i>', 'The Law Read (Chs. 8–10) — The sure covenant. <i>(Neh. 8:1, 8, 12; 9:6, 17, 38; 10:29)</i>', 'Dedication and Reform (Chs. 11–13) — Remember me for good. <i>(Neh. 12:43; 13:14, 31)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Nehemiah, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward prayer, perseverance, and humility without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Nehemiah simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Nehemiah stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
