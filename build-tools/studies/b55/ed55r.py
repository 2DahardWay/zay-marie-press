from edcommon import *
import re
def unb(segs):
    s=[list(x) for x in segs]
    if s[0][0].strip()=='•': s=s[1:]
    else: s[0][0]=re.sub(r'^•\s+','',s[0][0])
    return s
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study' and T(els[7])=='STUDY GOAL'
    # Rule 19 (8.1)
    i=find(els,'The common saving ground is Christ’s work.')
    els[i]['segs']=[['Salvation is always by faith and never by merit, but the content of faith is what God revealed within each program. Study 55 follows Paul’s reconciliation language for the Body and protects the assignment of Israel’s prophetic promises where Scripture places them.',False,False]]
    # Romans 11 standing line
    rep(els,'Standing is not program membership.','Standing is not program membership. Identity is fixed by divine program, not by metaphor.')
    # format: WYWL
    for k in range(1,7):
        assert T(els[k]).startswith('•')
        els[k]=mk('bul',unb(els[k]['segs']))
    els.insert(1,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    a=[k for k,e in enumerate(els) if P(e) and T(e)=='Study Outline'][0]; k=a+1; n=0
    while re.match(r'^\d+\.\t',T(els[k])):
        els[k]=mk('bul',[[re.sub(r'^\d+\.\t','',T(els[k])),False,False]]); k+=1; n+=1
    assert n==8,n
    # Key Distinctions typed bullets
    for k,e in enumerate(els):
        if P(e) and e['kind']=='body' and T(e).startswith('•'): els[k]=mk('bul',unb(e['segs']))
    # Teaching Outline roman -> numbered
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Teaching Outline'][0]; k=ta+1; ng=0
    while els[k]['kind']=='body':
        s=[list(x) for x in els[k]['segs']]; s[0][0]=re.sub(r'^[IVX]+\.\s+','',s[0][0])
        els[k]=mk('bul',s); k+=1; ng+=1
    assert ng==6,ng
    for e in els:
        if P(e):
            t=T(e)
            for bad in ['common saving ground','•','Framework']: assert bad not in t,(bad,t[:90])
    els[:]=[e for e in els if not (P(e) and T(e).strip()=='ZAY-MARIE PRESS DIGITAL STUDIES')]
    import re as _re
    _ra=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Review and Discussion Questions'][0]; _k=_ra+1; _n=0
    while P(els[_k]) and els[_k]['kind']=='body' and _re.match(r'^\d+\.\t',T(els[_k])):
        _s=[list(x) for x in els[_k]['segs']]; _s[0][0]=_re.sub(r'^\d+\.\t','',_s[0][0]); els[_k]=mk('num',_s); _k+=1; _n+=1
    assert _n>=8,_n
    number_outline(els)
    return els
