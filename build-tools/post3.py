import sys
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=Document(sys.argv[1]); n=0
for p in d.paragraphs:
    if p.text.startswith('Read these key texts first'):
        pPr=p._p.get_or_add_pPr()
        if pPr.find(qn('w:keepNext')) is None: pPr.insert(0,OxmlElement('w:keepNext')); n+=1
d.save(sys.argv[1]); print('keepNext',n)
