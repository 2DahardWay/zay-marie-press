# DRAFT for publisher approval.
BOOK = "Hosea"
TESTAMENT = "Old Testament"
GENRE = "prophets"
SUBTITLE = "Israel the Unfaithful Wife, and the LORD’s Faithful Love"
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
  P('Hosea is “the word of the LORD that came unto Hosea” in the days of the kings of Judah and Jeroboam king of Israel (Hos. 1:1). The prophet’s own marriage becomes a picture of the LORD and Israel. The book speaks of the LORD’s controversy with the land, of Israel called out of Egypt, of days without a king, of a return “in the latter days,” and of healing and love freely given (Hos. 3:4–5; 4:1; 11:1; 14:4).'),
  BOX("Program Identity:", 'This book belongs entirely to the Prophecy Program, where the LORD speaks to the children of Israel and to Ephraim about their unfaithfulness, their judgment and their return (Hos. 1:10; 3:5; 4:1; 14:1).'))

S(2, "Narrative Flow of Hosea",
  H('Movement 1 — The Prophet’s Marriage and the Children (Chs. 1–3)'),
  P('Hosea’s family speaks of Israel’s state, the LORD promises to betroth her for ever, and Israel is to abide many days without a king (Hos. 1:10; 2:19–20; 3:4–5).'),
  H('Movement 2 — The Controversy With the Land (Chs. 4–8)'),
  P('The LORD pleads with Israel for lack of knowledge and truth (Hos. 4:1, 6; 5:15).'),
  H('Movement 3 — Judgment and Mercy (Chs. 9–11)'),
  P('Ephraim is judged, yet the LORD asks how He can give him up (Hos. 6:6; 11:1, 8–9).'),
  H('Movement 4 — Redemption Promised (Ch. 13)'),
  P('The LORD will ransom from the power of the grave (Hos. 13:14).'),
  H('Movement 5 — Return and Healing (Ch. 14)'),
  P('Israel is told to return, and the LORD promises to heal their backsliding (Hos. 14:1, 4, 9).'))

S(3, "Prophecy-Program Themes in Hosea",
  H('1. A Numberless Israel'),
  P('“The number of the children of Israel shall be as the sand of the sea” (Hos. 1:10).'),
  H('2. Betrothed for Ever'),
  P('“I will betroth thee unto me for ever” (Hos. 2:19).'),
  H('3. Days Without a King'),
  P('“The children of Israel shall abide many days without a king, and without a prince, and without a sacrifice” (Hos. 3:4).'),
  H('4. David Their King'),
  P('“Afterward shall the children of Israel return, and seek the LORD their God, and David their king” (Hos. 3:5).'),
  H('5. Lack of Knowledge'),
  P('“My people are destroyed for lack of knowledge” (Hos. 4:6).'),
  H('6. Out of Egypt'),
  P('“When Israel was a child, then I loved him, and called my son out of Egypt” (Hos. 11:1).'),
  H('7. Love Freely Given'),
  P('“I will heal their backsliding, I will love them freely” (Hos. 14:4).'))

S(4, "Christ in Hosea: The Prophetic Trajectory",
  H('1. Called Out of Egypt'),
  P('“Called my son out of Egypt” (Hos. 11:1) is quoted in the Gospel of Matthew (Matt. 2:15).'),
  H('2. Mercy Not Sacrifice'),
  P('“I desired mercy, and not sacrifice” (Hos. 6:6) is quoted by the Lord (Matt. 9:13; 12:7).'),
  H('3. Ransomed From the Grave'),
  P('“I will ransom them from the power of the grave” (Hos. 13:14); Paul’s words in 1 Corinthians 15:55 are reported as written beside it.'))

S(5, "Israel’s Identity in Hosea",
  P("Hosea reinforces Israel’s:"),
  L('the children of Israel as the covenant people addressed (Hos. 1:10; 4:1)', 'the LORD’s betrothal of Israel for ever (Hos. 2:19)', 'days without king, sacrifice or image, and a return in the latter days (Hos. 3:4–5)', 'the LORD’s controversy with the land and Ephraim (Hos. 4:1; 11:8)'),
  P("All content belongs exclusively to the Prophecy Program."))

S(6, "Body-of-Christ Distinctions",
  P("Hosea does not teach:"),
  L("Body-of-Christ identity", "heavenly inheritance", "Pauline doctrine", "Mystery revelation", "Spirit baptism into one Body", "non-covenantal standing", "church worship structure"),
  P('Its marriage figure, its judgment and its return belong exclusively to Israel; its words on mercy and the ways of the LORD are also given to all who hear them.'))

S(7, "Program-Specific Truths Table",
  TBL(["Category", "Truth Revealed in Hosea", "Program Identity", "Scripture"], [
    ['A Numberless Israel', '“the number of the children of Israel shall be as the sand of the sea.”', ISR, 'Hos. 1:10'],
    ['Betrothed for Ever', '“I will betroth thee unto me for ever.”', ISR, 'Hos. 2:19'],
    ['Days Without a King', '“the children of Israel shall abide many days without a king, and without a prince, and without a sacrifice.”', ISR, 'Hos. 3:4'],
    ['The Latter Days', '“Afterward shall the children of Israel return, and seek the LORD their God, and David their king.”', ISR, 'Hos. 3:5'],
    ['The Controversy', '“the LORD hath a controversy with the inhabitants of the land.”', ISR, 'Hos. 4:1'],
    ['Lack of Knowledge', '“My people are destroyed for lack of knowledge.”', ISR, 'Hos. 4:6'],
    ['Seeking His Face', '“till they acknowledge their offence, and seek my face.”', ISR, 'Hos. 5:15'],
    ['The Son Out of Egypt', '“When Israel was a child, then I loved him, and called my son out of Egypt.”', ISR, 'Hos. 11:1'],
    ['Ransom From the Grave', '“I will ransom them from the power of the grave.”', ISR, 'Hos. 13:14'],
    ['Return, O Israel', '“O Israel, return unto the LORD thy God.”', ISR, 'Hos. 14:1'],
    ['Healed and Loved', '“I will heal their backsliding, I will love them freely.”', ISR, 'Hos. 14:4'],
  ], [20, 34, 26, 20]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ['Mercy and Knowledge', '“I desired mercy, and not sacrifice; and the knowledge of God more than burnt offerings.”', 'Hos. 6:6'],
    ['God and Not Man', '“I am God, and not man; the Holy One in the midst of thee.”', 'Hos. 11:9'],
    ['The Ways of the LORD', '“the ways of the LORD are right, and the just shall walk in them.”', 'Hos. 14:9'],
  ], [28, 48, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s covenant betrothal, king or land; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom. The Body of Christ should:'),
  OL('<b>Desire mercy</b> — The LORD desired mercy and the knowledge of God (Hos. 6:6).', '<b>Know He is God and not man</b> — The Holy One in the midst (Hos. 11:9).', '<b>Walk in His right ways</b> — The just shall walk in them (Hos. 14:9).'))

S(10, "Teaching Outline for Hosea",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR('The Prophet’s Marriage (Chs. 1–3) — Betrothed for ever. <i>(Hos. 1:10; 2:19; 3:4–5)</i>', 'The Controversy With the Land (Chs. 4–8) — Lack of knowledge. <i>(Hos. 4:1, 6; 5:15)</i>', 'Judgment and Mercy (Chs. 9–11) — Out of Egypt. <i>(Hos. 6:6; 11:1, 9)</i>', 'Redemption Promised (Ch. 13) — Ransom from the grave. <i>(Hos. 13:14)</i>', 'Return and Healing (Ch. 14) — Loved freely. <i>(Hos. 14:1, 4, 9)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Hosea, helping you see both the prophetic structure of the book and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and universal truths deepen your understanding. The Program-Safe Applications will guide your heart toward repentance, knowledge of God, and trust in His mercy without confusing Israel’s covenant commands with the Body of Christ’s calling today."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Hosea simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, prophecy-program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the tables to help your group distinguish Israel’s covenant identity from universal principles, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap Theology Series, Hosea stands firmly in Israel’s covenant story, yet it still reveals universal truths that shape Christian character today. This Companion shows you how to honor the book’s prophetic context while drawing out the timeless principles that apply to all believers in every age."))
