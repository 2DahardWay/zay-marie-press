"""Build-time only: for each use, find up to three studies / commentary volumes / parable studies that argue the NT passage (from the Fit Check Map data)."""
import json,sys,glob
FC='/home/claude/zay-marie-press/build-tools/fit-check/'
sys.path.insert(0,FC)
import bibleref as B
D=FC+'data/'
reg={r['id']:r for r in json.load(open(D+'registry.json'))}
cov=json.load(open(D+'coverage.json'))
pdf=[]
for f in sorted(glob.glob(D+'coverage_pdf_*.json')): pdf+=json.load(open(f))
items={c['item'] for c in pdf}
cov=[c for c in cov if c['item'] not in items or c['depth']=='book']+pdf
OK={'Digital Study','Commentary Volume','Parable Study'}
tot={}
for c in cov:
    if c['depth']=='argued': tot[(c['item'],c['book'])]=tot.get((c['item'],c['book']),0)+c['hi']-c['lo']+1
import re,os
ROOT='/home/claude/zay-marie-press/'
_cards={}
def cards(slug):
    if slug not in _cards:
        out=[]
        p=ROOT+slug
        if os.path.exists(p):
            t=open(p,encoding='utf-8').read()
            for m in re.finditer(r'<div class="scripture-card" id="([^"]+)"><h3>(.*?)</h3>',t):
                iv=[x for ref in B.find_refs(re.sub(r'<[^>]+>','',m.group(2)).replace('&amp;','&')) for x in ref[1]]
                out.append((m.group(1),iv))
        _cards[slug]=out
    return _cards[slug]
def anchor(slug,nt_ivs):
    best=None;bo=0
    for cid,iv in cards(slug):
        ov=0
        for c1,l1,h1 in iv:
            for c2,l2,h2 in nt_ivs:
                if c1==c2 and l1<=h2 and l2<=h1: ov+=min(h1,h2)-max(l1,l2)+1
        if ov>bo: bo=ov;best=cid
    return best
def label(i):
    r=reg[i];t=r['type']
    if t=='Digital Study': return 'Study %d: %s'%(r['n'],r['title'])
    if t=='Parable Study': return 'Parable Study: '+r['title']
    return '%s, Volume %s: %s'%(r['series'],r.get('n',''),r['title'])
def see(nt_label,maxspan=30):
    """Only coverage rows that name the verses themselves (a span of at most maxspan verses), never whole-chapter coverage."""
    iv=[x for ref in B.find_refs(nt_label) for x in ref[1]]
    L=sum(h-l+1 for _,l,h in iv) or 1
    sc={}
    for code,lo,hi in iv:
        for c in cov:
            if c['book']==code and c['depth'] in ('argued','reported') and c['hi']-c['lo']<=maxspan and c['lo']<=hi and lo<=c['hi'] and reg.get(c['item'],{}).get('type') in OK:
                ov=min(hi,c['hi'])-max(lo,c['lo'])+1
                k=sc.setdefault(c['item'],[0,0]);k[0]=max(k[0],ov);k[1]+=c.get('mentions',1)
    out=[(k,v) for k,v in sc.items() if v[0]/L>=.5]
    out.sort(key=lambda x:(-x[1][0],-x[1][1]))
    res=[]
    for k,_ in out[:3]:
        sl=reg[k]['slug']
        res.append([label(k),sl])
    return res
