from edcommon import *
KEEP={'STUDY GOAL','REMNANT STUDY CHAIN','INTERPRETIVE CONTROL','FINAL TRUTH','ROMANS 11 BOUNDARIES'}
R11B=ROM+" Identity is fixed by divine program, not by metaphor. “Salvation is come unto the Gentiles” speaks of salvation, not of covenant, prophetic identity or Israel’s program. Concurrency is operational, not transformational."
def apply(els):
    setbul(els,'Explain why a remnant of Israel remains Israel','Follow Paul’s argument in Romans 11:1–5, noting how he names himself, whom he calls “his people,” and whom he calls “a remnant.”')
    setbul(els,'Distinguish believing Israel','Compare the believing company of the Gospels and early Acts (Matt. 19:28; Acts 2–3) with Paul’s description of the Body, marking whom each text addresses and what each says about identity.')
    setbul(els,'Explain Acts 28 as suspension','Examine Acts 28:25–28 beside Isaiah 6, marking what the passage changes in Israel’s active program and what it leaves untouched.')
    setbul(els,'Handle Romans 11 and the olive-tree','Read the olive-tree imagery of Romans 11:16–24 closely, marking who is addressed, what the branches do and do not become, and what the passage says about boasting.')
    setbul(els,'Explain why Israel’s remnant and the Body','Trace the destinies described in Revelation 7 and in Ephesians 1:3 and 2:6, noting the terms each passage uses for who receives what.')
    rep(els,'Within the Acts Overlap framework, Acts 28','Within the Acts Overlap, Acts 28')
    rep(els,'The controlling boundary in this framework is Acts 28.','The controlling boundary is Acts 28.')
    rep(els,'This framework therefore seeks','This reading therefore seeks')
    for e in els:
        if P(e) and e['kind']=='h1' and T(e)=='A Note on the Acts Overlap Framework': e['segs']=[['A Note on the Acts Overlap',False,False]]
    rep(els,'Israel’s prophetic purpose therefore awaits its appointed resumption and fulfillment; it is not transferred','Israel’s prophetic purpose is not transferred')
    i=find(els,'During Acts 9–28, the continuing presence of Israel’s remnant')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    i=find(els,'Revelation continues the prophetic story')
    ins_after_idx(els,i,'The Body of Christ does not appear in Revelation’s prophetic scenes.')
    i=find(els,'Neither does participation in the olive tree')
    els[i+1:i+1]=[mk('ctitle',[['ROMANS 11 BOUNDARIES',True,False]]),mk('cbody',[[R11B,False,False]])]
    finish(els,KEEP)
    return els
