from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=Document('conf.docx'); ch=list(d.element.body); n=0
for i,e in enumerate(ch[:-1]):
    if e.tag==qn('w:p') and ch[i+1].tag==qn('w:tbl'):
        pPr=e.find(qn('w:pPr'))
        if pPr is None: pPr=OxmlElement('w:pPr'); e.insert(0,pPr)
        if pPr.find(qn('w:keepNext')) is None: pPr.insert(0,OxmlElement('w:keepNext')); n+=1
d.save('conf.docx'); print('keepNext before tables',n)
