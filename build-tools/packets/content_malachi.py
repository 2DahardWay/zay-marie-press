# DRAFT for publisher approval.
BOOK = "Malachi"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Burden to Israel, the Messenger of the Covenant, and the Sun of Righteousness"
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
  P('Malachi is “the burden of the word of the LORD to Israel by Malachi” (Mal. 1:1). It reproves the priests, charges Judah with treachery against the covenant of the fathers, calls for the tithes to the storehouse, records a book of remembrance for those who feared the LORD, and closes with the day that burns as an oven, the Sun of righteousness, the law of Moses and Elijah the prophet (Mal. 2:10; 3:10, 16–17; 4:1–2, 4–6).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to Israel, to the priests and to the sons of Jacob about the covenant of the fathers, the law of Moses and the great and dreadful day (Mal. 1:1; 3:6; 4:4–5).'))

S(2, "Narrative Flow of Malachi",
  H('Movement 1 — The LORD’s Love and the Priests’ Dishonour (Ch. 1)'),
  P('The LORD speaks to Israel and rebukes the priests who despise His name (Mal. 1:1, 6).'),
  H('Movement 2 — Treachery Against the Covenant (Ch. 2)'),
  P('The priest’s lips should keep knowledge, and Judah deals treacherously against his brother (Mal. 2:7, 10, 16).'),
  H('Movement 3 — The Messenger and the Tithes (Ch. 3)'),
  P('The LORD changes not, calls for the tithes, and writes a book of remembrance (Mal. 3:2, 6, 10, 16–17).'),
  H('Movement 4 — The Day and Elijah (Ch. 4)'),
  P('The day burns as an oven, the Sun of righteousness arises, and Elijah the prophet is sent (Mal. 4:1–2, 4–6).'))

S(3, "Prophecy-Program Themes in Malachi",
  H('1. The Burden to Israel'),
  P('“The burden of the word of the LORD to Israel by Malachi” (Mal. 1:1).'),
  H('2. The Priest’s Lips'),
  P('“The priest’s lips should keep knowledge, and they should seek the law at his mouth” (Mal. 2:7).'),
  H('3. The Covenant of the Fathers'),
  P('“Why do we deal treacherously every man against his brother, by profaning the covenant of our fathers?” (Mal. 2:10).'),
  H('4. The LORD Changes Not'),
  P('“I am the LORD, I change not; therefore ye sons of Jacob are not consumed” (Mal. 3:6).'),
  H('5. The Book of Remembrance'),
  P('“A book of remembrance was written before him for them that feared the LORD” (Mal. 3:16).'),
  H('6. The Sun of Righteousness'),
  P('“Unto you that fear my name shall the Sun of righteousness arise with healing in his wings” (Mal. 4:2).'),
  H('7. Elijah Sent'),
  P('“I will send you Elijah the prophet before the coming of the great and dreadful day of the LORD” (Mal. 4:5).'))

S(4, "Christ in Malachi: The Prophetic Trajectory",
  H('1. The Sun of Righteousness'),
  P('The Sun of righteousness who arises with healing in his wings (Mal. 4:2) is reported as written.'),
  H('2. The Day Like an Oven'),
  P('The day that burns as an oven, leaving the proud neither root nor branch (Mal. 4:1), stands within Israel’s prophetic hope.'),
  H('3. Elijah Before the Day'),
  P('The promise to send Elijah before the great and dreadful day (Mal. 4:5) is reported as written; the Gospels’ references to John and Elijah are read in their own chapters.'))

S(5, "Israel’s Identity in Malachi",
  P("Malachi reinforces Israel’s:"),
  L('Israel addressed by the burden of the word of the LORD (Mal. 1:1)', 'the priests, the law of Moses and the covenant of the fathers (Mal. 2:7, 10; 4:4)', 'the sons of Jacob who are not consumed (Mal. 3:6)', 'the tithes brought into the storehouse (Mal. 3:10)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Malachi does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its burden to Israel, its covenant of the fathers, its tithes, its day and Elijah belong exclusively to Israel; its words on the LORD who changes not and on one Father and one Creator are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Malachi", "Program Identity", "Scripture"], [
    ['The Burden to Israel', '“The burden of the word of the LORD to Israel by Malachi.”', ISR, 'Mal. 1:1'],
    ['The Priest’s Lips', '“the priest’s lips should keep knowledge, and they should seek the law at his mouth.”', ISR, 'Mal. 2:7'],
    ['The Covenant of the Fathers', '“profaning the covenant of our fathers.”', ISR, 'Mal. 2:10'],
    ['Sons of Jacob', '“ye sons of Jacob are not consumed.”', ISR, 'Mal. 3:6'],
    ['The Tithes', '“Bring ye all the tithes into the storehouse.”', ISR, 'Mal. 3:10'],
    ['The Book of Remembrance', '“a book of remembrance was written before him for them that feared the LORD.”', ISR, 'Mal. 3:16'],
    ['The Day Like an Oven', '“the day cometh, that shall burn as an oven.”', ISR, 'Mal. 4:1'],
    ['The Sun of Righteousness', '“unto you that fear my name shall the Sun of righteousness arise with healing in his wings.”', ISR, 'Mal. 4:2'],
    ['The Law of Moses', '“Remember ye the law of Moses my servant, which I commanded unto him in Horeb for all Israel.”', ISR, 'Mal. 4:4'],
    ['Elijah Sent', '“I will send you Elijah the prophet before the coming of the great and dreadful day of the LORD.”', ISR, 'Mal. 4:5'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['One Father, One God', '“Have we not all one father? hath not one God created us?”', 'Mal. 2:10'],
    ['The LORD Changes Not', '“I am the LORD, I change not.”', 'Mal. 3:6'],
    ['Justice for the Vulnerable', '“against those that oppress the hireling in his wages, the widow, and the fatherless.”', 'Mal. 3:5'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the covenant of the fathers, the tithes or Elijah; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Honour the one Father</b> — One God created us (Mal. 2:10).', '<b>Trust the LORD who changes not</b> — He is faithful (Mal. 3:6).', '<b>Do not oppress</b> — The hireling, the widow and the fatherless (Mal. 3:5).'))

S(10, "Teaching Outline for Malachi",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The LORD’s Love and the Priests’ Dishonour (Ch. 1) — A burden to Israel. <i>(Mal. 1:1, 6)</i>', 'Treachery Against the Covenant (Ch. 2) — One Father. <i>(Mal. 2:7, 10)</i>', 'The Messenger and the Tithes (Ch. 3) — The LORD changes not. <i>(Mal. 3:5–6, 10, 16–17)</i>', 'The Day and Elijah (Ch. 4) — The Sun of righteousness. <i>(Mal. 4:1–2, 4–6)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Malachi, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward honour toward God, faithfulness, and fear of His name without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Malachi simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Malachi stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
