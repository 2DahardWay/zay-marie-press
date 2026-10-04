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
    rep(els,"Apply a repeatable discipline for testing four common readings of the eternal state without transferring any passage to a different audience.","Apply a repeatable discipline: test four common readings of the eternal state against the text, and settle each passage’s audience before drawing anything from it.")
    rep(els,"This study reads the passage as addressed to them.","This study reads the passage as addressed to them. This reading rests on the letter’s own audience markers and setting.")
    rep(els,"This is the Framework of this series: Israel’s Prophecy Program","The reading that follows rests on those audiences: Israel’s Prophecy Program")
    rep(els,"Those statements are the study’s Framework position. The passages above","The Body of Christ does not appear in Revelation’s prophetic scenes. The passages above")
    rep(els,"and the Framework of this series draws the distinction that follows:","and the distinction follows:")
    rep(els,"The Framework distinguishes an earthly calling","This reading distinguishes an earthly calling")
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    for t,l in [('STATED BEFORE ORGANIZED','Stated Before Organized.'),('THE CITY BY ITS MARKERS','The City by Its Markers.'),('WHERE PAUL WRITES THE HOPE','Where Paul Writes the Hope.'),('CONTEXT FIRST','Context First.')]: runin(els,t,l)
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][:2]==['Passage','Wording'] and e['rows'][0][2]=='What it states']
    assert len(ts)==2,ts; els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
    return els
