import re,json
lines=[l.replace('\f','') for l in open('c45/t.txt').read().split('\n')]
FOOT=re.compile(r'^\s*ZAY-MARIE PRESS DIGITAL STUDIES SERIES • Page \d+\s*$')
HEAD={"What You Will Learn in This Study","Study Goal","Study Outline","Introduction","Conclusion","Study Summary","Key Distinctions to Retain","Scripture-Tracing Exercise","Review and Discussion Questions","Teaching Outline","Guided Further Study","Final Synthesis","Comparing the Two Programs' Sanctification"}
NUMH=re.compile(r'^[1-8]\. (What “Sanctify”|Positional Sanctification: Already|Practical Sanctification: God|Romans 6: Fruit|Progressive Sanctification: Beholding|Israel\'s Holiness Under|A Common Confusion|Testing the Three)')
blocks=[]; cur=[]
def flush():
    global cur
    if cur: blocks.append(cur); cur=[]
n=len(lines)
for idx,l in enumerate(lines):
    if FOOT.match(l):
        pn=idx>0 and lines[idx-1].strip()!=''; nn=idx+1<n and lines[idx+1].strip()!=''
        if not(pn and nn): flush()
        continue
    if l.strip()=='': flush(); continue
    s=l.strip()
    if (s in HEAD or NUMH.match(s)) and not l.startswith('     '):
        flush(); blocks.append([l]); continue
    cur.append(l)
flush()
start=[k for k,b in enumerate(blocks) if len(b)==1 and b[0].strip()=='What You Will Learn in This Study'][-1]
B=blocks[start:]
def join(ls):
    t=''
    for l in ls:
        s=l.strip()
        if not t: t=s
        elif t.endswith('-') and not t.endswith(' -'): t+=s
        else: t+=' '+s
    return t
P=lambda k,t,b=False: dict(type='para',kind=k,segs=[[t,b,False]],p=0,x0=0)
els=[]; sec=None
def items(b,pat):
    its=[]
    for l in b:
        if re.match(pat,l): its.append([l])
        elif its: its[-1].append(l)
    return its
for b in B:
    f=b[0].strip()
    if len(b)==1 and (f in HEAD or NUMH.match(f)):
        if f=='Study Goal': sec=f; continue
        sec=f
        if f=="Comparing the Two Programs' Sanctification": els.append(P('body',f)); els.append(dict(type='tbl',rows=[['Basis',"Israel's Holiness (Law)","The Body's Sanctification (Grace)"],['Covenant ground','Mosaic covenant, Leviticus 20:7–8','Union with Christ, 1 Cor. 1:2, 30'],['Standard','The statutes of the Law','Apostolic instruction under grace, 1 Thess. 4:2, 8'],['Program','Prophecy Program, national','Mystery Program, the one Body'],['Reason given',"“For I am the LORD your God” (Lev. 20:7)","“God hath… given unto us his holy Spirit” (1 Thess. 4:8)"]],xs=[(0,110),(110,375),(375,640)])); continue
        els.append(P('h1',f)); continue
    if b[0].strip().startswith('Basis') or re.match(r'^ (Covenant ground|Standard|Program|Reason given)\s{3,}',b[0]): continue
    if f.startswith('ZAY-MARIE PRESS DIGITAL STUDIES') or f.startswith('© Zay'): continue
    if f=='STUDY GOAL':
        els.append(P('ctitle','STUDY GOAL',True)); els.append(P('cbody',join(b[1:]))); continue
    if b[0].startswith(' ') and not b[0].startswith('  ') and b[0].strip().isupper():
        els.append(P('ctitle',b[0].strip(),True)); els.append(P('cbody',join(b[1:]))); continue
    if sec=='What You Will Learn in This Study' or sec=='Key Distinctions to Retain' or sec=='Guided Further Study' and '●' in b[0]:
        for it in items(b,r'^\s*●'): els.append(P('bul',join(it).lstrip('●').strip()))
        continue
    if sec=='Study Outline':
        for it in items(b,r'^\d\. '): els.append(P('num',re.sub(r'^\d+\.\s*','',join(it))))
        continue
    if sec in('Scripture-Tracing Exercise','Review and Discussion Questions') and re.match(r'^\s*\d+\. ',b[0]) :
        for it in items(b,r'^\s*\d+\. '): els.append(P('num',re.sub(r'^\d+\.\s*','',join(it))))
        continue
    if sec=='Teaching Outline':
        its=items(b,r'^\s*([IVX]+|[A-D])\. ')
        for it in its:
            t=join(it); m=re.match(r'^([IVX]+)\. (.*)',t)
            if m: els.append(P('body',m.group(2),True))
            else:
                m=re.match(r'^([A-D])\. (.*)',t); els.append(dict(type='para',kind='body',segs=[[m.group(1)+'.\t',False,False],[m.group(2),False,False]],p=0,x0=0))
        continue
    els.append(P('bul' if sec=='Study Summary' and False else 'body',join(b)))
for e in els:
    if e['type']=='para':
        for s in e['segs']: s[0]=s[0].replace("'","’")
    else: e['rows']=[[c.replace("'","’") for c in r] for r in e['rows']]
json.dump(els,open('els45.json','w'),ensure_ascii=False)
for i,e in enumerate(els):
    if e['type']=='tbl': print(i,'TBL'); continue
    print(i,e['kind'],''.join(s[0] for s in e['segs'])[:80])
