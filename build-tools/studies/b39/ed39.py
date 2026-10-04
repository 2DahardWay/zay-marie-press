from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','APPLICATION CONTROL','COVENANT CONTROL','APOSTOLIC CONTROL'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
G3="The seed is prophetic fulfillment in Christ; the Body receives blessing through Christ alone, not through participation in the Abrahamic covenant."
BUL=["Distinguish the original audience of an Old Testament passage from the later readers who benefit from it.",
"Explain the learning Paul identifies in Romans 15:4 and 1 Corinthians 10:1–13, and the usefulness of Scripture in 2 Timothy 3:14–17.",
"Separate an enduring revelation about God from a command or promise tied to Israel’s covenant setting.",
"Practice this distinction with Exodus 20:8–11, Deuteronomy 28, Psalm 23, Jeremiah 29:10–14, and Malachi 3:8–12.",
"Examine how Romans 4 draws on Genesis 15:6, noting what Paul quotes, the question he answers, and what the quotation does and does not carry into his argument.",
"State an Old Testament passage’s original claim, a defensible lesson for the Body, and a claim that the passage does not authorize."]
def apply(els):
    assert T(els[1]).startswith('By completing this study') and T(els[2]).startswith('You will practice')
    els[1:3]=[mk('body',[['By the end of this study, you should be able to:',False,False]])]+[mk('bul',[[b,False,False]]) for b in BUL]
    rep(els,'The Framework does not assign 2 Timothy as a book; this reading rests on','This reading rests on')
    rep(els,'The Framework does not assign Philippians as a book; this reading rests on','This reading rests on')
    rep(els,'Gentiles participate spiritually in that blessing.',G3)
    rep(els,'During the overlap, the circumcision apostleship ministers to Israel under the Prophecy Program; believing Jews are gathered into the Body through Paul’s ministry, and this speaks of identity, not program membership.',OVERLAP+' '+R17)
    rep(els,'Israel’s Prophecy Program enters national judicial suspension at Acts 28, while the Mystery continues.','Israel’s Prophecy Program was nationally suspended at Acts 28—not canceled, transferred or absorbed—while the Mystery continues. '+BND)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
