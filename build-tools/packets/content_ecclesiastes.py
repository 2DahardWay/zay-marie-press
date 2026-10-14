# DRAFT for publisher approval.
BOOK = "Ecclesiastes"
TESTAMENT = "Old Testament"
GENRE = "poetry"
SUBTITLE = "Life Under the Sun, the Gift of God, and the Whole Duty of Man"
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
  P('Ecclesiastes is “The words of the Preacher, the son of David, king in Jerusalem” (Eccl. 1:1). He declares that “all is vanity” (Eccl. 1:2), weighs what is done under the sun, gives a time to every purpose, counsels reverence and gladness in youth, and closes with the conclusion of the whole matter (Eccl. 3:1; 11:9; 12:13–14).'),
  BOX("Program Identity:", 'The book is introduced as the words of the Preacher, the son of David, king over Israel in Jerusalem (Eccl. 1:1, 12). Its reflections on life under the sun are placed in the Universal Truths Table; the verses that name the speaker’s setting are program-labeled.'))

S(2, "Narrative Flow of Ecclesiastes",
  H('Movement 1 — Vanity Under the Sun (Chs. 1–2)'),
  P('The Preacher sets out his search: “Vanity of vanities… all is vanity” (Eccl. 1:2, 9; 2:24).'),
  H('Movement 2 — A Time for Everything (Chs. 3–5)'),
  P('“To every thing there is a season,” and God has made everything beautiful in His time; the Preacher counsels that words before God be few (Eccl. 3:1, 11, 14; 5:2).'),
  H('Movement 3 — The House of Mourning (Chs. 6–8)'),
  P('It is better to go to the house of mourning, and God made man upright (Eccl. 7:2, 29).'),
  H('Movement 4 — Do It with Your Might (Chs. 9–11)'),
  P('Whatever the hand finds to do is to be done with might, and the young are told that God will bring them into judgment (Eccl. 9:10; 11:9).'),
  H('Movement 5 — Remember Thy Creator (Ch. 12)'),
  P('“Remember now thy Creator in the days of thy youth,” and the conclusion of the whole matter is given (Eccl. 12:1, 7, 13–14).'))

S(3, "Prophecy-Program Themes in Ecclesiastes",
  H('1. Vanity'),
  P('“Vanity of vanities, saith the Preacher, vanity of vanities; all is vanity” (Eccl. 1:2).'),
  H('2. Nothing New Under the Sun'),
  P('“There is no new thing under the sun” (Eccl. 1:9).'),
  H('3. A Season for Every Purpose'),
  P('“To every thing there is a season, and a time to every purpose under the heaven” (Eccl. 3:1).'),
  H('4. God’s Works Endure'),
  P('“Whatsoever God doeth, it shall be for ever” (Eccl. 3:14).'),
  H('5. Reverence in Words'),
  P('“Be not rash with thy mouth… let thy words be few” (Eccl. 5:2).'),
  H('6. Judgment Coming'),
  P('“God will bring thee into judgment” (Eccl. 11:9).'),
  H('7. The Whole Duty'),
  P('“Fear God, and keep his commandments: for this is the whole duty of man” (Eccl. 12:13).'))

S(4, "Christ in Ecclesiastes: The Prophetic Trajectory",
  H('1. The Son of David'),
  P('The Preacher is named “the son of David, king in Jerusalem” (Eccl. 1:1); the book is reported as written and no further identification is made.'),
  H('2. The Spirit Returns to God'),
  P('“The spirit shall return unto God who gave it” (Eccl. 12:7).'),
  H('3. Judgment of Every Work'),
  P('“God shall bring every work into judgment” (Eccl. 12:14).'))

S(5, "Israel’s Identity in Ecclesiastes",
  P("Ecclesiastes reinforces Israel’s:"),
  L('the speaker as son of David and king (Eccl. 1:1)', 'the speaker as king over Israel in Jerusalem (Eccl. 1:12)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Ecclesiastes does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its reflections on life under the sun and its closing counsel are given to the reader as wisdom, and none of them is taught as the Body of Christ’s calling.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Ecclesiastes", "Program Identity", "Scripture"], [
    ['The Preacher', '“The words of the Preacher, the son of David, king in Jerusalem.”', ISR, 'Eccl. 1:1'],
    ['King over Israel', '“I the Preacher was king over Israel in Jerusalem.”', ISR, 'Eccl. 1:12'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Vanity of Vanities', '“Vanity of vanities, saith the Preacher, vanity of vanities; all is vanity.”', 'Eccl. 1:2'],
    ['A Time for Everything', '“To every thing there is a season, and a time to every purpose under the heaven.”', 'Eccl. 3:1'],
    ['Eternity in the Heart', '“He hath made every thing beautiful in his time.”', 'Eccl. 3:11'],
    ['God’s Work Endures', '“whatsoever God doeth, it shall be for ever.”', 'Eccl. 3:14'],
    ['Reverent Words', '“let thy words be few.”', 'Eccl. 5:2'],
    ['The House of Mourning', '“It is better to go to the house of mourning, than to go to the house of feasting.”', 'Eccl. 7:2'],
    ['Man Made Upright', '“God hath made man upright; but they have sought out many inventions.”', 'Eccl. 7:29'],
    ['Do It with Might', '“Whatsoever thy hand findeth to do, do it with thy might.”', 'Eccl. 9:10'],
    ['Remember the Creator', '“Remember now thy Creator in the days of thy youth.”', 'Eccl. 12:1'],
    ['The Spirit Returns', '“the spirit shall return unto God who gave it.”', 'Eccl. 12:7'],
    ['The Whole Duty of Man', '“Fear God, and keep his commandments: for this is the whole duty of man.”', 'Eccl. 12:13'],
    ['Every Work Judged', '“God shall bring every work into judgment.”', 'Eccl. 12:14'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant commands or land promises; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Receive life as a gift of God</b> — Eat, drink and enjoy good in labour (Eccl. 2:24).', '<b>Keep reverent words</b> — Let thy words be few (Eccl. 5:2).', '<b>Learn from mourning</b> — The living lay it to heart (Eccl. 7:2).', '<b>Work with all your might</b> — Whatsoever thy hand findeth (Eccl. 9:10).', '<b>Remember the Creator early</b> — In the days of thy youth (Eccl. 12:1).', '<b>Fear God</b> — The whole duty of man (Eccl. 12:13).'))

S(10, "Teaching Outline for Ecclesiastes",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('Vanity Under the Sun (Chs. 1–2) — The Preacher’s search. <i>(Eccl. 1:1–2, 9; 2:24)</i>', 'A Time for Everything (Chs. 3–5) — God’s seasons and reverent words. <i>(Eccl. 3:1, 11, 14; 5:2)</i>', 'The House of Mourning (Chs. 6–8) — Sober counsel. <i>(Eccl. 7:2, 29)</i>', 'Do It with Might (Chs. 9–11) — Work, joy and judgment. <i>(Eccl. 9:10; 11:9)</i>', 'Remember Thy Creator (Ch. 12) — The whole duty of man. <i>(Eccl. 12:1, 7, 13–14)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Ecclesiastes, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward sobriety, gratitude, and the fear of God without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Ecclesiastes simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Ecclesiastes stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
