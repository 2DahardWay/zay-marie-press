from edcommon import *
import re
SUSP="nationally suspended—not canceled, transferred or absorbed"
SEQ="Acts 28 establishes the suspension boundary; the sequence this study draws from it — the Body’s gathering before Israel’s prophetic program resumes — rests on 1 Thessalonians 4–5 and 2 Thessalonians 2, not on Acts 28 alone."
def apply(els):
    assert T(els[3])=='By the end of the study, you should be able to:'
    els[3]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'Explain why Daniel’s seventieth week concerns Daniel’s people and holy city.','Read Daniel 9:24–27 for the audience the prophecy names, and test whether the seventieth week can be relabeled without changing that audience.')
    rep(els,'Explain 1 Thessalonians 1:10, 4:13–18, and 5:1–9 as a cumulative Pauline argument.','Follow 1 Thessalonians 1:10, 4:13–18 and 5:1–9 passage by passage, noting how each adds to the one before it.')
    rep(els,'Explain why the Rapture belongs to the Mystery revealed through Paul.','Trace where the catching away of the Body is revealed in Scripture, and compare its revelatory setting with the prophetic Tribulation passages.')
    rep(els,'Use the Acts Overlap chronology to explain why Prophecy can resume after the present Mystery purpose is complete.','Follow the Acts 9–28 overlap and the Acts 28 passage, noting what each says about the two programs and what each leaves unstated.')
    rep(els,'Trace and reproduce the biblical reasoning for the Body’s pre-Tribulation gathering to Christ.','Practise restating, from the passages and in your own words, how each step of the study’s argument is built, so that you can reproduce it for someone else.')
    # Study Outline and Teaching Outline: group lines bullet / number, items second level
    def regroup(h,group_kind):
        a=[k for k,e in enumerate(els) if P(e) and e['kind'] in('sub','h1') and T(e).startswith(h)][0]+1
        k=a
        while not (els[k]['kind']=='h1'  or (els[k]['kind']=='ctitle')):
            e=els[k]; t=T(e)
            if e['kind']=='body' and re.match(r'^[IVX]+\. ',t): els[k]=mk(group_kind,[[re.sub(r'^[IVX]+\. ','',t),False,False]])
            elif e['kind']=='bul': els[k]=mk('bul2',[[t,False,False]])
            k+=1
    regroup('Study Outline','bul')
    regroup('Teaching Outline','num')
    # Acts 28 conforming
    rep(els,'At Acts 28, Israel’s active Prophecy Program enters national judicial suspension, not abolition and not a transfer. The Mystery Program continues beyond Acts 28. Suspension, however, is not cancellation. God’s covenants','At Acts 28, Israel’s active Prophecy Program was %s. %s The Mystery Program continues beyond Acts 28. God’s covenants'%(SUSP,SEQ))
    rep(els,'Acts 28 is the national judicial suspension, not abolition and not a transfer of Israel’s active Prophecy Program; Mystery continues.','At Acts 28 Israel’s active Prophecy Program was %s; Mystery continues.'%SUSP)
    rep(els,'At Acts 28, Israel’s active Prophecy Program entered national judicial suspension, not abolition and not a transfer while Mystery continued.','At Acts 28, Israel’s active Prophecy Program was %s—while Mystery continued.'%SUSP.replace('—not','—not',1))
    rep(els,'Acts 28 is the national judicial suspension, not abolition and not a transfer of Prophecy without canceling Israel’s promises.','At Acts 28 Israel’s Prophecy Program was %s, and Israel’s promises stand.'%SUSP)
    rep(els,'Acts 28: national judicial suspension of Prophecy (not abolition, not a transfer); Mystery continues','Acts 28: Prophecy nationally suspended (not canceled, transferred or absorbed); Mystery continues')
    rep(els,'Prophecy under national judicial suspension, not abolition and not a transfer at Acts 28 while Mystery continues.','Prophecy nationally suspended—not canceled, transferred or absorbed—at Acts 28 while Mystery continues.')
    n=0
    for e in els:
        if e['type']=='tbl':
            for r in e['rows']:
                for ci,c in enumerate(r):
                    if c=='Acts 28 national judicial suspension of Prophecy': r[ci]='Acts 28 national suspension of Prophecy'; n+=1
    assert n==1
    i=find(els,'This is overlap, not replacement, blending')
    ins_after_idx(els,i,R17)
    number_outline(els)
    return els
