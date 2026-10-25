import sys,subprocess,os,docx,copy
sys.path.insert(0,'.')
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn
import toclib
from concl import C
FC=os.path.abspath('../s88b/fc.conf')
def txt(e):
    return ''.join(e.itertext()).strip() if e.tag in (qn('w:p'),qn('w:tbl')) else ''
def style(e):
    s=e.find(qn('w:pPr')+'/'+qn('w:pStyle'))
    return s.get(qn('w:val')) if s is not None else ''
def render(docxp,outdir):
    env=dict(os.environ,FONTCONFIG_FILE=FC)
    subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',outdir,docxp],env=env,capture_output=True)
    return os.path.join(outdir,os.path.basename(docxp).replace('.docx','.pdf'))
def run(n):
    d=docx.Document(f's{n}.docx'); body=d.element.body; kids=list(body)
    h1=lambda e: e.tag==qn('w:p') and style(e)=='Heading1'
    def idx(pred): return next((i for i,e in enumerate(kids) if pred(e)),None)
    ci=idx(lambda e:h1(e) and txt(e).startswith('Conclusion') and not kids.index(e)<30)
    imp=idx(lambda e:e.tag==qn('w:p') and txt(e).startswith('ZAY-MARIE PRESS DIGITAL STUDIES'))
    rm=[]
    # conclusion paragraph + extras
    cp=kids[ci+1]; P=Paragraph(cp,d); r0=P.runs[0]; r0.text=C[n]
    for r in P.runs[1:]: r._r.getparent().remove(r._r)
    if n=='11':
        ft=next(e for e in kids if e.tag==qn('w:tbl') and txt(e).startswith('FINAL CONTROL')); cp.addnext(ft)
    j=ci+2
    while j<len(kids) and not h1(kids[j]):
        t=txt(kids[j])
        if t.startswith(('RIGHT DIVISION','Final control','God is faithful')): rm.append(kids[j])
        if kids[j].tag==qn('w:tbl') and n in('02','03','04') and ('ANSWER IN ONE SENTENCE' in t or 'FINAL CONTROL' in t): rm.append(kids[j])
        j+=1
    if n=='09':
        for i,e in enumerate(kids):
            if h1(e) and txt(e).startswith(('Key Truths to Remember','A Note on the Acts Overlap')):
                k=i
                while True:
                    rm.append(kids[k]); k+=1
                    if h1(kids[k]): break
    # sections
    for i,e in enumerate(kids):
        t=txt(e)
        if h1(e) and t.startswith('Study Summary'):
            k=i; 
            while True:
                rm.append(kids[k]); k+=1
                if h1(kids[k]): break
        if (h1(e) and t.startswith('Final Synthesis')) or (e.tag==qn('w:p') and t.startswith('Final Synthesis — ')):
            k=i
            while k<imp: rm.append(kids[k]); k+=1
    # TOC entries
    for p in d.paragraphs[:40]:
        if p.text.startswith(('Study Summary','Final Synthesis','Key Truths to Remember','A Note on the Acts Overlap')) and '\t' in p.text: rm.append(p._p)
    if n=='11': rm=[e for e in rm if e is not ft]
    if n not in ('02','03','04','11'):
        keep=[e for e in dict.fromkeys(rm) if e.tag==qn('w:tbl') and len(e.findall('.//'+qn('w:tr')))==1]
        for e in reversed(keep): cp.addnext(e)
        rm=[e for e in rm if e not in keep]
        if keep: print(n,'relocated callouts:',[txt(e)[:25] for e in keep])
    for e in set(rm): e.getparent().remove(e)
    ks=list(body); ii=next(i for i,e in enumerate(ks) if e.tag==qn('w:p') and txt(e).startswith('ZAY-MARIE PRESS DIGITAL STUDIES'))
    for e in (ks[ii-1],ks[ii]):
        if e.tag==qn('w:p'): Paragraph(e,d).paragraph_format.keep_with_next=True
    for p in d.paragraphs:
        for r in p.runs:
            if 'Study Summary and Key' in r.text: r.text=r.text.replace('Study Summary and Key','Conclusion and Key')
    out=f'o{n}.docx'; d.save(out)
    # TOC pass x2
    for it in range(3):
        pdf=render(out,'pdf1'); d=docx.Document(out); tp=toclib.toc_paras(d)
        titles=[p.text.split('\t')[0] for p in tp]; res=toclib.compute(pdf,titles); ch=0
        for p,t in zip(tp,titles):
            new=f'{t}\t{res[t]}'
            if p.text!=new: p.runs[0].text=new; [r._r.getparent().remove(r._r) for r in p.runs[1:]]; ch+=1
        d.save(out)
        if not ch: break
    pdf=render(out,'pdf1')
    pages=toclib.pagelines(pdf)
    print(n,'pages',len(pages),'toc missing',[t for t in titles if res[t] is None],'removed',len(set(rm)))
    return pdf
if __name__=='__main__':
    for n in sys.argv[1:]: run(n)
