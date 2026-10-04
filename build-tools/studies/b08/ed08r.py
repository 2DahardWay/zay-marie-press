from edcommon import *
def apply(els):
    idx=[i for i in range(0,14) if els[i]['type']=='para' and els[i]['kind']=='bul']
    assert len(idx)==9 and idx==list(range(idx[0],idx[0]+9)) and els[idx[-1]+1]['kind']=='ctitle'
    new=['Collect Paul’s Day-of-Christ expressions and record exactly what each passage itself says.',
    'Test how far Philippians 1:6 and 2:16 carry, and note what each verse leaves unsaid.',
    'Keep what the Day texts state apart from what other Pauline passages add on resurrection, gathering, presentation and glory.',
    'Read the Judgment Seat passages for what they say about evaluation, reward and loss.',
    'Compare the Day of Christ and the Day of the Lord by their own contexts, and handle 2 Thessalonians 2 with attention to the translation question.']
    els[idx[0]:idx[-1]+1]=[mk('bul',[[t,False,False]]) for t in new]
    n=0
    for e in els:
        if P(e) and 'Study #8' in T(e):
            for s in e['segs']:
                if 'Study #8' in s[0]: s[0]=s[0].replace('Study #8','this study'); n+=1
    assert n==1
    number_outline(els)
    return els
