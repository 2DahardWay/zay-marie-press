from base import *
import re
def mk(kind,segs): return dict(type='para',kind=kind,segs=segs,p=0,x0=0)
def P(e): return e['type']=='para'
def strip_wywl(els):
    assert T(els[0])=='What You Will Learn in This Study'
    j=[k for k,e in enumerate(els) if P(e) and T(e).startswith('By the end of this study')][0]
    del els[1:j]
def setbul(els,start,new):
    i=[k for k,e in enumerate(els) if P(e) and e['kind']=='bul' and T(e).startswith(start)][0]
    els[i]['segs']=[[new,False,False]]
def runin_extras(els,keep):
    seen=set();k=0
    while k<len(els):
        e=els[k]
        if P(e) and e['kind']=='ctitle':
            t=T(e)
            if t in keep and t not in seen: seen.add(t); k+=1; continue
            lead=t.capitalize()+'.'
            bodies=[];m=k+1
            while m<len(els) and P(els[m]) and els[m]['kind']=='cbody': bodies.append(els[m]);m+=1
            new=[mk('body',[[lead,True,False],[' '+T(bodies[0]),False,False]])]+[mk('body',b['segs']) for b in bodies[1:]]
            els[k:m]=new; k+=len(new); continue
        k+=1
    n=sum(1 for e in els if P(e) and e['kind']=='ctitle'); assert n==5,n
def number_outline(els):
    import re as _re
    for _i,_e in enumerate(els):
        if _e['type']=='para' and _e['kind']=='h1' and ''.join(s[0] for s in _e['segs'])=='Review and Discussion Questions':
            _k=_i+1
            while _k<len(els) and els[_k]['type']=='para' and els[_k]['kind']=='body' and _re.match(r'^\d+\.[\t ]',''.join(s[0] for s in els[_k]['segs'])):
                _s=[list(x) for x in els[_k]['segs']]; _s[0][0]=_re.sub(r'^\d+\.[\t ]\s*','',_s[0][0]); els[_k]=dict(type='para',kind='num',segs=_s,p=0,x0=0); _k+=1
    sec=None
    for e in els:
        if P(e):
            if e['kind']=='h1': sec=T(e)
            elif sec and sec.startswith('Teaching Outline') and e['kind']=='bul': e['kind']='num'
def glyphs(els):
    for e in els:
        if P(e):
            for sg in e['segs']:
                sg[0]=sg[0].replace('→','»').replace('’heavenly','“heavenly')
                if sg[0].startswith('□ '): sg[0]='[ ] '+sg[0][2:]
        elif e['type']=='tbl':
            e['rows']=[[c.replace('→','»') for c in r] for r in e['rows']]
def finish(els,keep):
    strip_wywl(els); runin_extras(els,keep); number_outline(els); glyphs(els)
