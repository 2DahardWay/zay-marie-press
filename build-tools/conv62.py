import docx,json,re
from docx.text.paragraph import Paragraph
from docx.table import Table
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}w'
d=docx.Document('c62/fin.docx')
els=[]; started=False; sec=None; tn=0; i=0
def segs(p):
    o=[[r.text,bool(r.bold),bool(r.italic)] for r in p.runs if r.text!='']
    return o or [[p.text,False,False]]
P=lambda k,s: dict(type='para',kind=k,segs=s,p=0,x0=0)
def strip(s,pat):
    s=[x[:] for x in s]; s[0][0]=re.sub(pat,'',s[0][0],count=1); return s
CALL={'STUDY GOAL','SETTING BEFORE SENTENCE','FULFIL ≠ CANCEL','TWO MARKERS, ONE HORIZON','SAME CHRIST, DIFFERENT ASSIGNMENT','PROFIT ≠ JURISDICTION'}
chs=list(d.element.body.iterchildren())
skip=False
for ch in chs:
    tag=ch.tag.split('}')[1]
    if tag=='p':
        p=Paragraph(ch,d); t=p.text.strip(); st=p.style.name
        if skip: skip=False; continue
        if not t: continue
        if not started:
            if st.startswith('Heading') and t=='What You Will Learn in This Study': started=True
            else: continue
        if t.startswith('ZAY-MARIE PRESS DIGITAL STUDIES') or t.startswith('©'): continue
        s=segs(p)
        if st=='Heading 1': sec=t; els.append(P('h1',[[t,False,False]])); continue
        if st=='Heading 2': els.append(P('body',[[t,False,False]])); continue
        if t.split('\n')[0].strip() in CALL:
            a,b=t.split('\n',1); els.append(P('ctitle',[[a.strip(),True,False]])); els.append(P('cbody',[[b.strip(),False,False]])); continue
        if els and els[-1].get('kind')=='ctitle':
            els.append(P('cbody',s)); continue
        if sec=='What You Will Learn in This Study' and re.match(r'^\d+\.\t',p.text): els.append(P('bul',strip(s,r'^\d+\.\s*'))); continue
        if sec=='Teaching Outline' and re.match(r'^[IVX]+\.\s',t):
            tn+=1; x=strip(s,r'^[IVX]+\.\s*'); x[0][0]=f'{tn}. '+x[0][0]; els.append(P('body',x)); continue
        if re.match(r'^\d+\.\t',p.text): els.append(P('num',strip(s,r'^\d+\.\s*'))); continue
        els.append(P('body',s))
    elif tag=='tbl' and started:
        tb=Table(ch,d)
        grid=[int(g.get(W)) for g in tb._tbl.tblGrid]; xs=[];x=0
        for g in grid: xs.append([x,x+g]); x+=g
        xs=[[round(a*640/x),round(b*640/x)] for a,b in xs]
        els.append(dict(type='tbl',rows=[[c.text.strip() for c in r.cells] for r in tb.rows],xs=xs))
# fix: cbody only directly after ctitle; collapse state
out=[];prev=None
for e in els: out.append(e)
els=out
for e in els:
    if e['type']=='para':
        for s in e['segs']: s[0]=s[0].replace("'","’")
    else: e['rows']=[[c.replace("'","’") for c in r] for r in e['rows']]
json.dump(els,open('els62.json','w'),ensure_ascii=False)
for i,e in enumerate(els):
    if e['type']=='tbl': print(i,'TBL',len(e['rows']),e['xs']); continue
    if e['kind'] in('h1','ctitle','cbody'): print(i,e['kind'],''.join(s[0] for s in e['segs'])[:50])
