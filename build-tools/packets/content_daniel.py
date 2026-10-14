# DRAFT for publisher approval.
BOOK = "Daniel"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "Kingdoms of the Earth, Seventy Weeks, and the Kingdom of the Most High"
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
  P('Daniel opens with captives of Judah in Babylon, among them Daniel, who “purposed in his heart that he would not defile himself” (Dan. 1:8). It tells of the dream of the image, the fiery furnace, the king’s humbling, the writing on the wall, the lions’ den, and then of visions of beasts, the Son of man, seventy weeks, and the time of the end (Dan. 2:44; 3:17; 4:35; 5:27; 6:26; 7:13–14; 9:24–27; 12:1–4).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program: the visions concern “thy people” and “thy holy city,” and the kingdom of the most High is given to the saints (Dan. 7:18; 9:24; 12:1). Its words on God’s rule over every kingdom are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Daniel",
  H('Movement 1 — Captives in Babylon (Chs. 1–2)'),
  P('Daniel and his friends are taken into the king’s court, and the dream of the image is made known (Dan. 1:8, 17; 2:20–21, 44).'),
  H('Movement 2 — Faithful Under Pressure (Chs. 3–6)'),
  P('The three friends and Daniel stand in the furnace and in the den, and the kings confess the living God (Dan. 3:17–18; 4:35, 37; 5:27; 6:26).'),
  H('Movement 3 — Visions of the Beasts and the Son of Man (Chs. 7–8)'),
  P('Beasts rise from the sea, one like the Son of man receives a kingdom, and the saints possess it (Dan. 7:13–14, 18, 25, 27; 8:14).'),
  H('Movement 4 — Prayer and the Seventy Weeks (Ch. 9)'),
  P('Daniel confesses and prays for the city, and Gabriel gives the seventy weeks (Dan. 9:3, 19, 24–27).'),
  H('Movement 5 — The Last Vision (Chs. 10–12)'),
  P('The message comes by the prince Michael’s help, the time of trouble is described, and many that sleep shall awake (Dan. 10:13, 21; 11:32; 12:1–4, 9, 13).'))

S(3, "Prophecy-Program Themes in Daniel",
  H('1. The God Who Changes Times'),
  P('“He changeth the times and the seasons: he removeth kings, and setteth up kings” (Dan. 2:21).'),
  H('2. A Kingdom Never Destroyed'),
  P('“The God of heaven set up a kingdom, which shall never be destroyed” (Dan. 2:44).'),
  H('3. The Most High Rules'),
  P('“The most High ruleth in the kingdom of men” (Dan. 4:17).'),
  H('4. One Like the Son of Man'),
  P('“One like the Son of man came with the clouds of heaven, and came to the Ancient of days” (Dan. 7:13).'),
  H('5. The Saints Possess the Kingdom'),
  P('“The saints of the most High shall take the kingdom, and possess the kingdom for ever” (Dan. 7:18).'),
  H('6. The Seventy Weeks'),
  P('“Seventy weeks are determined upon thy people and upon thy holy city” (Dan. 9:24).'),
  H('7. Many Shall Awake'),
  P('“Many of them that sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt” (Dan. 12:2).'))

S(4, "Christ in Daniel: The Prophetic Trajectory",
  H('1. The Son of Man'),
  P('The vision of one like the Son of man receiving dominion is reported as written (Dan. 7:13–14); the Lord uses the title before the council (Matt. 26:64).'),
  H('2. Messiah the Prince'),
  P('“Unto the Messiah the Prince shall be seven weeks, and threescore and two weeks” and “shall Messiah be cut off, but not for himself” are reported as written (Dan. 9:25–26).'),
  H('3. The Kingdom Without End'),
  P('The kingdom the God of heaven sets up “shall never be destroyed” (Dan. 2:44), and the Son of man’s “dominion is an everlasting dominion” (Dan. 7:14).'))

S(5, "Israel’s Identity in Daniel",
  P("Daniel reinforces Israel’s:"),
  L('the saints of the most High and the kingdom given to them (Dan. 7:18, 27)', '“thy people” and “thy holy city” in the seventy weeks (Dan. 9:24)', 'Michael as the prince who stands for the children of Daniel’s people (Dan. 12:1)', 'the resurrection of many of Daniel’s people (Dan. 12:2)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Daniel does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its kingdom, seventy weeks, covenant and resurrection are given to Daniel’s people and the holy city and belong exclusively to Israel; its words on God’s rule over every nation are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Daniel", "Program Identity", "Scripture"], [
    ['The Kingdom Set Up', '“the God of heaven set up a kingdom, which shall never be destroyed.”', ISR, 'Dan. 2:44'],
    ['The Son of Man’s Dominion', '“there was given him dominion, and glory, and a kingdom.”', ISR, 'Dan. 7:14'],
    ['The Saints’ Kingdom', '“the saints of the most High shall take the kingdom, and possess the kingdom for ever.”', ISR, 'Dan. 7:18'],
    ['The Kingdom Given', '“the kingdom and dominion, and the greatness of the kingdom under the whole heaven, shall be given to the people of the saints of the most High.”', ISR, 'Dan. 7:27'],
    ['The Seventy Weeks', '“Seventy weeks are determined upon thy people and upon thy holy city.”', ISR, 'Dan. 9:24'],
    ['Messiah the Prince', '“unto the Messiah the Prince shall be seven weeks, and threescore and two weeks.”', ISR, 'Dan. 9:25'],
    ['Messiah Cut Off', '“shall Messiah be cut off, but not for himself.”', ISR, 'Dan. 9:26'],
    ['The Covenant for One Week', '“he shall confirm the covenant with many for one week.”', ISR, 'Dan. 9:27'],
    ['Michael Your Prince', '“none that holdeth with me in these things, but Michael your prince.”', ISR, 'Dan. 10:21'],
    ['Michael Stands Up', '“at that time shall Michael stand up, the great prince which standeth for the children of thy people.”', ISR, 'Dan. 12:1'],
    ['Many Shall Awake', '“many of them that sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt.”', ISR, 'Dan. 12:2'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Blessed Be His Name', '“Blessed be the name of God for ever and ever: for wisdom and might are his.”', 'Dan. 2:20'],
    ['He Changes Times', '“he changeth the times and the seasons: he removeth kings, and setteth up kings.”', 'Dan. 2:21'],
    ['Able to Deliver', '“our God whom we serve is able to deliver us.”', 'Dan. 3:17'],
    ['The Most High Rules', '“the most High ruleth in the kingdom of men.”', 'Dan. 4:17'],
    ['None Can Stay His Hand', '“none can stay his hand, or say unto him, What doest thou?”', 'Dan. 4:35'],
    ['Pride Abased', '“those that walk in pride he is able to abase.”', 'Dan. 4:37'],
    ['Weighed in the Balances', '“Thou art weighed in the balances, and art found wanting.”', 'Dan. 5:27'],
    ['The Living God', '“he is the living God, and stedfast for ever.”', 'Dan. 6:26'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s kingdom, seventy weeks or the people of Daniel; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Bless His name</b> — Wisdom and might are His (Dan. 2:20).', '<b>Trust His rule over rulers</b> — He removeth kings and setteth up kings (Dan. 2:21).', '<b>Stand while trusting</b> — Our God is able to deliver (Dan. 3:17).', '<b>Know who rules</b> — The most High ruleth (Dan. 4:17).', '<b>Remember none can stay His hand</b> — He doeth according to His will (Dan. 4:35).', '<b>Guard against pride</b> — He is able to abase (Dan. 4:37).', '<b>Live before the Judge</b> — Weighed in the balances (Dan. 5:27).', '<b>Worship the living God</b> — Stedfast for ever (Dan. 6:26).'))

S(10, "Teaching Outline for Daniel",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Captives in Babylon (Chs. 1–2) — The image and the kingdom. <i>(Dan. 1:8; 2:20–21, 44)</i>', 'Faithful Under Pressure (Chs. 3–6) — Furnace, den and the confessing kings. <i>(Dan. 3:17; 4:35; 5:27; 6:26)</i>', 'Beasts and the Son of Man (Chs. 7–8) — The kingdom given. <i>(Dan. 7:13–14, 18, 27)</i>', 'Prayer and the Seventy Weeks (Ch. 9) — Gabriel’s word. <i>(Dan. 9:24–27)</i>', 'The Last Vision (Chs. 10–12) — The time of trouble and the awakening. <i>(Dan. 10:21; 12:1–2)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Daniel, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward steadfastness, humility, and trust in God’s rule over the nations without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Daniel simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Daniel stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
