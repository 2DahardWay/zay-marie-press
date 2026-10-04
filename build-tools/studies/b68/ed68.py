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
    rep(els,"Apply a repeatable discipline for reading Revelation 20:11–15, and for testing four common readings of the Book of Life without transferring any passage to a different audience.","Apply a repeatable discipline: read Revelation 20:11–15 by its own markers, and test four common readings of the Book of Life without transferring any passage to a different audience.")
    rep(els,"without relabeling the company it names.","without relabeling the company it names. This reading rests on the letter’s own audience markers and setting.")
    rep(els,"is decided.","is decided. The Body of Christ does not appear in Revelation’s prophetic scenes.") if False else None
    rep(els,"does not read the throne as the place where the Body’s standing is decided.","does not read the throne as the place where the Body’s standing is decided. The Body of Christ does not appear in Revelation’s prophetic scenes.")
    rep(els,"and he does not attach a condition to the statement.","and he does not attach a condition to the statement. This reading rests on the letter’s own audience markers and setting.")
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    for t,l in [('REGISTERS BEFORE THE BOOK','Registers Before the Book.'),('THE VERB AND ITS SPEAKERS','The Verb and Its Speakers.'),('FOUND WRITTEN','Found Written.'),('THE LAMB’S BOOK','The Lamb’s Book.')]: runin(els,t,l)
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][:2]==['Passage','Setting']]
    assert len(ts)==2,ts; els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
    return els
