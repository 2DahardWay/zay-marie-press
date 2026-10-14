# DRAFT for publisher approval.
BOOK = "Mark"
TESTAMENT = "New Testament"
GENRE = "gospels"
SUBTITLE = "The Gospel of the Kingdom of God, the Servant, and the Ransom for Many"
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
  P('Mark begins “The beginning of the gospel of Jesus Christ, the Son of God” (Mark 1:1). The Lord comes into Galilee “preaching the gospel of the kingdom of God,” teaches as one that had authority, calms the sea, is confessed by Peter as the Christ, comes to give his life “a ransom for many,” and is crucified under the superscription “THE KING OF THE JEWS” before the empty tomb (Mark 1:14–15, 22; 4:41; 8:29; 10:45; 15:26; 16:6).'),
  BOX("Program Identity:", 'The portions of Mark treated here belong to the Prophecy Program: the gospel Jesus preaches is the gospel of the kingdom of God, and the title written over the cross is the King of the Jews (Mark 1:14–15; 15:26). Its words on love and service are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Mark",
  H('Movement 1 — The Gospel of the Kingdom Begins (Ch. 1)'),
  P('The Lord comes into Galilee preaching the kingdom of God, calls fishers of men and teaches with authority (Mark 1:1, 14–15, 17, 22).'),
  H('Movement 2 — Authority and Opposition (Chs. 2–6)'),
  P('The Lord calls sinners, speaks of the sabbath, and the wind and the sea obey him (Mark 2:17, 27; 3:35; 4:41).'),
  H('Movement 3 — The Christ Confessed (Chs. 7–9)'),
  P('Peter answers, “Thou art the Christ,” and the Lord calls the cross-bearing path (Mark 8:29, 34; 9:35).'),
  H('Movement 4 — The Road and the Ransom (Ch. 10)'),
  P('The Son of man comes to minister and to give his life a ransom for many (Mark 10:14, 45).'),
  H('Movement 5 — Jerusalem and the Great Commandment (Chs. 11–13)'),
  P('The house of prayer is cleansed, and the first commandment is named (Mark 11:17; 12:30–31).'),
  H('Movement 6 — The Cross and the Tomb (Chs. 14–16)'),
  P('The blood of the new testament, the King of the Jews on the cross, and the risen Lord (Mark 14:24; 15:26; 16:6, 15–16).'))

S(3, "Prophecy-Program Themes in Mark",
  H('1. The Gospel of the Kingdom of God'),
  P('“Jesus came into Galilee, preaching the gospel of the kingdom of God” (Mark 1:14).'),
  H('2. The Time Fulfilled'),
  P('“The time is fulfilled, and the kingdom of God is at hand: repent ye, and believe the gospel” (Mark 1:15).'),
  H('3. Fishers of Men'),
  P('“Come ye after me, and I will make you to become fishers of men” (Mark 1:17).'),
  H('4. The Servant of All'),
  P('“If any man desire to be first, the same shall be last of all, and servant of all” (Mark 9:35).'),
  H('5. The House of Prayer'),
  P('“My house shall be called of all nations the house of prayer” (Mark 11:17).'),
  H('6. The King of the Jews'),
  P('“THE KING OF THE JEWS” (Mark 15:26).'))

S(4, "Christ in Mark: The Prophetic Trajectory",
  H('1. The Son of God'),
  P('“The beginning of the gospel of Jesus Christ, the Son of God” (Mark 1:1); Peter says, “Thou art the Christ” (Mark 8:29).'),
  H('2. The Ransom for Many'),
  P('“The Son of man came not to be ministered unto, but to minister, and to give his life a ransom for many” (Mark 10:45).'),
  H('3. The Blood of the New Testament'),
  P('“This is my blood of the new testament, which is shed for many” (Mark 14:24), reported as written.'),
  H('4. He Is Risen'),
  P('“Ye seek Jesus of Nazareth, which was crucified: he is risen; he is not here” (Mark 16:6).'))

S(5, "Israel’s Identity in Mark",
  P("Mark reinforces Israel’s:"),
  L('the gospel of the kingdom of God preached in Galilee (Mark 1:14–15)', 'the Christ confessed by Peter (Mark 8:29)', 'the King of the Jews written over the cross (Mark 15:26)', 'the house of prayer named from Isaiah, set in Jerusalem (Mark 11:17)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Mark does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its gospel of the kingdom of God, its call to repent and believe the gospel, and its King of the Jews belong exclusively to Israel’s program; its words on love of God and neighbour, service and faith are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Mark", "Program Identity", "Scripture"], [
    ['The Gospel of the Kingdom of God', '“preaching the gospel of the kingdom of God.”', ISR, 'Mark 1:14'],
    ['The Kingdom at Hand', '“The time is fulfilled, and the kingdom of God is at hand: repent ye, and believe the gospel.”', ISR, 'Mark 1:15'],
    ['Peter’s Confession', '“Thou art the Christ.”', ISR, 'Mark 8:29'],
    ['The Ransom for Many', '“to give his life a ransom for many.”', ISR, 'Mark 10:45'],
    ['The Blood of the New Testament', '“This is my blood of the new testament, which is shed for many.”', ISR, 'Mark 14:24'],
    ['The Superscription', '“THE KING OF THE JEWS.”', ISR, 'Mark 15:26'],
    ['He Is Risen', '“he is risen; he is not here.”', ISR, 'Mark 16:6'],
    ['Go Into All the World', '“Go ye into all the world, and preach the gospel to every creature.”', ISR, 'Mark 16:15'],
    ['Believeth and Is Baptized', '“He that believeth and is baptized shall be saved.”', ISR, 'Mark 16:16'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['The First Commandment', '“thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy mind, and with all thy strength.”', 'Mark 12:30'],
    ['Love of Neighbour', '“Thou shalt love thy neighbour as thyself.”', 'Mark 12:31'],
    ['Servant of All', '“the same shall be last of all, and servant of all.”', 'Mark 9:35'],
    ['All Things Possible', '“all things are possible to him that believeth.”', 'Mark 9:23'],
    ['What Defiles', '“the things which come out of him, those are they that defile the man.”', 'Mark 7:15'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the gospel of the kingdom, the ransom or the great commission; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Love God with everything</b> — Heart, soul, mind and strength (Mark 12:30).', '<b>Love your neighbour</b> — As yourself (Mark 12:31).', '<b>Serve others</b> — Last of all, and servant of all (Mark 9:35).', '<b>Believe Him</b> — All things are possible to him that believeth (Mark 9:23).', '<b>Guard the heart</b> — What comes out defiles (Mark 7:15).'))

S(10, "Teaching Outline for Mark",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Gospel of the Kingdom Begins (Ch. 1) — Repent and believe. <i>(Mark 1:1, 14–15, 17, 22)</i>', 'Authority and Opposition (Chs. 2–6) — The wind and the sea obey. <i>(Mark 2:17, 27; 4:41)</i>', 'The Christ Confessed (Chs. 7–9) — Thou art the Christ. <i>(Mark 7:15; 8:29, 34; 9:23, 35)</i>', 'The Road and the Ransom (Ch. 10) — A ransom for many. <i>(Mark 10:14, 45)</i>', 'Jerusalem and the Great Commandment (Chs. 11–13) — The first commandment. <i>(Mark 11:17; 12:30–31)</i>', 'The Cross and the Tomb (Chs. 14–16) — The King of the Jews, risen. <i>(Mark 14:24; 15:26; 16:6, 15–16)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Mark, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward service, love of God and neighbour, and faith in the Lord’s power without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Mark simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Mark stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
