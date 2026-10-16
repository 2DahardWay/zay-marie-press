import cv2,numpy as np
from PIL import Image,ImageDraw,ImageFont
SRC='art1600.png'  # the publisher's supplied art, resized to 1600x2400 (original 5120x7680 upscayl)
src=cv2.imread(SRC); h0,w0=src.shape[:2]
# crop to 2:3 then resize
nh=round(w0*1.5)
if nh<=h0: y0=(h0-nh)//2; src=src[y0:y0+nh]
else: nw=round(h0/1.5); x0=(w0-nw)//2; src=src[:,x0:x0+nw]
H=2400;W=1600
canvas=cv2.resize(src,(W,H),interpolation=cv2.INTER_AREA).astype(np.float32)
dark=np.array([24,14,10],np.float32)
g=np.clip(1-np.arange(H)/(H*0.36),0,1)**1.1
al=(0.78*g)[:,None,None]; canvas=canvas*(1-al)+dark*al
g2=np.clip((np.arange(H)-H*0.90)/(H*0.10),0,1)[:,None,None]*0.75
canvas=canvas*(1-g2)+dark*g2
img=Image.fromarray(cv2.cvtColor(np.clip(canvas,0,255).astype(np.uint8),cv2.COLOR_BGR2RGB))
d=ImageDraw.Draw(img)
B='/root/.fonts/Roboto-Bold.ttf';gold=(232,184,72);white=(255,255,255)
F=lambda s:ImageFont.truetype(B,s)
def ct(y,t,f,fill,sh=True):
    w=d.textlength(t,font=f)
    if sh:d.text(((W-w)/2+3,y+4),t,font=f,fill=(0,0,0))
    d.text(((W-w)/2,y),t,font=f,fill=fill)
f=F(34);t='DOCTRINAL THEMES';w=d.textlength(t,font=f);d.text((W-w-100,80),t,font=f,fill=white)
ct(200,'THE LAST DAYS',F(158),gold)
ct(420,'Where Scripture Uses the Phrase, of Whom Each',F(46),white)
ct(490,'Passage Speaks, and What It Leaves Unsaid',F(46),white)
ct(2290,'DIGITAL STUDIES SERIES',F(40),white,False)
img.save('cover_1600x2400.png')
img.convert('RGB').save('cover_supplied.jpg',quality=94)
img.resize((320,480),Image.LANCZOS).save('proof_320x480.png')
img.resize((800,1200),Image.LANCZOS).save('proof_800.jpg',quality=92)
