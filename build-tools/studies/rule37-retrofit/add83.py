import sys,copy,docx
sys.path.insert(0,'.')
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import toclib
from retro import render
d=docx.Document('o83.docx'); b=list(d.element.body)
tpl=b[45]
def mk(title,text):
    t=copy.deepcopy(tpl)
    ts=t.findall('.//'+qn('w:t')); ts[0].text=title; ts[1].text=text
    return t
def hd(i,s): 
    assert ''.join(b[i].itertext()).startswith(s),(i,''.join(b[i].itertext())[:40])
hd(82,'7. Verses 39'); hd(74,'6. Verses 25'); hd(67,'5. Verses 17')
items=[(82,'THE SETTING PAUL NAMES','Paul names three settings for his advice in verses 25–38: “the present distress” (7:26), “the time is short” (7:29) and “the fashion of this world passeth away” (7:31). The chapter states these phrases and does not define “the present distress” beyond them.'),
 (74,'THE SAME RULE, THREE TIMES','Paul states the rule three times in verses 17–24: “so let him walk. And so ordain I in all churches” (7:17), “Let every man abide in the same calling wherein he was called” (7:20) and “Brethren, let every man, wherein he is called, therein abide with God” (7:24). Each statement stands beside his examples of circumcision, uncircumcision and servitude.'),
 (67,'WHOSE WORD PAUL SAYS IT IS','Three times in verses 1–16 Paul marks the source of his words: “I speak this by permission, and not of commandment” (7:6), “I command, yet not I, but the Lord” (7:10) and “speak I, not the Lord” (7:12). Each is Paul’s own statement about his words. In verse 25 he marks a fourth: “I have no commandment of the Lord: yet I give my judgment.”')]
for i,ti,tx in items:
    prev=b[i-1]
    assert prev.tag==qn('w:p')
    pPr=prev.find(qn('w:pPr'))
    if pPr is None: pPr=OxmlElement('w:pPr'); prev.insert(0,pPr)
    sp=pPr.find(qn('w:spacing'))
    if sp is None: sp=OxmlElement('w:spacing'); pPr.append(sp)
    sp.set(qn('w:after'),'200')
    b[i].addprevious(mk(ti,tx))
d.save('o83.docx')
for it in range(3):
    pdf=render('o83.docx','pdf1'); d=docx.Document('o83.docx'); tp=toclib.toc_paras(d)
    titles=[p.text.split('\t')[0] for p in tp]; res=toclib.compute(pdf,titles); ch=0
    for p,t in zip(tp,titles):
        new=f'{t}\t{res[t]}'
        if p.text!=new: p.runs[0].text=new; [r._r.getparent().remove(r._r) for r in p.runs[1:]]; ch+=1
    d.save('o83.docx')
    if not ch: break
pdf=render('o83.docx','pdf1'); print(len(toclib.pagelines(pdf)),'pages')
