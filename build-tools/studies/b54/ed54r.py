from edcommon import *
import re
def unb(t): return re.sub(r'^•\s+','',t)
def setp(els,prefix,new):
    i=find(els,prefix); els[i]['segs']=[[new,False,False]]; return i
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study' and T(els[7])=='STUDY GOAL'
    # Framework sentences (withdrawn wording)
    n=0
    for e in els:
        if P(e):
            for s in e['segs']:
                new,c=re.subn(r'The Framework does not assign [^;]*; this reading rests on the (passage|letter)’s own',r'This reading rests on the \1’s own',s[0])
                if c: s[0]=new; n+=c
    assert n==22,n
    rep(els,'This reading rests on the passage’s own audience markers and setting.','This reading rests on the passage’s own audience markers and setting.')
    i=find(els,'One implication follows for the believer’s own assurance')
    els[i]['segs'][0][0]=els[i]['segs'][0][0].replace('This reading rests on the passage’s own audience markers and setting.','This reading rests on these passages’ own audience markers and setting.')
    # Rule 19 / thesis
    setp(els,'By the end of this study, the reader should be able to trace what the passages on Israel','By the end of this study, the reader should be able to trace what the passages on Israel’s pursuit (Romans 9:30–10:4), Romans 3–5, Galatians 2:16 and Genesis 15:6 each name as the ground and the means of righteousness, and to say from the texts’ own markers what stays constant in justification—faith, never works—and what differs with the content God had revealed.')
    rep(els,'denying that Abraham himself, centuries before the law was given, already received the very verdict Romans 4 describes.','denying that Abraham himself, centuries before the law was given, was already counted righteous by believing God (Genesis 15:6).')
    rep(els,'or Israel’s own departure from what was always true?','or a departure from the means God had revealed?')
    rep(els,'establishes that faith-righteousness is not new but is Scripture’s own oldest pattern for how a sinner is declared righteous.','establishes that faith-righteousness is not new: Scripture’s own earliest case is Abraham, counted righteous by believing God.')
    rep(els,'The ground is always Christ’s own accomplished work','In Paul’s gospel the ground of the believer’s justification is Christ’s own accomplished work')
    rep(els,'The means is always faith, and faith alone (Romans 3:28), never a human contribution added beside it, however small.','The means is faith, and faith alone (Romans 3:28), never a human contribution added beside it, however small. Salvation is always by faith and never by merit; what differs between programs is the content God had revealed for faith to rest on.')
    rep(els,'when Scripture states the cause as already, and only, Christ’s own finished work.','when Paul states the cause as Christ’s own finished work.')
    rep(els,'believing Jews are gathered into the Body through Paul’s ministry, and this speaks of identity, not program membership.','XXOVERLAPXX')
    i=find(els,'Paul’s own testimony in the same verse states the purpose')
    t=els[i]['segs'][0][0]; j=t.index('During the overlap'); els[i]['segs'][0][0]=t[:j]+OVERLAP
    rep(els,'Paul draws the conclusion for every later believer, of any ancestry:','Paul draws a conclusion from Abraham’s case:')
    rep(els,'Abraham’s own pattern is not a special case reserved for one man or one nation; it is named as the pattern every person who is justified, in any age, shares. Gentiles who believe participate spiritually in Abraham’s blessing, and the seed is read as prophetic fulfillment in Christ; this is never described as an identity transfer, Israel remains Israel, and the Body is not called Israel.','Abraham was counted righteous by believing God, not by works, before circumcision and before the law. The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant.')
    rep(els,'Abraham’s own righteousness is declared on the single ground of belief — the same verdict, the same means, that Paul later names for the believer in Christ.','Abraham’s own righteousness is declared on belief, not works: he believed what God had told him. Paul later names faith, never works, as the means for the believer in Christ.')
    rep(els,'rather than a pattern already complete in Genesis 15:6.','rather than a means already present in Genesis 15:6.')
    rep(els,'could not disannul a covenant already ratified by God on that ground (Galatians 3:17).','could not disannul a covenant already ratified by God (Galatians 3:17).')
    rep(els,'Sections 1 through 5 have traced one doctrine from several directions','Sections 1 through 5 have traced justification by faith from several directions')
    setp(els,'Treating the law as a onetime valid path','Treating the law as a onetime valid path and treating faith-righteousness as a late invention are opposite conclusions from the same wrong assumption: that law and faith were ever presented as two competing methods for the same verdict, one succeeding where the other failed. Scripture never presents law-works as a method of righteousness: Israel’s pursuit by works stumbled, and Abraham was counted righteous by believing God (Genesis 15:6), as Paul is by faith. Salvation is always by faith and never by works; what differs is the content God had revealed for faith to rest on—to Abraham, his promise; to the Body, Paul’s gospel. Neither error is corrected by softening the law’s exclusion or faith’s priority; both are corrected by reading Romans 9–10 and Romans 4 for what each states.')
    setp(els,'Scripture names one righteousness, tested against two responses.','Scripture never presents law-works as the way to righteousness. Israel’s own pursuit of a law-righteousness, sincere but misdirected (Romans 9:30–10:4), stumbled because it sought by works what God gives to faith. Faith-righteousness was neither new in Paul’s hands nor late in arriving: Abraham was counted righteous by believing God centuries before the law existed (Genesis 15:6), the law and the prophets themselves testified to it in advance (Romans 3:21), and Paul states it as his own settled ground against the very error his countrymen fell into (Philippians 3:9; Galatians 2:16). Salvation is always by faith and never by merit, but the content of faith is what God revealed within each program: Abraham believed God’s promise; the Body is justified by believing Paul’s gospel (Romans 3:24–26; 4:25; 5:1). Reading Israel’s stumbling and the Body’s standing for what each passage states protects the reader from treating the law as a once-valid alternative and from treating faith as anything but the means God has always required.')
    rep(els,'This study traced one doctrine of justification tested against two responses.','This study traced what Scripture states about righteousness by faith, tested against two responses.')
    rep(els,'proves this was never a new doctrine,','shows that righteousness by faith, not works, was never a new idea,')
    rep(els,'as one continuous testimony rather than two competing doctrines.','for what each passage itself states, not as two rival doctrines.')
    rep(els,'proving faith-righteousness is Scripture’s oldest pattern, not Paul’s invention.','showing that righteousness by faith, not works, is not Paul’s invention.')
    setp(els,'•\tThe ground of justification is always another','•\tIn Paul’s gospel the ground of the believer’s justification is another’s accomplished work (Christ’s death and resurrection, Romans 4:25), never the believer’s own doing. Salvation is always by faith and never by merit; the content of faith is what God revealed within each program.')
    rep(els,'why Israel’s stumbling and the Body’s standing describe one doctrine, not two.','what each passage states about works and faith, and why neither describes law-works as a valid road to righteousness.')
    rep(els,'Conclude: one righteousness, tested against two responses','Conclude: faith, never works, tested against two responses')
    rep(els,'Romans 4:16’s “all the seed” is read under the Galatians 3 ruling: Gentiles participate spiritually in the promise, never by identity transfer, and Israel remains Israel.','The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant.')
    i=find(els,'Observe: how Isaiah’s own prophecy already anticipated'); els[i]['segs'][0][0]+=' '+ROM
    rep(els,'justification stated as one verdict for both companies.','justification stated as by faith for both the circumcision and the uncircumcision.')
    rep(els,'how Ephesians 2:8–9 states the same ground and means for the Body of Christ that Romans 3–5 states for Jew and Gentile alike.','how Ephesians 2:8–9 states the ground and means for the Body of Christ in terms Romans 3–5 also uses.')
    rep(els,'why one verdict, on one ground, by one means, does not erase','why justification by faith, never by works, does not erase')
    rep(els,'state the case for one doctrine of justification tested against two responses','state what Scripture says about righteousness by faith, tested against two responses')
    rep(els,'the righteousness of God by faith already present in Abraham','the righteousness of God by faith counted to Abraham')
    # format
    assert all(T(els[k]).startswith('•') for k in range(1,7))
    for k in range(1,7): els[k]=mk('bul',[[unb(T(els[k])),False,False]])
    els.insert(1,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    a=[k for k,e in enumerate(els) if P(e) and T(e)=='Study Outline'][0]; k=a+1
    while re.match(r'^\d+\.\t',T(els[k])):
        els[k]=mk('bul',[[re.sub(r'^\d+\.\t','',T(els[k])),False,False]]); k+=1
    assert k-a-1==6
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Teaching Outline'][0]; k=ta+1; ng=0
    while els[k]['kind']=='body':
        t=T(els[k])
        if re.match(r'^[A-Z]\.\t',t): els[k]=mk('bul2',[[re.sub(r'^[A-Z]\.\t','',t),False,False]])
        else: els[k]=mk('bul',[[t,False,False]]); ng+=1
        k+=1
    assert ng==8,ng
    for k,e in enumerate(els):
        if P(e) and e['kind']=='body' and T(e).startswith('•'): els[k]=mk('bul',[[unb(T(e)),False,False]])
    for e in els:
        if P(e):
            t=T(e)
            for bad in ['Framework','XXOVERLAP','•','one doctrine','same verdict','one verdict','oldest pattern','participate spiritually','gathered into']: assert bad not in t or bad=='same verdict',(bad,t[:90])
    number_outline(els)
    return els
