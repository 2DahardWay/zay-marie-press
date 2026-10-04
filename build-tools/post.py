from docx import Document
from docx.oxml.ns import qn
import sys
d=Document(sys.argv[1]); b=d.element.body; ch=list(b)
def setsp(p,key,val):
    pPr=p.find(qn('w:pPr'))
    if pPr is None:
        from docx.oxml import OxmlElement
        pPr=OxmlElement('w:pPr'); p.insert(0,pPr)
    sp=pPr.find(qn('w:spacing'))
    if sp is None:
        from docx.oxml import OxmlElement
        sp=OxmlElement('w:spacing'); pPr.append(sp)
    cur=int(sp.get(qn('w:'+key),'0'))
    if cur<val: sp.set(qn('w:'+key),str(val)); return 1
    return 0
n=0
for i,e in enumerate(ch):
    if e.tag==qn('w:tbl'):
        if i>0 and ch[i-1].tag==qn('w:p'): n+=setsp(ch[i-1],'after',200)
        if i+1<len(ch) and ch[i+1].tag==qn('w:p'): n+=setsp(ch[i+1],'before',200)
d.save(sys.argv[1]); print('adjusted',n)
