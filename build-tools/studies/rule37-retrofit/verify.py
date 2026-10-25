import subprocess,re,sys,docx
sys.path.insert(0,'.')
from concl import C
for k in range(int(sys.argv[1]),int(sys.argv[2])+1):
    n='%02d'%k; pdf=f'pdf1/o{n}.pdf'
    t=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout
    flat=re.sub(r'\s+',' ',t); pages=t.split('\f'); c=re.sub(r'\s+',' ',C[n])
    imp=[i+1 for i,p in enumerate(pages) if 'Copyright' in p and 'ZAY-MARIE PRESS DIGITAL' in p]
    fonts=set(re.sub(r'.*\+|-.*','',l.split()[0]) for l in subprocess.run(['pdffonts',pdf],capture_output=True,text=True).stdout.splitlines()[2:] if l.strip())
    hits=re.findall(r'Framework|PAM\b|Program Assignment|Master Standard|firewall|Rule \d|Study Summary|Final Synthesis|[Aa]nchor',flat)
    body=flat[:flat.rfind('Conclusion')]; nb=re.sub(r'[^a-z0-9]+','',body.lower())
    miss=[q for q in re.findall(r'“([^”]+)”',C[n]) if re.sub(r'[^a-z0-9]+','',q.lower()) not in nb]
    d=docx.Document(f'o{n}.docx'); co=len([1 for t in d.tables if len(t.rows)==1 and len(t.columns)==1])
    print(n,'pp',len(pages)-1,'concl',c[:80] in flat and c[-80:] in flat,'imp',imp,fonts,hits,'qmiss',miss,'callouts',co)
