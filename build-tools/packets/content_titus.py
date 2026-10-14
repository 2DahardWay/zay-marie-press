# DRAFT for publisher approval.
BOOK = "Titus"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Sound Doctrine, Good Works, and the Grace That Teaches"
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
  P('Titus is a letter from “Paul, a servant of God, and an apostle of Jesus Christ” to “Titus, mine own son after the common faith” (Titus 1:1, 4). Paul had left Titus in Crete “that thou shouldest set in order the things that are wanting, and ordain elders in every city” (Titus 1:5). The letter covers the qualifications of elders, sound teaching for each group in the church, and the grace of God that teaches and saves.'),
  BOX("Program Identity:", 'Titus is a pastoral letter from Paul to a younger minister in Crete. It is read for what it says about doctrine, order, and good works. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of Titus',
  H('Movement 1 — Elders and False Teachers (Ch. 1)'),
  P('Paul sets out the qualifications of elders, calls for holding fast the faithful word, and warns of unruly talkers, especially “they of the circumcision” (Titus 1:5–16).'),
  H('Movement 2 — Sound Doctrine and the Grace That Teaches (Ch. 2)'),
  P('Paul tells Titus to speak what befits sound doctrine to older men, older women, young women, young men, and servants, and grounds this in the grace of God that has appeared (Titus 2:1–15).'),
  H('Movement 3 — Good Works and the Washing of Regeneration (Ch. 3)'),
  P('Paul calls for subjection to rulers and gentleness to all men, recalls what they once were, speaks of the kindness of God our Saviour, and bids believers maintain good works (Titus 3:1–11).'))

S(3, 'Program Themes in Titus',
  H('1. Sound Doctrine'),
  P('Titus is to “speak thou the things which become sound doctrine” (Titus 2:1).'),
  H('2. Order in the Churches'),
  P('Elders are to be ordained in every city (Titus 1:5–9).'),
  H('3. Grace That Teaches'),
  P('The grace of God that bringeth salvation has appeared to all men and teaches us to live soberly, righteously, and godly (Titus 2:11–12).'),
  H('4. Not by Works'),
  P('“Not by works of righteousness which we have done, but according to his mercy he saved us” (Titus 3:5).'),
  H('5. Careful to Maintain Good Works'),
  P('Those who have believed in God are to be careful to maintain good works (Titus 3:8).'))

S(4, 'Christ in Titus',
  H('1. God Our Saviour'),
  P('Paul speaks of “God our Saviour” and “Jesus Christ our Saviour” (Titus 1:3–4; 3:4–6).'),
  H('2. The Blessed Hope'),
  P('Believers look for “that blessed hope, and the glorious appearing of the great God and our Saviour Jesus Christ” (Titus 2:13).'),
  H('3. He Gave Himself'),
  P('Christ “gave himself for us, that he might redeem us from all iniquity, and purify unto himself a peculiar people, zealous of good works” (Titus 2:14).'),
  H('4. Kindness and Love Appeared'),
  P('The kindness and love of God our Saviour toward man appeared (Titus 3:4).'),
  H('5. Heirs of Eternal Life'),
  P('Justified by His grace, believers are made heirs according to the hope of eternal life (Titus 3:7).'))

S(5, 'Israel and the Body in Titus',
  P('The letter names “they of the circumcision” and “Jewish fables” in pastoral warnings to Titus, and it does not place believers inside Israel’s covenants:'),
  L('Paul warns Titus of many unruly talkers, “specially they of the circumcision” (Titus 1:10), and warns against “Jewish fables” (Titus 1:14). These are pastoral warnings addressed to Titus for the protection of the believers in Crete, and they are not covenant identity markers.', 'Paul says the Cretians themselves had a prophet who called them liars, and tells Titus to rebuke them sharply (Titus 1:12–13).', '“A peculiar people” (Titus 2:14) is reported as written and is assigned to no covenant beyond the passage’s own setting.', 'The letter does not place believers under any Israelite covenant.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('Titus teaches how the church lives and holds doctrine:'),
  L('sound doctrine taught to every group in the church', 'elders ordained in every city', 'salvation by mercy, the washing of regeneration, and the Holy Ghost (Titus 3:5)', 'good works maintained as the fruit of grace', 'the blessed hope and glorious appearing'),
  P('It does not set out a complete church government beyond what the letter states.'))

S(7, 'Truths Table: What Titus Says',
  P('Program Identity shows how each passage is classified. “Addressed to Believers (Identity / Doctrine)” marks teaching for believers. “Addressed to Believers (Warnings / Corrections)” marks warnings, corrections, exhortations, and future conditions believers must prepare for. “Text Only” marks a passage with no instructional force, such as a greeting or a background statement.'),
  TBL(['Category', 'Truth Revealed in Titus', 'Program Identity', 'Scripture'], [['Sound Doctrine', 'Speak the things which become sound doctrine.', 'Addressed to Believers (Identity / Doctrine)', 'Titus 2:1'], ['Grace That Teaches', 'The grace of God hath appeared to all men and teaches godly living.', 'Addressed to Believers (Identity / Doctrine)', 'Titus 2:11–12'], ['The Blessed Hope', 'Looking for the glorious appearing of our Saviour Jesus Christ.', 'Addressed to Believers (Identity / Doctrine)', 'Titus 2:13'], ['Redeemed and Purified', 'Christ gave himself to redeem us from all iniquity.', 'Addressed to Believers (Identity / Doctrine)', 'Titus 2:14'], ['Not by Works', 'He saved us by mercy, not by works of righteousness we have done.', 'Addressed to Believers (Identity / Doctrine)', 'Titus 3:5'], ['Heirs', 'We are made heirs according to the hope of eternal life.', 'Addressed to Believers (Identity / Doctrine)', 'Titus 3:7'], ['The Circumcision', 'Unruly talkers, specially they of the circumcision.', 'Addressed to Believers (Warnings / Corrections)', 'Titus 1:10'], ['Jewish Fables', 'Give no heed to Jewish fables and commandments of men.', 'Addressed to Believers (Warnings / Corrections)', 'Titus 1:14']], [20, 36, 26, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Holding Fast the Word', 'Hold fast the faithful word as it has been taught.', 'Titus 1:9'], ['Be Sober', 'Teach the aged men to be sober, grave, temperate.', 'Titus 2:2'], ['Good Works', 'Show yourself a pattern of good works.', 'Titus 2:7'], ['Be Subject', 'Be subject to principalities and powers, to obey magistrates.', 'Titus 3:1'], ['Speak Evil of No Man', 'Speak evil of no man, be no brawlers, but gentle.', 'Titus 3:2'], ['Maintain Good Works', 'Be careful to maintain good works.', 'Titus 3:8'], ['Avoid Foolish Questions', 'Avoid foolish questions, and genealogies, and contentions.', 'Titus 3:9'], ['Learn to Maintain Good Works', 'Let ours also learn to maintain good works for necessary uses.', 'Titus 3:14']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what Titus says to believers, what it warns about the circumcision and Jewish fables, and what holds for all people. Its instructions apply to the church addressed. The reports are read in their own setting.'),
  P('Drawn from Titus’ instructions and from universal truths. The Body of Christ should:'),
  OL('<b>Teach sound doctrine</b> — Speak what befits it (Titus 2:1).', '<b>Order the churches</b> — Follow the qualifications for elders (Titus 1:5–9).', '<b>Live by the grace that teaches</b> — Deny ungodliness and live soberly (Titus 2:11–12).', '<b>Look for the blessed hope</b> — Wait for the appearing (Titus 2:13).', '<b>Be subject to rulers</b> — Be ready to every good work (Titus 3:1).', '<b>Be gentle to all</b> — Speak evil of no man (Titus 3:2).', '<b>Remember mercy</b> — Salvation is not by works we have done (Titus 3:5).', '<b>Maintain good works</b> — Be careful to do so (Titus 3:8).'))

S(10, "Teaching Outline for Titus",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Elders and Order (1:1–9) — Qualifications and the faithful word. <i>(Titus 1:5–9)</i>', 'False Teachers (1:10–16) — Rebuke and sound faith. <i>(Titus 1:10–14)</i>', 'Sound Doctrine for Each Group (2:1–10) — Older, younger, and servants. <i>(Titus 2:1–10)</i>', 'The Grace That Teaches (2:11–15) — Grace, hope, and redemption. <i>(Titus 2:11–14)</i>', 'Subject and Gentle (3:1–2) — Conduct toward rulers and all men. <i>(Titus 3:1–2)</i>', 'Mercy and Regeneration (3:3–7) — What we were and what He did. <i>(Titus 3:3–7)</i>', 'Maintain Good Works (3:8–15) — Final charges. <i>(Titus 3:8–14)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Titus, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what Titus itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Titus simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Titus was written during the overlap from Paul to a younger minister. This Companion shows you how to read its charges in their own setting while drawing out the principles that apply to all believers."))
