import sys,json,re,subprocess,glob,os,docx
n=sys.argv[1]
src=glob.glob(f'/root/.claude/uploads/c0ed2e22-30fa-5e68-8953-7079a3cff252/*Study_{n}_*')[0]
os.makedirs(f'b{int(n):02d}',exist_ok=True)
out=f'b{int(n):02d}/els{int(n):02d}.json'
subprocess.run(['python3','convdocx.py',src,out],stdout=subprocess.DEVNULL)
d=docx.Document(src);s=d.sections[0];print(os.path.basename(src),round(s.page_width.pt,1),round(s.page_height.pt,1))
els=json.load(open(out))
T=lambda e:''.join(x[0] for x in e['segs'])
sec=None
for i,e in enumerate(els):
    if e['type']=='tbl': print(i,'TBL',e['rows'][0]);continue
    if e['kind']=='h1': sec=T(e); print(i,'H1',sec)
    if e['kind']=='ctitle': print(i,'  CT',T(e))
full='\n'.join(T(e) for e in els if e['type']=='para')
for w in ["Framework","PAM","Program Assignment","Master Standard","irewall","Rule [0-9]","anchor","Study #","finished work","shared ground","Israel of God","spiritual Israel","Romans 11","olive","Revelation","synagogue","gathered into","resum","→","□","framework","covenants still","believing Jew","Abrahamic","Hebrews 3"]:
    m=[full[max(0,x.start()-60):x.start()+80].replace('\n',' ') for x in re.finditer(w,full)]
    if m: print('GREP',w,len(m),m[:2])
i=[k for k,e in enumerate(els) if e['type']=='para' and T(e)=='What You Will Learn in This Study'][0]
for e in els[i+1:i+16]:
    if e['type']=='para': print(e['kind'],T(e)[:150])
