#!/usr/bin/env python3
"""Remove the 'Made with AI' badge from the top-right corner of supplied cover art.
usage: python3 remove_ai_badge.py <in.png> <out.png>
The frame ornament is mirror-symmetric, so the badge area is rebuilt from the mirrored left side (mirror offset found by matching the frame), feathered at the edges."""
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
a=np.array(Image.open(sys.argv[1]).convert('RGB')).astype(np.float32); H,W,_=a.shape
L=a.mean(axis=2)
best=None
for dx in range(-300,301,2):
    c0=W-700+dx; c1=W-60+dx
    if c0<0 or c1>W: continue
    d=np.abs(L[int(H*.055):int(H*.147),60:700]-L[int(H*.055):int(H*.147),c0:c1][:,::-1]).mean()
    if best is None or d<best[0]: best=(d,dx)
dx=best[1]; s=W/4096.0
x0,x1,y0,y1=int(3060*s),W-1,int(20*s),int(345*s)
xs=np.arange(x0,x1+1); src=(W-1+dx)-xs
patch=a[y0:y1+1][:,src]
m=Image.new('L',(x1-x0+1,y1-y0+1),0); ImageDraw.Draw(m).rectangle((14,14,x1-x0-1,y1-y0-14),fill=255); m=m.filter(ImageFilter.GaussianBlur(9))
mk=np.array(m)[...,None]/255.0
out=a.copy(); out[y0:y1+1,x0:x1+1]=patch*mk+a[y0:y1+1,x0:x1+1]*(1-mk)
Image.fromarray(np.clip(out,0,255).astype(np.uint8)).save(sys.argv[2]); print('dx',dx,'score',round(float(best[0]),1))
