from edcommon import *
KEEP={'STUDY GOAL','PARALLEL CONTROL','ORIGIN CONTROL','OVERLAP CONTROL','BODY CONTROL'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
SUSP="nationally suspended—not canceled, transferred or absorbed"
BUL=["Check where the phrase “kingdom of heaven” appears in the New Testament and compare Matthew’s phrase with Mark’s and Luke’s “kingdom of God” in the parallel sayings.",
"Trace why Matthew speaks of “heaven,” following Daniel 2 and 7 and the way the Gospels describe the kingdom promised to Israel.",
"Follow how the kingdom is proclaimed “at hand,” and distinguish the mysteries of the kingdom in Matthew 13 from the Mystery revealed to Paul.",
"Trace the range of “kingdom of God” across Scripture: Israel’s promised kingdom, God’s universal reign, and Paul’s kingdom vocabulary for the Body, each in its own passages.",
"Read Acts 19:8, 28:23 and 28:31 by audience, source and setting, asking what kingdom language means at each point in Acts.",
"Classify any kingdom text by its program, audience and destiny, and test three common answers against Scripture."]
def apply(els):
    assert T(els[1]).startswith('You will check') and T(els[2]).startswith('You will also')
    els[1:3]=[mk('body',[['By the end of this study, you should be able to:',False,False]])]+[mk('bul',[[b,False,False]]) for b in BUL]
    for bk,w in (('2 Timothy','letter’s'),('1 Thessalonians','letter’s'),('Philippians','letter’s')):
        rep(els,'The Framework does not assign %s as a book; this reading rests on'%bk,'This reading rests on')
    rep(els,' The Framework does not assign Revelation as a book; this reading rests on the book’s own audience markers and setting.','')
    rep(els,'That framework does not decide what each phrase means before the text is read. The framework supplies the interpretive controls; the passages determine the classification.','These controls do not decide what each phrase means before the text is read; the passages determine the classification.')
    rep(els,'the program distinctions the framework requires','the program distinctions the passages themselves draw')
    rep(els,'This speaks of identity, not program membership; the remnant is ethnic-covenantal, and believing Jews are gathered into the Body during the Mystery administration.',R17)
    rep(els,'This is Prophecy-Program content spoken by the Mystery apostle. It does not make Paul a Prophecy apostle, and it does not transfer Israel’s kingdom to the Body.',R18+' It does not transfer Israel’s kingdom to the Body. '+OVERLAP)
    rep(els,'and her kingdom promises await their future resumption and fulfillment.','and her kingdom promises await their future resumption and fulfillment. '+ROM)
    rep(els,'It follows the national judicial suspension of Israel’s Prophecy Program.','It follows the national suspension of Israel’s Prophecy Program at Acts 28. '+BND)
    rep(els,'suspended nationally at Acts 28 without being abolished','%s at Acts 28'%SUSP)
    rep(els,'During Acts 9–28, Paul may testify of Israel’s kingdom to Jewish audiences from Israel’s Scriptures (Acts 19:8; 28:23).','During Acts 9–28, Paul reasons from Israel’s Scriptures and proclaims Israel’s kingdom hope to Jewish audiences (Acts 19:8; 28:23). '+R18S)
    n=0
    for e in els:
        if e.get('type')=='tbl':
            for r in e['rows']:
                for ci,c in enumerate(r):
                    c2=c.replace('Paul testifying of the kingdom in synagogues is Prophecy content spoken to Israel, not the Body’s inheritance.',R18S+' It is not the Body’s inheritance.').replace('Israel’s kingdom program was suspended at Acts 28, not cancelled;','Israel’s kingdom program was %s at Acts 28;'%SUSP)
                    if c2!=c: r[ci]=c2; n+=1
    assert n==2,n
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    rep(els,'Acts Overlap Theology supplies the controls for answering carefully.','The overlap of Acts 9–28 supplies the controls for answering carefully.')
    rep(els,'Acts Overlap Theology governs where these answers differ from Scripture’s own distinctions.','The overlap of Acts 9–28 governs where these answers differ from Scripture’s own distinctions.')
    els[:]=[e for e in els if not (P(e) and T(e).strip()=='ZAY-MARIE PRESS DIGITAL STUDIES')]
    return els
