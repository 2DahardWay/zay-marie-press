"""Generate study-88-unequally-yoked.html from the Study 87 page by segment replacement (run from repo root)."""
import re
SRC='study-87-the-last-days.html'; DST='study-88-unequally-yoked.html'
s=open(SRC,encoding='utf-8').read()
def sub(a,b,new):
    global s
    i=s.index(a); j=s.index(b,i); s=s[:i]+new+s[j:]
DESC='Study 88 walks 2 Corinthians 6:14–7:1 in order, separating what Paul commands the Corinthian assembly, what he quotes from Israel’s Scriptures and what he applies, with each quoted line read in its own chapter first. Preview the 16-page digital study.'
old=re.search(r'<meta name="description" content="([^"]*)"',s).group(1)
s=s.replace(old,DESC)
s=s.replace('The Last Days | Zay-Marie Press','Unequally Yoked | Zay-Marie Press')
s=s.replace('study-87-the-last-days.html','study-88-unequally-yoked.html').replace('study-87-','study-88-').replace('share-study-87','share-study-88').replace('#study-87','#study-88')
s=s.replace(old,DESC)
sub('"name":"The Last Days"','"inLanguage"','"name":"Unequally Yoked","alternativeName":"What Paul Commands, What He Quotes, and What He Applies in 2 Corinthians 6:14–7:1","author":{"@type":"Person","name":"Alexander S. Marien"},"publisher":{"@type":"Organization","name":"Zay-Marie Press"},"description":"2 Corinthians 6:14–7:1 holds a command, a chain of quotations from Israel’s Scriptures and an application. This study walks the passage in order, reading each quoted line in its own chapter before Paul’s use of it.","image":"https://zaymariepress.com/assets/study-88-cover.jpg","url":"https://zaymariepress.com/study-88-unequally-yoked.html",')
s=s.replace('"position":87','"position":88')
s=s.replace('STUDY 87 · DIGITAL STUDY','STUDY 88 · DIGITAL STUDY')
s=s.replace('<h1>The Last Days</h1>','<h1>Unequally Yoked</h1>').replace('alt="The Last Days cover"','alt="Unequally Yoked cover"')
sub('<p class="detail-subtitle">','<div class="detail-buyline">','<p class="detail-subtitle">What Paul Commands, What He Quotes, and What He Applies in 2 Corinthians 6:14–7:1</p><p class="detail-kicker">In 2 Corinthians 6:14–7:1, what does Paul command the Corinthian assembly, what does he quote from Israel’s Scriptures, and what does he apply from them?</p><p class="detail-copy">“Be ye not unequally yoked together with unbelievers” is read as a rule for marriage, business, friendship and church membership, sometimes all in one sermon. Then the passage turns, and Paul quotes Israel’s Scriptures in a chain of promises. The reader is left holding a command, a stack of quotations and no clear way to say how they fit together.</p><p class="detail-copy">This study walks the passage in order. It keeps three questions apart: what Paul commands, what he quotes, and what he applies. Each quoted line is read in its own chapter, audience and setting before Paul’s use of it is read.</p>')
sub('<h2>Ask Who Speaks, Who Hears and What Follows</h2>','<div class="study-distinction">','<h2>Keep the Command, the Quotation and the Application Apart</h2><p class="lead">You will read the frame of 6:11–13 and 7:2–4, the command of 6:14a, the five questions of 6:14b–16a, Paul’s own statement in 6:16a, and then the lines gathered in 6:16b–18 beside Leviticus 26, Ezekiel 37, Isaiah 52 and 2 Samuel 7, each in its own chapter. The study then reads the application in 7:1 and lists what the passage does not say.</p><p class="lead">Readers who already own Study 39 (The Church’s Relationship to Israel’s Scriptures), Study 37 (What Does Paul Mean by “New Creation”?), Study 45 (Sanctification Under Grace) or Study 52 (Sonship and Adoption) will recognize adjoining ground. Study 39 sets out the repeatable method for how the Body learns from Israel’s Scriptures, while this study walks one passage; Study 37 reads what “new creation” itself asserts, and this study does not enter 5:17; Study 45 reads the several things Paul means by sanctification language, and this study handles only 7:1; Study 52 reads sonship and adoption in Paul’s letters, and this study reports the Father and sons language only as part of the quoted chain. The question this study alone answers: in 2 Corinthians 6:14–7:1, what is Paul’s own command, what is quoted from Israel’s Scriptures, and what does he apply to Corinth?</p>\n')
rel='''<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4><p><a href="study-39-the-churchs-relationship-to-israels-scriptures.html">Study 39 — The Church’s Relationship to Israel’s Scriptures</a> Set out the repeatable method for how the Body learns from Israel’s Scriptures; Study 88 walks one passage.</p><p><a href="study-37-what-does-paul-mean-by-new-creation.html">Study 37 — What Does Paul Mean by “New Creation”?</a> Read what “new creation” itself asserts; Study 88 does not enter 5:17.</p><p><a href="study-45-sanctification-under-grace.html">Study 45 — Sanctification Under Grace</a> Read the several things Paul means by sanctification language; Study 88 handles only 7:1.</p></div></div><div class="rel-stack"><div class="rel-col o2"><h4>Commentary Series</h4><p><a href="commentary-typology-01-tabernacle-and-temple-typology.html">Typology Commentary Series, Volume 1 — Tabernacle and Temple Typology</a> Argues the tabernacle and temple pattern in Israel’s Scriptures; Study 88 reads Paul’s temple statement in its passage and does not argue the pattern.</p><p><a href="commentary-typology-02-prophetic-separation.html">Typology Commentary Series, Volume 2 — Prophetic Separation</a> Argues God separating the judged from the kept in Israel’s Tribulation; Study 88 concerns a believer’s separation from idolatry and unbelieving fellowship, a different subject.</p><p><a href="commentary-identity-03-the-new-covenant.html">Prophetic Identity Commentary Series, Volume 3 — The New Covenant</a> Argues the new covenant as promised to Israel; Study 88 reads the Leviticus and Ezekiel lines in their own settings and does not argue the covenant.</p></div></div></div><p class="connection-guide-link"><a href="study-connections.html#study-88">Explore the full connection guide for Study 88 →</a></p></div>
'''
sub('<div class="study-distinction">','<div class="eyebrow">WHAT YOU’LL STUDY</div>',rel)
s=s.replace('<h2>Follow the Phrase Through the Passages</h2>','<h2>Follow Command, Quotation and Application</h2>')
pts=[('Five Paired Contrasts','Trace the five paired contrasts in 6:14–16a by following each term Paul sets against another.'),
('“As God Hath Said”','Follow the words “as God hath said” back to the Old Testament lines Paul gathers in 6:16–18.'),
('Each Source in Its Own Setting','Read each quoted line in its own chapter, audience and setting before reading Paul’s use of it.'),
('Paul’s Wording Compared','Compare Paul’s wording with the wording of each source and note where he changes it.'),
('Command and Quotation Separated','Separate what Paul directly commands the Corinthian assembly from what he quotes.'),
('The Application in 7:1','Test the application in 7:1 against the passage’s own words.')]
h=''.join(f'<div class="study-point"><h3>{a}</h3><p>{b}</p></div>' for a,b in pts)
sub('<div class="study-points">','</div>\n<div class="eyebrow">KEY SCRIPTURES','<div class="study-points">'+h)
cards=[('2 Corinthians 6:14–16a','“Be ye not unequally yoked together with unbelievers,” followed by five questions built on “what.”'),
('2 Corinthians 6:16a','“Ye are the temple of the living God,” in Paul’s own voice and before the words “as God hath said.”'),
('Leviticus 26:11–12','“And I set my tabernacle among you,” spoken in a chapter of blessings and warnings.'),
('Ezekiel 37:26–27','“My tabernacle also shall be with them: yea, I will be their God, and they shall be my people.”'),
('Isaiah 52:11','A command addressed to those who “bear the vessels of the LORD,” in the setting of Zion’s redemption.'),
('2 Samuel 7:14','“I will be his father, and he shall be my son,” spoken to David through Nathan.'),
('2 Corinthians 7:1','“Let us cleanse ourselves from all filthiness of the flesh and spirit.”'),
('Deuteronomy 22:10','“Thou shalt not plow with an ox and an ass together,” read as an echo and nothing more.')]
def slug(t): return 'sc-'+re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
h=''.join(f'<div class="scripture-card" id="{slug(a)}"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)
sub('<div class="scripture-grid">','</div>\n<div class="eyebrow">FROM THE STUDY','<div class="scripture-grid">'+h)
sub('<blockquote>','</div>\n<div class="eyebrow">A LOOK INSIDE','<blockquote>In 2 Corinthians 6:14–7:1 there are three kinds of statement: what Paul commands, what he quotes, and what he applies. Keep them in three separate columns in your notes as you read.</blockquote><p>The study keeps those three columns apart from the first section to the last.</p>')
prev=[(1,'Table of Contents','See the full structure and the passages examined.','Study 88 table of contents'),
(2,'What You Will Learn','See the study’s scope and reading procedure.','Study 88 learning outcomes'),
(5,'The Five Questions','See how the study sets the five questions of 6:14b–16a in a KJV table, with what to observe.','Study 88 five questions of 2 Corinthians 6:14b–16a in a table')]
h=''.join(f'<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/study-88-page-{n}.jpg"><img src="assets/study-88-page-{n}.jpg" alt="{alt}"></a><div class="page-no">Interior Page {n}</div><h3>{t}</h3><p>{d}</p></div>' for n,t,d,alt in prev)
sub('<div class="preview-grid">','</div>\n<div class="eyebrow">WHAT’S INCLUDED','<div class="preview-grid">'+h)
s=s.replace('A Focused Study of Every Place the Phrase Is Printed','A Focused Study of One Passage, Verse by Verse')
s=s.replace('<h3>8 Teaching Sections</h3><p>A text-driven walk from the wordings in the King James Version to the passages side by side.</p>','<h3>7 Teaching Sections</h3><p>A text-driven walk from the frame of the passage to what it does not say.</p>')
s=s.replace('<h2>The Last Days</h2><p>16-page','<h2>Unequally Yoked</h2><p>16-page')
s=s.replace('Study 87','Study 88')
open(DST,'w',encoding='utf-8').write(s)
bad=[w for w in ['Last Days','last days','latter days','Study 87','study-87','87'] if w in s]
print('leftovers:',bad)
