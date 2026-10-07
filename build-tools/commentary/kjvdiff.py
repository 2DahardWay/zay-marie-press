import os,sys,glob
R='/tmp/claude-0/-home-claude/d70938a1-c1e3-53dc-bc4c-599e8ff01633/scratchpad/kjv'
def load(p):
    d={}
    if not os.path.exists(p): return None
    for ln in open(p,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln.strip(): continue
        if '\t' not in ln: d.setdefault('_bad',[]).append(ln); continue
        n,t=ln.split('\t',1)
        d[n.strip()]=t.strip()
    return d
codes=sorted({os.path.basename(f)[:-4] for s in 'AB' for f in glob.glob(f'{R}/{s}/*.txt')})
for c in codes:
    a=load(f'{R}/A/{c}.txt'); b=load(f'{R}/B/{c}.txt')
    if a is None or b is None:
        print(f'{c}: ONLY {"A" if b is None else "B"} ({len((a or b))} verses)'); continue
    bad=[k for k in ('_bad',) if k in a or k in b]
    ks=set(a)|set(b); ks.discard('_bad')
    diffs=[k for k in sorted(ks,key=lambda x:int(x) if x.isdigit() else 999) if a.get(k)!=b.get(k)]
    print(f'{c}: A={len(a)} B={len(b)} diffs={len(diffs)} {"BADLINES" if bad else ""}')
    for k in diffs[:6]:
        print('   v',k); print('     A:',(a.get(k) or '')[:160]); print('     B:',(b.get(k) or '')[:160])
