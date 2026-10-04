import sys; sys.path.insert(0,'..')
from edfix import *
import ed64
def apply(els):
    els=ed64.apply(els)
    rep(els,'Use this framework to explain','Use this outline to explain')
    n=study_outline_bullets(els); assert n>=4,n
    g=teaching_outline_numbered(els); assert g>=6,g
    number_outline(els); return els
