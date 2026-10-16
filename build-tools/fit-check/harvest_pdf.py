#!/usr/bin/env python3
"""Phase 2: grade passage depth from the publisher's PDFs.

Input : text files made with `pdftotext -layout` (one per item) in a txt dir, named S01.txt, V-...txt etc.
Output: data/coverage_pdf.json   rows {item, book, lo, hi, depth, mentions, source:"pdf"}
        data/pdf_items.json      per item: pdf pages, narrower-question sentence, text length

Depth is a COUNT-BASED grade, not a reading of the argument:
  argued   named 4 or more times in the item's text
  reported 2-3 times
  cited    once
The count grade says how much the item dwells on a passage; it cannot say whether the item takes a
position. Items worth a human read are flagged when a query hits them.
"""
import json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bibleref as B

QRX = re.compile(r"([^.?!]{0,300}(?:alone answers|alone answer|narrower question|single question)[^.?!]*[.?!])", re.I)


def grade(n):
    return "argued" if n >= 4 else ("reported" if n >= 2 else "cited")


def process(txtdir, prefix_filter=None):
    cov, items = [], {}
    for f in sorted(os.listdir(txtdir)):
        if not f.endswith(".txt"):
            continue
        iid = f[:-4]
        raw = open(os.path.join(txtdir, f), encoding="utf-8", errors="ignore").read()
        text = re.sub(r"-\n(?=[a-z])", "", raw)          # un-hyphenate line breaks
        text = re.sub(r"\s+", " ", text)
        cnt = collections.Counter()
        for _, ivs in B.find_refs(text):
            for iv in ivs:
                cnt[iv] += 1
        for (code, lo, hi), k in cnt.items():
            cov.append({"item": iid, "book": code, "lo": lo, "hi": hi, "depth": grade(k), "mentions": k, "source": "pdf"})
        q = QRX.search(text)
        items[iid] = {"chars": len(text), "question": q.group(1).strip() if q else ""}
    return cov, items


if __name__ == "__main__":
    txtdir, tag = sys.argv[1], sys.argv[2]
    cov, items = process(txtdir)
    d = os.path.join(HERE, "data")
    json.dump(cov, open(os.path.join(d, f"coverage_pdf_{tag}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(items, open(os.path.join(d, f"pdf_items_{tag}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(tag, "items", len(items), "rows", len(cov), dict(collections.Counter(c["depth"] for c in cov)),
          "questions found", sum(1 for v in items.values() if v["question"]))
