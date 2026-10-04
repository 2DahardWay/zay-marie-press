from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','HEADSHIP CONTROL','EVIDENCE CONTROL','DOCTRINAL BOUNDARY'}
def apply(els):
    assert T(els[1])=='By completing this study, you will be able to:'
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'The controlling Framework identifies the Body’s inheritance with the heavenly places and angelic seats. That identification is the Framework’s doctrinal position','The Body’s inheritance is identified in this study with the heavenly places and angelic seats. That identification is this study’s doctrinal position')
    rep(els,'Israel’s Prophecy Program was suspended at Acts 28, while the Mystery Program continues.','Israel’s Prophecy Program was nationally suspended at Acts 28—not canceled, transferred or absorbed—while the Mystery Program continues.')
    i=find(els,'Nor do they establish that the Body receives Israel’s promised earthly Kingdom administration')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    d=[n for n,e in enumerate(els) if e['type']=='para' and T(e).startswith('First Corinthians 3:8–15 teaches')]
    assert len(d)==2 and T(els[d[0]])==T(els[d[1]]); del els[d[1]]
    import re as _re
    for _k,_e in enumerate(els):
        if P(_e) and _e['kind']=='body' and _re.match(r'^\d+\.[\t ]',T(_e)) and len(T(_e))<120:
            _s=[list(x) for x in _e['segs']]; _s[0][0]=_re.sub(r'^\d+\.[\t ]\s*','',_s[0][0]); els[_k]=mk('num',_s)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
