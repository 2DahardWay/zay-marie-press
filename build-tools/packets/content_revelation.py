# DRAFT for publisher approval.
BOOK = "Revelation"
TESTAMENT = "New Testament"
GENRE = "revelation"
SUBTITLE = "The Revelation of Jesus Christ and the Kingdom of Our Lord and of His Christ"
SECTIONS = []
def S(n, t, *blocks): SECTIONS.append((n, t, list(blocks)))
P = lambda x: ("p", x)
L = lambda *xs: ("ul", list(xs))
H = lambda x: ("h3", x)
TBL = lambda head, rows, widths: ("table", head, rows, widths)
OL = lambda *xs: ("ol", list(xs))
OLR = lambda *xs: ("olr", list(xs))
BOX = lambda lead, text: ("box", lead, text)

S(1, "Book Overview (Program-Aware)",
  P('Revelation opens with “The Revelation of Jesus Christ, which God gave unto him, to shew unto his servants things which must shortly come to pass” (Rev. 1:1). John writes “to the seven churches which are in Asia” (Rev. 1:4). The book speaks about the Lord among the seven candlesticks, letters to seven churches, the throne in heaven and the Lamb that opens the seals, the sealing of the tribes of Israel, the seven trumpets, a woman and a man child, the beasts, the harvest and the vials, the white horse of the King, a thousand years, a new heaven and a new earth, and the closing words about the book itself.'),
  BOX("Program Identity:", 'Revelation names its own audience: God’s “servants” (Rev. 1:1) and “the seven churches which are in Asia” (Rev. 1:4). Its scenes include the tribes of the children of Israel (Rev. 7:4; 21:12). It is read as the prophecy it calls itself (Rev. 1:3). This reading rests on the book’s own audience markers and setting.'))

S(2, 'Narrative Flow of Revelation',
  H('Movement 1 — The Vision and the Seven Churches (Ch. 1–3)'),
  P('John sees one like the Son of man among seven golden candlesticks, is told to write the things he has seen, the things which are, and the things which shall be hereafter, and receives seven letters to the churches (Rev. 1:12–3:22).'),
  H('Movement 2 — The Throne and the Book (Ch. 4–5)'),
  P('A throne is set in heaven, worship is given to the Creator, and the Lamb that was slain is found worthy to take the book and open its seals (Rev. 4:1–5:14).'),
  H('Movement 3 — The Seals, the Sealed, and the Trumpets (Ch. 6–11)'),
  P('The seals are opened, the servants of God are sealed out of all the tribes of the children of Israel, a great multitude stands before the throne, and the seven trumpets sound until the kingdoms of this world are become the kingdoms of our Lord (Rev. 6:1–11:19).'),
  H('Movement 4 — The Woman, the Beasts, and the Lamb on Mount Sion (Ch. 12–14)'),
  P('A woman brings forth a man child, a beast rises out of the sea, and the Lamb stands on the mount Sion with an hundred forty and four thousand (Rev. 12:1–14:20).'),
  H('Movement 5 — The Vials, Babylon, and the King (Ch. 15–19)'),
  P('The song of Moses and of the Lamb is sung, the vials are poured out, Babylon falls, and heaven opens upon a white horse and one called Faithful and True (Rev. 15:1–19:21).'),
  H('Movement 6 — The Thousand Years and the New Heaven and Earth (Ch. 20–22)'),
  P('Thrones are set, those who lived and reigned with Christ a thousand years are seen, the dead are judged, and John sees a new heaven and a new earth and the holy Jerusalem descending out of heaven (Rev. 20:1–22:21).'))

S(3, 'Program Themes in Revelation',
  H('1. The Revelation of Jesus Christ'),
  P('“The Revelation of Jesus Christ, which God gave unto him” (Rev. 1:1).'),
  H('2. His Coming'),
  P('“Behold, he cometh with clouds; and every eye shall see him” (Rev. 1:7).'),
  H('3. The Lamb Worthy'),
  P('“Thou art worthy to take the book, and to open the seals thereof: for thou wast slain” (Rev. 5:9).'),
  H('4. The Sealed of Israel'),
  P('“There were sealed an hundred and forty and four thousand of all the tribes of the children of Israel” (Rev. 7:4).'),
  H('5. The Kingdom'),
  P('“The kingdoms of this world are become the kingdoms of our Lord, and of his Christ; and he shall reign for ever and ever” (Rev. 11:15).'),
  H('6. The Rider on the White Horse'),
  P('“He that sat upon him was called Faithful and True, and in righteousness he doth judge and make war” (Rev. 19:11).'),
  H('7. The Thousand Years'),
  P('“They lived and reigned with Christ a thousand years” (Rev. 20:4).'),
  H('8. A New Heaven and a New Earth'),
  P('“I saw a new heaven and a new earth” (Rev. 21:1).'))

S(4, 'Christ in Revelation',
  H('1. The Faithful Witness'),
  P('John writes of “Jesus Christ, who is the faithful witness, and the first begotten of the dead, and the prince of the kings of the earth” (Rev. 1:5).'),
  H('2. The Almighty'),
  P('“I am Alpha and Omega, the beginning and the ending, saith the Lord” (Rev. 1:8).'),
  H('3. The Lion and the Lamb'),
  P('“Behold, the Lion of the tribe of Juda, the Root of David, hath prevailed to open the book” (Rev. 5:5).'),
  H('4. Christ and His Throne'),
  P('“To him that overcometh will I grant to sit with me in my throne, even as I also overcame, and am set down with my Father in his throne” (Rev. 3:21). Both clauses are reported as written.'),
  H('5. King of Kings'),
  P('“KING OF KINGS, AND LORD OF LORDS” (Rev. 19:16).'),
  H('6. The Lord Jesus'),
  P('“Surely I come quickly. Amen. Even so, come, Lord Jesus” (Rev. 22:20).'))

S(5, 'The Audience of Revelation',
  P('The book’s audience markers are read as written:'),
  L('The book is given to show God’s “servants” things which must shortly come to pass (Rev. 1:1).', 'John writes “to the seven churches which are in Asia” (Rev. 1:4).', 'The sealed are “of all the tribes of the children of Israel” (Rev. 7:4), and the twelve gates of the city carry “the names of the twelve tribes of the children of Israel” (Rev. 21:12).', 'The Lamb stands on “the mount Sion” (Rev. 14:1), and the city is “the holy Jerusalem” (Rev. 21:10).', 'The book describes the nations and the kings of the earth in its scenes (Rev. 15:4; 21:24).', 'The prophetic scenes of the book do not describe the Body of Christ, and the great multitude of Rev. 7:9 is not the Body of Christ.'),
  P('This reading rests on the book’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('Revelation is read as the prophecy it says it is (Rev. 1:3). What it commands, warns and promises is not addressed to the Body of Christ and does not transfer to it. Truths about God and Christ that the book states stand as written:'),
  L('the Lord God which is, and which was, and which is to come, the Almighty (Rev. 1:8)', 'the Creator worthy to receive glory and honour and power (Rev. 4:11)', 'the Lamb slain and worthy (Rev. 5:9)', 'the Lord God omnipotent reigneth (Rev. 19:6)', 'God’s wiping away of all tears (Rev. 21:4)'),
  P('Its letters to the seven churches, its scenes of judgment and its promises to the one who overcometh are reported as written and are not turned into instructions or promises to the Body.'))

S(7, 'Truths Table: What Revelation Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the book.'),
  TBL(['Category', 'Truth Revealed in Revelation', 'Program Identity', 'Scripture'], [['The Revelation', 'The Revelation of Jesus Christ is given to show his servants things which must shortly come to pass; “Blessed is he that readeth.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 1:1–3'], ['His Coming', '“Behold, he cometh with clouds; and every eye shall see him.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 1:7'], ['The Seven Churches', '“He that hath an ear, let him hear what the Spirit saith unto the churches.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 2:7'], ['The Lamb Worthy', 'The Lamb “hast redeemed us to God by thy blood,” and “we shall reign on the earth.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 5:9–10'], ['The Sealed', 'The sealed are an hundred and forty and four thousand “of all the tribes of the children of Israel.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 7:4'], ['The Kingdom', '“The kingdoms of this world are become the kingdoms of our Lord, and of his Christ.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 11:15'], ['The Man Child', 'A man child “who was to rule all nations with a rod of iron” is “caught up unto God, and to his throne.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 12:5'], ['The Lamb on Mount Sion', 'The Lamb stands “on the mount Sion” with an hundred forty and four thousand.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 14:1–4'], ['Faithful and True', 'The rider is called “Faithful and True,” with the name “KING OF KINGS, AND LORD OF LORDS.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 19:11–16'], ['The Thousand Years', 'Those who “lived and reigned with Christ a thousand years”; “Blessed and holy is he that hath part in the first resurrection.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 20:4–6'], ['The New Heaven and Earth', '“I saw a new heaven and a new earth,” and “the tabernacle of God is with men.”', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 21:1–3'], ['The Words of This Book', 'A warning to any man who shall add to or take away from the words of the prophecy of this book.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Rev. 22:18–19']], [18, 32, 27, 23]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['The Almighty', '“I am Alpha and Omega, the beginning and the ending, saith the Lord.”', 'Rev. 1:8'], ['The Creator Is Worthy', '“Thou art worthy, O Lord, to receive glory and honour and power: for thou hast created all things.”', 'Rev. 4:11'], ['Just and True', '“just and true are thy ways, thou King of saints.”', 'Rev. 15:3'], ['The Lord Reigns', '“the Lord God omnipotent reigneth.”', 'Rev. 19:6'], ['No More Death', '“there shall be no more death, neither sorrow, nor crying.”', 'Rev. 21:4']], [28, 50, 22]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The table in Section 7 marks every row “Israel / Kingdom / Prophecy Explicit Truth” because Revelation is read on its own audience markers. The tables separate what the book says in its prophetic scenes from what holds for all people. Its commands, warnings and promises are not turned into the Body’s. The applications below draw only on the universal truths in Section 8.'),
  P('Drawn from the universal truths of Revelation. Readers can:'),
  OL('<b>Honour the Almighty</b> — He is Alpha and Omega (Rev. 1:8).', '<b>Give the Creator glory</b> — He is worthy because He created all things (Rev. 4:11).', '<b>Trust His ways</b> — They are just and true (Rev. 15:3).', '<b>Rest in His reign</b> — The Lord God omnipotent reigneth (Rev. 19:6).', '<b>Take comfort in His promise</b> — There shall be no more death (Rev. 21:4).'))

S(10, "Teaching Outline for Revelation",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Vision and the Seven Churches (Ch. 1–3) — What John saw and what he was told to write. <i>(Rev. 1:1–19)</i>', 'The Throne and the Book (Ch. 4–5) — The Creator and the Lamb. <i>(Rev. 4:11; 5:9–10)</i>', 'The Seals and the Sealed (Ch. 6–7) — The seals and the tribes. <i>(Rev. 6:2; 7:4, 9)</i>', 'The Trumpets (Ch. 8–11) — Until the kingdoms become our Lord’s. <i>(Rev. 11:15)</i>', 'The Woman, the Beasts, and Mount Sion (Ch. 12–14) — The man child and the Lamb. <i>(Rev. 12:5; 13:1; 14:1–4)</i>', 'The Vials, Babylon, and the King (Ch. 15–19) — Faithful and True. <i>(Rev. 15:3–4; 19:11–16)</i>', 'The Thousand Years and the New Creation (Ch. 20–22) — Thrones, a new heaven, and the closing words. <i>(Rev. 20:4–6; 21:1–4; 22:18–20)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Revelation, helping you see both what the book says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on the universal truths Revelation itself states, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Revelation simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the book states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Revelation is read on the book’s own audience markers and setting. This Companion shows you how to read the book in its own setting while drawing out the universal truths it states."))
