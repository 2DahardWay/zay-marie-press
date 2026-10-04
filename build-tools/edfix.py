import re
from edcommon import *
def rm_num(segs,pat):
    s=[list(x) for x in segs]
    if re.fullmatch(pat+r'[\t ]',s[0][0]): s=s[1:]
    else: s[0][0]=re.sub(r'^'+pat+r'\s+','',s[0][0])
    return s
def unb(segs):
    s=[list(x) for x in segs]
    if s[0][0].strip()=='•': s=s[1:]
    else: s[0][0]=re.sub(r'^•\s+','',s[0][0])
    return s
def study_outline_bullets(els):
    a=[k for k,e in enumerate(els) if P(e) and T(e)=='Study Outline'][0]; k=a+1; n=0
    while P(els[k]) and (els[k]['kind'] in ('num','bul') or (els[k]['kind']=='body' and re.match(r'^\d+\.[\t ]',T(els[k])))):
        s=els[k]['segs']
        if els[k]['kind']=='body': s=rm_num(s,r'\d+\.')
        els[k]=mk('bul',[list(x) for x in s]); k+=1; n+=1
    return n
def teaching_outline_numbered(els,pat=r'(\d+\.|[IVX]+\.)'):
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Teaching Outline'][0]; k=ta+1; ng=0
    while P(els[k]) and els[k]['kind']=='body' and not re.match(r'^'+pat+r'[\t ]',T(els[k])): k+=1
    while P(els[k]) and els[k]['kind']=='body' and re.match(r'^'+pat+r'[\t ]',T(els[k])):
        els[k]=mk('bul',rm_num(els[k]['segs'],pat)); k+=1; ng+=1
    return ng
