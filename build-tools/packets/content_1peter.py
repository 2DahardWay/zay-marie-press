# DRAFT for publisher approval.
BOOK = "1 Peter"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "A Living Hope, a Holy Walk, and Grace in the Trial of Faith"
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
  P('1 Peter is a letter from “Peter, an apostle of Jesus Christ, to the strangers scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia” (1 Pet. 1:1). It speaks about a lively hope, an inheritance reserved in heaven, the trial of faith, holy conduct, submission, suffering for well doing, and the care of the elders for the flock. Peter says he has written briefly, “exhorting, and testifying” (1 Pet. 5:12).'),
  BOX("Program Identity:", '1 Peter is addressed to “the strangers scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia” (1 Pet. 1:1). It is read on that audience marker and on the letter’s own setting, in which its readers are called “a chosen generation, a royal priesthood, an holy nation, a peculiar people” (1 Pet. 2:9). This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 1 Peter',
  H('Movement 1 — A Living Hope and a Holy Walk (1:1–2:10)'),
  P('Peter blesses God for a lively hope and an inheritance reserved in heaven, speaks of the trial of faith, calls for holiness and fervent love, and turns to the living stone and the chosen generation (1 Pet. 1:3–9, 13–16, 22; 2:4–10).'),
  H('Movement 2 — Conduct and Submission (2:11–3:12)'),
  P('Peter urges abstaining from fleshly lusts and honest conversation among the Gentiles, submission to every ordinance of man, patience in suffering after the example of Christ, and right conduct for wives, husbands, and all (1 Pet. 2:11–3:12).'),
  H('Movement 3 — Suffering for Righteousness (3:13–4:19)'),
  P('Peter writes of suffering for righteousness’ sake, of Christ who suffered once for sins, of arming with the same mind, of the fiery trial, and of judgment that must begin at the house of God (1 Pet. 3:13–18; 4:1–19).'),
  H('Movement 4 — Elders, Humility, and the Adversary (Ch. 5)'),
  P('Peter exhorts the elders to feed the flock, speaks of the chief Shepherd, calls all to humility and watchfulness against the adversary, and closes with greetings (1 Pet. 5:1–14).'))

S(3, 'Program Themes in 1 Peter',
  H('1. A Living Hope and an Inheritance'),
  P('Peter writes of a lively hope and of “an inheritance incorruptible, and undefiled, and that fadeth not away, reserved in heaven for you” (1 Pet. 1:3–4).'),
  H('2. The Trial of Faith'),
  P('The trial of faith is “much more precious than of gold that perisheth” (1 Pet. 1:7).'),
  H('3. Holy Conduct'),
  P('“Be ye holy; for I am holy” (1 Pet. 1:16).'),
  H('4. A Chosen People'),
  P('The readers “in time past were not a people, but are now the people of God” (1 Pet. 2:10).'),
  H('5. Suffering and Glory'),
  P('The readers are partakers of Christ’s sufferings, “when his glory shall be revealed” (1 Pet. 4:13).'),
  H('6. Humility and Care'),
  P('“Casting all your care upon him; for he careth for you” (1 Pet. 5:7).'))

S(4, 'Christ in 1 Peter',
  H('1. The Risen Lord'),
  P('The readers are begotten again “by the resurrection of Jesus Christ from the dead” (1 Pet. 1:3).'),
  H('2. The Precious Blood'),
  P('They were redeemed with “the precious blood of Christ, as of a lamb without blemish and without spot” (1 Pet. 1:19).'),
  H('3. The Living Stone'),
  P('Christ is “a living stone, disallowed indeed of men, but chosen of God, and precious” (1 Pet. 2:4).'),
  H('4. The Suffering Christ'),
  P('“Christ also suffered for us, leaving us an example,” and “his own self bare our sins in his own body on the tree” (1 Pet. 2:21, 24).'),
  H('5. At the Right Hand of God'),
  P('He “is gone into heaven, and is on the right hand of God” (1 Pet. 3:22).'),
  H('6. The Chief Shepherd'),
  P('“When the chief Shepherd shall appear, ye shall receive a crown of glory that fadeth not away” (1 Pet. 5:4).'))

S(5, 'The Scattered Strangers in 1 Peter',
  P('The letter’s audience markers are read as written:'),
  L('Peter writes “to the strangers scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia” (1 Pet. 1:1).', 'The readers were redeemed from a “vain conversation received by tradition from your fathers” (1 Pet. 1:18).', 'They are called “a chosen generation, a royal priesthood, an holy nation, a peculiar people” (1 Pet. 2:9), who “in time past were not a people, but are now the people of God” (1 Pet. 2:10).', 'The letter speaks of the Gentiles among whom the readers have their conversation (1 Pet. 2:12) and whose will they once wrought (1 Pet. 4:3).', 'Sara is named, and the readers are told “whose daughters ye are” (1 Pet. 3:6).', 'The letter does not use the name the Body of Christ for its readers.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('1 Peter is addressed to the scattered strangers of 1 Peter 1:1. What it commands, warns and promises to them is not addressed to the Body of Christ and does not transfer to it. Truths about God and Christ that the letter states stand as written:'),
  L('Christ’s resurrection, His precious blood, and His suffering (1 Pet. 1:3, 19; 2:21–24)', 'God’s judgment without respect of persons (1 Pet. 1:17)', 'the word of the Lord that endureth for ever (1 Pet. 1:25)', 'God’s resistance of the proud and grace to the humble (1 Pet. 5:5)', 'the God of all grace (1 Pet. 5:10)'),
  P('Its priesthood and nation language belongs to its own readers. It is not addressed to the Body and does not transfer to it.'))

S(7, 'Truths Table: What 1 Peter Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter.'),
  TBL(['Category', 'Truth Revealed in 1 Peter', 'Program Identity', 'Scripture'], [['The Audience', 'The letter is addressed to the strangers scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia.', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 1:1'], ['A Lively Hope', 'Begotten again to a lively hope and to an inheritance reserved in heaven.', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 1:3–4'], ['Holiness', '“Be ye holy; for I am holy.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 1:15–16'], ['A Chosen People', '“a chosen generation, a royal priesthood, an holy nation, a peculiar people.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 2:9–10'], ['Submission', '“Submit yourselves to every ordinance of man for the Lord’s sake.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 2:13–17'], ['Judgment Begins', 'The time is come that “judgment must begin at the house of God.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 4:17'], ['The Elders', '“Feed the flock of God” and the chief Shepherd will give a crown of glory.', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 5:1–4'], ['The Adversary', '“your adversary the devil, as a roaring lion, walketh about, seeking whom he may devour.”', 'Israel / Kingdom / Prophecy Explicit Truth', '1 Pet. 5:8–9']], [18, 40, 24, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['God Judges Without Partiality', 'The Father “without respect of persons judgeth according to every man’s work.”', '1 Pet. 1:17'], ['The Word Endures', '“the word of the Lord endureth for ever.”', '1 Pet. 1:25'], ['Honour All Men', '“Honour all men.”', '1 Pet. 2:17'], ['Seek Peace', '“let him seek peace, and ensue it.”', '1 Pet. 3:11'], ['The Eyes of the Lord', '“the eyes of the Lord are over the righteous.”', '1 Pet. 3:12'], ['Love Covers', '“charity shall cover the multitude of sins.”', '1 Pet. 4:8'], ['A Faithful Creator', 'Those who suffer according to the will of God commit their souls “as unto a faithful Creator.”', '1 Pet. 4:19'], ['Humility and Grace', '“God resisteth the proud, and giveth grace to the humble.”', '1 Pet. 5:5']], [28, 50, 22]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The table in Section 7 marks every row “Israel / Kingdom / Prophecy Explicit Truth” because 1 Peter is read on its own audience markers. The tables separate what the letter says to the readers it names from what holds for all people. The letter’s commands, warnings and promises to its readers are not turned into the Body’s. The applications below draw only on the universal truths in Section 8.'),
  P('Drawn from the universal truths of 1 Peter. Readers can:'),
  OL('<b>Rest in fair judgment</b> — God judges without respect of persons (1 Pet. 1:17).', '<b>Stand on the word</b> — The word of the Lord endures for ever (1 Pet. 1:25).', '<b>Honour all men</b> — Give honour to every person (1 Pet. 2:17).', '<b>Seek peace</b> — Pursue it and keep after it (1 Pet. 3:11).', '<b>Live before the Lord</b> — His eyes are over the righteous (1 Pet. 3:12).', '<b>Love fervently</b> — Love covers a multitude of sins (1 Pet. 4:8).', '<b>Commit your soul</b> — Keep doing well, trusting a faithful Creator (1 Pet. 4:19).', '<b>Humble yourself</b> — God gives grace to the humble (1 Pet. 5:5).'))

S(10, "Teaching Outline for 1 Peter",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('A Living Hope (1:1–12) — Inheritance and the trial of faith. <i>(1 Pet. 1:3–9)</i>', 'A Holy Walk (1:13–2:3) — Holiness, redemption, and fervent love. <i>(1 Pet. 1:13–25)</i>', 'A Chosen Generation (2:4–10) — The living stone and the royal priesthood. <i>(1 Pet. 2:4–10)</i>', 'Conduct and Submission (2:11–3:12) — Among the Gentiles and in the home. <i>(1 Pet. 2:11–25; 3:1–12)</i>', 'Suffering for Righteousness (3:13–4:19) — The fiery trial and the house of God. <i>(1 Pet. 3:13–18; 4:12–19)</i>', 'Elders and Humility (5:1–11) — Feed the flock; resist the adversary. <i>(1 Pet. 5:1–10)</i>', 'Greetings (5:12–14) — Silvanus, and peace to all. <i>(1 Pet. 5:12–14)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 Peter, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on the universal truths 1 Peter itself states, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 Peter simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 1 Peter is read on its own audience marker, the scattered strangers of 1 Peter 1:1. This Companion shows you how to read the letter in its own setting while drawing out the universal truths it states."))
