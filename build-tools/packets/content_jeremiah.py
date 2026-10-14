# DRAFT for publisher approval.
BOOK = "Jeremiah"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "Judgment on Judah, the Weeping Prophet, and the New Covenant Promised"
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
  P('Jeremiah records the word of the LORD to the prophet ordained “a prophet unto the nations” (Jer. 1:5) and sent to Judah and Jerusalem. It follows his call, his warnings and laments, the siege and fall of Jerusalem, and the promises of restoration, the Branch of David and the new covenant (Jer. 1:10; 23:5; 30:3; 31:31–34; 33:15).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to the house of Israel and the house of Judah about judgment, exile and a restoration with a new covenant made with them (Jer. 7:23; 30:3; 31:31).'))

S(2, "Narrative Flow of Jeremiah",
  H('Movement 1 — The Call and the Warnings (Chs. 1–25)'),
  P('Jeremiah is called, warns Judah from the temple gate, and speaks of the heart, the potter and the false shepherds (Jer. 1:5, 10; 7:23; 17:9–10; 23:5).'),
  H('Movement 2 — Conflict and Exile (Chs. 26–29)'),
  P('False prophets are answered, and the exiles in Babylon are told to seek the LORD (Jer. 29:11, 13).'),
  H('Movement 3 — The Book of Consolation (Chs. 30–33)'),
  P('The LORD promises to bring again the captivity, to make a new covenant, and to cause the Branch of righteousness to grow up unto David (Jer. 30:3; 31:3, 31–36; 32:37; 33:15, 20–21).'),
  H('Movement 4 — The Fall of Jerusalem (Chs. 34–45)'),
  P('The city falls, and Jeremiah is carried down to Egypt (Jer. 32:17; 34–45).'),
  H('Movement 5 — Oracles on the Nations (Chs. 46–52)'),
  P('The LORD speaks over the nations and against Babylon, and the book closes with the fall of Jerusalem (Jer. 10:10; 46–52).'))

S(3, "Prophecy-Program Themes in Jeremiah",
  H('1. A Prophet to the Nations'),
  P('“Before I formed thee in the belly I knew thee… I ordained thee a prophet unto the nations” (Jer. 1:5).'),
  H('2. Obey and Be His People'),
  P('“Obey my voice, and I will be your God, and ye shall be my people” (Jer. 7:23).'),
  H('3. The Heart'),
  P('“The heart is deceitful above all things, and desperately wicked: who can know it?” (Jer. 17:9).'),
  H('4. The Righteous Branch'),
  P('“I will raise unto David a righteous Branch” (Jer. 23:5).'),
  H('5. The Captivity Returned'),
  P('“I will bring again the captivity of my people Israel and Judah” (Jer. 30:3).'),
  H('6. The New Covenant'),
  P('“I will make a new covenant with the house of Israel, and with the house of Judah” (Jer. 31:31).'),
  H('7. The Covenant That Holds'),
  P('“If those ordinances depart from before me, saith the LORD, then the seed of Israel also shall cease from being a nation before me for ever” (Jer. 31:36).'))

S(4, "Christ in Jeremiah: The Prophetic Trajectory",
  H('1. The Righteous Branch'),
  P('The Branch raised to David is reported as written (Jer. 23:5; 33:15).'),
  H('2. The New Covenant'),
  P('The passage is quoted in the letter to the Hebrews (Jer. 31:31–34; Heb. 8:8–12). It is made with the house of Israel and the house of Judah (Jer. 31:31).'),
  H('3. The Weeping Prophet'),
  P('Jeremiah’s laments over the people are reported as written (Jer. 8:20; 9:1).'))

S(5, "Israel’s Identity in Jeremiah",
  P("Jeremiah reinforces Israel’s:"),
  L('covenant, land and exile of Judah (Jer. 30:3; 32:37)', 'the house of Israel and the house of Judah as the covenant parties (Jer. 31:31)', 'David’s Branch and throne (Jer. 23:5; 33:15, 21)', 'the LORD’s everlasting love for Israel (Jer. 31:3)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Jeremiah does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its covenant with the house of Israel and the house of Judah, the Branch of David and the land belong exclusively to Israel; the Body benefits from the blood on which the new covenant rests without becoming the covenant party.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Jeremiah", "Program Identity", "Scripture"], [
    ['Obey and Be His People', '“I will be your God, and ye shall be my people.”', ISR, 'Jer. 7:23'],
    ['The Righteous Branch', '“I will raise unto David a righteous Branch.”', ISR, 'Jer. 23:5'],
    ['Thoughts of Peace', '“thoughts of peace, and not of evil, to give you an expected end.”', ISR, 'Jer. 29:11'],
    ['The Captivity Returned', '“I will bring again the captivity of my people Israel and Judah.”', ISR, 'Jer. 30:3'],
    ['Everlasting Love', '“I have loved thee with an everlasting love.”', ISR, 'Jer. 31:3'],
    ['The New Covenant', '“I will make a new covenant with the house of Israel, and with the house of Judah.”', ISR, 'Jer. 31:31'],
    ['The Law Within', '“I will put my law in their inward parts.”', ISR, 'Jer. 31:33'],
    ['Israel Remains a Nation', '“the seed of Israel also shall cease from being a nation before me for ever.”', ISR, 'Jer. 31:36'],
    ['The Gathering', '“I will gather them out of all countries.”', ISR, 'Jer. 32:37'],
    ['The Branch of Righteousness', '“cause the Branch of righteousness to grow up unto David.”', ISR, 'Jer. 33:15'],
    ['The Covenant With David', '“my covenant be broken with David my servant.”', ISR, 'Jer. 33:21'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Glorying in the LORD', '“let him that glorieth glory in this, that he understandeth and knoweth me.”', 'Jer. 9:24'],
    ['The True God', '“the LORD is the true God, he is the living God, and an everlasting king.”', 'Jer. 10:10'],
    ['The Heart', '“The heart is deceitful above all things, and desperately wicked: who can know it?”', 'Jer. 17:9'],
    ['He Searches the Heart', '“I the LORD search the heart, I try the reins.”', 'Jer. 17:10'],
    ['Nothing Too Hard', '“there is nothing too hard for thee.”', 'Jer. 32:17'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s new covenant, land or Davidic kingdom; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Glory only in knowing Him</b> — Understanding and knowing the LORD (Jer. 9:24).', '<b>Worship the living God</b> — The true God and everlasting king (Jer. 10:10).', '<b>Distrust the heart</b> — It is deceitful above all things (Jer. 17:9).', '<b>Welcome His searching</b> — He tries the reins (Jer. 17:10).', '<b>Trust His power</b> — Nothing is too hard for Him (Jer. 32:17).'))

S(10, "Teaching Outline for Jeremiah",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Call and the Warnings (Chs. 1–25) — Sent to Judah. <i>(Jer. 1:5; 7:23; 17:9–10; 23:5)</i>', 'Conflict and Exile (Chs. 26–29) — The word to the exiles. <i>(Jer. 29:11)</i>', 'The Book of Consolation (Chs. 30–33) — Return, Branch and new covenant. <i>(Jer. 30:3; 31:31–36; 33:15)</i>', 'The Fall of Jerusalem (Chs. 34–45) — Nothing too hard. <i>(Jer. 32:17)</i>', 'Oracles on the Nations (Chs. 46–52) — The true God. <i>(Jer. 10:10)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Jeremiah, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward sober self-examination, trust, and reverence for the LORD without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Jeremiah simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Jeremiah stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
