# DRAFT for publisher approval.
BOOK = "James"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Faith That Works, Wisdom From Above, and Patience Until the Coming"
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
  P('James is a letter from “James, a servant of God and of the Lord Jesus Christ, to the twelve tribes which are scattered abroad” (James 1:1). It speaks about trials, wisdom, doing the word, partiality, faith and works, the tongue, worldliness, and patience until the coming of the Lord. The letter is practical and is full of short commands.'),
  BOX("Program Identity:", 'James is addressed to “the twelve tribes which are scattered abroad” (James 1:1). It is read on that audience marker and on the letter’s own setting. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of James',
  H('Movement 1 — Trials, Wisdom, and Doing the Word (Ch. 1)'),
  P('James calls for joy in trials, asks God for wisdom, and says to be doers of the word and not hearers only (James 1:2–8, 22–25).'),
  H('Movement 2 — Partiality and the Works of Faith (Ch. 2)'),
  P('James forbids respect of persons, sets out that faith without works is dead, and uses Abraham and Rahab as examples (James 2:1–26).'),
  H('Movement 3 — The Tongue and the Wisdom From Above (Ch. 3)'),
  P('James writes of the tongue that no man can tame and of the wisdom that is from above (James 3:1–18).'),
  H('Movement 4 — Worldliness, Pride, and Patience (Chs. 4–5)'),
  P('James calls his readers to submit to God, to resist the devil, to patience until the coming of the Lord, and to prayer, including for the sick (James 4:1–10; 5:7–20).'))

S(3, 'Program Themes in James',
  H('1. Trials and Patience'),
  P('The trying of faith worketh patience (James 1:3).'),
  H('2. Wisdom From God'),
  P('If any lack wisdom, let him ask of God (James 1:5).'),
  H('3. Doers of the Word'),
  P('“Be ye doers of the word, and not hearers only” (James 1:22).'),
  H('4. Faith and Works'),
  P('“Faith without works is dead” (James 2:20, 26).'),
  H('5. Patience Until the Coming'),
  P('“Be patient therefore, brethren, unto the coming of the Lord” (James 5:7).'))

S(4, 'Christ in James',
  H('1. The Lord Jesus Christ'),
  P('James names himself “a servant of God and of the Lord Jesus Christ” (James 1:1).'),
  H('2. The Lord of Glory'),
  P('Faith is spoken of as “the faith of our Lord Jesus Christ, the Lord of glory” (James 2:1).'),
  H('3. The Judge'),
  P('The Judge standeth before the door (James 5:9).'),
  H('4. The Coming of the Lord'),
  P('The coming of the Lord draweth nigh (James 5:8).'),
  H('5. The Name of the Lord'),
  P('Prayer is made in the name of the Lord (James 5:14).'))

S(5, 'The Twelve Tribes in James',
  P('The letter’s audience marker is read as written:'),
  L('James writes “to the twelve tribes which are scattered abroad” (James 1:1). The study reports the text as written.', 'The letter speaks of “your assembly” (James 2:2) in a word that can mean a synagogue, and the study reports it as written.', 'James cites Abraham and Rahab in the course of his argument on faith and works (James 2:21–25). The study reports the argument in the letter’s own setting.', 'The letter does not place believers under any Israelite covenant and does not state how its readers relate to other programs.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('James states instructions that hold for every believer in their own setting:'),
  L('trials borne with patience', 'wisdom asked of God', 'doing the word and not hearing only', 'care for the fatherless and widows (James 1:27)', 'patient waiting and prayer'),
  P('It does not give a full doctrine of justification, and its use of “justified by works” (James 2:21–25) is read in its own setting.'))

S(7, 'Truths Table: What James Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter. “Text Only” marks neutral narrative, greetings, travel notes and background statements.'),
  TBL(['Category', 'Truth Revealed in James', 'Program Identity', 'Scripture'], [['Wisdom', 'If any lack wisdom, let him ask of God.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 1:5'], ['Doers', 'Be doers of the word, and not hearers only.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 1:22'], ['Faith and Works', 'Faith without works is dead.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 2:26'], ['The Tongue', 'No man can tame the tongue.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 3:8'], ['Submit and Resist', 'Submit to God. Resist the devil, and he will flee.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 4:7'], ['The Twelve Tribes', 'The letter is addressed to the twelve tribes scattered abroad.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 1:1'], ['The Coming of the Lord', 'Be patient unto the coming of the Lord.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 5:7–8'], ['Prayer for the Sick', 'The elders pray over the sick, anointing with oil in the name of the Lord.', 'Israel / Kingdom / Prophecy Explicit Truth', 'James 5:14–15']], [20, 36, 26, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Pure Religion', 'Visit the fatherless and widows; keep unspotted from the world.', 'James 1:27'], ['No Respect of Persons', 'Have not the faith with respect of persons.', 'James 2:1'], ['Mercy Triumphs', 'Mercy rejoiceth against judgment.', 'James 2:13'], ['Control the Tongue', 'If any man offend not in word, the same is a perfect man.', 'James 3:2'], ['Humble Yourselves', 'God resisteth the proud, and giveth grace to the humble.', 'James 4:6'], ['The Brevity of Life', 'It is even a vapour, that appeareth for a little time.', 'James 4:14'], ['Do Good', 'To him that knoweth to do good, and doeth it not, to him it is sin.', 'James 4:17'], ['The Prayer of the Righteous', 'The effectual fervent prayer of a righteous man availeth much.', 'James 5:16']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what James says to the readers it names, what it reports about the twelve tribes, the coming of the Lord and prayer for the sick, and what holds for all people. The letter’s audience marker is kept in view.'),
  P('Drawn from James’ commands and from universal truths. Readers can:'),
  OL('<b>Count trials as joy</b> — Let patience have its work (James 1:2–4).', '<b>Ask for wisdom</b> — Ask in faith, nothing wavering (James 1:5–6).', '<b>Do the word</b> — Be doers and not hearers only (James 1:22).', '<b>Show no partiality</b> — Honor the poor and the rich alike (James 2:1–9).', '<b>Guard the tongue</b> — Be slow to speak (James 1:19; 3:2).', '<b>Submit to God</b> — Resist the devil and draw near to God (James 4:7–8).', '<b>Be patient</b> — Wait for the coming of the Lord (James 5:7–8).', '<b>Pray for one another</b> — Confess faults and pray (James 5:16).'))

S(10, "Teaching Outline for James",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Trials and Wisdom (1:1–18) — Joy, patience, and asking God. <i>(James 1:2–8)</i>', 'Doing the Word (1:19–27) — Hearers and doers. <i>(James 1:22–27)</i>', 'No Partiality (2:1–13) — The royal law. <i>(James 2:1–13)</i>', 'Faith and Works (2:14–26) — Abraham and Rahab. <i>(James 2:14–26)</i>', 'The Tongue and Wisdom (Ch. 3) — Taming and wisdom from above. <i>(James 3:1–18)</i>', 'Worldliness and Humility (4:1–17) — Submit to God. <i>(James 4:1–10)</i>', 'Patience and Prayer (Ch. 5) — The coming of the Lord and prayer. <i>(James 5:7–20)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read James, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what James itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching James simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, James is read on its own audience marker, the twelve tribes scattered abroad. This Companion shows you how to read the letter in its own setting while drawing out the principles that apply to all believers."))
