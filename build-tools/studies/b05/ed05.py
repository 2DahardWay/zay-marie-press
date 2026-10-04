from base import *
import re
KEEP={'STUDY GOAL','HEAVENLY CALLING CHAIN','CONTROLLING DEFINITION','ACTS OVERLAP CONTROL','FINAL SYNTHESIS QUESTION'}
def mk(kind,segs): return dict(type='para',kind=kind,segs=segs,p=0,x0=0)
def apply(els):
    # WYWL
    assert T(els[0])=='What You Will Learn in This Study'
    j=[k for k,e in enumerate(els) if e['type']=='para' and T(e).startswith('By the end of this study')][0]
    del els[1:j]
    i=find(els,'Explain how the Acts 9–28 overlap permits')
    els[i]['segs']=[['Examine Acts 9, Romans 16:25 and Acts 28:25–28 together, marking how the callings run in the overlap and what the Acts 28 passage changes and leaves untouched.',False,False]]
    # run-in conversion of extra callouts
    k=0
    while k<len(els):
        e=els[k]
        if e['type']=='para' and e['kind']=='ctitle' and T(e) not in KEEP:
            lead=T(e).capitalize()+'.'
            bodies=[];m=k+1
            while m<len(els) and els[m]['type']=='para' and els[m]['kind']=='cbody': bodies.append(els[m]);m+=1
            new=[mk('body',[[lead,True,False],[' '+T(bodies[0]),False,False]])]+[mk('body',b['segs']) for b in bodies[1:]]
            els[k:m]=new; k+=len(new); continue
        k+=1
    n=sum(1 for e in els if e['type']=='para' and e['kind']=='ctitle'); assert n==5,n
    # wording
    app(els,'This study therefore does not make its doctrine depend','Hebrews 3:1 is read on the letter’s own audience markers and setting, not as the ground of this doctrine.')
    rep(els,'Within the larger Acts Overlap framework, this gathering','Within the Acts Overlap, this gathering')
    i=find(els,'Within the larger Acts Overlap framework, the completion')
    els[i]['segs']=[['Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one. The point here is that the Body’s hope reaches completion without becoming Israel’s Kingdom hope.',False,False]]
    rep(els,'but Study #5 does not need to repeat the complete seven-distinction case established elsewhere.','but this study does not repeat the complete seven-distinction case here.')
    rep(els,'confirms the distinction without requiring Study #5 to re-teach the entire framework.','confirms the distinction without re-teaching the whole case here.')
    rep(els,'addressed Israel within the framework of prophetic promises','addressed Israel within the setting of prophetic promises')
    # overlap + R17
    i=find(els,'That historical overlap does not change the calling')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    # Teaching outline numbered
    sec=None
    for e in els:
        if e['type']=='para':
            if e['kind']=='h1': sec=T(e)
            elif sec=='Teaching Outline' and e['kind']=='bul': e['kind']='num'
    # checkboxes
    for e in els:
        if e['type']=='para' and T(e).startswith('□ '): e['segs'][0][0]='[ ] '+e['segs'][0][0][2:]
    return els
_old=apply
def apply(els):
    els=_old(els)
    for e in els:
        if e['type']=='para':
            for sg in e['segs']: sg[0]=sg[0].replace('→','»')
        else:
            e['rows']=[[c.replace('→','»') for c in r] for r in e['rows']]
    return els
_old2=apply
def apply(els):
    els=_old2(els)
    for e in els:
        if e['type']=='para':
            for sg in e['segs']: sg[0]=sg[0].replace('’heavenly places’','“heavenly places”')
    return els
