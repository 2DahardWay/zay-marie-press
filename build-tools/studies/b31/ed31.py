from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','GOSPEL CONTROL','JUDGMENT SEAT CONTROL','CHRONOLOGY CONTROL'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
SUSP="nationally suspended—not canceled, transferred or absorbed"
def apply(els):
    assert T(els[1])=='By completing this study, you will be able to:'
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'The Framework assigns Israel’s prophetic accountability and the Body’s Judgment Seat; the placement of Matthew 25 and Revelation 19–22 in this study is an interpretive reading drawn from each passage’s own markers, not a PAM assignment.','Israel’s prophetic accountability and the Body’s Judgment Seat belong to distinct programs; the placement of Matthew 25 and Revelation 19–22 in this study rests on each passage’s own audience markers and setting.')
    rep(els,'At the Cross, the sinless Redeemer suffers and provides the ground of salvation.','At the Cross, the sinless Redeemer bears the judicial consequences of sin (Rom. 5:8–9; Col. 2:13–15).')
    rep(els,'Prophecy began before Acts 9 and continued concurrently with Mystery until Israel’s national judicial suspension at Acts 28.','Prophecy began before Acts 9 and continued concurrently with Mystery until Israel’s Prophecy Program was %s at Acts 28. %s %s %s'%(SUSP,BND,OVERLAP,R17))
    rep(els,'Within the Acts Overlap framework, Israel’s Prophecy Program continued','During the overlap, Israel’s Prophecy Program continued')
    rep(els,'Acts 28 marks Israel’s national judicial suspension, not the abolition of prophetic promises.','At Acts 28 Israel’s Prophecy Program was %s, and its prophetic promises stand.'%SUSP)
    rep(els,'or use the five-question framework from this study','or use the five-question method from this study')
    i=find(els,'Matthew 24–25 belongs within this prophetic horizon.')
    ins_after_idx(els,i,'The Body is absent from the Day of the Lord, from Daniel’s seventieth week and from the Tribulation judgments of Revelation; these judgments belong to Israel’s Prophecy Program, not to the Body.')
    app(els,'The purpose is truthful evaluation by the Lord','This reading of Colossians 3:23–25 rests on the letter’s own audience markers and setting.')
    app(els,'Scripture also identifies angelic accountability.','This reading of 2 Peter and Jude rests on each letter’s own audience markers and setting.')
    n=0
    for e in els:
        if e['type']=='tbl':
            for r in e['rows']:
                for ci,c in enumerate(r):
                    if c=='National judicial suspension is not cancellation of promise': r[ci]='National suspension is not cancellation, transfer or absorption of promise'; n+=1
    assert n==1
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
