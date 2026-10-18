#!/usr/bin/env python3
"""Render the Fit Check Map (markdown + HTML preview) from data/*.json."""
import json, os, sys, glob, collections, html, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bibleref as B
D = os.path.join(HERE, "data"); OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
VERSION = sys.argv[1] if len(sys.argv) > 1 else "1.0"

reg = json.load(open(f"{D}/registry.json", encoding="utf-8")); R = {r["id"]: r for r in reg}
cov = json.load(open(f"{D}/coverage.json", encoding="utf-8"))
pdf = []
for f in sorted(glob.glob(f"{D}/coverage_pdf_*.json")): pdf += json.load(open(f, encoding="utf-8"))
pdf_items = {c["item"] for c in pdf}
cov = [c for c in cov if c["item"] not in pdf_items or c["depth"] == "book"] + pdf
edges = json.load(open(f"{D}/edges.json", encoding="utf-8"))
edge_n = collections.Counter(e["from"] for e in edges if e.get("to"))

CH = {"Gen":50,"Exod":40,"Lev":27,"Num":36,"Deut":34,"Josh":24,"Judg":21,"Ruth":4,"1Sam":31,"2Sam":24,"1Kgs":22,"2Kgs":25,"1Chr":29,"2Chr":36,"Ezra":10,"Neh":13,"Esth":10,"Job":42,"Ps":150,"Prov":31,"Eccl":12,"Song":8,"Isa":66,"Jer":52,"Lam":5,"Ezek":48,"Dan":12,"Hos":14,"Joel":3,"Amos":9,"Obad":1,"Jonah":4,"Mic":7,"Nah":3,"Hab":3,"Zeph":3,"Hag":2,"Zech":14,"Mal":4,"Matt":28,"Mark":16,"Luke":24,"John":21,"Acts":28,"Rom":16,"1Cor":16,"2Cor":13,"Gal":6,"Eph":6,"Phil":4,"Col":4,"1Thess":5,"2Thess":3,"1Tim":6,"2Tim":4,"Titus":3,"Phlm":1,"Heb":13,"Jas":5,"1Pet":5,"2Pet":3,"1John":5,"2John":1,"3John":1,"Jude":1,"Rev":22}
TREAT = ("argued", "reported", "key")           # an item "treats" a chapter at these depths
CORE = lambda i: not i.startswith(("C-", "B-", "Q", "RL")) and R[i]["type"] in ("Digital Study","Commentary Volume","Parable Study")

# chapter -> {item: best depth}
chap = collections.defaultdict(dict)
RK = {"argued": 3, "reported": 2, "key": 2, "cited": 1, "mentioned": 1}
for c in cov:
    if c["depth"] == "book" or c["item"] not in R: continue
    if c["hi"] // 1000 - c["lo"] // 1000 > 3: continue   # a range over 4 chapters is a sweep, not treatment of each chapter
    for ch in range(c["lo"] // 1000, c["hi"] // 1000 + 1):
        if ch < 1 or ch > CH.get(c["book"], 0): continue
        d = chap[(c["book"], ch)]
        if RK[c["depth"]] > RK.get(d.get(c["item"], ""), 0): d[c["item"]] = c["depth"]

def treat(book, ch, argued_only=False):
    d = chap.get((book, ch), {})
    return sorted(i for i, dep in d.items() if CORE(i) and (dep == "argued" if argued_only else dep in TREAT))

L = []; A = L.append
today = datetime.date.today().isoformat()
A(f"# Fit Check Map v{VERSION}\n")
A(f"Version {VERSION}. Internal editorial record, approved by the publisher {today}. Replaces the Digital Studies Relationship Map (v1.54, carried forward whole in the Appendix). Standing rule: this map is consulted first, as the opening step of every topic check (Approval Checkpoint 1), before any study, commentary volume, parable, reader question, companion, resource, map or book is proposed, outlined or drafted: check the passage, the one narrower question, the series arc and the neighbours, and state the verdict. A new product is added to the map in the same pass as its website package.")
A("## 1. How to use it\n")
A("1. Name the passage(s) and the one narrower question. 2. Run `python3 -I build-tools/fit-check/fitcheck.py \"<passage>\"` and read Sections 5 and 6 below. 3. Read the neighbours' own question in Section 4 (and the PDF when the grade is argued). 4. State the verdict: clear, fit by mode, fit by narrower question, overlap (needs a different question), or duplicate. 5. Check the series arc (Section 3) if a volume is proposed.\n")
A("Chapter-level tables (Sections 5 and 6) ignore any cited range wider than four chapters (for example \"Acts 9–28\"), because a sweep names a stretch of text without treating each chapter.\n")
A("Depth grades come from counts in the publisher's PDFs (argued = named 4+ times, reported 2–3, cited once); they show where an item dwells, not whether it takes a position. Items not yet received as PDFs are graded from their website page (key passages). Verdicts are provisional.\n")

A("## 2. What is mapped\n")
cnt = collections.Counter(r["type"] for r in reg)
A("| Product family | Items | Source of depth grade |\n|---|---|---|")
src = {"Digital Study":"PDF","Commentary Volume":"PDF","Parable Study":"Word file","Bible Book Companion":"PDF","Reader Questions Volume":"PDF","Reader Question":"page","Bible Book Summary (free)":"page","Interactive Map":"page","Free Resource":"page","Free Resource (library)":"library entry","Course":"page","Book":"print proof (eProof)"}
for t, n in sorted(cnt.items(), key=lambda x: -x[1]): A(f"| {t} | {n} | {src.get(t,'page')} |")
A("")


ARC = {
"Prophetic Commentary": ("Revelation's end-time figures and events, in order: the two riders (Vol 1; the beast between them is Daniel's little horn), the false prophet (Vol 2), the scarlet beast and the woman (Vol 3), Daniel's seventy weeks (Vol 4), Armageddon and the winepress (Vol 5).", 'The Standard has no overlap table (it states scope, not neighbours). Neighbours come from the coverage data: Daniel 9 and Revelation 6, 13, 17, 19 are also reported in Studies 7, 10, 61, 64, 68, 69 and 74 and in Prophecy & Mystery Vol 3–5; this series argues the identities and the order, those report or place them.'),
"Prophetic Identity Commentary": ('Who the prophetic figures are, each argued from the whole canon: the bride (Vol 1), the remnant (Vol 2), the new covenant (Vol 3), the olive tree (Vol 4), the eschatological community (Vol 5).', 'The Standard has no overlap table; its rulings name the boundaries: Romans 11:1, 5 (Vol 2) and Romans 11 (Vol 4) keep the Olive Tree treatment; Revelation 7:9, 12:5 and 12:17 (Vol 2) stand beside Study 61 and the 144,000; Hebrews 12:22–24 and Galatians 4:26 (Vol 5) are read as not enrolling the Body; Ephesians 5:22–33 (Vol 1) is a marriage pattern, not a Bride title. Shares ground with Studies 1, 9, 12, 13, 35 and Covenantal Vol 1–2.'),
"Prophecy & Mystery Commentary": ("Whose passage is this? Vol 1 sets Israel's program beside the Body's; Vol 2 reads the Mystery; Vol 3 the Kingdom; Vol 4 the resurrections; Vol 5 the courts. Each Preface states what the earlier volumes asked.", "Vol 1 shares ground with Study 4, Covenantal Vol 4 and the Prophetic Identity series. The Acts, Gospel and Pauline Standards name Vol 1 ch. 7, Vol 2, Vol 3 chs. 5–6, Vol 4 (1 Corinthians 15:23) and Vol 5 as neighbours."),
"Covenantal Commentary": ("The covenants in order: what God swore to Abraham (Vol 1), who the seed is (Vol 2), what the line was given to possess (Vol 3), why two callings serve one purpose (Vol 4), what God swore to David (Vol 5). Each Preface restates what the earlier volumes asked.", "Each theme shares a subject with Studies 17, 40, 56 and 57. Vol 1–2 also touch Prophetic Identity Vol 3 (new covenant) and Vol 4 (olive tree); the series cross-refers and does not repeat them."),
"Typology Commentary": ('Patterns that run from Exodus to Revelation, one typology per volume: tabernacle and temple (Vol 1), separation of the judged from the kept (Vol 2), priesthood (Vol 3), Exodus (Vol 4), kingdom (Vol 5).', "The Standard has no overlap table; its rulings leave named ground elsewhere: Vol 4 leaves the Law's jurisdiction over the Body to Study 59 and keeps the cup sentence; Vol 2 keeps 1 Thessalonians 4 and 1 Corinthians 15 in their own setting (Prophecy & Mystery Vol 4; Study 29 area); Vol 3 reads Hebrews on the Jeremiah 31 covenant (Prophetic Identity Vol 3, Studies 12 and 67); Vol 5 carries Acts 2:30–36 and Revelation 3:21 from the earlier volumes (Study 73, Covenantal Vol 5) and keeps the kingdom temple as in Vol 1."),
"Acts Commentary": ("Acts in order: Acts 1–8 (Vol 1), the Spirit from Pentecost to Ephesus (Vol 2), Paul called and sent (Vol 3), Cornelius and the Council (Vol 4), Acts 28 (Vol 5).", "No other product walks Acts section by section. Closest: Vol 1 and 5 with Prophecy & Mystery Vol 3; Vol 2 with Studies 20, 34, 38. Also Studies 14, 18, 19, 65 and Study 2."),
"Gospel Commentary": ("The Lord's ministry before the Cross as told to Israel: the Sermon on the Mount (Vol 1), the ministry to Israel (Vol 2), the Olivet Discourse (Vol 3), what the Twelve understood (Vol 4), the Upper Room (Vol 5).", "Closest: Vol 2 with Prophecy & Mystery Vol 3 and Study 2; Vol 3 with Study 29 and Typology Vol 2; Vol 4 with Study 75. No volume works through the parables (the Parable Studies carry them)."),
"Pauline Doctrine Series": ("Large Pauline themes, one narrow question each: Adam and Christ (Vol 1), the Cross (Vol 2), the person of Christ (Vol 3), the assembly in order (Vol 4), liberty, conscience and the walk (Vol 5).", "Closest: Vol 2 with Studies 53, 54, 55; Vol 4 with Studies 72, 81 and the 1 Corinthians and Timothy companions; Vol 5 with Studies 36, 77, 78; Vol 1 with Study 49 and Prophecy & Mystery Vol 4."),
"The Prophets Series": ("Questions the prophets raise themselves, one narrow question per volume: how the prophets spoke (Vol 1; built), what they condemned (Vol 2; built), the nations judged (Vol 3; built), Elijah must first come (Vol 4; built).", "Vol 1 shares passages with Study 75 (1 Peter 1:10–12), Study 67 (Psalm 110:4), Study 73 (Psalm 89), Covenantal Vol 5 (the sworn covenant), Prophetic Vol 2 (the false prophet of Revelation 13) and Acts Vol 1 (the prophet like Moses); it reads Deuteronomy 13 and 18, Jeremiah 23 and 28, 1 Kings 22 and Jonah where no other product argues them. Vol 2 shares Hebrews 10:1–10 with Study 24 and Typology Vols 1 and 3, Isaiah 58 and 66 with Study 78, and Amos 5:25–27 and Isaiah 66:1–2 (as Acts 7 quotes them) with Acts Vol 1; it reads Isaiah 1, Amos 5, Hosea 6, Micah 6, Jeremiah 6 and 7 and Malachi 1 and 2 where no other product argues them. Vol 4 shares Malachi 4:5 and Matthew 17:10–12 with Prophetic Vol 2 (the counterfeit Elijah), Acts 3:21 with Acts Vol 1 and Luke 1:16–17 with Gospel Vol 2; it reads Malachi 3:1 and 4:4–6, 1 Kings 17–19, 2 Kings 2, Matthew 11:7–19 and John 1:19–28 where no other product argues them. The Standard holds the overlap table."),
"The Sign Gifts Series": ("What signs were for, to whom they were given and where the record ends, one narrow question per volume: the sign gifts (Vol 1; built), tongues and prophecy (Vol 2; built), healing in the Body (Vol 3; built) and apostles and prophets (Vol 4; planned, conditional).", "Vol 1 shares passages with Study 25 (Mark 16:17–20), Study 38 and Acts Commentary Vol 2 (the Spirit scenes) and Vol 5 (Acts 28); 2 Corinthians 12:12 and Acts 28 are crowded chapters; Study 81 and Readers Question Vol 5 are neighbours, Hebrews 2:3–4 and the Exodus 4 signs are left to the companions. Vol 2 shares 1 Corinthians 12–14 with Pauline Vol 4 (the assembly) and Study 81 (praying in the Spirit), Acts 2, 10 and 19 with Acts Vol 2, Study 38 and Study 34, and Acts 28 with Acts Vol 5 and Sign Gifts Vol 1; it reads Isaiah 28:7–14 and 1 Corinthians 13 and 14:21–22 where no other product argues them."),
}
A("## 3. Series and arcs\n")
ser = collections.OrderedDict()
for r in reg:
    if r["type"] == "Commentary Volume": ser.setdefault(r["series"], []).append(r)
for s, vs in ser.items():
    A(f"**{s}** ({len(vs)} volume{'' if len(vs)==1 else 's'})\n")
    if s in ARC: A(f"*Arc:* {ARC[s][0]}\n\n*Neighbours (from the series Standard and the Prefaces):* {ARC[s][1]}\n")
    for v in sorted(vs, key=lambda x: x["n"]):
        A(f"- Vol {v['n']}: {v['title']} — {v.get('pages') or '?'} pp")
    A("")


# ---- Full Framework: chapters and nearest neighbours
import re
bt = open("/home/claude/fc-pdfs/txt/book/R-full-framework.txt", encoding="utf-8", errors="ignore").read() if os.path.exists("/home/claude/fc-pdfs/txt/book/R-full-framework.txt") else ""
chs = []
for m in re.finditer(r"^(Chapter \d+: [^\n.]+?|Appendix [A-D]: [^\n.]+?)\.{4,}", bt, re.M):
    chs.append(m.group(1).strip())
if chs:
    A("## 3b. The Full Framework (book)\n")
    A("The proof is 243 pages with 21 chapters and four appendices; the Table of Contents and chapter list below are read from it.\n")
    for c in chs: A(f"- {c}")
    A("")
    mine = {k for k, d in chap.items() if d.get("R-full-framework") in ("argued", "reported")}
    near = collections.Counter()
    for k in mine:
        for i in treat(*k, argued_only=False):
            if i != "R-full-framework": near[i] += 1
    A("Nearest neighbours by shared chapters (chapters the book argues or reports that the item also treats):\n")
    A("| Item | Title | Shared chapters |\n|---|---|---|")
    for i, n in near.most_common(12): A(f"| {i} | {R[i]['title'][:60]} | {n} |")
    A("")
A("## 4. Register (every item, one line)\n")
A("| ID | Type | Title | Pages | Related Reading links out |\n|---|---|---|---|---|")
for r in reg:
    if r["type"] in ("Digital Study","Commentary Volume","Parable Study","Reader Questions Volume","Interactive Map","Course","Book","Free Resource"):
        A(f"| {r['id']} | {r['type']} | {r['title'].replace('|','/')[:70]} | {r.get('pages') or ''} | {edge_n.get(r['id'],0)} |")
A("")


from drafted_questions import D as DQ
qs = json.load(open(f"{D}/questions.json", encoding="utf-8")) if os.path.exists(f"{D}/questions.json") else {}
A("## 4b. Narrower questions (each item's own statement)\n")
stated = sum(1 for v in qs.values() if v["source"] in ("page", "pdf") and v["question"])
A(f"{stated} of {len(qs)} studies, parables and volumes state a narrower question in so many words (marked **stated**). For the 70 that do not (35 parables, 24 volumes, 11 studies) a one-line question was drafted from the item\'s own text (marked *drafted, for review*) and is not yet approved.\n")
A("| ID | Title | Narrower question | Basis |\n|---|---|---|---|")
for r in reg:
    v = qs.get(r["id"])
    if not v: continue
    q = v["question"].replace("|", "/")
    is_stated = v["source"] in ("page", "pdf") and v["question"]
    if is_stated: basis = "**stated**"
    elif r["id"] in DQ: q, basis = DQ[r["id"]].replace("|", "/"), "*drafted, for review*"
    else: basis = "*inferred*"
    A(f"| {r['id']} | {r['title'].replace('|','/')[:50]} | {q[:300]} | {basis} |")
A("")
A("## 5. Crowded chapters (4 or more items argue them)\n")
A("Caution: the series keeps returning to a few anchor chapters (Acts 9, Acts 28, Ephesians 1–3, Romans 11), so a count of four or more can mean a refrain, not an argument. Treat Acts 9 and 28 as the series' shared ground; the question each item asks is what separates them, and that question is in Section 4 and the PDF.\n")
crowd = []
for (b, ch), d in chap.items():
    ids = treat(b, ch, argued_only=True)
    if len(ids) >= 4: crowd.append((len(ids), b, ch, ids))
crowd.sort(key=lambda x: (-x[0], B.ORDER[x[1]], x[2]))
A("| Chapter | Items arguing it | Who |\n|---|---|---|")
for n, b, ch, ids in crowd[:60]:
    A(f"| {B.NAME[b]} {ch} | {n} | {', '.join(ids)} |")
A(f"\n{len(crowd)} chapters in all; top 60 shown.\n")

A("## 6. Gaps (chapters no study, volume or parable argues, reports or lists as key)\n")
A("Companions, summaries and reader questions are not counted, because they read a whole book briefly or answer one verse. A gap is a place to look, not a mandate to write.\n")
A("| Book | Chapters with no treatment | Of |\n|---|---|---|")
for code, full, _ in B.BOOKS:
    gaps = [ch for ch in range(1, CH[code] + 1) if not treat(code, ch)]
    if not gaps: continue
    runs, s = [], gaps[0]; p = s
    for g in gaps[1:] + [None]:
        if g is None or g != p + 1:
            runs.append(f"{s}" if s == p else f"{s}–{p}")
            if g is not None: s = g
        if g is not None: p = g
    A(f"| {full} | {', '.join(runs)} | {CH[code]} |")
A("")

A("## 7. Relationships\n")
A(f"{len(edges)} Related Reading links were read from the website pages ({sum(1 for e in edges if e.get('to'))} resolve to a mapped item). Links are cross-references; they say a neighbour exists, not what the neighbour argues. The per-item neighbour notes are in `build-tools/fit-check/data/edges.json`.\n")

def fam(i):
    t = R[i]["type"] if i in R else "?"
    return {"Digital Study":"Study","Commentary Volume":"Volume","Parable Study":"Parable","Bible Book Companion":"Companion","Reader Question":"Reader Q","Reader Questions Volume":"Reader Q","Bible Book Summary (free)":"Summary"}.get(t, "Other")
mat = collections.Counter((fam(e["from"]), fam(e["to"])) for e in edges if e.get("to"))
fams = ["Study","Volume","Parable","Companion","Reader Q","Summary","Other"]
A("Related Reading links by product family (rows link to columns):\n")
A("| From \\ To | " + " | ".join(fams) + " |\n|---|" + "---|"*len(fams))
for a in fams:
    A(f"| {a} | " + " | ".join(str(mat.get((a, b), 0)) for b in fams) + " |")
A("")
A("## 8. Not yet in the map\n")
A("- The Full Framework is read from the print proof (eProof), not from the final interior.\n- Parable files are the published editions (publisher, 2026-10-15), though the files are named FULL_REVIEW.\n- Reader Questions Volumes 2 and 3: PDFs are 29 and 26 pages; the website says 30 and 27. The PDFs are treated as current.\n- Standards' overlap notes are merged as short neighbour lines (Section 3). All eight series Standards are now read; Typology, Prophetic and Prophetic Identity have no overlap table, so their neighbour lines come from their rulings and the coverage data.\n- Narrower questions for 70 items are drafted by Claude and kept by the publisher (2026-10-15).\n")
A("## 8b. Planned series items (not yet built; no PDFs to grade)\n")
A('**The Prophets Series** (ninth commentary series, registered 2026-10-15 in Master Standard v1.159; Standard `Prophets_Series_Standard_v1.11.md`). Volumes 1, 2, 3 and 4, How the Prophets Spoke (51 pages with the cover), What the Prophets Condemned (57 pages), The Nations Judged (60 pages) and Elijah Must First Come (55 pages), are built and in the map above. No planned items remain in the series. Passage lists and neighbour notes are in the Standard.')
A("")
A('**The Sign Gifts Series** (tenth commentary series, registered 2026-10-17 in Master Standard v1.168; Standard `Sign_Gifts_Series_Standard_v1.10.md`). Volume 1, The Sign Gifts (55 pages with the cover; subtitle The Purpose of Signs, Their Audience, and Their Programmatic End at Acts 28), Volume 2, Tongues and Prophecy (55 pages with the cover; subtitle Whether Tongues and Prophecy Continue in the Body), and Volume 3, Healing in the Body (55 pages with the cover; subtitle The Sign-Gift of Healing and the Body\'s Non-Sign Pattern), are built and in the map above. Volume 4 is planned, Mode 2, conditional on a 50-page outline test. Planned, with no PDFs to grade:\n')
A("| Vol | Planned title | Narrower question | Passages (planned) | Verdict | Main neighbours |\n|---|---|---|---|---|---|")
A("| 4 | Apostles and Prophets | Whether the apostolic and prophetic offices continue | Acts 1:21–26; 1 Corinthians 9:1, 15:8; Romans 16:7; Ephesians 2:20, 3:5, 4:11–13; Revelation 21:14 | Fit by narrower question; conditional | Pauline Vol 4 (Ephesians 4:12); Acts Vol 1 and 5 |")
A("")
A("## 9. Version history\n")
A(f"| Version | Date | Change |\n|---|---|---|\n| 1.0 | 2026-10-15 | First build from the website pages and the publisher's PDFs (86 studies, 40 commentary volumes, 35 parables, 66 companions, 66 summaries, 5 reader-question volumes and 50 questions, resources and maps, the Full Framework). Replaces the Digital Studies Relationship Map v1.54, carried forward whole in the Appendix. |")
A("| 1.1 | 2026-10-15 | Adds Section 8b, Planned series: The Prophets Series (four volumes, Volume 4 conditional) with each volume's provisional narrower question, ahead of any PDF. No grades changed. |")
A("| 1.2 | 2026-10-15 | Adds The Prophets Series Volume 1, How the Prophets Spoke (51 pages with the cover), to the registry, the passage tables, the series arcs and the Related Reading links, graded from its PDF; Section 8b now lists Volumes 2–4 only. Related Reading links added both ways with Studies 67, 73 and 75, Prophetic Commentary Vol 2, Acts Vol 1 and the Jeremiah, Deuteronomy and Ezekiel companions. |")
A("| 1.3 | 2026-10-16 | Adds The Prophets Series Volume 2, What the Prophets Condemned (57 pages with the cover), to the registry, the passage tables, the series arcs and the Related Reading links, graded from its PDF; Section 8b now lists Volumes 3–4 only. Related Reading links added both ways with Study 59, Study 78, Typology Commentary Vol 3, Acts Vol 1 and the Isaiah, Jeremiah and Amos companions. |")
A("| 1.4 | 2026-10-16 | Adds The Prophets Series Volume 3, The Nations Judged (60 pages with the cover), to the registry, the passage tables, the series arcs and the Related Reading links, graded from its PDF; Section 8b now lists Volume 4 only. Related Reading links added both ways with Study 31, Prophetic Commentary Vol 5 and the Ezekiel companion. |")
A("| 1.5 | 2026-10-16 | Adds The Prophets Series Volume 4, Elijah Must First Come (55 pages with the cover), to the registry, the passage tables, the series arcs and the Related Reading links, graded from its PDF; Section 8b now lists no planned items. Related Reading links added both ways with Prophetic Commentary Vol 2, Gospel Commentary Vol 2 and the Malachi companion. |")
A("| 1.6 | 2026-10-16 | Adds Digital Study 87, The Last Days (16 pages with the cover; Doctrinal Themes), to the registry, the passage tables and the Related Reading links, graded from its PDF; the question it answers is stated in the study. Related Reading links added both ways with Study 7. A fifth Prophets Series volume (The Prophetic Hope) was proposed, found to overlap by the Fit Check and dropped, and its time-words topic became Study 87; the Prophets Series stays at four volumes. |")
A("| 1.7 | 2026-10-17 | Regrades the 35 Parable Studies from their rebuilt PDFs (the 13-section format, Master Standard v1.164 Rule 35; 15 to 20 pages with the cover; the Sower and the Soils is 19), replacing the grades taken from the earlier editions. Passage depth for the parables now counts the whole rebuilt text, including the neighbour boundaries and the related-passage lists, so parable rows rise sharply (the standing sentence that names Paul\'s Acts 9 calling is left out of the count, because every parable carries it) and the crowded-chapter and gap tables move with them; read a parable's depth as where the study dwells, not as a position. No product, price or narrower question changed. |")
A('| 1.8 | 2026-10-17 | Adds the Parable Study Template and its Worked Example (two free PDFs, 5 and 4 pages with the cover; page `parable-study-template.html`) to the registry as one free resource. Its narrower question is how to work any one parable through on paper in eight sections (audience and occasion, the comparison, what Jesus names and leaves unnamed, boundaries, the stated point, the present lesson); the worked example reads Matthew 22:1–14, the same passage as Parable Study 8, which the publisher kept. No passage grades, prices or other products changed. Related links added from the Parables hub, the 35 Parable Study pages and the Resource Library. |')
A('| 1.9 | 2026-10-17 | Adds Readers Question Series Volume 6, Questions on Difficult Bible Verses (psalms the New Testament quotes; 26 pages with the cover), and its ten question pages to the registry, the passage tables and the Related Reading links, graded from its PDF (60 questions in 6 volumes). The Parable Study Template row is kept as in v1.8; study page counts (58, 66, 69, 73, 78, 82, 84, 86) follow `site.js` after the Rule 34 rebuilds. No product or price changed. |')
A("| 1.10 | 2026-10-17 | Adds Section 8b entry for the planned Sign Gifts Series (four volumes, Volume 4 conditional) with each volume's narrower question, planned passages, verdict and neighbours, ahead of any PDF. No grades changed. |")
A('| 1.11 | 2026-10-17 | Sign Gifts Series Volume 1 retitled The Sign Gifts (was The Sign Program) with the subtitle and four rulings recorded; verdict stays fit by mode and by narrower question after the closer check of Studies 25, 38 and 81, Acts Volumes 2 and 5, Pauline Volume 4 and Prophecy & Mystery Volume 3. No grades changed. |')
A('| 1.12 | 2026-10-17 | Adds The Sign Gifts Series Volume 1, The Sign Gifts (55 pages with the cover; subtitle The Purpose of Signs, Their Audience, and Their Programmatic End at Acts 28; $14.99), to the registry, the passage tables, the series arcs and the Related Reading links, graded from its PDF; Section 8b now lists Volumes 2–4 only. Related Reading links added both ways with Studies 25 and 38, Acts Commentary Vol 2 and 5, Gospel Commentary Vol 2 and the Exodus and John companions. The Parable Study Template page is now in the harvest list, so a re-harvest keeps it. Rows 1.10 and 1.11 now sit in this table (they had been appended at the end of the Appendix). |')
A('| 1.13 | 2026-10-17 | Adds The Sign Gifts Series Volume 2, Tongues and Prophecy (55 pages with the cover; subtitle Whether Tongues and Prophecy Continue in the Body; $14.99), to the registry, the passage tables, the series arcs and the Related Reading links, graded from its PDF; Section 8b now lists Volumes 3 and 4 only. Related Reading links added both ways with Pauline Doctrine Series Volume 4; Studies 81, 25 and 38, Acts Commentary Volume 2 and the 1 Corinthians and Isaiah companions already carry three links in their lists, so the volume page links to them and no link back was added. |')
A('| 1.14 | 2026-10-17 | Adds The Sign Gifts Series Volume 3, Healing in the Body (55 pages with the cover; subtitle The Sign-Gift of Healing and the Body\'s Non-Sign Pattern; $14.99), to the registry, the passage tables, the series arcs and the Related Reading links, graded from its PDF; Section 8b now lists Volume 4 only. Related Reading links added both ways with Study 86 and the James and 2 Corinthians companions; Studies 25 and 38, Sign Gifts Volumes 1 and 2, Acts Commentary Vol 5 and the 1 Corinthians companion already carry three links in their lists, so the volume page links to them and no link back was added. |')

import re as _re
A("\n## Appendix. Digital Studies Relationship Map v1.54 (carried forward whole)\n")
A("This is the earlier Digital Studies Relationship Map, kept word for word so that nothing it recorded is lost: the eight priced collections and prices, the study-by-study table for Studies 1-70, the Paul's Missionary Journeys cross-reference, the catalog classification, the implementation notes and its own version history. It is superseded by the sections above for deciding whether a new idea fits; the collection prices and the journeys cross-reference remain the record until they are moved into the Master Standard or a later edition. Headings below are lowered two levels.\n")
_leg = open(os.path.join(HERE, "data", "legacy_relationship_map_v1.54.md"), encoding="utf-8").read()
A(_re.sub(r"^(#+) ", lambda m: "#"*(len(m.group(1))+2)+" ", _leg, flags=_re.M))
md = "\n".join(L)
open(f"{OUT}/Fit_Check_Map_v{VERSION}.md", "w", encoding="utf-8").write(md)
print("written", len(md), "chars; crowded chapters", len(crowd))
