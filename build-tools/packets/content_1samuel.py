# DRAFT for publisher approval.
BOOK = "1 Samuel"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Samuel, the Demand for a King, Saul’s Rejection, and David Anointed"
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
  P('1 Samuel moves from Hannah’s prayer and the birth of Samuel to the people’s demand for a king. It records the anointing of Saul, his rejection for disobedience, the anointing of David, David’s victory over Goliath, and David’s flight from Saul (1 Sam. 1:20; 8:5; 10:1; 13:14; 15:23; 16:13; 17:45).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD is Israel’s King and the monarchy is set up within Israel’s covenant life in the land (1 Sam. 8:7; 12:22).'))

S(2, "Narrative Flow of 1 Samuel",
  H('Movement 1 — Hannah and Samuel (Chs. 1–3)'),
  P('Hannah vows and bears Samuel, her song declares that none is holy as the LORD, and the LORD calls the child Samuel (1 Sam. 1:11, 20; 2:2; 3:1, 10, 19).'),
  H('Movement 2 — The Demand for a King (Chs. 4–8)'),
  P('Israel asks, “make us a king to judge us like all the nations,” and the LORD says they have rejected Him (1 Sam. 8:5, 7).'),
  H('Movement 3 — Saul Anointed and Rejected (Chs. 9–15)'),
  P('Samuel anoints Saul, Saul is chosen, and the LORD later rejects him because he did not keep His commandment (1 Sam. 9:16; 10:1, 24; 13:14; 15:22–23).'),
  H('Movement 4 — David (Chs. 16–31)'),
  P('Samuel anoints David, the Spirit of the LORD comes upon him, David defeats Goliath, and he spares Saul as the LORD’s anointed (1 Sam. 16:13; 17:45, 47; 24:6).'))

S(3, "Prophecy-Program Themes in 1 Samuel",
  H('1. The LORD Is Unlike Any'),
  P('“There is none holy as the LORD: for there is none beside thee: neither is there any rock like our God” (1 Sam. 2:2).'),
  H('2. A King Demanded'),
  P('“Behold, thou art old, and thy sons walk not in thy ways: now make us a king to judge us like all the nations” (1 Sam. 8:5).'),
  H('3. The LORD Rejected as King'),
  P('“They have not rejected thee, but they have rejected me, that I should not reign over them” (1 Sam. 8:7).'),
  H('4. Obedience Over Sacrifice'),
  P('“To obey is better than sacrifice, and to hearken than the fat of rams” (1 Sam. 15:22).'),
  H('5. The LORD’s Anointed'),
  P('“The LORD forbid that I should do this thing unto my master, the LORD’s anointed” (1 Sam. 24:6).'),
  H('6. David Anointed'),
  P('“The Spirit of the LORD came upon David from that day forward” (1 Sam. 16:13).'))

S(4, "Christ in 1 Samuel: The Prophetic Trajectory",
  H('1. The Anointed One'),
  P('Saul and David are each called the LORD’s anointed (1 Sam. 10:1; 24:6), and the word points forward in Israel’s story to the King who is to come.'),
  H('2. The Man After His Own Heart'),
  P('The LORD “hath sought him a man after his own heart” (1 Sam. 13:14); the line of David leads to the promised King.'),
  H('3. The Battle Is the LORD’s'),
  P('“The battle is the LORD’s” (1 Sam. 17:47) is spoken by David to Goliath’s side.'))

S(5, "Israel’s Identity in 1 Samuel",
  P("1 Samuel reinforces Israel’s:"),
  L('covenant life in the land under the LORD as King (1 Sam. 8:7)', 'the monarchy, first Saul and then David (1 Sam. 10:1; 16:13)', 'the anointed king (1 Sam. 24:6)', 'the promise that the LORD will not forsake His people (1 Sam. 12:22)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("1 Samuel does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its kingship, anointing, priesthood and battles belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in 1 Samuel", "Program Identity", "Scripture"], [
    ['Samuel Asked of the LORD', '“Because I have asked him of the LORD.”', ISR, '1 Sam. 1:20'],
    ['Israel Asks for a King', '“now make us a king to judge us like all the nations.”', ISR, '1 Sam. 8:5'],
    ['Saul Anointed', '“Is it not because the LORD hath anointed thee to be captain over his inheritance?”', ISR, '1 Sam. 10:1'],
    ['The LORD Will Not Forsake His People', '“the LORD will not forsake his people for his great name’s sake.”', ISR, '1 Sam. 12:22'],
    ['A Man After His Own Heart', '“the LORD hath sought him a man after his own heart.”', ISR, '1 Sam. 13:14'],
    ['David Anointed', '“Samuel took the horn of oil, and anointed him in the midst of his brethren.”', ISR, '1 Sam. 16:13'],
    ['The LORD’s Anointed', '“seeing he is the anointed of the LORD.”', ISR, '1 Sam. 24:6'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The LORD Is Holy', '“There is none holy as the LORD.”', '1 Sam. 2:2'],
    ['Life and Death Are His', '“The LORD killeth, and maketh alive.”', '1 Sam. 2:6'],
    ['Obedience Over Offering', '“to obey is better than sacrifice.”', '1 Sam. 15:22'],
    ['The Battle Is the LORD’s', '“the LORD saveth not with sword and spear: for the battle is the LORD’s.”', '1 Sam. 17:47'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s kingship, anointing or covenant life in the land; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Honour the holiness of God</b> — None is holy as the LORD (1 Sam. 2:2).', '<b>Remember that life is in His hand</b> — He killeth and maketh alive (1 Sam. 2:6).', '<b>Choose obedience</b> — It is better than sacrifice (1 Sam. 15:22).', '<b>Trust Him in the fight</b> — The battle is the LORD’s (1 Sam. 17:47).'))

S(10, "Teaching Outline for 1 Samuel",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Hannah and Samuel (Chs. 1–3) — The child who hears. <i>(1 Sam. 1:20; 2:2; 3:10)</i>', 'The Demand for a King (Chs. 4–8) — Israel rejects the LORD as King. <i>(1 Sam. 8:5, 7)</i>', 'Saul (Chs. 9–15) — Anointed and rejected. <i>(1 Sam. 10:1; 13:14; 15:22–23)</i>', 'David (Chs. 16–31) — Anointed and tested. <i>(1 Sam. 16:13; 17:45, 47; 24:6)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 Samuel, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward trust, obedience, and humility without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 Samuel simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 1 Samuel stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
