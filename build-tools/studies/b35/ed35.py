from edcommon import *
import re
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','EQUALITY IS NOT IDENTITY TRANSFER','REMNANT CONTROL','IDENTITY CONTROL'}
BND="Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one."
TRI="Participation is not identity. Blessing is not covenant. Standing is not program membership. Identity is fixed by divine program, not by metaphor."
def apply(els):
    # real bullets / numbering from typed prefixes
    sec=None
    for e in els:
        if not P(e): continue
        if e['kind'] in('h1','sub'): sec=T(e)
        if e['kind']!='body': continue
        t=e['segs'][0][0]
        m=re.match(r'^(•|\d+\.|[IVX]+\.)\t',t)
        if m:
            e['segs'][0][0]=t[m.end():]
            if m.group(1)=='•' or sec in('Study Outline','Teaching Outline'): e['kind']='bul'
            else: e['kind']='num'
    rep(els,'after Israel’s national program enters national judicial suspension, not abolition.','after Israel’s Prophecy Program was nationally suspended—not canceled, transferred or absorbed. '+BND)
    rep(els,'The Olive Tree Firewall governs the reading:','Four boundaries govern the reading:')
    i=find(els,'Romans 11 depicts Gentiles as wild olive branches')
    ins_after_idx(els,i,TRI)
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
