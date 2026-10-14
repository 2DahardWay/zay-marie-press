# DRAFT for publisher approval.
BOOK = "Lamentations"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Fallen City, the Mercies of the LORD, and the Prayer for Return"
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
  P('Lamentations is five laments over Jerusalem after its fall. The city “sit solitary, that was full of people” (Lam. 1:1), the LORD’s anger is described, and in the middle of the book the speaker recalls, “It is of the LORD’s mercies that we are not consumed” (Lam. 3:22). The book closes with a prayer, “Turn thou us unto thee, O LORD” (Lam. 5:21).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program: it mourns Jerusalem, its sanctuary and its people after the exile and prays for their turning (Lam. 1:1; 4:1; 5:1, 21). Its words of mercy and hope are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Lamentations",
  H('Movement 1 — Jerusalem Sits Solitary (Ch. 1)'),
  P('The city is a widow and weeps, and there is none to comfort her (Lam. 1:1).'),
  H('Movement 2 — The LORD’s Anger (Ch. 2)'),
  P('The LORD has cast down the daughter of Zion, and the prophet mourns.'),
  H('Movement 3 — Hope in the LORD’s Mercies (Ch. 3)'),
  P('In the midst of affliction the speaker recalls that the LORD’s mercies are new every morning (Lam. 3:22–26, 32–33, 40).'),
  H('Movement 4 — The Sanctuary Stones (Ch. 4)'),
  P('The gold is dimmed and the stones of the sanctuary are poured out (Lam. 4:1).'),
  H('Movement 5 — Remember and Renew (Ch. 5)'),
  P('The people pray for the LORD’s remembrance and for renewal (Lam. 5:1, 19, 21).'))

S(3, "Prophecy-Program Themes in Lamentations",
  H('1. The Lonely City'),
  P('“How doth the city sit solitary, that was full of people!” (Lam. 1:1).'),
  H('2. Mercies Not Consumed'),
  P('“It is of the LORD’s mercies that we are not consumed, because his compassions fail not” (Lam. 3:22).'),
  H('3. New Every Morning'),
  P('“They are new every morning: great is thy faithfulness” (Lam. 3:23).'),
  H('4. The LORD as Portion'),
  P('“The LORD is my portion, saith my soul; therefore will I hope in him” (Lam. 3:24).'),
  H('5. Quiet Waiting'),
  P('“It is good that a man should both hope and quietly wait for the salvation of the LORD” (Lam. 3:26).'),
  H('6. Search and Return'),
  P('“Let us search and try our ways, and turn again to the LORD” (Lam. 3:40).'),
  H('7. Renewal as of Old'),
  P('“Turn thou us unto thee, O LORD, and we shall be turned; renew our days as of old” (Lam. 5:21).'))

S(4, "Christ in Lamentations: The Prophetic Trajectory",
  H('1. The Weeping Prophet'),
  P('Lamentations is placed after Jeremiah in the English Bible and takes up the fall of Jerusalem; the book names no author and is reported as written.'),
  H('2. The Man of Sorrows'),
  P('The book speaks of affliction borne; the New Testament does not quote it, and no passage is built on it here.'),
  H('3. Mercy in Judgment'),
  P('The LORD’s compassion stands beside His anger in the same chapters (Lam. 3:32–33).'))

S(5, "Israel’s Identity in Lamentations",
  P("Lamentations reinforces Israel’s:"),
  L('Jerusalem and its people as the subject of the laments (Lam. 1:1; 5:1)', 'the sanctuary and its stones (Lam. 4:1)', 'the prayer for the LORD’s turning of His people (Lam. 5:21)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Lamentations does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its laments over Jerusalem, the sanctuary and Israel’s exile belong exclusively to Israel; its words on the LORD’s mercy are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Lamentations", "Program Identity", "Scripture"], [
    ['The City Solitary', '“How doth the city sit solitary, that was full of people!”', ISR, 'Lam. 1:1'],
    ['The Sanctuary Stones', '“the stones of the sanctuary are poured out in the top of every street.”', ISR, 'Lam. 4:1'],
    ['Remember Us', '“Remember, O LORD, what is come upon us: consider, and behold our reproach.”', ISR, 'Lam. 5:1'],
    ['Renew Our Days', '“Turn thou us unto thee, O LORD, and we shall be turned; renew our days as of old.”', ISR, 'Lam. 5:21'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Mercies', '“It is of the LORD’s mercies that we are not consumed, because his compassions fail not.”', 'Lam. 3:22'],
    ['Faithfulness', '“They are new every morning: great is thy faithfulness.”', 'Lam. 3:23'],
    ['The LORD My Portion', '“The LORD is my portion, saith my soul; therefore will I hope in him.”', 'Lam. 3:24'],
    ['The LORD Is Good', '“The LORD is good unto them that wait for him, to the soul that seeketh him.”', 'Lam. 3:25'],
    ['Quiet Waiting', '“It is good that a man should both hope and quietly wait for the salvation of the LORD.”', 'Lam. 3:26'],
    ['Compassion After Grief', '“though he cause grief, yet will he have compassion according to the multitude of his mercies.”', 'Lam. 3:32'],
    ['He Afflicts Not Willingly', '“he doth not afflict willingly nor grieve the children of men.”', 'Lam. 3:33'],
    ['Search and Return', '“Let us search and try our ways, and turn again to the LORD.”', 'Lam. 3:40'],
    ['The LORD Remains', '“Thou, O LORD, remainest for ever; thy throne from generation to generation.”', 'Lam. 5:19'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s laments over Jerusalem or its sanctuary; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Lament honestly</b> — Bring the grief to the LORD (Lam. 5:1).', '<b>Rest in His mercies</b> — They are not consumed (Lam. 3:22).', '<b>Count on His faithfulness</b> — New every morning (Lam. 3:23).', '<b>Hope in Him as portion</b> — The LORD is my portion (Lam. 3:24).', '<b>Wait quietly</b> — It is good to hope and wait (Lam. 3:26).', '<b>Examine your ways</b> — Search, try and turn again (Lam. 3:40).', '<b>Remember He remains</b> — His throne endures (Lam. 5:19).'))

S(10, "Teaching Outline for Lamentations",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Jerusalem Sits Solitary (Ch. 1) — The city mourned. <i>(Lam. 1:1)</i>', 'The LORD’s Anger (Ch. 2) — The daughter of Zion cast down.', 'Hope in the LORD’s Mercies (Ch. 3) — New every morning. <i>(Lam. 3:22–26, 32–33, 40)</i>', 'The Sanctuary Stones (Ch. 4) — The dim gold. <i>(Lam. 4:1)</i>', 'Remember and Renew (Ch. 5) — The closing prayer. <i>(Lam. 5:1, 19, 21)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Lamentations, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward honest lament, patience, and hope in the LORD’s mercies without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Lamentations simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Lamentations stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
