# DRAFT for publisher approval.
BOOK = "1 Kings"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Solomon’s Temple, the Divided Kingdom, and the Prophet Elijah"
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
  P('1 Kings begins with David’s last days and Solomon’s throne. It records Solomon’s request for an understanding heart, the building and dedication of the temple, the LORD’s warning to Solomon, the division of the kingdom, the golden calves, and Elijah’s ministry against Baal worship (1 Kgs. 3:9; 6:38; 8:10–11; 9:3–5; 11:11; 12:16, 28; 18:21).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD dwells with Israel in the temple and Israel’s kings answer for the covenant (1 Kgs. 8:56; 9:3–5).'))

S(2, "Narrative Flow of 1 Kings",
  H('Movement 1 — Solomon’s Throne and Wisdom (Chs. 1–4)'),
  P('David charges Solomon to keep the law of Moses, and Solomon asks, “Give therefore thy servant an understanding heart to judge thy people” (1 Kgs. 2:3; 3:9, 12).'),
  H('Movement 2 — The Temple (Chs. 5–8)'),
  P('The house is finished in seven years, the glory of the LORD fills it, and Solomon blesses the LORD for His promise to Israel (1 Kgs. 6:38; 8:10–11, 23, 27, 56, 60).'),
  H('Movement 3 — Warning and Division (Chs. 9–12)'),
  P('The LORD answers Solomon’s prayer, sets conditions on the throne, rends the kingdom after Solomon’s idolatry, and Israel departs from David’s house (1 Kgs. 9:3–5; 11:4, 11, 36; 12:16, 28).'),
  H('Movement 4 — Elijah and Ahab (Chs. 13–22)'),
  P('Elijah speaks to Ahab, calls Israel to choose between the LORD and Baal, and hears a still small voice at Horeb (1 Kgs. 17:1, 24; 18:21, 39; 19:12, 18).'))

S(3, "Prophecy-Program Themes in 1 Kings",
  H('1. The Temple Filled with Glory'),
  P('“The glory of the LORD had filled the house of the LORD” (1 Kgs. 8:11).'),
  H('2. The Promise Kept'),
  P('“There hath not failed one word of all his good promise, which he promised by the hand of Moses his servant” (1 Kgs. 8:56).'),
  H('3. The Throne Conditioned'),
  P('“Then I will establish the throne of thy kingdom upon Israel for ever, as I promised to David thy father” (1 Kgs. 9:5).'),
  H('4. The Kingdom Rent'),
  P('“I will surely rend the kingdom from thee, and will give it to thy servant” (1 Kgs. 11:11).'),
  H('5. A Light for David'),
  P('“That David my servant may have a light alway before me in Jerusalem, the city which I have chosen me to put my name there” (1 Kgs. 11:36).'),
  H('6. The LORD or Baal'),
  P('“If the LORD be God, follow him: but if Baal, then follow him” (1 Kgs. 18:21).'))

S(4, "Christ in 1 Kings: The Prophetic Trajectory",
  H('1. The Son of David'),
  P('Solomon builds the house and the LORD promises the throne to David’s line (1 Kgs. 6:38; 9:5), within Israel’s kingdom hope.'),
  H('2. The Temple and the Glory'),
  P('The glory of the LORD fills the house (1 Kgs. 8:11); the book reports this as written.'),
  H('3. The Remnant'),
  P('The LORD says, “I have left me seven thousand in Israel” who have not bowed to Baal (1 Kgs. 19:18).'))

S(5, "Israel’s Identity in 1 Kings",
  P("1 Kings reinforces Israel’s:"),
  L('temple and glory of the LORD (1 Kgs. 8:10–11)', 'promise to David’s throne (1 Kgs. 9:5)', 'the divided kingdom (1 Kgs. 12:16)', 'prophets sent to Israel (1 Kgs. 17:1)', 'a remnant that has not bowed to Baal (1 Kgs. 19:18)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("1 Kings does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its temple, throne, divided kingdom and prophetic ministry belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in 1 Kings", "Program Identity", "Scripture"], [
    ['The Law of Moses Kept', '“as it is written in the law of Moses.”', ISR, '1 Kgs. 2:3'],
    ['The Temple Finished', '“in the eleventh year… was the house finished throughout all the parts thereof.”', ISR, '1 Kgs. 6:38'],
    ['The Glory Fills the House', '“the glory of the LORD had filled the house of the LORD.”', ISR, '1 Kgs. 8:11'],
    ['The Promise Not Failed', '“there hath not failed one word of all his good promise.”', ISR, '1 Kgs. 8:56'],
    ['The Throne Over Israel', '“I will establish the throne of thy kingdom upon Israel for ever.”', ISR, '1 Kgs. 9:5'],
    ['The Kingdom Rent', '“I will surely rend the kingdom from thee.”', ISR, '1 Kgs. 11:11'],
    ['A Light for David', '“that David my servant may have a light alway before me in Jerusalem.”', ISR, '1 Kgs. 11:36'],
    ['The Calves of Gold', '“made two calves of gold.”', ISR, '1 Kgs. 12:28'],
    ['The Seven Thousand', '“I have left me seven thousand in Israel.”', ISR, '1 Kgs. 19:18'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Understanding for Judging', '“Give therefore thy servant an understanding heart to judge thy people.”', '1 Kgs. 3:9'],
    ['No God Like Him', '“LORD God of Israel, there is no God like thee, in heaven above, or on earth beneath.”', '1 Kgs. 8:23'],
    ['The Heavens Cannot Contain Him', '“the heaven and heaven of heavens cannot contain thee.”', '1 Kgs. 8:27'],
    ['That All May Know', '“That all the people of the earth may know that the LORD is God, and that there is none else.”', '1 Kgs. 8:60'],
    ['The Still Small Voice', '“after the fire a still small voice.”', '1 Kgs. 19:12'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s temple, throne or divided kingdom; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Ask God for wisdom</b> — An understanding heart (1 Kgs. 3:9).', '<b>Confess that there is no God like Him</b> (1 Kgs. 8:23).', '<b>Remember He cannot be contained</b> (1 Kgs. 8:27).', '<b>Wish all peoples to know the LORD</b> (1 Kgs. 8:60).', '<b>Listen for His voice</b> — A still small voice (1 Kgs. 19:12).'))

S(10, "Teaching Outline for 1 Kings",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Solomon’s Throne (Chs. 1–4) — Wisdom asked. <i>(1 Kgs. 2:3; 3:9, 12)</i>', 'The Temple (Chs. 5–8) — The glory fills the house. <i>(1 Kgs. 6:38; 8:10–11, 56)</i>', 'Warning and Division (Chs. 9–12) — The kingdom rent. <i>(1 Kgs. 9:5; 11:11, 36; 12:16, 28)</i>', 'Elijah (Chs. 13–22) — The LORD or Baal. <i>(1 Kgs. 18:21, 39; 19:12, 18)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 Kings, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward wisdom, faithfulness, and trust without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 Kings simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 1 Kings stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
