# DRAFT for publisher approval.
BOOK = "2 Timothy"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "Hold Fast, Rightly Divide, and Finish the Course"
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
  P('2 Timothy is a letter from “Paul, an apostle of Jesus Christ by the will of God, according to the promise of life which is in Christ Jesus” to “Timothy, my dearly beloved son” (2 Tim. 1:1–2). Paul writes from prison near the end of his course. He urges Timothy to stir up the gift of God, to endure hardness, to hold the form of sound words, and to preach the word.'),
  BOX("Program Identity:", '2 Timothy is Paul’s last letter in the pastoral group, written to a younger minister. It is read for what it says about endurance, doctrine, and Scripture. This reading rests on the letter’s own audience markers and setting.'))

S(2, 'Narrative Flow of 2 Timothy',
  H('Movement 1 — Stir Up the Gift (Ch. 1)'),
  P('Paul gives thanks for Timothy’s faith, tells him not to be ashamed of the testimony, and recalls grace given in Christ Jesus before the world began (2 Tim. 1:3–14).'),
  H('Movement 2 — Endure and Rightly Divide (Ch. 2)'),
  P('Paul calls Timothy to be strong, to commit what he heard to faithful men, to endure as a soldier, and to study to be approved, rightly dividing the word of truth (2 Tim. 2:1–26).'),
  H('Movement 3 — Perilous Times and the Scriptures (Ch. 3)'),
  P('Paul describes perilous times in the last days and urges Timothy to continue in what he has learned from Scripture (2 Tim. 3:1–17).'),
  H('Movement 4 — Preach the Word and Finish the Course (Ch. 4)'),
  P('Paul charges Timothy to preach the word, speaks of his own departure, and says he has kept the faith (2 Tim. 4:1–22).'))

S(3, 'Program Themes in 2 Timothy',
  H('1. Not the Spirit of Fear'),
  P('“God hath not given us the spirit of fear; but of power, and of love, and of a sound mind” (2 Tim. 1:7).'),
  H('2. Faithful Men'),
  P('The things heard are to be committed to faithful men able to teach others (2 Tim. 2:2).'),
  H('3. Rightly Dividing'),
  P('“Study to shew thyself approved unto God, a workman that needeth not to be ashamed, rightly dividing the word of truth” (2 Tim. 2:15).'),
  H('4. All Scripture'),
  P('“All scripture is given by inspiration of God, and is profitable for doctrine” (2 Tim. 3:16).'),
  H('5. Preach the Word'),
  P('Paul charges Timothy to preach the word in season and out of season (2 Tim. 4:2).'))

S(4, 'Christ in 2 Timothy',
  H('1. Christ Jesus Who Abolished Death'),
  P('Our Saviour Jesus Christ has abolished death and brought life and immortality to light through the gospel (2 Tim. 1:10).'),
  H('2. Of the Seed of David'),
  P('“Remember that Jesus Christ of the seed of David was raised from the dead according to my gospel” (2 Tim. 2:8).'),
  H('3. The Sure Foundation'),
  P('“The foundation of God standeth sure” (2 Tim. 2:19).'),
  H('4. The Righteous Judge'),
  P('The Lord, the righteous judge, shall give a crown (2 Tim. 4:8).'),
  H('5. The Lord Stood With Me'),
  P('“The Lord stood with me, and strengthened me” (2 Tim. 4:17).'))

S(5, 'Israel and the Body in 2 Timothy',
  P('The letter speaks of the seed of David and of Paul’s gospel without placing believers inside Israel’s covenants:'),
  L('Paul says Jesus Christ was “of the seed of David” and raised from the dead “according to my gospel” (2 Tim. 2:8). The study reports the text as written.', 'Paul says he endures “for the elect’s sakes” (2 Tim. 2:10) and, “If we suffer, we shall also reign with him” (2 Tim. 2:12). The study reports these as written and builds no wider doctrine on them.', 'The “holy calling” in 2 Timothy 1:9 is reported as written, with grace given “in Christ Jesus before the world began.”', 'The letter does not place believers under any Israelite covenant.'),
  P('This reading rests on the letter’s own audience markers and setting.'))

S(6, "Body-of-Christ Distinctions",
  P('2 Timothy teaches endurance and faithfulness in doctrine:'),
  L('power, love, and a sound mind', 'teaching committed to faithful men', 'rightly dividing the word of truth', 'Scripture profitable for doctrine, reproof, correction, and instruction', 'a finished course and a kept faith'),
  P('It does not state which future events lie behind the “last days” it names beyond what the letter says.'))

S(7, 'Truths Table: What 2 Timothy Says',
  P('Program Identity shows where a truth belongs. “Text Only” marks a passage the companion reports as written, without assigning it to a program.'),
  TBL(['Category', 'Truth Revealed in 2 Timothy', 'Program Identity', 'Scripture'], [['A Holy Calling', 'God saved us and called us according to His own purpose and grace.', 'Addressed to Believers', '2 Tim. 1:9'], ['Death Abolished', 'Christ hath abolished death and brought life to light.', 'Addressed to Believers', '2 Tim. 1:10'], ['Rightly Dividing', 'Study to show thyself approved, rightly dividing the word of truth.', 'Addressed to Believers', '2 Tim. 2:15'], ['Scripture Inspired', 'All scripture is given by inspiration of God.', 'Addressed to Believers', '2 Tim. 3:16'], ['A Finished Course', 'I have fought a good fight, I have finished my course.', 'Addressed to Believers', '2 Tim. 4:7'], ['The Seed of David', 'Jesus Christ of the seed of David raised from the dead.', 'Addressed to Believers (warnings / corrections)', '2 Tim. 2:8'], ['Suffer and Reign', 'If we suffer, we shall also reign with him.', 'Text Only', '2 Tim. 2:12'], ['Last Days', 'In the last days perilous times shall come.', 'Text Only', '2 Tim. 3:1']], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Power, Love, Sound Mind', 'God hath not given us the spirit of fear.', '2 Tim. 1:7'], ['Endure Hardness', 'Endure hardness, as a good soldier of Jesus Christ.', '2 Tim. 2:3'], ['Flee Youthful Lusts', 'Follow righteousness, faith, charity, peace.', '2 Tim. 2:22'], ['Gentle Correction', 'The servant of the Lord must be gentle unto all men.', '2 Tim. 2:24'], ['Inspired Scripture', 'Scripture is profitable for doctrine, reproof, correction, instruction.', '2 Tim. 3:16'], ['Preach the Word', 'Be instant in season, out of season.', '2 Tim. 4:2'], ['Keep the Faith', 'I have kept the faith.', '2 Tim. 4:7'], ['Continue in What You Learned', 'Continue thou in the things which thou hast learned.', '2 Tim. 3:14']], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 separate what 2 Timothy says to believers, what it reports about the seed of David, suffering and reigning, and the last days, and what holds for all people. Its instructions apply to the church addressed. The reports are read in their own setting.'),
  P('Drawn from 2 Timothy’s instructions and from universal truths. The Body of Christ should:'),
  OL('<b>Stir up the gift</b> — Not fear, but power, love, and a sound mind (2 Tim. 1:6–7).', '<b>Hold the form of sound words</b> — Keep what was heard (2 Tim. 1:13).', '<b>Teach faithful men</b> — Pass the teaching on (2 Tim. 2:2).', '<b>Rightly divide the word</b> — Study to be approved (2 Tim. 2:15).', '<b>Be gentle in correction</b> — Instruct opponents in meekness (2 Tim. 2:24–25).', '<b>Continue in Scripture</b> — Hold to what was learned (2 Tim. 3:14–17).', '<b>Preach the word</b> — Reprove, rebuke, exhort (2 Tim. 4:2).', '<b>Finish the course</b> — Keep the faith (2 Tim. 4:7).'))

S(10, "Teaching Outline for 2 Timothy",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Stir Up the Gift (Ch. 1) — Power, love, and a sound mind. <i>(2 Tim. 1:6–14)</i>', 'A Soldier, an Athlete, a Husbandman (2:1–13) — Endurance. <i>(2 Tim. 2:1–13)</i>', 'A Workman Approved (2:14–26) — Rightly dividing and gentle correction. <i>(2 Tim. 2:15, 24–25)</i>', 'Perilous Times (3:1–9) — The last days. <i>(2 Tim. 3:1–9)</i>', 'The Scriptures (3:10–17) — Continue in what was learned. <i>(2 Tim. 3:14–17)</i>', 'Preach the Word (4:1–8) — The charge and the crown. <i>(2 Tim. 4:1–8)</i>', 'Personal Words (4:9–22) — Companions and the Lord who stood with Paul. <i>(2 Tim. 4:9–22)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 2 Timothy, helping you see both what the letter says and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications draw only on what 2 Timothy itself says, so your response stays tied to the text."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 2 Timothy simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group see what the letter states and what it leaves unsaid, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, 2 Timothy was written during the overlap from Paul to a younger minister. This Companion shows you how to read its charges in their own setting while drawing out the principles that apply to all believers."))
