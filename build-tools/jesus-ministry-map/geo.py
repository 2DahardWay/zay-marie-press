# -*- coding: utf-8 -*-
import json,math
import os
G=os.environ.get('NE_GEOJSON','geo/ne/geojson/')  # Natural Earth 10m GeoJSON folder (sparse clone of github.com/nvkelso/natural-earth-vector)
LON0,LON1,LAT0,LAT1=34.90,36.10,31.52,33.45
K=1000.0; C=math.cos(math.radians(32.5))
def P(lon,lat): return ((lon-LON0)*K*C,(LAT1-lat)*K)
W=(LON1-LON0)*K*C; H=(LAT1-LAT0)*K
def clip(ring):
    def cl(pts,inside,inter):
        out=[]
        for i in range(len(pts)):
            a,b=pts[i-1],pts[i]
            if inside(b):
                if not inside(a): out.append(inter(a,b))
                out.append(b)
            elif inside(a): out.append(inter(a,b))
        return out
    def ix(a,b,v): return (v,a[1]+(b[1]-a[1])*(v-a[0])/(b[0]-a[0]))
    def iy(a,b,v): return (a[0]+(b[0]-a[0])*(v-a[1])/(b[1]-a[1]),v)
    pts=[tuple(p[:2]) for p in ring]
    for ins,it in [(lambda p:p[0]>=LON0,lambda a,b:ix(a,b,LON0)),(lambda p:p[0]<=LON1,lambda a,b:ix(a,b,LON1)),(lambda p:p[1]>=LAT0,lambda a,b:iy(a,b,LAT0)),(lambda p:p[1]<=LAT1,lambda a,b:iy(a,b,LAT1))]:
        if not pts: break
        pts=cl(pts,ins,it)
    return pts
def path(rings):
    d=''
    for r in rings:
        r=clip(r)
        if len(r)<3: continue
        d+='M'+'L'.join('%.1f,%.1f'%P(*p) for p in r)+'Z'
    return d
def polys(f,name=None):
    out=[]
    for ft in json.load(open(G+f))['features']:
        if name and ft['properties'].get('name')!=name: continue
        g=ft['geometry']
        if not g: continue
        ps=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
        for p in ps:
            for r in p:
                xs=[q[0] for q in r];ys=[q[1] for q in r]
                if max(xs)<LON0 or min(xs)>LON1 or max(ys)<LAT0 or min(ys)>LAT1: continue
                out.append(r)
    return out
def lines(f,name):
    d=''
    for ft in json.load(open(G+f))['features']:
        if ft['properties'].get('name')!=name or not ft['geometry']: continue
        g=ft['geometry']; ls=g['coordinates'] if g['type']=='MultiLineString' else [g['coordinates']]
        for l in ls:
            seg=[]
            for p in l+[None]:
                if p and LON0<=p[0]<=LON1 and LAT0<=p[1]<=LAT1: seg.append(p)
                else:
                    if len(seg)>1: d+='M'+'L'.join('%.1f,%.1f'%P(*q) for q in seg)
                    seg=[]
    return d
def build():
    return dict(land=path(polys('ne_10m_land.geojson')),galilee=path(polys('ne_10m_lakes.geojson','Sea of Galilee')),dead=path(polys('ne_10m_lakes.geojson','Dead Sea')),jordan=lines('ne_10m_rivers_lake_centerlines.geojson','Jordan'),W=W,H=H)
if __name__=='__main__':
    b=build(); print({k:(len(v) if isinstance(v,str) else v) for k,v in b.items()})
