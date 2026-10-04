from edcommon import *
def apply(els):
    assert all(els[i]['kind']=='bul' for i in range(4,16)) and els[16]['kind']=='ctitle'
    new=['Trace the Day of the Lord through the prophets’ own vocabulary of intervention, wrath, darkness, judgment and restoration.',
    'Weigh what the prophets say about the Day’s length and scope, and test whether it fits a single twenty-four-hour day.',
    'Separate what 1 Thessalonians 5 explicitly states from conclusions drawn from the wider prophetic record, and follow the THEY/YOU contrast through the passage.',
    'Read 1 Thessalonians 4 beside chapter 5 and note what each passage addresses and to whom.',
    'Handle 2 Thessalonians 2 within the limits of what the passage itself says, without asking it to carry a complete chronology.']
    els[4:16]=[mk('bul',[[t,False,False]]) for t in new]
    for k,e in enumerate(els):
        if P(e) and 'Study #7' in T(e):
            for s in e['segs']: s[0]=s[0].replace('Study #7','this study')
    for e in els:
        if P(e) and 'Study #7' in T(e): raise SystemExit('left')
    number_outline(els)
    return els
