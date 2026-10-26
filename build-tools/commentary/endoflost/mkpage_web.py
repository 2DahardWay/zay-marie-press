"""Build commentary-end-of-the-lost.html from the Sign Gifts Volume 4 page (same template). Run from the repo root."""
import re, sys, html
sys.path.insert(0, 'build-tools/commentary/endoflost')
import kjvlib as k
SRC = 'commentary-sign-gifts-04-apostles-and-prophets.html'
DST = 'commentary-end-of-the-lost.html'
L = open(SRC, encoding='utf-8').read().split('\n')
assert len(L) in (42, 43), len(L)
TITLE = 'The End of the Lost'
SUB = 'Destruction, Eternal Punishment, and the Case Against Annihilationism'
DESC = ('A single-volume Commentary that argues that destruction language does not by itself establish annihilation, reads the words for death, destruction, punishment, torment, exclusion, the second death and final judgment in their own contexts, '
        'and argues that the passages taken together establish irreversible, everlasting punishment, so that those finally cast into the lake of fire do not cease to exist; it names modern writers on both sides and rules on each objection.')
def head(s):
    s = s.replace('sign-gifts-04-apostles-and-prophets', 'end-of-the-lost').replace('sign-gifts-04-', 'end-of-the-lost-')
    s = s.replace('commentary-sign-gifts-04', 'commentary-end-of-the-lost')
    s = s.replace('Apostles and Prophets | The Sign Gifts Series | Zay-Marie Press', TITLE + ' | Commentary Collection | Zay-Marie Press')
    s = s.replace('The Apostolic and Prophetic Offices in Scripture', SUB).replace('Apostles and Prophets', TITLE)
    s = re.sub(r'(content=")The Sign Gifts Series, Volume 4, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = re.sub(r'("description": ")The Sign Gifts Series, Volume 4, reads[^"]*"', lambda m: m.group(1) + DESC + '"', s)
    s = s.replace('"isPartOf": {"@type": "BookSeries", "name": "The Sign Gifts Series"}, "position": 4, ', '')
    s = s.replace('"numberOfPages": 52', '"numberOfPages": 66')
    return s
L = [head(x) for x in L]
def setl(n, s): L[n - 1] = s
setl(6, '<div class="eyebrow">COMMENTARY COLLECTION · SINGLE VOLUME SERIES</div>')
setl(9, '<p class="detail-kicker">Does the Bible’s language of destruction mean that the lost cease to exist, or does it describe a punishment that does not end?</p>')
setl(10, '<p class="detail-copy">Scripture speaks of the lost in the words of death, destruction, perishing, punishment, torment, exclusion and the second death. Some careful writers read those words as the end of existence; others read them as a punishment without end. What does each passage say, in the setting where it stands, and what do the passages say when they are read together?</p>')
setl(11, '<p class="detail-copy">It argues that destruction language does not by itself establish annihilation, that its meaning is fixed by context, and that the passages taken together establish irreversible, everlasting punishment: Revelation describes human beings under torment without rest, identifies the lake of fire as the second death and names that lake as the place of torment day and night for ever and ever. Those finally cast into it do not cease to exist. The case is cumulative and never rests on one Greek word or one proof text. In Chapter 9 it sets its reading beside modern writers on both sides and rules on each objection.</p>')
setl(13, '<div class="detail-buyline"><span class="detail-price">$14.99</span><span class="detail-format">Digital PDF · 66 Pages</span><span class="detail-button pending" aria-disabled="true">Checkout Coming Soon</span></div>')
setl(17, '<p class="lead">This volume does not gather what churches say about the end of the lost and leave the choice to the reader. It says what the author believes Scripture reveals, sets the verses in the order they stand, and answers the strongest objections from named modern writers, so that a reader who disagrees knows where the disagreement lies.</p>')
setl(18, '<p class="lead">It stands alone in the Commentary Collection and belongs to no series. It takes one question: whether the final punishment of the lost is their ceasing to exist. It is a different kind of book from the Digital Studies, which report what a passage says. Scripture is quoted from the King James Version throughout, checked word for word. The Lord’s words in the Gospels were spoken to Israel in His Kingdom ministry, and the visions of Revelation name the audience they were sent to; the volume reads them there and does not turn them into a warning to the Body of Christ.</p>')
def rr(href, label, note): return '<p><a href="%s">%s</a> %s</p>' % (href, label, note)
ds = ''.join([
 rr('study-79-the-realms-of-the-dead.html', 'Study 79 — The Realms of the Dead', 'Reports Sheol, Hades, Gehenna and the lake of fire as written and takes no position; this volume argues what the final punishment is.'),
 rr('study-31-the-judgments-of-scripture.html', 'Study 31 — The Judgments of Scripture', 'Reports the judgments of Scripture in their settings; this volume argues the end of the lost.'),
 rr('study-68-the-book-of-life.html', 'Study 68 — The Book of Life', 'Traces the book of life through the passages that name it; this volume reads Revelation 20:11–15 for the punishment that follows.')])
cs = ''.join([
 rr('commentary-prophecy-mystery-05-separate-courts.html', 'Prophecy & Mystery Commentary, Volume 5 — Separate Courts', 'Argues who is judged where and why Scripture does not merge the courts; this volume argues what the final punishment is.'),
 rr('commentary-gospel-03-the-olivet-discourse.html', 'Gospel Commentary Series, Volume 3 — The Olivet Discourse', 'Argues the Olivet Discourse as Israel’s; this volume reads Matthew 25:31–46 for what it says of the punishment.')])
ps = ''.join([
 rr('parable-24-the-rich-man-and-lazarus.html', 'Parable Study — The Rich Man and Lazarus', 'Reads Luke 16:19–31 as its own edition; this volume cites it only as the Lord’s account of the dead.'),
 rr('parable-31-the-sheep-and-the-goats.html', 'Parable Study — The Sheep and the Goats', 'Reads Matthew 25:31–46 as its own edition; this volume reads the closing verse for the word “eternal.”')])
bb = ''.join(rr('packet-%s.html' % s, 'Bible Book Companion — %s' % n, 'Interprets the book of %s through its key passages.' % n) for s, n in (('revelation', 'Revelation'), ('matthew', 'Matthew'), ('2-thessalonians', '2 Thessalonians')))
setl(19, '<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4>%s</div><div class="rel-col o3"><h4>Parable Studies</h4>%s</div></div><div class="rel-stack"><div class="rel-col o2"><h4>Commentary Series</h4>%s</div><div class="rel-col o4"><h4>Bible Book Companion Series</h4>%s</div></div></div><p class="connection-guide-link"><a href="commentary.html#end-of-the-lost">See the Commentary Collection →</a></p></div>' % (ds, ps, cs, bb))
setl(21, '<h2>From the Words of Destruction to the Lake of Fire</h2>')
pts = [('How the Case Is Argued', 'See how each claim is stated, the passages read in order, and how the evidence is marked Stated, shown by the context or Inferred.'),
 ('The Words in Their Contexts', 'Follow death, destruction and perishing through passages where the same word names an ending and a ruin of something that remains.'),
 ('Matthew 10:28 and 2 Thessalonians 1:7–10', 'Read the power to destroy soul and body, and everlasting destruction from the presence of the Lord, in the sentences that surround them.'),
 ('“Eternal,” the Fire and the Worm', 'Set Matthew 25:46, Daniel 12:2 and Jude 7 beside Mark 9:43–48 and Isaiah 66:24, and weigh the two readings of each.'),
 ('Revelation 14:9–11 and 20:10–15', 'Trace the one lake of fire across the passages that name it, the second death, and who stands at the great white throne.'),
 ('Objections and Replies', 'Weigh modern writers on both sides, each objection stated and answered from the text, with a verdict on each.')]
setl(23, ''.join('<div class="study-point"><h3>%s</h3><p>%s</p></div>' % p for p in pts))
cards = [('Matt', 10, 28, 'Matthew 10:28'), ('Matt', 25, 46, 'Matthew 25:46'), ('Mark', 9, 48, 'Mark 9:48'), ('2Thess', 1, 9, '2 Thessalonians 1:9'),
         ('Rev', 14, 11, 'Revelation 14:11'), ('Rev', 20, 10, 'Revelation 20:10'), ('Rev', 20, 15, 'Revelation 20:15'), ('Rev', 21, 8, 'Revelation 21:8')]
def vt(b, c, v): return html.escape(k.V[(b, c, v)], quote=False)
setl(27, ''.join('<div class="scripture-card"><h3>%s</h3><p>“%s”</p></div>' % (lab, vt(b, c, v)) for b, c, v, lab in cards))
setl(30, '<div class="excerpt"><blockquote>The word of destruction does not decide the question; the sentence around it does.</blockquote>')
setl(31, '<p>The volume asks of every verse who is addressed, what has just been said, and what the verse says follows, before it says what the passages establish when they are read together.</p></div> <div class="eyebrow" id="look-inside">A LOOK INSIDE</div>')
def pc(P, alt, title, note): return '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/end-of-the-lost-page-%d.jpg"><img src="assets/end-of-the-lost-page-%d.jpg" alt="The End of the Lost %s"></a><div class="page-no">Interior Page %d</div><h3>%s</h3><p>%s</p></div>' % (P, P, alt, P, title, note)
setl(35, ''.join([pc(1, 'table of contents', 'Table of Contents', 'See the full order of the argument, from the Preface to the Bibliography.'),
 pc(2, 'preface', 'Preface', 'See the question stated plainly, the three answers given to it and how the volume proceeds.'),
 pc(36, 'Revelation 14:9–11 and 20:10 side by side', 'The Argument at Work', 'See the method: Revelation 14:9–11 and 20:10 set side by side, what is Stated and what is Inferred.'),
 pc(46, 'objections and replies', 'Objections and Replies', 'See modern writers named, each objection stated, answered and given a verdict.')]))
setl(37, '<h2>A Full Commentary on the End of the Lost</h2>')
inc = [('66-Page Digital PDF', 'Cover and a fully numbered interior.'), ('Nine Chapters and a Conclusion', 'From the Preface and the method to the lake of fire, the objections and replies, and the conclusion.'),
 ('Objections and Replies', 'Modern writers named on both sides, each objection answered first and then proved from the text.'),
 ('Passage by Passage', 'Matthew 10, Matthew 25, Mark 9, 2 Thessalonians 1, Revelation 14 and Revelation 20 and 21 read in order, with what each states.'),
 ('Comparison Tables', 'The passages set side by side, with the KJV text and what to observe.'), ('Conclusion', 'The position restated in full, with a closing table.'),
 ('Appendices', 'The passages at a glance, the key passages in full and a verse-by-verse index of where the passages are read.'),
 ('Bibliography', 'Every work cited, listed by author and title.')]
setl(39, ''.join('<div class="include-item"><h3>%s</h3><p>%s</p></div>' % i for i in inc))
setl(40, '</div> <div class="final-buy"><div><div class="eyebrow">COMMENTARY COLLECTION · SINGLE VOLUME SERIES</div><h2>The End of the Lost</h2><p>66-page digital PDF · For personal use</p></div><div class="final-offer"><div class="detail-price">$14.99</div><span class="detail-button pending" aria-disabled="true">Checkout Coming Soon</span></div></div>')
setl(41, '<a class="back-link" href="commentary.html#end-of-the-lost">← Back to the Commentary Collection</a>')
open(DST, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', DST, len(L))
