#!/usr/bin/env python3
"""Harvest the Fit Check Map data from the repo.

Reads every product page family and writes three JSON files to ./data:
  registry.json  one row per product item
  coverage.json  one row per (item, passage interval, depth)
  edges.json     one row per related-reading link between items

Depth values for Phase 1 (page-level data; every row carries source="page"):
  key        the passage is named as a key passage on the item's own page
  mentioned  the passage appears in the item's page text
  book       the item covers the whole book (companions, free summaries)
Phase 2 (publisher PDFs) upgrades depth to argued / reported / listed / cited
and source to "pdf".
"""
import json, os, re, sys, glob
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bibleref as B

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(OUT, exist_ok=True)

SERIES = {  # filename prefix -> (series label, mode)
    "commentary-identity": ("Prophetic Identity Commentary", 2),
    "commentary-covenantal": ("Covenantal Commentary", 2),
    "commentary-prophecy-mystery": ("Prophecy & Mystery Commentary", 2),
    "commentary-typology": ("Typology Commentary", 2),
    "commentary-acts": ("Acts Commentary", 2),
    "commentary-gospel": ("Gospel Commentary", 2),
    "commentary-pauline": ("Pauline Doctrine Series", 2),
}
PROPHETIC_RX = re.compile(r"^commentary-0(\d)-")

# free resources and interactive maps that have their own page
RESOURCE_PAGES = {
    "second-coming-map.html": ("Second Coming Map", "interactive map"),
    "jesus-ministry-map.html": ("The Lord's Ministry Route Map", "interactive map"),
    "paul-missionary-journeys.html": ("Paul's Missionary Journeys", "interactive map"),
    "acts-overlap-visual-guide.html": ("Acts Overlap Visual Guide", "free resource"),
    "building-biblical-doctrine.html": ("Building Biblical Doctrine", "free resource"),
    "historical-drift.html": ("Historical Drift", "free resource"),
    "replacement-theology.html": ("Replacement Theology", "free resource"),
    "new-testament-and-new-covenant.html": ("New Testament and New Covenant Are Not the Same", "free resource"),
    "dispensational-readings-of-acts.html": ("Dispensational Readings of Acts", "free resource"),
    "biblical-hermeneutics-course.html": ("Biblical Hermeneutics Course", "course"),
    "full-framework.html": ("The Full Framework", "book"),
    "diagnostic-manual.html": ("Diagnostic Manual", "free resource"),
}

registry, coverage, edges = [], [], []
by_slug = {}


def soup_of(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return BeautifulSoup(f.read(), "lxml")


def clean(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def main_of(soup):
    m = soup.find("main") or soup.body or soup
    for t in m.find_all(["script", "style", "nav", "header", "footer"]):
        t.decompose()
    return m


QRX = re.compile(r"([^.?!]*?(?:alone answers|own question is|narrower question|question this (?:study|volume|edition) )[^.?!]*[.?!][^.?!]*[.?!]?)")


def question_of(text, fallback=""):
    m = QRX.search(text)
    if m:
        return clean(m.group(1))[:420]
    return clean(fallback)[:300]


def add_item(**kw):
    kw.setdefault("source", "page")
    registry.append(kw)
    by_slug[kw["slug"]] = kw["id"]


def add_cov(item_id, refs_text, depth, mode=None):
    n = 0
    for _, ivs in B.find_refs(refs_text):
        for code, lo, hi in ivs:
            coverage.append({"item": item_id, "book": code, "lo": lo, "hi": hi, "depth": depth, "source": "page"})
            n += 1
    return n


def parse_related(soup, item_id):
    box = soup.find(class_="study-distinction")
    if not box:
        return
    for col in box.find_all(class_="rel-col"):
        h = col.find("h4")
        lst = clean(h.get_text()) if h else ""
        for p in col.find_all("p"):
            a = p.find("a", href=True)
            if not a:
                continue
            note = clean(p.get_text().replace(a.get_text(), "", 1))
            edges.append({"from": item_id, "to_slug": a["href"].split("#")[0], "list": lst, "note": note[:300]})
    for a in box.find_all("a", href=True):
        pass


def common(soup, slug):
    h1 = soup.find("h1")
    title = clean(h1.get_text()) if h1 else slug
    sub = soup.find(class_="detail-subtitle")
    kick = soup.find(class_="detail-kicker")
    lead = soup.find(class_="lead")
    price = soup.find(class_=re.compile(r"(detail-price|para-price)"))
    bl = soup.find(class_="detail-buyline")
    pages = None
    txt_bl = clean(bl.get_text()) if bl else ""
    m = re.search(r"(\d+)\s*Pages?", txt_bl + " " + clean(price.get_text() if price else ""))
    if m:
        pages = int(m.group(1))
    return {
        "title": title,
        "subtitle": clean(sub.get_text()) if sub else "",
        "kicker": clean(kick.get_text()) if kick else "",
        "lead": clean(lead.get_text()) if lead else "",
        "pages": pages,
        "price": clean(price.get_text())[:60] if price else "",
    }


def cards(soup):
    return [clean(c.find("h3").get_text()) for c in soup.select(".scripture-card") if c.find("h3")]


def process_page(path, item_id, kind, mode, series="", n=None, extra=None, key_all=False, book=None):
    slug = os.path.basename(path)
    soup = soup_of(path)
    c = common(soup, slug)
    parse_related(soup, item_id)
    main = main_of(soup)
    box = main.find(class_="study-distinction")
    if box:
        box.decompose()
    text = clean(main.get_text(" "))
    q = question_of(text, c["lead"])
    row = dict(id=item_id, type=kind, mode=mode, series=series, n=n, title=c["title"], subtitle=c["subtitle"],
               slug=slug, pages=c["pages"], price=c["price"], question=q)
    if extra:
        row.update(extra)
    add_item(**row)
    nk = 0
    for ctext in cards(soup):
        nk += add_cov(item_id, ctext, "key")
    if key_all:
        nk += add_cov(item_id, text, "key")
    else:
        add_cov(item_id, text, "mentioned")
    if book:
        code = book
        coverage.append({"item": item_id, "book": code, "lo": 1001, "hi": 150999, "depth": "book", "source": "page"})
    registry[-1]["key_passages"] = nk
    return soup


def book_code_from_slug(slug_core):
    """packet-1-corinthians -> 1Cor ; packet-song-of-solomon -> Song"""
    name = slug_core.replace("-", " ")
    for code, full, _ in B.BOOKS:
        if full.lower() == name.lower():
            return code
    return None


def main():
    files = sorted(os.listdir(ROOT))
    # studies
    for f in files:
        m = re.match(r"^study-(\d+)-.*\.html$", f)
        if m:
            n = int(m.group(1))
            process_page(os.path.join(ROOT, f), f"S{n:02d}", "Digital Study", 1, "Digital Studies", n)
    # parables
    for f in files:
        if re.match(r"^parable-(\d+)-.*\.html$", f) or f == "parable-sower.html":
            m = re.match(r"^parable-(\d+)-", f)
            n = int(m.group(1)) if m else 0
            process_page(os.path.join(ROOT, f), f"P{n:02d}", "Parable Study", 1, "Parable Studies", n)
    # commentary volumes
    for f in files:
        if not f.startswith("commentary-") or f in ("commentary.html",):
            continue
        series = None
        for pre, (label, mode) in SERIES.items():
            if f.startswith(pre + "-"):
                series, md = label, mode
                key = pre.replace("commentary-", "")
                break
        else:
            m = PROPHETIC_RX.match(f)
            if m:
                series, md, key = "Prophetic Commentary", 2, "prophetic"
            else:
                continue
        m = re.search(r"-(\d\d)-", f)
        n = int(m.group(1))
        process_page(os.path.join(ROOT, f), f"V-{key}-{n}", "Commentary Volume", md, series, n)
    # bible book companions
    for f in files:
        m = re.match(r"^packet-(.*)\.html$", f)
        if m:
            code = book_code_from_slug(m.group(1))
            process_page(os.path.join(ROOT, f), f"C-{code or m.group(1)}", "Bible Book Companion", "companion", "Bible Book Companion Series",
                         None, extra={"book": code}, book=code)
    # free bible book summaries
    for f in files:
        m = re.match(r"^(.*)-summary\.html$", f)
        if m and f not in ("bible-book-summaries.html",):
            code = book_code_from_slug(m.group(1))
            p = os.path.join(ROOT, f)
            soup = soup_of(p)
            c = common(soup, f)
            add_item(id=f"B-{code or m.group(1)}", type="Bible Book Summary (free)", mode="summary", series="Bible Book Summaries", n=None,
                     title=c["title"], subtitle=c["subtitle"], slug=f, pages=None, price="free", question="", book=code)
            if code:
                coverage.append({"item": f"B-{code}", "book": code, "lo": 1001, "hi": 150999, "depth": "book", "source": "page"})
    # reader questions: entries
    for f in files:
        m = re.match(r"^reader-questions-v(\d+)-q(\d+)-.*\.html$", f)
        if m:
            v, n = int(m.group(1)), int(m.group(2))
            iid = f"Q{v}-{n:02d}"
            soup = process_page(os.path.join(ROOT, f), iid, "Reader Question", 3, f"Readers Question Series, Volume {v}", n, key_all=False)
            # title refs are key passages
            t = next(r for r in registry if r["id"] == iid)["title"]
            add_cov(iid, t, "key")
    # reader questions volumes
    for f in files:
        m = re.match(r"^reader-questions-0(\d)-.*\.html$", f)
        if m:
            v = int(m.group(1))
            process_page(os.path.join(ROOT, f), f"QV{v}", "Reader Questions Volume", 3, "Readers Question Series", v)
    # free resources with their own page
    for f, (name, kind) in RESOURCE_PAGES.items():
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            mode = "book" if kind == "book" else ("resource" if kind != "course" else "course")
            iid = "R-" + f.replace(".html", "")
            process_page(p, iid, kind.title() if kind != "interactive map" else "Interactive Map", mode, "Free resources" if kind not in ("book", "course") else kind.title(),
                         None, key_all=(kind == "interactive map"))
    # resource library entries (PDF resources without their own page)
    rl = os.path.join(ROOT, "resource-library.js")
    if os.path.exists(rl):
        js = open(rl, encoding="utf-8").read()
        for m in re.finditer(r"\{id:(\d+),title:'(.*?)',subtitle:'(.*?)',category:'(.*?)',tags:\[(.*?)\],desc:'(.*?)'", js, re.S):
            rid, title, sub, cat, tags, desc = m.groups()
            iid = f"RL{int(rid):02d}"
            if any(clean(title).lower() in (r["title"] or "").lower() or (r["title"] or "").lower() in clean(title).lower() for r in registry
                   if r["id"].startswith("R-")):
                continue
            add_item(id=iid, type="Free Resource (library)", mode="resource", series="Free resources", n=int(rid), title=clean(title),
                     subtitle=clean(sub), slug=f"resource-library#{rid}", pages=None, price="free", question=clean(desc)[:300], category=cat)
            add_cov(iid, " ".join([sub, desc, tags]), "mentioned")
    # resolve edges
    ids = by_slug
    out = []
    for e in edges:
        tgt = ids.get(e["to_slug"])
        e["to"] = tgt
        out.append(e)
    # drop exact duplicate coverage rows
    seen, cov2 = set(), []
    for c in coverage:
        k = (c["item"], c["book"], c["lo"], c["hi"], c["depth"])
        if k not in seen:
            seen.add(k); cov2.append(c)
    json.dump(registry, open(os.path.join(OUT, "registry.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(cov2, open(os.path.join(OUT, "coverage.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(out, open(os.path.join(OUT, "edges.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # report
    from collections import Counter
    print("items:", len(registry), dict(Counter(r["type"] for r in registry)))
    print("coverage rows:", len(cov2), dict(Counter(c["depth"] for c in cov2)))
    print("edges:", len(out), "resolved:", sum(1 for e in out if e["to"]), "unresolved:", sum(1 for e in out if not e["to"]))
    nokey = [r["id"] for r in registry if r["type"] in ("Digital Study", "Commentary Volume") and not r.get("key_passages")]
    print("studies/volumes with no key passages parsed:", nokey)


if __name__ == "__main__":
    main()
