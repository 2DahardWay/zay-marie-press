from base import T,rep,find,app,OVERLAP,R18S
from clean import mk
XS=[(0,135),(135,435),(435,640)]
def tbl(rows): return dict(type='tbl',rows=[['Verse','KJV text','What to observe']]+rows,xs=XS)
def addt(els,after,lead,rows):
    j=find(els,after); els.insert(j+1,mk('body',[[lead,False,False]])); els.insert(j+2,tbl(rows))
BUL=[
"Read Genesis 17:9–14 for what the sign is called, who receives it and what is said of refusing it, and note where Leviticus 12:3 and Joshua 5 take it up.",
"Trace how Deuteronomy 10:16, 30:6 and Jeremiah 4:4; 9:25–26 use the language of the heart alongside the physical sign, noting to whom each passage is addressed.",
"Follow Acts 15:1, 10–11, Acts 16:1–3 and Galatians 2:3–5 side by side, noting who presses circumcision, on what ground, and how each setting answers.",
"Trace the sequence Paul sets out in Romans 4:9–12 and what he says circumcision does and does not accomplish in Galatians 5:2–6 and 6:12–15.",
"Examine what Colossians 2:11–13 and Philippians 3:2–3 themselves say about circumcision “made without hands,” and compare their audience and setting with Romans 2:28–29.",
"Practise a diagnostic of covenant, company and kind of reality on every circumcision passage, and test each reading against the passages already traced."]
RUN={"THE NON-TRANSFER PRINCIPLE APPLIED":"The Non-Transfer Principle Applied.","THE PRESSURE DID NOT END AT JERUSALEM":"The Pressure Did Not End at Jerusalem.","REQUIRING WARNING":"Requiring Warning.","COLLAPSING WARNING":"Collapsing Warning."}
def apply(els):
    for k,t in enumerate(BUL): els[1+k]['segs']=[[t,False,False]]
    i=find(els,"To trace circumcision as Israel’s fleshly")
    els[i]['segs']=[["By the end of this study, the reader should be able to trace, from Genesis 17, Leviticus 12, Deuteronomy 10 and 30, Acts 15 and 16, Romans 4 and Colossians 2, the covenant, the company and the kind of reality (physical rite or spiritual reality) that each circumcision passage names, and to say from the texts’ own markers whether circumcision is required, permitted or set aside for the audience addressed.",False,False]]
    # callouts -> run-ins (4)
    n=0
    while n<len(els):
        e=els[n]
        if e['type']=='para' and e['kind']=='ctitle' and T(e) in RUN:
            lead=RUN[T(e)]; j=n+1; bodies=[]
            while j<len(els) and els[j]['type']=='para' and els[j]['kind']=='cbody': bodies.append(els[j]); j+=1
            new=[]
            for b,bd in enumerate(bodies):
                segs=[[lead,True,False],[' ',False,False]]+bd['segs'] if b==0 else bd['segs']
                new.append(mk('body',segs))
            els[n:j]=new; n+=len(new); continue
        n+=1
    # Galatians 2:1-10 chronology; text only
    rep(els,"precisely to protect the same gospel liberty the Jerusalem Council had already secured.","precisely to protect the truth of the gospel for those Gentile believers, in the passage’s own words. Galatians 2:1–10 is reported here as text only: Paul recounts the visit, and this study does not fix it on a timeline against Acts 15.")
    # 3.3 overlap + audience-specific
    app(els,"Timothy circumcised and Titus not compelled are not a contradiction","That was audience-specific conduct, not a change of Paul’s commission or gospel. "+R18S+" "+OVERLAP)
    # 3.6 Acts 10-11, Acts 15
    app(els,"The sequence across Acts is therefore continuous","Acts 10–11, the Cornelius account, is a Prophecy Program event inside the overlap, and Acts 15 belongs to the overlap itself; neither is assigned to a single program, and neither makes its Gentile hearers Israel.")
    # 4.1 Romans 4:9-12
    rep(els,"and Paul uses that very sequence to secure Gentile believers’ standing in Abraham’s fatherhood without requiring them to receive the sign at all.","and Paul uses that very sequence to show that the sign was never the ground of righteousness, so it could not be required of Gentile believers. The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant. This reading of Romans 4:9–12 rests on the passage’s own audience markers and setting.")
    # 4.2, 4.3
    app(els,"Paul states the stakes for the Body","This reading of Galatians 5:2–6 rests on the passage’s own audience markers and setting.")
    app(els,"Paul closes the letter by naming the motive","This reading of Galatians 6:12–15 rests on the passage’s own audience markers and setting.")
    # 5.2 Philippians
    app(els,"Paul goes further still, applying the very name","This reading rests on the letter’s own audience markers and setting.")
    # 5.3 Romans 2:28-29
    rep(els,"from a New-Covenant, in-Christ reality named directly","from an in-Christ reality named directly")
    app(els,"Paul makes a related statement earlier in Romans","This reading of Romans 2:28–29 rests on the passage’s own audience markers and setting.")
    # 5.4 Ephesians
    app(els,"Verse 13 then states the change","Brought near is not made Israel.")
    # 6.1
    rep(els,"under a covenant the Body does not inherit by descent,","under a covenant to which the Body is not a party,")
    # checklist Q1
    rep(els,"or a New-Covenant reality named for the Body?","or an in-Christ reality named for the Body?")
    # Group 2, 3
    app(els,"Observe: how Romans 3:29–30 grounds","For Romans 3:29–30 and 6:3–6, this reading rests on the passages’ own audience markers and setting. For Titus 1:10, this reading rests on the letter’s own audience markers and setting.")
    app(els,"Observe: how the same historical moment could hold","For Acts 21:20–25: "+OVERLAP)
    # KJV tables (4)
    addt(els,"God’s covenant with Abraham comes with a sign attached","The table sets out Genesis 17:9–14 in KJV wording. Observe what the sign is called, who is to receive it, when, and what is said of the one who refuses.",[
     ["Gen. 17:9–11","“And God said unto Abraham, Thou shalt keep my covenant therefore, thou, and thy seed after thee in their generations. This is my covenant, which ye shall keep, between me and you and thy seed after thee; Every man child among you shall be circumcised. And ye shall circumcise the flesh of your foreskin; and it shall be a token of the covenant betwixt me and you.”","Whose covenant is kept; what the sign is called; where it is cut."],
     ["Gen. 17:12–13","“And he that is eight days old shall be circumcised among you, every man child in your generations, he that is born in the house, or bought with money of any stranger, which is not of thy seed. He that is born in thy house, and he that is bought with thy money, must needs be circumcised: and my covenant shall be in your flesh for an everlasting covenant.”","The timing; who is included; the phrase “in your flesh.”"],
     ["Gen. 17:14","“And the uncircumcised man child whose flesh of his foreskin is not circumcised, that soul shall be cut off from his people; he hath broken my covenant.”","The stated penalty and the reason given for it."]])
    addt(els,"The concrete dispute Study 19 examines in full","The table sets out Acts 15:1 and 15:10–11 in KJV wording. Observe the claim stated, the question Peter asks and the ground he gives.",[
     ["Acts 15:1","“And certain men which came down from Judaea taught the brethren, and said, Except ye be circumcised after the manner of Moses, ye cannot be saved.”","Who makes the claim; what is required; what is attached to it."],
     ["Acts 15:10–11","“Now therefore why tempt ye God, to put a yoke upon the neck of the disciples, which neither our fathers nor we were able to bear? But we believe that through the grace of the Lord Jesus Christ we shall be saved, even as they.”","The question asked; the ground of salvation named."]])
    addt(els,"Paul states the stakes for the Body","The table sets out Galatians 5:2–6 in KJV wording. Observe what Paul says of the one who is circumcised, what he says of the one justified by the law, and what he says availeth.",[
     ["Gal. 5:2–3","“Behold, I Paul say unto you, that if ye be circumcised, Christ shall profit you nothing. For I testify again to every man that is circumcised, that he is a debtor to do the whole law.”","The condition and its stated result; the debt named."],
     ["Gal. 5:4","“Christ is become of no effect unto you, whosoever of you are justified by the law; ye are fallen from grace.”","Who is addressed; what is said of grace."],
     ["Gal. 5:5–6","“For we through the Spirit wait for the hope of righteousness by faith. For in Jesus Christ neither circumcision availeth any thing, nor uncircumcision; but faith which worketh by love.”","What availeth, and what does not."]])
    addt(els,"Paul names the Body’s own distinct reality","The table sets out Colossians 2:11–13 in KJV wording. Observe how the circumcision is described, who performs it and what it is joined with.",[
     ["Col. 2:11","“In whom also ye are circumcised with the circumcision made without hands, in putting off the body of the sins of the flesh by the circumcision of Christ:”","The phrase “made without hands”; what is put off; whose circumcision it is called."],
     ["Col. 2:12","“Buried with him in baptism, wherein also ye are risen with him through the faith of the operation of God, who hath raised him from the dead.”","What it is joined with; the means named."],
     ["Col. 2:13","“And you, being dead in your sins and the uncircumcision of your flesh, hath he quickened together with him, having forgiven you all trespasses;”","How the audience is described; what is said to have been done for them."]])
    return els
