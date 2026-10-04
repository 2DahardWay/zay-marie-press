import sys; sys.path.insert(0,'..')
from base import T,rep,find
from clean import mk
def apply(els):
    # What You Will Learn: one lead-in line, bullets only, closing paragraph removed
    i=find(els,"This study gives you a repeatable method")
    els[i]['segs']=[["By the end of this study, you should be able to:",False,False]]
    els.pop(find(els,"Each point is a skill you will practice"))
    rep(els,"and for receiving what belongs to Israel’s prophecy without transferring its assignment.","and for settling to whom the sign was addressed and what may be drawn from it for the Body.")
    # reader-facing wording
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    # callout -> run-in (extra beyond five)
    n=[k for k,e in enumerate(els) if e['type']=='para' and e['kind']=='ctitle' and T(e)=='WORD EVIDENCE, NOT WORD ALONE'][0]
    body=els[n+1]; els[n:n+2]=[mk('body',[["Word Evidence, Not Word Alone.",True,False],[' '+T(body),False,False]])]
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    return els
