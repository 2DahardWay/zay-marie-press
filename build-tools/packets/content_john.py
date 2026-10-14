# DRAFT for publisher approval.
BOOK = "John"
TESTAMENT = "New Testament"
GENRE = "gospels"
SUBTITLE = "The Word Made Flesh, the Signs and Witness, and the Life Given to Those Who Believe"
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
  P('John begins “In the beginning was the Word,” and says that “the Word was made flesh, and dwelt among us” (John 1:1, 14). The Gospel records John the Baptist’s witness that the Lord was to “be made manifest to Israel,” the signs he did, the feasts at Jerusalem, the raising of Lazarus, the King’s entry, the upper room, the cross and the empty tomb, and it states its purpose: “these are written, that ye might believe that Jesus is the Christ, the Son of God” (John 1:31; 2:11; 11:25; 12:13; 20:31).'),
  BOX("Program Identity:", 'The portions of John treated here belong to the Prophecy Program: the Word came to his own, the Baptist was sent that the Lord should be made manifest to Israel, and Nathanael confesses him the King of Israel (John 1:11, 31, 49). Its words on love, truth and worship are also placed in the Universal Truths Table.'))

S(2, "Narrative Flow of John",
  H('Movement 1 — The Word (Ch. 1)'),
  P('The Word who was with God and was God is made flesh, and the Baptist bears witness that the Lord should be made manifest to Israel (John 1:1, 14, 29, 31).'),
  H('Movement 2 — Signs and Witness (Chs. 2–4)'),
  P('The beginning of miracles in Cana, the conversation about worshipping in spirit and truth, and the word that salvation is of the Jews (John 2:11; 4:22, 24).'),
  H('Movement 3 — The Feasts and the Conflict (Chs. 5–10)'),
  P('The Lord bids them search the scriptures, calls himself the bread of life and the good shepherd, and is received by some and refused by others (John 5:39; 6:14, 35; 10:11).'),
  H('Movement 4 — Lazarus and the King’s Entry (Chs. 11–12)'),
  P('The Lord is the resurrection and the life, and the crowd cries, “Blessed is the King of Israel” (John 11:25; 12:13, 15).'),
  H('Movement 5 — The Upper Room and the Prayer (Chs. 13–17)'),
  P('The new commandment to love one another, the Lord’s own words in chapter 14 and the prayer that the disciples be sanctified through the truth (John 13:34; 14:6; 15:12; 17:17).'),
  H('Movement 6 — The Cross, the Tomb and the Purpose (Chs. 18–21)'),
  P('The kingdom not of this world, the title on the cross, the signs written that the reader might believe, and the testimony that is true (John 18:36; 19:19; 20:30–31; 21:24).'))

S(3, "Prophecy-Program Themes in John",
  H('1. The Word'),
  P('“In the beginning was the Word, and the Word was with God, and the Word was God” (John 1:1).'),
  H('2. His Own'),
  P('“He came unto his own, and his own received him not” (John 1:11).'),
  H('3. Manifest to Israel'),
  P('“That he should be made manifest to Israel, therefore am I come baptizing with water” (John 1:31).'),
  H('4. Signs'),
  P('“This beginning of miracles did Jesus in Cana of Galilee, and manifested forth his glory” (John 2:11).'),
  H('5. Salvation of the Jews'),
  P('“For salvation is of the Jews” (John 4:22).'),
  H('6. Worship in Spirit and Truth'),
  P('“God is a Spirit: and they that worship him must worship him in spirit and in truth” (John 4:24).'),
  H('7. Written That You Might Believe'),
  P('“These are written, that ye might believe that Jesus is the Christ, the Son of God” (John 20:31).'))

S(4, "Christ in John: The Prophetic Trajectory",
  H('1. The Lamb of God'),
  P('“Behold the Lamb of God, which taketh away the sin of the world” (John 1:29).'),
  H('2. The King of Israel'),
  P('“Thou art the Son of God; thou art the King of Israel” (John 1:49).'),
  H('3. The Bread of Life'),
  P('“I am the bread of life: he that cometh to me shall never hunger” (John 6:35).'),
  H('4. The Good Shepherd'),
  P('“I am the good shepherd: the good shepherd giveth his life for the sheep” (John 10:11).'),
  H('5. The Resurrection and the Life'),
  P('“I am the resurrection, and the life” (John 11:25).'),
  H('6. The Way, the Truth, and the Life'),
  P('“I am the way, the truth, and the life: no man cometh unto the Father, but by me” (John 14:6), reported as written, in the upper room with the disciples.'),
  H('7. The Title on the Cross'),
  P('“JESUS OF NAZARETH THE KING OF THE JEWS” (John 19:19).'))

S(5, "Israel’s Identity in John",
  P("John reinforces Israel’s:"),
  L('the King of Israel confessed by Nathanael and by the crowd (John 1:49; 12:13)', 'the Lord made manifest to Israel (John 1:31)', 'his own who received him not (John 1:11)', 'salvation of the Jews (John 4:22)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("John does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its King of Israel, its Lord made manifest to Israel and its salvation of the Jews belong exclusively to Israel’s program; its words on truth, love and worship are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in John", "Program Identity", "Scripture"], [
    ['His Own', '“He came unto his own, and his own received him not.”', ISR, 'John 1:11'],
    ['Manifest to Israel', '“that he should be made manifest to Israel.”', ISR, 'John 1:31'],
    ['King of Israel', '“thou art the King of Israel.”', ISR, 'John 1:49'],
    ['Salvation of the Jews', '“salvation is of the Jews.”', ISR, 'John 4:22'],
    ['That Prophet', '“This is of a truth that prophet that should come into the world.”', ISR, 'John 6:14'],
    ['Hosanna', '“Blessed is the King of Israel that cometh in the name of the Lord.”', ISR, 'John 12:13'],
    ['Daughter of Sion', '“Fear not, daughter of Sion: behold, thy King cometh.”', ISR, 'John 12:15'],
    ['The Title', '“JESUS OF NAZARETH THE KING OF THE JEWS.”', ISR, 'John 19:19'],
    ['Why These Are Written', '“these are written, that ye might believe that Jesus is the Christ, the Son of God.”', ISR, 'John 20:31'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['In the Beginning', '“All things were made by him; and without him was not any thing made that was made.”', 'John 1:3'],
    ['God’s Love for the World', '“For God so loved the world, that he gave his only begotten Son.”', 'John 3:16'],
    ['Worship in Spirit and Truth', '“God is a Spirit: and they that worship him must worship him in spirit and in truth.”', 'John 4:24'],
    ['The Truth Frees', '“ye shall know the truth, and the truth shall make you free.”', 'John 8:32'],
    ['Love One Another', '“A new commandment I give unto you, That ye love one another.”', 'John 13:34'],
    ['Greater Love', '“Greater love hath no man than this, that a man lay down his life for his friends.”', 'John 15:13'],
    ['The Word Is Truth', '“Sanctify them through thy truth: thy word is truth.”', 'John 17:17'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s Israel’s King, manifestation or salvation; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Worship in spirit and truth</b> — God is a Spirit (John 4:24).', '<b>Seek the truth</b> — The truth shall make you free (John 8:32).', '<b>Love one another</b> — As the Lord loved (John 13:34).', '<b>Lay down your life for your friends</b> — Greater love hath no man (John 15:13).', '<b>Hold to the Word</b> — Thy word is truth (John 17:17).'))

S(10, "Teaching Outline for John",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Word (Ch. 1) — The Word made flesh. <i>(John 1:1, 11, 14, 29, 31)</i>', 'Signs and Witness (Chs. 2–4) — Spirit and truth. <i>(John 2:11; 4:22, 24)</i>', 'The Feasts and the Conflict (Chs. 5–10) — Bread of life and good shepherd. <i>(John 5:39; 6:14, 35; 10:11)</i>', 'Lazarus and the King’s Entry (Chs. 11–12) — The resurrection and the life. <i>(John 11:25; 12:13, 15)</i>', 'The Upper Room and the Prayer (Chs. 13–17) — Love one another. <i>(John 13:34; 14:6; 15:12–13; 17:17)</i>', 'The Cross, the Tomb and the Purpose (Chs. 18–21) — Written that ye might believe. <i>(John 18:36; 19:19; 20:30–31; 21:24)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read John, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward truth, love, and worship in spirit and truth without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching John simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, John stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
