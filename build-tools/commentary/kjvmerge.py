"""Merge the two independently fetched KJV copies (A, B) into kjv_all.txt.
Rule: A is the base. Differences that are only printing conventions are resolved
to the form below; any other difference stops the merge and is printed."""
import os,glob,re,sys
R='/tmp/claude-0/-home-claude/d70938a1-c1e3-53dc-bc4c-599e8ff01633/scratchpad/kjv'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'kjv_all.txt')
def load(p):
    d={}
    for ln in open(p,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if ln.strip() and '\t' in ln:
            n,t=ln.split('\t',1); d[int(n)]=t.strip()
    return d
def canon(s):
    s=s.replace('æ','ae').replace('Æ','Ae').replace('-','').replace('’',"'")
    s=re.sub(r'[.:;,]+$','',s)
    return s.lower()
codes=sorted({os.path.basename(f)[:-4] for f in glob.glob(f'{R}/A/*.txt')})
lines=[];problems=0
for c in codes:
    a=load(f'{R}/A/{c}.txt'); b=load(f'{R}/B/{c}.txt')
    if c=='Ps_45': a[1]=re.sub(r'^\([^)]*\)\s*','',a[1])
    for v in sorted(a):
        ta=a[v]; tb=b.get(v)
        if tb is None: print('MISSING in B',c,v); problems+=1; continue
        if ta!=tb and canon(ta)!=canon(tb):
            # LORD small caps: B keeps LORD, take B's capitalisation when only case of Lord differs
            if re.sub(r'\bLORD\b','Lord',tb)==ta or canon(ta.replace('Lord','LORD'))==canon(tb):
                ta=tb
            else:
                print('REAL DIFF',c,v); print('  A:',ta); print('  B:',tb); problems+=1
        elif ta!=tb and 'LORD' in tb and 'LORD' not in ta:
            ta=tb  # keep small-caps LORD
        lines.append(f'{c}\t{v}\t{ta}')
open(OUT,'w',encoding='utf-8').write('\n'.join(lines)+'\n')
print('wrote',OUT,len(lines),'verses;',problems,'problems')
