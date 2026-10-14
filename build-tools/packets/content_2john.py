# DRAFT for publisher approval.
BOOK = "2 John"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Truth, Love, and the Doctrine of Christ"
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
  P('2 John is a short letter from “The elder unto the elect lady and her children” (2 John 1). It speaks about truth, love, walking after His commandments, deceivers who confess not that Jesus Christ is come in the flesh, the doctrine of Christ, and whom the house is to receive. It closes with the hope to come and speak face to face (2 John 12).'),
  BOX("Program Identity:", '2 John is addressed to “the elect lady and her children” (2 John 1). It is read on that audience marker and on the letter’s own setting. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 2 John',
  H('Movement 1 — Truth and Love (vv. 1–6)'),
  P('The elder greets the elect lady and her children, rejoices to find them walking in truth, and beseeches that they love one another and walk after His commandments (2 John 1–6).'),
  H('Movement 2 — Deceivers and the Doctrine of Christ (vv. 7–11)'),
  P('The elder writes that many deceivers have entered the world, calls his readers to look to themselves, speaks of abiding in the doctrine of Christ, and says not to receive into the house one who brings not this doctrine (2 John 7–11).'),
  H('Movement 3 — Closing (vv. 12–13)'),
  P('The elder has many things to write but hopes to come and speak face to face, and the children of the elect sister send greetings (2 John 12–13).'))

S(3, 'Program Themes in 2 John',
  H('1. The Truth'),
  P('The elder writes to those “whom I love in the truth” (2 John 1).'),
  H('2. Walking in Truth'),
  P('“I rejoiced greatly that I found of thy children walking in truth” (2 John 4).'),
  H('3. Love'),
  P('The commandment from the beginning is “that we love one another” (2 John 5).'),
  H('4. Deceivers'),
  P('“Many deceivers are entered into the world” (2 John 7).'),
  H('5. A Full Reward'),
  P('“Look to yourselves, that we lose not those things which we have wrought, but that we receive a full reward” (2 John 8).'),
  H('6. The Doctrine of Christ'),
  P('“He that abideth in the doctrine of Christ, he hath both the Father and the Son” (2 John 9).'))

S(4, 'Christ in 2 John',
  H('1. The Son of the Father'),
  P('Grace, mercy, and peace come “from God the Father, and from the Lord Jesus Christ, the Son of the Father” (2 John 3).'),
  H('2. Come in the Flesh'),
  P('The deceivers are those “who confess not that Jesus Christ is come in the flesh” (2 John 7).'),
  H('3. The Doctrine of Christ'),
  P('“Whosoever transgresseth, and abideth not in the doctrine of Christ, hath not God” (2 John 9).'),
  H('4. The Father and the Son'),
  P('“He that abideth in the doctrine of Christ, he hath both the Father and the Son” (2 John 9).'))

S(5, 'Israel and the Body in 2 John',
  P('The letter is a short appeal and names no program:'),
  L('The letter does not name Israel, does not mention a covenant, and does not use the name the Body of Christ.', 'It is addressed to “the elect lady and her children” and sends greetings from “the children of thy elect sister” (2 John 1, 13).', 'It speaks of “many deceivers” and of one who is “a deceiver and an antichrist” (2 John 7), and the letter reports this as written.', 'It does not state how its readers relate to other programs.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('2 John states instructions and truths for its readers:'),
  L('truth and love held together (2 John 1–6)', 'walking after His commandments (2 John 6)', 'the doctrine of Christ (2 John 9)', 'care over whom the house receives (2 John 10–11)'),
  P('It does not give a full account of church order and does not use the name the Body of Christ. It is read on the letter’s own audience markers and setting.'))

S(7, 'Truths Table: What 2 John Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter. “Universal Truth” marks truth that applies to all people, in all time, regardless of program.'),
  TBL(['Category', 'Truth Revealed in 2 John', 'Program Identity', 'Scripture'], [['The Address', 'The elder writes to the elect lady and her children.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 1'], ['Walking in Truth', 'Children found walking in truth, as a commandment from the Father.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 4'], ['Love One Another', 'The commandment from the beginning: that we love one another.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 5–6'], ['Deceivers', 'Many deceivers are entered into the world, who confess not that Jesus Christ is come in the flesh.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 7'], ['A Full Reward', 'Look to yourselves, that we lose not what we have wrought but receive a full reward.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 8'], ['The Doctrine of Christ', 'He that abideth in the doctrine of Christ hath both the Father and the Son.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 9'], ['Receive Him Not', 'If any come and bring not this doctrine, receive him not into your house.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 10–11'], ['Face to Face', 'Many things to write; a hope to come and speak face to face.', 'Israel / Kingdom / Prophecy Explicit Truth', '2 John 12']], [18, 32, 27, 23]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Truth Abides', '“the truth’s sake, which dwelleth in us, and shall be with us for ever.”', '2 John 2'], ['Walking in Truth', '“walking in truth.”', '2 John 4'], ['Love One Another', '“that we love one another.”', '2 John 5'], ['Love Is Walking', '“this is love, that we walk after his commandments.”', '2 John 6'], ['Full Joy', '“that our joy may be full.”', '2 John 12']], [28, 50, 22]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 2 John says to believers, what it reports about deceivers, and what holds for all people. It is a short letter and its instructions are read in that setting.'),
  P('Drawn from 2 John’s instructions and from universal truths. Believers can:'),
  OL('<b>Walk in truth</b> — Let the truth be the way you live (2 John 4).', '<b>Love one another</b> — Hold to the commandment from the beginning (2 John 5).', '<b>Walk after His commandments</b> — Let love take that shape (2 John 6).', '<b>Look to yourselves</b> — Guard what has been wrought (2 John 8).', '<b>Abide in the doctrine of Christ</b> — Stay in what has been taught (2 John 9).', '<b>Take care whom you receive</b> — Weigh what a visitor brings (2 John 10).', '<b>Refuse a share in evil deeds</b> — Do not bid God speed to what is wrong (2 John 11).', '<b>Value face-to-face fellowship</b> — Let joy be made full (2 John 12).'))

S(10, "Teaching Outline for 2 John",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Greeting (vv. 1–3) — The elder, the elect lady, and the truth. <i>(2 John 1–3)</i>', 'Walking in Truth and Love (vv. 4–6) — The commandment from the beginning. <i>(2 John 4–6)</i>', 'Deceivers (v. 7) — Who confess not that Jesus Christ is come in the flesh. <i>(2 John 7)</i>', 'Look to Yourselves (vv. 8–9) — A full reward and the doctrine of Christ. <i>(2 John 8–9)</i>', 'Receive Him Not (vv. 10–11) — The house and the evil deeds. <i>(2 John 10–11)</i>', 'Closing (vv. 12–13) — Face to face and greetings. <i>(2 John 12–13)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 John, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, verse by verse, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw on what 2 John itself says to believers and on the truths it states for all people, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 John simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for a single lesson. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, 2 John is read on the letter’s own audience markers and setting. This Companion shows you how to read the letter in its own setting while drawing out the principles that apply to all believers."))
