# DRAFT for publisher approval.
BOOK = "Nahum"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Burden of Nineveh, and the LORD Who Knows Those Who Trust Him"
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
  P('Nahum is “the burden of Nineveh. The book of the vision of Nahum the Elkoshite” (Nah. 1:1). It describes the LORD slow to anger and great in power, His way in the whirlwind, His goodness to those who trust in Him, the fall of Nineveh, and good tidings for Judah (Nah. 1:3, 7, 15; 3:7, 19).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks of Nineveh’s fall and of Judah and Jacob restored (Nah. 1:15; 2:2). Its words on the LORD’s character are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Nahum",
  H('Movement 1 — The LORD’s Character and Judgment (Ch. 1)'),
  P('The LORD is slow to anger and good to those who trust Him; good tidings come to Judah (Nah. 1:3, 7, 15).'),
  H('Movement 2 — The Siege of Nineveh (Ch. 2)'),
  P('The LORD turns away the excellency of Jacob, and Nineveh is emptied (Nah. 2:2).'),
  H('Movement 3 — Woe to the Bloody City (Ch. 3)'),
  P('Nineveh is laid waste, and her wound has no healing (Nah. 3:7, 19).'))

S(3, "Prophecy-Program Themes in Nahum",
  H('1. A Burden Against Nineveh'),
  P('“The burden of Nineveh” (Nah. 1:1).'),
  H('2. Slow to Anger'),
  P('“The LORD is slow to anger, and great in power, and will not at all acquit the wicked” (Nah. 1:3).'),
  H('3. A Strong Hold'),
  P('“The LORD is good, a strong hold in the day of trouble; and he knoweth them that trust in him” (Nah. 1:7).'),
  H('4. Good Tidings for Judah'),
  P('“Behold upon the mountains the feet of him that bringeth good tidings, that publisheth peace!” (Nah. 1:15).'),
  H('5. The Excellency of Jacob'),
  P('“The LORD hath turned away the excellency of Jacob, as the excellency of Israel” (Nah. 2:2).'),
  H('6. No Healing'),
  P('“There is no healing of thy bruise; thy wound is grievous” (Nah. 3:19).'))

S(4, "Christ in Nahum: The Prophetic Trajectory",
  H('1. The Bearer of Good Tidings'),
  P('The feet of him that publisheth peace (Nah. 1:15) are reported as written; Isaiah 52:7 has similar words and is read in its own chapter.'),
  H('2. The LORD a Strong Hold'),
  P('The LORD is “a strong hold in the day of trouble” (Nah. 1:7).'),
  H('3. Judgment Without Acquittal'),
  P('The LORD “will not at all acquit the wicked” (Nah. 1:3).'))

S(5, "Israel’s Identity in Nahum",
  P("Nahum reinforces Israel’s:"),
  L('Judah called to keep her solemn feasts and perform her vows (Nah. 1:15)', 'Jacob and Israel, whose excellency the LORD turns away and restores (Nah. 2:2)', 'the LORD’s judgment on Nineveh for the sake of His people (Nah. 1:1, 15)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Nahum does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its judgment on Nineveh, its good tidings to Judah and its word on Jacob belong exclusively to Israel; its words on the LORD’s goodness and justice are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Nahum", "Program Identity", "Scripture"], [
    ['The Burden of Nineveh', '“The burden of Nineveh.”', ISR, 'Nah. 1:1'],
    ['Good Tidings to Judah', '“O Judah, keep thy solemn feasts, perform thy vows.”', ISR, 'Nah. 1:15'],
    ['The Excellency of Jacob', '“the LORD hath turned away the excellency of Jacob, as the excellency of Israel.”', ISR, 'Nah. 2:2'],
    ['Nineveh Laid Waste', '“Nineveh is laid waste: who will bemoan her?”', ISR, 'Nah. 3:7'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Slow to Anger', '“The LORD is slow to anger, and great in power, and will not at all acquit the wicked.”', 'Nah. 1:3'],
    ['A Strong Hold', '“The LORD is good, a strong hold in the day of trouble.”', 'Nah. 1:7'],
    ['Knows Those Who Trust', '“he knoweth them that trust in him.”', 'Nah. 1:7'],
    ['Wickedness Judged', '“upon whom hath not thy wickedness passed continually?”', 'Nah. 3:19'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s Judah, Jacob or Nineveh’s fall; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Trust Him in trouble</b> — He is a strong hold (Nah. 1:7).', '<b>Know that He knows</b> — He knoweth them that trust (Nah. 1:7).', '<b>Remember His patience and justice</b> — Slow to anger, and He will not acquit the wicked (Nah. 1:3).'))

S(10, "Teaching Outline for Nahum",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The LORD’s Character (Ch. 1) — Slow to anger, a strong hold. <i>(Nah. 1:3, 7, 15)</i>', 'The Siege of Nineveh (Ch. 2) — Jacob’s excellency. <i>(Nah. 2:2)</i>', 'Woe to the Bloody City (Ch. 3) — Nineveh laid waste. <i>(Nah. 3:7, 19)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Nahum, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward trust in the LORD, patience with His justice, and good tidings of peace without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Nahum simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Nahum stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
