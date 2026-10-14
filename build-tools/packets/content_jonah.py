# DRAFT for publisher approval.
BOOK = "Jonah"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Prophet’s Flight, Nineveh’s Repentance, and the Mercy of God"
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
  P('Jonah opens with “the word of the LORD” coming to “Jonah the son of Amittai,” who is told to arise, go to Nineveh and cry against it (Jonah 1:1–2). The book follows his flight toward the sea, the great fish prepared by the LORD, his prayer out of the fish’s belly, the preaching in Nineveh, the city’s turning, and the LORD’s closing question to a prophet who was displeased (Jonah 1:17; 2:1; 3:4–10; 4:1, 11).'),
  BOX("Program Identity:", 'Jonah is the book of a prophet of the LORD sent from Israel’s side of the sea to a Gentile city, and its place is Israel’s Prophecy Program: Jonah speaks of himself as a Hebrew and looks toward the LORD’s holy temple (Jonah 1:9; 2:4). Its words on mercy and repentance are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Jonah",
  H('Movement 1 — The Flight (Ch. 1)'),
  P('The word of the LORD sends Jonah to Nineveh, Jonah goes down toward the sea, the LORD sends out a great wind, and the lot falls upon Jonah (Jonah 1:1–4, 7, 15).'),
  H('Movement 2 — The Prayer from the Fish (Ch. 2)'),
  P('The LORD prepares a great fish, and Jonah prays to the LORD his God out of the fish’s belly (Jonah 1:17; 2:1, 4, 6).'),
  H('Movement 3 — Nineveh Hears (Ch. 3)'),
  P('The word of the LORD comes the second time, Jonah cries that Nineveh shall be overthrown, and the people believe God and turn from their evil way. The book reports what they are said to have believed and what followed, as written (Jonah 3:1–5, 8–10).'),
  H('Movement 4 — The Question (Ch. 4)'),
  P('Jonah is displeased, the LORD God prepares a gourd and a worm and a vehement east wind, and the book ends with the LORD’s question about sparing Nineveh (Jonah 4:1, 6–9, 11).'))

S(3, "Prophecy-Program Themes in Jonah",
  H('1. The Word of the LORD Comes'),
  P('The book begins with the word of the LORD coming to a named prophet, not with the prophet’s own plan (Jonah 1:1; 3:1).'),
  H('2. The LORD Prepares'),
  P('The LORD sends the wind, prepares the fish, and prepares the gourd, the worm and the east wind (Jonah 1:4, 17; 4:6–8).'),
  H('3. Nineveh Believed God'),
  P('“So the people of Nineveh believed God” is reported with the fast, the sackcloth and the turning from the evil way (Jonah 3:5, 8).'),
  H('4. God Repented of the Evil'),
  P('“God saw their works, that they turned from their evil way; and God repented of the evil” (Jonah 3:10).'),
  H('5. A Question Left Standing'),
  P('“Should not I spare Nineveh, that great city” is the last word of the book, and Jonah’s answer is not recorded (Jonah 4:11).'))

S(4, "Christ in Jonah: The Prophetic Trajectory",
  H('1. The Prophet Who Went Down and Was Brought Up'),
  P('Jonah’s descent into the sea and his life brought up from corruption are reported as written in his prayer (Jonah 2:5–6).'),
  H('2. The Sign of Jonah'),
  P('The book does not itself mention a sign; the Lord’s later words about Jonah are read in their own chapters, not here.'))

S(5, "Israel’s Identity in Jonah",
  P("Jonah reinforces Israel’s:"),
  L('the word of the LORD to a named prophet of Israel, Jonah the son of Amittai (Jonah 1:1)', 'a prophet who calls himself a Hebrew (Jonah 1:9)', 'the LORD’s holy temple as the place toward which Jonah looks (Jonah 2:4)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Jonah does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its prophet, its Hebrew confession and its look toward the holy temple belong to Israel’s program; its words on mercy, repentance and compassion are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Jonah", "Program Identity", "Scripture"], [
    ['The Word to a Prophet', '“Now the word of the LORD came unto Jonah the son of Amittai.”', ISR, 'Jonah 1:1'],
    ['Sent to Nineveh', '“Arise, go to Nineveh, that great city, and cry against it.”', ISR, 'Jonah 1:2'],
    ['Toward the Holy Temple', '“yet I will look again toward thy holy temple.”', ISR, 'Jonah 2:4'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Honest Confession', '“for I know that for my sake this great tempest is upon you.”', 'Jonah 1:12'],
    ['Called to Pray', '“arise, call upon thy God.”', 'Jonah 1:6'],
    ['Forsaking Mercy', '“They that observe lying vanities forsake their own mercy.”', 'Jonah 2:8'],
    ['Turning from Evil', '“let them turn every one from his evil way, and from the violence that is in their hands.”', 'Jonah 3:8'],
    ['God Repented of the Evil', '“God saw their works, that they turned from their evil way; and God repented of the evil.”', 'Jonah 3:10'],
    ['Sparing a City', '“should not I spare Nineveh, that great city.”', 'Jonah 4:11'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s Israel’s covenant calling, Hebrew identity or temple; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Confess honestly</b> — Own the cause of the trouble (Jonah 1:12).', '<b>Call upon God</b> — Arise, call upon thy God (Jonah 1:6).', '<b>Turn from evil</b> — From the evil way and the violence in the hands (Jonah 3:8).', '<b>Hold to mercy</b> — Do not forsake it for lying vanities (Jonah 2:8).', '<b>Weigh your anger</b> — Hear the LORD’s question about the city (Jonah 4:11).'))

S(10, "Teaching Outline for Jonah",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Flight (Ch. 1) — The word of the LORD and the lot. <i>(Jonah 1:1–2, 6, 12, 15)</i>', 'The Prayer from the Fish (Ch. 2) — Toward the holy temple. <i>(Jonah 2:1, 4, 6, 8)</i>', 'Nineveh Hears (Ch. 3) — They believed God and turned. <i>(Jonah 3:1–2, 5, 8, 10)</i>', 'The Question (Ch. 4) — Should not I spare. <i>(Jonah 4:1, 6–9, 11)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Jonah, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward mercy, repentance, and compassion toward others without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Jonah simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Jonah stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
