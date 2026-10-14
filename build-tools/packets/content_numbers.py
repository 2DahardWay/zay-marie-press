# DRAFT for publisher approval.
BOOK = "Numbers"
TESTAMENT = "Old Testament"
GENRE = "law"
SUBTITLE = "Wilderness Journey, Unbelief, and the Promise Held"
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
  P('Numbers follows Israel from Sinai toward the land. It numbers the tribes, orders the camp around the tabernacle, and sets the Levites apart. It then records the people’s murmuring, the report of the spies and the refusal to go up, the forty years in the wilderness, the bronze serpent, Balaam’s blessings, the second numbering, Joshua’s appointment, and the borders of the land (Num. 1:1–3; 14:11; 21:8–9; 24:17; 27:18; 34:2).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel is God’s covenant nation on its way to the land of promise, with its tribes, camp, priesthood and inheritance (Num. 6:27; 34:2).'))

S(2, "Narrative Flow of Numbers",
  H("Movement 1 — The Camp at Sinai (Chs. 1–10)"),
  P("The tribes are numbered, the camp is set in order around the tabernacle, the Levites are given to the service, and the priestly blessing is given (Num. 1:1–3; 6:24–27)."),
  H("Movement 2 — Murmuring and the Spies (Chs. 11–14)"),
  P("The people murmur, the spies bring back their report, and the LORD says, “How long will this people provoke me?” (Num. 11:23; 13:30; 14:11, 24)."),
  H("Movement 3 — Rebellion and the Priesthood (Chs. 15–19)"),
  P("Korah’s rebellion is judged, and Aaron’s rod that budded confirms the priesthood (Num. 15:38; 16:1–35; 17:8)."),
  H("Movement 4 — Meribah, the Serpent, and Balaam (Chs. 20–25)"),
  P("Moses and Aaron are barred from the land, the bronze serpent heals the bitten, and Balaam blesses Israel instead of cursing (Num. 20:12; 21:8–9; 23:19; 24:9, 17)."),
  H("Movement 5 — The New Generation and the Borders (Chs. 26–36)"),
  P("A second numbering is taken, Joshua is appointed, and the borders and the inheritance of the land are set out (Num. 27:18; 32:23; 34:2; 35:34)."))

S(3, "Prophecy-Program Themes in Numbers",
  H("1. The Priestly Blessing"),
  P("“The LORD bless thee, and keep thee” (Num. 6:24). “They shall put my name upon the children of Israel; and I will bless them” (Num. 6:27)."),
  H("2. Unbelief at the Border"),
  P("“How long will it be ere they believe me, for all the signs which I have shewed among them?” (Num. 14:11)."),
  H("3. A Faithful Remnant"),
  P("“My servant Caleb, because he had another spirit with him, and hath followed me fully, him will I bring into the land” (Num. 14:24)."),
  H("4. The Bronze Serpent"),
  P("“Every one that is bitten, when he looketh upon it, shall live” (Num. 21:8)."),
  H("5. God Does Not Lie"),
  P("“God is not a man, that he should lie” (Num. 23:19)."),
  H("6. A Star and a Sceptre"),
  P("“There shall come a Star out of Jacob, and a Sceptre shall rise out of Israel” (Num. 24:17)."),
  H("7. The Inheritance"),
  P("“When ye come into the land of Canaan; (this is the land that shall fall unto you for an inheritance)” (Num. 34:2)."))

S(4, "Christ in Numbers: The Prophetic Trajectory",
  H("1. The Lifted Serpent"),
  P("The serpent lifted on a pole is the figure the Lord uses of Himself (Num. 21:8–9; John 3:14–15)."),
  H("2. The Star out of Jacob"),
  P("Balaam’s words are reported as written: a Star out of Jacob and a Sceptre out of Israel (Num. 24:17)."),
  H("3. The Priestly Blessing"),
  P("The blessing of Aaron’s sons puts the LORD’s name upon Israel (Num. 6:24–27)."),
  H("4. The Faithful Servant"),
  P("Caleb followed fully, and Israel’s later Joshua is appointed to lead them in (Num. 14:24; 27:18)."))

S(5, "Israel’s Identity in Numbers",
  P("Numbers reinforces Israel’s:"),
  L("tribal order and camp around the tabernacle (Num. 1:1–3)", "priestly blessing and the LORD’s name upon the children of Israel (Num. 6:24–27)", "inheritance and its borders (Num. 34:2)", "call to take possession of the land (Num. 13:30; 33:53)", "covenant with the God who does not lie (Num. 23:19)"),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Numbers does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P("Its camp order, priesthood, commands, inheritance and journey belong exclusively to Israel."))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Numbers", "Program Identity", "Scripture"], [
    ["The Tribes Numbered", "The LORD speaks to Moses in the tabernacle and the congregation is numbered.", ISR, "Num. 1:1–3"],
    ["The Priestly Blessing", "“The LORD bless thee, and keep thee.”", ISR, "Num. 6:24–26"],
    ["The Name Upon Israel", "“they shall put my name upon the children of Israel; and I will bless them.”", ISR, "Num. 6:27"],
    ["Unbelief", "“How long will it be ere they believe me, for all the signs which I have shewed among them?”", ISR, "Num. 14:11"],
    ["Caleb Followed Fully", "“he had another spirit with him, and hath followed me fully.”", ISR, "Num. 14:24"],
    ["Barred from the Land", "“Because ye believed me not… ye shall not bring this congregation into the land.”", ISR, "Num. 20:12"],
    ["The Bronze Serpent", "“every one that is bitten, when he looketh upon it, shall live.”", ISR, "Num. 21:8–9"],
    ["Balaam’s Blessing", "“Blessed is he that blesseth thee, and cursed is he that curseth thee.”", ISR, "Num. 24:9"],
    ["A Star out of Jacob", "“there shall come a Star out of Jacob, and a Sceptre shall rise out of Israel.”", ISR, "Num. 24:17"],
    ["Joshua Appointed", "“Take thee Joshua the son of Nun, a man in whom is the spirit.”", ISR, "Num. 27:18"],
    ["The Land of Canaan", "“When ye come into the land of Canaan.”", ISR, "Num. 34:2"],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["The Lord’s Hand", "“Is the LORD’s hand waxed short?”", "Num. 11:23"],
    ["Mercy and Justice", "“The LORD is longsuffering, and of great mercy, forgiving iniquity and transgression.”", "Num. 14:18"],
    ["His Glory", "“all the earth shall be filled with the glory of the LORD.”", "Num. 14:21"],
    ["God Does Not Lie", "“God is not a man, that he should lie; neither the son of man, that he should repent.”", "Num. 23:19"],
    ["Sin Finds You Out", "“be sure your sin will find you out.”", "Num. 32:23"],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s camp orders or inheritance; they are timeless truths rooted in God’s character."),
  P("Drawn only from universal truths, never from Israel’s covenant, priesthood or inheritance. The Body of Christ should:"),
  OL("<b>Trust the Lord’s power</b> — His hand is not short (Num. 11:23).",
     "<b>Rest in His mercy</b> — He is longsuffering and forgives (Num. 14:18).",
     "<b>Look for His glory</b> — The earth shall be filled with it (Num. 14:21).",
     "<b>Rely on His word</b> — God does not lie (Num. 23:19).",
     "<b>Take sin seriously</b> — It will find you out (Num. 32:23)."))

S(10, "Teaching Outline for Numbers",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("The Camp at Sinai (Chs. 1–10) — Numbered tribes and the priestly blessing. <i>(Num. 1:1–3; 6:24–27)</i>",
     "Murmuring and the Spies (Chs. 11–14) — Unbelief at the border. <i>(Num. 11:23; 14:11, 24)</i>",
     "Rebellion and the Priesthood (Chs. 15–19) — Korah and Aaron’s rod. <i>(Num. 16:1–35; 17:8)</i>",
     "Meribah and the Serpent (Chs. 20–21) — The barred leaders and the lifted serpent. <i>(Num. 20:12; 21:8–9)</i>",
     "Balaam (Chs. 22–25) — Blessing instead of cursing. <i>(Num. 23:19; 24:9, 17)</i>",
     "The New Generation (Chs. 26–31) — Numbering and Joshua. <i>(Num. 27:18)</i>",
     "The Borders and the Inheritance (Chs. 32–36) — The land set out. <i>(Num. 32:23; 34:2)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Numbers, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward trust, humility, and faithfulness without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Numbers simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Numbers stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
