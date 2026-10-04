from edcommon import *
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
SUSP="nationally suspended at Acts 28—not canceled, transferred or absorbed"
def apply(els):
    s=[k for k,e in enumerate(els) if P(e) and e['kind']=='sub' and T(e)=='Study Outline'][0]
    k=s+1
    while els[k]['kind']=='num': els[k]['kind']='bul'; k+=1
    rep(els,'marking where the text states the same ground (Deuteronomy 7:7; Ephesians 2:8–9) and where it does not.','marking what each passage gives as the reason for the choice (Deuteronomy 7:7; Ephesians 2:8–9) and where the passages differ.')
    rep(els,'Israel’s judicial suspension, examined fully in Study 21, describes a present administrative condition, with membership unchanged; it is not the revocation of an election God Himself calls irrevocable.','Israel’s Prophecy Program was %s (see Study 21); that suspension is not the revocation of an election God Himself calls irrevocable. %s'%(SUSP,BND))
    rep(els,'a Kingdom destiny that Israel’s present unbelief suspends in administration but does not cancel.','a Kingdom destiny that the national suspension of Israel’s Prophecy Program at Acts 28 does not cancel.')
    rep(els,'that national unbelief can suspend the administration of the promise without ever placing the promise itself at risk.','that the national suspension of Israel’s program leaves the promise itself untouched.')
    rep(els,'an earthly Kingdom destiny that present national unbelief has suspended but not cancelled.','an earthly Kingdom destiny that the national suspension of Israel’s program at Acts 28 has not cancelled.')
    rep(els,'so this, too, belongs to the shared ground of Section 5.1 rather than the list of divergences:','so this, too, is a point of likeness rather than of divergence:')
    rep(els,'5.1 Shared Ground: Sovereign Grace, Not Human Merit','5.1 What Both Elections Share: God’s Sovereign Initiative')
    rep(els,'Both elections rest on the same governing principle: God’s initiative, not man’s. Israel was not chosen for her size (Deuteronomy 7:7). The Body is not chosen “of works” (Ephesians 2:8–9; Romans 11:6). In both cases, Scripture forecloses any explanation rooted in the object’s own merit. This shared ground is the one point','Both elections are made by God’s initiative, not man’s. Israel was not chosen for her size (Deuteronomy 7:7). The Body is not chosen on the basis of works (Ephesians 2:8–9). In both cases, Scripture forecloses any explanation rooted in the object’s own merit. This shared feature is the one point')
    rep(els,'this shared ground does not make them one election.','this shared feature does not make them one election.')
    rep(els,'shared ground (grace, not merit) versus never-shared features','shared feature (God’s initiative, not merit) versus never-shared features')
    i=find(els,'Paul makes the connection between this election and his own gospel explicit')
    sg=els[i]['segs'][-1]
    tail='This reading rests on the passage’s own audience markers and setting.'
    assert sg[0].endswith(tail)
    sg[0]=sg[0][:-len(tail)]+'The Day of the Lord described earlier in the chapter (2:1–12) belongs to Israel’s Prophecy Program; this study draws on verses 13–14 only, where Paul turns to the gospel through which his readers were called. '+tail
    number_outline(els)
    return els
