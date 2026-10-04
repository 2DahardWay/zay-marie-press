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
    rep(els,"The Framework of this series places the earthly ministry of Jesus, the preaching of the kingdom, and the promises made to David’s house within the Prophecy Program:","The earthly ministry of Jesus, the preaching of the kingdom, and the promises made to David’s house belong to the Prophecy Program:")
    rep(els,"compare what you find with the study’s framework —","compare what you find with the study’s controlling questions —")
    runin(els,'A PROMISE THAT NAMES A LINE','A Promise That Names a Line.')
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][:2]==['Point','Matthew 1']]
    assert len(ts)==2,ts; els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
    return els
