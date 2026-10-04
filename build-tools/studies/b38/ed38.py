from edcommon import *
KEEP={'STUDY GOAL','PROGRAMMATIC CONTROL','NARRATIVE CONTROL','INTERPRETIVE CONTROL','PRESENT-DOCTRINE CONTROL'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
CORN="Acts 10–11, the Cornelius account, is a Prophecy Program event inside the overlap; the Gentiles who appear in it belong to prophetic fulfillment, not to the Body, and their presence implies no Body membership."
BUL=["Read a passage in Acts in its immediate context and identify its audience and apostolic commission.",
"Distinguish what Luke describes from what Scripture commands.",
"Test whether Acts 2, 4, 5, 9, 10, 15, 19, 21, and 28 can be read as one universal experience pattern or require separate treatment.",
"Work through signs, baptism, communal property, repeated filling, visions, and Paul’s Jewish practices case by case.",
"State, for each case, what the text establishes and what it does not establish.",
"Identify what further doctrinal evidence would be needed before claiming a continuing obligation for the Body of Christ."]
def apply(els):
    assert T(els[1]).startswith('By completing this study') and T(els[2]).startswith('You will work through')
    els[1:3]=[mk('body',[['By the end of this study, you should be able to:',False,False]])]+[mk('bul',[[b,False,False]]) for b in BUL]
    rep(els,'which are read as the Framework assigns them;','which are read in their own audience and setting;')
    rep(els,'Within this framework, that scene marks the national judicial suspension of Israel’s Prophecy Program.','Within the Acts Overlap, that scene marks the national suspension of Israel’s Prophecy Program—not canceled, transferred or absorbed. '+BND)
    rep(els,'the national judicial conclusion within the Acts Overlap framework,','the national suspension within the Acts Overlap,')
    rep(els,'During the overlap, the circumcision apostleship ministers to Israel under the Prophecy Program; believing Jews are gathered into the Body through Paul’s ministry, and this speaks of identity, not program membership.',OVERLAP)
    app(els,'In Acts 9 the risen Christ calls Paul.',R18S)
    i=find(els,'In Acts 9 the risen Christ calls Paul.'); ins_after_idx(els,i,R17)
    i=find(els,'Paul circumcises Timothy because of Jews'); ins_after_idx(els,i,R11)
    i=find(els,'In Acts 10:34–48, Peter speaks to Cornelius’s household'); ins_after_idx(els,i,CORN)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
