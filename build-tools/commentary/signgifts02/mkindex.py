"""Build appg.py (verse-level index 'Where the Passages Are Read') from the rendered PDF.
usage: python3 mkindex.py out/volume.pdf
Reads each page's text and the footer page number, finds every citation with a book name,
and records the section (Preface, Thesis, ch. N, Conclusion) and the page. Appendices and the
contents page are not indexed. Never typed by hand."""
import sys, os, re, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import content
pdf = sys.argv[1]
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
BOOKS = [('Joshua','Joshua'),('Josh','Joshua'),('2 Thessalonians','2 Thessalonians'),('2 Thess','2 Thessalonians'),('Gen','Genesis'),('Judges','Judges'),('Judg','Judges'),('2 Corinthians','2 Corinthians'),('2 Cor','2 Corinthians'),('Galatians','Galatians'),('Gal','Galatians'),('Philippians','Philippians'),('Phil','Philippians'),('1 Timothy','1 Timothy'),('1 Tim','1 Timothy'),('2 Timothy','2 Timothy'),('2 Tim','2 Timothy'),('Rom','Romans'),('1 Kgs','1 Kings'),('Mark','Mark'),('John','John'),('James','James'),('2 Chronicles','2 Chronicles'),('2 Chr','2 Chronicles'),('Genesis','Genesis'),('Exodus','Exodus'),('Exod','Exodus'),('Lamentations','Lamentations'),('Lam','Lamentations'),('Joel','Joel'),('Habakkuk','Habakkuk'),('Hab','Habakkuk'),('Matthew','Matthew'),('Matt','Matthew'),('1 John','1 John'),('1 Corinthians','1 Corinthians'),('1 Cor','1 Corinthians'),('1 Thessalonians','1 Thessalonians'),('1 Thess','1 Thessalonians'),('Micah','Micah'),('Mic','Micah'),('Hosea','Hosea'),('Hos','Hosea'),('Zechariah','Zechariah'),('Zech','Zechariah'),('Ps','Psalms'),('Numbers','Numbers'),('Deuteronomy','Deuteronomy'),('1 Samuel','1 Samuel'),('1 Kings','1 Kings'),('Psalms','Psalms'),('Psalm','Psalms'),('Isaiah','Isaiah'),('Jeremiah','Jeremiah'),('Ezekiel','Ezekiel'),('Jonah','Jonah'),('Amos','Amos'),('Malachi','Malachi'),('Micah','Micah'),
         ('Acts','Acts'),('Hebrews','Hebrews'),('1 Peter','1 Peter'),('2 Peter','2 Peter'),('Revelation','Revelation'),('Romans','Romans'),
         ('Num','Numbers'),('Nahum','Nahum'),('Nah','Nahum'),('Obadiah','Obadiah'),('Obad','Obadiah'),('Zephaniah','Zephaniah'),('Zeph','Zephaniah'),('2 Kings','2 Kings'),('Luke','Luke'),('Daniel','Daniel'),('Dan','Daniel'),('Deut','Deuteronomy'),('Jer','Jeremiah'),('Ezek','Ezekiel'),('Isa','Isaiah'),('Mal','Malachi'),('Heb','Hebrews'),('1 Pet','1 Peter'),('2 Pet','2 Peter'),('1 Kings','1 Kings')]
ORDER = ['Genesis','Exodus','Numbers','Deuteronomy','Joshua','Judges','1 Samuel','1 Kings','2 Kings','2 Chronicles','Psalms','Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk','Zephaniah','Zechariah','Malachi','Matthew','Mark','Luke','John','Acts','Romans','1 Corinthians','2 Corinthians','Galatians','Philippians','1 Thessalonians','2 Thessalonians','1 Timothy','2 Timothy','1 John','Hebrews','James','1 Peter','2 Peter','Revelation']
bk = '|'.join(re.escape(a) for a, _ in sorted(BOOKS, key=lambda x: -len(x[0])))
SPEC = r'\d{1,3}(?:\s*[–-]\s*\d{1,3})?(?:\s*,\s*\d{1,3}(?:\s*[–-]\s*\d{1,3})?)*'
CIT = re.compile(r'(?<![A-Za-z0-9])(' + bk + r')\s+(\d{1,3}):(' + SPEC + r')((?:\s*;\s*\d{1,3}:' + SPEC + r')*)')
CH = re.compile(r'(\d{1,3}):(' + SPEC + r')')
canon = dict(BOOKS)
def fixob(t): return re.sub(r'\b(Obadiah|Obad)\s+(?!1:)(\d{1,2}(?:\s*[–-]\s*\d{1,2})?)(?!\s*:)', r'\1 1:\2', t)
h1s = [e[1] for e in content.ALL if e[0] == 'h1']
sections = {t: t for t in h1s}
def label(t):
    m = re.match(r'^(\d+)\.\s', t)
    return 'ch. %s' % m.group(1) if m else t
skip = lambda t: t.startswith('Appendix') or t == 'Bibliography' or t == 'Table of Contents'
def norm(s): return re.sub(r'\s+', '', s).replace('-', '–')
def span(spec):
    out = []
    for seg in spec.split(','):
        seg = norm(seg)
        a, _, b = seg.partition('–'); out.append((int(a), int(b or a)))
    return out
pages = []
for i in range(1, n + 1):
    t = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), pdf, '-'], capture_output=True, text=True).stdout
    pages.append(t)
# footer number of a page is its pdf index (cover is page 1 -> index 0, contents is footer 1)
found = {}   # (book, normalized citation text) -> {(label, page)}
cur = None
prev = None   # (section, footer, last chunk text) of the previous page
for idx in range(3, n + 1):                      # skip cover (1) and contents (2): pdf page idx -> footer idx-1
    footer = idx - 1
    lines = [re.sub(r'\s+', ' ', l).strip() for l in pages[idx - 1].splitlines()]
    lines = [l for l in lines if l]
    # drop the footer line
    lines = [l for l in lines if not l.startswith('ZAY-MARIE PRESS')]
    # split page into (section, text) runs at heading lines
    chunks = []; buf = []; sec = cur
    j = 0
    while j < len(lines):
        hit = None
        for k in (1, 2, 3):
            cand = ' '.join(lines[j:j + k])
            if cand in sections and (cand != sec or True):
                hit = (cand, k); break
        if hit:
            if buf: chunks.append((sec, fixob(' '.join(buf)))); buf = []
            sec = hit[0]; j += hit[1]; continue
        buf.append(lines[j]); j += 1
    if buf: chunks.append((sec, fixob(' '.join(buf))))
    cur = sec
    # a citation split by a page break is credited to the page it begins on
    if prev and chunks and chunks[0][0] == prev[0] and not skip(prev[0]):
        tail = prev[2][-60:]
        both = tail + ' ' + chunks[0][1][:60]
        for m in CIT.finditer(both):
            if m.start() < len(tail) and m.end() > len(tail) + 1:
                book = canon[m.group(1)]
                cites = [m.group(2) + ':' + norm(m.group(3))] + [norm(r.strip().lstrip(';').strip()) for r in re.findall(r';\s*\d{1,3}:' + SPEC, m.group(4))]
                for c in cites: found.setdefault((book, c), set()).add((label(prev[0]), prev[1]))
    prev = (chunks[-1][0], footer, chunks[-1][1]) if chunks else prev
    for sec, txt in chunks:
        if sec is None or skip(sec): continue
        for m in CIT.finditer(txt):
            book = canon[m.group(1)]
            first = m.group(2) + ':' + norm(m.group(3))
            rest = [r.strip().lstrip(';').strip() for r in re.findall(r';\s*\d{1,3}:' + SPEC, m.group(4))]
            cites = [first] + [norm(r) for r in rest]
            for c in cites:
                found.setdefault((book, c), set()).add((label(sec), footer))
# canonical order
def key(item):
    (book, c), _ = item
    ch, _, sp = c.partition(':')
    a, b = span(sp)[0]
    return (ORDER.index(book), int(ch), a, b, c)
# key-passage ranges printed in Appendix D
import appf as _af
_CN={'Exod':'Exodus','Deut':'Deuteronomy','Heb':'Hebrews','1Kgs':'1 Kings','2Kgs':'2 Kings','Mal':'Malachi','Luke':'Luke','John':'John','Matt':'Matthew','Mark':'Mark','Acts':'Acts','Rev':'Revelation','Jer':'Jeremiah','Isa':'Isaiah','Ezek':'Ezekiel','Jonah':'Jonah','Nah':'Nahum','Amos':'Amos','Obad':'Obadiah','Zeph':'Zephaniah','Joel':'Joel','Zech':'Zechariah','1Cor':'1 Corinthians','2Cor':'2 Corinthians'}
KEYP = {}
for _t, _parts in _af._L:
    for _b, _c, _r in _parts:
        KEYP.setdefault((_CN[_b], _c), []).extend(_r)
def inkey(book, c):
    ch, _, sp = c.partition(':'); ch = int(ch)
    rngs = KEYP.get((book, ch))
    if rngs is None: return False
    if isinstance(rngs, tuple): rngs = [rngs]
    return all(any(lo <= a and b <= hi for lo, hi in rngs) for a, b in span(sp))
rows = [('Passage', 'Where it is read', 'Key passage')]
secord = {label(t): i for i, t in enumerate(h1s)}
for (book, c), locs in sorted(found.items(), key=key):
    bysec = {}
    for lab, p in sorted(locs, key=lambda x: (secord[x[0]], x[1])): bysec.setdefault(lab, []).append(p)
    where = '; '.join('%s, p. %d' % (l, ps[0]) if len(ps) == 1 else '%s, pp. %s' % (l, ', '.join(map(str, ps))) for l, ps in bysec.items())
    rows.append(('%s %s' % (book, c.replace(',', ', ')), where, 'In full, Appendix D' if inkey(book, c) else ''))
intro = ('Every passage cited in the chapters, the Preface, the Thesis and the Conclusion, in the order of the Bible, with the pages on which it is read. '
         'Each citation is listed as written in the text. The appendices are not indexed. A page number is the number in the footer.')
out = 'APPG = [\n("h1", "Appendix E. Where the Passages Are Read"),\n("p", %r),\n("ctbl", %r, %r, [0.25, 0.50, 0.25]),\n]\n' % (intro, 'The passages in the order of the Bible.', rows)
open(os.path.join(HERE, 'appg.py'), 'w', encoding='utf-8').write(out)
print('index rows:', len(rows) - 1)
