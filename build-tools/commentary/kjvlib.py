import os,re
HERE=os.path.dirname(os.path.abspath(__file__))
ALIAS={'gen':'Gen','deut':'Deut','ps':'Ps','psalm':'Ps','isa':'Isa','jer':'Jer','ezek':'Ezek','hos':'Hos','joel':'Joel',
 'matt':'Matt','mark':'Mark','luke':'Luke','john':'John','rom':'Rom','2cor':'2Cor','gal':'Gal','eph':'Eph','col':'Col',
 'heb':'Heb','1pet':'1Pet','rev':'Rev'}
V={}   # (code,ch,v)->text
def _load():
    for ln in open(os.path.join(HERE,'kjv_all.txt'),encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln: continue
        c,v,t=ln.split('\t',2); b,ch=c.rsplit('_',1); V[(b,int(ch),int(v))]=t
_load()
def code(book): return ALIAS[book.replace(' ','').lower()]
def parse(ref):
    """'Isa 54:5–6, 8; Rev 19:7' -> list of (code,ch,v). Raises KeyError if verse not in corpus."""
    out=[];book=None;ch=None
    for part in re.split(r'\s*;\s*',ref.strip()):
        m=re.match(r'^((?:\d\s?)?[A-Za-z]+)\s+(\d+):(.+)$',part)
        if m: book=code(m.group(1)); ch=int(m.group(2)); rest=m.group(3)
        else:
            m2=re.match(r'^(\d+):(.+)$',part)
            if m2: ch=int(m2.group(1)); rest=m2.group(2)
            else: rest=part
        for seg in re.split(r'\s*,\s*',rest):
            mm=re.match(r'^(\d+)(?:\s*[–-]\s*(\d+))?$',seg.strip())
            if not mm: raise ValueError(f'bad ref segment {seg!r} in {ref!r}')
            a=int(mm.group(1)); b=int(mm.group(2) or a)
            for v in range(a,b+1):
                if (book,ch,v) not in V: raise KeyError(f'{book} {ch}:{v} not in corpus')
                out.append((book,ch,v))
    return out
def text(ref): return ' '.join(V[k] for k in parse(ref))
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','').replace('”','').replace('"','')
    s=s.replace('æ','ae').replace('—',' ').replace('–',' ').replace('-',' ')
    s=re.sub(r"[^A-Za-z0-9' ]+",' ',s)
    return re.sub(r'\s+',' ',s).strip().lower()
_CORPUS=None
def corpus():
    global _CORPUS
    if _CORPUS is None:
        chs={}
        for (b,c,v),t in sorted(V.items()): chs.setdefault((b,c),[]).append(t)
        _CORPUS=' | '.join(' '.join(norm(x) for x in vs) for vs in chs.values())
        _CORPUS=' '+_CORPUS+' '
    return _CORPUS
def in_corpus(q):
    n=norm(q)
    return bool(n) and (' '+n+' ') in corpus()
def in_ref(q,ref):
    n=norm(q); body=' '+' '.join(norm(V[k]) for k in parse(ref))+' '
    return bool(n) and (' '+n+' ') in body
