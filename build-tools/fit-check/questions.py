#!/usr/bin/env python3
"""Extract each item's own statement of its narrower question.
Studies, parables, volumes: the last lead paragraph of the page's opening section (the distinction paragraph),
cut to its closing sentence; volumes also take the PDF sentence "This volume asks a narrower question: ...".
Writes data/questions.json  {id: {"question", "distinction", "source"}}
"""
import json, os, re, sys
from bs4 import BeautifulSoup
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
reg = json.load(open(f"{HERE}/data/registry.json", encoding="utf-8"))
out = {}
QS = re.compile(r"(?:The )?(?:narrower )?question (?:this (?:study|volume|parable study|edition) )?(?:alone )?(?:answers|asks)[^:]*:\s*(.+?[?.])(?:\s|$)", re.I)

def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+(?=[A-Z“\"])", t) if s.strip()]

for r in reg:
    if r["type"] not in ("Digital Study", "Parable Study", "Commentary Volume"):
        continue
    p = os.path.join(ROOT, r["slug"])
    s = BeautifulSoup(open(p, encoding="utf-8", errors="ignore").read(), "lxml")
    h = s.find("h2")
    sec = (h.find_parent(class_="wrap") or h.parent) if h else None
    leads = [x.get_text(" ", strip=True) for x in (sec.find_all("p", class_="lead") if sec else [])]
    dist = leads[-1] if leads else ""
    q, src = "", "page"
    cand = [x for x in sentences(" ".join(leads)) if re.search(r"narrower question|question[^.?]{0,60}alone|alone[^.?]{0,40}question|task is narrower|asks the narrower", x, re.I)]
    if cand:
        sx = cand[-1]
        q = sx.split(":", 1)[1].strip() if ":" in sx else sx
    elif dist:
        q = sentences(dist)[-1]; src = "page (closing sentence of the distinction paragraph)"
    if r["type"] == "Commentary Volume":
        f = f"/home/claude/fc-pdfs/txt/comm/{r['id']}.txt"
        if os.path.exists(f):
            t = re.sub(r"-\n(?=[a-z])", "", open(f, encoding="utf-8", errors="ignore").read()); t = re.sub(r"\s+", " ", t)
            mm = re.search(r"asks a narrower question:\s*(.+?\?)", t)
            if mm: q, src = mm.group(1).strip(), "pdf"
    out[r["id"]] = {"question": q, "distinction": dist, "source": src}
json.dump(out, open(f"{HERE}/data/questions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
import collections
print(len(out), "items;", "with question:", sum(1 for v in out.values() if v["question"]), dict(collections.Counter(v["source"][:12] for v in out.values())))
for i in ["S41", "S74", "P14", "V-acts-1", "V-pauline-4"]:
    print(i, "->", out[i]["question"][:260])
