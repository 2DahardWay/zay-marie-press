from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','ROMANS 11 CONTROL','ACTS 28 BOUNDARY','FINAL CONTROL'}
def apply(els):
    assert T(els[1]).startswith('Israel’s judicial blinding is a phrase')
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'reproducible teaching framework','reproducible teaching outline')
    rep(els,'Within the Acts Overlap framework, the answer must','Within the Acts Overlap, the answer must')
    rep(els,'This distinction is essential to the Acts Overlap framework.','This distinction is essential to the Acts Overlap.')
    rep(els,'Within this framework, that pronouncement','On this reading, that pronouncement')
    rep(els,'Within the Acts Overlap framework, this is the judicial','Within the Acts Overlap, this is the judicial')
    i=find(els,'The Framework classifies the remnant of Romans 11:5')
    els[i]['segs']=[['The remnant of Romans 11:5 is Israel’s believing remnant, the same remnant as in the Old Testament, within the Prophecy Program. It is never Gentiles and is not the Body. The remnant never becomes the Body and stays outside the Body, the Mystery Program and the heavenly calling.',False,False]]
    i=find(els,'Romans 11:7–15 develops the argument further')
    ins_after_idx(els,i,'“Salvation is come unto the Gentiles” speaks of salvation, not of covenant, prophetic identity or Israel’s program.')
    i=find(els,'The judicial blinding is therefore real but non-covenant-canceling')
    ins_after_idx(els,i,ROM+' Identity is fixed by divine program, not by metaphor. Concurrency is operational, not transformational.')
    i=find(els,'Paul’s conversion and commissioning at Acts 9 marks')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    i=find(els,'The sequence is crucial: Israel is addressed')
    ins_after_idx(els,i,R18)
    rep(els,'It does not mark the cancellation of Israel’s Prophecy Program, covenants, promises, or future fulfillment.','It is not a cancellation, transfer or absorption of Israel’s Prophecy Program, covenants, promises, or future fulfillment.')
    app(els,'Acts 28 should therefore be described with precise language','Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one.')
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
