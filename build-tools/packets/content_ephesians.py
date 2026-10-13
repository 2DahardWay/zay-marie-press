# Ephesians: DRAFT of the New Testament variant of the Bible Companion structure (for publisher approval).
BOOK = "Ephesians"
TESTAMENT = "New Testament"
GENRE = "letters"
SUBTITLE = "The Mystery, the One Body, and the Walk Worthy of the Calling"
SECTIONS = []
def S(n, t, *blocks): SECTIONS.append((n, t, list(blocks)))
P = lambda x: ("p", x)
L = lambda *xs: ("ul", list(xs))
H = lambda x: ("h3", x)
TBL = lambda head, rows, widths: ("table", head, rows, widths)
OL = lambda *xs: ("ol", list(xs))
OLR = lambda *xs: ("olr", list(xs))
BOX = lambda lead, text: ("box", lead, text)

S(1, "Book Overview (Program-Aware)",
  P("Ephesians is a letter from Paul, “the apostle of Jesus Christ by the will of God,” written as “the prisoner of the Lord” to “the saints which are at Ephesus, and to the faithful in Christ Jesus” (Eph. 1:1; 3:1; 4:1). Its readers are Gentile believers who were once “aliens from the commonwealth of Israel” and are now “in Christ Jesus” (Eph. 2:11–13). Paul writes from imprisonment (Eph. 6:20) to explain the mystery committed to him, the Body’s heavenly position in Christ, and the walk that fits that calling (Eph. 3:1–9; 4:1)."),
  BOX("Program Identity:", "Ephesians belongs to the Mystery Program: the revelation given to Paul concerning the Body of Christ, a calling hid in God from the beginning of the world and made known through Paul’s ministry (Eph. 3:2–9; Rom. 16:25–26)."))

S(2, "Narrative Flow of Ephesians",
  H("Movement 1 — Blessed in Heavenly Places (Ch. 1)"),
  P("Paul blesses God for every spiritual blessing in Christ, chosen “before the foundation of the world,” redeemed, sealed, and given an inheritance, then prays that the readers know the hope of His calling (Eph. 1:3–14, 18–19)."),
  H("Movement 2 — Dead, Made Alive, and Brought Near (Ch. 2)"),
  P("Dead in trespasses, the readers are saved by grace through faith, raised and seated in Christ, and brought near by His blood, with Jew and Gentile made one in one body (Eph. 2:1–10, 13–18)."),
  H("Movement 3 — The Mystery Made Known (Ch. 3)"),
  P("Paul describes the dispensation of the grace of God given to him, the mystery not made known in other ages, and prays that Christ dwell in their hearts by faith (Eph. 3:2–9, 14–19)."),
  H("Movement 4 — One Body and Its Walk (Chs. 4–5)"),
  P("The readers are to walk worthy of their calling, keep the unity of the Spirit, grow through the gifts Christ gave, put off the old man, and walk in love, light, and wisdom (Eph. 4:1–6, 11–16, 22–24; 5:1–2, 8, 15)."),
  H("Movement 5 — The Household and the Armour (5:22–6:24)"),
  P("Paul addresses wives and husbands, children and parents, servants and masters, then calls the readers to stand in the whole armour of God (Eph. 5:22–6:9; 6:10–18)."))

S(3, "Mystery-Program Themes in Ephesians",
  H("1. The Mystery Committed to Paul"),
  P("The mystery was hid in God and made known by revelation to Paul, whose ministry is a stewardship of grace for the Gentiles (Eph. 3:2–5, 9; Col. 1:25–26)."),
  H("2. One New Man, One Body"),
  P("Christ makes Jew and Gentile one in a single new man and reconciles both to God in one body by the cross (Eph. 2:15–16; 3:6)."),
  H("3. Seated in Heavenly Places"),
  P("The Body’s position and blessing are in the heavenlies in Christ, not in earthly kingdom promises (Eph. 1:3; 2:6)."),
  H("4. Grace Through Faith"),
  P("Salvation is the gift of God, by grace through faith, not of works (Eph. 2:8–9)."),
  H("5. Unity and Growth in Christ"),
  P("Christ gives gifts to build the Body into a perfect man, in love, each part working together (Eph. 4:7–16)."))

S(4, "Christ in Ephesians: Fulfillment and Revelation",
  H("1. The Head of the Body"),
  P("God gave Christ to be head over all things to the church, which is His body (Eph. 1:22–23; 5:23)."),
  H("2. The Redeemer by His Blood"),
  P("Redemption through His blood and the forgiveness of sins are according to the riches of His grace (Eph. 1:7; 2:13)."),
  H("3. Our Peace"),
  P("Christ is our peace, who made both one and reconciled them to God by the cross (Eph. 2:14–16)."),
  H("4. The Giver of Gifts"),
  P("The ascended Christ gave gifts to men for the work of the ministry and the edifying of the body (Eph. 4:8–12)."),
  H("5. The Bridegroom Pattern for Marriage"),
  P("Paul sets Christ’s love for the church beside the husband’s love for his wife and calls it a great mystery concerning Christ and the church (Eph. 5:25–32)."))

S(5, "Israel and the Body in Ephesians",
  P("Ephesians mentions Israel to describe where the Gentile readers once stood, not to make them Israel:"),
  L("They were “aliens from the commonwealth of Israel, and strangers from the covenants of promise” (Eph. 2:12).",
    "Christ abolished in His flesh the enmity, “the law of commandments contained in ordinances,” to make in Himself one new man (Eph. 2:14–15).",
    "The Gentiles are “fellowheirs, and of the same body, and partakers of his promise in Christ by the gospel” (Eph. 3:6).",
    "The letter never calls the Body Israel and never places it under Israel’s covenants."),
  P("This reading rests on the letter’s own audience markers and setting."))

S(6, "Body-of-Christ Distinctions",
  P("Ephesians teaches:"),
  L("the Body’s heavenly identity and position in Christ", "the mystery revealed through Paul", "one new man from Jew and Gentile", "standing by grace through faith, apart from works", "the Spirit’s sealing and the unity of the Spirit", "a calling and inheritance in the heavenlies"),
  P("It does not give Israel’s covenant promises, earthly kingdom, Temple worship, or national commands to the Body."))

S(7, "Body-Specific Truths Table (Program-Specific)",
  TBL(["Category", "Truth Revealed in Ephesians", "Program Identity", "Scripture"], [
    ["The Mystery", "A dispensation of grace committed to Paul and hid until revealed to him.", "Body-Specific", "Eph. 3:2–9"],
    ["One Body", "Jew and Gentile are made one body in Christ.", "Body-Specific", "Eph. 2:15–16; 3:6"],
    ["Heavenly Blessing", "Every spiritual blessing is in heavenly places in Christ.", "Body-Specific", "Eph. 1:3"],
    ["Heavenly Seat", "Believers are raised up and made to sit together in heavenly places.", "Body-Specific", "Eph. 2:6"],
    ["Headship of Christ", "Christ is head over all things to the church, His body.", "Body-Specific", "Eph. 1:22–23"],
    ["Sealing of the Spirit", "Believers are sealed with the Holy Spirit of promise.", "Body-Specific", "Eph. 1:13; 4:30"],
    ["Wall Abolished", "The enmity of the law of commandments is abolished for the Body.", "Body-Specific", "Eph. 2:14–15"],
    ["Gifts for the Body", "Christ’s gifts build up the Body to maturity.", "Body-Specific", "Eph. 4:11–13"],
    ["Walk Worthy", "The Body’s conduct flows from its calling.", "Body-Specific", "Eph. 4:1; 5:1–2"],
    ["Unity of the Spirit", "One body, one Spirit, one hope, one Lord, one faith, one baptism.", "Body-Specific", "Eph. 4:3–6"],
  ], [22, 43, 17, 18]))

S(8, "Universal Truths Table (All People, All Time)",
  TBL(["Universal Truth", "Description", "Scripture"], [
    ["God’s Grace", "Salvation is God’s gift, not earned.", "Eph. 2:8–9"],
    ["God’s Love and Mercy", "God is rich in mercy and great in love.", "Eph. 2:4"],
    ["Truth Spoken in Love", "Truth is to be spoken in love.", "Eph. 4:15"],
    ["Honest Speech", "Put away lying and speak truth with your neighbour.", "Eph. 4:25"],
    ["Controlled Anger", "Do not let the sun go down on your wrath.", "Eph. 4:26"],
    ["Kindness and Forgiveness", "Be kind and forgive, as God forgave.", "Eph. 4:32"],
    ["Honor in the Family", "Children are to obey and honor parents.", "Eph. 6:1–3"],
    ["Honest Labor", "Work as unto the Lord, not merely to please men.", "Eph. 6:5–8"],
  ], [30, 46, 24]))

S(9, "Program-Safe Application Grid",
  BOX("Why This Section Exists", "The tables in Sections 7 and 8 separate what Ephesians reveals about the Body’s calling from truths that hold for all people in all ages. Because Ephesians is addressed to the Body, its conduct instructions apply to the Body directly, and this section shows how they shape daily life. They do not turn Israel’s covenant commands or kingdom promises into the Body’s obligations."),
  P("Drawn from Ephesians’ own instructions to believers. The Body of Christ should:"),
  OL("<b>Rest in grace</b> — Salvation is God’s gift, not our achievement (Eph. 2:8–9).",
     "<b>Know its position</b> — We are blessed and seated in Christ (Eph. 1:3; 2:6).",
     "<b>Keep the unity of the Spirit</b> — Bear with one another in love (Eph. 4:2–3).",
     "<b>Speak truth in love</b> — Grow together in Christ (Eph. 4:15, 25).",
     "<b>Put off the old and put on the new</b> — Walk as renewed in the spirit of the mind (Eph. 4:22–24).",
     "<b>Forgive as forgiven</b> — Kindness and tenderheartedness reflect God’s mercy (Eph. 4:32).",
     "<b>Honor Christ in the home</b> — Love, submission, obedience, and nurture (Eph. 5:22–6:4).",
     "<b>Stand in the armour of God</b> — Be strong in the Lord and pray with perseverance (Eph. 6:10–18)."))

S(10, "Teaching Outline for Ephesians",
  P("<i>Teacher-ready, movement-based outline</i>"),
  OLR("Every Spiritual Blessing in Christ (Ch. 1) — God’s purpose, redemption, sealing, and the prayer for understanding. <i>(Eph. 1:3–14, 15–23)</i>",
     "From Death to Life, and One Body (Ch. 2) — Saved by grace, seated in Christ, and brought near by His blood. <i>(Eph. 2:1–10, 11–22)</i>",
     "The Mystery and the Prayer for Strength (Ch. 3) — Paul’s stewardship and the Gentiles as fellowheirs of the same body. <i>(Eph. 3:1–13, 14–21)</i>",
     "Walking Worthy of the Calling (Ch. 4) — Unity, gifts, maturity, and the old and new man. <i>(Eph. 4:1–16, 17–32)</i>",
     "Walking in Love, Light, and Wisdom (5:1–21) — Imitating God, living as children of light, and being filled with the Spirit. <i>(Eph. 5:1–2, 8, 15–21)</i>",
     "The Christian Household (5:22–6:9) — Marriage, parents and children, servants and masters. <i>(Eph. 5:22–33; 6:1–9)</i>",
     "Standing in the Whole Armour of God (6:10–24) — Strength in the Lord, the armour, and prayer. <i>(Eph. 6:10–20)</i>"))
