import sys; sys.path.insert(0,'..')
from edfix import *
def apply(els):
    ra=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e)=='Review and Discussion Questions'][0]; k=ra+1; n=0
    while P(els[k]) and els[k]['kind']=='bul': els[k]['kind']='num'; k+=1; n+=1
    assert n>=5,n
    assert sum(1 for e in els if P(e) and e['kind']=='ctitle')==5
    number_outline(els); return els
