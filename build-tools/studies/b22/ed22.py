from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','OVERLAP CONTROL','GRACE PRAYER CONTROL','FINAL CONTROL'}
def apply(els):
    assert T(els[1]).startswith('Prayer is one of the most familiar')
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'The Framework assigns John 14 to the Prophecy Program:','John 14 belongs to the Prophecy Program:')
    i=find(els,'Acts 9 introduces Paul’s calling and the beginning of the Mystery Program')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
