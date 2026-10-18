import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("Isaiah 53:1–6", [('Isa',53,[(1,6)])]),
 ("Matthew 8:14–17", [('Matt',8,[(14,17)])]),
 ("Acts 28:8–10, 25–31", [('Acts',28,[(8,10),(25,31)])]),
 ("1 Corinthians 12:7–13, 27–31", [('1Cor',12,[(7,13),(27,31)])]),
 ("James 5:7–8, 13–20", [('Jas',5,[(7,8),(13,20)])]),
 ("Philippians 2:25–30", [('Phil',2,[(25,30)])]),
 ("2 Corinthians 12:1–10", [('2Cor',12,[(1,10)])]),
 ("1 Peter 2:19–25", [('1Pet',2,[(19,25)])]),
]
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "D.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
