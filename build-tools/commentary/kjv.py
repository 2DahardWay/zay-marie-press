import sys,re
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import kjvlib
for a in sys.argv[1:]:
    m=re.match(r'^([^:]+):(\d+):(\d+)(?:-(\d+))?$',a)
    if not m: print('usage: kjv.py Book:ch:v1-v2'); continue
    b,ch,v1,v2=m.group(1),int(m.group(2)),int(m.group(3)),int(m.group(4) or m.group(3))
    c=kjvlib.code(b)
    for v in range(v1,v2+1): print(f'{b} {ch}:{v}  {kjvlib.V[(c,ch,v)]}')
