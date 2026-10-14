# DRAFT for publisher approval.
BOOK = "Exodus"
TESTAMENT = "Old Testament"
GENRE = "law"
SUBTITLE = "Redeemed from Egypt, the Covenant at Sinai, and the Tabernacle Among Them"
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
  P('Exodus tells how the children of Israel, grown into a nation in Egypt, were brought out under Moses, given the law and the covenant at Sinai, and given the pattern of the tabernacle so that God might “dwell among them” (Ex. 25:8). It moves from bondage and the plagues, to the Passover and the crossing of the sea, to the wilderness and Sinai, to the tabernacle, and closes with the glory of the LORD filling it (Ex. 40:34).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel is God’s covenant nation, redeemed from Egypt, given the law, and set apart as “a kingdom of priests, and an holy nation” (Ex. 19:5–6).'))

S(2, "Narrative Flow of Exodus",
  H("Movement 1 — Bondage and the Call of Moses (Chs. 1–4)"),
  P("Israel is oppressed in Egypt, Moses is called at the burning bush, and the LORD says, “Israel is my son, even my firstborn” (Ex. 3:8; 4:22)."),
  H("Movement 2 — The Plagues, the Passover, and the Sea (Chs. 5–15)"),
  P("Pharaoh refuses, the plagues fall, the Passover is kept, and Israel passes through the sea and sings the song of deliverance (Ex. 12:13; 14:13; 15:2, 18)."),
  H("Movement 3 — From the Sea to Sinai (Chs. 16–18)"),
  P("The LORD provides manna and water on the way, and Israel comes to the wilderness of Sinai (Ex. 16:4; 19:1–2)."),
  H("Movement 4 — The Law and the Covenant (Chs. 19–24)"),
  P("The LORD speaks the ten commandments, gives the judgments, and the people say, “All that the LORD hath said will we do, and be obedient” (Ex. 19:5–6; 20:2–3; 24:7)."),
  H("Movement 5 — The Tabernacle and the Golden Calf (Chs. 25–40)"),
  P("The pattern of the sanctuary and the priesthood is given, the people make the golden calf, the covenant is renewed, and the glory of the LORD fills the tabernacle (Ex. 25:8; 34:6; 40:34)."))

S(3, "Prophecy-Program Themes in Exodus",
  H("1. Israel the Firstborn Son"),
  P("“Thus saith the LORD, Israel is my son, even my firstborn” (Ex. 4:22)."),
  H("2. Redemption by the Passover Blood"),
  P("“When I see the blood, I will pass over you” (Ex. 12:13)."),
  H("3. Deliverance"),
  P("“Stand still, and see the salvation of the LORD” (Ex. 14:13)."),
  H("4. A Kingdom of Priests"),
  P("“Ye shall be unto me a kingdom of priests, and an holy nation” (Ex. 19:6)."),
  H("5. The Covenant at Sinai"),
  P("“All that the LORD hath said will we do, and be obedient” (Ex. 24:7)."),
  H("6. God Dwelling Among Them"),
  P("“Let them make me a sanctuary; that I may dwell among them” (Ex. 25:8)."),
  H("7. The Sign of the Sabbath"),
  P("“It is a sign between me and you throughout your generations” (Ex. 31:13)."))

S(4, "Christ in Exodus: The Prophetic Trajectory",
  H("1. The Passover Lamb"),
  P("The blood on the houses is a token, and the LORD says, “when I see the blood, I will pass over you” (Ex. 12:13). Christ is called our passover (1 Cor. 5:7)."),
  H("2. The Prophet Like Moses"),
  P("Moses is Israel’s mediator at Sinai, and Moses later says the LORD will raise up a Prophet like him (Ex. 20:19; Deut. 18:15; Acts 3:22–23)."),
  H("3. The Tabernacle and the Dwelling"),
  P("The tabernacle is the place where God dwells among Israel, and the glory of the LORD fills it (Ex. 25:8; 40:34; John 1:14)."),
  H("4. The Deliverer"),
  P("Moses brings Israel out of Egypt by the hand of the LORD, and Israel sings, “The LORD shall reign for ever and ever” (Ex. 15:18)."))

S(5, "Israel’s Identity in Exodus",
  P("Exodus reinforces Israel’s:"),
  L("standing as the LORD’s firstborn son (Ex. 4:22)", "redemption from Egypt by the Passover (Ex. 12:13–14)", "covenant at Sinai and its law (Ex. 19:5–6; 24:7)", "tabernacle, priesthood and worship (Ex. 25:8)", "sign of the Sabbath (Ex. 31:13)"),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Exodus does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P("Its covenant, law, commands, sign and worship pattern belong exclusively to Israel."))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Exodus", "Program Identity", "Scripture"], [
    ["Israel the Firstborn", "“Israel is my son, even my firstborn.”", ISR, "Ex. 4:22"],
    ["Deliverance from Egypt", "The LORD comes down “to deliver them out of the hand of the Egyptians.”", ISR, "Ex. 3:8"],
    ["The Passover", "“when I see the blood, I will pass over you.”", ISR, "Ex. 12:13"],
    ["A Memorial for Ever", "“ye shall keep it a feast to the LORD throughout your generations.”", ISR, "Ex. 12:14"],
    ["A Kingdom of Priests", "“ye shall be unto me a kingdom of priests, and an holy nation.”", ISR, "Ex. 19:5–6"],
    ["The Ten Commandments", "“I am the LORD thy God, which have brought thee out of the land of Egypt.”", ISR, "Ex. 20:2–3"],
    ["The Covenant Sworn", "“All that the LORD hath said will we do, and be obedient.”", ISR, "Ex. 24:7"],
    ["The Sanctuary", "“let them make me a sanctuary; that I may dwell among them.”", ISR, "Ex. 25:8"],
    ["The Sabbath Sign", "“it is a sign between me and you throughout your generations.”", ISR, "Ex. 31:13"],
    ["The Glory Fills the Tabernacle", "“the glory of the LORD filled the tabernacle.”", ISR, "Ex. 40:34"],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["The Name of God", "“I AM THAT I AM.”", "Ex. 3:14"],
    ["The Lord Is Salvation", "“The LORD is my strength and song, and he is become my salvation.”", "Ex. 15:2"],
    ["None Like Him", "“Who is like unto thee, O LORD, among the gods? who is like thee, glorious in holiness.”", "Ex. 15:11"],
    ["The Lord Reigns", "“The LORD shall reign for ever and ever.”", "Ex. 15:18"],
    ["Merciful and Gracious", "“The LORD, The LORD God, merciful and gracious, longsuffering, and abundant in goodness and truth.”", "Ex. 34:6"],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant commands or tabernacle worship; they are timeless truths rooted in God’s character."),
  P("Drawn only from universal truths, never from Israel’s law, covenant or worship. The Body of Christ should:"),
  OL("<b>Know who God is</b> — He is I AM (Ex. 3:14).",
     "<b>Rest in His salvation</b> — The LORD is become salvation (Ex. 15:2).",
     "<b>Give Him the glory</b> — None is like Him (Ex. 15:11).",
     "<b>Trust His reign</b> — The LORD shall reign for ever (Ex. 15:18).",
     "<b>Count on His mercy</b> — He is merciful and gracious (Ex. 34:6)."))

S(10, "Teaching Outline for Exodus",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Bondage and the Call of Moses (Chs. 1–4) — The firstborn son. <i>(Ex. 3:8, 14; 4:22)</i>",
     "The Plagues and the Passover (Chs. 5–13) — The blood and the memorial. <i>(Ex. 12:13–14)</i>",
     "The Sea and the Song (Chs. 14–15) — Salvation and reign. <i>(Ex. 14:13; 15:2, 18)</i>",
     "The Wilderness to Sinai (Chs. 16–18) — Provision on the way. <i>(Ex. 16:4)</i>",
     "The Law and the Covenant (Chs. 19–24) — A kingdom of priests. <i>(Ex. 19:5–6; 20:2–3; 24:7)</i>",
     "The Tabernacle (Chs. 25–31) — God dwelling among them and the Sabbath sign. <i>(Ex. 25:8; 31:13)</i>",
     "The Calf, the Renewal, and the Glory (Chs. 32–40) — Mercy and the filled tabernacle. <i>(Ex. 34:6; 40:34)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Exodus, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward devotion, worship, and trust without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Exodus simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Exodus stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
