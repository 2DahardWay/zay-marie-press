import re,json,glob
R='/home/claude/zay-marie-press/'
pages=json.load(open('/tmp/gq/pages.json'))
VP={1:'reader-questions-01-ten-questions-on-difficult-verses.html',2:'reader-questions-02-questions-on-difficult-bible-verses.html',3:'reader-questions-03-questions-on-difficult-bible-verses.html',4:'reader-questions-04-questions-on-difficult-bible-verses.html',5:'reader-questions-05-questions-on-difficult-bible-verses.html'}
for v,f in VP.items():
    s=open(R+f,encoding='utf-8').read()
    lst=pages[str(v)]; cnt=[0]
    def rep(m):
        k=cnt[0]; cnt[0]+=1
        return f'<p class="rq-more"><a href="{lst[k]}">Read the full answer →</a> · <a href="#get-volume" class="rq-buy">or download the whole volume as a free PDF</a></p>'
    s,c=re.subn(r'<p class="rq-more">This is the short answer only\..*?</p>',rep,s,flags=re.S); assert c==10,(v,c)
    a='These are summaries, not the complete answers. The complete answer to each question, with the passage in its context, the evidence, the other readings and the modern writers behind them, is in the full entry in this volume.'
    assert a in s,v
    s=s.replace(a,'These are summaries, not the complete answers. Each question has its own page with the full answer, with the passage in its context, the evidence, the other readings and the modern writers behind them, and the whole volume is a free PDF.')
    open(R+f,'w',encoding='utf-8').write(s)
q=open(R+'questions.html',encoding='utf-8').read()
box='''<section class="detail-section"><div class="wrap"><div class="eyebrow" id="search">SEARCH THE QUESTIONS</div><h2>Find a Verse or a Question</h2><p class="lead">Type a verse (Luke 17:21), a word (baptism, trumpet, thorn) or part of a question. Every result opens its own page with the full answer.</p><div class="rq-search"><label for="rq-q" class="sr-only">Search the questions</label><input id="rq-q" type="search" placeholder="Search the 50 questions" autocomplete="off"><div id="rq-count" aria-live="polite"></div><ol id="rq-results"></ol></div></div></section>'''
css='<style>.rq-search input{width:100%;max-width:640px;padding:14px 16px;font-size:1.05rem;border:2px solid #b9c7bc;border-radius:3px}.rq-search input:focus{outline:3px solid #176b3a33;border-color:#176b3a}#rq-count{margin:10px 0;color:#35433d;font-size:.95rem}#rq-results{list-style:none;padding:0;margin:0;max-width:820px}#rq-results li{padding:14px 0;border-bottom:1px solid #e6e0d0}#rq-results a{font-family:Georgia,serif;font-size:1.12rem;color:#143823;font-weight:700}#rq-results small{display:block;font-family:Arial,sans-serif;letter-spacing:.06em;color:#176b3a;text-transform:uppercase;margin-bottom:3px}#rq-results p{margin:4px 0 0;font-size:.98rem;line-height:1.55;color:#35433d}.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}</style>'
js='''<script>(function(){var inp=document.getElementById('rq-q'),out=document.getElementById('rq-results'),cnt=document.getElementById('rq-count'),data=null;
function norm(s){return s.toLowerCase().replace(/[\\u2018\\u2019\\u201c\\u201d"'.,;:?!()]/g,' ').replace(/[\\u2013\\u2014]/g,'-').replace(/\\s+/g,' ').trim();}
function load(cb){if(data)return cb();fetch('assets/reader-questions-index.json').then(function(r){return r.json()}).then(function(d){data=d.map(function(x){x.h=norm(x.t+' '+x.s);x.tt=norm(x.t);return x});cb();}).catch(function(){cnt.textContent='Search is not available right now. Use the volumes below.';});}
function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function run(){var t=norm(inp.value);out.innerHTML='';if(t.length<2){cnt.textContent='';return;}var ws=t.split(' ');var hits=data.filter(function(x){return ws.every(function(w){return x.h.indexOf(w)>-1})});hits.sort(function(a,b){return (b.tt.indexOf(t)>-1)-(a.tt.indexOf(t)>-1)||a.v-b.v||a.n-b.n});cnt.textContent=hits.length?hits.length+(hits.length===1?' question found':' questions found'):'No question matches. Try a verse such as Matthew 24 or a word such as baptism.';out.innerHTML=hits.slice(0,25).map(function(x){return '<li><small>Volume '+x.v+' · Question '+x.n+'</small><a href="'+x.u+'">'+esc(x.t)+'</a><p>'+esc(x.s)+'</p></li>'}).join('');}
inp.addEventListener('input',function(){load(run)});inp.addEventListener('focus',function(){load(function(){})});})();</script>'''
assert 'id="rq-q"' not in q
q=q.replace('<section class="detail-section soft"><div class="wrap"><div class="eyebrow">THE VOLUMES</div>',box+'<section class="detail-section soft"><div class="wrap"><div class="eyebrow">THE VOLUMES</div>',1)
assert 'SEARCH THE QUESTIONS' in q
q=q.replace('</head>',css+'</head>',1)
q=q.replace('</body>',js+'</body>',1)
q=q.replace('Each question has a short answer on its volume page, and the free PDF gives each one in full:','Every question has its own page with the full answer, each volume page has a short answer for each, and the free PDF holds the whole volume:')
q=q.replace('<meta name="description" content="Ten questions in each volume, each answered in full in a free PDF:','<meta name="description" content="Search fifty questions on difficult Bible verses. Each has its own page with the full answer, and every volume is a free PDF:')
open(R+'questions.html','w',encoding='utf-8').write(q)
# sitemap
sm=open(R+'sitemap.xml',encoding='utf-8').read()
new=''.join(f'<url><loc>https://zaymariepress.com/{p}</loc></url>' for v in sorted(pages) for p in pages[v])
anchor='<url><loc>https://zaymariepress.com/reader-questions-05-questions-on-difficult-bible-verses.html</loc></url>'
assert anchor in sm and 'reader-questions-v1-q01' not in sm
sm=sm.replace(anchor,anchor+new,1); open(R+'sitemap.xml','w',encoding='utf-8').write(sm)
print('wired')
