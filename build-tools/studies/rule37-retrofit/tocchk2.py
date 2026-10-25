import re,sys,pdfplumber
def norm(s): return re.sub(r'[^a-z0-9]+','',s.lower())
def run(pdf):
    heads=[];foot={};toc=[]
    with pdfplumber.open(pdf) as P:
        for i,pg in enumerate(P.pages):
            txt=pg.extract_text() or ''
            m=re.search(r'SERIES • (\d+)',txt); foot[i]=int(m.group(1)) if m else None
            # lines by top with size
            lines={}
            for c in pg.chars:
                lines.setdefault(round(c['top']/3),[]).append(c)
            for k in sorted(lines):
                cs=lines[k]; sz=max(c['size'] for c in cs)
                t=''.join(c['text'] for c in sorted(cs,key=lambda c:c['x0']))
                if sz>=16 and len(t)>2: heads.append((i,t))
                if '....' in t and sz<12 and i<4: toc.append(t)
    # merge consecutive wrapped heading lines on same page
    merged=[]
    for i,t in heads:
        if merged and merged[-1][0]==i and not re.match(r'^(\d+\.|Table|What|Intro|Concl|Key|Script|Review|Teach|Guided)',t): merged[-1]=(i,merged[-1][1]+' '+t)
        else: merged.append((i,t))
    ent=[(re.sub(r'\s*\.{3,}\s*\d+$','',t),int(re.search(r'(\d+)$',t).group(1))) for t in toc if re.search(r'\d$',t)]
    bad=[]
    for t,n in ent:
        k=norm(t)[:20]
        hit=[(i,h) for i,h in merged if norm(h).startswith(k)]
        if not hit: bad.append((t,n,'nohead')); continue
        i=hit[-1][0] if len(hit)>1 else hit[0][0]
        if foot[i]!=n: bad.append((t,n,foot[i]))
    return len(ent),bad
for n in sys.argv[1:]:
    c,b=run(f'pdf1/o{n}.pdf'); print(n,c,len(b),b[:3])
