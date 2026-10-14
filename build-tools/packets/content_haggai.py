# DRAFT for publisher approval.
BOOK = "Haggai"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "Consider Your Ways, Build the House, and the Glory of the Latter House"
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
  P('Haggai records four words of the LORD “by Haggai the prophet unto Zerubbabel the son of Shealtiel, governor of Judah, and to Joshua the son of Josedech, the high priest” (Hag. 1:1). The people are told to consider their ways and build the house; the LORD says He is with them; He promises to shake the heavens and the earth and fill the house with glory; and Zerubbabel is chosen as a signet (Hag. 1:5, 8; 2:4, 7, 9, 23).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to Judah’s governor, Joshua the high priest and the people about the house, His covenant from Egypt, and the shaking of the nations (Hag. 1:1; 2:5–7, 22–23).'))

S(2, "Narrative Flow of Haggai",
  H('Movement 1 — Consider Your Ways (Ch. 1)'),
  P('The people are told to go up to the mountain, bring wood and build the house (Hag. 1:1, 5, 7–8).'),
  H('Movement 2 — The Glory of the Latter House (Ch. 2:1–9)'),
  P('The LORD says, “be strong… for I am with you,” and promises to fill the house with glory (Hag. 2:4–7, 9).'),
  H('Movement 3 — From This Day I Will Bless (Ch. 2:10–19)'),
  P('The people are told to consider, and the LORD says, “from this day will I bless you” (Hag. 2:19).'),
  H('Movement 4 — Zerubbabel the Signet (Ch. 2:20–23)'),
  P('The LORD will shake the heavens and the earth and take Zerubbabel as a signet (Hag. 2:21–23).'))

S(3, "Prophecy-Program Themes in Haggai",
  H('1. Consider Your Ways'),
  P('“Thus saith the LORD of hosts; Consider your ways” (Hag. 1:5).'),
  H('2. Build the House'),
  P('“Go up to the mountain, and bring wood, and build the house; and I will take pleasure in it” (Hag. 1:8).'),
  H('3. I Am With You'),
  P('“Be strong… and work: for I am with you, saith the LORD of hosts” (Hag. 2:4).'),
  H('4. The Covenant From Egypt'),
  P('“According to the word that I covenanted with you when ye came out of Egypt, so my spirit remaineth among you: fear ye not” (Hag. 2:5).'),
  H('5. The Shaking'),
  P('“I will shake all nations, and the desire of all nations shall come: and I will fill this house with glory” (Hag. 2:7).'),
  H('6. Peace in This Place'),
  P('“In this place will I give peace, saith the LORD of hosts” (Hag. 2:9).'),
  H('7. The Signet'),
  P('“will I take thee, O Zerubbabel, my servant… and will make thee as a signet: for I have chosen thee” (Hag. 2:23).'))

S(4, "Christ in Haggai: The Prophetic Trajectory",
  H('1. The Desire of All Nations'),
  P('The words “the desire of all nations shall come” (Hag. 2:7) are reported as written, with no further identification made here.'),
  H('2. The Latter House'),
  P('“The glory of this latter house shall be greater than of the former” (Hag. 2:9).'),
  H('3. The Signet'),
  P('Zerubbabel, the LORD’s servant, is made “as a signet” (Hag. 2:23); the line of Judah’s governor is recorded as written.'))

S(5, "Israel’s Identity in Haggai",
  P("Haggai reinforces Israel’s:"),
  L('Zerubbabel the governor of Judah and Joshua the high priest (Hag. 1:1; 2:4)', 'the covenant made when Israel came out of Egypt (Hag. 2:5)', 'the house to be built and filled with glory (Hag. 2:7, 9)', 'the shaking of the kingdoms of the heathen (Hag. 2:22)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Haggai does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its house, its covenant from Egypt, its shaking of nations and its signet belong exclusively to Israel; its words on putting God first and on His presence are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Haggai", "Program Identity", "Scripture"], [
    ['Zerubbabel and Joshua', '“came the word of the LORD by Haggai the prophet unto Zerubbabel… and to Joshua the son of Josedech, the high priest.”', ISR, 'Hag. 1:1'],
    ['Build the House', '“build the house; and I will take pleasure in it, and I will be glorified, saith the LORD.”', ISR, 'Hag. 1:8'],
    ['The Covenant From Egypt', '“According to the word that I covenanted with you when ye came out of Egypt.”', ISR, 'Hag. 2:5'],
    ['The Shaking', '“I will shake the heavens, and the earth, and the sea, and the dry land.”', ISR, 'Hag. 2:6'],
    ['The House Filled', '“I will fill this house with glory, saith the LORD of hosts.”', ISR, 'Hag. 2:7'],
    ['The Latter House', '“The glory of this latter house shall be greater than of the former.”', ISR, 'Hag. 2:9'],
    ['The Kingdoms Overthrown', '“I will overthrow the throne of kingdoms, and I will destroy the strength of the kingdoms of the heathen.”', ISR, 'Hag. 2:22'],
    ['The Signet', '“will I take thee, O Zerubbabel, my servant, the son of Shealtiel, saith the LORD, and will make thee as a signet.”', ISR, 'Hag. 2:23'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Consider Your Ways', '“Thus saith the LORD of hosts; Consider your ways.”', 'Hag. 1:5'],
    ['Be Strong and Work', '“be strong, all ye people of the land, saith the LORD, and work: for I am with you.”', 'Hag. 2:4'],
    ['His Blessing', '“from this day will I bless you.”', 'Hag. 2:19'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the house, the covenant from Egypt or the signet; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Consider your ways</b> — Put the LORD’s work first (Hag. 1:5).', '<b>Be strong and work</b> — The LORD is with you (Hag. 2:4).', '<b>Receive His blessing</b> — From this day He will bless (Hag. 2:19).'))

S(10, "Teaching Outline for Haggai",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Consider Your Ways (Ch. 1) — Build the house. <i>(Hag. 1:1, 5, 7–8)</i>', 'The Glory of the Latter House (Ch. 2:1–9) — I am with you. <i>(Hag. 2:4–7, 9)</i>', 'From This Day I Will Bless (Ch. 2:10–19) — Consider. <i>(Hag. 2:19)</i>', 'Zerubbabel the Signet (Ch. 2:20–23) — The shaking and the choice. <i>(Hag. 2:21–23)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Haggai, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward putting God first, strength for the work, and trust in His presence without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Haggai simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Haggai stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
