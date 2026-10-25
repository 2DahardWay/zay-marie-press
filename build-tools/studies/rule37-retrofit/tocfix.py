import re,sys,docx,pdfplumber
sys.path.insert(0,'.')
import toclib
def _tp(d):
    out=[];on=False
    for p in d.paragraphs:
        if p.style.name.startswith('Heading'):
            if on: break
            if p.text.strip().startswith('Table of Contents'): on=True
            continue
        if on and '\t' in p.text: out.append(p)
    return out
toclib.toc_paras=_tp
from retro import render
def norm(s): return re.sub(r'[^a-z0-9]+','',s.lower())
def heads_foot(pdf):
    merged=[];foot={}
    with pdfplumber.open(pdf) as P:
        for i,pg in enumerate(P.pages):
            txt=pg.extract_text() or ''
            m=re.search(r'SERIES • (\d+)',txt); foot[i]=int(m.group(1)) if m else None
            lines={}
            for c in pg.chars: lines.setdefault(round(c['top']/3),[]).append(c)
            for k in sorted(lines):
                cs=lines[k]; sz=max(c['size'] for c in cs)
                t=''.join(c['text'] for c in sorted(cs,key=lambda c:c['x0']))
                if sz>=16 and len(t)>2:
                    if merged and merged[-1][0]==i and not re.match(r'^(\d+\.|Table|What|Intro|Concl|Key|Script|Review|Teach|Guided)',t): merged[-1]=(i,merged[-1][1]+' '+t)
                    else: merged.append((i,t))
    return merged,foot
def fix(n):
    f=f'o{n}.docx'
    for it in range(4):
        pdf=render(f,'pdf1'); d=docx.Document(f); tp=toclib.toc_paras(d)
        merged,foot=heads_foot(pdf); ch=0; miss=[]
        for p in tp:
            t=p.text.split('\t')[0]; k=norm(t)[:20]
            hit=[(i,h) for i,h in merged if norm(h).startswith(k) and i>2]
            if not hit: miss.append(t); continue
            # first big-heading hit after the TOC page (TOC page heading itself excluded by i>2? use page index>TOC)
            i=hit[0][0]
            new=f'{t}\t{foot[i]}'
            if p.text!=new: p.runs[0].text=new; [r._r.getparent().remove(r._r) for r in p.runs[1:]]; ch+=1
        d.save(f)
        if not ch: break
    print(n,'iters',it+1,'missing',miss)
if __name__=='__main__':
    for n in sys.argv[1:]: fix(n)
