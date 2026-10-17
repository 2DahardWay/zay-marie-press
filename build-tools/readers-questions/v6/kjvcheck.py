import re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import kjvlib
from c1 import ENTRIES as A
from c2 import ENTRIES as B
import rev; rev.apply(A+B)
Q=re.compile('“([^”]+)”')
def pcs(q): return [p.strip(' ,.;:?!') for p in re.split(r'…|\.\.\.',q) if p.strip(' ,.;:?!')]
miss=[];rb=[];n=0
def scan(c,s):
    global n
    for m in Q.finditer(s):
        for p in pcs(m.group(1)):
            n+=1
            if not kjvlib.in_corpus(p): miss.append((c,p))
for e in A+B:
    c=e['title'][:30]
    for k in('answer','means','related'):
        v=e[k]; 
        for s in (v if isinstance(v,list) else [v]): scan(c,s)
    for s in e['stand']+e['other']: scan(c,s)
    for t,x in e['carry']: scan(c,x)
    for r in e['rows']:
        scan(c,r[2])
        for m in Q.finditer(r[2]):
            for p in pcs(m.group(1)):
                for ref in r[1].split(';'):
                    pass
                if not any(kjvlib.in_ref(p,ref.strip()) for ref in r[1].split(';')): rb.append((c,r[1],p))
    for r in e['rtbl']:
        for x in r: scan(c,x)
print(n,'checked',len(miss),'missing',len(rb),'row-outside')
for c,p in miss: print(' MISS',c,'::',p)
for c,r,p in rb: print(' ROW',c,r,'::',p)
