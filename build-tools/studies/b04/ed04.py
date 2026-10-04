from base import *
import re
def setbul(els,start,new):
    i=find(els,start); els[i]['segs']=[[new,False,False]]
def apply(els):
    # drop imprint remnants
    els[:]=[e for e in els if not (e['type']=='para' and (T(e).startswith('ZAY-MARIE PRESS DIGITAL STUDIES') or T(e).startswith('Copyright ©')))]
    # WYWL: remove two intro paragraphs
    assert T(els[1]).startswith('Few distinctions') and T(els[2]).startswith('This study trains')
    del els[1:3]
    setbul(els,'Explain the Body of Christ as a distinct','Trace how Paul describes the Body of Christ through terms such as “head,” “one body” and “one new man” (Eph. 1:22–23; 2:15; Gal. 3:28), noting what each term says about its identity.')
    setbul(els,'Distinguish benefiting from Christ','Read Ephesians 2:12–13 beside Jeremiah 31:31, noting who the covenant recipients are and what being “made nigh by the blood of Christ” does and does not say.')
    setbul(els,'Explain why Acts 28 suspension','Examine Acts 28:25–28 alongside Romans 16:25, marking what the passage changes in Israel’s active program and what it leaves untouched.')
    # Study outline / teaching outline roman -> arabic
    n=0;sec=None
    for e in els:
        if e['type']!='para': continue
        if e['kind']=='h1': sec=T(e); n=0
        if e['kind']=='body' and sec in('Study Outline','Teaching Outline — Explaining the Study to Someone Else') and re.match(r'^[IVX]+\. ',T(e)):
            n+=1; e['segs']=[[f"{n}. "+re.sub(r'^[IVX]+\. ','',T(e)),False,False]]
    # Rule 19
    rep(els,"This distinction does not imply a different saving efficacy in Christ’s blood for Israel and for the Body. The finished work of Christ is fully sufficient; the distinction concerns","Salvation is always by faith, and the content of faith is what God revealed within each program. The distinction examined here concerns")
    # resumption wording
    rep(els,"Within the larger Acts Overlap framework, their fulfillment awaits the appointed resumption of the suspended Prophecy Program. Acts 28 establishes the suspension boundary; the fuller future sequence is established cumulatively from the broader prophetic and Pauline revelation.","Acts 28 establishes the suspension boundary; it does not by itself establish any further sequence, and this study does not reconstruct one.")
    rep(els,"Israel’s Prophecy Program can later resume without becoming the Body.","Israel’s promises remain grounded in God’s faithfulness without becoming the Body’s.")
    # Rule 7 / 17
    i=find(els,"Concurrency must not be confused with merger")
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    app(els,"Israel is a nation with a covenantal and prophetic identity.","The Body is not Israel, and Israel is not the Body.")
    n=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert n==5,n
    return els
