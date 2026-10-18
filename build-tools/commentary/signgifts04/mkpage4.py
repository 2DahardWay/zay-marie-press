"""Build commentary-sign-gifts-04-apostles-and-prophets.html from the Volume 3 page (same template). Run from the repo root."""
import re, sys, html
sys.path.insert(0, 'build-tools/commentary/signgifts04')
import kjvlib as k
SRC = 'commentary-sign-gifts-03-healing-in-the-body.html'
DST = 'commentary-sign-gifts-04-apostles-and-prophets.html'
L = open(SRC, encoding='utf-8').read().split('\n')
assert len(L) in (42, 43), len(L)
SUB = 'The Apostolic and Prophetic Offices in Scripture'
OLDSUB = 'The Sign-Gift of Healing and the Body’s Non-Sign Pattern'
DESC = ('The Sign Gifts Series, Volume 4, reads the passages that name apostles and prophets, argues that “apostle” names three kinds of person, that the office of the Twelve is suspended with Israel’s program at Acts 28 and resumes in the Kingdom, '
        'that the apostolic office as a sign-authenticated witness ends with the sign-program while Paul’s authority continues in his letters, and that the prophets of Ephesians 2:20 and 3:5 are prophets of the Mystery, and rules on the strongest objections by name.')
def head(s):
    s = s.replace('sign-gifts-03-healing-in-the-body', 'sign-gifts-04-apostles-and-prophets').replace('sign-gifts-03-', 'sign-gifts-04-')
    s = s.replace(OLDSUB, SUB).replace('Healing in the Body', 'Apostles and Prophets')
    s = re.sub(r'(content=")The Sign Gifts Series, Volume 3, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = re.sub(r'("description": ")The Sign Gifts Series, Volume 3, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = s.replace('"position": 3', '"position": 4').replace('VOLUME&nbsp;3', 'VOLUME&nbsp;4')
    s = re.sub(r'"numberOfPages": 55', '"numberOfPages": 52', s)
    return s
L = [head(x) for x in L]
def setl(n, s): L[n - 1] = s
setl(9, '<p class="detail-kicker">What do the passages mean by “apostle” and “prophet,” and does any verse say that the offices continue?</p>')
setl(10, '<p class="detail-copy">The New Testament names apostles and prophets, lists them first among the gifts God has set in the church, and says the household of God is “built upon the foundation of the apostles and prophets.” Yet the word “apostle” is used of the Twelve, of Paul, of Barnabas and of Epaphroditus, and the word “prophet” is used of Agabus, of the daughters of Philip and of a poet of Crete. What does each passage mean, and to whom does it speak?</p>')
setl(11, '<p class="detail-copy">It argues that “apostle” names three kinds of person, that the Twelve’s office is suspended with Israel’s program at Acts 28 and resumes in the Kingdom, that the apostolic office as a sign-authenticated witness ends with the sign-program while Paul’s authority continues in his letters, and that the prophets of Ephesians 2:20 and 3:5 are prophets of the Mystery. It states plainly that no verse names a successor and makes no statement about God’s power. In Chapter 13 it sets its reading beside modern writers on both sides and rules on each objection.</p>')
setl(13, '<div class="detail-buyline"><span class="detail-price">$14.99</span><span class="detail-format">Digital PDF · 52 Pages</span><span class="detail-button pending" aria-disabled="true">Checkout Coming Soon</span></div>')
setl(17, '<p class="lead">This volume does not list the views held on apostles and prophets and leave the choice to the reader. It says what the author believes the passages state: what the word “apostle” means in each place, who the Twelve were and what became of their office, what Paul’s apostleship rests on, who the prophets of Ephesians are, and what the foundation is. It gives the evidence from the passages and rules on the strongest objections by name.</p>')
setl(18, '<p class="lead">It is the fourth and last volume of The Sign Gifts Series, each volume of which is built around one narrower question about the signs of Scripture. Volume 1 asks what signs were for and where the record of them ends, Volume 2 asks what tongues and prophecy are, and Volume 3 asks what healing is for; this volume asks what the offices of apostle and prophet are and whether they continue. It is a different kind of book from the Digital Studies, which report what a passage says. Scripture is quoted from the King James Version throughout, checked word for word, and the writers named in Chapter 13 are described from their published works and are not quoted.</p>')
def rr(href, label, note): return '<p><a href="%s">%s</a> %s</p>' % (href, label, note)
ds = ''.join([
 rr('study-18-peter-and-paul-distinct-apostolic-commissions.html', 'Study 18 — Peter and Paul: Distinct Apostolic Commissions', 'Reads the two commissions as the passages state them; this volume asks what an apostle is and whether the office continues.'),
 rr('study-14-acts-9-and-the-beginning-of-mystery.html', 'Study 14 — Acts 9 and the Beginning of Mystery', 'Reads Acts 9 and the beginning of the Mystery; this volume reads Paul’s apostleship and the signs of an apostle.'),
 rr('study-36-jews-gentiles-and-the-church-of-god.html', 'Study 36 — Jews, Gentiles, and the Church of God', 'Reads the identity of Jew, Gentile and the church; this volume reads the foundation of Ephesians 2:20.')])
cs = ''.join([
 rr('commentary-sign-gifts-01-the-sign-gifts.html', 'The Sign Gifts Series, Volume 1 — The Sign Gifts', 'Argues what signs were for, to whom and that the record ends in Acts 28; this volume takes the offices that stood with the signs.'),
 rr('commentary-acts-03-paul-called-and-sent.html', 'Acts Commentary Series, Volume 3 — Paul Called and Sent', 'Argues Paul’s call and sending in Acts 9, 13, 22 and 26; this volume reads his apostleship and its marks.'),
 rr('commentary-pauline-04-the-assembly-in-order.html', 'Pauline Doctrine Series, Volume 4 — The Assembly in Order', 'Argues the order of the assembly and the gift lists; this volume argues the offices of apostle and prophet.')])
bb = ''.join(rr('packet-%s.html' % s, 'Bible Book Companion — %s' % n, 'Interprets the book of %s through its key passages.' % n) for s, n in (('ephesians', 'Ephesians'), ('galatians', 'Galatians'), ('2-corinthians', '2 Corinthians')))
setl(19, '<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4>%s</div><div class="rel-col o3"><h4>Bible Book Companion Series</h4>%s</div></div><div class="rel-stack"><div class="rel-col o2"><h4>Commentary Series</h4>%s</div></div></div><p class="connection-guide-link"><a href="commentary.html#sign-gifts">See The Sign Gifts Series →</a></p></div>' % (ds, bb, cs))
setl(21, '<h2>From the Word “Apostle” to the Foundation</h2>')
pts = [('The Words', 'Trace “apostle,” “apostolos,” “messenger” and “prophet,” and mark where one Greek word stands behind two English renderings.'),
 ('The Twelve', 'Read the choosing, the sending and the promised thrones in Matthew, Luke and Acts 1, recording who is chosen, by whom and to whom.'),
 ('Others Called Apostles', 'Follow Barnabas, Epaphroditus, Andronicus and Junia through their passages, marking what each says and leaves unsaid.'),
 ('Paul’s Apostleship', 'Read Galatians 1 and 2, 1 Corinthians 9 and 15, and 2 Corinthians 11 and 12 in order, noting the marks Paul himself gives.'),
 ('The Prophets of Ephesians', 'Read Ephesians 2:19–22 and 3:1–13 together, tracing who the prophets are by the passage’s own markers.'),
 ('The Gifts and Their Limits', 'Read Ephesians 4:7–16, then weigh modern writers on both sides of the question and the ruling on each.')]
setl(23, ''.join('<div class="study-point"><h3>%s</h3><p>%s</p></div>' % p for p in pts))
cards = [('Luke', 6, 13, 'Luke 6:13'), ('Acts', 14, 14, 'Acts 14:14'), ('1Cor', 9, 1, '1 Corinthians 9:1'), ('Gal', 1, 1, 'Galatians 1:1'),
         ('2Cor', 12, 12, '2 Corinthians 12:12'), ('Eph', 2, 20, 'Ephesians 2:20'), ('Eph', 3, 5, 'Ephesians 3:5'), ('Eph', 4, 11, 'Ephesians 4:11')]
def vt(b, c, v): return html.escape(k.V[(b, c, v)], quote=False)
setl(27, ''.join('<div class="scripture-card"><h3>%s</h3><p>“%s”</p></div>' % (lab, vt(b, c, v)) for b, c, v, lab in cards))
setl(30, '<div class="excerpt"><blockquote>No verse names a successor to an apostle or to a prophet.</blockquote>')
setl(31, '<p>The volume reads the word “apostle” where it stands in each passage, and the foundation of Ephesians 2:20 beside Ephesians 3:5, before it says what the offices were or whether they continue.</p></div> <div class="eyebrow" id="look-inside">A LOOK INSIDE</div>')
def pc(P, alt, title, note): return '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/sign-gifts-04-page-%d.jpg"><img src="assets/sign-gifts-04-page-%d.jpg" alt="Volume 4 %s"></a><div class="page-no">Interior Page %d</div><h3>%s</h3><p>%s</p></div>' % (P, P, alt, P, title, note)
setl(35, ''.join([pc(1, 'table of contents', 'Table of Contents', 'See the full order of the argument, from the Preface to the Bibliography.'),
 pc(2, 'preface', 'Preface', 'See the question stated plainly and how the volume proceeds.'),
 pc(28, 'Ephesians 4 read in order', 'The Argument at Work', 'See the method: Ephesians 4:7–13 read in order, with the KJV text set beside what each verse states.'),
 pc(36, 'objections and replies', 'Objections and Replies', 'See modern writers named on both sides, each position stated, and the ruling on each objection.')]))
setl(37, '<h2>A Full Commentary on Apostles and Prophets</h2>')
inc = [('52-Page Digital PDF', 'Cover and a fully numbered interior.'), ('Thirteen Chapters', 'From the question and the word “apostle” to the foundation of Ephesians 2:20 and the objections and replies.'),
 ('Objections and Replies', 'Modern writers named on both sides, each objection ruled on from the text.'),
 ('Passage by Passage', 'Matthew 10, Acts 1, Galatians 1 and 2, 1 Corinthians 9 and 15, 2 Corinthians 11 and 12 and Ephesians 2 to 4 read in order, with what each leaves unsaid.'),
 ('Comparison Tables', 'The passages set side by side, with the KJV text and what to observe.'), ('Conclusion', 'The position restated in full, with a closing table.'),
 ('Five Appendices', 'The passages at a glance, key words, questions for study, the key passages in full and a verse-by-verse index of where the passages are read.'),
 ('Bibliography', 'Every work cited, listed by author and title.')]
setl(39, ''.join('<div class="include-item"><h3>%s</h3><p>%s</p></div>' % i for i in inc))
setl(40, L[39].replace('55-page', '52-page'))
open(DST, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', DST, len(L))
