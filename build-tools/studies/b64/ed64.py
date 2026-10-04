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
    rep(els,"and for receiving Revelation’s imagery without transferring its assignment.","and for settling which scene they belong to and what may be drawn from it for the Body.")
    # reader-facing wording
    rep(els,"from that evidence and from the governing framework of this series: the Bride","from that evidence: the Bride")
    rep(els,"Within this series’ framework, the scene belongs to Israel’s Prophecy Program, and its guests are classified there: they are those","The scene belongs to Revelation’s Prophecy-Program sequence, and its guests are those")
    rep(els,"This classification governs the scene’s setting","This reading governs the scene’s setting")
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    # Body absent from Revelation's prophetic scenes (replaces the neutral stance)
    rep(els,"The wedding and the supper stand in Revelation’s Prophecy-Program sequence, and the Body’s calling","The Body of Christ does not appear in Revelation’s prophetic scenes; the wedding and the supper belong to Israel’s Prophecy Program, and the Body’s calling")
    rep(els," The study neither affirms nor denies the Body’s presence at the supper; it declines to read Paul’s teaching into a scene where Paul is not speaking.","")
    rep(els,"The study does not extend the wife’s identity to the Body, does not place the Body among the called, and does not supply a timetable the text does not give.","The Body of Christ does not appear in Revelation’s prophetic scenes, so the study does not extend the wife’s identity to the Body or place the Body among the called, and it does not supply a timetable the text does not give.")
    # transliteration
    for e in els:
        if e['type']=='para':
            for s in e['segs']:
                if 'kekleimenoi' in s[0]: s[0]=s[0].replace('kekleimenoi','keklēmenoi')
    # callouts: eight -> five
    runin(els,'SETTING BEFORE SCENE','Setting Before Scene.')
    runin(els,'WORD EVIDENCE, NOT WORD ALONE','Word Evidence, Not Word Alone.')
    runin(els,'A SCENE AT THE THRESHOLD','A Scene at the Threshold.')
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    return els
