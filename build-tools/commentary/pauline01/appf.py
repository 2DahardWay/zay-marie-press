import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold."),
("sub", "D.1 Romans 5:12–21"),
("p", blk('Rom', 5, 12, 21)),
("sub", "D.2 1 Corinthians 15:20–28"),
("p", blk('1Cor', 15, 20, 28)),
("sub", "D.3 1 Corinthians 15:35–58"),
("p", blk('1Cor', 15, 35, 58)),
]
