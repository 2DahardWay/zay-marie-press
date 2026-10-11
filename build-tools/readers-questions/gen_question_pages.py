import re,json,os,html as H,unicodedata
from bs4 import BeautifulSoup
SP='/tmp/claude-0/-home-claude-zay-marie-press/34ae0af5-839e-5dbd-b659-ae9d557f675c/scratchpad/'
REPO='/home/claude/zay-marie-press/'
VOL={1:('rqv/vol1.html','reader-questions-01-ten-questions-on-difficult-verses.html'),
2:('rqv2/vol2.html','reader-questions-02-questions-on-difficult-bible-verses.html'),
3:('rqv3/vol3.html','reader-questions-03-questions-on-difficult-bible-verses.html'),
4:('rqv4/vol4.html','reader-questions-04-questions-on-difficult-bible-verses.html'),
5:('rqv5/vol5.html','reader-questions-05-questions-on-difficult-bible-verses.html')}
STOP=set('what does is are who in the of a an mean means and to by have i my me unto from do for with it that be this these those at on as or his her their'.split())
def slugify(t):
    t=re.sub(r'^\d+\.\s*','',t).replace('–',' '); t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower()
    ws=[w for w in re.findall(r'[a-z0-9]+',t)]
    keep=[w for w in ws if w not in STOP]
    return '-'.join(keep[:7])
def esc(s): return H.escape(s,quote=True)
vp={}  # volume page html
for v,(src,page) in VOL.items(): vp[v]=open(REPO+page,encoding='utf-8').read()
# head/foot template from vol 3 page
tpl=vp[3]; HEAD_END=tpl.find('<main'); FOOT_START=tpl.find('</main>')
FOOT=tpl[FOOT_START+len('</main>'):]
# drop the lightbox script from foot (no lightbox on question pages): keep as is - harmless
CSS='''<style>.rq-q{max-width:820px}.rq-q h2{font-family:Georgia,serif;color:#143823;font-size:1.45rem;margin:34px 0 10px}.rq-q p,.rq-q li{font-size:1.05rem;line-height:1.7}.rq-q ul{padding-left:22px}.rq-answer{background:#eef4ea;border-left:5px solid #b8871c;padding:20px 24px;margin:0 0 8px}.rq-answer .eyebrow{margin:0 0 6px}.rq-answer p{margin:0}.rq-n{color:#143823;font-weight:700}.rq-tbl{overflow-x:auto;margin:16px 0}.rq-tbl table{width:100%;border-collapse:collapse;font-size:.95rem;line-height:1.5;min-width:560px}.rq-tbl th{background:#3B6E91;color:#fff;text-align:left;padding:8px 10px;font-family:Arial,sans-serif;font-size:.78rem;letter-spacing:.04em;text-transform:uppercase}.rq-tbl td{border:1px solid #c9d6de;padding:8px 10px;vertical-align:top;background:#fff}.rq-nav{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin:38px 0 8px;padding-top:22px;border-top:1px solid #d8d1bf}.rq-nav a{font-family:Arial,sans-serif;font-weight:700;font-size:.9rem;color:#176b3a}.rq-bib{font-size:.92rem;color:#35433d}.rq-bib li{font-size:.92rem;line-height:1.55;margin-bottom:6px}.rq-get{background:#082d45;color:#fff;border-top:4px solid #b8871c;padding:26px 30px;margin:34px 0 0;display:flex;gap:24px;align-items:center;justify-content:space-between;flex-wrap:wrap}.rq-get p{color:#fff;margin:0;font-size:1rem}.rq-get .detail-button{background:#176b3a}@media(max-width:560px){.rq-answer{padding:16px 16px}.rq-get{padding:22px 20px}}</style>'''
def head(title,desc,url,img,ld):
    h=tpl[:HEAD_END]
    h=re.sub(r'<title>.*?</title>','<title>'+esc(title)+' | Reader Questions | Zay-Marie Press</title>',h,1)
    h=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+esc(desc)+'">',h,1)
    h=re.sub(r'<link rel="canonical" href="[^"]*">','<link rel="canonical" href="'+url+'">',h,1)
    h=re.sub(r'<meta property="og:type" content="[^"]*">','<meta property="og:type" content="article">',h,1)
    h=re.sub(r'<meta property="og:title" content="[^"]*">','<meta property="og:title" content="'+esc(title)+'">',h,1)
    h=re.sub(r'<meta property="og:description" content="[^"]*">','<meta property="og:description" content="'+esc(desc)+'">',h,1)
    h=re.sub(r'<meta property="og:url" content="[^"]*">','<meta property="og:url" content="'+url+'">',h,1)
    h=re.sub(r'<meta property="og:image" content="[^"]*">','<meta property="og:image" content="'+img+'">',h,1)
    h=re.sub(r'<meta name="twitter:title" content="[^"]*">','<meta name="twitter:title" content="'+esc(title)+'">',h,1)
    h=re.sub(r'<meta name="twitter:image" content="[^"]*">','<meta name="twitter:image" content="'+img+'">',h,1)
    h=re.sub(r'<script type="application/ld\+json">.*?</script>','<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>',h,1,flags=re.S)
    h=h.replace('</head>',CSS+'</head>')
    return h
def clean(el):
    """convert a PDF-html element to site html"""
    for t in el.find_all(True):
        if t.name=='span' and 'n' in (t.get('class') or []): t['class']=['rq-n']
        for a in ('style','width'):
            if t.has_attr(a): del t[a]
        if t.name=='span' and 'rq-n' not in (t.get('class') or []): t.unwrap()
    return el
def bib_items(soup):
    out=[]
    for h in soup.find_all('h1'):
        if 'Modern Writers' in h.get_text():
            ul=h.find_next('ul')
            out=[str(li) for li in ul.find_all('li')]
    return out
index=[];allpages={}
for v,(src,page) in VOL.items():
    s=open(SP+src,encoding='utf-8').read()
    body=s[s.find('</style>')+8:]
    parts=re.split(r'(?=<h1[ >])',body)
    ents=[p for p in parts if re.match(r'<h1[^>]*>\d+\. ',p)]
    assert len(ents)==10,(v,len(ents))
    bibsoup=BeautifulSoup(body,'html.parser'); bibs=bib_items(bibsoup)
    # short answers from the volume page
    rows=re.findall(r'<details><summary><span>(\d+)\.</span> (.*?)</summary><div class="rq-body"><p>(.*?)</p>',vp[v],flags=re.S)
    assert len(rows)==10,(v,len(rows))
    vpage=VOL[v][1]; share=f'https://zaymariepress.com/assets/share-{vpage.replace(".html",".jpg")}'
    pdf='assets/'+vpage.replace('.html','.pdf')
    slugs=[]
    for k,e in enumerate(ents,1):
        soup=BeautifulSoup(e,'html.parser')
        h1=soup.find('h1'); title=re.sub(r'^\d+\.\s*','',h1.get_text()).strip()
        slug=f'reader-questions-v{v}-q{k:02d}-'+slugify(title); fn=slug+'.html'; slugs.append((fn,title))
    for k,e in enumerate(ents,1):
        soup=BeautifulSoup(e,'html.parser')
        h1=soup.find('h1'); title=slugs[k-1][1]; fn=slugs[k-1][0]
        box=soup.find('div',class_='box'); assert box and 'Answer' in box.find('p',class_='t').get_text(),(v,k)
        answer=box.find_all('p')[1].get_text().strip()
        parts_html=[]
        for el in list(soup.children):
            if getattr(el,'name',None) in (None,'h1'): continue
            if el is box: continue
            if el.name=='h2':
                parts_html.append(f'<h2>{esc(el.get_text())}</h2>'); continue
            if el.name=='table':
                clean(el); parts_html.append('<div class="rq-tbl">'+str(el)+'</div>'); continue
            clean(el); parts_html.append(str(el))
        txt=BeautifulSoup(''.join(parts_html),'html.parser').get_text(' ')
        used=[b for b in bibs if re.match(r'<li>([^,]+),',b) and re.match(r'<li>([^,]+),',b).group(1).split()[-1] in txt]
        prev=slugs[k-2] if k>1 else None; nxt=slugs[k] if k<10 else None
        nav='<div class="rq-nav">'+(f'<a href="{prev[0]}">← Question {k-1}: {esc(prev[1])}</a>' if prev else '<span></span>')+(f'<a href="{nxt[0]}">Question {k+1}: {esc(nxt[1])} →</a>' if nxt else '<span></span>')+'</div>'
        url='https://zaymariepress.com/'+fn
        desc=re.sub(r'\s+',' ',rows[k-1][2]); desc=re.sub(r'<[^>]+>','',H.unescape(desc))
        desc=desc if len(desc)<=300 else desc[:297].rsplit(' ',1)[0]+'…'
        ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":title,"acceptedAnswer":{"@type":"Answer","text":answer}}],"isPartOf":{"@type":"Book","name":f"Reader Questions, Volume {v}","url":"https://zaymariepress.com/"+vpage},"author":{"@type":"Person","name":"Alexander S. Marien"},"publisher":{"@type":"Organization","name":"Zay-Marie Press"},"inLanguage":"en","isAccessibleForFree":True}
        main=(f'<main><section class="detail-hero"><div class="wrap"><div class="eyebrow">READERS QUESTION SERIES · VOLUME&nbsp;{v} · QUESTION&nbsp;{k}</div><h1>{esc(title)}</h1>'
              f'<p class="detail-copy">From <a href="{vpage}">Reader Questions, Volume {v}: Questions on Difficult Bible Verses</a>. Free to read here; the whole volume is a free PDF.</p>'
              f'<div class="detail-buyline"><span class="detail-price">Free</span><a class="detail-button" href="{pdf}" download>Download Volume {v} (PDF)</a></div></div></section>'
              f'<section class="detail-section"><div class="wrap rq-q"><div class="rq-answer"><div class="eyebrow">THE ANSWER</div><p>{esc(answer)}</p></div>'
              +''.join(parts_html)
              +(('<h2>Writers Named in This Answer</h2><ul class="rq-bib">'+''.join(used)+'</ul>') if used else '')
              +nav
              +f'<div class="rq-get"><p>All ten questions in Volume {v} are in one free PDF, with the bibliography and the passages quoted in full.</p><a class="detail-button" href="{pdf}" download>Download the Free PDF</a></div>'
              +f'<a class="back-link" href="{vpage}#free">← All ten questions in Volume {v}</a> &nbsp; <a class="back-link" href="questions.html">← Reader Questions</a>'
              +'</div></section></main>')
        page_html=head(title,desc,url,share,ld)+main+FOOT
        open(REPO+fn,'w',encoding='utf-8').write(page_html)
        sa=re.sub(r'<[^>]+>','',H.unescape(rows[k-1][2]))
        index.append({"v":v,"n":k,"t":title,"u":fn,"s":sa,"a":answer})
        allpages.setdefault(v,[]).append(fn)
json.dump(index,open(REPO+'assets/reader-questions-index.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
json.dump(allpages,open('/tmp/gq/pages.json','w'))
print(len(index),'pages');[print(i['u']) for i in index[:12]]
