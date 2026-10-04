from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','WARNING CONTROL','IMAGE CONTROL','ASSIGNMENT CONTROL'}
HEB="This reading rests on the letter’s own audience markers and on the covenant it quotes (Jeremiah 31:31–34), which belongs to the house of Israel and the house of Judah, the Body benefiting from Christ’s blood without being the covenant party."
R19A="Salvation is always by faith and never by merit, but the content of faith is what God revealed within each program; that is why a warning addressed to one audience does not become the governing doctrine of the Body of Christ."
R19B="Salvation is always by faith and never by merit, but the content of faith is what God revealed within each program. The Body is saved by believing Pauline revelation, the gospel of the grace of God, through faith alone. The required response of Hebrews’ own audience, such as endurance and holding fast, is never a ground of salvation and never transfers to the Body. The distinction preserves differences in audience, revealed content, covenant relationship, required response, inheritance, and accountability."
def apply(els):
    assert T(els[1])=='By completing this study, you will be able to:'
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'The finished work of Christ remains the only ground of redemption, but common redemption does not make every warning the governing doctrine of the Body of Christ.',R19A)
    i=find(els,'The Framework does not assign Hebrews as a book'); els[i]['segs']=[[HEB,False,False]]
    rep(els,'which the Framework locates in the Mystery,','which belongs to the Mystery,')
    rep(els,'The Acts Overlap framework provides','The Acts Overlap provides')
    i=find(els,'This distinction does not create two grounds of redemption'); els[i]['segs']=[[R19B,False,False]]
    i=find(els,'The Body of Christ belongs to the Mystery revealed through Paul and begins at Acts 9')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
