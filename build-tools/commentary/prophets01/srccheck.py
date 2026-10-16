"""Every curly-quoted string that is not KJV must be inside a verified extract in source_extracts.txt."""
import re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kjvlib, content
ok = [l.strip().replace("'", '’').replace('-', '–').lower() for l in open(os.path.join(HERE, 'source_extracts.txt'), encoding='utf-8') if l.strip() and not l.startswith('#')]
Q = re.compile('“([^”]+)”'); bad = []
def scan(s):
    for m in Q.finditer(s):
        for p in [x.strip() for x in re.split(r'…|\.\.\.', m.group(1)) if x.strip()]:
            if kjvlib.in_corpus(p): continue
            q = p.rstrip('.,').lower().replace('-', '–')
            if not any(q in e for e in ok): bad.append(p)
for el in content.ALL:
    if el[0] in ('p', 'sub', 'h1', 'bib'): scan(el[1])
    elif el[0] == 'call': scan(el[2])
    elif el[0] in ('bul', 'num'): [scan(t) for t in el[1]]
    elif el[0] in ('tbl', 'ctbl'):
        scan(el[1]); [scan(c) for r in el[2] for c in r]
print('unverified non-KJV quotations:', len(bad)); [print('  ', b) for b in bad]
