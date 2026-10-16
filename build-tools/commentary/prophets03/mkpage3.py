"""Build commentary-prophets-03-the-nations-judged.html from the Volume 2 page (same template). Run from the repo root."""
import re, sys, html
sys.path.insert(0, 'build-tools/commentary/prophets03')
import kjvlib as k
SRC = 'commentary-prophets-02-what-the-prophets-condemned.html'
DST = 'commentary-prophets-03-the-nations-judged.html'
L = open(SRC, encoding='utf-8').read().split('\n')
assert len(L) == 42 or len(L) == 43, len(L)
OLD_SLUG = 'commentary-prophets-02-what-the-prophets-condemned'; NEW_SLUG = 'commentary-prophets-03-the-nations-judged'
SUB = 'The Grounds, the Terms, and the Endings the LORD Gave Each Nation'
DESC = ('The Prophets Series, Volume 3, reads the oracles against Nineveh, Damascus, Philistia, Moab, Ammon, Elam, Egypt and Tyre — Jonah 3, Nahum, Amos 1 and 2, '
        'Jeremiah 25 and 46–49, Isaiah 19, 20 and 23, Ezekiel 26 and 28–30, Obadiah, Zephaniah 3 and Zechariah 14 — argues that each names its own ground, term and ending, '
        'and that some are closed, some part-fulfilled and some held open for the Kingdom, and answers the strongest objections by name.')
def head(s):
    s = s.replace(OLD_SLUG, NEW_SLUG).replace('What the Prophets Condemned', 'The Nations Judged')
    s = s.replace('The Worshipers, the Worship, and the Offerings the LORD Appointed', SUB)
    s = re.sub(r'(content=")The Prophets Series, Volume 2, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = re.sub(r'("description": ")The Prophets Series, Volume 2, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = s.replace('prophets-02-', 'prophets-03-').replace('"position": 2', '"position": 3').replace('"numberOfPages": 57', '"numberOfPages": 60')
    s = s.replace('VOLUME&nbsp;2', 'VOLUME&nbsp;3').replace('57 Pages', '60 Pages').replace('57-page', '60-page').replace('57-Page', '60-Page')
    return s
L = [head(x) for x in L]
def setl(n, s): L[n - 1] = s
setl(9, '<p class="detail-kicker">Were the oracles against Egypt, Tyre, Moab and Nineveh all fulfilled long ago, all still to come, or all about the church? What does each oracle say of its own ground, its term and its ending?</p>')
setl(10, '<p class="detail-copy">Jonah goes to Nineveh and the city turns. Nahum later gives its sentence, and no word of return is attached. Jeremiah says the LORD will bring again the captivity of Moab in the latter days. Ezekiel says Nebuchadrezzar had no wages for Tyre, and gives him Egypt. Isaiah says Egypt will be called “my people.” Are these one prophecy on one timeline?</p>')
setl(11, '<p class="detail-copy">It argues that they are not. Each oracle names a ground, a term and an ending, and the text sorts them into those that are closed, those that are part-fulfilled and those that are open. The open ones it holds for the Kingdom, as nations blessed through Israel’s restored line. In Chapter 9 it sets its reading beside modern writers who see it differently.</p>')
setl(17, '<p class="lead">This volume does not list the views held about the oracles against the nations and leave the choice to the reader. It says what the author believes each oracle is: what it names as its ground, what it names as its term, what it says comes after, and whether the text itself reports it done. It gives the evidence from the prophets’ own sentences and answers the strongest objections by name.</p>')
setl(18, '<p class="lead">It is the third volume of The Prophets Series, each volume of which is built around one narrower question the prophets raise themselves, not a walk through the prophetic books. <a href="commentary-prophets-01-how-the-prophets-spoke.html">Volume 1</a> asks how the prophets say a word of the LORD is known, and <a href="commentary-prophets-02-what-the-prophets-condemned.html">Volume 2</a> asks what they condemned in Israel’s worship; this volume asks what each oracle against a nation says of its own ground, term and ending. Babylon, Edom and Revelation 17 and 18 stay with the volumes that read them. It is a different kind of book from the Digital Studies, which report what a passage says. Scripture is quoted from the King James Version throughout, checked word for word, and the writers named in Chapter 9 are quoted only from texts the author has read.</p>')
def rr(href, label, note): return '<p><a href="%s">%s</a> %s</p>' % (href, label, note)
ds = ''.join([
 rr('study-31-the-judgments-of-scripture.html', 'Study 31 — The Judgments of Scripture', 'Sets the judgments of Scripture side by side as the passages state them; this volume argues what each oracle against a nation says of its own ground, term and ending.'),
 rr('study-07-the-day-of-the-lord.html', 'Study 7 — The Day of the Lord', 'Reads the day of the LORD through judgment and restoration; this volume takes Joel 3 and Zephaniah 3:8 only as they tie the oracles to a day.'),
 rr('study-27-israels-seven-appointed-feasts.html', 'Study 27 — Israel’s Seven Appointed Feasts', 'Reads the feast of tabernacles inside Leviticus 23; this volume reads Zechariah 14:16–19 only for the nations that go up to keep it.')])
cs = ''.join([
 rr('commentary-05-armageddon-and-the-winepress.html', 'Prophetic Commentary Series, Volume 5 — Armageddon and the Winepress', 'Argues the gathering, the campaign and the coming of Revelation 14, 16 and 19 and Isaiah 63; this volume reads Edom and the cup only as the oracles tie them to a day and leaves that campaign there.'),
 rr('commentary-prophecy-mystery-05-separate-courts.html', 'Prophecy &amp; Mystery Commentary Series, Volume 5 — Separate Courts', 'Argues the separate courts of judgment, the living nations of Matthew 25 among them; this volume reads the oracles against the nations and sets Joel 3 and Zephaniah 3:8 into no court.'),
 rr('commentary-prophecy-mystery-03-the-kingdom-program.html', 'Prophecy &amp; Mystery Commentary Series, Volume 3 — The Kingdom Program', 'Argues the Kingdom promised to Israel on the earth; this volume reads the open clauses of the oracles as nations blessed through that restored line.')])
bb = ''.join(rr('packet-%s.html' % s, 'Bible Book Companion — %s' % n, 'Interprets the book of %s through its key passages.' % n) for s, n in (('isaiah', 'Isaiah'), ('jeremiah', 'Jeremiah'), ('ezekiel', 'Ezekiel')))
setl(19, '<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-col"><h4>Digital Studies</h4>%s</div><div class="rel-col"><h4>Commentary Series</h4>%s</div><div class="rel-col"><h4>Bible Book Companion Series</h4>%s</div></div><p class="connection-guide-link"><a href="commentary.html#prophets">See The Prophets Series →</a></p></div>' % (ds, cs, bb))
setl(21, '<h2>From the Nature of an Oracle to the Objections</h2>')
pts = [('What an Oracle Is', 'Read Jeremiah 1:10, Jeremiah 18:7–10 and the cup of Jeremiah 25, and mark the four ways Scripture reports an oracle fulfilled.'),
 ('The Grounds', 'Trace violence, betrayal, gloating, pride and idols through Amos 1 and 2, Obadiah and Ezekiel 25, and note what each oracle names as its reason.'),
 ('Nineveh and the Near Nations', 'Follow Jonah 3, Nahum and Zephaniah 2:13–15, then Damascus, Philistia, Moab, Ammon and Elam, and mark which sentences carry a clause of return.'),
 ('Egypt and Tyre', 'Read Isaiah 19 and 20, Jeremiah 46, Isaiah 23 and Ezekiel 26 and 28 to 30, noting what the text reports done and what it states further.'),
 ('The Cup and the Day', 'Follow the measure through Jeremiah 25, Obadiah 15, Zephaniah 3:8 and Joel 3, and see how each sentence is cut to its ground.'),
 ('The Nations That Come, and the Objections', 'Read Isaiah 2, Zephaniah 3 and Zechariah 8 and 14, then hear named modern writers who read the oracles differently and weigh each reply.')]
setl(23, ''.join('<div class="study-point"><h3>%s</h3><p>%s</p></div>' % p for p in pts))
cards = [('Jeremiah', 25, 15, 'Jeremiah 25:15'), ('Jonah', 3, 10, 'Jonah 3:10'), ('Jeremiah', 48, 47, 'Jeremiah 48:47'), ('Isaiah', 19, 25, 'Isaiah 19:25'),
         ('Ezek', 29, 18, 'Ezekiel 29:18'), ('Obad', 1, 15, 'Obadiah 15'), ('Zeph', 3, 9, 'Zephaniah 3:9'), ('Zech', 14, 16, 'Zechariah 14:16')]
def vt(b, c, v):
    b = {'Jeremiah': 'Jer', 'Isaiah': 'Isa'}.get(b, b)
    return html.escape(k.V[(b, c, v)], quote=False)
setl(27, ''.join('<div class="scripture-card"><h3>%s</h3><p>“%s”</p></div>' % (lab, vt(b, c, v)) for b, c, v, lab in cards))
setl(30, '<div class="excerpt"><blockquote>Each oracle against a nation names a ground, a term and an ending. Some are closed, some are part-fulfilled and some are open, and the text itself says which.</blockquote>')
setl(31, '<p>A sentence on one nation is not a sentence on every nation, and a word of return attached to one oracle is not a word attached to all. The volume asks each oracle what it says of its own ground, term and ending, and the reader will see where the sentences fall.</p></div> <div class="eyebrow" id="look-inside">A LOOK INSIDE</div>')
def pc(P, alt, title, note): return '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/prophets-03-page-%d.jpg"><img src="assets/prophets-03-page-%d.jpg" alt="Volume 3 %s"></a><div class="page-no">Interior Page %d</div><h3>%s</h3><p>%s</p></div>' % (P, P, alt, P, title, note)
setl(35, ''.join([pc(1, 'table of contents', 'Table of Contents', 'See the full order of the argument, from the Preface to the Bibliography.'),
 pc(2, 'preface', 'Preface', 'See the position stated plainly and how the volume proceeds.'),
 pc(19, 'Isaiah 19 read in order', 'The Argument at Work', 'See the method: Isaiah 19 read in order, the “in that day” verses set out, and what the text says and does not say.'),
 pc(34, 'objections and replies', 'Objections and Replies', 'See the modern writers named on both sides, each position described as read, and the answer to it.')]))
setl(37, '<h2>A Full Commentary on the Nations Judged</h2>')
inc = [('60-Page Digital PDF', 'Cover and a fully numbered interior.'), ('Nine Chapters', 'From the nature of an oracle to the objections and replies.'),
 ('Objections and Replies', 'Modern writers named on both sides, each objection answered from the text.'),
 ('Passage by Passage', 'Jonah 3, Nahum, Amos 1 and 2, Jeremiah 25 and 46 to 49, Isaiah 19, 20 and 23, Ezekiel 26 and 28 to 30, Obadiah, Zephaniah 3, Joel 3, Isaiah 2 and Zechariah 8 and 14 read in order, with what each leaves unsaid.'),
 ('Comparison Tables', 'Each nation’s ground set beside its term, its ending and its class.'), ('Conclusion', 'The position restated in full, with a closing table.'),
 ('Five Appendices', 'The oracles at a glance, the key words in Roman letters, study questions, the key passages in full and a verse-by-verse index of where the passages are read.'),
 ('Bibliography', 'Every work cited, listed by author and title.')]
setl(39, ''.join('<div class="include-item"><h3>%s</h3><p>%s</p></div>' % i for i in inc))
open(DST, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', DST, len(L))
