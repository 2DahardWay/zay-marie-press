import sys; sys.path.insert(0,'..')
from base import T,rep,find
from clean import mk
def runin(els,title,lead):
    n=[k for k,e in enumerate(els) if e['type']=='para' and e['kind']=='ctitle' and T(e)==title][0]
    body=els[n+1]; els[n:n+2]=[mk('body',[[lead,True,False],[' '+T(body),False,False]])]
def apply(els):
    i=find(els,"This study gives you a repeatable method")
    els[i]['segs']=[["By the end of this study, you should be able to:",False,False]]
    els.pop(find(els,"Each point is a skill you will practice"))
    rep(els,"Apply a repeatable discipline for testing four common readings of the verse, and for receiving Scripture’s report of the Jerusalem church without transferring its assignment.","Apply a repeatable discipline: test four common readings of the verse against the text, and settle to whom the Jerusalem report was addressed before drawing anything from it.")
    rep(els,"The framework of this series distinguishes two programs operating concurrently through the book of Acts. Israel’s","Acts shows two commissions operating concurrently. Israel’s")
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    runin(els,'SETTING BEFORE VERSE','Setting Before Verse.')
    runin(els,'THE WORD IN ITS COMPANY','The Word in Its Company.')
    runin(els,'THE FOUR IN THEIR PLACE','The Four in Their Place.')
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    # merge split table of section 9
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][0]=='Reading']
    assert len(ts)==2
    els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
    return els
