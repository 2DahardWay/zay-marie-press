import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("Isaiah 28:7–14", [('Isa',28,[(7,14)])]),
 ("Acts 2:1–11", [('Acts',2,[(1,11)])]),
 ("Acts 10:44–48", [('Acts',10,[(44,48)])]),
 ("Acts 19:1–7", [('Acts',19,[(1,7)])]),
 ("1 Corinthians 12:27–31", [('1Cor',12,[(27,31)])]),
 ("1 Corinthians 13:1–13", [('1Cor',13,[(1,13)])]),
 ("1 Corinthians 14:1–5", [('1Cor',14,[(1,5)])]),
 ("1 Corinthians 14:10–15", [('1Cor',14,[(10,15)])]),
 ("1 Corinthians 14:20–25", [('1Cor',14,[(20,25)])]),
 ("1 Corinthians 14:26–33, 37–40", [('1Cor',14,[(26,33),(37,40)])]),
 ("Acts 28:25–31", [('Acts',28,[(25,31)])]),
]
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "D.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
