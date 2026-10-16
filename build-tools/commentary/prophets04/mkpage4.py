"""Build commentary-prophets-04-elijah-must-first-come.html from the Volume 3 page (same template). Run from the repo root."""
import re, sys, html
sys.path.insert(0, 'build-tools/commentary/prophets04')
import kjvlib as k
SRC = 'commentary-prophets-03-the-nations-judged.html'
DST = 'commentary-prophets-04-elijah-must-first-come.html'
L = open(SRC, encoding='utf-8').read().split('\n')
assert len(L) in (42, 43), len(L)
OLD_SLUG = 'commentary-prophets-03-the-nations-judged'; NEW_SLUG = 'commentary-prophets-04-elijah-must-first-come'
SUB = 'Malachi’s Promise, John’s Answer, and the Coming the Lord Still Names'
DESC = ('The Prophets Series, Volume 4, reads Malachi’s promise of Elijah the prophet before the day of the LORD — Malachi 3 and 4, 1 Kings 17–19, 2 Kings 1 and 2, Isaiah 40, Luke 1, John 1 and 3, '
        'Matthew 11 and 17, Mark 9 and Acts 3 — argues that Gabriel, John and the Lord make three statements in three settings and that the text points to a further coming of Elijah before the day, '
        'and answers the strongest objections by name.')
def head(s):
    s = s.replace(OLD_SLUG, NEW_SLUG).replace('The Nations Judged', 'Elijah Must First Come')
    s = s.replace('The Grounds, the Terms, and the Endings the LORD Gave Each Nation', SUB)
    s = re.sub(r'(content=")The Prophets Series, Volume 3, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = re.sub(r'("description": ")The Prophets Series, Volume 3, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = s.replace('prophets-03-', 'prophets-04-').replace('"position": 3', '"position": 4').replace('"numberOfPages": 60', '"numberOfPages": 55')
    s = s.replace('VOLUME&nbsp;3', 'VOLUME&nbsp;4').replace('60 Pages', '55 Pages').replace('60-page', '55-page').replace('60-Page', '55-Page')
    s = s.replace('share-commentary-prophets-03', 'share-commentary-prophets-04')
    return s
L = [head(x) for x in L]
def setl(n, s): L[n - 1] = s
setl(9, '<p class="detail-kicker">Did John the Baptist fulfil Malachi’s promise of Elijah, or does the promise still wait? What do Gabriel, John and the Lord each say, and what does the text leave unsaid?</p>')
setl(10, '<p class="detail-copy">Malachi promises Elijah the prophet before the day of the LORD. Gabriel says John will go before the Lord in the spirit and power of Elias. John, asked whether he is Elias, says, “I am not.” The Lord says, “if ye will receive it, this is Elias,” and after John’s death, “Elias truly shall first come, and restore all things.” Are these one statement?</p>')
setl(11, '<p class="detail-copy">It argues that they are three statements in three settings, and that the text points to a further coming of Elijah before the day, in Israel’s line. In Chapter 12 it sets its reading beside modern writers who agree in part and others who hold the promise closed in John.</p>')
setl(17, '<p class="lead">This volume does not list the views held on Malachi 4:5 and leave the choice to the reader. It says what the author believes the passages state: what Malachi promises, what Gabriel, John and the Lord each say in their own settings, and what the text points to. It gives the evidence from the passages and answers the strongest objections by name.</p>')
setl(18, '<p class="lead">It is the fourth volume of The Prophets Series, each volume of which is built around one narrower question the prophets raise themselves, not a walk through the prophetic books. <a href="commentary-prophets-01-how-the-prophets-spoke.html">Volume 1</a> asks how the prophets say a word of the LORD is known, <a href="commentary-prophets-02-what-the-prophets-condemned.html">Volume 2</a> what they condemned in Israel’s worship, and <a href="commentary-prophets-03-the-nations-judged.html">Volume 3</a> what each oracle against a nation says of its own ground, term and ending; this volume asks who the Elijah is that Malachi says will be sent, and whether the promise has been met. The two witnesses of Revelation 11 are set beside the question and not named. It is a different kind of book from the Digital Studies, which report what a passage says. Scripture is quoted from the King James Version throughout, checked word for word, and the writers named in Chapter 12 are quoted only from texts the author has read.</p>')
def rr(href, label, note): return '<p><a href="%s">%s</a> %s</p>' % (href, label, note)
ds = ''.join([
 rr('study-07-the-day-of-the-lord.html', 'Study 7 — The Day of the Lord', 'Reads the day of the LORD through judgment and restoration; this volume asks only who is sent before it and whether that promise has been met.'),
 rr('study-75-faith-before-the-cross.html', 'Study 75 — Faith Before the Cross', 'Records what each person before the Cross is said to have believed, John among them; this volume reads John 1 and 3 only for what John says of himself and of the one he is sent before.')])
cs = ''.join([
 rr('commentary-02-beast-false-prophet.html', 'Prophetic Commentary Series, Volume 2 — The Beast and the False Prophet', 'Argues the false prophet of Revelation 13 as the counterfeit of Elijah; this volume asks only who the genuine prophet is.'),
 rr('commentary-acts-01-what-the-twelve-were-told-and-did.html', 'Acts Commentary Series, Volume 1 — What the Twelve Were Told, and Did', 'Argues the apostles’ question in Acts 1:6 and the times of restitution in Acts 3:21; this volume cites Acts 3:21 only beside the Lord’s “restore all things.”'),
 rr('commentary-gospel-02-the-lords-ministry-to-israel.html', 'Gospel Commentary Series, Volume 2 — The Lord’s Ministry to Israel', 'Argues the Lord’s ministry to Israel, John’s errand included; this volume asks only what Gabriel, John and the Lord each say of Elias.')])
bb = ''.join(rr('packet-%s.html' % s, 'Bible Book Companion — %s' % n, 'Interprets the book of %s through its key passages.' % n) for s, n in (('malachi', 'Malachi'), ('matthew', 'Matthew'), ('luke', 'Luke')))
setl(19, '<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-col"><h4>Digital Studies</h4>%s</div><div class="rel-col"><h4>Commentary Series</h4>%s</div><div class="rel-col"><h4>Bible Book Companion Series</h4>%s</div></div><p class="connection-guide-link"><a href="commentary.html#prophets">See The Prophets Series →</a></p></div>' % (ds, cs, bb))
setl(21, '<h2>From Malachi’s Promise to the Objections</h2>')
pts = [('Malachi’s Promise', 'Read Malachi 3:1 and 4:4–6, and mark who is sent, by whom and before what.'),
 ('Elijah in Kings', 'Follow Carmel, Horeb and the whirlwind, and note what Kings says of the man and what it leaves unsaid.'),
 ('Gabriel and John', 'Read Luke 1 and John 1 and 3, and mark what Gabriel says of John, what John says of himself and what each leaves out.'),
 ('The Lord’s Words', 'Read Matthew 11 and Luke 7, then Matthew 17 and Mark 9, tracing each tense and each condition.'),
 ('The People’s Lists', 'Follow Herod, the crowds and the cross, and see how John and Elias stand in each list.'),
 ('The Objections', 'Hear named modern writers who agree in part and others who hold the promise closed in John, and weigh each reply.')]
setl(23, ''.join('<div class="study-point"><h3>%s</h3><p>%s</p></div>' % p for p in pts))
cards = [('Mal', 4, 5, 'Malachi 4:5'), ('Luke', 1, 17, 'Luke 1:17'), ('John', 1, 21, 'John 1:21'), ('Matt', 11, 14, 'Matthew 11:14'),
         ('Matt', 17, 11, 'Matthew 17:11'), ('Matt', 17, 12, 'Matthew 17:12'), ('2Kgs', 2, 15, '2 Kings 2:15'), ('Acts', 3, 21, 'Acts 3:21')]
def vt(b, c, v):
    return html.escape(k.V[(b, c, v)], quote=False)
setl(27, ''.join('<div class="scripture-card"><h3>%s</h3><p>“%s”</p></div>' % (lab, vt(b, c, v)) for b, c, v, lab in cards))
setl(30, '<div class="excerpt"><blockquote>Gabriel, John and the Lord each speak of John’s relation to Elijah in different words, and each statement stands in its own setting.</blockquote>')
setl(31, '<p>The Lord’s “shall first come” and “is come already” are two sentences spoken in order. The volume reads both in that order before it says what they mean together, and the reader will see where the text leads.</p></div> <div class="eyebrow" id="look-inside">A LOOK INSIDE</div>')
def pc(P, alt, title, note): return '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/prophets-04-page-%d.jpg"><img src="assets/prophets-04-page-%d.jpg" alt="Volume 4 %s"></a><div class="page-no">Interior Page %d</div><h3>%s</h3><p>%s</p></div>' % (P, P, alt, P, title, note)
setl(35, ''.join([pc(1, 'table of contents', 'Table of Contents', 'See the full order of the argument, from the Preface to the Bibliography.'),
 pc(2, 'preface', 'Preface', 'See the position stated plainly and how the volume proceeds.'),
 pc(26, 'the Lord’s two answers on Elias', 'The Argument at Work', 'See the method: the Lord’s two sentences on Elias read in order, with what each says and what the text leaves unsaid.'),
 pc(34, 'objections and replies', 'Objections and Replies', 'See the modern writers named on both sides, each position quoted as read, and the answer to it.')]))
setl(37, '<h2>A Full Commentary on Elijah Must First Come</h2>')
inc = [('55-Page Digital PDF', 'Cover and a fully numbered interior.'), ('Twelve Chapters', 'From Malachi’s promise to the objections and replies.'),
 ('Objections and Replies', 'Modern writers named on both sides, each objection answered from the text.'),
 ('Passage by Passage', 'Malachi 3 and 4, 1 Kings 17 to 19 and 21, 2 Kings 1 and 2, Isaiah 40, Luke 1, John 1 and 3, Matthew 11, 14, 16, 17 and 27, Mark 9, Acts 3 and Revelation 11 read in order, with what each leaves unsaid.'),
 ('Comparison Tables', 'Malachi’s two sayings, John’s descriptions, the Lord’s statements and the reasons for a further coming set side by side.'), ('Conclusion', 'The position restated in full, with a closing table.'),
 ('Five Appendices', 'The passages at a glance, the key words in Roman letters, study questions, the key passages in full and a verse-by-verse index of where the passages are read.'),
 ('Bibliography', 'Every work cited, listed by author and title.')]
setl(39, ''.join('<div class="include-item"><h3>%s</h3><p>%s</p></div>' % i for i in inc))
open(DST, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', DST, len(L))
