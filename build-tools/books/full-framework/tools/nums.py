import subprocess,json,re,sys
pdf=sys.argv[1]; titles=json.load(open('titles.json'))
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
pages=[]
for i in range(1,n+1):
    t=subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'-layout',pdf,'-'],capture_output=True,text=True).stdout
    lines=[l.strip() for l in t.split('\n') if l.strip()]
    pages.append(lines)
def label(l): return l[-1] if l else ''
res={}
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).strip()
tocpages=set()
for i,l in enumerate(pages):
    if len(l)>1 and norm(l[1])=='Table of Contents' : tocpages.add(i)
    # TOC continuation pages: lines with dot leaders
    if sum('....' in x for x in l)>10: tocpages.add(i)
for t in titles:
    nt=norm(t)
    for i,l in enumerate(pages):
        if i in tocpages and nt!='Table of Contents': continue
        if i==0: continue
        # heading is first content line (after running head) possibly wrapped
        head=norm(' '.join(l[1:4]))
        if head.startswith(nt) or (len(l)>1 and norm(l[1])==nt):
            if nt=='Table of Contents' and i in tocpages and not norm(l[1])==nt: continue
            res[t]=label(l); break
    else: res[t]='??'
json.dump(res,open('nums.json','w'),ensure_ascii=False,indent=0)
print(n,'pages');
for t in titles: print(res[t],'|',t[:60])
