# DRAFT for publisher approval.
BOOK = "Esther"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "The Jews Scattered, the Decree Reversed, and the Feast of Purim"
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
  P('Esther is set in the reign of Ahasuerus over “an hundred and seven and twenty provinces” (Esth. 1:1). Esther, a Jewess brought up by her kinsman Mordecai, becomes queen; Haman seeks to destroy “all the Jews that were throughout the whole kingdom”; the king’s decree is answered by fasting, by Esther’s going in to the king, and by a second decree; and the days of Purim are kept (Esth. 2:7, 17; 3:6; 4:16; 9:26).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel is a people scattered among the nations yet preserved, with Mordecai the Jew and Esther the queen standing among them (Esth. 2:5; 3:8; 10:3).'))

S(2, "Narrative Flow of Esther",
  H('Movement 1 — The Feast and the New Queen (Chs. 1–2)'),
  P('Vashti is set aside, Esther is brought up and made queen, and Mordecai sits at the king’s gate (Esth. 1:1; 2:7, 17).'),
  H('Movement 2 — Haman’s Decree (Chs. 3–4)'),
  P('Haman, offended by Mordecai, obtains a decree against the Jews; Mordecai mourns and sends word to Esther (Esth. 3:6, 13; 4:1, 14).'),
  H('Movement 3 — Esther Goes In (Chs. 4–7)'),
  P('The Jews fast three days, Esther goes in to the king, and Haman is exposed at her banquet (Esth. 4:16; 7:6).'),
  H('Movement 4 — The Decree Reversed (Chs. 8–9)'),
  P('A second decree is sent, the Jews have joy and gladness, and their enemies’ hope is turned (Esth. 8:17; 9:1).'),
  H('Movement 5 — Purim Kept (Chs. 9–10)'),
  P('Mordecai writes to the Jews, the days of Purim are set, and Mordecai is next unto the king (Esth. 9:20, 26; 10:3).'))

S(3, "Prophecy-Program Themes in Esther",
  H('1. A People Scattered'),
  P('Haman speaks of “a certain people scattered abroad and dispersed among the people in all the provinces of thy kingdom” (Esth. 3:8).'),
  H('2. Deliverance from Another Place'),
  P('“Then shall there enlargement and deliverance arise to the Jews from another place” (Esth. 4:14).'),
  H('3. Fasting and Courage'),
  P('“Go, gather together all the Jews that are present in Shushan, and fast ye for me” (Esth. 4:16).'),
  H('4. The Adversary Exposed'),
  P('“The adversary and enemy is this wicked Haman” (Esth. 7:6).'),
  H('5. Sorrow Turned to Joy'),
  P('The Jews “rested from their enemies, and the month which was turned unto them from sorrow to joy” (Esth. 9:22).'),
  H('6. A Memorial in Every Generation'),
  P('“These days should be remembered and kept throughout every generation, every family, every province, and every city” (Esth. 9:28).'),
  H('7. Mordecai Seeking His People’s Good'),
  P('Mordecai was “seeking the wealth of his people, and speaking peace to all his seed” (Esth. 10:3).'))

S(4, "Christ in Esther: The Prophetic Trajectory",
  H('1. The Preserved People'),
  P('The book follows the Jews as a people kept alive in exile, from whom Christ comes after the flesh; the book itself names no such line and is reported as written (Esth. 2:5; 9:28).'),
  H('2. Deliverance and Reversal'),
  P('A sentence of death is turned to joy for the Jews (Esth. 9:22). The book is read as the preservation of Israel and is not applied to the Body.'),
  H('3. The Hidden Hand'),
  P('The book does not name God, and it is reported as written; the deliverance is told in what happened and in Mordecai’s words (Esth. 4:14).'))

S(5, "Israel’s Identity in Esther",
  P("Esther reinforces Israel’s:"),
  L('Jewish identity among the nations (Esth. 2:5; 3:8)', 'Esther and Mordecai as the Jews’ deliverers (Esth. 4:14; 10:3)', 'a decree turned against those who sought their destruction (Esth. 7:6; 9:1)', 'the memorial days of Purim for their seed (Esth. 9:26, 28)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Esther does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its decrees, fasts, memorial days and the Jews’ deliverance belong exclusively to Israel.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Esther", "Program Identity", "Scripture"], [
    ['The Jew in Shushan', '“a certain Jew, whose name was Mordecai, the son of Jair, the son of Shimei, the son of Kish, a Benjamite.”', ISR, 'Esth. 2:5'],
    ['Esther Made Queen', '“the king loved Esther above all the women… and made her queen instead of Vashti.”', ISR, 'Esth. 2:17'],
    ['A People Scattered', '“a certain people scattered abroad and dispersed among the people in all the provinces of thy kingdom.”', ISR, 'Esth. 3:8'],
    ['Deliverance to the Jews', '“then shall there enlargement and deliverance arise to the Jews from another place.”', ISR, 'Esth. 4:14'],
    ['The Fast of the Jews', '“gather together all the Jews that are present in Shushan, and fast ye for me.”', ISR, 'Esth. 4:16'],
    ['The Enemy Named', '“The adversary and enemy is this wicked Haman.”', ISR, 'Esth. 7:6'],
    ['Joy and Gladness', '“the Jews had joy and gladness, a feast and a good day.”', ISR, 'Esth. 8:17'],
    ['Sorrow Turned to Joy', '“the month which was turned unto them from sorrow to joy.”', ISR, 'Esth. 9:22'],
    ['The Days of Purim', '“they called these days Purim after the name of Pur.”', ISR, 'Esth. 9:26'],
    ['Remembered Every Generation', '“these days should be remembered and kept throughout every generation.”', ISR, 'Esth. 9:28'],
    ['Mordecai the Jew', '“Mordecai the Jew was next unto king Ahasuerus, and great among the Jews.”', ISR, 'Esth. 10:3'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Courage in a Hard Hour', '“I also and my maidens will fast likewise; and so will I go in unto the king.”', 'Esth. 4:16'],
    ['Mourning Before God', '“Mordecai rent his clothes, and put on sackcloth with ashes.”', 'Esth. 4:1'],
    ['Speaking Peace', '“seeking the wealth of his people, and speaking peace to all his seed.”', 'Esth. 10:3'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s decrees, fasts or memorial days; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Take courage in a hard hour</b> — Esther goes in at the risk of her life (Esth. 4:16).', '<b>Mourn honestly</b> — Mordecai cries with a loud and bitter cry (Esth. 4:1).', '<b>Seek others’ good</b> — Mordecai speaks peace to all his seed (Esth. 10:3).'))

S(10, "Teaching Outline for Esther",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Feast and the New Queen (Chs. 1–2) — Esther raised up. <i>(Esth. 1:1; 2:7, 17)</i>', 'Haman’s Decree (Chs. 3–4) — A people marked for destruction. <i>(Esth. 3:6, 8; 4:14)</i>', 'Esther Goes In (Chs. 4–7) — The fast and the banquet. <i>(Esth. 4:16; 7:6)</i>', 'The Decree Reversed (Chs. 8–9) — Joy for the Jews. <i>(Esth. 8:17; 9:22)</i>', 'Purim Kept (Chs. 9–10) — The memorial and Mordecai. <i>(Esth. 9:26, 28; 10:3)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Esther, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward devotion, courage, and trust in unseen providence without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Esther simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Esther stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
