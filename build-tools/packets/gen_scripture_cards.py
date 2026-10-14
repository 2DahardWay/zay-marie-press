import glob,importlib,sys,os,re,html
sys.path.insert(0,'/home/claude/zay-marie-press/build-tools/packets')
AB={'1 Chr.':'1 Chronicles','2 Chr.':'2 Chronicles','1 Cor.':'1 Corinthians','2 Cor.':'2 Corinthians','1 Kgs.':'1 Kings','2 Kgs.':'2 Kings','1 Pet.':'1 Peter','2 Pet.':'2 Peter','1 Sam.':'1 Samuel','2 Sam.':'2 Samuel','1 Thess.':'1 Thessalonians','2 Thess.':'2 Thessalonians','1 Tim.':'1 Timothy','2 Tim.':'2 Timothy','Col.':'Colossians','Dan.':'Daniel','Deut.':'Deuteronomy','Eccl.':'Ecclesiastes','Eph.':'Ephesians','Esth.':'Esther','Ex.':'Exodus','Ezek.':'Ezekiel','Gal.':'Galatians','Gen.':'Genesis','Hab.':'Habakkuk','Hag.':'Haggai','Heb.':'Hebrews','Hos.':'Hosea','Isa.':'Isaiah','Jer.':'Jeremiah','Josh.':'Joshua','Judg.':'Judges','Lam.':'Lamentations','Lev.':'Leviticus','Mal.':'Malachi','Matt.':'Matthew','Mic.':'Micah','Nah.':'Nahum','Neh.':'Nehemiah','Num.':'Numbers','Obad.':'Obadiah','Phil.':'Philippians','Philem.':'Philemon','Prov.':'Proverbs','Ps.':'Psalm','Rev.':'Revelation','Rom.':'Romans','Song':'Song of Solomon','Zech.':'Zechariah','Zeph.':'Zephaniah'}
SINGLE={'Obadiah','Philemon','2 John','3 John','Jude'}
def full(ref):
    parts=[]
    for g in ref.split(';'):
        g=g.strip()
        for a in sorted(AB,key=len,reverse=True):
            if g.startswith(a+' ') or g.startswith(a+' '): g=AB[a]+g[len(a):]; break
        parts.append(g)
    return '; '.join(parts)
def key(ref,single):
    m=re.search(r'(\d+):(\d+)',ref)
    if m: return (int(m.group(1)),int(m.group(2)))
    m=re.search(r'(?:^|\D)(\d+)(?!\d*\s*(?:John|Cor|Kings|Chr|Sam|Pet|Thess|Tim))',ref.split(' ',1)[1] if ' ' in ref else ref)
    n=int(re.findall(r'\d+',ref.split(' ',1)[1] if ' ' in ref else ref)[0]) if re.findall(r'\d+',ref.split(' ',1)[1] if ' ' in ref else ref) else 0
    return (1,n) if single else (n,0)
def pick(rows,k):
    if k>=len(rows): return list(rows)
    if k<=0: return []
    idx=sorted({round(i*(len(rows)-1)/(k-1)) if k>1 else 0 for i in range(k)})
    i=0
    while len(idx)<k:
        if i not in idx: idx.append(i)
        i+=1
    return [rows[j] for j in sorted(idx)]
def cards(mod):
    r7=[];r8=[]
    for n,t,b in mod.SECTIONS:
        for x in b:
            if x[0]=='table' and n==7: r7=[(r[0],r[-1]) for r in x[2]]
            if x[0]=='table' and n==8: r8=[(r[0],r[-1]) for r in x[2]]
    k8=min(len(r8),3)
    k7=min(len(r7),8-k8); k8=min(len(r8),8-k7)
    sel=pick(r7,k7)+pick(r8,k8)
    seen=set(); out=[]
    for cat,ref in sel:
        if ref in seen: continue
        seen.add(ref); out.append((cat,ref))
    for cat,ref in r7+r8:
        if len(out)>=8: break
        if ref not in seen: seen.add(ref); out.append((cat,ref))
    single=mod.BOOK in SINGLE
    out.sort(key=lambda c:key(c[1],single))
    return out
def render(c):
    return '<div class="scripture-grid">'+''.join(f'<div class="scripture-card"><h3>{html.escape(full(ref),quote=False)}</h3><p>{html.escape(cat.rstrip("."),quote=False)}.</p></div>' for cat,ref in c)+'</div>'
if __name__=='__main__':
    only=sys.argv[1:]
    for f in sorted(glob.glob('/home/claude/zay-marie-press/packet-*.html')):
        slug=os.path.basename(f)[7:-5]
        if only and slug not in only: continue
        mod=None
        for n in ['content_'+slug.replace('-',''),'content_'+slug.replace('-','').replace('chronicles','chr')]:
            if os.path.exists(f'/home/claude/zay-marie-press/build-tools/packets/{n}.py'): mod=importlib.import_module(n); break
        c=cards(mod); assert len(c)>=7,(slug,len(c))
        if len(c)<8: print("short",slug,len(c))
        s=open(f,encoding='utf-8').read()
        s2,k=re.subn(r'<div class="scripture-grid">(?:<div class="scripture-card">.*?</div>)+</div>',lambda m:render(c),s,count=1,flags=re.S)
        assert k==1,slug
        open(f,'w',encoding='utf-8').write(s2)
        if only: print(slug,[ (full(r),t) for t,r in c])
