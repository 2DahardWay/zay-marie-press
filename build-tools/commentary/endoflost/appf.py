import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("Daniel 12:1–3", [('Dan',12,[(1,3)])]),
 ("Isaiah 66:22–24", [('Isa',66,[(22,24)])]),
 ("Matthew 10:5–8, 16–23, 26–33", [('Matt',10,[(5,8),(16,23),(26,33)])]),
 ("Luke 12:1–5", [('Luke',12,[(1,5)])]),
 ("Mark 9:42–50", [('Mark',9,[(42,50)])]),
 ("Matthew 25:31–46", [('Matt',25,[(31,46)])]),
 ("Philippians 3:17–21", [('Phil',3,[(17,21)])]),
 ("2 Thessalonians 1:3–12", [('2Thess',1,[(3,12)])]),
 ("Jude 1:5–7, 13", [('Jude',1,[(5,7),(13,13)])]),
 ("Revelation 14:6–13", [('Rev',14,[(6,13)])]),
 ("Revelation 19:11–21", [('Rev',19,[(11,21)])]),
 ("Revelation 20:1–15", [('Rev',20,[(1,15)])]),
 ("Revelation 21:1–8", [('Rev',21,[(1,8)])]),
]
APPF = [
("h1", "Appendix B. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "B.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
