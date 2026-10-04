from edcommon import *
KEEP={'STUDY GOAL','ROMANS CONTROL','INTERPRETIVE CONTROL','SEED CONTROL','HEIR CONTROL'}
G3="The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant."
BUL=["Trace how the word “seed” is used in Genesis, Romans 4 and 9, and Galatians 3, asking in each passage who the referent is and what argument the word serves.",
"Examine why Romans 4 appeals to Abraham’s justification before circumcision, and what that appeal does and does not carry into Paul’s argument.",
"Follow how Galatians 3:16 handles the promise to the seed, and how Galatians 3:29 describes heirs according to promise.",
"Compare Genesis 12, 15, 17, and 22 with Romans 4:1–17; 9:6–13; and Galatians 3:6–5:6.",
"Name the specific benefit Paul states in a cited passage and set it beside Israel’s national covenant terms in Genesis.",
"Explain a difficult seed passage without treating every use of the word as identical."]
def apply(els):
    assert T(els[1]).startswith('You will trace') and T(els[2]).startswith('You will compare')
    els[1:3]=[mk('body',[['By the end of this study, you should be able to:',False,False]])]+[mk('bul',[[b,False,False]]) for b in BUL]
    rep(els,'During the overlap, the circumcision apostleship ministers to Israel under the Prophecy Program; believing Jews are gathered into the Body through Paul’s ministry, and this speaks of identity, not program membership.',OVERLAP+' '+R17)
    rep(els,'Gentiles participate spiritually in the blessing and heirship Paul names here.',G3)
    rep(els,'they receive righteousness through faith before and apart from circumcision, and participate in promise on the basis of grace rather than law.','they receive righteousness through faith before and apart from circumcision, on the basis of grace rather than law.')
    rep(els,'Gentiles are not asked to complete their Abrahamic heirship by adopting a sign','Gentiles are not asked to complete the standing Paul describes by adopting a sign')
    rep(els,'believing Gentiles participate spiritually in Abrahamic blessing by faith, receive the promised Spirit, and are heirs in Christ.',G3+' Paul grants that believers receive the promised Spirit and are heirs in Christ.')
    rep(els,'These claims together give believers a substantial Abrahamic connection without converting','These claims together show what Paul says believers receive in Christ—righteousness, the Spirit, and sonship—without converting')
    n=0
    for e in els:
        if e.get('type')=='tbl':
            for r in e['rows']:
                for ci,c in enumerate(r):
                    if 'Gentiles participate spiritually in that blessing.' in c:
                        r[ci]=c.replace('Gentiles participate spiritually in that blessing.',G3); n+=1
    assert n==1
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
