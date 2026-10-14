# DRAFT for publisher approval.
BOOK = "1 Timothy"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Sound Doctrine, Order in the Church, and the Good Fight"
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
  P('1 Timothy is a letter from “Paul, an apostle of Jesus Christ by the commandment of God our Saviour, and Lord Jesus Christ” to “Timothy, my own son in the faith” (1 Tim. 1:1–2). Paul had left Timothy at Ephesus to charge some not to teach other doctrine (1 Tim. 1:3). The letter covers sound doctrine, prayer, order in the church, the qualifications of overseers and deacons, and personal charges to Timothy.'),
  BOX("Program Identity:", '1 Timothy is a pastoral letter from Paul to a younger minister. It is read for what it says about doctrine, godliness, and the church’s order. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 1 Timothy',
  H('Movement 1 — Sound Doctrine and the Law (Ch. 1)'),
  P('Paul charges Timothy about other doctrine, says the law is good if used lawfully, and gives his own testimony of mercy (1 Tim. 1:3–5, 8–16).'),
  H('Movement 2 — Prayer and Order in the Church (Chs. 2–3)'),
  P('Paul urges prayers for all men, names one God and one mediator, gives directions for the assembly, and sets out the qualifications for bishops and deacons (1 Tim. 2:1–8; 3:1–13).'),
  H('Movement 3 — The Mystery of Godliness and False Teaching (Chs. 3:14–4:16)'),
  P('Paul writes of the house of God and the mystery of godliness, warns of some who depart from the faith, and charges Timothy to take heed to himself and the doctrine (1 Tim. 3:15–16; 4:1–16).'),
  H('Movement 4 — Care for Others and Godly Contentment (Chs. 5–6)'),
  P('Paul gives directions about widows, elders, and servants, warns about the love of money, and gives a final charge to fight the good fight (1 Tim. 5:1–8, 17; 6:6–12, 20).'))

S(3, 'Program Themes in 1 Timothy',
  H('1. Sound Doctrine'),
  P('Paul charges that no other doctrine be taught (1 Tim. 1:3, 10).'),
  H('2. Prayer for All'),
  P('He urges supplications and prayers for all men and for kings (1 Tim. 2:1–2).'),
  H('3. The House of God'),
  P('The church of the living God is “the pillar and ground of the truth” (1 Tim. 3:15).'),
  H('4. Godliness'),
  P('“Godliness with contentment is great gain” (1 Tim. 6:6).'),
  H('5. The Good Fight'),
  P('“Fight the good fight of faith, lay hold on eternal life” (1 Tim. 6:12).'))

S(4, 'Christ in 1 Timothy',
  H('1. The Saviour'),
  P('Christ Jesus came into the world to save sinners (1 Tim. 1:15).'),
  H('2. The One Mediator'),
  P('There is “one God, and one mediator between God and men, the man Christ Jesus” (1 Tim. 2:5).'),
  H('3. A Ransom for All'),
  P('He gave himself a ransom for all (1 Tim. 2:6).'),
  H('4. God Manifest in the Flesh'),
  P('“Great is the mystery of godliness: God was manifest in the flesh” (1 Tim. 3:16).'),
  H('5. The Saviour of All Men'),
  P('God is “the Saviour of all men, specially of those that believe” (1 Tim. 4:10).'))

S(5, 'The Church, the Law, and Israel in 1 Timothy',
  P('The letter speaks of the law and of the church without placing believers inside Israel’s covenants:'),
  L('“The law is good, if a man use it lawfully” (1 Tim. 1:8). The study reports this as written and builds no wider doctrine of the law from it.', 'The church of the living God is called “the pillar and ground of the truth” (1 Tim. 3:15).', 'The letter refers to Paul as a pattern for those who should believe on Christ (1 Tim. 1:16).', 'The letter does not place the church under any Israelite covenant.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('1 Timothy teaches the church’s order and doctrine:'),
  L('one God and one mediator between God and men (1 Tim. 2:5)', 'prayer for all men and for kings', 'qualifications for bishops and deacons (1 Tim. 3:1–13)', 'the mystery of godliness (1 Tim. 3:16)', 'godliness with contentment and the good fight of faith'),
  P('It does not give a single church-government program beyond what the letter states, and it leaves the wider questions to other studies.'))

S(7, 'Truths Table: What 1 Timothy Says',
  P('Program Identity shows where a truth belongs. “Body of Christ (Pauline) Truth” marks a statement, command, warning or instruction given to the Body of Christ through Paul.'),
  TBL(['Category', 'Truth Revealed in 1 Timothy', 'Program Identity', 'Scripture'], [['Christ Came to Save', 'Christ Jesus came into the world to save sinners.', 'Body of Christ (Pauline) Truth', '1 Tim. 1:15'], ['One Mediator', 'There is one God and one mediator between God and men.', 'Body of Christ (Pauline) Truth', '1 Tim. 2:5'], ['The Church', 'The house of God is the church of the living God.', 'Body of Christ (Pauline) Truth', '1 Tim. 3:15'], ['Mystery of Godliness', 'God was manifest in the flesh.', 'Body of Christ (Pauline) Truth', '1 Tim. 3:16'], ['Departing from the Faith', 'In the latter times some shall depart from the faith.', 'Body of Christ (Pauline) Truth', '1 Tim. 4:1'], ['Qualifications', 'The bishop must be blameless, the husband of one wife.', 'Body of Christ (Pauline) Truth', '1 Tim. 3:1–7'], ['The Law', 'The law is good if a man use it lawfully.', 'Body of Christ (Pauline) Truth', '1 Tim. 1:8'], ['The Good Fight', 'Fight the good fight of faith.', 'Body of Christ (Pauline) Truth', '1 Tim. 6:12']], [20, 36, 26, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Pray for All', 'Supplications, prayers, intercessions and thanks for all men.', '1 Tim. 2:1'], ['Godliness with Contentment', 'Godliness with contentment is great gain.', '1 Tim. 6:6'], ['Love of Money', 'The love of money is the root of all evil.', '1 Tim. 6:10'], ['Provide for Family', 'Provide for your own, and specially for those of your own house.', '1 Tim. 5:8'], ['Be an Example', 'Be an example of the believers in word, conversation, charity, faith, purity.', '1 Tim. 4:12'], ['Take Heed', 'Take heed unto thyself, and unto the doctrine.', '1 Tim. 4:16'], ['Honor Those Who Labour', 'Let the elders that rule well be counted worthy of double honour.', '1 Tim. 5:17'], ['Good Works', 'Be rich in good works, ready to distribute.', '1 Tim. 6:18']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 1 Timothy says to believers, what it reports about the law and later departures, and what holds for all people. Its instructions apply to the church addressed. The reports are read in their own setting.'),
  P('Drawn from 1 Timothy’s instructions and from universal truths. The Body of Christ should:'),
  OL('<b>Hold sound doctrine</b> — Keep to the doctrine taught (1 Tim. 1:3; 4:16).', '<b>Pray for all</b> — Offer prayers for all men and for those in authority (1 Tim. 2:1–2).', '<b>Order the church well</b> — Follow the qualifications for those who lead (1 Tim. 3:1–13).', '<b>Honor those who labour</b> — Honor elders who rule well (1 Tim. 5:17).', '<b>Care for family</b> — Provide for your own (1 Tim. 5:8).', '<b>Be an example</b> — Set an example in word, conduct, love, faith, and purity (1 Tim. 4:12).', '<b>Pursue godliness with contentment</b> — Resist the love of money (1 Tim. 6:6–10).', '<b>Fight the good fight</b> — Lay hold on eternal life (1 Tim. 6:12).'))

S(10, "Teaching Outline for 1 Timothy",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('A Charge Against Other Doctrine (1:1–20) — The law and Paul’s mercy. <i>(1 Tim. 1:3–5, 15)</i>', 'Prayer for All (Ch. 2) — One God and one mediator. <i>(1 Tim. 2:1–8)</i>', 'Bishops and Deacons (3:1–13) — Qualifications. <i>(1 Tim. 3:1–13)</i>', 'The House of God (3:14–16) — The pillar and ground of the truth. <i>(1 Tim. 3:15–16)</i>', 'Departing and Holding On (Ch. 4) — Doctrine and example. <i>(1 Tim. 4:1, 12, 16)</i>', 'Widows, Elders, and Servants (Chs. 5–6:2) — Care and honor. <i>(1 Tim. 5:1–8, 17)</i>', 'Contentment and the Good Fight (6:3–21) — Godliness and the final charge. <i>(1 Tim. 6:6–12, 20)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 Timothy, helping you see both what the letter says to believers and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what 1 Timothy itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 Timothy simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, 1 Timothy was written during the overlap from Paul to a younger minister. This Companion shows you how to read the letter’s charges and church order in their own setting while drawing out the principles that apply to all believers."))
