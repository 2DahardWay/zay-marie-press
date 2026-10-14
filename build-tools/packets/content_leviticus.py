# DRAFT for publisher approval.
BOOK = "Leviticus"
TESTAMENT = "Old Testament"
GENRE = "law"
SUBTITLE = "Holiness, Atonement, and the Worship of Israel’s Camp"
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
  P('Leviticus is the LORD’s word to Moses for the children of Israel from the tabernacle. It gives the offerings, the consecration of the priests, the laws of clean and unclean, the day of atonement, the laws of holy living, the feasts and sabbaths, the jubile, and the blessings and curses of the covenant (Lev. 1:1; 16:30; 23:2; 25:10; 26:12).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel is God’s covenant nation, set apart from other people, with a priesthood and a tabernacle for its worship (Lev. 20:26; 26:12).'))

S(2, "Narrative Flow of Leviticus",
  H("Movement 1 — The Offerings (Chs. 1–7)"),
  P("The burnt offering, the meat offering, the peace offering, the sin offering and the trespass offering are set out, each with its own ordinance (Lev. 1:4; 4:1–3)."),
  H("Movement 2 — The Priesthood Consecrated (Chs. 8–10)"),
  P("Aaron and his sons are consecrated, the offerings begin, and Nadab and Abihu are judged (Lev. 8:1–36; 10:3)."),
  H("Movement 3 — Clean and Unclean (Chs. 11–15)"),
  P("Laws on food, birth, leprosy and issues separate the clean from the unclean in Israel’s camp (Lev. 11:44; 13:1–3)."),
  H("Movement 4 — The Day of Atonement (Ch. 16)"),
  P("On one day in the year the priest makes an atonement for the people to cleanse them (Lev. 16:30)."),
  H("Movement 5 — The Holiness Code (Chs. 17–22)"),
  P("Laws on blood, on conduct, on neighbour and stranger, and on the priests call Israel to be holy (Lev. 17:11; 19:2, 18; 20:26)."),
  H("Movement 6 — Feasts, Sabbaths, and the Jubile (Chs. 23–25)"),
  P("The feasts of the LORD, the sabbath, the sabbath of the land and the jubile are given (Lev. 23:2–3; 25:10)."),
  H("Movement 7 — Blessings, Curses, and the Covenant (Chs. 26–27)"),
  P("The LORD sets out blessings for obedience and curses for disobedience, and says He will not break His covenant with them (Lev. 26:12, 44)."))

S(3, "Prophecy-Program Themes in Leviticus",
  H("1. Atonement by Offering"),
  P("The offerer lays his hand on the head of the burnt offering, “and it shall be accepted for him to make atonement for him” (Lev. 1:4)."),
  H("2. The Priesthood"),
  P("Aaron and his sons are consecrated to minister at the tabernacle (Lev. 8:1–36)."),
  H("3. Holiness"),
  P("“Ye shall be holy: for I the LORD your God am holy” (Lev. 19:2)."),
  H("4. The Blood"),
  P("“It is the blood that maketh an atonement for the soul” (Lev. 17:11)."),
  H("5. The Day of Atonement"),
  P("“On that day shall the priest make an atonement for you, to cleanse you” (Lev. 16:30)."),
  H("6. The Feasts of the LORD"),
  P("“Concerning the feasts of the LORD, which ye shall proclaim to be holy convocations, even these are my feasts” (Lev. 23:2)."),
  H("7. The Jubile"),
  P("“Ye shall hallow the fiftieth year, and proclaim liberty throughout all the land” (Lev. 25:10)."))

S(4, "Christ in Leviticus: The Prophetic Trajectory",
  H("1. The Offering"),
  P("The offerings of Leviticus point to the one offering of Christ (Lev. 1:4; Heb. 10:1–10)."),
  H("2. The Great High Priest"),
  P("Aaron’s priesthood anticipates Christ as Israel’s great high priest (Lev. 8:1–12; Heb. 4:14–15)."),
  H("3. The Blood and Atonement"),
  P("The blood that makes atonement for the soul is the pattern the New Testament uses of Christ’s blood (Lev. 17:11; Heb. 9:11–14)."),
  H("4. The Day of Atonement"),
  P("The yearly atonement for Israel is the background of Hebrews’ account of Christ’s entrance (Lev. 16:30; Heb. 9:24–28)."))

S(5, "Israel’s Identity in Leviticus",
  P("Leviticus reinforces Israel’s:"),
  L("covenant separation from other people (Lev. 20:26)", "priesthood and tabernacle worship (Lev. 8:1–12)", "sacrificial system (Lev. 1:4; 17:11)", "feasts, sabbaths and jubile (Lev. 23:2–3; 25:10)", "covenant with its blessings and curses (Lev. 26:12, 44)"),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Leviticus does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P("Its offerings, priesthood, feasts, sabbaths, commands and worship pattern belong exclusively to Israel."))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Leviticus", "Program Identity", "Scripture"], [
    ["The Burnt Offering", "“it shall be accepted for him to make atonement for him.”", ISR, "Lev. 1:4"],
    ["Holy Because He Is Holy", "“ye shall therefore sanctify yourselves, and ye shall be holy; for I am holy.”", ISR, "Lev. 11:44"],
    ["The Day of Atonement", "“on that day shall the priest make an atonement for you, to cleanse you.”", ISR, "Lev. 16:30"],
    ["The Blood", "“the life of the flesh is in the blood: and I have given it to you upon the altar.”", ISR, "Lev. 17:11"],
    ["A Holy Congregation", "“Speak unto all the congregation of the children of Israel, and say unto them, Ye shall be holy.”", ISR, "Lev. 19:2"],
    ["Severed from Other People", "“have severed you from other people, that ye should be mine.”", ISR, "Lev. 20:26"],
    ["The Feasts of the LORD", "“Concerning the feasts of the LORD, which ye shall proclaim to be holy convocations.”", ISR, "Lev. 23:2"],
    ["The Sabbath of Rest", "“the seventh day is the sabbath of rest, an holy convocation.”", ISR, "Lev. 23:3"],
    ["The Jubile", "“it shall be a jubile unto you.”", ISR, "Lev. 25:10"],
    ["The Covenant Held", "“I will walk among you, and will be your God, and ye shall be my people.”", ISR, "Lev. 26:12"],
    ["The Covenant Not Broken", "“I will not cast them away, neither will I abhor them, to destroy them utterly.”", ISR, "Lev. 26:44"],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["The Holiness of God", "“for I the LORD your God am holy.”", "Lev. 19:2"],
    ["Honest Dealing", "“Thou shalt not defraud thy neighbour, neither rob him.”", "Lev. 19:13"],
    ["Love of Neighbour", "“thou shalt love thy neighbour as thyself.”", "Lev. 19:18"],
    ["Honour for the Aged", "“Thou shalt rise up before the hoary head, and honour the face of the old man.”", "Lev. 19:32"],
    ["Just Measures", "“Just balances, just weights, a just ephah, and a just hin, shall ye have.”", "Lev. 19:36"],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s offerings, feasts or covenant commands; they are timeless truths rooted in God’s character and in right dealing among people."),
  P("Drawn only from universal truths, never from Israel’s offerings, priesthood or feasts. The Body of Christ should:"),
  OL("<b>Honour the holiness of God</b> — He is the LORD, and He is holy (Lev. 19:2).",
     "<b>Deal honestly</b> — Do not defraud or rob (Lev. 19:13).",
     "<b>Love your neighbour</b> — As yourself (Lev. 19:18).",
     "<b>Honour the aged</b> — Rise before the hoary head (Lev. 19:32).",
     "<b>Keep just measures</b> — Use just balances and weights (Lev. 19:36)."))

S(10, "Teaching Outline for Leviticus",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("The Offerings (Chs. 1–7) — Atonement at the altar. <i>(Lev. 1:4)</i>",
     "The Priesthood (Chs. 8–10) — Aaron and his sons consecrated. <i>(Lev. 8:1–12; 10:3)</i>",
     "Clean and Unclean (Chs. 11–15) — The camp set apart. <i>(Lev. 11:44)</i>",
     "The Day of Atonement (Ch. 16) — The yearly cleansing. <i>(Lev. 16:30)</i>",
     "The Holiness Code (Chs. 17–22) — Blood, neighbour, stranger and priests. <i>(Lev. 17:11; 19:2, 18; 20:26)</i>",
     "Feasts, Sabbaths, and the Jubile (Chs. 23–25) — The appointed times. <i>(Lev. 23:2–3; 25:10)</i>",
     "Blessings and Curses (Chs. 26–27) — The covenant held. <i>(Lev. 26:12, 44)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Leviticus, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward devotion, worship, and humility without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Leviticus simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Leviticus stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
