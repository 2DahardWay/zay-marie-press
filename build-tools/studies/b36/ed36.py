from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','CATEGORY CONTROL','EQUALITY IS NOT ERASURE','PRESENT IDENTITY CONTROL'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
TRI="Participation is not identity. Blessing is not covenant. Standing is not program membership. Identity is fixed by divine program, not by metaphor."
def apply(els):
    rep(els,'when Prophecy’s national operation was judicially suspended, with membership unchanged.','when Israel’s Prophecy Program was nationally suspended at Acts 28—not canceled, transferred or absorbed. '+BND)
    rep(els,'The unity of the saving God and the common ground of faith do not require Paul to abandon the designations.','The oneness of God and the justification by faith that Paul states do not require Paul to abandon the designations.')
    i=find(els,'Romans 9–11 continues the distinction at programmatic depth')
    ins_after_idx(els,i,TRI)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
