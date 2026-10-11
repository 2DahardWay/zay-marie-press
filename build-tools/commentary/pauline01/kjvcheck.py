"""Check every curly-quoted string in the volume content against the KJV corpus.
usage: python3 kjvcheck.py   (run in the build dir). Prints quotes not found in KJV text and table rows whose
quote is not inside the verse reference given in the same row."""
import sys,re,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import kjvlib, content
Q=re.compile('“([^”]+)”')
def pieces(q):
    return [p.strip() for p in re.split(r'…|\.\.\.',q) if p.strip()]
miss=[];rowbad=[];nq=0
def scan(ctx,s):
    global nq
    for m in Q.finditer(s):
        for p in pieces(m.group(1)):
            nq+=1
            if not kjvlib.in_corpus(p): miss.append((ctx,p))
cur='front'
for el in content.ALL:
    k=el[0]
    if k=='h1': cur=el[1]
    if k in('p','sub','h1'): scan(cur,el[1])
    elif k=='call': scan(cur,el[2])
    elif k in('bul','num'):
        for t in el[1]: scan(cur,t)
    elif k=='bib': scan(cur,el[1])
    elif k in('tbl','ctbl'):
        scan(cur,el[1])
        for r in el[2]:
            for cell in r: scan(cur,cell)
        if k=='tbl':
            for r in el[2]:
                ref,txt=r[0],r[1]
                for m in Q.finditer(txt):
                    for p in pieces(m.group(1)):
                        try:
                            if not kjvlib.in_ref(p,ref): rowbad.append((cur,ref,p))
                        except (KeyError,ValueError) as e: rowbad.append((cur,ref,f'REF ERROR {e}'))
print(f'{nq} quoted pieces checked; {len(miss)} not found in KJV corpus; {len(rowbad)} table rows outside their verse reference')
for c,p in miss: print('  NOT KJV  [%s] %s'%(c[:38],p))
for c,r,p in rowbad: print('  ROW      [%s] %s :: %s'%(c[:30],r,p))
