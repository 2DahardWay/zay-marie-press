from base import T,rep,find,app
from clean import mk
XS=[(0,135),(135,435),(435,640)]
def tbl(rows): return dict(type='tbl',rows=[['Verse','KJV text','What to observe']]+rows,xs=XS)
def addt(els,after,lead,rows):
    j=find(els,after); els.insert(j+1,mk('body',[[lead,False,False]])); els.insert(j+2,tbl(rows))
def apply(els):
    i=find(els,"This study gives you a repeatable method"); els[i]['segs']=[["By the end of this study, you should be able to:",False,False]]
    els.pop(find(els,"Each point is a skill you will practice"))
    rep(els,"and the assignment markers in Matthew 4:17–5:2","and the audience markers in Matthew 4:17–5:2")
    # callout -> run-in (Setting Before Sentence)
    n=[k for k,e in enumerate(els) if e['type']=='para' and e['kind']=='ctitle' and T(e)=='SETTING BEFORE SENTENCE'][0]
    body=els[n+1]; els[n:n+2]=[mk('body',[["Setting Before Sentence.",True,False],[' '+T(body),False,False]])]
    rep(els,"compare what you find with the study’s controlling framework —","compare what you find with the study’s controlling questions —")
    rep(els,"Paul is not speaking of the Law’s existence but of its separating function between Jew and Gentile in the one new man.","Paul speaks of what is abolished for the Body: not the Law’s existence, but its separating function between Jew and Gentile in the one new man. Brought near is not made Israel. This reading of Romans 6:14, Galatians 3:24–25 and Ephesians 2:15 rests on the passages’ own audience markers and setting.")
    app(els,"Notice what this does and does not establish","This reading of Romans 15:8 and Galatians 4:4 rests on the passages’ own audience markers and setting.")
    app(els,"Entrance into the kingdom belongs to the Gospel of the Kingdom","This reading of Romans 3:21–22 and 10:4 rests on the passages’ own audience markers and setting.")
    k=[n for n,e in enumerate(els) if e['type']=='para' and e['kind']=='cbody' and T(e).startswith("“All scripture is given by inspiration")][0]
    els[k]['segs'].append([" This reading of 2 Timothy 3:16 rests on the letter’s own audience markers and setting.",False,False])
    addt(els,"Verse 17 opens with a correction of an assumption","The table sets out Matthew 5:17–20 in KJV wording. Observe the two verbs of verse 17, the two limits in verse 18, and the two places named in verses 19 and 20.",[
     ["Matt. 5:17","“Think not that I am come to destroy the law, or the prophets: I am not come to destroy, but to fulfil.”","The two verbs set against each other; what they are said of."],
     ["Matt. 5:18","“For verily I say unto you, Till heaven and earth pass, one jot or one tittle shall in no wise pass from the law, till all be fulfilled.”","The two “till” clauses; what is said not to pass."],
     ["Matt. 5:19","“Whosoever therefore shall break one of these least commandments, and shall teach men so, he shall be called the least in the kingdom of heaven: but whosoever shall do and teach them, the same shall be called great in the kingdom of heaven.”","The word “therefore”; where the least and the great are placed."],
     ["Matt. 5:20","“For I say unto you, That except your righteousness shall exceed the righteousness of the scribes and Pharisees, ye shall in no case enter into the kingdom of heaven.”","The comparison drawn; what is said of entering."]])
    addt(els,"Some readers set verse 18 against Luke 16:16","The table sets out Luke 16:16–17 and Matthew 24:34–35 in KJV wording. Observe what each verse says passes, what does not, and which verse follows the statement about John.",[
     ["Luke 16:16","“The law and the prophets were until John: since that time the kingdom of God is preached, and every man presseth into it.”","What is said to have been until John; what is preached since."],
     ["Luke 16:17","“And it is easier for heaven and earth to pass, than one tittle of the law to fail.”","What is easier; what is said not to fail."],
     ["Matt. 24:34–35","“Verily I say unto you, This generation shall not pass, till all these things be fulfilled. Heaven and earth shall pass away, but my words shall not pass away.”","The “till” clause; what passes and what does not."]])
    addt(els,"Set the Lord’s words in Matthew 5:18 beside three statements","The table sets out the three statements of Paul in KJV wording. Observe who is addressed in each, and what each says the Body is or is not under.",[
     ["Rom. 6:14","“For sin shall not have dominion over you: for ye are not under the law, but under grace.”","The reason given; what the readers are said not to be under."],
     ["Gal. 3:24–25","“Wherefore the law was our schoolmaster to bring us unto Christ, that we might be justified by faith. But after that faith is come, we are no longer under a schoolmaster.”","The purpose stated; the time marker “after that faith is come.”"],
     ["Eph. 2:15","“Having abolished in his flesh the enmity, even the law of commandments contained in ordinances; for to make in himself of twain one new man, so making peace;”","What is abolished; the purpose stated; the phrase “of twain one new man.”"]])
    return els
