# -*- coding: utf-8 -*-
import json,re,sys,html
sys.path.insert(0,'.')
from kjv import get
import content as C

def esc(s): return html.escape(s,quote=False)
def norm(t): return re.sub(r'[^a-z0-9 ]','',re.sub(r'[“”‘’"\'—–-]',' ',t.lower())).split()

# ---- build data with passage texts
data=[];errs=[]
for st in C.ST:
    d={k:st[k] for k in ('id','num','band','title','short','when','where','reading','presides','judged','ground','outcome','silent')}
    d['more']=st['more']; d['roles']={}
    for pid,_ in C.PARTS:
        r=st['roles'][pid]; d['roles'][pid]=list(r) if r[1] or r[0]!='X' else ['X','']
    corpus=[]
    ps=[]
    for ref,tag,note,spec in st['passages']:
        vs=[]
        for b,ch,a,z in spec:
            got=get(b,ch,a,z)
            if len(got)!=z-a+1: errs.append(f'{st["id"]} {ref}: verses missing')
            vs+=[{'v':v,'t':t,'c':ch} for v,t in got]
        corpus+= [x['t'] for x in vs]
        ps.append({'ref':ref,'tag':tag,'note':note,'vs':vs})
    d['passages']=ps
    if 'features' in st:
        fs=[]
        for f in st['features']:
            fp=[]
            for ref,spec in f['passages']:
                vs=[]
                for b,ch,a,z in spec:
                    got=get(b,ch,a,z)
                    if len(got)!=z-a+1: errs.append(f'{st["id"]} feature {ref}: verses missing')
                    vs+=[{'v':v,'t':t,'c':ch} for v,t in got]
                corpus+=[x['t'] for x in vs]
                fp.append({'ref':ref,'vs':vs})
            fs.append({'name':f['name'],'refs':f['refs'],'line':f['line'],'passages':fp,'note':f.get('note','')})
        d['features']=fs
    # quote check: every “...” fragment in reading/outcome/ground/judged/passage notes/roles must be in station corpus
    big=' '.join(norm(' '.join(corpus)))
    texts=[st['reading'],st['outcome'],st['ground'],st['judged'],st['when'],st['where']]+[p[2] for p in st['passages']]+[r[1] for r in st['roles'].values()]+st['silent']
    for t in texts:
        for q in re.findall(r'“([^”]+)”',t):
            qn=' '.join(norm(q))
            if qn and qn not in big: errs.append(f'{st["id"]}: quote not in station KJV: “{q}”')
    data.append(d)
if errs:
    print('\n'.join(errs))
json.dump(data,open('data.json','w'),ensure_ascii=False)
print('stations',len(data),'errs',len(errs))
