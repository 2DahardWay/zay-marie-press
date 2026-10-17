"""Build commentary-sign-gifts-02-tongues-and-prophecy.html from the Volume 1 page (same template). Run from the repo root."""
import re, sys, html
sys.path.insert(0, 'build-tools/commentary/signgifts02')
import kjvlib as k
SRC = 'commentary-sign-gifts-01-the-sign-gifts.html'
DST = 'commentary-sign-gifts-02-tongues-and-prophecy.html'
L = open(SRC, encoding='utf-8').read().split('\n')
assert len(L) in (42, 43), len(L)
SUB = 'Whether Tongues and Prophecy Continue in the Body'
DESC = ('The Sign Gifts Series, Volume 2, reads 1 Corinthians 12 to 14 with Isaiah 28 and the three instances of tongues in Acts, argues that the tongues are languages given as a sign to unbelieving Israel, '
        'that the Corinthian gifts belonged to the overlap and ended with the national suspension at Acts 28, and rules on the strongest objections by name.')
def head(s):
    s = s.replace('sign-gifts-01-the-sign-gifts', 'sign-gifts-02-tongues-and-prophecy').replace('sign-gifts-01-', 'sign-gifts-02-')
    s = s.replace('<title>The Sign Gifts |', '<title>Tongues and Prophecy |').replace('content="The Sign Gifts"', 'content="Tongues and Prophecy"')
    s = s.replace('The Purpose of Signs, Their Audience, and Their Programmatic End at Acts 28', SUB)
    s = re.sub(r'(content=")The Sign Gifts Series, Volume 1, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = re.sub(r'("description": ")The Sign Gifts Series, Volume 1, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = s.replace('"position": 1', '"position": 2').replace('VOLUME&nbsp;1', 'VOLUME&nbsp;2')
    s = s.replace('content="The Sign Gifts"', 'content="Tongues and Prophecy"').replace('<h2>The Sign Gifts</h2>', '<h2>Tongues and Prophecy</h2>').replace('<h1>The Sign Gifts</h1>', '<h1>Tongues and Prophecy</h1>')
    s = s.replace('"name": "The Sign Gifts"', '"name": "Tongues and Prophecy"').replace('alt="The Sign Gifts cover"', 'alt="Tongues and Prophecy cover"')
    return s
L = [head(x) for x in L]
def setl(n, s): L[n - 1] = s

setl(9, '<p class="detail-kicker">What does 1 Corinthians 14 say tongues are, who they were for, and when did they end?</p>')
setl(10, '<p class="detail-copy">Paul writes of tongues and prophecy in three chapters, and Luke records tongues at Jerusalem, at Caesarea and at Ephesus. The same word is used in each, and one sentence of Paul’s quotes Isaiah to say what a tongue is for. Are the tongues of the Corinthians the same as the tongues of Acts, and does the sign Paul describes belong to every believer?</p>')
setl(11, '<p class="detail-copy">It argues that the tongues are languages, given as a sign to unbelieving Israel on the authority of Isaiah 28:11, 12, that the Corinthian gifts belong to the overlap and end with the national suspension of Israel’s program at Acts 28, and that no present practice of tongues is the biblical gift. It states plainly that the end of prophecy is an inference. In Chapter 13 it sets its reading beside modern writers who hold that the gifts continue and others who hold that they ended, and rules on each.</p>')
setl(13, '<div class="detail-buyline"><span class="detail-price">$14.99</span><span class="detail-format">Digital PDF · 55 Pages</span><span class="detail-button pending" aria-disabled="true">Checkout Coming Soon</span></div>')
setl(17, '<p class="lead">This volume does not list the views held on tongues and prophecy and leave the choice to the reader. It says what the author believes the passages state: what a tongue is, whom it was given to, what Paul says it was for and when the gifts ended. It gives the evidence from the passages and rules on the strongest objections by name.</p>')
setl(18, '<p class="lead">It is the second volume of The Sign Gifts Series, each volume of which is built around one narrower question about the signs of Scripture. Volume 1 asks what signs were for and where the record of them ends; this volume asks what tongues and prophecy are and whether they continue in the Body. It is a different kind of book from the Digital Studies, which report what a passage says. Scripture is quoted from the King James Version throughout, checked word for word, and the writers named in Chapter 13 are described from their published works and are not quoted.</p>')
def rr(href, label, note): return '<p><a href="%s">%s</a> %s</p>' % (href, label, note)
ds = ''.join([
 rr('study-81-praying-in-the-spirit.html', 'Study 81 — Praying in the Spirit', 'Reports what the passages say of praying in the Spirit and speaking in tongues without taking a position; this volume argues what the tongues are and whether they continue.'),
 rr('study-25-the-signs-that-followed.html', 'Study 25 — The Signs That Followed', 'Reports what Mark 16 says of signs and its textual question; this volume does not treat Mark 16.'),
 rr('study-38-why-acts-is-not-a-universal-experience-manual.html', 'Study 38 — Why Acts Is Not a Universal Experience Manual', 'Reads Acts as inspired history that is not a command for every believer; this volume reads the three instances of tongues in Acts beside 1 Corinthians 14.')])
cs = ''.join([
 rr('commentary-sign-gifts-01-the-sign-gifts.html', 'The Sign Gifts Series, Volume 1 — The Sign Gifts', 'Argues what signs were for, to whom they were given and that the record of signs ends in Acts 28; this volume argues the nature of tongues and prophecy and rests on that ending.'),
 rr('commentary-pauline-04-the-assembly-in-order.html', 'Pauline Doctrine Series, Volume 4 — The Assembly in Order', 'Argues the order of the assembly in 1 Corinthians 11 to 14; this volume cites the rules of 14:26–40 for what they show about the gift.'),
 rr('commentary-acts-02-the-spirit-in-acts.html', 'Acts Commentary Series, Volume 2 — The Spirit in Acts: Pentecost to Ephesus', 'Argues the Spirit scenes in Acts from Pentecost to Ephesus; this volume reads the three instances of tongues beside 1 Corinthians 14.')])
bb = ''.join(rr('packet-%s.html' % s, 'Bible Book Companion — %s' % n, 'Interprets the book of %s through its key passages.' % n) for s, n in (('1-corinthians', '1 Corinthians'), ('isaiah', 'Isaiah'), ('acts', 'Acts')))
setl(19, '<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4>%s</div><div class="rel-col o3"><h4>Bible Book Companion Series</h4>%s</div></div><div class="rel-stack"><div class="rel-col o2"><h4>Commentary Series</h4>%s</div></div></div><p class="connection-guide-link"><a href="commentary.html#sign-gifts">See The Sign Gifts Series →</a></p></div>' % (ds, bb, cs))
setl(21, '<h2>From the Word “Tongue” to the End of the Gift</h2>')
pts = [('The Words', 'Trace “tongue,” “prophesy” and “interpret,” and mark the KJV’s italic “unknown” and its lowercase “spirit” where they stand.'),
 ('Isaiah 28', 'Read Isaiah 28:7–14 in its own chapter and mark the speaker, the hearers and the speech before Paul quotes it.'),
 ('Tongues in Acts', 'Set Acts 2, Acts 10 and Acts 19 side by side, recording who speaks, who hears and what each passage leaves unsaid.'),
 ('First Corinthians 12 to 14', 'Walk the three chapters in the order Paul wrote them, from the list of gifts to the rules for the assembly.'),
 ('Prophecy', 'Follow prophecy through Acts and Paul’s letters and mark what each passage says a prophet does.'),
 ('The End of the Gift', 'Read Acts 28 and 1 Corinthians 13:8–10, then weigh modern writers on both sides of the question and the ruling on each.')]
setl(23, ''.join('<div class="study-point"><h3>%s</h3><p>%s</p></div>' % p for p in pts))
cards = [('Isa', 28, 11, 'Isaiah 28:11'), ('1Cor', 14, 21, '1 Corinthians 14:21'), ('1Cor', 14, 22, '1 Corinthians 14:22'), ('1Cor', 14, 10, '1 Corinthians 14:10'),
         ('1Cor', 13, 8, '1 Corinthians 13:8'), ('Acts', 2, 4, 'Acts 2:4'), ('Acts', 10, 46, 'Acts 10:46'), ('Acts', 28, 28, 'Acts 28:28')]
def vt(b, c, v): return html.escape(k.V[(b, c, v)], quote=False)
setl(27, ''.join('<div class="scripture-card"><h3>%s</h3><p>“%s”</p></div>' % (lab, vt(b, c, v)) for b, c, v, lab in cards))
setl(30, '<div class="excerpt"><blockquote>Paul says what tongues are for, and he says it by quoting Isaiah.</blockquote>')
setl(31, '<p>The volume reads the sentence where it stands, in 1 Corinthians 14:21, 22, and in the chapter of Isaiah it comes from, before it says what the gift is or whether it continues.</p></div> <div class="eyebrow" id="look-inside">A LOOK INSIDE</div>')
def pc(P, alt, title, note): return '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/sign-gifts-02-page-%d.jpg"><img src="assets/sign-gifts-02-page-%d.jpg" alt="Volume 2 %s"></a><div class="page-no">Interior Page %d</div><h3>%s</h3><p>%s</p></div>' % (P, P, alt, P, title, note)
setl(35, ''.join([pc(1, 'table of contents', 'Table of Contents', 'See the full order of the argument, from the Preface to the Bibliography.'),
 pc(2, 'preface', 'Preface', 'See the question stated plainly and how the volume proceeds.'),
 pc(9, 'Isaiah 28 read in its chapter', 'The Argument at Work', 'See the method: Isaiah 28:7–14 read in order, with the KJV text set beside what each passage says.'),
 pc(34, 'objections and replies', 'Objections and Replies', 'See modern writers named on both sides, each position stated, and the ruling on each objection.')]))
setl(37, '<h2>A Full Commentary on Tongues and Prophecy</h2>')
inc = [('55-Page Digital PDF', 'Cover and a fully numbered interior.'), ('Thirteen Chapters', 'From the question and the words to the end of the gift at Acts 28 and the objections and replies.'),
 ('Objections and Replies', 'Modern writers named on both sides, each objection ruled on from the text.'),
 ('Passage by Passage', 'Isaiah 28, Acts, and 1 Corinthians 12 to 14 read in order, with what each leaves unsaid.'),
 ('Comparison Tables', 'The words, the three instances in Acts and the readings of 13:10 set side by side.'), ('Conclusion', 'The position restated in full, with a closing table.'),
 ('Five Appendices', 'The passages at a glance, key words, questions for study, the key passages in full and a verse-by-verse index of where the passages are read.'),
 ('Bibliography', 'Every work cited, listed by author and title.')]
setl(39, ''.join('<div class="include-item"><h3>%s</h3><p>%s</p></div>' % i for i in inc))
setl(40, L[39].replace('<h2>The Sign Gifts</h2>', '<h2>Tongues and Prophecy</h2>'))
open(DST, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', DST, len(L))
