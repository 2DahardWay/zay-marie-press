# DRAFT for publisher approval.
BOOK = "Genesis"
TESTAMENT = "Old Testament"
GENRE = "law"
SUBTITLE = "Creation, the Promise to Abraham, and the Family Called Israel"
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
  P('Genesis is the book of beginnings. It opens with “In the beginning God created the heaven and the earth” (Gen. 1:1), follows mankind through the fall, the flood and the nations, and then narrows to one man, Abram, called out of his country (Gen. 12:1). From there it follows his seed through Isaac, Jacob and the twelve sons, and closes with Joseph in Egypt and the promise of a return to the land (Gen. 50:24). The book was received by Israel, the nation that came from the family it describes.'),
  BOX("Program Identity:", 'Genesis 1–11 reports creation, the fall, the flood and the nations, before Israel exists. From Genesis 12 the book turns to the covenant promises to Abraham, Isaac and Jacob, which belong to the Prophecy Program and to the nation that came from them (Gen. 12:1–3; 17:7; 32:28).'))

S(2, "Narrative Flow of Genesis",
  H("Movement 1 — Creation, the Fall, the Flood, and the Nations (Chs. 1–11)"),
  P("God creates the heaven and the earth and makes man in His own image, sin enters, the flood comes, and the nations are scattered at Babel (Gen. 1:1; 3:1–24; 6:1–9:17; 11:1–9)."),
  H("Movement 2 — The Call and Covenant of Abraham (Chs. 12–25)"),
  P("The LORD calls Abram, makes a covenant with him, gives circumcision as its sign, and gives Isaac as the son of promise (Gen. 12:1–3; 15:18; 17:7–10; 21:1–5)."),
  H("Movement 3 — Isaac and Jacob (Chs. 25–36)"),
  P("The promise passes to Isaac and then to Jacob, who is renamed Israel (Gen. 26:3–4; 28:13–15; 32:28; 35:10–12)."),
  H("Movement 4 — Joseph and the Descent into Egypt (Chs. 37–50)"),
  P("Joseph is sold into Egypt, raised up, and preserves his family in the famine; Jacob blesses his sons, and Joseph speaks of a return to the land (Gen. 45:5; 49:10; 50:20; 50:24)."))

S(3, "Prophecy-Program Themes in Genesis",
  H("1. Creation"),
  P("The book opens with God as Creator of the heaven and the earth (Gen. 1:1)."),
  H("2. The Call of Abram"),
  P("The LORD says, “I will make of thee a great nation, and I will bless thee, and make thy name great” (Gen. 12:2)."),
  H("3. The Land"),
  P("“Unto thy seed have I given this land, from the river of Egypt unto the great river, the river Euphrates” (Gen. 15:18)."),
  H("4. The Everlasting Covenant"),
  P("“I will establish my covenant between me and thee and thy seed after thee in their generations for an everlasting covenant” (Gen. 17:7)."),
  H("5. The Family Named Israel"),
  P("“Thy name shall be called no more Jacob, but Israel” (Gen. 32:28)."),
  H("6. Judah’s Sceptre"),
  P("“The sceptre shall not depart from Judah, nor a lawgiver from between his feet, until Shiloh come” (Gen. 49:10)."),
  H("7. Preservation"),
  P("“God meant it unto good, to bring to pass, as it is this day, to save much people alive” (Gen. 50:20)."))

S(4, "Christ in Genesis: The Prophetic Trajectory",
  H("1. The Seed of the Woman"),
  P("The LORD says to the serpent, “it shall bruise thy head, and thou shalt bruise his heel” (Gen. 3:15). The verse is reported as written."),
  H("2. The Seed of Abraham"),
  P("“In thy seed shall all the nations of the earth be blessed” (Gen. 22:18). The seed is prophetic fulfillment in Christ (Gal. 3:16)."),
  H("3. The Line of Judah"),
  P("Jacob speaks of a sceptre that shall not depart from Judah “until Shiloh come” (Gen. 49:10). The genealogies of Christ run through Judah (Matt. 1:2–3; Luke 3:33)."),
  H("4. The Blessing to the Families of the Earth"),
  P("The promise to Abram reads, “in thee shall all families of the earth be blessed” (Gen. 12:3), and is repeated to Jacob (Gen. 28:14)."))

S(5, "Israel’s Identity in Genesis",
  P("Genesis shows how the family became Israel:"),
  L("the call of Abram and the promise of a great nation (Gen. 12:1–3)", "the covenant of the land and of circumcision (Gen. 15:18; 17:10)", "the promise carried through Isaac and Jacob (Gen. 26:3–4; 28:14)", "Jacob renamed Israel and the promise of a nation and kings (Gen. 32:28; 35:11)", "the sojourn in Egypt and the promise of a return (Gen. 46:3; 50:24)"),
  P("From Genesis 12 onward the book’s covenant content belongs to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Genesis does not teach:"),
  L("Body-of-Christ identity", "the Mystery revealed through Paul", "heavenly inheritance for the Body", "Spirit baptism into one Body", "the Body’s participation in the Abrahamic covenant"),
  P("The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant."))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Genesis", "Program Identity", "Scripture"], [
    ["The Call of Abram", "“I will make of thee a great nation.”", ISR, "Gen. 12:1–3"],
    ["The Land Promised", "“For all the land which thou seest, to thee will I give it, and to thy seed for ever.”", ISR, "Gen. 13:15"],
    ["The Covenant of the Land", "“Unto thy seed have I given this land.”", ISR, "Gen. 15:18"],
    ["The Everlasting Covenant", "A covenant “between me and thee and thy seed after thee.”", ISR, "Gen. 17:7"],
    ["Circumcision", "“Every man child among you shall be circumcised.”", ISR, "Gen. 17:10"],
    ["The Seed Blessed", "“In thy seed shall all the nations of the earth be blessed.”", ISR, "Gen. 22:18"],
    ["The Promise to Jacob", "“Thy seed shall be as the dust of the earth.”", ISR, "Gen. 28:14"],
    ["Israel Named", "“Thy name shall be called no more Jacob, but Israel.”", ISR, "Gen. 32:28"],
    ["A Nation and Kings", "“A nation and a company of nations shall be of thee, and kings shall come out of thy loins.”", ISR, "Gen. 35:11"],
    ["Judah’s Sceptre", "“The sceptre shall not depart from Judah.”", ISR, "Gen. 49:10"],
    ["The Return Promised", "God “will surely visit you, and bring you out of this land unto the land which he sware to Abraham, to Isaac, and to Jacob.”", ISR, "Gen. 50:24"],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["God the Creator", "“In the beginning God created the heaven and the earth.”", "Gen. 1:1"],
    ["Made in God’s Image", "“God created man in his own image, in the image of God created he him.”", "Gen. 1:27"],
    ["The Penalty of Sin", "“in the day that thou eatest thereof thou shalt surely die.”", "Gen. 2:17"],
    ["The Seasons Continue", "“seedtime and harvest, and cold and heat, and summer and winter, and day and night shall not cease.”", "Gen. 8:22"],
    ["The Worth of Human Life", "“in the image of God made he man.”", "Gen. 9:6"],
    ["Nothing Too Hard", "“Is any thing too hard for the LORD?”", "Gen. 18:14"],
    ["The Righteous Judge", "“Shall not the Judge of all the earth do right?”", "Gen. 18:25"],
    ["God’s Good Purpose", "“God meant it unto good.”", "Gen. 50:20"],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 help us see clearly what belongs to Israel’s covenant line and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not the covenant promises to Abraham, Isaac and Jacob; they are timeless truths rooted in God’s character."),
  P("Drawn only from universal truths, never from the covenant promises to Israel. The Body of Christ should:"),
  OL("<b>Honour the Creator</b> — He made the heaven and the earth (Gen. 1:1).",
     "<b>Value every person</b> — Man is made in God’s image (Gen. 1:27; 9:6).",
     "<b>Take sin seriously</b> — Its penalty is death (Gen. 2:17).",
     "<b>Rely on the faithful order of creation</b> — The seasons do not cease (Gen. 8:22).",
     "<b>Trust the Lord’s power</b> — Nothing is too hard for Him (Gen. 18:14).",
     "<b>Rest in His justice</b> — The Judge of all the earth does right (Gen. 18:25).",
     "<b>Look for His good purpose</b> — God meant it unto good (Gen. 50:20)."))

S(10, "Teaching Outline for Genesis",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Creation and the Fall (Chs. 1–3) — God creates and sin enters. <i>(Gen. 1:1, 27; 2:17)</i>",
     "The Flood and the Nations (Chs. 4–11) — Judgment, covenant with Noah, and Babel. <i>(Gen. 8:22; 9:6)</i>",
     "The Call of Abram (Chs. 12–14) — A great nation and the blessing. <i>(Gen. 12:1–3)</i>",
     "The Covenant (Chs. 15–17) — The land and circumcision. <i>(Gen. 15:18; 17:7, 10)</i>",
     "The Son of Promise (Chs. 18–25) — Isaac, and the question put to the Lord. <i>(Gen. 18:14, 25; 22:18)</i>",
     "Jacob Becomes Israel (Chs. 25–36) — The promise carried forward. <i>(Gen. 28:14; 32:28; 35:11)</i>",
     "Joseph and Judah (Chs. 37–50) — Preservation and the sceptre. <i>(Gen. 49:10; 50:20, 24)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Genesis, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward devotion and trust without confusing Israel’s covenant promises with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Genesis simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Genesis begins with truths for all people and then follows the covenant line that becomes Israel. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless truths that apply to all believers in every age."))
