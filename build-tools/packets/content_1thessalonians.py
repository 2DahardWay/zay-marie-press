# DRAFT for publisher approval.
BOOK = "1 Thessalonians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Faith, Love, Hope, and the Lord’s Coming for Us"
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
  P('1 Thessalonians is a letter from Paul, Silvanus and Timotheus “unto the church of the Thessalonians which is in God the Father and in the Lord Jesus Christ” (1 Thess. 1:1). Paul recalls how the gospel came to them, how they turned from idols, and how he cared for them. He then gives instruction on holy living, comfort about those who sleep, and the day of the Lord.'),
  BOX("Program Identity:", '1 Thessalonians is addressed to a young church of believers. It sets the hope of those in Christ beside the day of the Lord, and it says that God has not appointed them to wrath (1 Thess. 5:9). This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 1 Thessalonians',
  H('Movement 1 — The Gospel Received and the Work of Faith (Chs. 1–2)'),
  P('Paul gives thanks for their work of faith, labour of love, and patience of hope, recalls how they turned to God from idols, and describes his gentle care among them (1 Thess. 1:3, 9–10; 2:7–13).'),
  H('Movement 2 — Timothy’s Report and Holy Living (Chs. 3–4:12)'),
  P('Paul sends Timothy, receives good news, and urges them to abound in love, to be sanctified, and to walk honestly (1 Thess. 3:1–6, 12; 4:1–12).'),
  H('Movement 3 — The Hope and the Day of the Lord (4:13–5:11)'),
  P('Paul comforts them about those who sleep with the Lord’s descent from heaven, then writes of the day of the Lord coming as a thief (1 Thess. 4:13–18; 5:1–11).'),
  H('Movement 4 — Closing Exhortations (5:12–28)'),
  P('Paul gives short commands for the church’s life and prays that they be sanctified wholly (1 Thess. 5:12–24).'))

S(3, 'Program Themes in 1 Thessalonians',
  H('1. The Work of Faith'),
  P('Paul remembers their “work of faith, and labour of love, and patience of hope” (1 Thess. 1:3).'),
  H('2. Turning to God'),
  P('They turned to God from idols “to serve the living and true God” (1 Thess. 1:9).'),
  H('3. The Word Received'),
  P('They received the word “not as the word of men, but as it is in truth, the word of God” (1 Thess. 2:13).'),
  H('4. Comfort in Death'),
  P('Paul does not want them ignorant concerning those who sleep (1 Thess. 4:13).'),
  H('5. Not Appointed to Wrath'),
  P('“God hath not appointed us to wrath, but to obtain salvation by our Lord Jesus Christ” (1 Thess. 5:9).'))

S(4, 'Christ in 1 Thessalonians',
  H('1. God’s Son from Heaven'),
  P('They wait for His Son from heaven, whom He raised from the dead, who delivered them from the wrath to come (1 Thess. 1:10).'),
  H('2. The Lord Who Died and Rose'),
  P('“If we believe that Jesus died and rose again” (1 Thess. 4:14).'),
  H('3. The Lord Himself'),
  P('“The Lord himself shall descend from heaven with a shout” (1 Thess. 4:16).'),
  H('4. Who Died for Us'),
  P('Christ died for us, “that, whether we wake or sleep, we should live together with him” (1 Thess. 5:10).'),
  H('5. Our Lord Jesus Christ'),
  P('Salvation is obtained by our Lord Jesus Christ (1 Thess. 5:9).'))

S(5, 'The Day of the Lord in 1 Thessalonians',
  P('The letter sets the hope of believers beside the day of the Lord:'),
  L('The letter names the Lord’s descent from heaven, the dead in Christ rising first, and the living being caught up together with them (1 Thess. 4:16–17).', 'The day of the Lord is set beside this hope, and Paul tells the church it is not appointed to wrath (1 Thess. 5:2, 9).', 'The letter speaks of Jews who killed the Lord Jesus and of wrath come upon them (1 Thess. 2:14–16). The study reports the text as written.', 'The letter does not make the church a party to any Israelite covenant.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('1 Thessalonians teaches the standing and hope of the church in Christ:'),
  L('a church in God the Father and in the Lord Jesus Christ', 'the Lord’s descent and the gathering of the dead and living in Christ (1 Thess. 4:16–17)', 'not appointed to wrath but to salvation (1 Thess. 5:9)', 'sanctification, love and quiet living (1 Thess. 4:3, 9–11)', 'comfort one toward another with these words (1 Thess. 4:18)'),
  P('It does not set a date for the Lord’s coming, and it says that the times and seasons are not written to them (1 Thess. 5:1).'))

S(7, 'Truths Table: What 1 Thessalonians Says',
  P('Program Identity shows how each passage is classified. “Addressed to Believers (Identity / Doctrine)” marks teaching for believers. “Addressed to Believers (Warnings / Corrections)” marks warnings, corrections, exhortations, and future conditions believers must prepare for. “Text Only” marks a passage with no instructional force, such as a greeting or a background statement.'),
  TBL(['Category', 'Truth Revealed in 1 Thessalonians', 'Program Identity', 'Scripture'], [['Turning to God', 'They turned from idols to serve the living and true God.', 'Addressed to Believers (Identity / Doctrine)', '1 Thess. 1:9'], ['The Hope', 'The Lord himself shall descend from heaven; the dead in Christ rise first.', 'Addressed to Believers (Identity / Doctrine)', '1 Thess. 4:16'], ['Caught Up', 'The living are caught up together with them in the clouds to meet the Lord in the air.', 'Addressed to Believers (Identity / Doctrine)', '1 Thess. 4:17'], ['Not Appointed to Wrath', 'God hath not appointed us to wrath.', 'Addressed to Believers (Identity / Doctrine)', '1 Thess. 5:9'], ['Sanctification', 'This is the will of God, even your sanctification.', 'Addressed to Believers (Identity / Doctrine)', '1 Thess. 4:3'], ['The Day of the Lord', 'It so cometh as a thief in the night.', 'Addressed to Believers (Warnings / Corrections)', '1 Thess. 5:2'], ['Jews and Wrath', 'Wrath is come upon them to the uttermost.', 'Addressed to Believers (Warnings / Corrections)', '1 Thess. 2:14–16'], ['Wake or Sleep', 'Whether we wake or sleep, we should live together with Christ.', 'Addressed to Believers (Identity / Doctrine)', '1 Thess. 5:10']], [20, 36, 26, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Love One Another', 'Increase and abound in love one toward another.', '1 Thess. 3:12'], ['Quiet Living', 'Study to be quiet, and to do your own business, and to work with your own hands.', '1 Thess. 4:11'], ['Comfort One Another', 'Comfort one another with these words.', '1 Thess. 4:18'], ['Rejoice Evermore', 'Rejoice evermore.', '1 Thess. 5:16'], ['Pray Without Ceasing', 'Pray without ceasing.', '1 Thess. 5:17'], ['Give Thanks', 'In every thing give thanks.', '1 Thess. 5:18'], ['Prove All Things', 'Prove all things; hold fast that which is good.', '1 Thess. 5:21'], ['Abstain from Evil', 'Abstain from all appearance of evil.', '1 Thess. 5:22']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 1 Thessalonians says to believers, what it reports about the day of the Lord and Israel, and what holds for all people. The instructions apply to the believers addressed, and the reports are read in their own setting.'),
  P('Drawn from 1 Thessalonians’ instructions to believers and from universal truths. The Body of Christ should:'),
  OL('<b>Work in faith and love</b> — Keep the work of faith and labour of love (1 Thess. 1:3).', '<b>Serve the living God</b> — Turn from idols to serve Him (1 Thess. 1:9).', '<b>Walk in holiness</b> — Live in sanctification (1 Thess. 4:3–7).', '<b>Comfort one another</b> — Use the words about the Lord’s coming for comfort (1 Thess. 4:18).', '<b>Be watchful and sober</b> — Put on faith and love and the hope of salvation (1 Thess. 5:6–8).', '<b>Respect those who labour</b> — Know them that labour among you (1 Thess. 5:12–13).', '<b>Rejoice, pray, give thanks</b> — Practice the short commands of 5:16–18.', '<b>Hold fast the good</b> — Prove all things (1 Thess. 5:21).'))

S(10, "Teaching Outline for 1 Thessalonians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Gospel Received (Ch. 1) — Their work of faith and turning to God. <i>(1 Thess. 1:3, 9–10)</i>', 'Paul’s Care (Ch. 2) — The word received and Paul’s gentle labour. <i>(1 Thess. 2:7–13)</i>', 'Timothy’s Report (Ch. 3) — Faith and love established. <i>(1 Thess. 3:6–13)</i>', 'Walking to Please God (4:1–12) — Sanctification, love, quiet living. <i>(1 Thess. 4:3, 9–11)</i>', 'The Hope of Those Who Sleep (4:13–18) — The Lord’s descent and comfort. <i>(1 Thess. 4:13–18)</i>', 'The Day of the Lord (5:1–11) — Not appointed to wrath. <i>(1 Thess. 5:2, 9)</i>', 'Closing Commands (5:12–28) — Short exhortations and prayer. <i>(1 Thess. 5:16–24)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 Thessalonians, helping you see both what the letter says to believers and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what 1 Thessalonians itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 Thessalonians simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, 1 Thessalonians was written during the overlap to a church of believers. This Companion shows you how to read its hope and its report on the day of the Lord each in its own setting while drawing out the principles that apply to all believers."))
