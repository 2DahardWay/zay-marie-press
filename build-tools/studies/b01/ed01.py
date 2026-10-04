from edcommon import *
import re
KEEP={'STUDY GOAL','CENTRAL QUESTION','REVELATION’S OWN IDENTIFICATION MATTERS','EPHESIANS 5 ESTABLISHES A PROFOUND CHRIST–CHURCH MARRIAGE ANALOGY','ACTS 9–28: TWO PROGRAMS OPERATING CONCURRENTLY'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
SUSP="nationally suspended—not canceled, transferred or absorbed"
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study' and T(els[3]).startswith('By the end of the study')
    els[1:4]=[mk('body',[['By the end of this study, you should be able to:',False,False]])]
    j=2
    while els[j]['kind']=='body' and T(els[j]).startswith('• '):
        els[j]=mk('bul',[[T(els[j])[2:],False,False]]); j+=1
    assert els[j]['kind']=='ctitle' and j==10,j
    a=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Study Outline'][0]+1
    b=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e).startswith('Introduction')][0]
    for k in range(a,b):
        t=T(els[k])
        if re.match(r'^[IVX]+\. ',t): els[k]=mk('bul',[[re.sub(r'^[IVX]+\. ','',t),False,False]])
        elif re.match(r'^[A-Z]\. ',t): els[k]=mk('bul2',[[t[3:],False,False]])
        else: raise Exception(t)
    rep(els,'These programs are related to the same sovereign God and rest ultimately upon the finished work of the same Christ, but they are not interchangeable.','These programs are related to the same sovereign God, but they are not interchangeable.')
    rep(els,'The fact that both groups are redeemed through Christ does not collapse their revealed identities. The finished work of Christ is the ground upon which God accomplishes His purposes, but the content and programmatic application of revelation must still be distinguished.','Salvation is always by faith, never by merit; the content of faith is what God revealed within each program. That both groups are saved by faith does not collapse their revealed identities, and the content and programmatic application of revelation must still be distinguished.')
    rep(els,'At Acts 28, Israel’s Prophecy Program reaches its national judicial suspension point (Acts 28:25–28): national judicial suspension, not abolition and not a transfer.','At Acts 28, Israel’s Prophecy Program was %s (Acts 28:25–28). %s'%(SUSP,BND))
    rep(els,'At Acts 28, Israel’s Prophecy Program reaches national judicial suspension, not abolition and not a transfer, and her promises are not cancelled.','At Acts 28, Israel’s Prophecy Program was %s, and her promises stand.'%SUSP)
    rep(els,'At Acts 28 Israel’s Prophecy Program reaches national judicial suspension, not cancellation, not abolition and not a transfer.','At Acts 28 Israel’s Prophecy Program was %s.'%SUSP)
    rep(els,'Acts 28 is Israel’s national judicial suspension point (not abolition and not a transfer); suspension','At Acts 28 Israel’s Prophecy Program was %s; suspension'%SUSP)
    rep(els,'the national judicial suspension point (not abolition and not a transfer) of Israel’s Prophecy Program within the Acts Overlap.','the national suspension of Israel’s Prophecy Program (%s) within the Acts Overlap.'%SUSP)
    rep(els,'ACTS 28: NATIONAL JUDICIAL SUSPENSION, NOT CANCELLATION','ACTS 28: NATIONALLY SUSPENDED—NOT CANCELED, TRANSFERRED OR ABSORBED')
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
