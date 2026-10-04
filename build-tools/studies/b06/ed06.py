from edcommon import *
KEEP={'STUDY GOAL','MYSTERY REVELATION CHAIN','CONTROLLING DEFINITION','ACTS OVERLAP CONTROL','FINAL SYNTHESIS QUESTION'}
def apply(els):
    setbul(els,'Define the Pauline Mystery','Trace what Paul means by “mystery” by following the term through Romans 16:25–26, Ephesians 3 and Colossians 1:25–27, noting how each passage describes its hiddenness and its revelation.')
    setbul(els,'Show from Romans 16','Read Romans 16:25–26, Ephesians 3:2–9 and Colossians 1:25–27 side by side, marking each phrase that speaks of the time before the revelation.')
    setbul(els,'Distinguish prophetic Gentile blessing','Compare the prophetic pattern of Gentile blessing with Paul’s language of “the same body” (Eph. 3:6), marking where each places the Gentile in relation to Israel.')
    setbul(els,'Explain Acts 28 as the suspension','Examine Acts 28:25–28 beside Isaiah 6 and Romans 11:25, marking what the passage changes in Israel’s active program and what it leaves untouched.')
    rep(els,'within the Acts Overlap framework is a broader','within the Acts Overlap is a broader')
    i=find(els,'Within the larger framework, Israel’s Prophecy Program has a future resumption')
    els[i]['segs']=[['Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one.',False,False]]
    i=find(els,'Paul speaks of Israel’s fall, diminishing')
    ins_after_idx(els,i,ROM)
    i=find(els,'From Acts 9–28 the two programs operate distinctly')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    finish(els,KEEP)
    return els
