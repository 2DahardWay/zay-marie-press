"""Build commentary-sign-gifts-01-the-sign-gifts.html from the Prophets Volume 4 page (same template). Run from the repo root."""
import re, sys, html
sys.path.insert(0, 'build-tools/commentary/signgifts01')
import kjvlib as k
SRC = 'commentary-prophets-04-elijah-must-first-come.html'
DST = 'commentary-sign-gifts-01-the-sign-gifts.html'
L = open(SRC, encoding='utf-8').read().split('\n')
assert len(L) in (42, 43), len(L)
OLD = 'commentary-prophets-04-elijah-must-first-come'; NEW = 'commentary-sign-gifts-01-the-sign-gifts'
SUB = 'The Purpose of Signs, Their Audience, and Their Programmatic End at Acts 28'
DESC = ('The Sign Gifts Series, Volume 1, reads every sign, wonder and miracle Scripture records, from Exodus 4 to Acts 28 and Paul’s own letters, argues that a sign is given to a hearer for a purpose the passage states, '
        'that the signs belonged to Israel’s line and its messengers, and that the record of signs in Acts ends in chapter 28, and rules on the strongest objections by name.')
def head(s):
    s = s.replace('share-commentary-prophets-04-elijah-must-first-come', 'share-commentary-sign-gifts-01-the-sign-gifts')
    s = s.replace(OLD, NEW).replace('Elijah Must First Come', 'The Sign Gifts').replace('The Prophets Series', 'The Sign Gifts Series')
    s = s.replace('Malachi’s Promise, John’s Answer, and the Coming the Lord Still Names', SUB)
    s = re.sub(r'(content=")The Sign Gifts Series, Volume 4, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = re.sub(r'("description": ")The Sign Gifts Series, Volume 4, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = s.replace('prophets-04-', 'sign-gifts-01-').replace('"position": 4', '"position": 1')
    s = s.replace('VOLUME&nbsp;4', 'VOLUME&nbsp;1')
    return s
L = [head(x) for x in L]
def setl(n, s): L[n - 1] = s
setl(9, '<p class="detail-kicker">What were signs for, to whom were they given, and what is the last sign the book of Acts records?</p>')
setl(10, '<p class="detail-copy">Scripture uses one set of words, sign, wonder, miracle and token, for what God does to mark a messenger, to move a nation and to answer a doubter. Moses before Pharaoh, the Lord in Galilee, Peter in Solomon’s porch and Paul on Malta each stand in a passage that names a giver, a hearer and a purpose. Are these one thing?</p>')
setl(11, '<p class="detail-copy">It argues that the signs belonged to Israel’s line, given to a hearer to confirm a messenger’s word, that the last sign Acts records is the healing on Malta in chapter 28, and that signs do not continue into the Mystery. In Chapter 11 it sets its reading beside modern writers who hold that the gifts continue and others who hold that they ended, and rules on each.</p>')
setl(13, '<div class="detail-buyline"><span class="detail-price">$14.99</span><span class="detail-format">Digital PDF · 55 Pages</span><span class="detail-button pending" aria-disabled="true">Checkout Coming Soon</span></div>')
setl(17, '<p class="lead">This volume does not list the views held on the sign gifts and leave the choice to the reader. It says what the author believes the passages state: what a sign is, whom it was given to, what it was set to prove and where the record of signs ends. It gives the evidence from the passages and rules on the strongest objections by name.</p>')
setl(18, '<p class="lead">It is the first volume of The Sign Gifts Series, each volume of which is built around one narrower question about the signs of Scripture. This volume asks what signs were for, to whom they were given and where the record of them ends. More volumes will follow. It is a different kind of book from the Digital Studies, which report what a passage says. Scripture is quoted from the King James Version throughout, checked word for word, and the writers named in Chapter 11 are described from their published works and are not quoted.</p>')
def rr(href, label, note): return '<p><a href="%s">%s</a> %s</p>' % (href, label, note)
ds = ''.join([
 rr('study-25-the-signs-that-followed.html', 'Study 25 — The Signs That Followed', 'Reports what Mark 16 says of signs and the textual question of its last verses; this volume reads the commission only for its audience and the tense of its confirmation.'),
 rr('study-38-why-acts-is-not-a-universal-experience-manual.html', 'Study 38 — Why Acts Is Not a Universal Experience Manual', 'Reads Acts as inspired history that is not a command for every believer; this volume asks only what the signs in Acts were for and where the record of them ends.'),
 rr('study-81-praying-in-the-spirit.html', 'Study 81 — Praying in the Spirit', 'Reports what the passages say of praying in the Spirit and speaking in tongues; this volume does not treat that question.')])
cs = ''.join([
 rr('commentary-acts-02-the-spirit-in-acts.html', 'Acts Commentary Series, Volume 2 — The Spirit in Acts: Pentecost to Ephesus', 'Argues the Spirit scenes in Acts from Pentecost to Ephesus; this volume cites them only as signs in the record.'),
 rr('commentary-acts-05-acts-28-the-close-of-the-book.html', 'Acts Commentary Series, Volume 5 — Acts 28: The Close of the Book', 'Argues the national suspension at Acts 28; this volume argues that the last sign in the record falls in the same chapter.'),
 rr('commentary-gospel-02-the-lords-ministry-to-israel.html', 'Gospel Commentary Series, Volume 2 — The Lord’s Ministry to Israel', 'Argues the Lord’s ministry to Israel; this volume reads His signs only for whom they were given to and what they were set to prove.')])
bb = ''.join(rr('packet-%s.html' % s, 'Bible Book Companion — %s' % n, 'Interprets the book of %s through its key passages.' % n) for s, n in (('acts', 'Acts'), ('exodus', 'Exodus'), ('john', 'John')))
setl(19, '<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4>%s</div><div class="rel-col o3"><h4>Bible Book Companion Series</h4>%s</div></div><div class="rel-stack"><div class="rel-col o2"><h4>Commentary Series</h4>%s</div></div></div><p class="connection-guide-link"><a href="commentary.html#sign-gifts">See The Sign Gifts Series →</a></p></div>' % (ds, bb, cs))
setl(21, '<h2>From the Word “Sign” to the End of the Record</h2>')
pts = [('The Word “Sign”', 'Trace “sign,” “token,” “wonder” and “miracle” through Exodus and the prophets, and mark who gives each one, who receives it and what it is set to prove.'),
 ('Messenger Signs', 'Follow Moses before Pharaoh and Israel, the signs of the prophets and the Lord’s own signs, and see what each one confirms.'),
 ('The Commission', 'Read Mark 16, Matthew 10, Luke 10 and Hebrews 2 in order, tracing the audience and the tense of each.'),
 ('Signs in Acts', 'Walk Acts 1 to 8 and Acts 9 to 28 passage by passage, recording who works each sign, before whom, and what the book leaves unsaid.'),
 ('Paul’s Own Letters', 'Read 2 Corinthians 12:12, the illnesses of Paul’s companions, and the word “sign” in Romans and 2 Thessalonians.'),
 ('The End of the Record', 'Read Acts 28 from Malta to the last two verses, then weigh modern writers on both sides of the question and the ruling on each.')]
setl(23, ''.join('<div class="study-point"><h3>%s</h3><p>%s</p></div>' % p for p in pts))
cards = [('Exod', 4, 5, 'Exodus 4:5'), ('John', 20, 31, 'John 20:31'), ('Acts', 2, 22, 'Acts 2:22'), ('Mark', 16, 20, 'Mark 16:20'),
         ('Heb', 2, 4, 'Hebrews 2:4'), ('2Cor', 12, 12, '2 Corinthians 12:12'), ('Acts', 28, 9, 'Acts 28:9'), ('Acts', 28, 28, 'Acts 28:28')]
def vt(b, c, v): return html.escape(k.V[(b, c, v)], quote=False)
setl(27, ''.join('<div class="scripture-card"><h3>%s</h3><p>“%s”</p></div>' % (lab, vt(b, c, v)) for b, c, v, lab in cards))
setl(30, '<div class="excerpt"><blockquote>A sign in Scripture is given to someone and for something.</blockquote>')
setl(31, '<p>Each passage names a giver, a hearer and a purpose. The volume reads every sign the same way, who gave it, who received it and what it was set to prove, before it says what any of them mean together.</p></div> <div class="eyebrow" id="look-inside">A LOOK INSIDE</div>')
def pc(P, alt, title, note): return '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/sign-gifts-01-page-%d.jpg"><img src="assets/sign-gifts-01-page-%d.jpg" alt="Volume 1 %s"></a><div class="page-no">Interior Page %d</div><h3>%s</h3><p>%s</p></div>' % (P, P, alt, P, title, note)
setl(35, ''.join([pc(1, 'table of contents', 'Table of Contents', 'See the full order of the argument, from the Preface to the Bibliography.'),
 pc(2, 'preface', 'Preface', 'See the position stated plainly and how the volume proceeds.'),
 pc(24, 'signs in Acts 9 to 28', 'The Argument at Work', 'See the method: the signs in Acts 9 to 28 set out in a table, with what the text reports and what it leaves unsaid.'),
 pc(32, 'objections and replies', 'Objections and Replies', 'See modern writers named on both sides, each position stated, and the ruling on each objection.')]))
setl(37, '<h2>A Full Commentary on The Sign Gifts</h2>')
inc = [('55-Page Digital PDF', 'Cover and a fully numbered interior.'), ('Eleven Chapters', 'From the question and the method to the end of the record in Acts 28 and the objections and replies.'),
 ('Objections and Replies', 'Modern writers named on both sides, each objection ruled on from the text.'),
 ('Passage by Passage', 'Exodus, the prophets, the Gospels, Acts, Paul’s letters and Hebrews read in order, with what each leaves unsaid.'),
 ('Comparison Tables', 'The messenger signs, the Lord’s signs, the commission and the signs in Acts set side by side.'), ('Conclusion', 'The position restated in full, with a closing table.'),
 ('Five Appendices', 'The passages at a glance, key words, questions for study, the key passages in full and a verse-by-verse index of where the passages are read.'),
 ('Bibliography', 'Every work cited, listed by author and title.')]
setl(39, ''.join('<div class="include-item"><h3>%s</h3><p>%s</p></div>' % i for i in inc))
setl(41, '<a class="back-link" href="commentary.html#sign-gifts">← Back to the Commentary Collection</a>')
open(DST, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', DST, len(L))
