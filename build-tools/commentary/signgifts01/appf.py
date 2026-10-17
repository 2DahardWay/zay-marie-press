import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("Exodus 4:1–9, 28–31", [('Exod',4,[(1,9),(28,31)])]),
 ("Deuteronomy 13:1–5", [('Deut',13,[(1,5)])]),
 ("1 Kings 18:36–39", [('1Kgs',18,[(36,39)])]),
 ("Isaiah 7:10–14", [('Isa',7,[(10,14)])]),
 ("Joel 2:28–32", [('Joel',2,[(28,32)])]),
 ("Matthew 12:38–40", [('Matt',12,[(38,40)])]),
 ("John 20:30, 31", [('John',20,[(30,31)])]),
 ("Mark 16:14–20", [('Mark',16,[(14,20)])]),
 ("Hebrews 2:1–4", [('Heb',2,[(1,4)])]),
 ("Acts 2:19–22", [('Acts',2,[(19,22)])]),
 ("Acts 14:1–3", [('Acts',14,[(1,3)])]),
 ("Acts 28:8–10, 23–31", [('Acts',28,[(8,10),(23,31)])]),
]
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "D.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
