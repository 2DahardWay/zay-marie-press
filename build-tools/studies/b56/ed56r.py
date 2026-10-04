from edcommon import *
import re
def rm_num(segs,pat):
    s=[list(x) for x in segs]
    if re.fullmatch(pat+r'\t',s[0][0]): s=s[1:]
    else: s[0][0]=re.sub(r'^'+pat+r'\s+','',s[0][0])
    return s
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study'
    rep(els,'according to promise (3:29); The seed is prophetic fulfillment','according to promise (3:29). The seed is prophetic fulfillment')
    els.insert(1,mk('body',[['By the end of this study, you should be able to:',False,False]]))
    a=[k for k,e in enumerate(els) if P(e) and T(e)=='Study Outline'][0]; k=a+1; n=0
    while els[k]['kind']=='num':
        els[k]['kind']='bul'; k+=1; n+=1
    assert n==5,n
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Teaching Outline'][0]; k=ta+1; ng=0
    while els[k]['kind']=='body' and re.match(r'^[IVX]+\.',T(els[k])):
        els[k]=mk('bul',rm_num(els[k]['segs'],r'[IVX]+\.')); k+=1; ng+=1
    assert ng==5,ng
    for e in els:
        if P(e): assert not re.match(r'^(•|[IVX]+\.\t)',T(e))
    number_outline(els)
    return els
