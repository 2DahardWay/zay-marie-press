# DRAFT for publisher approval.
BOOK = "2 Thessalonians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Steadfast Under Pressure, and the Day of Christ Set in Order"
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
  P('2 Thessalonians is a letter from Paul, Silvanus and Timotheus “unto the church of the Thessalonians in God our Father and the Lord Jesus Christ” (2 Thess. 1:1). Paul thanks God for their growing faith and patience under persecution. He writes about the Lord’s revelation from heaven, corrects a worry about the day of Christ, and gives directions about the idle.'),
  BOX("Program Identity:", '2 Thessalonians is addressed to believers under pressure and sets out what must precede the day it names. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 2 Thessalonians',
  H('Movement 1 — Thanksgiving and Patience in Persecution (Ch. 1)'),
  P('Paul gives thanks for their faith and love and writes of the Lord Jesus being revealed from heaven with His mighty angels (2 Thess. 1:3–10).'),
  H('Movement 2 — The Day of Christ and What Must Come First (Ch. 2)'),
  P('Paul asks them not to be shaken, names a falling away and the man of sin, and speaks of what withholds and of the working of error (2 Thess. 2:1–12). He then gives thanks for their choosing and bids them stand fast (2 Thess. 2:13–15).'),
  H('Movement 3 — Prayer and Orderly Living (Ch. 3)'),
  P('Paul asks for prayer, says the Lord is faithful, and directs that those who will not work should not eat (2 Thess. 3:1–15).'))

S(3, 'Program Themes in 2 Thessalonians',
  H('1. Faith Growing and Love Abounding'),
  P('Their faith groweth exceedingly and their love toward each other abounds (2 Thess. 1:3).'),
  H('2. Patience Under Persecution'),
  P('Paul speaks of their patience and faith in all their persecutions (2 Thess. 1:4).'),
  H('3. Not Shaken'),
  P('Paul asks them not to be soon shaken in mind or troubled (2 Thess. 2:2).'),
  H('4. Stand Fast'),
  P('“Stand fast, and hold the traditions which ye have been taught” (2 Thess. 2:15).'),
  H('5. Not Weary in Well-Doing'),
  P('“Be not weary in well doing” (2 Thess. 3:13).'))

S(4, 'Christ in 2 Thessalonians',
  H('1. The Lord Jesus Revealed'),
  P('The Lord Jesus is revealed from heaven with His mighty angels, in flaming fire (2 Thess. 1:7–8).'),
  H('2. Glorified in His Saints'),
  P('He comes to be glorified in His saints and admired in all them that believe (2 Thess. 1:10).'),
  H('3. The Lord Shall Consume'),
  P('The Lord shall consume with the spirit of His mouth and destroy with the brightness of His coming (2 Thess. 2:8).'),
  H('4. Our Lord Jesus Christ'),
  P('Paul prays that our Lord Jesus Christ Himself and God our Father comfort and stablish them (2 Thess. 2:16–17).'),
  H('5. The Lord of Peace'),
  P('“The Lord of peace himself give you peace always by all means” (2 Thess. 3:16).'))

S(5, 'The Day of Christ in 2 Thessalonians',
  P('The letter’s central passage is read as written:'),
  L('Paul asks them not to be shaken by a spirit, a word, or a letter as from him that “the day of Christ is at hand” (2 Thess. 2:2). The study leaves the wording of verse 2 open.', 'Paul writes that that day shall not come “except there come a falling away first, and that man of sin be revealed, the son of perdition” (2 Thess. 2:3).', 'Paul writes that he “sitteth in the temple of God, shewing himself that he is God” (2 Thess. 2:4). The study reports the “temple of God” as written, with no location or timing.', 'Paul writes of what “withholdeth” and of one who “letteth” until he be taken out of the way (2 Thess. 2:6–7). The study reports this exactly as written and identifies neither.', 'The man of sin is not set beside other passages in this companion; the study reports each text in its own place.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('2 Thessalonians teaches the church’s steadfastness under pressure:'),
  L('thanksgiving for growing faith and abounding love', 'patience and faith in persecution', 'standing fast and holding what was taught', 'the Lord’s comfort and establishment of hearts and works', 'orderly work and quiet living'),
  P('It does not say how long before the day it names, and it does not identify the one who letteth beyond what the text says.'))

S(7, 'Truths Table: What 2 Thessalonians Says',
  P('Program Identity shows where a truth belongs. “Body of Christ (Pauline) Truth” marks a statement, command, warning or instruction given to the Body of Christ through Paul.'),
  TBL(['Category', 'Truth Revealed in 2 Thessalonians', 'Program Identity', 'Scripture'], [['Growing Faith', 'Faith grows exceedingly and love abounds.', 'Body of Christ (Pauline) Truth', '2 Thess. 1:3'], ['The Lord Revealed', 'The Lord Jesus is revealed from heaven with mighty angels.', 'Body of Christ (Pauline) Truth', '2 Thess. 1:7–8'], ['Gathering Together', 'Paul writes concerning the coming of the Lord and our gathering together unto Him.', 'Body of Christ (Pauline) Truth', '2 Thess. 2:1'], ['The Falling Away', 'A falling away comes first, and the man of sin is revealed.', 'Body of Christ (Pauline) Truth', '2 Thess. 2:3'], ['What Withholdeth', 'What withholdeth and he who letteth are reported without identification.', 'Body of Christ (Pauline) Truth', '2 Thess. 2:6–7'], ['Chosen to Salvation', 'God hath from the beginning chosen you to salvation.', 'Body of Christ (Pauline) Truth', '2 Thess. 2:13'], ['Stand Fast', 'Hold the traditions taught by word or epistle.', 'Body of Christ (Pauline) Truth', '2 Thess. 2:15'], ['Orderly Work', 'If any would not work, neither should he eat.', 'Body of Christ (Pauline) Truth', '2 Thess. 3:10']], [20, 36, 26, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['God Is Just', 'It is a righteous thing with God to recompense tribulation.', '2 Thess. 1:6'], ['The Lord Is Faithful', 'The Lord is faithful, who shall stablish you and keep you from evil.', '2 Thess. 3:3'], ['Work for Your Bread', 'If any would not work, neither should he eat.', '2 Thess. 3:10'], ['Quietness', 'Work with quietness and eat their own bread.', '2 Thess. 3:12'], ['Well-Doing', 'Be not weary in well doing.', '2 Thess. 3:13'], ['Brotherly Admonition', 'Count him not as an enemy, but admonish him as a brother.', '2 Thess. 3:15'], ['Pray for Us', 'Brethren, pray for us, that the word of the Lord may have free course.', '2 Thess. 3:1'], ['Peace', 'The Lord of peace give you peace always by all means.', '2 Thess. 3:16']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 2 Thessalonians says to believers, what it reports about the day of Christ and the man of sin, and what holds for all people. The reports are read as written and are not joined to other passages here.'),
  P('Drawn from 2 Thessalonians’ instructions to believers and from universal truths. The Body of Christ should:'),
  OL('<b>Grow in faith and love</b> — Let faith grow and love abound (2 Thess. 1:3).', '<b>Endure in patience</b> — Keep faith in persecution (2 Thess. 1:4).', '<b>Not be shaken</b> — Hold steady when troubled by reports (2 Thess. 2:2).', '<b>Stand fast</b> — Hold what was taught (2 Thess. 2:15).', '<b>Pray for ministers</b> — Pray that the word have free course (2 Thess. 3:1).', '<b>Work quietly</b> — Eat your own bread (2 Thess. 3:10–12).', '<b>Not be weary</b> — Keep doing well (2 Thess. 3:13).', '<b>Admonish as a brother</b> — Correct without treating as an enemy (2 Thess. 3:15).'))

S(10, "Teaching Outline for 2 Thessalonians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Thanksgiving (1:1–12) — Faith, love, and patience under persecution. <i>(2 Thess. 1:3–4)</i>', 'The Lord Revealed (1:7–12) — The revelation from heaven. <i>(2 Thess. 1:7–10)</i>', 'Do Not Be Shaken (2:1–2) — The gathering and the day of Christ. <i>(2 Thess. 2:1–2)</i>', 'The Falling Away and the Man of Sin (2:3–12) — Read as written. <i>(2 Thess. 2:3–12)</i>', 'Chosen and Called (2:13–17) — Salvation, stand fast, and comfort. <i>(2 Thess. 2:13–17)</i>', 'Prayer and Faithfulness (3:1–5) — The Lord is faithful. <i>(2 Thess. 3:1–5)</i>', 'Orderly Living (3:6–18) — Work, well-doing, and peace. <i>(2 Thess. 3:10–16)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 Thessalonians, helping you see both what the letter says to believers and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what 2 Thessalonians itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 Thessalonians simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, 2 Thessalonians was written during the overlap to believers under pressure. This Companion shows you how to read its central passage exactly as written while drawing out the principles that apply to all believers."))
