from PIL import Image,ImageDraw,ImageFont
R='/home/claude/zay-marie-press/assets/'
bg=Image.open(R+'share-acts-overlap-visual-guide.jpg').getpixel((5,5))
F='/usr/share/fonts/truetype/dejavu/'
def f(n,s): return ImageFont.truetype(F+n,s)
GOLD=(212,175,55);WH=(255,255,255);MU=(150,170,196)
def base(eyebrow,title_lines,sub):
    im=Image.new('RGB',(1200,630),bg);d=ImageDraw.Draw(im)
    d.text((90,118),eyebrow,font=f('DejaVuSans-Bold.ttf',24),fill=(196,160,96))
    y=165
    for t in title_lines:
        d.text((90,y),t,font=f('DejaVuSerif-Bold.ttf',50),fill=WH);y+=66
    d.text((90,y+14),sub,font=f('DejaVuSerif.ttf',27),fill=MU)
    return im,d
# search page: a search box with a verse range and one result line
im,d=base('ZAY-MARIE PRESS · FREE RESOURCE',['Search the New Testament’s','Use of the Old Testament'],'Both KJV texts side by side, with what each verse marks')
d.rounded_rectangle((90,400,1110,470),radius=14,outline=GOLD,width=3,fill=(12,26,48))
d.text((120,418),'acts 28:26-27',font=f('DejaVuSans-Bold.ttf',30),fill=WH)
d.rounded_rectangle((90,495,1110,560),radius=12,fill=(20,34,58),outline=(50,67,95),width=2)
d.rectangle((90,495,96,560),fill=GOLD)
d.text((120,510),'Acts 28:25–27  ←  Isaiah 6:9–10',font=f('DejaVuSerif-Bold.ttf',26),fill=WH)
im.save(R+'share-ot-in-nt-quotations.jpg',quality=90)
# guide: two stacked bars NT <- OT
im,d=base('ZAY-MARIE PRESS · FREE RESOURCE',['The New Testament’s Use','of the Old Testament'],'How, where and why the writers reach back into Israel’s Scriptures')
d.text((90,410),'OLD TESTAMENT',font=f('DejaVuSans-Bold.ttf',20),fill=GOLD)
d.rounded_rectangle((90,440,1090,466),radius=13,fill=GOLD)
d.text((390,495),'NEW TESTAMENT',font=f('DejaVuSans-Bold.ttf',20),fill=(100,160,255))
d.rounded_rectangle((390,525,1090,551),radius=13,fill=(47,128,237))
im.save(R+'share-new-testament-use-of-old-testament.jpg',quality=90)
