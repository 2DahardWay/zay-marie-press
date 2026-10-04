from edcommon import *
KEEP={'STUDY GOAL','WALKING IS NOT TRYING HARDER','THE BODY’S SPIRIT MINISTRY IS NOT MEASURED BY THE SPIRIT’S ACTIVITY RECORDED IN ACTS','THE FRUIT IS SINGULAR','NO CONDEMNATION IS SETTLED STANDING, NOT SINLESS PERFECTION'}
def apply(els):
    # WYWL bullet 6: process wording
    i=find(els,'Why this study is not a study of the believer’s identity')
    els[i]=mk('bul',[['Trace how Romans 8:9–14 and Galatians 5 together describe the Spirit’s ongoing ministry to the Body, noting each verb tense and each “if” clause.',False,False]])
    # Study Outline bulleted
    s=[k for k,e in enumerate(els) if P(e) and e['kind']=='sub' and T(e)=='Study Outline'][0]
    k=s+1
    while els[k]['type']=='para' and els[k]['kind']=='num': els[k]['kind']='bul'; k+=1
    rep(els,'the Body’s Ministry of the Spirit and Israel’s Signs','the Body’s Spirit Ministry and Acts')
    rep(els,'the Body’s Ministry of the Spirit and Israel’s Signs','the Body’s Spirit Ministry and Acts')
    rep(els,'THE BODY’S SPIRIT MINISTRY IS NOT ISRAEL’S ACTS-ERA SIGNS','THE BODY’S SPIRIT MINISTRY IS NOT MEASURED BY THE SPIRIT’S ACTIVITY RECORDED IN ACTS')
    rep(els,'is not Israel’s Acts-era signs, wonders, and repeated fillings (see Study 34 and Study 38)','is not measured by the signs, wonders, and repeated fillings recorded in Acts (see Study 34 and Study 38)')
    rep(els,'why Israel’s Acts-era signs, wonders, and repeated fillings of the Spirit are not the standard','why the signs, wonders, and repeated fillings of the Spirit recorded in Acts are not the standard')
    rep(els,'Whose Ministry This Is (the Body, not Israel’s Acts-era signs)','Whose Ministry This Is (the Body’s, not measured by the activity recorded in Acts)')
    rep(els,'kept distinct from Israel’s Acts-era signs and repeated fillings (Section 2)','kept distinct from the signs and repeated fillings recorded in Acts (Section 2)')
    rep(els,'measured by Acts-era phenomena rather than','measured by the signs and fillings Acts records rather than')
    rep(els,'not by Acts-era phenomena the Mystery Program was never given to reproduce.','not by the signs and repeated fillings Acts records, which Paul never sets before the Body as the measure of its walk.')
    rep(els,'Israel’s Prophecy-setting ministry: signs, wonders, repeated fillings.','The Spirit’s activity recorded in Acts: signs, wonders, repeated fillings.')
    rep(els,'examine that Acts-era pattern in detail','examine the pattern Acts records in detail')
    rep(els,'Compare this with the Acts-era pattern in the next group.','Compare this with the pattern Acts records in the next group.')
    number_outline(els)
    return els
