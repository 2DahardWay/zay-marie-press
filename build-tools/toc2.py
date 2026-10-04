import subprocess,re,sys
from docx import Document
N=int(sys.argv[1])
pg=[re.sub(r'\s+',' ',subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'conf.pdf','-'],capture_output=True,text=True).stdout) for i in range(1,N+1)]
d=Document('conf.docx'); prev=3; out=[]
for p in d.paragraphs[:45]:
    if '\t' in p.text and p.text.split('\t')[-1].strip().isdigit():
        t,n=p.text.split('\t'); k=re.sub(r'\s+',' ',t)[:26]
        act=next(i for i in range((3 if k.startswith('Introduction') else prev),N+1) if k in pg[i-1]); prev=act
        for r in reversed(p.runs):
            if re.search(r'\d+$',r.text): r.text=re.sub(r'\d+$',str(act),r.text); break
        out.append((t[:30],n,act))
for o in out: print(o)
d.save('conf.docx')
