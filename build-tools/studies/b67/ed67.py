import sys; sys.path.insert(0,'..')
from base import T,rep,find
from clean import mk
def runin(els,title,lead):
    n=[k for k,e in enumerate(els) if e['type']=='para' and e['kind']=='ctitle' and T(e)==title][0]
    body=els[n+1]; els[n:n+2]=[mk('body',[[lead,True,False],[' '+T(body),False,False]])]
def merge(els,h0):
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][0]==h0]
    assert len(ts)==2,ts
    els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
def apply(els):
    i=find(els,"This study gives you a repeatable method")
    els[i]['segs']=[["By the end of this study, you should be able to:",False,False]]
    els.pop(find(els,"Each point is a skill you will practice"))
    rep(els,"Apply a repeatable discipline for testing four common readings of Melchizedek, and for receiving the priesthood argument of Hebrews without transferring its assignment.","Apply a repeatable discipline: test four common readings of Melchizedek against the text, and settle who the readers are before drawing anything from the priesthood argument of Hebrews.")
    rep(els,"This fits the framework of this series. Israel’s Prophecy Program","This reading rests on the letter’s own audience markers and on the covenant it quotes (Jeremiah 31:31–34), which belongs to the house of Israel and the house of Judah, the Body benefiting from Christ’s blood without being the covenant party. Israel’s Prophecy Program")
    rep(els,"The Melchizedek argument of Hebrews belongs with the first.","The Melchizedek argument of Hebrews is read here within the first.")
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    for t,l in [('SETTING BEFORE TITLE','Setting Before Title.'),('TWO TITLES, ONE OFFICE','Two Titles, One Office.'),('STATED, NOT SUPPLIED','Stated, Not Supplied.'),('THE READERS FIRST','The Readers First.')]: runin(els,t,l)
    nc=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert nc==5,nc
    merge(els,'Name or title'); 
    ts=[k for k,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][0]=='Passage']
    assert len(ts)==2; els[ts[0]]['rows']+=els[ts[1]]['rows'][1:]; els.pop(ts[1])
    return els
