# DRAFT for publisher approval.
BOOK = "2 Peter"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Precious Promises, the More Sure Word of Prophecy, and the Day of the Lord"
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
  P('2 Peter is a letter from “Simon Peter, a servant and an apostle of Jesus Christ” (2 Pet. 1:1). It speaks about precious promises, adding to faith, the more sure word of prophecy, false teachers, scoffers in the last days, the day of the Lord, and growing in grace. Peter writes as one who knows that shortly he must put off his tabernacle (2 Pet. 1:13–14).'),
  BOX("Program Identity:", '2 Peter calls itself “This second epistle” (2 Pet. 3:1) and speaks of both letters as written to the same readers. It is read on the audience markers set out in Section 5. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 2 Peter',
  H('Movement 1 — Promises, Virtues, and the More Sure Word (Ch. 1)'),
  P('Peter writes of divine power, exceeding great and precious promises, the things to add to faith, the making sure of calling and election, the eyewitnesses of Christ’s majesty, and the word of prophecy (2 Pet. 1:3–21).'),
  H('Movement 2 — False Teachers and Examples of Judgment (Ch. 2)'),
  P('Peter warns of false teachers who bring in damnable heresies, and recalls the angels that sinned, the old world, Sodom and Gomorrha, and Lot, and the way of Balaam (2 Pet. 2:1–22).'),
  H('Movement 3 — Scoffers and the Day of the Lord (3:1–13)'),
  P('Peter says scoffers shall come in the last days, answers their question about the promise of his coming, and writes of the day of the Lord and of new heavens and a new earth (2 Pet. 3:3–13).'),
  H('Movement 4 — Be Diligent and Grow (3:14–18)'),
  P('Peter calls his readers to be diligent, speaks of the longsuffering of the Lord and of Paul’s epistles, warns them to beware, and closes with a call to grow in grace (2 Pet. 3:14–18).'))

S(3, 'Program Themes in 2 Peter',
  H('1. Divine Power and Precious Promises'),
  P('The letter speaks of “exceeding great and precious promises” (2 Pet. 1:4).'),
  H('2. Diligence'),
  P('“Giving all diligence, add to your faith virtue” (2 Pet. 1:5).'),
  H('3. The More Sure Word of Prophecy'),
  P('“We have also a more sure word of prophecy” (2 Pet. 1:19).'),
  H('4. False Teachers'),
  P('“There shall be false teachers among you” (2 Pet. 2:1).'),
  H('5. The Promise of His Coming'),
  P('Scoffers say, “Where is the promise of his coming?” (2 Pet. 3:4).'),
  H('6. The Day of the Lord'),
  P('“The day of the Lord will come as a thief in the night” (2 Pet. 3:10).'),
  H('7. Growth in Grace'),
  P('“Grow in grace, and in the knowledge of our Lord and Saviour Jesus Christ” (2 Pet. 3:18).'))

S(4, 'Christ in 2 Peter',
  H('1. Our Saviour Jesus Christ'),
  P('Peter writes “through the righteousness of God and our Saviour Jesus Christ” (2 Pet. 1:1).'),
  H('2. The Everlasting Kingdom'),
  P('An entrance is spoken of “into the everlasting kingdom of our Lord and Saviour Jesus Christ” (2 Pet. 1:11).'),
  H('3. The Power and Coming'),
  P('Peter and the others “made known unto you the power and coming of our Lord Jesus Christ” (2 Pet. 1:16).'),
  H('4. The Beloved Son'),
  P('The voice from the excellent glory said, “This is my beloved Son, in whom I am well pleased” (2 Pet. 1:17).'),
  H('5. The Lord That Bought'),
  P('False teachers are described as “denying the Lord that bought them” (2 Pet. 2:1).'),
  H('6. Glory Now and For Ever'),
  P('“To him be glory both now and for ever” (2 Pet. 3:18).'))

S(5, 'The Audience of 2 Peter',
  P('The letter’s audience markers are read as written:'),
  L('Peter calls the letter “This second epistle” and says that “in both which” he stirs up their pure minds (2 Pet. 3:1). The letter speaks of two epistles to the same readers.', 'Peter’s first letter is addressed “to the strangers scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia” (1 Pet. 1:1).', 'Peter calls his readers to be mindful of “the words which were spoken before by the holy prophets, and of the commandment of us the apostles of the Lord and Saviour” (2 Pet. 3:2).', 'Peter says that “our beloved brother Paul also according to the wisdom given unto him hath written unto you” (2 Pet. 3:15), and that in Paul’s epistles are some things “hard to be understood” (2 Pet. 3:16). The letter reports this and says no more about those epistles here.', 'The letter does not name Israel in its address and does not use the name the Body of Christ.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('2 Peter is read with its first letter. What it commands, warns and promises to its readers is not addressed to the Body of Christ and does not transfer to it. Truths about God and Christ that the letter states stand as written:'),
  L('Christ’s divine power and majesty (2 Pet. 1:3, 16–18)', 'the moving of holy men of God by the Holy Ghost (2 Pet. 1:21)', 'the Lord’s knowledge of how to deliver the godly (2 Pet. 2:9)', 'the longsuffering of the Lord (2 Pet. 3:9, 15)', 'grace and the knowledge of our Lord and Saviour Jesus Christ (2 Pet. 3:18)'),
  P('Its description of the day of the Lord and of new heavens and a new earth is reported as written and is not turned into a promise to the Body.'))

S(7, 'Truths Table: What 2 Peter Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter.'),
  TBL(['Category', 'Truth Revealed in 2 Peter', 'Program Identity', 'Scripture'], [['Divine Power', 'His divine power hath given us “all things that pertain unto life and godliness.”', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 1:3–4'], ['Add to Faith', 'Add virtue, knowledge, temperance, patience, godliness, brotherly kindness, and charity to faith.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 1:5–7'], ['Calling and Election', 'Give diligence to make calling and election sure: “ye shall never fall.”', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 1:10–11'], ['The Word of Prophecy', '“no prophecy of the scripture is of any private interpretation.”', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 1:19–21'], ['False Teachers', '“there shall be false teachers among you, who privily shall bring in damnable heresies.”', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 2:1–3'], ['Scoffers', 'Scoffers shall come in the last days, “walking after their own lusts.”', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 3:3–4'], ['The Day of the Lord', '“the day of the Lord will come as a thief in the night.”', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 3:10–13'], ['Beware', '“beware lest ye also, being led away with the error of the wicked, fall from your own stedfastness.”', 'Israel / Kingdom / Prophecy Explicit Truth', '2 Pet. 3:17–18']], [18, 40, 24, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['The Source of Scripture', '“holy men of God spake as they were moved by the Holy Ghost.”', '2 Pet. 1:21'], ['The Lord Delivers', '“The Lord knoweth how to deliver the godly out of temptations.”', '2 Pet. 2:9'], ['Bondage', '“of whom a man is overcome, of the same is he brought in bondage.”', '2 Pet. 2:19'], ['By the Word of God', '“by the word of God the heavens were of old.”', '2 Pet. 3:5'], ['The Lord’s Time', '“one day is with the Lord as a thousand years, and a thousand years as one day.”', '2 Pet. 3:8'], ['The Lord’s Patience', 'The Lord is “not willing that any should perish, but that all should come to repentance.”', '2 Pet. 3:9'], ['Longsuffering', '“the longsuffering of our Lord is salvation.”', '2 Pet. 3:15'], ['Grow in Grace', '“grow in grace, and in the knowledge of our Lord and Saviour Jesus Christ.”', '2 Pet. 3:18']], [28, 50, 22]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The table in Section 7 marks every row “Israel / Kingdom / Prophecy Explicit Truth” because 2 Peter is read on its own audience markers. The tables separate what the letter says to its readers from what holds for all people. Its commands, warnings and promises to those readers are not turned into the Body’s. The applications below draw only on the universal truths in Section 8.'),
  P('Drawn from the universal truths of 2 Peter. Readers can:'),
  OL('<b>Trust the source of Scripture</b> — Holy men spake as moved by the Holy Ghost (2 Pet. 1:21).', '<b>Rest in the Lord’s deliverance</b> — He knows how to deliver the godly (2 Pet. 2:9).', '<b>Watch for bondage</b> — Whoever is overcome is brought into bondage (2 Pet. 2:19).', '<b>Remember the word of God</b> — By it the heavens were of old (2 Pet. 3:5).', '<b>Take the long view</b> — One day with the Lord is as a thousand years (2 Pet. 3:8).', '<b>See His patience</b> — He is not willing that any should perish (2 Pet. 3:9).', '<b>Count longsuffering as salvation</b> — Receive the Lord’s patience as His gift (2 Pet. 3:15).', '<b>Grow</b> — Grow in grace and in the knowledge of the Lord and Saviour (2 Pet. 3:18).'))

S(10, "Teaching Outline for 2 Peter",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Divine Power and Precious Promises (1:1–4) — What God has given. <i>(2 Pet. 1:3–4)</i>', 'Add to Your Faith (1:5–11) — Diligence, calling, and election. <i>(2 Pet. 1:5–11)</i>', 'Eyewitnesses and the More Sure Word (1:12–21) — Majesty and prophecy. <i>(2 Pet. 1:16–21)</i>', 'False Teachers and Judgments (Ch. 2) — Heresies and examples of judgment. <i>(2 Pet. 2:1–9)</i>', 'Scoffers and the Promise of His Coming (3:1–9) — The word of God and the Lord’s patience. <i>(2 Pet. 3:3–9)</i>', 'The Day of the Lord (3:10–13) — New heavens and a new earth. <i>(2 Pet. 3:10–13)</i>', 'Be Diligent and Grow (3:14–18) — Longsuffering, warning, and grace. <i>(2 Pet. 3:14–18)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 Peter, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on the universal truths 2 Peter itself states, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 Peter simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 2 Peter is read with its first letter, on the audience markers the letters themselves give. This Companion shows you how to read the letter in its own setting while drawing out the universal truths it states."))
