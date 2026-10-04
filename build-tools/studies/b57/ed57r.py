from edcommon import *
import re
def unb(segs):
    s=[list(x) for x in segs]
    if s[0][0].strip()=='•': s=s[1:]
    else: s[0][0]=re.sub(r'^•\s+','',s[0][0])
    return s
def rm_num(segs,pat):
    s=[list(x) for x in segs]
    if re.fullmatch(pat+r'\t',s[0][0]): s=s[1:]
    else: s[0][0]=re.sub(r'^'+pat+r'\s+','',s[0][0])
    return s
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study' and T(els[7])=='STUDY GOAL'
    for k in range(1,7):
        assert T(els[k]).startswith('•'); els[k]=mk('bul',unb(els[k]['segs']))
    els.insert(1,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    a=[k for k,e in enumerate(els) if P(e) and T(e)=='Study Outline'][0]; k=a+1; n=0
    while re.match(r'^\d+\.\t',T(els[k])):
        els[k]=mk('bul',rm_num(els[k]['segs'],r'\d+\.')); k+=1; n+=1
    assert n==6,n
    for k,e in enumerate(els):
        if P(e) and e['kind']=='body' and T(e).startswith('•'): els[k]=mk('bul',unb(e['segs']))
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Teaching Outline'][0]; k=ta+1; ng=0
    while els[k]['kind']=='body' and re.match(r'^[IVX]+\.',T(els[k])):
        els[k]=mk('bul',rm_num(els[k]['segs'],r'[IVX]+\.')); k+=1; ng+=1
    assert ng==7,ng
    els[:]=[e for e in els if not (P(e) and T(e).strip()=='ZAY-MARIE PRESS DIGITAL STUDIES')]
    for e in els:
        if P(e):
            assert '•' not in T(e)
    number_outline(els)
    return els
