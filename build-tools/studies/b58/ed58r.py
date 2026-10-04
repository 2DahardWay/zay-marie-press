import sys; sys.path.insert(0,'..')
from edfix import *
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study'
    for k in range(1,7):
        assert T(els[k]).startswith('•'); els[k]=mk('bul',unb(els[k]['segs']))
    els.insert(1,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    n=study_outline_bullets(els); assert n==7,n
    for k,e in enumerate(els):
        if P(e) and e['kind']=='body' and T(e).startswith('•'): els[k]=mk('bul',unb(e['segs']))
    ra=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Review and Discussion Questions'][0]; k=ra+1; nq=0
    while P(els[k]) and els[k]['kind']=='body' and re.match(r'^\d+\.\t',T(els[k])):
        els[k]=mk('num',rm_num(els[k]['segs'],r'\d+\.')); k+=1; nq+=1
    assert nq==10,nq
    g=teaching_outline_numbered(els,r'[IVX]+\.'); assert g==5,g
    els[:]=[e for e in els if not (P(e) and T(e).strip()=='ZAY-MARIE PRESS DIGITAL STUDIES')]
    assert sum(1 for e in els if P(e) and e['kind']=='ctitle')==5
    for e in els:
        if P(e): assert not re.match(r'^(•|[IVX]+\.\t)',T(e)),T(e)[:40]
    number_outline(els); return els
