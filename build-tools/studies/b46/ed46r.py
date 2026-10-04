from edcommon import *
import re
def unb(t): return re.sub(r'^•\s+','',t)
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study' and T(els[10])=='STUDY GOAL'
    for k in range(2,10):
        assert T(els[k]).startswith('•'),k
        els[k]=mk('bul',[[unb(T(els[k])),False,False]])
    els.insert(2,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    a=[k for k,e in enumerate(els) if P(e) and T(e)=='Study Outline'][0]
    assert T(els[a+1]).startswith('This study moves in three stages')
    del els[a+1]
    k=a+1
    while T(els[k]).startswith('•'):
        els[k]=mk('bul',[[unb(T(els[k])),False,False]]); k+=1
    assert els[k]['kind']=='h1'
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e).startswith('Teaching Outline')][0]
    k=ta+1; ng=0
    while els[k]['kind']=='body' and not T(els[k]).startswith('ZAY-MARIE') :
        t=T(els[k])
        if t.startswith('•'): els[k]=mk('bul2',[[unb(t),False,False]])
        else: els[k]=mk('bul',[[t,False,False]]); ng+=1
        k+=1
        if k>=len(els) or els[k]['kind']!='body' or T(els[k]).startswith('ZAY-MARIE') or els[k]['kind']=='h1': break
    assert ng==6,ng
    rep(els,'The believer’s security is anchored, in this text,','The believer’s security rests, in this text,')
    import re as _re
    _ra=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Review and Discussion Questions'][0]; _k=_ra+1; _n=0
    while P(els[_k]) and els[_k]['kind']=='body' and _re.match(r'^\d+\.\t',T(els[_k])):
        _s=[list(x) for x in els[_k]['segs']]; _s[0][0]=_re.sub(r'^\d+\.\t','',_s[0][0]); els[_k]=mk('num',_s); _k+=1; _n+=1
    assert _n>=8,_n
    number_outline(els)
    return els
