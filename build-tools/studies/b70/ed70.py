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
    rep(els,"Apply a repeatable discipline for testing four common readings of John 3:5 without carrying the verse to a different audience or borrowing its meaning from another writer.","Apply a repeatable discipline: test four common readings of John 3:5 against the text, and settle its audience before borrowing meaning from another writer.")
    rep(els,"The Framework of this series places the earthly ministry of Jesus, the preaching of the kingdom, and the words He spoke to Israel’s leaders within the Prophecy Program:","The earthly ministry of Jesus, the preaching of the kingdom, and the words He spoke to Israel’s leaders belong to the Prophecy Program:")
    rep(els,"promises of Ezekiel 36 to the house of Israel.","promises of Ezekiel 36 to the house of Israel. This reading rests on the passage’s own audience markers and setting.")
    rep(els,"The framework of this series holds that water baptism is not the same as Spirit baptism into the one Body,","Water baptism is not the same as Spirit baptism into the one Body,")
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    runin(els,'A PERSON AND A GROUP','A Person and a Group.')
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][1]=='Water language']
    assert len(ts)==2,ts; els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
    return els
