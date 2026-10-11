import cv2,numpy as np
from PIL import Image,ImageDraw,ImageFont
SRC='/root/.claude/uploads/616c96b2-28fa-501c-be7f-d13c7668caf0/1bf9b011-image.png'
src=cv2.imread(SRC)
h0,w0=src.shape[:2]; s=1600/w0; ah=round(h0*s)
art=cv2.resize(src,(1600,ah),interpolation=cv2.INTER_AREA).astype(np.float32)
H=2400; top=H-ah
canvas=np.zeros((H,1600,3),np.float32)
canvas[top:]=art
ext=cv2.GaussianBlur(cv2.flip(art[:top+40],0),(0,0),25)
canvas[:top]=ext[:top]
dark=np.array([24,14,10],np.float32)   # BGR navy-ish dark
g=np.clip(1-np.arange(H)/(H*0.42),0,1)**1.2
al=(0.80*g)[:,None,None]; canvas=canvas*(1-al)+dark*al
g2=np.clip((np.arange(H)-H*0.90)/(H*0.10),0,1)[:,None,None]*0.7
canvas=canvas*(1-g2)+dark*g2
img=Image.fromarray(cv2.cvtColor(np.clip(canvas,0,255).astype(np.uint8),cv2.COLOR_BGR2RGB))
d=ImageDraw.Draw(img);W=1600
B='/root/.fonts/Roboto-Bold.ttf';gold=(232,184,72);white=(255,255,255)
F=lambda s:ImageFont.truetype(B,s)
def ct(y,t,f,fill,sh=True):
    w=d.textlength(t,font=f)
    if sh:d.text(((W-w)/2+3,y+4),t,font=f,fill=(0,0,0))
    d.text(((W-w)/2,y),t,font=f,fill=fill)
f=F(34);t='PASSAGES';w=d.textlength(t,font=f);d.text((W-w-100,80),t,font=f,fill=white)
ct(170,'MARRIAGE AND',F(150),gold)
ct(340,'SINGLENESS',F(150),gold)
ct(560,'1 Corinthians 7 in Its Own Setting',F(58),white)
ct(660,'Whose Word Each Instruction Is',F(36),white)
ct(2290,'DIGITAL STUDIES SERIES',F(40),white,False)
img.save('cover_1600x2400.png')
img.convert('RGB').save('cover_supplied.jpg',quality=94)
img.resize((320,480),Image.LANCZOS).save('proof_320x480.png')
img.resize((800,1200),Image.LANCZOS).save('proof_800.jpg',quality=92)
print(img.size,top)
