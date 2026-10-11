"""Verify transcribed KJV chapters against the SHA-256 hashes computed in the browser from the source page.
usage: python3 verify_raw.py raw_a.txt [raw_b.txt ...]   (header line: '## Code_ch N hash')"""
import sys,hashlib,re
ok=bad=0
for f in sys.argv[1:]:
    cur=None;rows=[];hdr=None
    def flush():
        global ok,bad
        if hdr is None: return
        code,n,h=hdr
        body='\n'.join(rows)
        got=hashlib.sha256(body.encode('utf-8')).hexdigest()
        good=(got==h and len(rows)==int(n))
        print(('OK  ' if good else 'BAD ')+code,len(rows),'/',n)
        ok+=good; bad+=(not good)
    for ln in open(f,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if ln.startswith('## '):
            flush(); p=ln[3:].split(); hdr=(p[0],p[1],p[2]); rows=[]
        elif ln.strip(): rows.append(ln)
    flush(); hdr=None
print('verified',ok,'chapters;',bad,'bad')
sys.exit(1 if bad else 0)
