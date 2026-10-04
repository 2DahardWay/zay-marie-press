import re,copy
from base import T
FOOT=re.compile(r'\s*\d*\s*ZAY-MARIE PRESS DIGITAL STUDIES SERIES\s*•\s*\d*\s*')
def mk(kind,segs,like=None):
    return dict(type='para',kind=kind,segs=segs,p=0,top=0,x0=0,lasttop=0,lastp=0)
def clean(els,n):
    for e in els:
        if e['type']=='para': e.setdefault('p',0); e.setdefault('x0',0)
    # drop TOC pages: start at first WYWL h1 after TOC
    i0=[i for i,e in enumerate(els) if e['type']=='para' and e['kind']=='h1' and T(e).startswith('What You Will Learn')][0]
    els=els[i0:]
    out=[]
    for e in els:
        if e['type']=='para':
            for s in e['segs']:
                s[0]=FOOT.sub(' ',s[0]); s[0]=s[0].replace("'","’")
            for s in e['segs']: s[0]=re.sub(r' {2,}',' ',s[0])
            if e['segs']: e['segs'][0][0]=e['segs'][0][0].lstrip(); e['segs'][-1][0]=e['segs'][-1][0].rstrip()
            e['segs']=[s for s in e['segs'] if s[0].strip()] or e['segs']
            if not T(e).strip(): continue
        out.append(e)
    els=out
    # swap cbody before ctitle; merge consecutive cbody
    i=0
    while i<len(els)-1:
        if els[i]['type']=='para' and els[i]['kind']=='cbody' and els[i+1]['type']=='para' and els[i+1]['kind']=='ctitle':
            els[i],els[i+1]=els[i+1],els[i]; i+=2; continue
        i+=1
    o=[]
    for e in els:
        if o and e['type']=='para' and e['kind']=='cbody' and o[-1]['type']=='para' and o[-1]['kind']=='cbody':
            o[-1]['segs'][-1][0]=o[-1]['segs'][-1][0].rstrip()+' '+e['segs'][0][0].lstrip()
        else: o.append(e)
    els=o
    # merge continuation 'body' lines after bul/num (hanging wraps)
    o=[]
    for e in els:
        if o and e['type']=='para' and e['kind']=='body' and o[-1]['type']=='para' and o[-1]['kind'] in('bul','num') and len(T(e))<130 and not re.match(r'^\d+\.\s',T(e)) and T(o[-1])[-1] not in '.?!”)':
            o[-1]['segs'][-1][0]=o[-1]['segs'][-1][0].rstrip()+' '+T(e).lstrip()
        elif o and e['type']=='para' and e['kind']=='body' and o[-1]['type']=='para' and o[-1]['kind'] in('bul','num') and len(T(e))<60 and T(e)[0].islower()==False and o[-1]['kind']=='bul' and not T(o[-1]).rstrip().endswith(('.','?','”')):
            o[-1]['segs'][-1][0]=o[-1]['segs'][-1][0].rstrip()+' '+T(e).lstrip()
        else: o.append(e)
    els=o
    # strip numerals from num items
    for e in els:
        if e['type']=='para' and e['kind']=='num':
            e['segs'][0][0]=re.sub(r'^(\d+|[IVX]+)\.\s+','',e['segs'][0][0])
    return els
def italics(els):
    for e in els:
        if e['type']!='para': continue
        new=[]
        for t,b,i in e['segs']:
            parts=re.split(r'\*([^*]+)\*',t)
            for k,p in enumerate(parts):
                if p: new.append([p,b,(k%2==1) or i])
        e['segs']=new
def to_bul(els,start,stop):
    # convert num items between headings to bullets
    on=False
    for e in els:
        if e['type']!='para': continue
        if e['kind']=='h1': on=T(e).startswith(start)
        elif on and e['kind']=='num': e['kind']='bul'
def kjv(els,after_h1,lead,rows):
    i=[k for k,e in enumerate(els) if e['type']=='para' and e['kind']=='h1' and T(e).startswith(after_h1)][0]
    els.insert(i+1,mk('body',[[lead,False,False]]))
    els.insert(i+2,dict(type='tbl',rows=[['Verse','KJV text','What to observe']]+rows,xs=[(0,135),(135,435),(435,640)]))
