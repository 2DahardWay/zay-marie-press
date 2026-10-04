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
    rep(els,"Apply a repeatable discipline for setting the commission beside the commission committed to Paul, so that you can receive what each passage says without transferring an assignment from one to the other.","Apply a repeatable discipline: set the commission beside the commission committed to Paul, and receive what each passage says without transferring an assignment from one to the other.")
    rep(els,"The framework of this series holds that Israel’s Prophecy Program","Israel’s Prophecy Program")
    rep(els,"The framework of this series distinguishes two commissions operating concurrently in the book of Acts.","Acts shows two commissions operating concurrently.")
    rep(els,"the framework’s treatment of Acts 28","the treatment of Acts 28 in section 6.3")
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    runin(els,'SETTING BEFORE COMMAND','Setting Before Command.')
    runin(els,'AUTHORITY BEFORE ASSIGNMENT','Authority Before Assignment.')
    runin(els,'ONE COMMAND','One Command.')
    runin(els,'THE AGE MATTHEW NAMES','The Age Matthew Names.')
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][0]=='Passage' and e['rows'][0][1]=='Wording']
    assert len(ts)==2
    els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
    return els
