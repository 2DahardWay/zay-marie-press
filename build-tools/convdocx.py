import docx,json,sys,re
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
src,out=sys.argv[1],sys.argv[2]
d=docx.Document(src)
def segs(p):
    s=[]
    for r in p.runs:
        t=r.text
        if not t: continue
        b=bool(r.bold); i=bool(r.italic)
        if s and s[-1][1]==b and s[-1][2]==i: s[-1][0]+=t
        else: s.append([t,b,i])
    return s
def P(kind,sg): return dict(type='para',kind=kind,segs=sg,p=0,x0=0)
els=[];sec=None
body=d.element.body
for ch in body.iterchildren():
    if ch.tag==qn('w:p'):
        p=Paragraph(ch,d); t=p.text.strip(); st=p.style.name
        if not t: continue
        if st=='Heading 1':
            sec=t
            if t=='Table of Contents': continue
            els.append(P('h1',[[t,False,False]])); continue
        if sec=='Table of Contents': continue
        if st=='Heading 2': els.append(P('sub',[[t,True,False]])); continue
        sg=segs(p)
        if st.startswith('List Bullet'): els.append(P('bul',sg))
        elif st.startswith('List Number'): els.append(P('num',sg))
        else: els.append(P('body',sg))
    elif ch.tag==qn('w:tbl'):
        tb=docx.table.Table(ch,d)
        if len(tb.columns)==1:
            ps=[Paragraph(x,d) for r in tb.rows for x in r.cells[0]._tc.findall(qn('w:p'))]
            ps=[x for x in ps if x.text.strip()]
            els.append(P('ctitle',[[ps[0].text.strip(),True,False]]))
            for x in ps[1:]: els.append(P('cbody',segs(x)))
        else:
            rows=[[c.text.strip() for c in r.cells] for r in tb.rows]
            n=len(rows[0]); xs=[[round(i*640/n),round((i+1)*640/n)] for i in range(n)]
            els.append(dict(type='tbl',rows=rows,xs=xs))
for e in els:
    if e['type']=='para':
        for sg in e['segs']: sg[0]=sg[0].replace("'","’")
json.dump(els,open(out,'w'),ensure_ascii=False)
import collections;print(collections.Counter((x['type'],x.get('kind')) for x in els))
