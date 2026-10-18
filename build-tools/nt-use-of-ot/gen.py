import sys,re,html
sys.path.insert(0,'/home/claude/zay-marie-press/build-tools/parables')
import kjvlib
from rows import R
def verses(refs):
    out=[]
    for b,c,vs in refs:
        for seg in vs.split(','):
            a,_,z=seg.partition('-'); z=z or a
            for v in range(int(a),int(z)+1):
                out.append((c,v,kjvlib.V[(b,c,v)]))
    return out
def fmt(refs,bolds):
    res=[]
    for c,v,t in verses(refs):
        t=html.escape(t)
        for p in bolds:
            pe=html.escape(p)
            if pe in t: t=t.replace(pe,'<b>'+pe+'</b>',1)
        res.append(f'<sup>{c}:{v}</sup> {t}')
    return ' '.join(res)
tagcls={'Marked':'t1','Shown by the context':'t2'}
tabrows='';cards=''
for i,(nl,ol,ty,tg,pu,nr,orf,bd) in enumerate(R,1):
    tabrows+=f'<tr><td>{i}</td><td>{html.escape(nl)}</td><td>{html.escape(ol)}</td><td>{html.escape(ty)}</td><td><span class="tag {tagcls[tg]}">{"Marked by the text" if tg=="Marked" else tg}</span></td></tr>'
    line='Israel line' if i<=15 else "Paul's letters"
    nb=[b for b in bd]
    cards+=f'''<article class="uc" id="row-{i}"><div class="uc-h"><span class="uc-n">{i}</span><div><h3>{html.escape(nl)} <span class="arrow">←</span> {html.escape(ol)}</h3><p class="uc-meta">{line} · {html.escape(ty)} · <span class="tag {tagcls[tg]}">{"Marked by the text" if tg=="Marked" else tg}</span></p></div></div><p class="uc-p">{html.escape(pu)}</p><div class="uc-cols"><div><h4>New Testament (KJV)</h4><p>{fmt(nr,bd)}</p></div><div><h4>Old Testament (KJV)</h4><p>{fmt(orf,[])}</p></div></div></article>'''
open('chart_table.html','w').write(tabrows); open('chart_cards.html','w').write(cards)
print(len(R),'rows ok')
