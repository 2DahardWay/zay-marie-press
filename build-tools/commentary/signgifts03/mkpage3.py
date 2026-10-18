"""Build commentary-sign-gifts-03-healing-in-the-body.html from the Volume 2 page (same template). Run from the repo root."""
import re, sys, html
sys.path.insert(0, 'build-tools/commentary/signgifts03')
import kjvlib as k
SRC = 'commentary-sign-gifts-02-tongues-and-prophecy.html'
DST = 'commentary-sign-gifts-03-healing-in-the-body.html'
L = open(SRC, encoding='utf-8').read().split('\n')
assert len(L) in (42, 43), len(L)
SUB = 'The Sign-Gift of Healing and the Body’s Non-Sign Pattern'
DESC = ('The Sign Gifts Series, Volume 3, reads the healing passages from Exodus to James and Paul’s letters, argues that healing in the Gospels and Acts 1 to 8 confirmed a messenger to Israel, '
        'that James 5 is Israel’s passage, that the gifts of healing belonged to the overlap and ended with the sign-program at Acts 28, and that the letters to the Body meet sickness with prayer, care and the mercy of God, and rules on the strongest objections by name.')
def head(s):
    s = s.replace('sign-gifts-02-tongues-and-prophecy', 'sign-gifts-03-healing-in-the-body').replace('sign-gifts-02-', 'sign-gifts-03-')
    s = s.replace('Whether Tongues and Prophecy Continue in the Body', SUB).replace('Tongues and Prophecy', 'Healing in the Body')
    s = re.sub(r'(content=")The Sign Gifts Series, Volume 2, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = re.sub(r'("description": ")The Sign Gifts Series, Volume 2, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = s.replace('"position": 2', '"position": 3').replace('VOLUME&nbsp;2', 'VOLUME&nbsp;3')
    return s
L = [head(x) for x in L]
def setl(n, s): L[n - 1] = s
setl(9, '<p class="detail-kicker">Does any passage addressed to the Body give healing as a gift, an authority or a promise, and what do the letters to the Body do with sickness?</p>')
setl(10, '<p class="detail-copy">Healing runs through Scripture from Exodus 15:26 to James 5, and the passages that name it do not all say the same thing. The Lord healed multitudes, the Twelve were sent to heal, Paul lists gifts of healing at Corinth, and James tells the sick to call the elders. Yet Epaphroditus was sick nigh unto death and God had mercy on him, Trophimus was left sick, and Paul’s thorn was not removed. What does each passage say, and to whom?</p>')
setl(11, '<p class="detail-copy">It argues that healing in the Gospels and in Acts 1 to 8 confirmed a messenger to Israel, that James 5 is Israel’s passage, that the gifts of healing belong to the Corinthian overlap and end programmatically at Acts 28, and that the Body prays for the sick because Paul commands prayer, not because a gift or a promise is given. It states plainly that no verse states the end, and it makes no statement about God’s power. In Chapter 14 it sets its reading beside modern writers on both sides and rules on each objection.</p>')
setl(13, '<div class="detail-buyline"><span class="detail-price">$14.99</span><span class="detail-format">Digital PDF · 55 Pages</span><span class="detail-button pending" aria-disabled="true">Checkout Coming Soon</span></div>')
setl(17, '<p class="lead">This volume does not list the views held on healing and leave the choice to the reader. It says what the author believes the passages state: what healing was for in each setting, to whom James 5 is written, what the gifts of healing were and when they ended, and what the letters to the Body do with sickness. It gives the evidence from the passages and rules on the strongest objections by name.</p>')
setl(18, '<p class="lead">It is the third volume of The Sign Gifts Series, each volume of which is built around one narrower question about the signs of Scripture. Volume 1 asks what signs were for and where the record of them ends, and Volume 2 asks what tongues and prophecy are; this volume asks what the Scriptures say healing is for and what the Body does with sickness. It is a different kind of book from the Digital Studies, which report what a passage says. Scripture is quoted from the King James Version throughout, checked word for word, and the writers named in Chapter 14 are described from their published works and are not quoted.</p>')
def rr(href, label, note): return '<p><a href="%s">%s</a> %s</p>' % (href, label, note)
ds = ''.join([
 rr('study-86-the-servant-in-isaiah.html', 'Study 86 — The Servant in Isaiah', 'Reads the servant passages of Isaiah 41 to 53 in order; this volume reads only the clauses of Isaiah 53:4–6 beside Matthew 8:17 and 1 Peter 2:24.'),
 rr('study-25-the-signs-that-followed.html', 'Study 25 — The Signs That Followed', 'Reports what Mark 16 says of signs and its textual question; this volume does not treat Mark 16.'),
 rr('study-38-why-acts-is-not-a-universal-experience-manual.html', 'Study 38 — Why Acts Is Not a Universal Experience Manual', 'Reads Acts as inspired history that is not a command for every believer; this volume reads the healings of Acts 1 to 8 and 9 to 28 for what they were for.')])
cs = ''.join([
 rr('commentary-sign-gifts-01-the-sign-gifts.html', 'The Sign Gifts Series, Volume 1 — The Sign Gifts', 'Argues what signs were for, to whom and that the record ends in Acts 28; this volume takes healing in full and rests on that ending.'),
 rr('commentary-sign-gifts-02-tongues-and-prophecy.html', 'The Sign Gifts Series, Volume 2 — Tongues and Prophecy', 'Argues what tongues and prophecy are and the gift lists of 1 Corinthians 12; this volume takes only the healing clauses.'),
 rr('commentary-acts-05-acts-28-the-close-of-the-book.html', 'Acts Commentary Series, Volume 5 — Acts 28: The Close of the Book', 'Argues the suspension itself in Acts 28; this volume applies it to the gifts of healing.')])
bb = ''.join(rr('packet-%s.html' % s, 'Bible Book Companion — %s' % n, 'Interprets the book of %s through its key passages.' % n) for s, n in (('james', 'James'), ('1-corinthians', '1 Corinthians'), ('2-corinthians', '2 Corinthians')))
setl(19, '<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4>%s</div><div class="rel-col o3"><h4>Bible Book Companion Series</h4>%s</div></div><div class="rel-stack"><div class="rel-col o2"><h4>Commentary Series</h4>%s</div></div></div><p class="connection-guide-link"><a href="commentary.html#sign-gifts">See The Sign Gifts Series →</a></p></div>' % (ds, bb, cs))
setl(21, '<h2>From the Word “Heal” to the End of the Gift</h2>')
pts = [('The Words', 'Trace “sick,” “infirmity,” “heal,” “cure” and “anoint,” and mark the plural in “gifts of healings” where it stands.'),
 ('Israel’s Scriptures', 'Read the healing promises of the Law and the psalms in their own settings, and Isaiah 53:4–6 in its own chapter.'),
 ('The Lord and the Twelve', 'Set Matthew 8, Matthew 10 and Luke 10 beside the first chapters of Acts, recording who is sent, to whom and for what.'),
 ('Paul’s Companions', 'Follow Epaphroditus, Timothy, Trophimus and Luke through the letters and mark what each passage says and leaves unsaid.'),
 ('James and the Thorn', 'Read James 5:13–20 and 2 Corinthians 12:7–10 in their own settings before comparing them.'),
 ('The End of the Gift', 'Read Acts 28 and 1 Peter 2:24, then weigh modern writers on both sides of the question and the ruling on each.')]
setl(23, ''.join('<div class="study-point"><h3>%s</h3><p>%s</p></div>' % p for p in pts))
cards = [('Isa', 53, 5, 'Isaiah 53:5'), ('Matt', 8, 17, 'Matthew 8:17'), ('1Cor', 12, 9, '1 Corinthians 12:9'), ('Jas', 5, 15, 'James 5:15'),
         ('Phil', 2, 27, 'Philippians 2:27'), ('2Cor', 12, 9, '2 Corinthians 12:9'), ('1Pet', 2, 24, '1 Peter 2:24'), ('Acts', 28, 8, 'Acts 28:8')]
def vt(b, c, v): return html.escape(k.V[(b, c, v)], quote=False)
setl(27, ''.join('<div class="scripture-card"><h3>%s</h3><p>“%s”</p></div>' % (lab, vt(b, c, v)) for b, c, v, lab in cards))
setl(30, '<div class="excerpt"><blockquote>Paul asked three times, and the answer was grace.</blockquote>')
setl(31, '<p>The volume reads the thorn where it stands, in 2 Corinthians 12:7–10, beside the account of Epaphroditus in Philippians 2, before it says what the gifts of healing were or whether they continue.</p></div> <div class="eyebrow" id="look-inside">A LOOK INSIDE</div>')
def pc(P, alt, title, note): return '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/sign-gifts-03-page-%d.jpg"><img src="assets/sign-gifts-03-page-%d.jpg" alt="Volume 3 %s"></a><div class="page-no">Interior Page %d</div><h3>%s</h3><p>%s</p></div>' % (P, P, alt, P, title, note)
setl(35, ''.join([pc(1, 'table of contents', 'Table of Contents', 'See the full order of the argument, from the Preface to the Bibliography.'),
 pc(2, 'preface', 'Preface', 'See the question stated plainly and how the volume proceeds.'),
 pc(24, 'James 5 read in its setting', 'The Argument at Work', 'See the method: James 5:13–20 read in its Israel setting, with the KJV text set beside what each passage says.'),
 pc(37, 'objections and replies', 'Objections and Replies', 'See modern writers named on both sides, each position stated, and the ruling on each objection.')]))
setl(37, '<h2>A Full Commentary on Healing in the Body</h2>')
inc = [('55-Page Digital PDF', 'Cover and a fully numbered interior.'), ('Fourteen Chapters', 'From the question and the words to the end of the gift at Acts 28 and the objections and replies.'),
 ('Objections and Replies', 'Modern writers named on both sides, each objection ruled on from the text.'),
 ('Passage by Passage', 'Isaiah 53, the Gospels, Acts, 1 Corinthians 12, James 5 and 2 Corinthians 12 read in order, with what each leaves unsaid.'),
 ('Comparison Tables', 'The healing passages set side by side, with the KJV text and what to observe.'), ('Conclusion', 'The position restated in full, with a closing table.'),
 ('Five Appendices', 'The passages at a glance, key words, questions for study, the key passages in full and a verse-by-verse index of where the passages are read.'),
 ('Bibliography', 'Every work cited, listed by author and title.')]
setl(39, ''.join('<div class="include-item"><h3>%s</h3><p>%s</p></div>' % i for i in inc))
open(DST, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', DST, len(L))
