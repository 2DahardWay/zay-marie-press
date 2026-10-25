import json,re,subprocess,sys
pdf=sys.argv[1]; heads=json.load(open('heads.json'))
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
def norm(s): return re.sub(r'[^A-Za-z0-9]+','',s.replace('“','"').replace('”','"').replace('’',"'"))
pg=[norm(subprocess.run(['pdftotext','-f',str(i),'-l',str(i),pdf,'-'],capture_output=True,text=True).stdout) for i in range(1,n+1)]
out={};prev=3
for h in heads:
    k=norm(h)
    for i in range(prev,n+1):
        # skip TOC page (2) itself
        if i>=3 and k in pg[i-1]:
            out[h]=i-1; prev=i; break
    else: out[h]=0
json.dump(out,open('toc.json','w'),indent=1); print(out)
