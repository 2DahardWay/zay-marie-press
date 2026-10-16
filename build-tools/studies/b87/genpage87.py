"""Generate study-87-the-last-days.html from the Study 86 page by exact-substring replacement (run from repo root)."""
import re
SRC='study-86-the-servant-in-isaiah.html'; DST='study-87-the-last-days.html'
s=open(SRC).read()
def cut(a,b):
    i=s.index(a); j=s.index(b,i); return i,j
def sub(a,b,new):
    global s
    i,j=cut(a,b); s=s[:i]+new+s[j:]
# ---- head/meta
DESC='Study 87 reads every place the King James Version prints “the last days,” “the latter days” and their near wordings, recording who speaks, who hears, what each passage says follows and what it leaves unsaid. Preview the 16-page digital study.'
old_desc=re.search(r'<meta name="description" content="([^"]*)"',s).group(1)
s=s.replace(old_desc,DESC)
s=s.replace('The Servant in Isaiah | Zay-Marie Press','The Last Days | Zay-Marie Press')
s=s.replace('study-86-the-servant-in-isaiah.html','study-87-the-last-days.html').replace('share-study-86.jpg','share-study-87.jpg')
s=s.replace('study-86-cover','study-87-cover').replace('#study-86','#study-87')
# JSON-LD
sub('"name":"The Servant in Isaiah"','"inLanguage"','"name":"The Last Days","alternativeName":"Where Scripture Uses the Phrase, of Whom Each Passage Speaks, and What It Leaves Unsaid","author":{"@type":"Person","name":"Alexander S. Marien"},"publisher":{"@type":"Organization","name":"Zay-Marie Press"},"description":"The words “the last days” and “the latter days” stand in many passages, spoken by different people to different hearers. This study reads each place in its own chapter, recording who speaks, who hears, what each passage says follows and what it leaves unsaid.","image":"https://zaymariepress.com/assets/study-87-cover.jpg","url":"https://zaymariepress.com/study-87-the-last-days.html",')
s=s.replace('"position":86','"position":87')
# ---- hero
s=s.replace('STUDY 86 · DIGITAL STUDY','STUDY 87 · DIGITAL STUDY')
s=s.replace('<h1>The Servant in Isaiah</h1>','<h1>The Last Days</h1>')
s=s.replace('alt="The Servant in Isaiah cover"','alt="The Last Days cover"')
sub('<p class="detail-subtitle">','<p class="detail-kicker">','<p class="detail-subtitle">Where Scripture Uses the Phrase, of Whom Each Passage Speaks, and What It Leaves Unsaid</p>')
sub('<p class="detail-kicker">','<div class="detail-buyline">','<p class="detail-kicker">Where does the King James Version say “the last days” or “the latter days,” who is speaking in each place, and what does the passage say follows?</p><p class="detail-copy">“The last days” is a phrase heard in sermons, charts and headlines, and it is usually taken to name one period. Yet the King James Version prints it, and its near wordings, in the mouths of Jacob, Balaam, Moses, the prophets, Peter, Paul and the writers of the letters. This study reads each place in its own chapter.</p><p class="detail-copy">It asks four things of every passage: who speaks, who is addressed, what the passage says follows the phrase, and what it leaves unsaid. It then sets the passages side by side and tests three common readings against the words.</p>')
# ---- about
sub('<h2>Ask Whom Each Passage Names','<div class="study-distinction">','<h2>Ask Who Speaks, Who Hears and What Follows</h2><p class="lead">You will sort the wordings the King James Version prints, read Genesis 49:1, Numbers 24:14 and Deuteronomy 4:30 and 31:29, compare Isaiah 2:2 with Micah 4:1, read the time words of Jeremiah, Ezekiel, Hosea and Daniel, read Acts 2:14–21 beside Joel, follow the six letters that use the phrase and the letters to Timothy, and then set the passages side by side.</p><p class="lead">Readers who already own Study 7 (The Day of the Lord), Study 20 (Understanding Acts 2:38), Study 74 (The Man of Sin) or Study 80 (The Lamb Foreordained) will recognize adjoining ground. Study 7 reads the passages on that day across the Scriptures; Study 20 sets Joel 2:28–32 beside Acts 2:16–21 for the sake of Acts 2:38, while this study reports only the opening phrase of Acts 2:17; Study 74 reports the final-ruler passages, and this study reads 1 John 2:18 only for the words “the last time”; Study 80 reads 1 Peter 1:20 among the passages on the foundation of the world, and this study reads it only for “these last times.” The question this study alone answers: where does the King James Version print “the last days,” “the latter days” and their near wordings, to whom is each spoken, what does each passage say follows, and what does each leave unsaid?</p>\n')
# ---- related reading
sub('<div class="study-distinction">','<p class="connection-guide-link">','''<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4><p><a href="study-07-the-day-of-the-lord.html">Study 7 — The Day of the Lord</a> Read the passages on that day across the Scriptures; Study 87 reads only the places that print “the last days” and “the latter days” and does not follow the day.</p><p><a href="study-20-understanding-acts-2-38.html">Study 20 — Understanding Acts 2:38</a> Set Joel 2:28–32 beside Acts 2:16–21 for the sake of Acts 2:38; Study 87 reports only the opening phrase of Acts 2:17.</p><p><a href="study-74-the-man-of-sin.html">Study 74 — The Man of Sin</a> Report the final-ruler passages; Study 87 reads 1 John 2:18 only for the words “the last time.”</p></div></div><div class="rel-stack"><div class="rel-col o2"><h4>Commentary Series</h4><p><a href="commentary-acts-02-the-spirit-in-acts.html">Acts Commentary Series, Volume 2 — The Spirit in Acts</a> Argues that the four scenes in which Acts reports the Spirit’s coming follow no single order; Study 87 reports only the opening phrase of Acts 2:17 and builds no argument on the scenes.</p><p><a href="commentary-prophecy-mystery-03-the-kingdom-program.html">Prophecy &amp; Mystery Commentary Series, Volume 3 — The Kingdom Program</a> Argues that the kingdom is promised to Israel and still to come; Study 87 reads Isaiah 2:2 and Micah 4:1 only for the phrase and does not argue the kingdom.</p></div></div></div>''')
s=s.replace('connection guide for Study 86','connection guide for Study 87')
s=s.replace('<h2>Follow the Servant Through the Passages</h2>','<h2>Follow the Phrase Through the Passages</h2>')
# ---- what you'll study
pts=[('The Wordings in the King James Version','Locate each place where the King James Version prints “the last days,” “the latter days” or a near wording, and sort them by the exact words used.'),
('Four Questions for Each Passage','Read each passage in its own chapter and mark who speaks, who is addressed and what the passage says follows the phrase.'),
('Two Pairs Compared','Compare Isaiah 2:2 with Micah 4:1, and Joel’s opening words with Peter’s, and record which words agree and which differ.'),
('The Verbs of the New Testament','Follow the tense of the verbs in the New Testament passages (“hath spoken,” “was manifest,” “is,” “shall come”) without reconciling them beyond the text.'),
('The Readers Each Letter Names','Trace how the letter writers introduce the phrase, and note which readers each letter names for itself.'),
('Three Readings Tested','Test three common readings of the phrase against its own wording, sorting what the text states from what readers add.')]
h=''.join(f'<div class="study-point"><h3>{a}</h3><p>{b}</p></div>' for a,b in pts)
sub('<div class="study-points">','</div>\n<div class="eyebrow">KEY','<div class="study-points">'+h)
# ---- key scriptures
cards=[('Genesis 49:1; Numbers 24:14','Jacob tells his sons “that which shall befall you in the last days”; Balaam says what Israel “shall do to thy people in the latter days.”'),
('Deuteronomy 4:30; 31:29','Moses gives “the latter days” in two different sentences.'),
('Isaiah 2:2; Micah 4:1','Two prophets, near-identical words, and a mountain “in the last days.”'),
('Daniel 2:28; 10:14','“What shall be in the latter days,” spoken to a king and to Daniel.'),
('Daniel 12:4–13','“The time of the end” and “the end of the days.”'),
('Acts 2:14–21','“And it shall come to pass in the last days, saith God,” in Peter’s words.'),
('Hebrews 1:1–2','God “hath in these last days spoken unto us by his Son.”'),
('2 Timothy 3:1; 2 Peter 3:3','“In the last days perilous times shall come,” and scoffers “in the last days.”')]
h=''.join(f'<div class="scripture-card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)
sub('<div class="scripture-grid">','</div>\n<div class="eyebrow">FROM','<div class="scripture-grid">'+h)
# ---- from the study
sub('<blockquote>','</div>\n<div class="eyebrow">A LOOK','<blockquote>Each passage is read in its own place, with its speaker, its audience and the sentence that carries the phrase. A link between passages is made only where a passage makes it.</blockquote><p>Where the text is silent, the study records the silence and stops.</p>')
# ---- look inside
sub('<div class="preview-grid">','</div>\n<div class="eyebrow">WHAT’S','<div class="preview-grid"><div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/study-87-page-1.jpg"><img src="assets/study-87-page-1.jpg" alt="Study 87 table of contents"></a><div class="page-no">Interior Page 1</div><h3>Table of Contents</h3><p>See the full structure and the passages examined.</p></div><div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/study-87-page-2.jpg"><img src="assets/study-87-page-2.jpg" alt="Study 87 learning outcomes"></a><div class="page-no">Interior Page 2</div><h3>What You Will Learn</h3><p>See the study’s scope and reading procedure.</p></div><div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/study-87-page-6.jpg"><img src="assets/study-87-page-6.jpg" alt="Study 87 Isaiah 2:2 beside Micah 4:1 in a table"></a><div class="page-no">Interior Page 6</div><h3>Isaiah 2:2 Beside Micah 4:1</h3><p>See how the study sets two passages side by side in a table.</p></div>')
# ---- included
s=s.replace('A Focused Study of the Servant Passages of Isaiah 41–53','A Focused Study of Every Place the Phrase Is Printed')
s=s.replace('<h3>7 Teaching Sections</h3><p>A text-driven walk through Isaiah 41–53, from the setting to the passages side by side.</p>','<h3>8 Teaching Sections</h3><p>A text-driven walk from the wordings in the King James Version to the passages side by side.</p>')
s=s.replace('<h2>The Servant in Isaiah</h2><p>16-page','<h2>The Last Days</h2><p>16-page')
open(DST,'w').write(s)
bad=[w for w in ['Servant','servant','Isaiah 41','Study 86','86'] if w in re.sub(r'Isaiah 2:2|Isaiah 12','',s) and w not in('Isaiah 41',)]
print('leftovers:',[ (w,[m.start() for m in re.finditer(w,s)][:3]) for w in bad])
