"""Typographic placeholder cover for the interior review copy (the approved cover art replaces it)."""
import os
from PIL import Image, ImageDraw, ImageFont
import content
F=os.path.expanduser('~/.fonts/')
def font(n,s): return ImageFont.truetype(F+n,s)
def wrap(d,text,f,maxw):
    words=text.split(); lines=[];cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=f)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines
def make(path):
    W,H=1600,2400
    im=Image.new('RGB',(W,H),(18,38,63)); d=ImageDraw.Draw(im)
    # minimalist geometric: two thin concentric circles and a vertical rule
    cx,cy=W//2,1000
    for r,wd in ((520,3),(430,2)):
        d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(176,196,222),width=wd)
    d.line([(cx,cy-620),(cx,cy+620)],fill=(176,196,222),width=2)
    d.line([(cx-620,cy),(cx+620,cy)],fill=(176,196,222),width=2)
    lab='VOLUME %d'%content.META['vol']; fl=font('Roboto-Bold.ttf',54)
    d.text((W-110-d.textlength(lab,font=fl),110),lab,font=fl,fill=(236,241,247))
    ft=font('Roboto-Bold.ttf',150); y=1720
    for ln in wrap(d,content.META['title'],ft,W-260):
        d.text(((W-d.textlength(ln,font=ft))/2,y),ln,font=ft,fill=(255,255,255)); y+=180
    fs=font('Roboto-Bold.ttf',46); s=content.META['series'].upper()
    d.text(((W-d.textlength(s,font=fs))/2,H-170),s,font=fs,fill=(236,241,247))
    im.save(path)
if __name__=='__main__': make('cover_placeholder.png')
