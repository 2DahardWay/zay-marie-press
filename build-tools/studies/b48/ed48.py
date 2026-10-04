from edcommon import *
import re
def unbullet(els,lo,hi,pat):
    for i in range(lo,hi):
        e=els[i]; t=T(e)
        m=re.match(pat,t); assert m,(i,t[:40])
        e['segs']=[[t[m.end():],False,False]]; e['kind']='bul'
def apply(els):
    # drop source imprint lines (template supplies the imprint)
    assert T(els[-1]).startswith('Copyright ©') and T(els[-2])=='ZAY-MARIE PRESS DIGITAL STUDIES'
    del els[-2:]
    unbullet(els,1,8,r'•\t')
    # Study Outline
    unbullet(els,11,23,r'\d+\.\t')
    # Guided Further Study bullets
    unbullet(els,147,151,r'•\t')
    # WYWL: lead-in + process bullets
    els.insert(1,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    rep(els,'What Paul actually commands husbands in Ephesians 5:25–33 — trace the standard against Christ’s own self-giving love for the church, and test it against any reading that would make it a license to rule.','Trace the standard Paul sets for husbands in Ephesians 5:25–33 against Christ’s own self-giving love for the church, and test it against any reading that would make it a license to rule.')
    rep(els,'Why children are told to obey (Eph. 6:1–3) and fathers are told not to provoke to wrath (6:4) in the same breath, and what that balance protects.','Read the instruction to children (Eph. 6:1–3) beside the instruction to fathers (6:4), noting what each is told and what each is told to avoid.')
    rep(els,'What 1 Timothy 5:8 means by providing “for his own, and specially for those of his own house,” and how it fits with the rest of the household instruction.','Follow the phrase “for his own, and specially for those of his own house” in 1 Timothy 5:8, and compare it with the household instruction in Ephesians and Colossians.')
    # standing sentences
    rep(els,'The Framework does not assign 1 Peter as a book; this reading rests on the letter’s own audience markers and setting.','This reading rests on the letter’s own audience markers and setting.')
    rep(els,'The PAM makes no assignment for Galatians 3:28; this reading rests on the passage’s own audience markers and setting.','This reading rests on the passage’s own audience markers and setting.')
    # section 12 title (heading, outline, TOC source)
    for _ in range(2):
        rep(els,'A Common Confusion: Submission Is Not Inferiority, Headship Is Not Superiority','Submission Is Not Inferiority, Headship Is Not Superiority')
    # Teaching Outline numbered
    s=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Teaching Outline'][0]
    k=s+1
    while els[k]['kind']=='body': els[k]['kind']='bul'; k+=1
    number_outline(els)
    return els
