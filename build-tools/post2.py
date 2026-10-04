import sys
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=Document(sys.argv[1]); ch=list(d.element.body); n=0
def style(p):
    ps=p.find(qn('w:pPr')+'/'+qn('w:pStyle'))
    return ps.get(qn('w:val')) if ps is not None else ''
for i,e in enumerate(ch[:-1]):
    if e.tag!=qn('w:p'): continue
    s=style(e)
    if s.startswith('ListBullet') or s.startswith('ListNumber') or s in('List Bullet','List Number'):
        nx=ch[i+1]
        if nx.tag==qn('w:p') and style(nx)==s: continue
        pPr=e.find(qn('w:pPr')); sp=pPr.find(qn('w:spacing'))
        if sp is None: sp=OxmlElement('w:spacing'); pPr.append(sp)
        if sp.get(qn('w:after')) not in ('120',):
            sp.set(qn('w:after'),'120'); n+=1
d.save(sys.argv[1]); print('list-end spacing set',n)
