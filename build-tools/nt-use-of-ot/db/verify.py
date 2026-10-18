import sys,re
sys.path.insert(0,'/home/claude/zay-marie-press/build-tools/parables')
import kjvlib
from data2 import R
def vs(refs):
    out=[]
    for b,c,s in refs:
        for seg in s.split(','):
            a,_,z=seg.partition('-'); z=z or a
            for v in range(int(a),int(z)+1):
                k=(b,c,v)
                if k not in kjvlib.V: raise KeyError(k)
                out.append((c,v,kjvlib.V[k]))
    return out
def norm(s): return re.sub(r'\s+',' ',re.sub(r"[^a-z0-9' ]",' ',s.lower().replace('’',"'"))).strip()
bad=0
for i,r in enumerate(R,1):
    try:
        nt=' '.join(t for _,_,t in vs(r['nt'])); ot=' '.join(t for _,_,t in vs(r['ot'])) if r['ot'] else ''
    except KeyError as e: print(i,r['nt_label'],'MISSING',e); bad+=1; continue
    if r['fm'] and norm(r['fm']) not in norm(nt): print(i,r['nt_label'],'FORMULA NOT FOUND:',r['fm']); bad+=1
    if not ot: continue
    nw=norm(nt).split(); ow=set(zip(*[norm(ot).split()[k:] for k in range(3)]))
    sh=sum(1 for t in zip(*[nw[k:] for k in range(3)]) if t in ow)
    if sh<2: print(i,r['nt_label'],'low overlap',sh,'(loose or composite)')
print(len(R),'rows;',bad,'problems')
