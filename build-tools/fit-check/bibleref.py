"""Bible reference parsing for the Fit Check Map.

A passage is stored as an interval on a linear key: key = chapter * 1000 + verse.
A whole chapter is (ch*1000+1, ch*1000+999). No verse counts are needed, because
overlap is interval intersection within one book.

parse_ref("Isaiah 52:13–53:12; 54:5")  -> [("Isa", 52013, 53012), ("Isa", 54005, 54005)]
find_refs(text)                         -> list of (matched_text, intervals)
"""
import re

# canonical code, full name, aliases (matched case-sensitively, optional trailing period)
BOOKS = [
    ("Gen", "Genesis", ["Genesis", "Gen"]),
    ("Exod", "Exodus", ["Exodus", "Exod", "Ex"]),
    ("Lev", "Leviticus", ["Leviticus", "Lev"]),
    ("Num", "Numbers", ["Numbers", "Num"]),
    ("Deut", "Deuteronomy", ["Deuteronomy", "Deut"]),
    ("Josh", "Joshua", ["Joshua", "Josh"]),
    ("Judg", "Judges", ["Judges", "Judg"]),
    ("Ruth", "Ruth", ["Ruth"]),
    ("1Sam", "1 Samuel", ["1 Samuel", "1 Sam"]),
    ("2Sam", "2 Samuel", ["2 Samuel", "2 Sam"]),
    ("1Kgs", "1 Kings", ["1 Kings", "1 Kgs"]),
    ("2Kgs", "2 Kings", ["2 Kings", "2 Kgs"]),
    ("1Chr", "1 Chronicles", ["1 Chronicles", "1 Chr"]),
    ("2Chr", "2 Chronicles", ["2 Chronicles", "2 Chr"]),
    ("Ezra", "Ezra", ["Ezra"]),
    ("Neh", "Nehemiah", ["Nehemiah", "Neh"]),
    ("Esth", "Esther", ["Esther", "Esth"]),
    ("Job", "Job", ["Job"]),
    ("Ps", "Psalms", ["Psalms", "Psalm", "Ps"]),
    ("Prov", "Proverbs", ["Proverbs", "Prov"]),
    ("Eccl", "Ecclesiastes", ["Ecclesiastes", "Eccl"]),
    ("Song", "Song of Solomon", ["Song of Solomon", "Song of Songs"]),
    ("Isa", "Isaiah", ["Isaiah", "Isa"]),
    ("Jer", "Jeremiah", ["Jeremiah", "Jer"]),
    ("Lam", "Lamentations", ["Lamentations", "Lam"]),
    ("Ezek", "Ezekiel", ["Ezekiel", "Ezek"]),
    ("Dan", "Daniel", ["Daniel", "Dan"]),
    ("Hos", "Hosea", ["Hosea", "Hos"]),
    ("Joel", "Joel", ["Joel"]),
    ("Amos", "Amos", ["Amos"]),
    ("Obad", "Obadiah", ["Obadiah", "Obad"]),
    ("Jonah", "Jonah", ["Jonah"]),
    ("Mic", "Micah", ["Micah", "Mic"]),
    ("Nah", "Nahum", ["Nahum", "Nah"]),
    ("Hab", "Habakkuk", ["Habakkuk", "Hab"]),
    ("Zeph", "Zephaniah", ["Zephaniah", "Zeph"]),
    ("Hag", "Haggai", ["Haggai", "Hag"]),
    ("Zech", "Zechariah", ["Zechariah", "Zech"]),
    ("Mal", "Malachi", ["Malachi", "Mal"]),
    ("Matt", "Matthew", ["Matthew", "Matt"]),
    ("Mark", "Mark", ["Mark"]),
    ("Luke", "Luke", ["Luke"]),
    ("John", "John", ["John"]),
    ("Acts", "Acts", ["Acts"]),
    ("Rom", "Romans", ["Romans", "Rom"]),
    ("1Cor", "1 Corinthians", ["1 Corinthians", "1 Cor"]),
    ("2Cor", "2 Corinthians", ["2 Corinthians", "2 Cor"]),
    ("Gal", "Galatians", ["Galatians", "Gal"]),
    ("Eph", "Ephesians", ["Ephesians", "Eph"]),
    ("Phil", "Philippians", ["Philippians", "Phil"]),
    ("Col", "Colossians", ["Colossians", "Col"]),
    ("1Thess", "1 Thessalonians", ["1 Thessalonians", "1 Thess"]),
    ("2Thess", "2 Thessalonians", ["2 Thessalonians", "2 Thess"]),
    ("1Tim", "1 Timothy", ["1 Timothy", "1 Tim"]),
    ("2Tim", "2 Timothy", ["2 Timothy", "2 Tim"]),
    ("Titus", "Titus", ["Titus"]),
    ("Phlm", "Philemon", ["Philemon", "Phlm"]),
    ("Heb", "Hebrews", ["Hebrews", "Heb"]),
    ("Jas", "James", ["James", "Jas"]),
    ("1Pet", "1 Peter", ["1 Peter", "1 Pet"]),
    ("2Pet", "2 Peter", ["2 Peter", "2 Pet"]),
    ("1John", "1 John", ["1 John"]),
    ("2John", "2 John", ["2 John"]),
    ("3John", "3 John", ["3 John"]),
    ("Jude", "Jude", ["Jude"]),
    ("Rev", "Revelation", ["Revelation", "Rev"]),
]
ORDER = {code: i for i, (code, _, _) in enumerate(BOOKS)}
NAME = {code: full for code, full, _ in BOOKS}
ALIAS = {}
for code, full, al in BOOKS:
    for a in al:
        ALIAS[a] = code
SINGLE_CHAPTER = {"Obad", "Phlm", "2John", "3John", "Jude"}

_names = sorted(ALIAS, key=len, reverse=True)
_book_rx = "|".join(re.escape(n) for n in _names)
DASH = r"[–—\-]"
# a reference tail: digits, colons, dashes, commas, semicolons, spaces and 'and'
_TAIL = r"(?:\d+(?::\d+)?(?:\s*" + DASH + r"\s*\d+(?::\d+)?)?)"
_REF_RX = re.compile(
    r"(?<![A-Za-z])(" + _book_rx + r")\.?\s+(" + _TAIL + r"(?:\s*[,;]\s*(?:" + _book_rx + r"\.?\s+)?" + _TAIL + r")*)"
)


def _iv(code, c1, v1, c2, v2):
    return (code, c1 * 1000 + v1, c2 * 1000 + v2)


def _parse_tail(code, tail):
    """Parse the chapter/verse tail for one book into intervals."""
    out = []
    ch = None          # current chapter (for verse-only continuations)
    verse_mode = False  # True once a colon has been seen in this book run
    segs = re.split(r"\s*[;,]\s*", tail.strip())
    for seg in segs:
        seg = seg.strip()
        if not seg:
            continue
        # a new book name inside the list (e.g. "Isa 7:14; Matt 1:23") is handled by the caller
        m = re.match(r"^(\d+):(\d+)(?:\s*" + DASH + r"\s*(?:(\d+):)?(\d+))?$", seg)
        if m:
            ch = int(m.group(1)); v1 = int(m.group(2))
            if m.group(4) is None:
                out.append(_iv(code, ch, v1, ch, v1))
            elif m.group(3):
                out.append(_iv(code, ch, v1, int(m.group(3)), int(m.group(4))))
            else:
                out.append(_iv(code, ch, v1, ch, int(m.group(4))))
            verse_mode = True
            continue
        m = re.match(r"^(\d+)(?:\s*" + DASH + r"\s*(\d+))?$", seg)
        if m:
            a = int(m.group(1)); b = int(m.group(2) or a)
            if code in SINGLE_CHAPTER and ch is None and not verse_mode:
                out.append(_iv(code, 1, a, 1, b)); ch = 1; verse_mode = True
            elif verse_mode and ch is not None:
                out.append(_iv(code, ch, a, ch, b))   # verses in current chapter
            else:
                out.append(_iv(code, a, 1, b, 999))   # whole chapters
            continue
        m = re.match(r"^(\d+)(?:\s*" + DASH + r"\s*(\d+):(\d+))?$", seg)
        # chapter-through-chapter:verse (rare) is not supported; skip silently
    return out


def parse_ref(text):
    """Parse one or more references in a string into intervals."""
    out = []
    for _, ivs in find_refs(text):
        out.extend(ivs)
    return out


def find_refs(text):
    """Find every reference in free text. Returns [(matched_text, [intervals])]."""
    found = []
    for m in _REF_RX.finditer(text):
        code = ALIAS[m.group(1)]
        tail = m.group(2)
        # split at embedded book names so "Isa 7:14; Matt 1:23" yields two books
        pieces = re.split(r"\s*[;,]\s*(?=(?:" + _book_rx + r")\.?\s+\d)", tail)
        ivs = []
        cur = code
        first = True
        for p in pieces:
            bm = re.match(r"^(" + _book_rx + r")\.?\s+(.*)$", p)
            if bm and not first:
                cur = ALIAS[bm.group(1)]
                p = bm.group(2)
            ivs.extend(_parse_tail(cur, p))
            first = False
        if ivs:
            found.append((m.group(0).strip(), ivs))
    return found


def fmt(code, lo, hi):
    c1, v1, c2, v2 = lo // 1000, lo % 1000, hi // 1000, hi % 1000
    name = NAME[code]
    if v1 == 1 and v2 == 999:
        return f"{name} {c1}" if c1 == c2 else f"{name} {c1}–{c2}"
    if c1 == c2:
        return f"{name} {c1}:{v1}" if v1 == v2 else f"{name} {c1}:{v1}–{v2}"
    return f"{name} {c1}:{v1}–{c2}:{v2}"


def overlap(a, b):
    """Intersection test for two (code, lo, hi) intervals."""
    return a[0] == b[0] and a[1] <= b[2] and b[1] <= a[2]


if __name__ == "__main__":
    tests = [
        "Isaiah 44:21; 48:20", "Isaiah 52:13–53:12", "Isaiah 41–53", "Matthew 5–7; Luke 6",
        "1 Corinthians 15:21–22, 45–49", "Psalms 6, 16, 49", "Jude 6", "Obadiah 1–4",
        "Isa 7:14; Matt 1:23", "Rev. 11:1–2", "Daniel 10:1–12:13", "2 John 7", "Malachi 3:1–4:6",
        "Romans 5:12–21", "Genesis 12:3", "Hosea 6:6", "1 Peter 1:10–12", "Mark 9:11–13",
    ]
    for t in tests:
        print(f"{t:36s} ->", [fmt(*iv) for iv in parse_ref(t)])
