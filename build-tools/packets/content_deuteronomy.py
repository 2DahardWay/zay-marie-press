# DRAFT for publisher approval.
BOOK = "Deuteronomy"
TESTAMENT = "Old Testament"
GENRE = "law"
SUBTITLE = "Hear, O Israel: Covenant Renewed at the Edge of the Land"
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
  P('Deuteronomy is the words Moses spoke “unto all Israel” on the plains beside Jordan (Deut. 1:1). He recalls the way from Horeb, restates the law, sets before the people the blessing and the curse, speaks of the scattering and the gathering, and appoints Joshua before his song and blessing close the book (Deut. 5:2; 11:26; 30:3; 31:6; 32:4).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where Israel is a holy people chosen by the LORD, bound to Him by covenant, and promised the land (Deut. 7:6; 30:5).'))

S(2, "Narrative Flow of Deuteronomy",
  H("Movement 1 — Moses Looks Back (Chs. 1–4)"),
  P("Moses recalls the journey from Horeb and calls Israel to hear the statutes (Deut. 1:1; 4:39)."),
  H("Movement 2 — The Law Restated (Chs. 5–11)"),
  P("The covenant made in Horeb is rehearsed, and Israel is told to love the LORD and to remember what He has done (Deut. 5:2; 6:4–5; 7:6–9; 8:3)."),
  H("Movement 3 — The Statutes and the Place (Chs. 12–26)"),
  P("Laws for worship at the place the LORD shall choose, for judges, kings, prophets and daily life are given (Deut. 12:5; 18:15)."),
  H("Movement 4 — Blessing and Curse (Chs. 27–30)"),
  P("The blessings and curses are set out, and Israel is told of scattering and of a gathering back into the land (Deut. 28:1; 29:29; 30:3, 5–6, 19)."),
  H("Movement 5 — Joshua, the Song, and the Blessing (Chs. 31–34)"),
  P("Joshua is charged, Moses sings, blesses the tribes, and dies on the mount (Deut. 31:6; 32:4)."))

S(3, "Prophecy-Program Themes in Deuteronomy",
  H("1. One LORD"),
  P("“Hear, O Israel: The LORD our God is one LORD” (Deut. 6:4)."),
  H("2. A Holy People Chosen"),
  P("“For thou art an holy people unto the LORD thy God: the LORD thy God hath chosen thee to be a special people unto himself” (Deut. 7:6)."),
  H("3. The Covenant Kept"),
  P("“The LORD thy God, he is God, the faithful God, which keepeth covenant and mercy with them that love him and keep his commandments to a thousand generations” (Deut. 7:9)."),
  H("4. A Prophet like Moses"),
  P("“The LORD thy God will raise up unto thee a Prophet from the midst of thee, of thy brethren, like unto me; unto him ye shall hearken” (Deut. 18:15)."),
  H("5. Blessing and Curse"),
  P("“Behold, I set before you this day a blessing and a curse” (Deut. 11:26)."),
  H("6. Scattering and Gathering"),
  P("“The LORD thy God will turn thy captivity, and have compassion upon thee, and will return and gather thee from all the nations” (Deut. 30:3)."),
  H("7. The Land Possessed"),
  P("“The LORD thy God will bring thee into the land which thy fathers possessed, and thou shalt possess it” (Deut. 30:5)."))

S(4, "Christ in Deuteronomy: The Prophetic Trajectory",
  H("1. The Prophet like Moses"),
  P("The promise of a Prophet “like unto me” is quoted in the New Testament (Deut. 18:15; Acts 3:22–23)."),
  H("2. The Word that Gives Life"),
  P("“Man doth not live by bread only, but by every word that proceedeth out of the mouth of the LORD doth man live” (Deut. 8:3). The Lord quotes it when tempted (Matt. 4:4)."),
  H("3. The Great Commandment"),
  P("“Thou shalt love the LORD thy God with all thine heart” (Deut. 6:5) is the commandment the Lord names first (Matt. 22:37–38)."),
  H("4. The Circumcised Heart"),
  P("“The LORD thy God will circumcise thine heart, and the heart of thy seed” (Deut. 30:6) belongs to Israel’s promised restoration."))

S(5, "Israel’s Identity in Deuteronomy",
  P("Deuteronomy reinforces Israel’s:"),
  L("covenant made in Horeb (Deut. 5:2)", "standing as a holy and chosen people (Deut. 7:6)", "calling to love the LORD (Deut. 6:4–5)", "place of worship chosen by the LORD (Deut. 12:5)", "blessing, curse, scattering and gathering (Deut. 11:26; 30:3)", "promise of the land (Deut. 30:5)"),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Deuteronomy does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P("Its covenant, statutes, blessings, curses, place of worship and land promise belong exclusively to Israel."))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Deuteronomy", "Program Identity", "Scripture"], [
    ["The Covenant in Horeb", "“The LORD our God made a covenant with us in Horeb.”", ISR, "Deut. 5:2"],
    ["Hear, O Israel", "“Hear, O Israel: The LORD our God is one LORD.”", ISR, "Deut. 6:4"],
    ["A Holy People", "“thou art an holy people unto the LORD thy God.”", ISR, "Deut. 7:6"],
    ["Chosen Because He Loved", "“because the LORD loved you, and because he would keep the oath which he had sworn unto your fathers.”", ISR, "Deut. 7:8"],
    ["The Faithful God", "“which keepeth covenant and mercy with them that love him.”", ISR, "Deut. 7:9"],
    ["Blessing and Curse", "“I set before you this day a blessing and a curse.”", ISR, "Deut. 11:26"],
    ["The Place Chosen", "“the place which the LORD your God shall choose out of all your tribes to put his name there.”", ISR, "Deut. 12:5"],
    ["A Prophet like Moses", "“a Prophet from the midst of thee, of thy brethren, like unto me.”", ISR, "Deut. 18:15"],
    ["The Turning of Captivity", "“will turn thy captivity, and have compassion upon thee.”", ISR, "Deut. 30:3"],
    ["The Land Possessed", "“thou shalt possess it.”", ISR, "Deut. 30:5"],
    ["The Circumcised Heart", "“will circumcise thine heart, and the heart of thy seed.”", ISR, "Deut. 30:6"],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["The LORD Alone Is God", "“the LORD he is God in heaven above, and upon the earth beneath: there is none else.”", "Deut. 4:39"],
    ["Man Lives by His Word", "“man doth not live by bread only, but by every word that proceedeth out of the mouth of the LORD doth man live.”", "Deut. 8:3"],
    ["God of Gods", "“the LORD your God is God of gods, and Lord of lords, a great God.”", "Deut. 10:17"],
    ["Revealed Things", "“The secret things belong unto the LORD our God.”", "Deut. 29:29"],
    ["His Presence", "“the LORD thy God, he it is that doth go with thee; he will not fail thee, nor forsake thee.”", "Deut. 31:6"],
    ["The Rock", "“He is the Rock, his work is perfect: for all his ways are judgment.”", "Deut. 32:4"],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s statutes, blessings or land promise; they are timeless truths rooted in God’s character."),
  P("Drawn only from universal truths, never from Israel’s covenant, statutes or land. The Body of Christ should:"),
  OL("<b>Know that He alone is God</b> — There is none else (Deut. 4:39).",
     "<b>Live by His word</b> — Every word that proceedeth from His mouth (Deut. 8:3).",
     "<b>Revere His greatness</b> — God of gods and Lord of lords (Deut. 10:17).",
     "<b>Rest in what is revealed</b> — The secret things are His (Deut. 29:29).",
     "<b>Take courage in His presence</b> — He will not fail nor forsake (Deut. 31:6).",
     "<b>Trust the Rock</b> — His work is perfect (Deut. 32:4)."))

S(10, "Teaching Outline for Deuteronomy",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Moses Looks Back (Chs. 1–4) — The way from Horeb. <i>(Deut. 1:1; 4:39)</i>",
     "The Law Restated (Chs. 5–11) — Love the LORD. <i>(Deut. 5:2; 6:4–5; 7:6–9; 8:3)</i>",
     "The Statutes and the Place (Chs. 12–26) — Worship and the Prophet. <i>(Deut. 12:5; 18:15)</i>",
     "Blessing and Curse (Chs. 27–28) — The covenant terms. <i>(Deut. 11:26; 28:1)</i>",
     "Scattering and Gathering (Chs. 29–30) — The return promised. <i>(Deut. 29:29; 30:3, 5–6, 19)</i>",
     "Joshua Charged (Ch. 31) — He will not fail thee. <i>(Deut. 31:6)</i>",
     "The Song of Moses (Chs. 32–34) — The Rock. <i>(Deut. 32:4)</i>"))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Deuteronomy, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward devotion, trust, and humility without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Deuteronomy simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Deuteronomy stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
