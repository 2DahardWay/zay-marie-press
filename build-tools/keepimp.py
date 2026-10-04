import sys,os,docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
d=docx.Document(sys.argv[1]); ps=d.paragraphs
i=max(k for k,p in enumerate(ps) if p.text.strip().startswith(os.environ.get('KEEPFROM','Final Synthesis')))
n=0
for p in ps[i:]:
    pPr=p._p.get_or_add_pPr()
    if pPr.find(qn('w:keepNext')) is None: pPr.insert(0,OxmlElement('w:keepNext')); n+=1
    if p.text.startswith('Copyright'): break
d.save(sys.argv[1]); print('keepNext imprint',n)
