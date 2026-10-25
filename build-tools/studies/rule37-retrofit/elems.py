import docx,sys
from docx.oxml.ns import qn
def elems(d):
    out=[]
    for e in d.element.body:
        tag=e.tag.split('}')[1]
        if tag=='p':
            from docx.text.paragraph import Paragraph
            p=Paragraph(e,d)
            out.append((e,'p',p.style.name,p.text.strip()))
        elif tag=='tbl':
            t=''.join(e.itertext())[:60]
            out.append((e,'tbl','',t))
        else: out.append((e,tag,'',''))
    return out
if __name__=='__main__':
    d=docx.Document(sys.argv[1]); a=int(sys.argv[2]) if len(sys.argv)>2 else 0
    names=sys.argv[3] if len(sys.argv)>3 else ''
    es=elems(d)
    start=next((i for i,x in enumerate(es) if x[3].startswith(names)  and x[2]=='Heading 1'),0) if names else 0
    for i,x in enumerate(es[start:],start):
        has_pb = 'w:br w:type="page"' in x[0].xml or 'pageBreakBefore' in x[0].xml
        print(i,x[1],x[2],repr(x[3][:70]),'PB' if has_pb else '', 'SECT' if 'sectPr' in x[0].xml and x[1]=='p' else '')
