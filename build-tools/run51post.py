import sys,re
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=Document('conf.docx'); n=0
for p in d.paragraphs:
    if re.match(r'^\d\.\d\s',p.text):
        pPr=p._p.get_or_add_pPr()
        if pPr.find(qn('w:keepNext')) is None: pPr.insert(0,OxmlElement('w:keepNext')); n+=1
d.save('conf.docx'); print('keepNext sub',n)
