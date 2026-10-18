import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("Matthew 10:1–8", [('Matt',10,[(1,8)])]),
 ("Acts 1:15–26", [('Acts',1,[(15,26)])]),
 ("Galatians 1:1, 11–24; 2:6–9", [('Gal',1,[(1,1),(11,24)]),('Gal',2,[(6,9)])]),
 ("1 Corinthians 3:9–11; 9:1, 2; 15:7–10", [('1Cor',3,[(9,11)]),('1Cor',9,[(1,2)]),('1Cor',15,[(7,10)])]),
 ("2 Corinthians 11:1–5, 12–15; 12:11–13", [('2Cor',11,[(1,5),(12,15)]),('2Cor',12,[(11,13)])]),
 ("Ephesians 2:19–22; 3:1–13", [('Eph',2,[(19,22)]),('Eph',3,[(1,13)])]),
 ("Ephesians 4:7–16", [('Eph',4,[(7,16)])]),
 ("Acts 28:8–10", [('Acts',28,[(8,10)])]),
]
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "D.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
