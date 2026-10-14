# DRAFT for publisher approval.
BOOK = "Isaiah"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "The Holy One of Israel, the Servant, and the Kingdom Promised"
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
  P('Isaiah is “The vision of Isaiah the son of Amoz, which he saw concerning Judah and Jerusalem” (Isa. 1:1). It moves from judgment on Judah and the vision of the LORD, through the sign of Immanuel and the child born, to oracles over the nations, the days of Hezekiah, the comfort of Israel, the Servant, and the new heavens and the new earth (Isa. 6:3; 7:14; 9:6; 40:3; 53:5; 65:17).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to Judah and Jerusalem and to Israel about their sin, their judgment, their restoration and their King, with word to the nations beside it (Isa. 1:1; 2:2; 43:1).'))

S(2, "Narrative Flow of Isaiah",
  H('Movement 1 — Judgment and the King Promised (Chs. 1–12)'),
  P('The LORD reasons with Judah, Isaiah sees Him on a throne, and the sign and the child and the Branch are promised (Isa. 1:18; 6:3; 7:14; 9:6–7; 11:1).'),
  H('Movement 2 — The Nations and the Day of the LORD (Chs. 13–35)'),
  P('Oracles on the nations, the LORD’s counsel, and the opening of the eyes of the blind (Isa. 14:24; 25:8; 26:3; 35:5).'),
  H('Movement 3 — Hezekiah and the Turning Point (Chs. 36–39)'),
  P('Jerusalem is threatened and delivered, and Babylon is named for the first time (Isa. 36–39).'),
  H('Movement 4 — Comfort and the Servant (Chs. 40–55)'),
  P('The voice in the wilderness, the incomparable LORD, the Servant, and the invitation to the thirsty (Isa. 40:3, 28; 42:1; 49:6; 53:5–6; 55:1).'),
  H('Movement 5 — Glory and the New Heavens (Chs. 56–66)'),
  P('The Redeemer comes to Zion, the light arises, and the new heavens and the new earth are made (Isa. 59:20; 60:1; 61:1; 65:17; 66:22).'))

S(3, "Prophecy-Program Themes in Isaiah",
  H('1. The LORD Reasoning With Judah'),
  P('“Come now, and let us reason together, saith the LORD” (Isa. 1:18).'),
  H('2. The Mountain of the LORD'),
  P('“It shall come to pass in the last days, that the mountain of the LORD’s house shall be established in the top of the mountains” (Isa. 2:2).'),
  H('3. The Holy One'),
  P('“Holy, holy, holy, is the LORD of hosts: the whole earth is full of his glory” (Isa. 6:3).'),
  H('4. The Throne of David'),
  P('“Of the increase of his government and peace there shall be no end, upon the throne of David, and upon his kingdom” (Isa. 9:7).'),
  H('5. The Remnant Recovered'),
  P('“The Lord shall set his hand again the second time to recover the remnant of his people” (Isa. 11:11).'),
  H('6. The Servant'),
  P('“Behold my servant, whom I uphold; mine elect, in whom my soul delighteth” (Isa. 42:1).'),
  H('7. The New Heavens and the New Earth'),
  P('“I create new heavens and a new earth” (Isa. 65:17).'))

S(4, "Christ in Isaiah: The Prophetic Trajectory",
  H('1. The Sign'),
  P('“A virgin shall conceive, and bear a son, and shall call his name Immanuel” (Isa. 7:14) is quoted in the Gospel of Matthew (Matt. 1:22–23).'),
  H('2. The Child Born'),
  P('“Unto us a child is born, unto us a son is given” (Isa. 9:6).'),
  H('3. The Voice in the Wilderness'),
  P('“The voice of him that crieth in the wilderness, Prepare ye the way of the LORD” (Isa. 40:3) is quoted of John the Baptist (Matt. 3:3).'),
  H('4. The Suffering Servant'),
  P('“He was wounded for our transgressions” (Isa. 53:5) and “the LORD hath laid on him the iniquity of us all” (Isa. 53:6) are the verses the New Testament takes up (Acts 8:32–35; 1 Pet. 2:24–25).'),
  H('5. The Anointed One'),
  P('“The Spirit of the Lord GOD is upon me” (Isa. 61:1) is the passage the Lord reads at Nazareth (Luke 4:16–21).'))

S(5, "Israel’s Identity in Isaiah",
  P("Isaiah reinforces Israel’s:"),
  L('Judah and Jerusalem as the LORD’s people addressed (Isa. 1:1)', 'the mountain of the LORD’s house and the nations coming to it (Isa. 2:2)', 'the throne of David and a kingdom without end (Isa. 9:7)', 'the remnant of his people recovered (Isa. 11:11)', 'the Redeemer coming to Zion (Isa. 59:20)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Isaiah does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its covenant words, the throne of David, the remnant, Zion and the kingdom belong exclusively to Israel; its testimony to the LORD’s holiness and word is also given to all who hear it.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Isaiah", "Program Identity", "Scripture"], [
    ['Concerning Judah and Jerusalem', '“which he saw concerning Judah and Jerusalem.”', ISR, 'Isa. 1:1'],
    ['The Mountain of the LORD', '“the mountain of the LORD’s house shall be established in the top of the mountains.”', ISR, 'Isa. 2:2'],
    ['The Sign of Immanuel', '“a virgin shall conceive, and bear a son.”', ISR, 'Isa. 7:14'],
    ['The Throne of David', '“upon the throne of David, and upon his kingdom, to order it.”', ISR, 'Isa. 9:7'],
    ['The Branch', '“there shall come forth a rod out of the stem of Jesse.”', ISR, 'Isa. 11:1'],
    ['The Remnant Recovered', '“recover the remnant of his people.”', ISR, 'Isa. 11:11'],
    ['Jacob and Israel Redeemed', '“I have redeemed thee, I have called thee by thy name; thou art mine.”', ISR, 'Isa. 43:1'],
    ['The Preserved of Israel', '“to restore the preserved of Israel.”', ISR, 'Isa. 49:6'],
    ['The Redeemer Comes to Zion', '“the Redeemer shall come to Zion.”', ISR, 'Isa. 59:20'],
    ['The Anointed Servant', '“The Spirit of the Lord GOD is upon me.”', ISR, 'Isa. 61:1'],
    ['The Seed Remaining', '“so shall your seed and your name remain.”', ISR, 'Isa. 66:22'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The Holy LORD', '“Holy, holy, holy, is the LORD of hosts: the whole earth is full of his glory.”', 'Isa. 6:3'],
    ['Perfect Peace', '“Thou wilt keep him in perfect peace, whose mind is stayed on thee.”', 'Isa. 26:3'],
    ['The Word Stands', '“the word of our God shall stand for ever.”', 'Isa. 40:8'],
    ['The Creator Faints Not', '“the everlasting God, the LORD, the Creator of the ends of the earth, fainteth not, neither is weary.”', 'Isa. 40:28'],
    ['The First and the Last', '“I am the first, and I am the last; and beside me there is no God.”', 'Isa. 44:6'],
    ['Look and Be Saved', '“Look unto me, and be ye saved, all the ends of the earth: for I am God, and there is none else.”', 'Isa. 45:22'],
    ['The End From the Beginning', '“Declaring the end from the beginning.”', 'Isa. 46:10'],
    ['All Have Gone Astray', '“All we like sheep have gone astray.”', 'Isa. 53:6'],
    ['His Thoughts and Ways', '“my thoughts are not your thoughts, neither are your ways my ways.”', 'Isa. 55:8'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant, throne or land; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Revere His holiness</b> — Holy, holy, holy (Isa. 6:3).', '<b>Keep the mind on Him</b> — Perfect peace (Isa. 26:3).', '<b>Trust the word</b> — It shall stand for ever (Isa. 40:8).', '<b>Rest in the Creator</b> — He fainteth not (Isa. 40:28).', '<b>Know there is no other God</b> — The first and the last (Isa. 44:6).', '<b>Look to Him</b> — Look unto me, and be ye saved (Isa. 45:22).', '<b>Admit the common need</b> — All have gone astray (Isa. 53:6).', '<b>Receive His higher ways</b> — His thoughts are not ours (Isa. 55:8).'))

S(10, "Teaching Outline for Isaiah",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Judgment and the King Promised (Chs. 1–12) — Vision, sign and child. <i>(Isa. 1:18; 6:3; 7:14; 9:6–7; 11:1)</i>', 'The Nations and the Day of the LORD (Chs. 13–35) — Counsel and peace. <i>(Isa. 14:24; 26:3; 35:5)</i>', 'Hezekiah and the Turning Point (Chs. 36–39) — Deliverance and Babylon. <i>(Isa. 36–39)</i>', 'Comfort and the Servant (Chs. 40–55) — The incomparable LORD. <i>(Isa. 40:3, 8, 28; 44:6; 53:5–6; 55:8)</i>', 'Glory and the New Heavens (Chs. 56–66) — The Redeemer and the new creation. <i>(Isa. 59:20; 61:1; 65:17; 66:22)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Isaiah, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward worship, trust, and attention to the word of the LORD without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Isaiah simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Isaiah stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
