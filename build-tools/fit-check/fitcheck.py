#!/usr/bin/env python3
"""Fit check query.  Usage:
    python3 -I fitcheck.py "Malachi 3:1; Matthew 11:14"          # passage check
    python3 -I fitcheck.py --text "two witnesses"                  # topic words against titles/questions
Reports who already treats each passage, at what depth and from what source, and a
provisional verdict.  Verdicts are provisional until Phase 2 (PDF depth) is complete.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bibleref as B

D = os.path.join(HERE, "data")
reg = {r["id"]: r for r in json.load(open(os.path.join(D, "registry.json"), encoding="utf-8"))}
cov = json.load(open(os.path.join(D, "coverage.json"), encoding="utf-8"))
import glob
_pdf = []
for _f in sorted(glob.glob(os.path.join(D, "coverage_pdf_*.json"))):
    _pdf += json.load(open(_f, encoding="utf-8"))
_pdf_items = {c["item"] for c in _pdf}
# an item with PDF data is graded from the PDF; its page-based rows are dropped
cov = [c for c in cov if c["item"] not in _pdf_items or c["depth"] == "book"] + _pdf
RANK = {"argued": 5, "reported": 4, "key": 3, "mentioned": 1, "listed": 1, "cited": 1, "book": 0}


def check_passage(iv):
    code, lo, hi = iv
    hits = {}
    for c in cov:
        if c["book"] == code and c["lo"] <= hi and lo <= c["hi"]:
            h = hits.setdefault(c["item"], [c["depth"], c["source"]])
            if RANK[c["depth"]] > RANK[h[0]]:
                h[0] = c["depth"]
    return hits


def verdict(hits):
    # companions and free summaries read a whole book briefly; they never count as treating a passage
    non_book = {i: h for i, h in hits.items() if h[0] != "book" and not i.startswith(("C-", "B-"))}
    keyed = [i for i, h in non_book.items() if h[0] in ("key", "argued", "reported")]
    if any(h[0] == "argued" for h in non_book.values()):
        keyed = [i for i, h in non_book.items() if h[0] == "argued"]
    if not keyed:
        return "clear (only passing mentions)" if non_book else "clear (no page treats it; book companion/summary only)"
    modes = {reg[i]["mode"] for i in keyed}
    if len(keyed) >= 4:
        return "overlap (crowded: needs a narrower question)"
    return "fit by mode or narrower question (check each neighbour's question)"


def main():
    a = sys.argv[1:]
    if a and a[0] == "--text":
        words = [w.lower() for w in " ".join(a[1:]).split()]
        for r in reg.values():
            blob = " ".join([r.get("title", ""), r.get("subtitle", ""), r.get("question", "")]).lower()
            if all(w in blob for w in words):
                print(f'{r["id"]:12s} {r["type"]:24s} {r["title"][:60]}')
        return
    for ref in B.find_refs(" ".join(a)):
        for iv in ref[1]:
            hits = check_passage(iv)
            print(f"\n== {B.fmt(*iv)}")
            for depth in ("argued", "reported", "key", "cited", "mentioned", "book"):
                ids = sorted(i for i, h in hits.items() if h[0] == depth)
                if depth == "book":
                    ids = [i for i in ids if i.startswith("C-")]
                if ids:
                    print(f"  {depth:9s} [{ 'pdf' if depth in ('argued','reported','cited') else 'page'}] " + ", ".join(f"{i} ({reg[i]['title'][:28]})" for i in ids[:14]) + (" ..." if len(ids) > 14 else ""))
            print("  verdict (provisional):", verdict(hits))


if __name__ == "__main__":
    main()
