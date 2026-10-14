# DRAFT for publisher approval.
BOOK = "Hebrews"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "A Better Covenant, a Greater Priest, and a Faith That Endures"
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
  P('Hebrews opens by saying that God, who spoke in time past to the fathers by the prophets, “hath in these last days spoken unto us by his Son” (Heb. 1:1–2). The letter does not name its author. It sets the Son above angels, above Moses, and above the Levitical priesthood, speaks of a better covenant, and calls its readers to hold fast and to run with patience.'),
  BOX("Program Identity:", 'Hebrews is read on its own audience markers and on the covenant it quotes. This reading rests on the letter’s own audience markers and on the covenant it quotes (Jeremiah 31:31–34), which belongs to the house of Israel and the house of Judah, the Body benefiting from Christ’s blood without being the covenant party.'))

S(2, 'Narrative Flow of Hebrews',
  H('Movement 1 — The Son Above the Angels and Moses (Chs. 1–4)'),
  P('The letter sets the Son’s person and work above the angels and above Moses, and speaks of a rest that remains (Heb. 1:1–4; 3:1–6; 4:1–11).'),
  H('Movement 2 — A Great High Priest (Chs. 4:14–7)'),
  P('The letter presents Christ as a great high priest after the order of Melchisedec, able to save to the uttermost those who come unto God by Him (Heb. 4:14–16; 5:5–10; 7:25).'),
  H('Movement 3 — The Better Covenant and the One Sacrifice (Chs. 8–10)'),
  P('The letter quotes the new covenant of Jeremiah 31, sets the tabernacle and its offerings as shadows, and speaks of the one offering of Christ and the entrance into the holiest by His blood (Heb. 8:6–13; 9:11–14, 22; 10:1–22).'),
  H('Movement 4 — Faith, Endurance, and Exhortation (Chs. 10:23–13)'),
  P('The letter calls for holding fast, lists those who lived by faith, points to Jesus the author and finisher of faith, and closes with exhortations (Heb. 10:23–25; 11:1–40; 12:1–2; 13:1–25).'))

S(3, 'Program Themes in Hebrews',
  H('1. The Son Is Greater'),
  P('God has spoken by His Son, the brightness of His glory and the express image of His person (Heb. 1:1–3).'),
  H('2. A Better Covenant'),
  P('The letter speaks of a better covenant established upon better promises (Heb. 8:6).'),
  H('3. One Offering'),
  P('Christ was offered once to bear the sins of many (Heb. 9:28; 10:10–14).'),
  H('4. Hold Fast'),
  P('The readers are urged to hold fast the profession of faith without wavering (Heb. 10:23).'),
  H('5. Faith'),
  P('“Now faith is the substance of things hoped for, the evidence of things not seen” (Heb. 11:1).'))

S(4, 'Christ in Hebrews',
  H('1. The Son and Heir'),
  P('The Son is appointed heir of all things and upholds all things by the word of His power (Heb. 1:2–3).'),
  H('2. Made Lower, Crowned'),
  P('Jesus was made a little lower than the angels for the suffering of death, that He should taste death for every man (Heb. 2:9).'),
  H('3. A Merciful and Faithful High Priest'),
  P('He is a merciful and faithful high priest in things pertaining to God (Heb. 2:17).'),
  H('4. After the Order of Melchisedec'),
  P('He is a priest for ever after the order of Melchisedec (Heb. 5:6; 7:17).'),
  H('5. The Same Yesterday, Today, Forever'),
  P('“Jesus Christ the same yesterday, and to day, and for ever” (Heb. 13:8).'))

S(5, 'The Covenant in Hebrews',
  P('Hebrews quotes the new covenant and speaks of the blood of the covenant. It is read as written:'),
  L('The letter quotes Jeremiah 31:31–34 in full: “I will make a new covenant with the house of Israel and with the house of Judah” (Heb. 8:8–12). The covenant belongs to the house of Israel and the house of Judah.', 'The Body benefits from Christ’s blood without being the covenant party.', 'The warnings (Heb. 6:4–6; 10:26–31; 12:25) are reported as written, in the letter’s own setting. They are not converted into warnings to the Body.', 'The rest of Hebrews 4 and the faith of Hebrews 11 are reported as written, with no identification beyond the letter’s own words.'),
  P('This reading rests on the letter’s own audience markers and on the covenant it quotes (Jeremiah 31:31–34), which belongs to the house of Israel and the house of Judah, the Body benefiting from Christ’s blood without being the covenant party.'))

S(6, "Body-of-Christ Distinctions",
  P('Hebrews, read in its own setting, still states truths that hold for every believer:'),
  L('Christ’s person, His priesthood, and His one offering', 'access through His blood (Heb. 10:19–22)', 'faith as the way people have pleased God (Heb. 11:6)', 'endurance, brotherly love, and holiness (Heb. 12:1–14; 13:1)', 'grace and mercy at the throne (Heb. 4:16)'),
  P('It does not place the Body inside the new covenant, and it does not make the letter’s warnings the Body’s.'))

S(7, 'Truths Table: What Hebrews Says',
  P('Program Identity shows where a truth belongs. “Israel / Kingdom / Prophecy Explicit Truth” marks a statement, command, warning or instruction addressed to Israel within its covenant and kingdom setting; it is not addressed to the Body of Christ and does not transfer to it. A verse that names Israel as the audience is labeled the same way, because it fixes the program identity of the letter.'),
  TBL(['Category', 'Truth Revealed in Hebrews', 'Program Identity', 'Scripture'], [['The Son’s Person', 'The Son is the brightness of His glory and the express image of His person.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 1:3'], ['The Great High Priest', 'We have a great high priest, Jesus the Son of God.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 4:14'], ['The Better Covenant', 'The new covenant with the house of Israel and the house of Judah.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 8:8–12'], ['One Offering', 'Christ offered once to bear the sins of many.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 9:28'], ['The Warnings', 'The letter’s warnings are reported in its own setting.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 6:4–6; 10:26–31'], ['Faith', 'Without faith it is impossible to please God.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 11:6'], ['Access', 'Boldness to enter the holiest by the blood of Jesus.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 10:19'], ['The Rest', 'There remaineth therefore a rest to the people of God.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Heb. 4:9']], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['The Word Is Living', 'The word of God is quick, and powerful.', 'Heb. 4:12'], ['Grace at the Throne', 'Come boldly unto the throne of grace to obtain mercy.', 'Heb. 4:16'], ['Without Faith', 'Without faith it is impossible to please Him.', 'Heb. 11:6'], ['The Cloud of Witnesses', 'Run with patience the race that is set before us.', 'Heb. 12:1'], ['Looking to Jesus', 'Looking unto Jesus the author and finisher of our faith.', 'Heb. 12:2'], ['Brotherly Love', 'Let brotherly love continue.', 'Heb. 13:1'], ['Contentment', 'Be content with such things as ye have.', 'Heb. 13:5'], ['Praise and Sharing', 'To do good and to communicate forget not.', 'Heb. 13:16']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The table in Section 7 marks every row “Israel / Kingdom / Prophecy Explicit Truth” because Hebrews is read on its own audience markers and on the covenant it quotes. The tables separate what the letter states from what holds for all people. The letter’s exhortations, warnings and the new covenant are set in Israel’s covenant and kingdom setting and are not turned into the Body’s covenant or warnings.'),
  P('Drawn from Hebrews’ exhortations and from universal truths. Believers can:'),
  OL('<b>Hold fast</b> — Keep the profession of faith without wavering (Heb. 10:23).', '<b>Come boldly to grace</b> — Seek mercy and help in time of need (Heb. 4:16).', '<b>Live by faith</b> — Please God as faith has always done (Heb. 11:6).', '<b>Run with patience</b> — Lay aside every weight (Heb. 12:1).', '<b>Look to Jesus</b> — Keep eyes on the author and finisher (Heb. 12:2).', '<b>Pursue peace and holiness</b> — Follow peace with all men (Heb. 12:14).', '<b>Love as brethren</b> — Let brotherly love continue (Heb. 13:1).', '<b>Be content</b> — Be content with what you have (Heb. 13:5).'))

S(10, "Teaching Outline for Hebrews",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Son Speaks (Chs. 1–2) — Above the angels. <i>(Heb. 1:1–3; 2:9)</i>', 'Greater Than Moses (Chs. 3–4) — Faithful and the rest. <i>(Heb. 3:1–6; 4:9)</i>', 'The High Priest (Chs. 5–7) — After the order of Melchisedec. <i>(Heb. 5:5–10; 7:25)</i>', 'The Better Covenant (Ch. 8) — Jeremiah quoted. <i>(Heb. 8:6–13)</i>', 'The Holiest and the One Offering (Chs. 9–10) — Blood and access. <i>(Heb. 9:11–14; 10:19–22)</i>', 'Faith (Ch. 11) — Those who lived by faith. <i>(Heb. 11:1–6)</i>', 'Endure and Love (Chs. 12–13) — Looking to Jesus and brotherly love. <i>(Heb. 12:1–2; 13:1–8)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Hebrews, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what Hebrews itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Hebrews simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Hebrews is read on its own audience markers and on the covenant it quotes. This Companion shows you how to keep Israel’s new covenant in its place while drawing out the principles that apply to all believers."))
