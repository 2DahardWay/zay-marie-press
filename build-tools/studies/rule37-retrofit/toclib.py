import re,subprocess,docx
def norm(s): return re.sub(r'[^A-Za-z0-9]+','',s.replace('“','"').replace('”','"').replace('’',"'")).lower()
def pagelines(pdf):
    n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
    return [[norm(l) for l in subprocess.run(['pdftotext','-f',str(i),'-l',str(i),pdf,'-'],capture_output=True,text=True).stdout.split('\n') if l.strip()] for i in range(1,n+1)]
def toc_paras(d):
    ps=d.paragraphs; out=[]
    for p in ps[2:]:
        if p.style.name.startswith('Heading'): break
        if '\t' in p.text: out.append(p)
    return out
def compute(pdf,titles):
    pg=pagelines(pdf); res={}; cur=3
    for t in titles:
        k=norm(t); k20=k[:22]
        found=None
        for i in range(cur,len(pg)+1):
            lines=pg[i-1]
            # heading line must start with the first chunk, and full heading must be contained in joined text of the next lines
            for j,l in enumerate(lines):
                if l.startswith(k20) or (len(l)>=12 and k.startswith(l) and len(l)>=8 and l==k[:len(l)] and ''.join(lines[j:j+3]).startswith(k)):
                    if ''.join(lines[j:j+3]).startswith(k): found=i;break
            if found: break
        res[t]=found; cur=found or cur
    return res
