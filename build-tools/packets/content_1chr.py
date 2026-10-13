# 1 Chronicles: content for the new Bible Book Companion structure (text as supplied by the publisher, 2026-10-13).
BOOK = "1 Chronicles"
TESTAMENT = "Old Testament"
GENRE = "history"
SUBTITLE = "Israel’s Line, David’s Throne, and the House of the LORD"
SECTIONS = []  # filled below as (number, title, blocks)

def S(n, t, *blocks): SECTIONS.append((n, t, list(blocks)))
P = lambda x: ("p", x)
L = lambda *xs: ("ul", list(xs))
H = lambda x: ("h3", x)            # numbered item heading (body-weight bold line)
TBL = lambda head, rows, widths: ("table", head, rows, widths)
OL = lambda *xs: ("ol", list(xs))
OLR = lambda *xs: ("olr", list(xs))
BOX = lambda lead, text: ("box", lead, text)

S(1, "Book Overview (Program-Aware)",
  P("1 Chronicles retells Israel’s history to reaffirm God’s covenant faithfulness, Davidic kingship, and Temple-centered worship for a post-exilic Israel struggling with identity and hope (1 Chr. 16:15–17; 2 Sam. 7:12–16). The audience is returning Jewish exiles in the Persian period (Ezra 1:1–5). The book was written after the Babylonian exile, during the rebuilding of Israel’s national and worship life (2 Chr. 36:22–23)."),
  BOX("Program Identity:", "This book belongs entirely to the Prophecy Program, where Israel is God’s covenant nation with an earthly kingdom destiny (Ex. 19:5–6; Jer. 31:35–37)."))

S(2, "Narrative Flow of 1 Chronicles",
  H("Movement 1 — Genealogies from Adam to the Post-Exilic Community (Chs. 1–9)"),
  P("The genealogies trace Israel’s identity from Adam through the tribes, showing God’s preservation of His covenant people (1 Chr. 1:1; 1 Chr. 9:1–2)."),
  H("Movement 2 — Saul’s Fall and Theological Verdict (Ch. 10)"),
  P("Saul’s fall is attributed to his unfaithfulness and consulting a medium instead of seeking the LORD (1 Chr. 10:13–14)."),
  H("Movement 3 — David’s Rise, Reign, and Military Victories (Chs. 11–20)"),
  P("David is anointed king, secures Jerusalem, brings the Ark, and defeats Israel’s enemies (1 Chr. 11:3; 1 Chr. 15:25–28; 1 Chr. 18:6)."),
  H("Movement 4 — The Davidic Covenant (Ch. 17)"),
  P("God promises David an eternal throne, house, and kingdom (1 Chr. 17:11–14)."),
  H("Movement 5 — Temple Preparation and National Organization (Chs. 21–29)"),
  P("David organizes Levites, priests, musicians, gatekeepers, and gives Solomon the Temple plans (1 Chr. 23:1–5; 1 Chr. 28:11–19). The book ends with David’s prayer, offerings, Solomon’s coronation, and David’s death (1 Chr. 29:10–22)."))

S(3, "Prophecy-Program Themes in 1 Chronicles",
  H("1. Covenant Continuity"),
  P("God preserves Israel’s identity through exile, proving He remembers His covenant forever (1 Chr. 9:1; Ps. 105:8–10)."),
  H("2. Davidic Kingship"),
  P("The eternal throne promised to David is the foundation of Israel’s kingdom hope (1 Chr. 17:12–14; Ps. 89:3–4)."),
  H("3. Temple-Centered Worship"),
  P("Worship is ordered, Levitical, and central to Israel’s prophetic identity (1 Chr. 15:13–15; 1 Chr. 23:28–32)."),
  H("4. National Accountability"),
  P("Saul’s death and David’s census show Israel’s leaders are accountable to God within the covenant framework (1 Chr. 10:13–14; 1 Chr. 21:7–14)."),
  H("5. Prophetic Hope"),
  P("The book reinforces Israel’s expectation of a future kingdom ruled by David’s Son (Isa. 9:6–7; Jer. 23:5–6)."))

S(4, "Christ in 1 Chronicles: The Prophetic Trajectory",
  H("1. The Son of David"),
  P("The Davidic covenant anticipates Christ as Israel’s promised King (Luke 1:32–33; Matt. 1:1)."),
  H("2. The True Temple Builder"),
  P("Solomon builds the earthly Temple; Christ builds the greater Temple in the kingdom (1 Chr. 22:10; John 2:19–21)."),
  H("3. The Perfect Worshiper"),
  P("David’s ordered worship anticipates Christ’s perfect obedience and leadership in Israel’s future kingdom (Ps. 40:7–8; Heb. 10:5–7)."),
  H("4. The Messianic Shepherd-King"),
  P("David’s shepherd role foreshadows Christ as Israel’s Shepherd-King (1 Chr. 11:2; John 10:11)."))

S(5, "Israel’s Identity in 1 Chronicles",
  P("1 Chronicles reinforces Israel’s:"),
  L("covenant nationhood", "earthly kingdom destiny", "Temple worship and Levitical order", "Davidic monarchy", "prophetic timeline"),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("1 Chronicles does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P("Its covenants, promises, commands, and worship patterns belong exclusively to Israel."))

S(7, "Israel-Specific Truths Table (Program-Specific)",
  TBL(["Category", "Truth Revealed in 1 Chronicles", "Program Identity", "Scripture"], [
    ["Covenant Nationhood", "Israel is God’s covenant people with a unique national identity.", "Israel-Specific", "Ex. 19:5–6; 1 Chr. 1–9"],
    ["Davidic Covenant", "God promises David an eternal throne, house, and kingdom.", "Israel-Specific", "1 Chr. 17:11–14"],
    ["Earthly Kingdom Destiny", "Israel’s future includes an earthly kingdom ruled by David’s Son.", "Israel-Specific", "Luke 1:32–33; 1 Chr. 17"],
    ["Temple-Centered Worship", "Worship is Levitical, sacrificial, and centered on the physical Temple.", "Israel-Specific", "1 Chr. 23:28–32"],
    ["Levitical Priesthood", "Only Levites serve in priestly functions; tribal roles are fixed.", "Israel-Specific", "1 Chr. 24:1–19"],
    ["National Accountability", "Israel’s leaders judged by covenant faithfulness.", "Israel-Specific", "1 Chr. 10:13–14"],
    ["Prophetic Timeline", "Israel awaits restoration and Messiah’s earthly reign.", "Israel-Specific", "Acts 3:19–21"],
    ["National Worship Structure", "Gatekeepers, musicians, singers, priests serve nationally.", "Israel-Specific", "1 Chr. 16:4–6"],
    ["Sacrificial System", "Burnt offerings and sacrifices belong to Israel’s covenant worship.", "Israel-Specific", "1 Chr. 29:21"],
    ["Land Promises", "Israel’s inheritance tied to the land.", "Israel-Specific", "Deut. 30:5"],
  ], [24, 41, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["God’s Faithfulness", "God keeps His word across generations.", "Ps. 105:8"],
    ["Wholehearted Devotion", "God calls all people to seek Him sincerely.", "1 Chr. 28:9"],
    ["God’s Holiness", "God’s holiness demands reverence.", "1 Chr. 13:9–10"],
    ["Ordered Worship", "God is worthy of intentional worship.", "1 Chr. 16:29"],
    ["Leadership Accountability", "Leaders must walk faithfully.", "1 Chr. 10:13–14"],
    ["Diligence in God’s Work", "God honors preparation and excellence.", "1 Chr. 22:5"],
    ["Bold Prayer", "God hears sincere prayer.", "1 Chr. 29:10–19"],
    ["Humility and Repentance", "God honors the humble heart.", "1 Chr. 21:16–17"],
  ], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant commands or kingdom requirements; they are timeless principles rooted in God’s character and the posture of the human heart."),
  P("Drawn only from universal truths—never from Israel’s covenants, kingdom promises, or Temple worship. The Body of Christ should:"),
  OL("<b>Trust God’s faithfulness</b> — He keeps His word across generations.",
     "<b>Seek God wholeheartedly</b> — God desires sincere pursuit.",
     "<b>Honor God’s holiness</b> — Approach Him with reverence.",
     "<b>Value ordered worship</b> — Worship intentionally and thoughtfully.",
     "<b>Learn from leadership failures</b> — Faithfulness matters.",
     "<b>Prepare for God’s work</b> — Serve with diligence and excellence.",
     "<b>Pray boldly</b> — Approach God with confidence and gratitude.",
     "<b>Walk in humility</b> — Repentance restores fellowship."))

S(10, "Teaching Outline for 1 Chronicles",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Israel’s Lineage Preserved (Chs. 1–9) — God preserves Israel’s covenant identity through genealogies from Adam to the post-exilic community. <i>(1 Chr. 1:1; 1 Chr. 9:1–2)</i>",
     "Saul’s Fall and David’s Rise (Chs. 10–12) — Saul’s unfaithfulness leads to his downfall; David is established as God’s chosen king. <i>(1 Chr. 10:13–14; 1 Chr. 11:3)</i>",
     "The Ark, Worship, and National Order (Chs. 13–16) — David restores proper worship, brings the Ark to Jerusalem, and establishes Levitical order. <i>(1 Chr. 13:9–10; 1 Chr. 15:25–28; 1 Chr. 16:4–36)</i>",
     "The Davidic Covenant (Ch. 17) — God promises David an eternal house, throne, and kingdom, forming the foundation of Israel’s prophetic hope. <i>(1 Chr. 17:11–14)</i>",
     "David’s Victories and Failures (Chs. 18–21) — David’s military triumphs expand Israel’s borders; his census brings judgment and mercy. <i>(1 Chr. 18:6; 1 Chr. 21:7–14)</i>",
     "Temple Preparation and National Organization (Chs. 22–27) — David prepares materials, assigns Levites, priests, musicians, gatekeepers, and organizes national service for the future Temple. <i>(1 Chr. 22:5; 1 Chr. 23:28–32)</i>",
     "David’s Final Charge, Prayer, and Solomon’s Coronation (Chs. 28–29) — David commissions Solomon, prays over the nation, leads offerings, and Israel anoints Solomon king. <i>(1 Chr. 28:9; 1 Chr. 29:10–22)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read 1 Chronicles, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward devotion, worship, and humility without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching 1 Chronicles simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, 1 Chronicles stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
