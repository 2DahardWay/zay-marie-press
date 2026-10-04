import sys; sys.path.insert(0,'..')
from edfix import *
def apply(els):
    assert T(els[0])=='What You Will Learn in This Study'
    rep(els,'Use this framework to explain','Use this outline to explain')
    n=study_outline_bullets(els); assert n>=5,n
    assert teaching_outline_numbered(els)==7
    assert sum(1 for e in els if P(e) and e['kind']=='ctitle')==5
    number_outline(els); return els
