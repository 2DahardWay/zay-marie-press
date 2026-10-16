import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("Malachi 1:1; 3:1–5; 4:4–6", [('Mal',1,[(1,1)]),('Mal',3,[(1,5)]),('Mal',4,[(4,6)])]),
 ("1 Kings 17:1; 18:36–39; 19:8–18", [('1Kgs',17,[(1,1)]),('1Kgs',18,[(36,39)]),('1Kgs',19,[(8,18)])]),
 ("2 Kings 2:1–18", [('2Kgs',2,[(1,18)])]),
 ("Isaiah 40:1–5", [('Isa',40,[(1,5)])]),
 ("Luke 1:13–17, 76–79", [('Luke',1,[(13,17),(76,79)])]),
 ("John 1:19–28; 3:27–30", [('John',1,[(19,28)]),('John',3,[(27,30)])]),
 ("Matthew 11:7–19", [('Matt',11,[(7,19)])]),
 ("Matthew 17:9–13", [('Matt',17,[(9,13)])]),
 ("Mark 9:11–13", [('Mark',9,[(11,13)])]),
 ("Acts 3:19–21", [('Acts',3,[(19,21)])]),
 ("Revelation 11:3–12", [('Rev',11,[(3,12)])]),
]
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "D.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
