from edcommon import *
def apply(els):
    # WYWL lead-in and process bullets
    els.insert(1,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    rep(els,'What Paul means by “grace giving” in 2 Corinthians 8–9 — trace the relationship between the grace already received and the giving that follows, and test whether the text ever frames it as a command imposed.','Trace what Paul means by “grace giving” in 2 Corinthians 8–9, following the relationship between the grace already received and the giving that follows, and test whether the text ever frames it as a command imposed.')
    rep(els,'How 2 Corinthians 9:6–15 moves from the cheerful giver to the harvest of righteousness the gift produces and the thanksgiving it returns to God.','Follow the movement of 2 Corinthians 9:6–15 from the cheerful giver to the harvest of righteousness the gift produces and the thanksgiving it returns to God.')
    rep(els,'How 1 Corinthians 16:1–2 establishes an orderly weekly pattern of setting aside — and what to look for in the text before deciding whether that pattern functions as a tithe.','Read 1 Corinthians 16:1–2 for the orderly weekly pattern of setting aside, noting what the text says before deciding whether that pattern functions as a tithe.')
    rep(els,'What Philippians 4:10–19 adds: contentment that does not depend on the gift, and giving as partnership (fellowship) in the gospel.','Read Philippians 4:10–19 for how Paul speaks of contentment apart from the gift and of giving as partnership (fellowship) in the gospel.')
    # Study Outline bulleted
    s=[k for k,e in enumerate(els) if P(e) and e['kind']=='sub' and T(e)=='Study Outline'][0]
    k=s+1
    while els[k]['kind']=='num': els[k]['kind']='bul'; k+=1
    # Romans 15:27 sentence (publisher-approved)
    old='Romans 15:27 says the Gentiles “have been made partakers of their spiritual things”; that describes participation in blessing, not identity, and it does not place the Body in Israel’s covenants or make the Body Israel.'
    new='Romans 15:27 says the Gentiles “have been made partakers of their spiritual things” and are debtors to them in carnal things. That records a debt of gratitude between two companies during the overlap, not a place in Israel’s covenants or in Israel’s program. Participation is not identity. Blessing is not covenant. Standing is not program membership.'
    rep(els,old,new)
    number_outline(els)
    return els
