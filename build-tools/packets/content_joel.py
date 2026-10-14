# DRAFT for publisher approval.
BOOK = "Joel"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Locusts, the Day of the LORD, and the Spirit Poured Out"
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
  P('Joel is “the word of the LORD that came to Joel the son of Pethuel” (Joel 1:1). It speaks of a plague of locusts, calls for the trumpet in Zion and for a turning to the LORD, promises that the LORD will pour out His spirit, and speaks of the great and terrible day of the LORD, the gathering of the nations, and Judah dwelling for ever (Joel 1:15; 2:1, 12–13, 28–32; 3:2, 20).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to Zion, Judah and Jerusalem about the day of the LORD, deliverance in Zion, and the nations gathered before Him (Joel 2:1, 32; 3:1–2, 17, 20).'))

S(2, "Narrative Flow of Joel",
  H('Movement 1 — The Locusts and the Day at Hand (Ch. 1)'),
  P('The land is stripped, and the prophet cries, “the day of the LORD is at hand” (Joel 1:15).'),
  H('Movement 2 — The Trumpet and the Turning (Ch. 2:1–17)'),
  P('The trumpet is blown in Zion, and the people are told to rend the heart and not the garments (Joel 2:1, 11–13).'),
  H('Movement 3 — Restoration and the Spirit (Ch. 2:18–32)'),
  P('The LORD promises to restore the years the locust hath eaten and to pour out His spirit (Joel 2:25, 28–32).'),
  H('Movement 4 — The Nations in the Valley (Ch. 3:1–16)'),
  P('The LORD will bring again the captivity of Judah and Jerusalem and gather all nations (Joel 3:1–2, 14, 16).'),
  H('Movement 5 — Judah Shall Dwell for Ever (Ch. 3:17–21)'),
  P('The LORD dwells in Zion, and Jerusalem is holy (Joel 3:17, 20).'))

S(3, "Prophecy-Program Themes in Joel",
  H('1. The Day at Hand'),
  P('“The day of the LORD is at hand, and as a destruction from the Almighty shall it come” (Joel 1:15).'),
  H('2. The Trumpet in Zion'),
  P('“Blow ye the trumpet in Zion, and sound an alarm in my holy mountain” (Joel 2:1).'),
  H('3. Turn With the Heart'),
  P('“Rend your heart, and not your garments, and turn unto the LORD your God” (Joel 2:13).'),
  H('4. Years Restored'),
  P('“I will restore to you the years that the locust hath eaten” (Joel 2:25).'),
  H('5. The Spirit Poured Out'),
  P('“I will pour out my spirit upon all flesh” (Joel 2:28).'),
  H('6. Deliverance in Zion'),
  P('“In mount Zion and in Jerusalem shall be deliverance” (Joel 2:32).'),
  H('7. Judah Dwells'),
  P('“Judah shall dwell for ever, and Jerusalem from generation to generation” (Joel 3:20).'))

S(4, "Christ in Joel: The Prophetic Trajectory",
  H('1. The Outpouring'),
  P('Peter quotes Joel 2:28–32 at Pentecost (Acts 2:16–21); the passage is reported as written.'),
  H('2. Deliverance Named'),
  P('“Whosoever shall call on the name of the LORD shall be delivered” is given with “in mount Zion and in Jerusalem shall be deliverance” (Joel 2:32).'),
  H('3. The Day of the LORD'),
  P('The great and terrible day of the LORD is described in Joel 2:11, 31 and 3:14.'))

S(5, "Israel’s Identity in Joel",
  P("Joel reinforces Israel’s:"),
  L('Zion and Jerusalem as the place of the LORD’s word and deliverance (Joel 2:1, 32)', 'Judah and Jerusalem and the captivity brought again (Joel 3:1)', 'the nations gathered for the LORD’s people and heritage Israel (Joel 3:2)', 'Judah dwelling for ever (Joel 3:20)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Joel does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its day of the LORD, outpouring, deliverance in Zion and gathering of the nations belong exclusively to Israel; its words on the LORD’s grace are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Joel", "Program Identity", "Scripture"], [
    ['The Day at Hand', '“the day of the LORD is at hand, and as a destruction from the Almighty shall it come.”', ISR, 'Joel 1:15'],
    ['The Trumpet in Zion', '“Blow ye the trumpet in Zion, and sound an alarm in my holy mountain.”', ISR, 'Joel 2:1'],
    ['Years Restored', '“I will restore to you the years that the locust hath eaten.”', ISR, 'Joel 2:25'],
    ['The Spirit Poured Out', '“I will pour out my spirit upon all flesh.”', ISR, 'Joel 2:28'],
    ['The Great Day', '“before the great and the terrible day of the LORD come.”', ISR, 'Joel 2:31'],
    ['Deliverance in Zion', '“in mount Zion and in Jerusalem shall be deliverance.”', ISR, 'Joel 2:32'],
    ['The Captivity Brought Again', '“I shall bring again the captivity of Judah and Jerusalem.”', ISR, 'Joel 3:1'],
    ['The Nations Gathered', '“I will also gather all nations, and will bring them down into the valley of Jehoshaphat.”', ISR, 'Joel 3:2'],
    ['Hope of His People', '“the LORD will be the hope of his people.”', ISR, 'Joel 3:16'],
    ['The LORD in Zion', '“I am the LORD your God dwelling in Zion, my holy mountain.”', ISR, 'Joel 3:17'],
    ['Judah Dwells for Ever', '“Judah shall dwell for ever, and Jerusalem from generation to generation.”', ISR, 'Joel 3:20'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['A Torn Heart', '“rend your heart, and not your garments, and turn unto the LORD your God.”', 'Joel 2:13'],
    ['Gracious and Merciful', '“he is gracious and merciful, slow to anger, and of great kindness.”', 'Joel 2:13'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s day of the LORD, Zion or the outpouring; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Turn with the heart</b> — Rend the heart, not the garments (Joel 2:13).', '<b>Rely on His grace</b> — Gracious and merciful, slow to anger (Joel 2:13).'))

S(10, "Teaching Outline for Joel",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Locusts and the Day at Hand (Ch. 1) — A land stripped. <i>(Joel 1:15)</i>', 'The Trumpet and the Turning (Ch. 2:1–17) — Rend the heart. <i>(Joel 2:1, 11–13)</i>', 'Restoration and the Spirit (Ch. 2:18–32) — Years restored. <i>(Joel 2:25, 28–32)</i>', 'The Nations in the Valley (Ch. 3:1–16) — Captivity brought again. <i>(Joel 3:1–2, 16)</i>', 'Judah Shall Dwell for Ever (Ch. 3:17–21) — The LORD in Zion. <i>(Joel 3:17, 20)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Joel, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward repentance, reverence, and trust in the LORD’s kindness without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Joel simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Joel stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
