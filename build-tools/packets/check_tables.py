#!/usr/bin/env python3
"""Table-integrity check for Bible Book Companions.
usage: python3 check_tables.py <slug-module> [<pdf>]   (run from build-tools/packets)
Compares every table in content_<slug>.py with the same table in git HEAD (or a baseline file) cell for cell:
row count, column count and every cell must match exactly. Program Identity cells may differ only where the new value is one of the
two-class labels. With a PDF, also confirms every cell's words appear in the rendered PDF text. Exit 1 on any difference."""
import sys,re,subprocess,types,importlib
from pathlib import Path
D=Path(__file__).resolve().parent
LAB={'Israel / Kingdom / Prophecy Explicit Truth','Body of Christ (Pauline) Truth','Universal Truth'}
def tables(m): return [b for n,t,bl in m.SECTIONS for b in bl if b[0]=='table']
def run(k,baseline=None,pdf=None):
    new=importlib.import_module('content_'+k)
    src=baseline or subprocess.run(['git','show',f'HEAD:build-tools/packets/content_{k}.py'],capture_output=True,text=True,cwd=D).stdout
    old=types.ModuleType('old'); exec(src,old.__dict__)
    a,b=tables(old),tables(new); bad=[]
    if len(a)!=len(b): bad.append(f'table count {len(a)} -> {len(b)}')
    for ti,(x,y) in enumerate(zip(a,b)):
        if x[1]!=y[1]: bad.append(f'table {ti} header {x[1]} -> {y[1]}')
        if len(x[2])!=len(y[2]): bad.append(f'table {ti} rows {len(x[2])} -> {len(y[2])}')
        for ri,(r1,r2) in enumerate(zip(x[2],y[2])):
            if len(r1)!=len(r2): bad.append(f'table {ti} row {ri} cols'); continue
            for ci,(c1,c2) in enumerate(zip(r1,r2)):
                if c1!=c2 and not (len(r1)==4 and ci==2 and c2 in LAB): bad.append(f'table {ti} r{ri} c{ci}: {c1!r} -> {c2!r}')
    if pdf:
        txt=subprocess.run(['pdftotext',str(pdf),'-'],capture_output=True,text=True).stdout
        norm=lambda s:re.sub(r'[^a-z0-9]+',' ',re.sub('<[^>]+>','',s).replace('&amp;','&').lower()).split()
        bag=set(norm(txt))
        for t in b:
            for r in [t[1]]+t[2]:
                for c in r:
                    miss=[w for w in norm(c) if w not in bag]
                    if miss: bad.append(f'not in PDF: {c!r} {miss}')
    return bad
if __name__=='__main__':
    k=sys.argv[1]; bad=run(k,None,sys.argv[2] if len(sys.argv)>2 else None)
    print(k,'TABLES OK' if not bad else 'TABLE DIFFERENCES'); [print('  ',x) for x in bad]; sys.exit(1 if bad else 0)
