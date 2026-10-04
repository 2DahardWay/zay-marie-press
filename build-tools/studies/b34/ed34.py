from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','REPEATED FILLING ≠ REPEATED SALVATION','OVERLAP WITHOUT TRANSFER','PRESENT APPLICATION'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
def apply(els):
    strip_wywl(els)
    i=find(els,'Acts 9 introduces Saul’s calling')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    j=find(els,'Saul’s immediate synagogue witness')
    ins_after_idx(els,j,R11)
    app(els,'Saul’s immediate synagogue witness',R18S)
    rep(els,'continues beyond Acts 28 after Israel’s national judicial suspension.','continues beyond Acts 28 after Israel’s Prophecy Program was nationally suspended—not canceled, transferred or absorbed. '+BND)
    for e in els:
        if e['type']!='para':
            e['rows']=[[c.replace('read as the Framework assigns them;','read in their own audience and setting;') for c in r] for r in e['rows']]
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
