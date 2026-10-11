# -*- coding: utf-8 -*-
import json,re,sys
sys.path.insert(0,'.')
import stops as S, geo
from chk import text
def vs(ref):
    return [{'c':c,'v':v,'t':t} for c,v,t in text(ref)]
stops=[]
for i,t in enumerate(S.S,1):
    id,ph,lab,la,lo,loc,tags,refs,hap,sil=t
    stops.append(dict(id=id,n=i,ph=ph,label=lab,lat=la,lon=lo,loc=loc,tags=tags,happens=hap,silent=sil,
        passages=[{'ref':r,'vs':vs(r)} for r in refs]))
week=[dict(day=d,title=t,happens=h,passages=[{'ref':r,'vs':vs(r)} for r in refs]) for d,t,refs,h in S.WEEK]
ph=[dict(id=k,name=v[0],sub=v[1],color=v[2],quiet=v[3]) for k,v in S.PH.items()]
g=geo.build()
DATA=json.dumps(dict(stops=stops,week=week,weekSilent=S.WEEK_SILENT,glob=S.GLOBAL_SILENT,ph=ph,geo=g,
  proj=dict(lon0=geo.LON0,lat1=geo.LAT1,K=geo.K,C=geo.C,W=geo.W,H=geo.H)),ensure_ascii=False,separators=(',',':'))
TITLE="The Lord’s Ministry Route Map | Zay-Marie Press"
DESC="An interactive map of the Lord’s ministry in the Gospels, from Nazareth and Capernaum through the Galilean circuits and the feasts in Jerusalem to the final road, with what happens at each stop and the passages in the KJV."
CSS=open('page.css',encoding='utf-8').read()
JS=open('page.js',encoding='utf-8').read().replace('__DATA__',DATA)
BODY=open('body.html',encoding='utf-8').read()
HTML=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>{TITLE}</title><meta name="description" content="{DESC}"/><link rel="canonical" href="https://zaymariepress.com/jesus-ministry-map.html"/><link rel="icon" href="assets/zay-marie-press-favicon.png" type="image/png"/><style>{CSS}</style><meta property="og:type" content="website"><meta property="og:site_name" content="Zay-Marie Press"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{DESC}"><meta property="og:url" content="https://zaymariepress.com/jesus-ministry-map.html"><meta property="og:image" content="https://zaymariepress.com/assets/share-site-default.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{TITLE}"><meta name="twitter:description" content="{DESC}"><meta name="twitter:image" content="https://zaymariepress.com/assets/share-site-default.jpg">
</head><body>{BODY}<script>{JS}</script></body></html>"""
open('jesus-ministry-map.html','w',encoding='utf-8').write(HTML)
print(len(HTML),'bytes; stops',len(stops))
