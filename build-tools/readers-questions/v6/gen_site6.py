"""Volume 6 website package generator (question pages, volume page, index, Questions page block, sitemap)."""
import re,json,html as H,sys,os,unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import kjvlib
from c1 import ENTRIES as A
from c2 import ENTRIES as B
import rev
E=A+B; rev.apply(E)
R='/home/claude/zay-marie-press/'
V5=R+'reader-questions-05-questions-on-difficult-bible-verses.html'
VP='reader-questions-06-questions-on-difficult-bible-verses.html'
PDF='assets/reader-questions-06-questions-on-difficult-bible-verses.pdf'
SHARE='https://zaymariepress.com/assets/share-reader-questions-06-questions-on-difficult-bible-verses.jpg'
PAGES=26
def esc(s): return H.escape(s,quote=True)
STOP=set('what does is are who in the of a an mean means and to by have i my me unto from do for with it that be this these those at on as or his her their'.split())
def slugify(t):
    t=t.replace('–',' '); t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower()
    return '-'.join([w for w in re.findall(r'[a-z0-9]+',t) if w not in STOP][:7])
def plain(s): return re.sub(r'<[^>]+>','',H.unescape(s))
def rqn(s): return re.sub(r'<b>(.*?)</b>',r'<span class="rq-n">\1</span>',s)
DESC=("Reader Questions Volume 6 answers ten questions readers ask about psalms the New Testament quotes, among them why Jesus cried “My God, my God, why hast thou forsaken me,” what “ye are gods” means, why Satan quoted Psalm 91, whether believers may pray the cursing psalms, and what “this day have I begotten thee” means. Each answer is argued from the psalm’s own passage and the chapter that quotes it.")
v5=open(V5,encoding='utf-8').read()
def retag(h):
    h=h.replace('reader-questions-05','reader-questions-06').replace('Volume 5','Volume 6').replace('VOLUME&nbsp;5','VOLUME&nbsp;6').replace('Volume&nbsp;5','Volume&nbsp;6')
    return h
# ---------- volume page head
i=v5.find('<main'); head=retag(v5[:i]); foot=v5[v5.find('</main>')+7:]
d5=re.search(r'<meta name="description" content="([^"]*)"',head)
head=head.replace('"position": 5','"position": 6').replace('"numberOfPages": 25','"numberOfPages": %d'%PAGES)
old=re.findall(r'Reader Questions Volume 6 answers ten questions readers ask about daily[^"]*',head)
for o in set(old): head=head.replace(o,DESC.replace('"','\\"') if o.endswith('\\') else DESC)
# fix: description inside JSON needs escaped quotes only if they are straight (they are curly) -> fine
q=[]
# ---------- question pages
tpl5=open(R+'reader-questions-v5-q10-conscience-romans-2-15.html',encoding='utf-8').read()
th=tpl5[:tpl5.find('<main')]; tf=tpl5[tpl5.find('</main>')+7:]
def qhead(title,desc,url,ld):
    h=th
    h=re.sub(r'<title>.*?</title>','<title>'+esc(title)+' | Reader Questions | Zay-Marie Press</title>',h,1)
    for pat,val in [(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+esc(desc)+'">'),(r'<link rel="canonical" href="[^"]*">','<link rel="canonical" href="'+url+'">'),(r'<meta property="og:title" content="[^"]*">','<meta property="og:title" content="'+esc(title)+'">'),(r'<meta property="og:description" content="[^"]*">','<meta property="og:description" content="'+esc(desc)+'">'),(r'<meta property="og:url" content="[^"]*">','<meta property="og:url" content="'+url+'">'),(r'<meta property="og:image" content="[^"]*">','<meta property="og:image" content="'+SHARE+'">'),(r'<meta name="twitter:title" content="[^"]*">','<meta name="twitter:title" content="'+esc(title)+'">'),(r'<meta name="twitter:image" content="[^"]*">','<meta name="twitter:image" content="'+SHARE+'">')]:
        h=re.sub(pat,lambda m:val,h,1)
    h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>',h,1,flags=re.S)
    return h
def kjvcell(ref):
    return ' … '.join('“'+kjvlib.text(p.strip())+'”' for p in ref.split(';'))
slugs=[(f'reader-questions-v6-q{k:02d}-'+slugify(re.sub(r'^\d+\.\s*','',e['title']))+'.html', re.sub(r'^\d+\.\s*','',e['title'])+((' '+e['sub'].replace('&amp;','&')) if re.search(r'\d',e['sub']) else '')) for k,e in enumerate(E,1)]
index=[]
for k,e in enumerate(E,1):
    fn,tt=slugs[k-1]; title=re.sub(r'^\d+\.\s*','',e['title'])
    kt=(f'<div class="rq-tbl"><table><tr><th>Verse</th><th>KJV text</th><th>What to observe</th></tr>'+''.join(f'<tr><td>{esc(r[0])}</td><td>{kjvcell(r[1])}</td><td>{r[2]}</td></tr>' for r in e['rows'])+'</table></div>')
    rt=('<div class="rq-tbl"><table class="c"><tr><th>Reading</th><th>What it must say</th><th>Where it strains</th></tr>'+''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in e['rtbl'])+'</table></div>')
    carry='<ul>'+''.join(f'<li><span class="rq-n">{t}:</span> {x}</li>' for t,x in e['carry'])+'</ul>'
    other='<ul>'+''.join(f'<li>{rqn(x)}</li>' for x in e['other'])+'</ul>'
    prev=slugs[k-2] if k>1 else None; nxt=slugs[k] if k<10 else None
    nav='<div class="rq-nav">'+(f'<a href="{prev[0]}">← Question {k-1}: {esc(prev[1])}</a>' if prev else '<span></span>')+(f'<a href="{nxt[0]}">Question {k+1}: {esc(nxt[1])} →</a>' if nxt else '<span></span>')+'</div>'
    url='https://zaymariepress.com/'+fn
    ans=e['answer']; desc=plain(ans); desc=desc if len(desc)<=300 else desc[:297].rsplit(' ',1)[0]+'…'
    full=tt
    ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":full,"acceptedAnswer":{"@type":"Answer","text":plain(ans)}}],"isPartOf":{"@type":"Book","name":"Reader Questions, Volume 6","url":"https://zaymariepress.com/"+VP},"author":{"@type":"Person","name":"Alexander S. Marien"},"publisher":{"@type":"Organization","name":"Zay-Marie Press"},"inLanguage":"en","isAccessibleForFree":True}
    main=(f'<main><section class="detail-hero"><div class="wrap"><div class="eyebrow">READERS QUESTION SERIES · VOLUME&nbsp;6 · QUESTION&nbsp;{k}</div><h1>{esc(full)}</h1>'
      f'<p class="detail-copy">From <a href="{VP}">Reader Questions, Volume 6: Questions on Difficult Bible Verses</a>. Free to read here; the whole volume is a free PDF.</p>'
      f'<div class="detail-buyline"><span class="detail-price">Free</span><a class="detail-button" href="{PDF}" download>Download Volume 6 (PDF)</a></div></div></section>'
      f'<section class="detail-section"><div class="wrap rq-q"><div class="rq-answer"><div class="eyebrow">THE ANSWER</div><p>{ans}</p></div>'
      f'<h2>Where the Verses Stand</h2><p>{e["stand"][0]}</p>{kt}<h2>What Carries the Weight</h2>{carry}<h2>The Other Readings</h2>{other}{rt}'
      f'<h2>What It Means for the Reader</h2><p>{e["means"][0]}</p><h2>Related Reading</h2><p>{rqn(e["related"])}</p>'
      +nav+f'<div class="rq-get"><p>All ten questions in Volume 6 are in one free PDF, with the passages quoted in full.</p><a class="detail-button" href="{PDF}" download>Download the Free PDF</a></div>'
      +f'<a class="back-link" href="{VP}#free">← All ten questions in Volume 6</a> &nbsp; <a class="back-link" href="questions.html">← Reader Questions</a></div></section></main>')
    open(R+fn,'w',encoding='utf-8').write(qhead(full,desc,url,ld)+main+tf)
    index.append({"v":6,"n":k,"t":full,"u":fn,"s":plain(ans),"a":plain(ans)})
# ---------- volume page main
def short_list():
    out=[]
    for k,e in enumerate(E,1):
        out.append(f'<details><summary><span>{k}.</span> {esc(re.sub(r"^\d+\.\s*","",e["title"]))} ({e["sub"]})</summary><div class="rq-body"><p>{e["answer"]}</p><p class="rq-more"><a href="{slugs[k-1][0]}">Read the full answer →</a> · <a href="#get-volume" class="rq-buy">or download the whole volume as a free PDF</a></p></div></details>')
    return ''.join(out)
def kc(ref,label):
    return f'<div class="scripture-card"><h3>{label}</h3><p>{kjvcell(ref)}</p></div>'
cards=''.join([kc('Ps 22:1','Psalm 22:1'),kc('John 10:34','John 10:34'),kc('Ps 91:11','Psalm 91:11'),kc('Heb 2:8–9','Hebrews 2:8–9'),kc('Eph 4:8','Ephesians 4:8'),kc('2Pet 3:8','2 Peter 3:8'),kc('Heb 4:9','Hebrews 4:9'),kc('Ps 2:7','Psalm 2:7')])
def pt(h,p): return f'<div class="study-point"><h3>{h}</h3><p>{p}</p></div>'
points=''.join([pt('The Cry on the Cross','Read Matthew 27:46 with Psalm 22 to see how the scene is built from the psalm and where the psalm turns.'),
 pt('“Ye Are Gods”','Set John 10:34–36 beside Psalm 82 and Exodus 22 to see who is addressed and what Jesus uses the line to answer.'),
 pt('The Temptation Quotation','Read Psalm 91:9–12 with Matthew 4:5–7 and Deuteronomy 6:16 to see what the quotation leaves out.'),
 pt('Dominion and the World to Come','Follow Psalm 8 into Hebrews 2:5–9 to see what the writer says is seen and not yet seen.'),
 pt('The Cursing Psalms','Read Psalm 69:25 and 109:8 in Acts 1:20 beside Romans 12:14, 19 to see where each is spoken and to whom.'),
 pt('Anger, Gifts, Years, Rest and Sonship','Trace Psalm 4:4, 68:18, 90:4, 95:7–11 and 2:7 into Ephesians, 2 Peter, Hebrews and Acts to see what each writer does with the line.')])
rel=('<div class="study-distinction"><h3>Related Reading</h3><div class="rel-cols"><div class="rel-stack"><div class="rel-col o1"><h4>Digital Studies</h4>'
 '<p><a href="study-24-the-willful-sin-warning.html">Study 24 — The Willful Sin Warning</a> Reports the Hebrews 3 wilderness warning as written; entry 9 argues what the rest is.</p>'
 '<p><a href="study-28-the-warning-of-hebrews-6-4-6.html">Study 28 — The Warning of Hebrews 6:4–6</a> Reports Hebrews’ warnings as written; entry 9 argues the rest and the audience.</p>'
 '<p><a href="study-82-the-kinsman-redeemer.html">Study 82 — The Kinsman-Redeemer</a> Reports Hebrews 2 as written; entry 4 argues one quotation.</p></div>'
 '<div class="rel-col o2"><h4>Commentary Series</h4>'
 '<p><a href="commentary-gospel-02-the-lords-ministry-to-israel.html">Gospel Commentary, Volume 2 — The Lord’s Ministry to Israel</a> Argues the Lord’s ministry to Israel, John 10 among it.</p>'
 '<p><a href="commentary-acts-01-what-the-twelve-were-told-and-did.html">Acts Commentary, Volume 1 — What the Twelve Were Told, and Did</a> Argues Acts 1–8, the setting of Acts 1:20.</p>'
 '<p><a href="commentary-typology-01-tabernacle-and-temple-typology.html">Typology Commentary, Volume 1 — Tabernacle &amp; Temple Typology</a> Argues the rent veil of Matthew 27:51.</p></div></div>'
 '<div class="rel-stack"><div class="rel-col o2"><h4>Bible Book Companion Series</h4>'
 '<p><a href="packet-psalms.html">Bible Book Companion — Psalms</a> Interprets the book through its key passages.</p>'
 '<p><a href="packet-hebrews.html">Bible Book Companion — Hebrews</a> Interprets the book through its key passages.</p>'
 '<p><a href="packet-acts.html">Bible Book Companion — Acts</a> Interprets the book through its key passages.</p></div></div></div>'
 '<p class="connection-guide-link"><a href="questions.html">See the Questions page →</a></p></div>')
main=(f'<main><section class="detail-hero"><div class="wrap detail-hero-grid"><div class="detail-cover"><picture><source srcset="assets/reader-questions-06-cover.webp" type="image/webp"><img src="assets/reader-questions-06-cover.jpg" alt="Reader Questions, Volume 6: Questions on Difficult Bible Verses cover"></picture></div><div><div class="eyebrow">READERS QUESTION SERIES · VOLUME&nbsp;6</div><h1>Reader Questions</h1><p class="detail-subtitle">Questions on Difficult Bible Verses</p><p class="detail-kicker">What does this psalm mean, and what does the New Testament do with it?</p>'
 '<p class="detail-copy">A reader asks about one psalm the New Testament quotes: why Jesus cried from Psalm 22, what “ye are gods” means, why Satan quoted Psalm 91, what the rest in Psalm 95 is. Each entry gives the answer first, then walks back through the psalm and the chapter that quotes it, and marks every point as stated, shown by the context or inferred.</p>'
 '<p class="detail-copy">The entries argue a position and say so. Where another reading is held, it is set beside the answer with the place where it strains.</p>'
 f'<div class="detail-buyline"><span class="detail-price">Free</span><span class="detail-format">Digital PDF · {PAGES} Pages</span><a class="detail-button" href="{PDF}" download>Download the Free PDF</a></div></div></div></section> '
 '<section class="detail-section"><div class="wrap"><div class="eyebrow">ABOUT THIS VOLUME</div><h2>One Psalm, Read Where It Is Quoted</h2>'
 '<p class="lead">Each entry answers one question about one psalm and the New Testament passage that quotes it. It begins with the verse, reads it in its own passage and in the chapter before it, and lets the rest of Scripture support what the context shows.</p>'
 '<p class="lead">It is the sixth volume of the Readers Question Series. It is shorter than a Commentary Volume and takes one question at a time, and it is a different kind of book from a Digital Study, which reports what a passage says and leaves the question open. Scripture is quoted from the King James Version throughout.</p>'
 +rel+'<div class="eyebrow">WHAT THE VOLUME COVERS</div><h2>Ten Questions, Ten Psalms</h2><div class="study-points">'+points+'</div> '
 '<div class="eyebrow" id="free">FREE SHORT ANSWERS</div><h2>The Ten Questions, Answered in Brief</h2><p class="lead">Open a question to read its short answer. Each question has its own page with the full entry, with the passage in its context, the evidence, the other readings and what the answer means, and the whole volume is a free PDF.</p><div class="rq-free">'+short_list()+'</div> '
 '<div class="eyebrow">KEY SCRIPTURES</div><h2>Read the Word in Its Context</h2><div class="scripture-grid">'+cards+'</div> '
 '<div class="eyebrow">FROM THE VOLUME</div><h2>How Each Entry Works</h2><div class="excerpt"><blockquote>Each entry marks what the text states, what the context shows, and what is inferred, so that the reader can see what carries the weight and judge it.</blockquote><p>The entries argue a position, and the other readings are set beside it with the places where each strains.</p></div> '
 '<div class="eyebrow" id="look-inside">A LOOK INSIDE</div><h2>Preview the Volume Before You Download</h2><p class="preview-instruction">Click any page to enlarge it for reading.</p><div class="preview-grid">'
 '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/reader-questions-06-page-1.jpg"><img src="assets/reader-questions-06-page-1.jpg" alt="Volume 6 title page, how to read this volume and contents"></a><div class="page-no">Interior Page 1</div><h3>How to Read This Volume</h3><p>See the plan of every entry and the ten questions the volume answers.</p></div>'
 '<div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/reader-questions-06-page-2.jpg"><img src="assets/reader-questions-06-page-2.jpg" alt="Volume 6 first entry opening, the answer, context and KJV passages"></a><div class="page-no">Interior Page 2</div><h3>The First Entry Opens</h3><p>See an entry begin with its answer, then the question’s setting and the passages quoted in full from the King James Version.</p></div></div> '
 '<div class="eyebrow">WHAT’S INCLUDED</div><h2>Ten Answers in One Volume</h2><div class="includes-grid">'
 f'<div class="include-item"><h3>{PAGES}-Page Free Digital PDF</h3><p>Cover and a fully numbered interior.</p></div>'
 '<div class="include-item"><h3>Ten Full Entries</h3><p>Each question answered from the psalm’s own passage and the chapter that quotes it.</p></div>'
 '<div class="include-item"><h3>Marked Evidence</h3><p>Every point marked as stated, shown by the context, or inferred.</p></div>'
 '<div class="include-item"><h3>KJV Tables</h3><p>The passages quoted in full, beside what to observe in each.</p></div>'
 '<div class="include-item"><h3>Other Readings</h3><p>The competing readings set beside the answer, with where each strains.</p></div>'
 '<div class="include-item"><h3>What It Means</h3><p>What each answer means for the reader.</p></div>'
 '<div class="include-item"><h3>Related Reading</h3><p>Commentaries and Bible Book Companions on the same passages.</p></div>'
 '<div class="include-item"><h3>Passages Quoted</h3><p>An index of every passage printed in the volume, by entry.</p></div></div> '
 f'<div class="final-buy" id="get-volume"><div><div class="eyebrow">READERS QUESTION SERIES · VOLUME&nbsp;6</div><h2>Reader Questions, Volume 6</h2><p>{PAGES}-page digital PDF · Free · For personal use</p></div><div class="final-offer"><div class="detail-price">Free</div><a class="detail-button" href="{PDF}" download>Download the Free PDF</a></div></div><a class="back-link" href="questions.html">← Back to the Questions page</a></div></section> </main>')
open(R+VP,'w',encoding='utf-8').write(head+main+retag(foot))
# ---------- index
ix=json.load(open(R+'assets/reader-questions-index.json',encoding='utf-8'))
ix=[x for x in ix if x['v']!=6]+index
json.dump(ix,open(R+'assets/reader-questions-index.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(ix),'index entries')
json.dump([s[0] for s in slugs],open(os.path.dirname(os.path.abspath(__file__))+'/slugs.json','w'))
