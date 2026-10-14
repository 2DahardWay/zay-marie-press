# DRAFT for publisher approval.
BOOK = "Matthew"
TESTAMENT = "New Testament"
GENRE = "gospels"
SUBTITLE = "The King of the Jews, the Kingdom at Hand, and the Lost Sheep of the House of Israel"
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
  P('Matthew begins “The book of the generation of Jesus Christ, the son of David, the son of Abraham” (Matt. 1:1). It records the birth of Him who is “born King of the Jews,” the preaching “Repent: for the kingdom of heaven is at hand,” the Lord’s teaching on the mountain, the Twelve sent to “the lost sheep of the house of Israel,” the discourse on Olivet, the Supper, the cross and the empty tomb, and the closing charge to the eleven (Matt. 2:2; 4:17; 10:5–7; 24:14; 26:28; 27:37; 28:6, 19–20).'),
  BOX("Program Identity:", 'The portions of Matthew treated here belong to the Prophecy Program: the Lord is sent “unto the lost sheep of the house of Israel,” and the Twelve are sent to Israel and not to the way of the Gentiles (Matt. 10:5–6; 15:24). Its words on mercy and love are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of Matthew",
  H('Movement 1 — The King Born (Chs. 1–2)'),
  P('The genealogy of Jesus Christ, son of David and son of Abraham, and the question of the wise men, “Where is he that is born King of the Jews?” (Matt. 1:1, 21; 2:2).'),
  H('Movement 2 — The Kingdom at Hand (Chs. 3–4)'),
  P('John and then the Lord preach, “the kingdom of heaven is at hand,” and the Lord goes about Galilee preaching the gospel of the kingdom (Matt. 3:2, 17; 4:4, 17, 23).'),
  H('Movement 3 — The Teaching on the Mountain (Chs. 5–7)'),
  P('The Lord teaches the blessed, the law and the prophets, love of enemies and the golden rule (Matt. 5:3, 17, 44; 6:33; 7:12).'),
  H('Movement 4 — The Twelve Sent to Israel (Chs. 8–16)'),
  P('The Twelve are sent to the lost sheep of the house of Israel, and Peter confesses, “Thou art the Christ” (Matt. 10:5–7; 12:7; 15:24; 16:16).'),
  H('Movement 5 — The Road to Jerusalem (Chs. 17–23)'),
  P('The Twelve are promised thrones, the great commandment is given, and Jerusalem is lamented (Matt. 19:28; 22:37–39; 23:37, 39).'),
  H('Movement 6 — The Olivet Discourse (Chs. 24–25)'),
  P('The gospel of the kingdom is to be preached to all nations, and the Son of man sits on the throne of his glory (Matt. 24:14; 25:31, 34).'),
  H('Movement 7 — The Cross, the Tomb, and the Charge (Chs. 26–28)'),
  P('The blood of the new testament, the title over the cross, the empty tomb and the charge to the eleven (Matt. 26:28; 27:37; 28:6, 19–20).'))

S(3, "Prophecy-Program Themes in Matthew",
  H('1. The Son of David'),
  P('“Jesus Christ, the son of David, the son of Abraham” (Matt. 1:1).'),
  H('2. King of the Jews'),
  P('“Where is he that is born King of the Jews?” (Matt. 2:2).'),
  H('3. The Kingdom at Hand'),
  P('“Repent: for the kingdom of heaven is at hand” (Matt. 4:17).'),
  H('4. The Gospel of the Kingdom'),
  P('“Preaching the gospel of the kingdom, and healing all manner of sickness” (Matt. 4:23).'),
  H('5. The Law and the Prophets Fulfilled'),
  P('“I am not come to destroy, but to fulfil” (Matt. 5:17).'),
  H('6. The Twelve Sent to Israel'),
  P('“Go not into the way of the Gentiles… But go rather to the lost sheep of the house of Israel” (Matt. 10:5–6).'),
  H('7. Twelve Thrones'),
  P('“Ye also shall sit upon twelve thrones, judging the twelve tribes of Israel” (Matt. 19:28).'))

S(4, "Christ in Matthew: The Prophetic Trajectory",
  H('1. Jesus, Who Saves His People'),
  P('“Thou shalt call his name JESUS: for he shall save his people from their sins” (Matt. 1:21).'),
  H('2. The Son of God'),
  P('“This is my beloved Son, in whom I am well pleased” (Matt. 3:17); Peter says, “Thou art the Christ, the Son of the living God” (Matt. 16:16).'),
  H('3. The Blood of the New Testament'),
  P('“This is my blood of the new testament, which is shed for many for the remission of sins” (Matt. 26:28), reported as written, in the Lord’s own words to the Twelve.'),
  H('4. He Is Risen'),
  P('“He is not here: for he is risen, as he said” (Matt. 28:6).'))

S(5, "Israel’s Identity in Matthew",
  P("Matthew reinforces Israel’s:"),
  L('the son of David and the son of Abraham (Matt. 1:1)', 'the King of the Jews (Matt. 2:2; 27:37)', 'the lost sheep of the house of Israel, to whom the Twelve are sent (Matt. 10:5–6; 15:24)', 'the twelve thrones judging the twelve tribes of Israel (Matt. 19:28)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Matthew does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its kingdom message, its mission of the Twelve to the house of Israel, its twelve thrones and its Olivet discourse belong exclusively to Israel’s program; its words on mercy, love of neighbour and every word of God are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Matthew", "Program Identity", "Scripture"], [
    ['Son of David, Son of Abraham', '“the son of David, the son of Abraham.”', ISR, 'Matt. 1:1'],
    ['He Shall Save His People', '“he shall save his people from their sins.”', ISR, 'Matt. 1:21'],
    ['King of the Jews', '“Where is he that is born King of the Jews?”', ISR, 'Matt. 2:2'],
    ['The Kingdom at Hand', '“Repent: for the kingdom of heaven is at hand.”', ISR, 'Matt. 4:17'],
    ['The Gospel of the Kingdom', '“preaching the gospel of the kingdom.”', ISR, 'Matt. 4:23'],
    ['The Poor in Spirit', '“theirs is the kingdom of heaven.”', ISR, 'Matt. 5:3'],
    ['Law and Prophets', '“I am not come to destroy, but to fulfil.”', ISR, 'Matt. 5:17'],
    ['Not to the Gentiles', '“Go not into the way of the Gentiles.”', ISR, 'Matt. 10:5'],
    ['The Lost Sheep', '“go rather to the lost sheep of the house of Israel.”', ISR, 'Matt. 10:6'],
    ['Sent Only to Israel', '“I am not sent but unto the lost sheep of the house of Israel.”', ISR, 'Matt. 15:24'],
    ['The Christ', '“Thou art the Christ, the Son of the living God.”', ISR, 'Matt. 16:16'],
    ['Twelve Thrones', '“ye also shall sit upon twelve thrones, judging the twelve tribes of Israel.”', ISR, 'Matt. 19:28'],
    ['Gospel of the Kingdom to All Nations', '“this gospel of the kingdom shall be preached in all the world for a witness unto all nations.”', ISR, 'Matt. 24:14'],
    ['The Blood of the New Testament', '“this is my blood of the new testament, which is shed for many for the remission of sins.”', ISR, 'Matt. 26:28'],
    ['The Title Over the Cross', '“THIS IS JESUS THE KING OF THE JEWS.”', ISR, 'Matt. 27:37'],
    ['He Is Risen', '“He is not here: for he is risen, as he said.”', ISR, 'Matt. 28:6'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Every Word of God', '“Man shall not live by bread alone, but by every word that proceedeth out of the mouth of God.”', 'Matt. 4:4'],
    ['Love Your Enemies', '“Love your enemies, bless them that curse you, do good to them that hate you.”', 'Matt. 5:44'],
    ['The Golden Rule', '“all things whatsoever ye would that men should do to you, do ye even so to them.”', 'Matt. 7:12'],
    ['Mercy Over Sacrifice', '“I will have mercy, and not sacrifice.”', 'Matt. 12:7'],
    ['The Great Commandment', '“Thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy mind.”', 'Matt. 22:37'],
    ['Love of Neighbour', '“Thou shalt love thy neighbour as thyself.”', 'Matt. 22:39'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s the kingdom of heaven, the Twelve or Olivet; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Live by every word of God</b> — Not by bread alone (Matt. 4:4).', '<b>Love your enemies</b> — Bless and do good (Matt. 5:44).', '<b>Treat others as you would be treated</b> — The golden rule (Matt. 7:12).', '<b>Prefer mercy</b> — Mercy, and not sacrifice (Matt. 12:7).', '<b>Love the Lord with all your heart</b> — The first and great commandment (Matt. 22:37–38).', '<b>Love your neighbour</b> — As yourself (Matt. 22:39).'))

S(10, "Teaching Outline for Matthew",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The King Born (Chs. 1–2) — Son of David, King of the Jews. <i>(Matt. 1:1, 21; 2:2)</i>', 'The Kingdom at Hand (Chs. 3–4) — Repent. <i>(Matt. 3:2, 17; 4:4, 17, 23)</i>', 'The Teaching on the Mountain (Chs. 5–7) — Law, prophets and the golden rule. <i>(Matt. 5:3, 17, 44; 7:12)</i>', 'The Twelve Sent to Israel (Chs. 8–16) — The lost sheep. <i>(Matt. 10:5–7; 15:24; 16:16)</i>', 'The Road to Jerusalem (Chs. 17–23) — Twelve thrones. <i>(Matt. 19:28; 22:37–39; 23:37, 39)</i>', 'The Olivet Discourse (Chs. 24–25) — The gospel of the kingdom. <i>(Matt. 24:14; 25:31, 34)</i>', 'The Cross, the Tomb, and the Charge (Chs. 26–28) — He is risen. <i>(Matt. 26:28; 27:37; 28:6, 19–20)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Matthew, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward mercy, love of neighbour, and living by every word of God without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Matthew simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Matthew stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
