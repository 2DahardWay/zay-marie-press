import sys,copy
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=Document(sys.argv[1]); body=d.element.body
numpart=d.part.numbering_part.element
groups=[];cur=[]
for p in d.paragraphs:
    if p.style.name=='List Number': cur.append(p)
    elif p.style.name=='List Bullet 2' and cur: pass
    else:
        if cur: groups.append(cur); cur=[]
if cur: groups.append(cur)
print('groups',[len(g) for g in groups])
# find numId used by style
st=d.styles['List Number'].element
nid=st.find('.//'+qn('w:numId')).get(qn('w:val'))
num=[n for n in numpart.findall(qn('w:num')) if n.get(qn('w:numId'))==nid][0]
abs_id=num.find(qn('w:abstractNumId')).get(qn('w:val'))
mx=max(int(n.get(qn('w:numId'))) for n in numpart.findall(qn('w:num')))
for g in groups[1:]:
    mx+=1
    n=OxmlElement('w:num'); n.set(qn('w:numId'),str(mx))
    a=OxmlElement('w:abstractNumId'); a.set(qn('w:val'),abs_id); n.append(a)
    lo=OxmlElement('w:lvlOverride'); lo.set(qn('w:ilvl'),'0'); so=OxmlElement('w:startOverride'); so.set(qn('w:val'),'1'); lo.append(so); n.append(lo)
    numpart.append(n)
    for p in g:
        pPr=p._p.get_or_add_pPr()
        np_=pPr.find(qn('w:numPr'))
        if np_ is None:
            np_=OxmlElement('w:numPr'); pPr.insert(1,np_)
        for c in list(np_): np_.remove(c)
        il=OxmlElement('w:ilvl'); il.set(qn('w:val'),'0'); ni=OxmlElement('w:numId'); ni.set(qn('w:val'),str(mx)); np_.append(il); np_.append(ni)
d.save(sys.argv[1])
