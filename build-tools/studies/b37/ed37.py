from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','NON-TRANSFER CONTROL','RENEWAL CONTROL','PROGRAMMATIC CONTROL'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
def apply(els):
    rep(els,'the expression refers to believing Jews within the Body—Israelites by identity.','the expression refers to believing Jews within Israel’s prophetic identity—not members of the Body.')
    rep(els,'This speaks of identity, not program membership; the remnant is ethnic-covenantal, and believing Jews are gathered into the Body during the Mystery administration.',R17)
    rep(els,'During the overlap, the circumcision apostleship ministers to Israel under the Prophecy Program; believing Jews are gathered into the Body through Paul’s ministry, and this speaks of identity, not program membership.',OVERLAP)
    rep(els,'when Israel’s Prophecy Program reached its national judicial suspension point.','when Israel’s Prophecy Program was nationally suspended at Acts 28—not canceled, transferred or absorbed. '+BND)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
