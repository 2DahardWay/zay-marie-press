from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','SACRIFICIAL LOGIC','THREEFOLD DESCRIPTION','ACTS OVERLAP CONTROL'}
HEB="This reading rests on the letter’s own audience markers and on the covenant it quotes (Jeremiah 31:31–34), which belongs to the house of Israel and the house of Judah, the Body benefiting from Christ’s blood without being the covenant party."
def apply(els):
    assert T(els[1]).startswith('Hebrews 10:26–31 is one of')
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'and the Framework’s ruling on the New Covenant,','and the New Covenant it quotes (Jeremiah 31:31–34),')
    rep(els,'Within the Acts Overlap framework, that urgency','Within the Acts Overlap, that urgency')
    rep(els,'Within the controlling Acts Overlap framework, this fits','Within the Acts Overlap, this fits')
    i=find(els,'The Framework does not assign Hebrews as a book')
    els[i]['segs']=[[HEB,False,False]]
    j=find(els,'Within the Acts Overlap, this fits')
    ins_after_idx(els,j,R17); ins_after_idx(els,j,OVERLAP)
    rep(els,'loss- of-salvation','loss-of-salvation')
    h=find(els,'Audience and Program: Hebrews in Its Covenant Setting')
    els[h]['segs'][0][0]='10. '+els[h]['segs'][0][0]
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
