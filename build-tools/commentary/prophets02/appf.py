import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
def blks(book, ch, rngs):
    return '  …  '.join(blk(book, ch, a, b) for a, b in rngs)
_L = [
 ("1 Samuel 15:17–26", [('1Sam',15,[(17,26)])]),
 ("Psalm 40:6–8; 50:7–15", [('Ps',40,[(6,8)]),('Ps',50,[(7,15)])]),
 ("Psalm 51:16–19", [('Ps',51,[(16,19)])]),
 ("Isaiah 1:10–20", [('Isa',1,[(10,20)])]),
 ("1 Kings 12:26–33", [('1Kgs',12,[(26,33)])]),
 ("Amos 4:4, 5; 5:21–27", [('Amos',4,[(4,5)]),('Amos',5,[(21,27)])]),
 ("Hosea 6:1–6; 14:1–3", [('Hos',6,[(1,6)]),('Hos',14,[(1,3)])]),
 ("Micah 6:6–8", [('Mic',6,[(6,8)])]),
 ("Jeremiah 6:19, 20; 7:1–11", [('Jer',6,[(19,20)]),('Jer',7,[(1,11)])]),
 ("Jeremiah 7:12–15, 21–23, 31", [('Jer',7,[(12,15),(21,23),(31,31)])]),
 ("Isaiah 58:1–7", [('Isa',58,[(1,7)])]),
 ("Isaiah 56:6, 7; 66:1–4, 20, 21", [('Isa',56,[(6,7)]),('Isa',66,[(1,4),(20,21)])]),
 ("Zechariah 7:4–14; 8:19", [('Zech',7,[(4,14)]),('Zech',8,[(19,19)])]),
 ("Malachi 1:6–14", [('Mal',1,[(6,14)])]),
 ("Malachi 2:1–9; 3:3, 4", [('Mal',2,[(1,9)]),('Mal',3,[(3,4)])]),
 ("Ezekiel 20:11–13, 21–26, 40, 41", [('Ezek',20,[(11,13),(21,26),(40,41)])]),
 ("Hebrews 10:1–10", [('Heb',10,[(1,10)])]),
]
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold. A row of dots marks a gap between verses."),
]
for i, (t, parts) in enumerate(_L, 1):
    APPF.append(("sub", "D.%d %s" % (i, t)))
    APPF.append(("p", '  …  '.join(blks(b, c, r) for b, c, r in parts)))
