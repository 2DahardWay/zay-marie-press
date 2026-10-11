"""Find the footer page number of every h1 in the rendered PDF -> toc.json. usage: tocmap.py file.pdf [--check]"""
import sys,os,re,json,subprocess
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import content
pdf=sys.argv[1]
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
pages=[]
for i in range(1,n+1):
    t=subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'-layout',pdf,'-'],capture_output=True,text=True).stdout
    pages.append([re.sub(r'\s+',' ',l).strip() for l in t.splitlines() if l.strip()])
titles=[e[1] for e in content.ALL if e[0]=='h1']
res={};missing=[]
for t in titles:
    found=None
    for i in range(2,n):                      # skip cover (index 0) and the TOC page (index 1)
        L=pages[i]
        for j,l in enumerate(L):
            if l==t or (j+1<len(L) and (l+' '+L[j+1])==t) or (j+2<len(L) and (l+' '+L[j+1]+' '+L[j+2])==t):
                found=i; break
        if found is not None: break
    if found is None: missing.append(t)
    else: res[t]=found       # pdf index i -> footer number = i  (cover is index 0, TOC index 1 = footer 1)
if '--check' in sys.argv:
    old=json.load(open(os.path.join(HERE,'toc.json')))
    print('TOC stable' if old==res and not missing else 'TOC CHANGED', 'missing:',missing)
else:
    json.dump(res,open(os.path.join(HERE,'toc.json'),'w'),indent=1)
    print('mapped',len(res),'headings; missing:',missing)
print('pdf pages:',n)
