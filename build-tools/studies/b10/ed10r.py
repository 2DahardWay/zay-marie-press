from edcommon import *
SEQ="Acts 28 establishes the suspension boundary; that the seventieth week remains future rests on Daniel 9:24–27 and the prophetic passages traced here, not on Acts 28 alone."
def sub(els,old,new):
    n=0
    for e in els:
        if P(e):
            for s in e['segs']:
                if old in s[0]: s[0]=s[0].replace(old,new,1); n+=1
    assert n==1,(old,n)
def apply(els):
    assert T(els[2]).startswith('You will learn how the biblical evidence') and T(els[3]).startswith('You will also examine')
    els[2]=mk('body',[['You will trace the textual markers for the beginning of that final week, its midpoint, the abomination of desolation, the Great Tribulation, Israel’s judgment and preservation, and the return of Christ, testing each step against the passages themselves.',False,False]])
    els[3]=mk('body',[['You will also examine how Daniel’s prophetic timetable relates to the Acts 9–28 period, reading the Acts record for what continues, what begins, and what is said at Acts 28.',False,False]])
    idx=[i for i in range(4,14) if els[i]['kind']=='bul']
    assert len(idx)==8 and els[idx[-1]+1]['kind']=='ctitle'
    new=['Read Daniel 9:24–27 for the people, city and objectives it names.',
    'Follow the sixty-nine weeks to Messiah and test what Daniel 9:26–27 says comes next.',
    'Read Acts 1–9 and Acts 28 for what continues and what begins, and note what they leave unstated.',
    'Collect the markers Daniel 9:27 gives for the beginning and midpoint of the week, and compare Matthew 24 and Revelation to separate the whole week from its latter half.',
    'Trace what the prophets say about Israel’s judgment, preservation and recognition of Messiah, and what each says preservation is.',
    'Reconstruct the argument directly from Scripture rather than from an inherited prophetic chart.']
    els[idx[0]:idx[-1]+1]=[mk('bul',[[t,False,False]]) for t in new]
    sub(els,'this marks the national judicial suspension of Israel’s Prophecy Program—not abolition and not a transfer.','Israel’s Prophecy Program was nationally suspended—not canceled, transferred or absorbed. '+SEQ)
    sub(els,'entered its national judicial suspension at Acts 28.','was nationally suspended at Acts 28.')
    sub(els,'The national judicial suspension of Prophecy at Acts 28 did not cancel them.','The national suspension of Prophecy at Acts 28 did not cancel them.')
    sub(els,'At Acts 28, Israel’s Prophecy Program entered its national judicial suspension—not abolition and not a transfer—while','At Acts 28, Israel’s Prophecy Program was nationally suspended—not canceled, transferred or absorbed—while')
    sub(els,'Acts 28 is the national judicial suspension of Israel’s Prophecy Program (not abolition and not a transfer);','At Acts 28 Israel’s Prophecy Program was nationally suspended (not canceled, transferred or absorbed);')
    sub(els,'Prophecy then enters its national judicial suspension (not abolition and not a transfer) while','Prophecy is then nationally suspended (not canceled, transferred or absorbed) while')
    for e in els:
        if P(e):
            assert 'judicial suspension' not in T(e) and 'not abolition' not in T(e), T(e)[:80]
    number_outline(els)
    return els
