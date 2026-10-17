#!/usr/bin/env python3
"""Covers for the Parable Study Template and its Worked Example. Usage: python3 mkcovers.py <art_template.png> <art_example.png> <outdir>
Art is the publisher's supplied 5120x7680 (2:3); output 1600x2400 PNG/JPG plus 1024x1536 jpg/webp for the site."""
import sys,os,cv2,numpy as np
from PIL import Image,ImageDraw,ImageFont
B='/root/.fonts/Roboto-Bold.ttf'; R='/root/.fonts/Roboto-Regular.ttf'
NAVY=(27,51,80); WHITE=(255,255,255); GOLD=(232,184,72)
def base(src,top_dark=0.0):
    im=cv2.imread(src); im=cv2.resize(im,(1600,2400),interpolation=cv2.INTER_AREA).astype(np.float32)
    H=2400
    if top_dark:
        dark=np.array([24,14,10],np.float32); g=np.clip(1-np.arange(H)/(H*0.36),0,1)**1.1; al=(top_dark*g)[:,None,None]; im=im*(1-al)+dark*al
    g2=np.clip((np.arange(H)-H*0.93)/(H*0.07),0,1)[:,None,None]*0.55
    im=im*(1-g2)+np.array([20,20,20],np.float32)*g2
    return Image.fromarray(cv2.cvtColor(np.clip(im,0,255).astype(np.uint8),cv2.COLOR_BGR2RGB))
def ct(d,y,t,size,fill,font=B,shadow=None):
    f=ImageFont.truetype(font,size); w=d.textlength(t,font=f)
    if shadow: d.text(((1600-w)/2+3,y+4),t,font=f,fill=shadow)
    d.text(((1600-w)/2,y),t,font=f,fill=fill)
def make(src,out,dark,sub_lines,subfill):
    img=base(src,0.8 if dark else 0.0); d=ImageDraw.Draw(img)
    f=ImageFont.truetype(B,34); t='PARABLES'; w=d.textlength(t,font=f); d.text((1600-w-100,80),t,font=f,fill=WHITE if dark else NAVY)
    tf=WHITE if dark else NAVY; sh=(0,0,0) if dark else None
    ct(d,190,'PARABLE STUDY',150,GOLD if dark else NAVY,B,sh); ct(d,360,'TEMPLATE',150,GOLD if dark else NAVY,B,sh)
    y=570
    for s,sz in sub_lines: ct(d,y,s,sz,subfill,B if dark else R,sh); y+=sz+22
    ct(d,2290,'DIGITAL STUDIES SERIES',40,WHITE,B)
    img.save(out+'_1600x2400.png'); j=img.convert('RGB'); j.save(out+'_1600x2400.jpg',quality=94)
    s=img.resize((1024,1536),Image.LANCZOS).convert('RGB'); s.save(out+'_1024.jpg',quality=88,optimize=True); s.save(out+'_1024.webp',quality=82)
if __name__=='__main__':
    a,b,o=sys.argv[1:4]; os.makedirs(o,exist_ok=True)
    make(a,o+'/template',False,[('A Guided Worksheet for Reading',50),('Any Parable in Its Gospel Setting',50)],NAVY)
    make(b,o+'/example',True,[('Worked Example:',56),('The Wedding Banquet (Matthew 22:1–14)',56)],WHITE)
