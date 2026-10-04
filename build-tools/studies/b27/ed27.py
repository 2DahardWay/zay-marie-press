from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','PENTECOST CONTROL','EVIDENCE CONTROL','NON-TRANSFER PRINCIPLE'}
HEB="This reading rests on the letter’s own audience markers and on the covenant it quotes (Jeremiah 31:31–34), which belongs to the house of Israel and the house of Judah, the Body benefiting from Christ’s blood without being the covenant party."
def apply(els):
    assert T(els[1])=='By completing this study, you will be able to:'
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'what contradicts the revealed framework','what contradicts what Scripture has revealed')
    rep(els,'until Prophecy is suspended at Acts 28.','until Israel’s Prophecy Program was nationally suspended at Acts 28—not canceled, transferred or absorbed.')
    i=find(els,'Pentecost therefore belongs to Israel’s Prophecy Program')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    i=find(els,'Hebrews’ discussion does not erase')
    ins_after_idx(els,i,HEB)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
