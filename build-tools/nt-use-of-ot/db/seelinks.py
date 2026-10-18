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
    return [[label(k),reg[k]['slug']] for k,_ in out[:3]]
