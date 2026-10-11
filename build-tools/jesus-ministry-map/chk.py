import re,sys
sys.path.insert(0,'.')
from kjv import get
import stops as S
def parse(ref):
    m=re.match(r'(\d?\s?[A-Za-z]+) (\d+):(\d+)(?:[–-](\d+))?$',ref); b,ch,a,z=m.groups(); return b,int(ch),int(a),int(z or a)
def parse2(ref):
    # allow cross-chapter "Mark 11:20–12:44"
    m=re.match(r'(\d?\s?[A-Za-z]+) (\d+):(\d+)[–-](\d+):(\d+)$',ref)
    if m: b,c1,v1,c2,v2=m.groups(); return [(b,int(c1),int(v1),999),(b,int(c2),1,int(v2))]
    b,ch,a,z=parse(ref); return [(b,ch,a,z)]
def text(ref):
    out=[]
    for b,ch,a,z in parse2(ref):
        out+=[(ch,v,t) for v,t in get(b,ch,a,min(z,200))]
    return out
norm=lambda t:' '.join(re.sub(r'[^a-z0-9 ]','',re.sub(r'[“”‘’"\'—–-]',' ',t.lower())).split())
errs=0
def check(label,refs,texts):
    global errs
    corp=norm(' '.join(t for r in refs for _,_,t in text(r)))
    for r in refs:
        if not text(r): print('MISSING',label,r); errs+=1
    for t in texts:
        for q in re.findall(r'“([^”]+)”',t):
            qn=norm(q)
            if qn and qn not in corp: print('QUOTE?',label,q); errs+=1
for s in S.S: check(s[0],s[7],[s[8]]+s[9])
for d,t,refs,h in S.WEEK: check(t,refs,[h])
print('stops',len(S.S),'errs',errs)
