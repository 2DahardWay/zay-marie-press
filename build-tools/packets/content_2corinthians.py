# DRAFT for publisher approval.
BOOK = "2 Corinthians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Comfort, the Ministry of Reconciliation, and Strength in Weakness"
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
  P('2 Corinthians is a letter from “Paul an apostle of Jesus Christ by the will of God, and Timothy our brother” to “the church of God which is at Corinth, with all the saints which are in all Achaia” (2 Cor. 1:1). Paul writes about his affliction and comfort, his change of plans, the ministry he has received, the collection for the saints, and the defense of his apostleship against those who questioned it.'),
  BOX("Program Identity:", '2 Corinthians is Paul’s letter to a Gentile church during the Acts 9–28 overlap. His ministry belongs to the Mystery Program, and the letter is read with the standing boundary on the new covenant: the covenant belongs to the house of Israel and the house of Judah (Jer. 31:31–34), and the Body benefits from Christ’s blood without being the covenant party.'))

S(2, 'Narrative Flow of 2 Corinthians',
  H('Movement 1 — Comfort in Affliction and the Ministry (Chs. 1–7)'),
  P('Paul blesses the God of all comfort, explains his delay, describes the ministry of the new testament and the glory of Christ, and speaks of the ministry of reconciliation (2 Cor. 1:3–4; 3:6; 4:6–7; 5:17–21).'),
  H('Movement 2 — The Collection for the Saints (Chs. 8–9)'),
  P('Paul sets the Macedonians’ giving beside Christ’s grace and gives directions for a willing gift (2 Cor. 8:1–9; 9:6–8).'),
  H('Movement 3 — The Defense of His Apostleship (Chs. 10–13)'),
  P('Paul answers his critics, recounts his labours, a vision, and a thorn in the flesh, and calls on the Corinthians to examine themselves (2 Cor. 11:2, 23–28; 12:1–10; 13:5).'))

S(3, 'Program Themes in 2 Corinthians',
  H('1. The God of All Comfort'),
  P('God comforts us in all our tribulation so that we may comfort others (2 Cor. 1:3–4).'),
  H('2. The Ministry of the New Testament'),
  P('Paul and his companions are “able ministers of the new testament” (2 Cor. 3:6).'),
  H('3. Treasure in Earthen Vessels'),
  P('The light of the knowledge of God’s glory is held in earthen vessels (2 Cor. 4:6–7).'),
  H('4. A New Creature'),
  P('“If any man be in Christ, he is a new creature” (2 Cor. 5:17).'),
  H('5. Strength in Weakness'),
  P('“My grace is sufficient for thee: for my strength is made perfect in weakness” (2 Cor. 12:9).'))

S(4, 'Christ in 2 Corinthians',
  H('1. The Image of God'),
  P('Christ “is the image of God” (2 Cor. 4:4).'),
  H('2. The One Who Died for All'),
  P('One died for all, and those who live should live unto Him who died for them (2 Cor. 5:14–15).'),
  H('3. Made Sin for Us'),
  P('God made Him “to be sin for us, who knew no sin; that we might be made the righteousness of God in him” (2 Cor. 5:21).'),
  H('4. Rich, Yet Poor'),
  P('Though He was rich, for our sakes He became poor (2 Cor. 8:9).'),
  H('5. The Judgment Seat'),
  P('We must all appear before the judgment seat of Christ (2 Cor. 5:10).'))

S(5, 'Israel and the Body in 2 Corinthians',
  P('The letter uses Israel’s own history and the word “new testament” without placing the Body inside Israel’s covenants:'),
  L('Paul and his companions are “ministers of the new testament” (2 Cor. 3:6). The covenant itself belongs to the house of Israel and the house of Judah (Jer. 31:31–34); Paul’s ministry stays with the Mystery.', 'The Body benefits from Christ’s blood without being a party to Israel’s New Covenant.', 'The reading of Moses and the veil is set beside the turning to the Lord (2 Cor. 3:12–18). The study reports it as written and assigns no program beyond the passage’s own audience.', 'The letter does not make the Body a party to any Israelite covenant.'),
  P('This reading rests on the passage’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('2 Corinthians teaches the Body’s standing and ministry in Christ:'),
  L('comfort in affliction from the God of all comfort', 'a new creature in Christ (2 Cor. 5:17)', 'the ministry of reconciliation committed to Paul and his companions (2 Cor. 5:18–19)', 'the righteousness of God in Christ (2 Cor. 5:21)', 'grace sufficient in weakness (2 Cor. 12:9)'),
  P('It does not place the Body under Israel’s covenants and does not say more about the thorn in the flesh than Paul wrote.'))

S(7, 'Program-Specific Truths Table',
  P('Program Identity shows where a truth belongs. “Text Only” marks a passage the companion reports as written, without assigning it to a program.'),
  TBL(['Category', 'Truth Revealed in 2 Corinthians', 'Program Identity', 'Scripture'], [['The Ministry of Reconciliation', 'God committed to Paul and his companions the word of reconciliation.', 'Body-Specific', '2 Cor. 5:18–19'], ['A New Creature', 'Any man in Christ is a new creature; old things are passed away.', 'Body-Specific', '2 Cor. 5:17'], ['The Righteousness of God', 'Christ was made sin for us that we might be made the righteousness of God in Him.', 'Body-Specific', '2 Cor. 5:21'], ['Walking by Faith', 'We walk by faith, not by sight.', 'Body-Specific', '2 Cor. 5:7'], ['The Judgment Seat of Christ', 'We must all appear before it, that each may receive for what he has done.', 'Body-Specific', '2 Cor. 5:10'], ['Sufficient Grace', 'Christ’s grace is sufficient; His strength is made perfect in weakness.', 'Body-Specific', '2 Cor. 12:9'], ['The New Testament Ministry', 'Paul’s ministry stays with the Mystery; the covenant itself belongs to Israel.', 'Text Only', '2 Cor. 3:6'], ['The Espousal', 'Paul has espoused them to one husband, to present as a chaste virgin to Christ.', 'Text Only', '2 Cor. 11:2']], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['The God of All Comfort', 'God comforts us in all our tribulation.', '2 Cor. 1:3–4'], ['A Cheerful Giver', 'God loveth a cheerful giver.', '2 Cor. 9:7'], ['God’s Power Made Perfect', 'His strength is made perfect in weakness.', '2 Cor. 12:9'], ['Sowing and Reaping', 'He which soweth sparingly shall reap also sparingly.', '2 Cor. 9:6'], ['Seen and Unseen', 'The things which are seen are temporal; the things which are not seen are eternal.', '2 Cor. 4:18'], ['Examine Yourselves', 'Examine yourselves, whether ye be in the faith.', '2 Cor. 13:5'], ['Walk by Faith', 'We walk by faith, not by sight.', '2 Cor. 5:7'], ['Be of One Mind', 'Be perfect, be of good comfort, be of one mind, live in peace.', '2 Cor. 13:11']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 2 Corinthians says to the Body, what it reports about the new covenant and Israel’s history, and what holds for all people. Because the letter is addressed to a church of believers, its instructions apply to the Body directly. They do not make Israel’s new covenant the Body’s.'),
  P('Drawn from 2 Corinthians’ instructions to believers and from universal truths. The Body of Christ should:'),
  OL('<b>Comfort one another</b> — Pass on the comfort received from God (2 Cor. 1:3–4).', '<b>Live as a new creature</b> — Walk in the newness Christ gives (2 Cor. 5:17).', '<b>Be reconciled and speak reconciliation</b> — Receive and share the word of reconciliation (2 Cor. 5:18–20).', '<b>Walk by faith</b> — Trust what is unseen (2 Cor. 5:7; 4:18).', '<b>Give willingly</b> — Give as purposed in the heart, not grudgingly (2 Cor. 9:7).', '<b>Rest in sufficient grace</b> — Boast in weaknesses (2 Cor. 12:9).', '<b>Examine yourselves</b> — Test whether you are in the faith (2 Cor. 13:5).', '<b>Live in peace</b> — Be of one mind and of good comfort (2 Cor. 13:11).'))

S(10, "Teaching Outline for 2 Corinthians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Comfort in Affliction (1:1–2:17) — The God of all comfort and Paul’s change of plans. <i>(2 Cor. 1:3–4)</i>', 'The Ministry and the Glory (Chs. 3–4) — The new testament ministry and treasure in earthen vessels. <i>(2 Cor. 3:6; 4:6–7)</i>', 'Reconciliation (Ch. 5) — A new creature, the judgment seat, and the word of reconciliation. <i>(2 Cor. 5:10, 17–21)</i>', 'Open Hearts (Chs. 6–7) — Paul’s appeal and the godly sorrow that works repentance. <i>(2 Cor. 6:11–13; 7:10)</i>', 'The Collection (Chs. 8–9) — Grace in giving and the cheerful giver. <i>(2 Cor. 8:9; 9:6–8)</i>', 'The Apostle’s Defense (Chs. 10–11) — His labours and his jealousy for the church. <i>(2 Cor. 11:2, 23–28)</i>', 'Weakness and Strength (Chs. 12–13) — The thorn, sufficient grace, and the call to self-examination. <i>(2 Cor. 12:7–10; 13:5)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 Corinthians, helping you see both what the letter says to believers and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what 2 Corinthians itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 Corinthians simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, 2 Corinthians was written during the overlap and shows Paul’s ministry in the Mystery Program. This Companion shows you how to keep the new covenant’s own audience in its place while drawing out the principles that apply to all believers."))
