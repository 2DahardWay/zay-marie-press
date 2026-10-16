import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("Jeremiah 1:5, 10; 18:7–10", [('Jer',1,[(5,5),(10,10)]),('Jer',18,[(7,10)])]),
 ("Jeremiah 25:12–17, 26, 29–33", [('Jer',25,[(12,17),(26,26),(29,33)])]),
 ("Jonah 3:4–10", [('Jonah',3,[(4,10)])]),
 ("Nahum 1:1; 3:1–7", [('Nah',1,[(1,1)]),('Nah',3,[(1,7)])]),
 ("Amos 1:3–5; 9:7", [('Amos',1,[(3,5)]),('Amos',9,[(7,7)])]),
 ("Jeremiah 48:47; 49:2, 6, 39", [('Jer',48,[(47,47)]),('Jer',49,[(2,2),(6,6),(39,39)])]),
 ("Isaiah 19:1–4, 16–25", [('Isa',19,[(1,4),(16,25)])]),
 ("Jeremiah 46:26; Ezekiel 29:13–20", [('Jer',46,[(26,26)]),('Ezek',29,[(13,20)])]),
 ("Isaiah 23:1, 15–18", [('Isa',23,[(1,1),(15,18)])]),
 ("Ezekiel 26:3–14", [('Ezek',26,[(3,14)])]),
 ("Ezekiel 28:1–10", [('Ezek',28,[(1,10)])]),
 ("Obadiah 10–21", [('Obad',1,[(10,21)])]),
 ("Zephaniah 3:8–10, 20", [('Zeph',3,[(8,10),(20,20)])]),
 ("Joel 3:1–8", [('Joel',3,[(1,8)])]),
 ("Isaiah 2:2–4", [('Isa',2,[(2,4)])]),
 ("Zechariah 8:20–23; 14:16–21", [('Zech',8,[(20,23)]),('Zech',14,[(16,21)])]),
]
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "D.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
