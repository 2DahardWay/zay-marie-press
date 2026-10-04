from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','GRAFTING CONTROL','MYSTERY CONTROL','ACTS OVERLAP CONTROL'}
def apply(els):
    setbul(els,'Why Romans 11 begins','Read Romans 11:1–2 for the question Paul asks, the answer he gives, and the controls those verses set on the chapter.')
    setbul(els,'How Israel’s remnant','Trace Israel’s condition through Romans 11:3–15, marking the remnant, the stumbling, the diminishing, and what Paul says follows for the Gentiles.')
    setbul(els,'How to identify','Identify the root, the natural branches, and the wild branch as Paul introduces them in Romans 11:16–24, marking what he calls each.')
    setbul(els,'Why grafting changes','Follow the verbs of breaking off and grafting in at Romans 11:17–24, marking what Paul says is changed and what he does not say.')
    setbul(els,'Why olive-tree participation','Compare the olive-tree language of Romans 11 with Paul’s vocabulary for the one Body, marking which terms each passage uses.')
    setbul(els,'How Romans 11 and Ephesians 2','Set Romans 11 beside Ephesians 2, marking who is addressed, what is described, and what question each passage answers.')
    setbul(els,'How Romans 11 fits','Place Romans 11 against the Acts 9–28 record, marking what the text shows Prophecy and Mystery each doing in that period.')
    assert T(els[1]).startswith('Romans 11 must be read')
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'establishes the proper framework for everything that follows','sets the controls for everything that follows')
    rep(els,'Without this framework, interpreters','Without this chronology, interpreters')
    i=find(els,'The fact that salvation is going to Gentiles')
    ins_after_idx(els,i,'“Salvation is come unto the Gentiles” speaks of salvation, not of covenant, prophetic identity or Israel’s program.')
    i=find(els,'Grafting explains participation. The one Body')
    ins_after_idx(els,i,ROM+' Identity is fixed by divine program, not by metaphor.')
    i=find(els,'This is the essential feature of the Acts Overlap')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    rep(els,'At Acts 28 Prophecy is suspended—not canceled—while Mystery continues.','At Acts 28 Israel’s Prophecy Program is nationally suspended—not canceled, transferred or absorbed—while Mystery continues.')
    app(els,'At Acts 28, Israel’s Prophecy Program reaches its suspension point','Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one.')
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
