import json,re,os
D='/home/claude/aruljohn/bible-kjv/'
_c={}
def book(b):
    if b not in _c:
        _c[b]={ (int(c['chapter']),int(v['verse'])):v['text'] for c in json.load(open(D+b.replace(' ','')+'.json'))['chapters'] for v in c['verses']}
    return _c[b]
def get(b,ch,v1,v2=None):
    v2=v2 or v1; bk=book(b)
    return [(v,bk[(ch,v)]) for v in range(v1,v2+1) if (ch,v) in bk]
if __name__=='__main__':
    import sys
    for a in sys.argv[1:]:
        m=re.match(r'(\d?\s?[A-Za-z]+) (\d+):(\d+)(?:-(\d+))?$',a); b,ch,v1,v2=m.groups()
        print('##',a)
        for v,t in get(b,int(ch),int(v1),int(v2) if v2 else None): print(v,t)
