from edcommon import *
import re
def unb(t): return re.sub(r'^•\s+','',t)
def setp(els,prefix,new):
    i=find(els,prefix); els[i]['segs']=[[new,False,False]]; return i
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study' and T(els[8])=='STUDY GOAL'
    new=['Trace where Scripture speaks of resurrection in more than one connection, noting for each passage who is raised, when and toward what destination.',
    'Trace what “firstfruits” in 1 Corinthians 15:20–23 says Christ’s resurrection secures, and what the word “afterward” in verse 23 introduces.',
    'Follow 1 Thessalonians 4:13–18 and 1 Corinthians 15:51–54 to see what each passage ties the believer’s resurrection to, and what each leaves unsaid.',
    'Examine the “out-resurrection” wording of Philippians 3:11 and test what it does and does not claim.',
    'Trace what Revelation 20:4–6 and 20:5, 11–15 say about who is raised, when, and after what interval, alongside Daniel 12:2 and John 5:28–29.',
    'Ask how Ezekiel 37 identifies its own subject, and what follows for the way the passage is used.',
    'Compare the shared vocabulary—“resurrection,” “raised,” “changed”—across these passages, and test whether the same word names the same event in each.']
    els[1:8]=[mk('body',[['By the end of this study, you should be able to:',False,False]])]+[mk('bul',[[t,False,False]]) for t in new]
    a=[k for k,e in enumerate(els) if P(e) and T(e)=='Study Outline'][0]
    k=a+1
    while re.match(r'^\d+\.\t',T(els[k])):
        els[k]=mk('bul',[[re.sub(r'^\d+\.\t','',T(els[k])),False,False]]); k+=1
    assert k-a-1==12
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Teaching Outline'][0]
    k=ta+1
    while els[k]['kind']=='body':
        els[k]=mk('bul',[[T(els[k]),False,False]]); k+=1
    assert k-ta-1==12
    ga=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Guided Further Study'][0]
    k=ga+1
    while k<len(els) and els[k]['kind']=='body' and T(els[k]).startswith('•'):
        els[k]=mk('bul',[[unb(T(els[k])),False,False]]); k+=1
    rep(els,'State the Framework principle:','State the governing principle:')
    rep(els,'under the Framework’s distinction between Israel’s prophetic resurrections and the Body’s heavenly one.','by the distinction between Israel’s prophetic resurrections and the Body’s heavenly one.')
    rep(els,'The Framework governs how this study reads each passage:','This study reads each passage by its own audience and program:')
    rep(els,'matching the Framework’s description of the Body’s resurrection as tied to glorification rather than to the Kingdom.','consistent with the Body’s resurrection being tied to glorification rather than to the Kingdom.')
    rep(els,'The Framework does not assign 1 Thessalonians as a book; this reading rests','This reading rests')
    rep(els,'The Framework does not assign Philippians as a book; this reading rests','This reading rests')
    rep(els,'Paul anchors the entire chapter','Paul builds the entire chapter')
    rep(els,'The plain sense of the passage anchors the point instead','The plain sense of the passage supports the point instead')
    rep(els,'Reading these passages under the Framework’s distinction preserves','Reading these passages by this distinction preserves')
    rep(els,'Held together under the Framework’s distinction —','Held together under this distinction —')
    i=find(els,'Concurrency is operational, not transformational.'); assert T(els[i])=='Concurrency is operational, not transformational.'
    els[i]['segs']=[[R17,False,False]]
    for k,e in enumerate(els):
        if P(e) and e['kind']=='body' and T(e).startswith('•'):
            els[k]=mk('bul',[[unb(T(e)),False,False]])
    for e in els:
        if P(e):
            t=T(e)
            for bad in ['Framework','anchor','•']: assert bad not in t,(bad,t[:80])
    number_outline(els)
    return els
