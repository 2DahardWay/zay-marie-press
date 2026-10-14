# DRAFT for publisher approval.
BOOK = "Job"
TESTAMENT = "Old Testament"
GENRE = "poetry"
SUBTITLE = "Suffering, Counsel, and the Answer from the Whirlwind"
SECTIONS = []
def S(n, t, *blocks): SECTIONS.append((n, t, list(blocks)))
P = lambda x: ("p", x)
L = lambda *xs: ("ul", list(xs))
H = lambda x: ("h3", x)
TBL = lambda head, rows, widths: ("table", head, rows, widths)
OL = lambda *xs: ("ol", list(xs))
OLR = lambda *xs: ("olr", list(xs))
BOX = lambda lead, text: ("box", lead, text)
ISR = 'Israel / Kingdom / Prophecy Explicit Truth'

S(1, "Book Overview (Program-Aware)",
  P('Job is set “in the land of Uz,” where a man named Job was “perfect and upright, and one that feared God, and eschewed evil” (Job 1:1). The book moves from the scenes before the LORD and Job’s losses, through the long speeches of Job and his friends, to Elihu, to the LORD’s answer “out of the whirlwind,” and to Job’s restoration (Job 1:6, 21; 38:1; 42:10).'),
  BOX("Program Identity:", 'This book is set in the land of Uz. It names no covenant with Israel, no land promise, no tabernacle and no priesthood, and it speaks of God to man as man. Its truths are placed in the Universal Truths Table (Job 1:1).'))

S(2, "Narrative Flow of Job",
  H('Movement 1 — The Scenes and the Losses (Chs. 1–2)'),
  P('The sons of God present themselves before the LORD, Satan comes among them, and Job loses his goods and his children and is struck with sores (Job 1:6, 12, 21; 2:10).'),
  H('Movement 2 — Job and His Friends (Chs. 3–31)'),
  P('Job laments, and Eliphaz, Bildad and Zophar answer in three rounds while Job holds fast to his case (Job 5:17; 9:2; 14:14; 19:25–27).'),
  H('Movement 3 — Elihu (Chs. 32–37)'),
  P('Elihu speaks after the three friends, and says that “God is great, and we know him not” (Job 36:26).'),
  H('Movement 4 — The LORD Answers (Chs. 38–41)'),
  P('The LORD answers Job out of the whirlwind with questions about the earth and its creatures (Job 38:1, 4, 7).'),
  H('Movement 5 — Job Restored (Ch. 42)'),
  P('Job answers the LORD, prays for his friends, and the LORD gives him twice as much as before (Job 42:2, 5–6, 7, 10).'))

S(3, "Themes in Job",
  H('1. The Upright Man'),
  P('“There was a man in the land of Uz, whose name was Job” (Job 1:1).'),
  H('2. The Lord Gave and Took'),
  P('“The LORD gave, and the LORD hath taken away; blessed be the name of the LORD” (Job 1:21).'),
  H('3. The Question of Justice'),
  P('“How should man be just with God?” (Job 9:2).'),
  H('4. A Redeemer Who Lives'),
  P('“I know that my redeemer liveth, and that he shall stand at the latter day upon the earth” (Job 19:25).'),
  H('5. Tried as Gold'),
  P('“When he hath tried me, I shall come forth as gold” (Job 23:10).'),
  H('6. The LORD’s Answer'),
  P('“Where wast thou when I laid the foundations of the earth?” (Job 38:4).'),
  H('7. Seeing God'),
  P('“I have heard of thee by the hearing of the ear: but now mine eye seeth thee” (Job 42:5).'))

S(4, "Christ in Job: The Prophetic Trajectory",
  H('1. The Redeemer'),
  P('Job’s words, “I know that my redeemer liveth” (Job 19:25), are reported as written, and the book does not say how much Job understood by them.'),
  H('2. The Mediator Sought'),
  P('Job’s question, “How should man be just with God?” (Job 9:2), is reported as written.'),
  H('3. The Prayer for the Friends'),
  P('The LORD accepts Job as the one who shall pray for his friends (Job 42:8).'))

S(5, "Israel’s Identity in Job",
  P("Job does not speak of Israel’s covenant, land, tabernacle or priesthood. Its man is set in the land of Uz (Job 1:1), and the book is read as speaking of God to man as man."),
  P("No content in this book is assigned to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Job does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Job does not mention Israel’s covenants, land, priesthood or kingdom, and nothing in it is taught as the Body of Christ’s calling.'))

S(7, "Program-Specific Truths Table",
  P('Job is set in the land of Uz and names no covenant, land, tabernacle or priesthood of Israel (Job 1:1). No verse in the book is labeled as Israel’s program truth. Every truth the book reveals is placed in the Universal Truths Table (Section 8).'))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['God Rules and Gives', '“the LORD gave, and the LORD hath taken away; blessed be the name of the LORD.”', 'Job 1:21'],
    ['Receiving Good and Evil', '“shall we receive good at the hand of God, and shall we not receive evil?”', 'Job 2:10'],
    ['The Question of Man and God', '“how should man be just with God?”', 'Job 9:2'],
    ['Wisdom and Strength', '“With him is wisdom and strength, he hath counsel and understanding.”', 'Job 12:13'],
    ['Hope Beyond Death', '“If a man die, shall he live again?”', 'Job 14:14'],
    ['A Redeemer Lives', '“I know that my redeemer liveth.”', 'Job 19:25'],
    ['Seeing God', '“yet in my flesh shall I see God.”', 'Job 19:26'],
    ['Tried as Gold', '“when he hath tried me, I shall come forth as gold.”', 'Job 23:10'],
    ['God Is Great', '“God is great, and we know him not.”', 'Job 36:26'],
    ['Creation Is His', '“Where wast thou when I laid the foundations of the earth?”', 'Job 38:4'],
    ['Nothing Withheld', '“no thought can be withholden from thee.”', 'Job 42:2'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant commands; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Bless His name in loss</b> — The LORD gave and took away (Job 1:21).', '<b>Receive good and evil from God</b> — Without sin with the lips (Job 2:10).', '<b>Hold hope beyond death</b> — A redeemer liveth (Job 19:25–26).', '<b>Trust the trial</b> — He will bring forth as gold (Job 23:10).', '<b>Remember the Creator</b> — He laid the foundations of the earth (Job 38:4).', '<b>Know God by sight and not by report</b> — Now mine eye seeth thee (Job 42:5).'))

S(10, "Teaching Outline for Job",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Scenes and the Losses (Chs. 1–2) — The upright man and his trial. <i>(Job 1:1, 21; 2:10)</i>', 'Job and His Friends (Chs. 3–31) — Counsel, complaint and hope. <i>(Job 9:2; 14:14; 19:25–26; 23:10)</i>', 'Elihu (Chs. 32–37) — God is great. <i>(Job 36:26)</i>', 'The LORD Answers (Chs. 38–41) — The whirlwind. <i>(Job 38:1, 4)</i>', 'Job Restored (Ch. 42) — Seeing God and the double portion. <i>(Job 42:2, 5–6, 10)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Job, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward trust, humility, and reverence before God without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Job simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Job stands outside Israel’s covenant story, and it reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
