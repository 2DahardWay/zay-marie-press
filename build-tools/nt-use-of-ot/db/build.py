import sys,re,json,html
sys.path.insert(0,'/home/claude/zay-marie-press/build-tools/nt-use-of-ot/db')
from seelinks import see
sys.path.insert(0,'/home/claude/zay-marie-press/build-tools/parables')
import kjvlib
from data2 import R
ROOT='/home/claude/zay-marie-press/'
def verses(refs):
    out=[]
    for b,c,s in refs:
        for seg in s.split(','):
            a,_,z=seg.partition('-'); z=z or a
            for v in range(int(a),int(z)+1): out.append(f"{c}:{v} "+kjvlib.V[(b,c,v)])
    return out
_old={"Matthew 8:16–17","Matthew 11:10","Romans 2:24","Romans 4:3","Romans 10:5","Romans 12:19","Romans 15:9","Hebrews 12:26"}
def _n(t): return re.sub(r'\s+',' ',re.sub(r"[^a-z0-9' ]",' ',t.lower().replace('’',"'"))).strip().split()
def loose(r):
    if not r['typ'].startswith('Quotation') or not r['ot']: return False
    nt=_n(' '.join(x.split(' ',1)[1] for x in verses(r['nt']))); ot=_n(' '.join(x.split(' ',1)[1] for x in verses(r['ot'])))
    O=set(zip(*[ot[k:] for k in range(3)])); return sum(1 for t in zip(*[nt[k:] for k in range(3)]) if t in O)<2
TMAP={'Quotation':'Quotation (direct)','Allusion':'Allusion (lexical)','Typology':'Allusion (typological)','Allegory':'Interpretive Device (Pauline)'}
TYPO={
"Matthew 12:40":("Jonah three days and three nights in the belly of the fish (Jonah 1:17)","The Son of man three days and three nights in the heart of the earth (Matthew 12:40)","\u201cFor as Jonas was … so shall the Son of man be\u201d (Matthew 12:40)."),
"John 3:14\u201315":("The serpent lifted up by Moses in the wilderness (Numbers 21:8\u20139)","The Son of man lifted up (John 3:14\u201315)","\u201cAs Moses lifted up the serpent … even so must the Son of man be lifted up\u201d (John 3:14)."),
"Romans 5:14":("Adam (Genesis 3:6)","\u201cHim that was to come\u201d (Romans 5:14; Jesus Christ is named in 5:15)","\u201cWho is the figure of him that was to come\u201d (Romans 5:14)."),
"1 Corinthians 10:1\u20136":("Israel under the cloud, through the sea, fed with manna and given water from the Rock (Exodus 14:22; 16:4; 17:6)","\u201cUs, upon whom the ends of the world are come\u201d (1 Corinthians 10:11)","\u201cThese things were our examples\u201d (10:6) and \u201cthese things happened unto them for ensamples\u201d (10:11)."),
"Hebrews 7:1\u20133":("Melchisedec, king of Salem and priest of the most high God (Genesis 14:18\u201320)","The Son of God (Hebrews 7:3)","\u201cMade like unto the Son of God\u201d (Hebrews 7:3)."),
"Hebrews 9:23\u201324":("The holy places made with hands (Exodus 25:40)","Heaven itself (Hebrews 9:24)","\u201cThe figures of the true\u201d (Hebrews 9:24)."),
"1 Peter 3:20\u201321":("Noah and the few saved by water (Genesis 7:7)","Baptism (1 Peter 3:21)","\u201cThe like figure whereunto even baptism doth also now save us\u201d (1 Peter 3:21)."),
"Galatians 4:21\u201331":("Hagar and Sarah, the two sons of Abraham (Genesis 21:10)","The two covenants (Galatians 4:24)","\u201cWhich things are an allegory\u201d (Galatians 4:24), the one place the KJV uses the word."),
}
rows=[]
for i,r in enumerate(R,1):
    book=r['nt_label'].rsplit(' ',1)[0]
    rows.append(dict(id=i,nt=r['nt_label'],book=book,ot=r['ot_label'],otb=sorted({b for b,_,_ in r['ot']}),
      typ=TMAP.get(r['typ'],r['typ']),typo=TYPO.get(r['nt_label']),tag={'Marked':'Marked by the text','Shown':'Shown by the context','None':'Not signalled by the text'}[r['tag']],
      fm=r['fm'],note=('' if r['typ'] in ('Typology','Allegory') else r['note']),ntv=verses(r['nt']),otv=verses(r['ot']),
      line=('Acts' if book=='Acts' else 'Paul\'s letters' if book in ('Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians','Philippians','1 Timothy','2 Timothy') else 'Israel line'),loose=loose(r),see=see(r['nt_label'])))
json.dump(rows,open(ROOT+'assets/ot-in-nt-quotations.json','w'),ensure_ascii=False,separators=(',',':'))
src=open(ROOT+'new-testament-use-of-old-testament.html').read()
css=re.search(r'<style>(.*?)</style>',src,re.S).group(1)
EXTRA='''
.hero{padding:34px 0 10px!important;min-height:0!important}.hero h1{font-size:clamp(30px,5vw,46px)!important}
.sbox{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0 10px}.sbox input[type=search]{flex:1 1 280px;min-width:0;padding:13px 14px;font:16px Arial;border-radius:10px;border:1px solid var(--gold);background:#0c1a30;color:#fff}
.flt{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 8px}.flt select{padding:10px;border-radius:8px;border:1px solid rgba(212,175,55,.5);background:#0c1a30;color:#fff;font:15px Arial;max-width:100%}
.uc-see{margin-top:14px;padding-top:12px;border-top:1px solid rgba(212,175,55,.25);font-size:14px;line-height:1.7}.uc-see a{color:var(--gold,#d4af37);text-decoration:underline;text-underline-offset:3px}#count{margin:10px 0 16px;color:#cfd8e6;font-size:15px}#res .uc{margin-bottom:14px}.note2{font-size:14px;color:#cfd8e6;margin:6px 0 0}mark{background:#d4af37;color:#091426;padding:0 2px;border-radius:2px}
.tag.t3{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.35);color:#e6edf7}.tip{background:rgba(212,175,55,.1);border:1px solid rgba(212,175,55,.4);border-radius:10px;padding:12px 14px;font-size:15px;margin:10px 0}
'''
TITLE="Search the New Testament’s Use of the Old Testament"
DESC="A free searchable list of places where New Testament writers quote, allude to, or mark a type or allegory from the Old Testament, with both KJV texts, the introducing words and what the text itself marks. Pilot: Matthew, Romans and Hebrews."
BOOKS=[]
for x in rows:
    if x['book'] not in BOOKS: BOOKS.append(x['book'])
ORDER=['Matthew','Mark','Luke','John','Acts','Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians','Philippians','Philippians','1 Timothy','2 Timothy','Hebrews','James','1 Peter','2 Peter','Revelation']
BOOKS=[b for b in ORDER if b in BOOKS]
head=f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>{TITLE}</title><meta name="description" content="{html.escape(DESC)}"/><link rel="canonical" href="https://zaymariepress.com/ot-in-nt-quotations.html"/><link rel="icon" href="assets/zay-marie-press-favicon.png" type="image/png"/><style>{css}{EXTRA}</style></head>'
body='''<body><header class="top"><div class="wrap nav"><a class="brand" href="resources.html">Zay-Marie Press</a><nav class="navlinks"><a href="new-testament-use-of-old-testament.html">Read the survey guide</a></nav><a class="closex" href="resources.html" aria-label="Close and return to Resources" title="Close and return to Resources">✕</a></div></header><main>
<section class="hero"><div class="wrap"><p class="eyebrow">FREE RESOURCE · SEARCH</p><h1>Search the New Testament’s Use of the Old Testament</h1><p class="lead">Type a New Testament verse, an Old Testament verse, a book, or a word. Each result shows both texts in the KJV, the words that introduce the quotation, and what the text itself marks.</p><p class="note2">Edition 1: <span id="n">0</span> uses classified under eight kinds, across the New Testament. More books will be added. This is a lookup, not a ruling on any passage; the companion <a href="new-testament-use-of-old-testament.html">survey guide</a> gives the wider background.</p></div></section>
<section><div class="wrap">
<div class="sbox"><input id="q" type="search" placeholder="e.g. Isaiah 7:14, Romans 4, Habakkuk, “it is written”, Psalm 110" aria-label="Search quotations" autofocus/></div>
<div class="flt"><select id="fb" aria-label="New Testament book"><option value="">All books</option>%%BOOKS%%</select><select id="ft" aria-label="Type of use"><option value="">All types</option><option value="Quotation">Quotation (all)</option><option>Quotation (direct)</option><option>Quotation (composite)</option><option value="Allusion">Allusion (all)</option><option>Allusion (lexical)</option><option>Allusion (thematic)</option><option>Allusion (narrative)</option><option>Allusion (typological)</option><option>Echo (verbal resonance)</option><option>Parallel (non-dependent similarity)</option><option>Interpretive Device (Pauline)</option></select><select id="fg" aria-label="Tag"><option value="">All tags</option><option>Marked by the text</option><option>Shown by the context</option><option>Not signalled by the text</option></select></div>
<details class="tip"><summary><b>How each use is classified</b> (open for the definitions)</summary><p><b>Quotation (direct)</b>: the New Testament gives Old Testament words from one source. <b>Quotation (composite)</b>: words from more than one source joined or placed under one introduction. <b>Allusion (lexical)</b>: no quotation, but the wording clearly matches. <b>Allusion (narrative)</b>: the verse points to an Old Testament account or person and says so. <b>Allusion (typological)</b>: an Old Testament type set beside a New Testament antitype in a pattern the New Testament text itself names; each shows the type, the antitype and the justification. <b>Allusion (thematic)</b>: the New Testament text itself signals an Old Testament theme without quoting it. <b>Echo (verbal resonance)</b>: distinctive Old Testament vocabulary too rare to be accidental. <b>Parallel (non-dependent similarity)</b>: the similarity is clear, but the New Testament gives no signal of dependence. <b>Interpretive Device (Pauline)</b>: Galatians 4:21–31 only, where Paul himself says “an allegory”; it is not counted as an allusion or as typology. No other allegorical reading is in the list.</p><p><b>Tags.</b> “Marked by the text” means the verse itself says it is quoting or pointing back (for example “it is written”). “Shown by the context” means no such words appear, but the link is clear from the passage. “Not signalled by the text” is used only for parallels. The tag says how the link is shown, not how to read the verse.</p></details>
<div id="count" aria-live="polite"></div><div id="res"></div></div></section></main>
<button type="button" class="totop" id="totop" aria-label="Back to top" hidden>↑</button><footer class="footer"><strong>© Zay-Marie Press</strong><br/>Free resource · Edition 1 · Passages are listed as written; no position is taken on any of them.</footer>
<script>
(function(){var D=[],q=document.getElementById('q'),fb=document.getElementById('fb'),ft=document.getElementById('ft'),fg=document.getElementById('fg'),res=document.getElementById('res'),cnt=document.getElementById('count');
function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function norm(s){return s.toLowerCase().replace(/[“”"’']/g,'').replace(/\\s+/g,' ').trim()}
var AB={'matt':'matthew','mt':'matthew','rom':'romans','heb':'hebrews','ps':'psalm','psalms':'psalm','isa':'isaiah','gen':'genesis','exod':'exodus','ex':'exodus','lev':'leviticus','deut':'deuteronomy','jer':'jeremiah','hab':'habakkuk','mic':'micah','mal':'malachi','zech':'zechariah','hos':'hosea','prov':'proverbs','hag':'haggai','1 kgs':'1 kings','2 sam':'2 samuel'};
function qn(s){s=norm(s).replace(/\\./g,'').replace(/:/g,':');var w=s.split(' ');if(AB[w[0]])w[0]=AB[w[0]];else if(w.length>1&&AB[w[0]+' '+w[1]]){w.splice(0,2,AB[w[0]+' '+w[1]])}return w.join(' ').replace(/–|—/g,'-')}
function hay(r){return qn(r.nt+' '+r.ot+' '+r.fm+' '+r.note+' '+r.ntv.join(' ')+' '+r.otv.join(' ')+' '+r.typ+' '+r.tag+' '+(r.typo?r.typo.join(' '):'')).replace(/\\s+/g,' ')}
function chap(label){var m=label.match(/^(.*?) (\\d+):/);return m?m[1].toLowerCase()+' '+m[2]:''}
function match(r,t){if(!t)return true;var n=qn(t);var H=r._h;var rg=n.match(/^([1-3]? ?[a-z ]+?) (\\d+):(\\d+) ?(?:-| to ) ?(\\d+)$/);if(rg){var rb=rg[1].trim(),rc=+rg[2],r1=+rg[3],r2=+rg[4];if(r2<r1){var tt=r1;r1=r2;r2=tt}var al=(r.nt+'; '+r.ot).split(/; */);for(var ii=0;ii<al.length;ii++){var xx=qn(al[ii]).match(/^([1-3]? ?[a-z ]+?) (\\d+):(\\d+)(?:-(\\d+))?/);if(xx&&xx[1].trim()===rb&&+xx[2]===rc){var a1=+xx[3],a2=xx[4]?+xx[4]:a1;if(a1<=r2&&a2>=r1)return true}}return false}var isRef=/^([1-3]? ?[a-z ]+?) (\\d+)(?::(\\d+))?$/.test(n);if(!isRef&&H.indexOf(n)>=0)return true;
 var m=n.match(/^([1-3]? ?[a-z ]+?) (\\d+)(?::(\\d+))?$/);if(m){var b=m[1].trim(),c=+m[2],v=m[3]?+m[3]:null;var lab=[r.nt,r.ot];for(var k=0;k<lab.length;k++){var parts=lab[k].toLowerCase().split(/; */);for(var p=0;p<parts.length;p++){var mm=parts[p].match(/^(?:(.*?) )?(\\d+)[:](\\d+)(?:[–-](\\d+))?(?:, (\\d+))?/);}}
  var all=(r.nt+'; '+r.ot).split(/; */);for(var i=0;i<all.length;i++){var x=qn(all[i]);var mx=x.match(/^([1-3]? ?[a-z ]+?) (\\d+):(\\d+)(?:-(\\d+))?/);if(mx&&mx[1].trim()===b&&+mx[2]===c){if(v===null)return true;var a=+mx[3],z=mx[4]?+mx[4]:a;if(v>=a&&v<=z)return true}}
  if(!r._fb)return false;var sides=[[r.ntv,r.nt],[r.otv,r.ot]];for(var q2=0;q2<2;q2++){if(qn(sides[q2][1]).indexOf(b)<0)continue;var vv=sides[q2][0];for(var j=0;j<vv.length;j++){var vm=vv[j].match(/^(\\d+):(\\d+)/);if(vm&&+vm[1]===c&&(v===null||+vm[2]===v))return true}}return false}
 var ws=n.split(' ');return ws.every(function(w){return H.indexOf(w)>=0})}
function hl(s,t){return esc(s)}
function card(r){var cls=r.tag.charAt(0)==='M'?'t1':r.tag.charAt(0)==='S'?'t2':'t3';var fm=r.fm;
 function fmt(arr,bold){return arr.map(function(v){var i=v.indexOf(' ');var t=esc(v.slice(i+1));if(bold&&fm){var e=esc(fm);var k=t.indexOf(e);if(k>=0)t=t.replace(e,'<b>'+e+'</b>')}return'<sup>'+v.slice(0,i)+'</sup> '+t}).join(' ')}
 return'<article class="uc"><div class="uc-h"><span class="uc-n">'+r.id+'</span><div><h3>'+esc(r.nt)+' <span class="arrow">←</span> '+esc(r.ot)+'</h3><p class="uc-meta">'+esc(r.line)+' · '+esc(r.typ)+' · <span class="tag '+cls+'">'+esc(r.tag)+'</span></p></div></div>'+(r.typo?'<div class="uc-cols" style="margin-bottom:10px"><div><h4>'+(r.typ.indexOf('Interpretive')===0?'Accounts Paul names':'Old Testament type')+'</h4><p>'+esc(r.typo[0])+'</p></div><div><h4>'+(r.typ.indexOf('Interpretive')===0?'What he says they are':'New Testament antitype')+'</h4><p>'+esc(r.typo[1])+'</p></div></div><p class="uc-p"><b>'+(r.typ.indexOf('Interpretive')===0?'Marked by Paul':'Canonical justification')+'.</b> '+esc(r.typo[2])+'</p>':'')+(r.note?'<p class="uc-p">'+esc(r.note)+'</p>':'')+(r.loose&&r.note.indexOf('differs')<0?'<p class="uc-p"><i>The New Testament wording differs from the KJV Old Testament wording here; both are given as written.</i></p>':'')+'<div class="uc-cols"><div><h4>New Testament (KJV)</h4><p>'+fmt(r.ntv,true)+'</p></div><div><h4>Old Testament (KJV)</h4><p>'+(r.otv.length?fmt(r.otv,false):'<i>The source is given as named in the New Testament verse; no Old Testament text is shown.</i>')+'</p></div></div>'+(r.see&&r.see.length?'<p class="uc-p uc-see"><b>Read more on this passage:</b> '+r.see.map(function(x){return'<a href="'+x[1]+'">'+esc(x[0])+'</a>'}).join(' · ')+'</p>':'')+'</article>'}
function run(){var t=q.value;var out=D.filter(function(r){return(!fb.value||r.book===fb.value)&&(!ft.value||r.typ.indexOf(ft.value)===0)&&(!fg.value||r.tag===fg.value)&&match(r,t)});
 cnt.textContent=out.length+' of '+D.length+' uses shown';res.innerHTML=out.length?out.map(card).join(''):'<p>No match in this edition. Try a book name, a chapter (for example “Isaiah 53”), or a word from the verse.</p>'}
fetch('assets/ot-in-nt-quotations.json').then(function(r){return r.json()}).then(function(d){D=d;D.forEach(function(r){r._h=hay(r);r._fb=(r.nt+'; '+r.ot).split(/; */).some(function(x){return !/^[1-3]? ?[A-Za-z ]+? \\d+:\\d+(?:[–-]\\d+)?$/.test(x.trim())})});document.getElementById('n').textContent=D.length;run()});
[q,fb,ft,fg].forEach(function(e){e.addEventListener('input',run);e.addEventListener('change',run)});
var b=document.getElementById('totop');function y(){return window.pageYOffset||document.documentElement.scrollTop||0}addEventListener('scroll',function(){b.hidden=y()<=innerHeight*1.5},{passive:true});b.addEventListener('click',function(){var s=y();window.scrollTo({top:0,behavior:'smooth'});setTimeout(function(){if(y()>0&&y()>=s-2)window.scrollTo({top:0,behavior:'instant'})},400)})})();
</script></body></html>'''
open(ROOT+'ot-in-nt-quotations.html','w').write((head+body).replace('%%BOOKS%%',''.join('<option>'+b+'</option>' for b in BOOKS)))
print(len(rows),'rows')
