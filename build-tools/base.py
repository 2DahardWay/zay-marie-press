def T(e): return ''.join(s[0] for s in e['segs'])
def rep(els,old,new):
    for e in els:
        if e['type']=='para':
            for s in e['segs']:
                if old in s[0]: s[0]=s[0].replace(old,new,1); return
    raise Exception('NF: '+old[:50])
def find(els,start):
    for i,e in enumerate(els):
        if e['type']=='para' and T(e).startswith(start): return i
    raise Exception('NF start: '+start[:50])
def app(els,start,add):
    e=els[find(els,start)]; e['segs'].append([' '+add,False,False])
def ins_after(els,start,text,kind='body',bold=False):
    i=find(els,start); src=els[i]
    els.insert(i+1,dict(type='para',kind=kind,segs=[[text,bold,False]],p=src['p'],top=src['top']+1,x0=src['x0'],lasttop=0,lastp=src['p']))
def ins_after_idx(els,i,text,kind='body'):
    src=els[i]; els.insert(i+1,dict(type='para',kind=kind,segs=[[text,False,False]],p=src['p'],top=0,x0=src['x0'],lasttop=0,lastp=src['p']))
OVERLAP="During the overlap, the circumcision apostleship ministers to Israel under the Prophecy Program, and Paul’s gospel forms the Body; the two operate concurrently and never merge, transfer or absorb one another."
R17="During Acts 9–28, the remnant remains Israel’s prophetic believing company, and the Body remains the Mystery new creation. They coexist historically but never merge in identity, membership, calling, covenant, gospel, hope, or destiny. Concurrency is operational, not transformational."
R18="Paul’s commission never changes: he is the apostle of the Gentiles, and his own gospel is the gospel of the grace of God. When he reasons in the synagogues from Israel’s Scriptures, he proclaims Israel’s Messiah and kingdom hope to Israel, whose prophetic program remained operative until its national suspension at Acts 28. That is audience-specific proclamation, not a second gospel and not a change of commission; it does not make Paul a Prophecy apostle, and it does not make his hearers members of the Body by that message."
R18S="Paul’s synagogue preaching was audience-specific, not commission-specific."
R11="These are recorded in settings shaped by Israel’s Prophecy Program, which remained operative throughout Acts 9–28 even as the Mystery Program began. Acts 9–28 is the overlap; where Paul or his companions are the ones filled or working signs, the study reports the text and does not assign the event to a single program."
ROM="Four boundaries govern the Romans 11 reading: the olive tree is prophetic blessing, not the Body; the Gentiles of Romans 11 are prophetic participants, not Body Gentiles; wild branches are not Body members; and grafting changes participation, not identity. Participation is not identity. Blessing is not covenant. Standing is not program membership."
def apply(els):
    rep(els,"Within the Acts Overlap framework, Acts 9 is","Within the Acts Overlap, Acts 9 is")
    rep(els,"Within the controlling framework, Acts 9 marks","On this reading, Acts 9 marks")
    rep(els,"Within the Acts Overlap framework, this is","Within the Acts Overlap, this is")
    rep(els,"a stable framework for interpreting","a stable chronology for interpreting")
    # Rule 18
    ins_after(els,"This distinction protects both sides of the Acts record",R18)
    app(els,"Paul repeatedly enters synagogues after Acts 9",R18S)
    app(els,"Paul’s Gentile ministry becomes increasingly prominent",R18S)
    # Rule 11
    app(els,"Signs also continue during Paul’s Acts ministry",R11)
    # Acts 10-12 Cornelius
    app(els,"Peter remains central. The Cornelius account","Acts 10–11, the Cornelius account, is a Prophecy Program event inside the overlap; the Gentiles who appear in it belong to prophetic fulfillment, not to the Body, and their presence implies no Body membership.")
    # overlap + R17
    ins_after(els,"Nor is the overlap a merger",OVERLAP)
    ins_after(els,"Acts 9 is therefore both a boundary and a beginning",R17)
    # Acts 28
    rep(els,"Acts 28 is the later judicial suspension point of Prophecy","Acts 28 is the later national judicial suspension of Prophecy, not abolition and not a transfer")
    # Guided further study
    rep(els,"Paul’s voluntary adaptation to different audiences.","Paul’s voluntary conduct toward different audiences, not a changed gospel.")
    rep(els,"distinguish historical accommodation from doctrinal obligation.","customs and vows are audience-specific, not a change of commission, and historical participation is not doctrinal obligation.")
    i=find(els,"As you study, keep separate")
    ins_after_idx(els,i-1,ROM)
    ins_after_idx(els,i,"This reading of 1 Timothy rests on the letter’s own audience markers and setting.")
    return els
