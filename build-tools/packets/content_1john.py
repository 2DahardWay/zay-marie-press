# DRAFT for publisher approval.
BOOK = "1 John"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Light, Love, and the Assurance of Eternal Life"
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
  P('1 John does not name its author and opens with no greeting. It begins with “That which was from the beginning, which we have heard, which we have seen with our eyes” concerning “the Word of life” (1 John 1:1). It speaks about fellowship, walking in the light, sin and forgiveness, love, the world, antichrists, being born of God, and eternal life. It returns again and again to light, love, and belief.'),
  BOX("Program Identity:", '1 John speaks to its readers as “my little children” and “beloved” (1 John 2:1; 3:2) and names no program in its opening. It is read on its own audience markers and setting. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 1 John',
  H('Movement 1 — The Word of Life and Fellowship (1:1–4)'),
  P('John declares what was heard, seen, and handled of the Word of life, so that his readers may have fellowship with him and with the Father and His Son Jesus Christ (1 John 1:1–4).'),
  H('Movement 2 — Walking in the Light (1:5–2:11)'),
  P('The message is that God is light. John writes of walking in the light, of confessing sins, of an advocate with the Father, and of keeping His commandments and loving the brother (1 John 1:5–2:11).'),
  H('Movement 3 — The World and the Antichrists (2:12–27)'),
  P('John writes to little children, fathers, and young men, says not to love the world, and speaks of many antichrists and of the anointing that abideth (1 John 2:12–27).'),
  H('Movement 4 — Children of God (2:28–3:24)'),
  P('John calls his readers to abide in Him, speaks of the love by which they are called the sons of God, of righteousness and sin, and of love in deed and in truth (1 John 2:28–3:24).'),
  H('Movement 5 — The Spirits and Love (Ch. 4)'),
  P('John calls his readers to try the spirits, and writes that God is love and that those who love God love their brother also (1 John 4:1–21).'),
  H('Movement 6 — Faith and Eternal Life (Ch. 5)'),
  P('John writes of believing that Jesus is the Christ, of the victory that overcometh the world, of the record God gave of His Son, and of eternal life (1 John 5:1–21).'))

S(3, 'Program Themes in 1 John',
  H('1. Fellowship'),
  P('“Our fellowship is with the Father, and with his Son Jesus Christ” (1 John 1:3).'),
  H('2. Light and Darkness'),
  P('“God is light, and in him is no darkness at all” (1 John 1:5).'),
  H('3. Sin and Forgiveness'),
  P('“If we confess our sins, he is faithful and just to forgive us our sins” (1 John 1:9).'),
  H('4. The World'),
  P('“Love not the world, neither the things that are in the world” (1 John 2:15).'),
  H('5. Antichrists'),
  P('“Even now are there many antichrists” (1 John 2:18).'),
  H('6. Love'),
  P('“Beloved, let us love one another: for love is of God” (1 John 4:7).'),
  H('7. Eternal Life'),
  P('“That ye may know that ye have eternal life” (1 John 5:13).'))

S(4, 'Christ in 1 John',
  H('1. The Word of Life'),
  P('John writes of what was heard, seen, and handled “of the Word of life” (1 John 1:1).'),
  H('2. The Blood of Jesus Christ'),
  P('“The blood of Jesus Christ his Son cleanseth us from all sin” (1 John 1:7).'),
  H('3. Advocate and Propitiation'),
  P('“We have an advocate with the Father, Jesus Christ the righteous,” and “he is the propitiation for our sins” (1 John 2:1–2).'),
  H('4. Manifested to Take Away Sins'),
  P('“He was manifested to take away our sins” (1 John 3:5).'),
  H('5. Sent as Saviour'),
  P('“The Father sent the Son to be the Saviour of the world” (1 John 4:14).'),
  H('6. The Son of God'),
  P('“He that hath the Son hath life” (1 John 5:12).'))

S(5, 'Israel and the Body in 1 John',
  P('The letter is a letter of fellowship and assurance and names no program:'),
  L('The letter does not name Israel, does not mention a covenant, and does not use the name the Body of Christ.', 'It speaks to its readers as “little children,” “brethren,” and “beloved” (1 John 2:1, 7; 3:2).', 'It writes to those who “believe on the name of the Son of God” (1 John 5:13).', 'It speaks of antichrist and of those who “went out from us” (1 John 2:18–19), and the letter reports this as written.', 'It does not state how its readers relate to other programs.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('1 John states truths about God and Christ and instructions for its readers:'),
  L('God is light and God is love (1 John 1:5; 4:8)', 'the blood of Jesus Christ that cleanseth from all sin (1 John 1:7)', 'an advocate with the Father (1 John 2:1)', 'love of the brethren in deed and in truth (1 John 3:14, 18)', 'eternal life in the Son (1 John 5:11–12)'),
  P('It does not give a program for its readers and does not use the name the Body of Christ. It is read on the letter’s own audience markers and setting.'))

S(7, 'Truths Table: What 1 John Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter. “Universal Truth” marks truth that applies to all people, in all time, regardless of program.'),
  TBL(['Category', 'Truth Revealed in 1 John', 'Program Identity', 'Scripture'], [['Fellowship', 'Fellowship with the Father and with His Son Jesus Christ.', 'Israel / Kingdom / Prophecy Explicit Truth', '1 John 1:3'], ['God Is Light', '“God is light, and in him is no darkness at all.”', 'Universal Truth', '1 John 1:5'], ['Cleansing', '“the blood of Jesus Christ his Son cleanseth us from all sin.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 John 1:7'], ['Confession and Forgiveness', '“he is faithful and just to forgive us our sins.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 John 1:9'], ['Advocate and Propitiation', 'An advocate with the Father, and the propitiation for our sins.', 'Israel / Kingdom / Prophecy Explicit Truth', '1 John 2:1–2'], ['Keeping His Commandments', 'The one who says he knows Him and keepeth not His commandments is a liar.', 'Israel / Kingdom / Prophecy Explicit Truth', '1 John 2:3–4'], ['The World', '“Love not the world, neither the things that are in the world.”', 'Universal Truth', '1 John 2:15–17'], ['Antichrists', 'Many antichrists are reported, and the one who denieth that Jesus is the Christ is called antichrist.', 'Israel / Kingdom / Prophecy Explicit Truth', '1 John 2:18–23'], ['Try the Spirits', '“try the spirits whether they are of God.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 John 4:1–3'], ['Eternal Life', '“God hath given to us eternal life, and this life is in his Son.”', 'Universal Truth', '1 John 5:11–13']], [18, 32, 27, 23]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['No One Without Sin', '“If we say that we have no sin, we deceive ourselves.”', '1 John 1:8'], ['The World Passes', '“the world passeth away, and the lust thereof: but he that doeth the will of God abideth for ever.”', '1 John 2:17'], ['Compassion for Need', 'One who “seeth his brother have need” and shuts up compassion is asked, “how dwelleth the love of God in him?”', '1 John 3:17'], ['Love in Deed', '“let us not love in word, neither in tongue; but in deed and in truth.”', '1 John 3:18'], ['God Is Love', '“God is love.”', '1 John 4:8'], ['Love Casts Out Fear', '“perfect love casteth out fear.”', '1 John 4:18'], ['He First Loved', '“We love him, because he first loved us.”', '1 John 4:19'], ['Love of God and Brother', '“he that loveth not his brother whom he hath seen, how can he love God whom he hath not seen?”', '1 John 4:20']], [28, 50, 22]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 1 John says to believers, what it reports about antichrists and the spirits, and what holds for all people. The applications below draw on the letter’s own instructions to believers and on its universal truths.'),
  P('Drawn from 1 John’s instructions and from universal truths. Believers can:'),
  OL('<b>Walk in the light</b> — Fellowship and cleansing follow (1 John 1:7).', '<b>Confess sins</b> — God is faithful and just to forgive (1 John 1:9).', '<b>Keep His commandments</b> — Let words and walk agree (1 John 2:3–6).', '<b>Love in deed and truth</b> — Not in word only (1 John 3:18).', '<b>Try the spirits</b> — Test them whether they are of God (1 John 4:1).', '<b>Love because He first loved</b> — Let His love lead (1 John 4:19).', '<b>Hold to the Son</b> — He that hath the Son hath life (1 John 5:12).', '<b>Keep from idols</b> — Guard what has the heart (1 John 5:21).'))

S(10, "Teaching Outline for 1 John",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Word of Life (1:1–4) — What was heard, seen, and handled. <i>(1 John 1:1–4)</i>', 'Light and Darkness (1:5–2:2) — Walking, confessing, and the advocate. <i>(1 John 1:5–2:2)</i>', 'Commandments and Love (2:3–11) — Knowing Him and loving the brother. <i>(1 John 2:3–11)</i>', 'The World and the Antichrists (2:12–27) — Not loving the world; the anointing. <i>(1 John 2:15–27)</i>', 'Children of God (2:28–3:24) — Abiding, righteousness, and love in deed. <i>(1 John 3:1–3, 16–18)</i>', 'The Spirits and Love (Ch. 4) — Trying the spirits; God is love. <i>(1 John 4:1–21)</i>', 'Faith and Eternal Life (Ch. 5) — The record God gave of His Son. <i>(1 John 5:1–21)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 John, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw on what 1 John itself says to believers and on the truths it states for all people, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 John simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 1 John is read on the letter’s own audience markers and setting. This Companion shows you how to read the letter in its own setting while drawing out the principles that apply to all believers."))
