import kjvlib as k
def blk(book, ch, a, b):
    return '  '.join('**%d** %s' % (v, k.V[(book, ch, v)]) for v in range(a, b + 1))
APPF = [
("h1", "Appendix D. The Key Passages in Full"),
("p", "The passages on which the volume turns are given here in full, so that a reader can test the argument against the whole text and not only against the verses quoted in the chapters. Verse numbers are in bold."),
("sub", "D.1 Romans 14:1–23"),
("p", blk('Rom', 14, 1, 23)),
("sub", "D.2 Romans 15:1–7"),
("p", blk('Rom', 15, 1, 7)),
("sub", "D.3 1 Corinthians 8:1–13"),
("p", blk('1Cor', 8, 1, 13)),
("sub", "D.4 1 Corinthians 9:19–27"),
("p", blk('1Cor', 9, 19, 27)),
("sub", "D.5 1 Corinthians 10:14–33"),
("p", blk('1Cor', 10, 14, 33)),
("sub", "D.6 Galatians 5:1–6"),
("p", blk('Gal', 5, 1, 6)),
("sub", "D.7 Galatians 5:13–26"),
("p", blk('Gal', 5, 13, 26)),
("sub", "D.8 Colossians 2:16–23"),
("p", blk('Col', 2, 16, 23)),
("sub", "D.9 1 Corinthians 6:9–20"),
("p", blk('1Cor', 6, 9, 20)),
]
