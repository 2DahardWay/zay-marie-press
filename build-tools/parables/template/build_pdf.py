#!/usr/bin/env python3
"""Builds the two Parable Study Template PDFs (reportlab). Usage: python3 build_pdf.py <outdir>
Page 483.846 x 725.754 pt (9677 x 14515 twips); margins L/R 1031, top 864, bottom 1224 twips; Roboto only."""
import sys, os
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import NextPageTemplate, PageBreak, BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Flowable, KeepTogether, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle
import content as C
from reportlab import rl_config
F=os.path.join(HERE,'..','..','..','fonts')
for n,f in (('Roboto','Regular'),('Roboto-Bold','Bold'),('Roboto-Italic','Italic'),('Roboto-BoldItalic','BoldItalic')):
    pdfmetrics.registerFont(TTFont(n,os.path.join(F,'Roboto-%s.ttf'%f)))
rl_config.canvas_basefontname='Roboto'
pdfmetrics.registerFontFamily('Roboto',normal='Roboto',bold='Roboto-Bold',italic='Roboto-Italic',boldItalic='Roboto-BoldItalic')
TW=20
W,H=9677/TW,14515/TW; LM=RM=1031/TW; TM=864/TW; BM=1224/TW
NAVY=HexColor('#1B3350'); RULE=HexColor('#B9C4CF'); BOX=HexColor('#3B6E91')
FOOT='ZAY-MARIE PRESS PARABLE STUDIES SERIES'
IMPRINT=("Copyright © 2026 Alexander S. Marien. All rights reserved. Published by Zay-Marie Press. Licensed for the personal use of the purchaser; "
 "no part may be reproduced or distributed without permission. Scripture quotations are from the King James Version (KJV).")
body=ParagraphStyle('b',fontName='Roboto',fontSize=10,leading=10*1.2,spaceAfter=6,textColor=black)
hint=ParagraphStyle('h',parent=body,fontName='Roboto-Italic',fontSize=9,leading=11,spaceAfter=4)
lab=ParagraphStyle('l',parent=body,fontName='Roboto-Bold',spaceAfter=2,keepWithNext=1)
h1=ParagraphStyle('h1',fontName='Roboto-Bold',fontSize=14,leading=17,textColor=NAVY,spaceBefore=12,spaceAfter=8,keepWithNext=1)
ttl=ParagraphStyle('t',fontName='Roboto-Bold',fontSize=20,leading=24,textColor=NAVY,spaceAfter=4)
sub=ParagraphStyle('s',fontName='Roboto-Italic',fontSize=11,leading=14,spaceAfter=3)
imp=ParagraphStyle('i',parent=body,fontSize=9,leading=11,spaceBefore=16)
imph=ParagraphStyle('ih',fontName='Roboto-Bold',fontSize=10,textColor=NAVY,spaceBefore=18,spaceAfter=3,keepWithNext=1)
class Lines(Flowable):
    """Writing box: border + ruled lines."""
    def __init__(s,h): Flowable.__init__(s); s.h=h
    def wrap(s,aw,ah): s.w=aw; return aw,s.h
    def draw(s):
        c=s.canv; c.setStrokeColor(BOX); c.setLineWidth(.75); c.rect(0,0,s.w,s.h)
        c.setStrokeColor(RULE); c.setLineWidth(.5); y=s.h-18
        while y>6: c.line(8,y,s.w-8,y); y-=18
class Field(Flowable):
    def __init__(s,label,answer): Flowable.__init__(s); s.label=label; s.answer=answer
    def wrap(s,aw,ah): s.w=aw; return aw,26
    def draw(s):
        c=s.canv; c.setFont('Roboto-Bold',10); c.drawString(0,8,s.label); x=pdfmetrics.stringWidth(s.label,'Roboto-Bold',10)+6
        c.setStrokeColor(RULE); c.setLineWidth(.6); c.line(x,5,s.w,5)
        if s.answer: c.setFont('Roboto',10); c.drawString(x+2,8,s.answer)
def listflow(items,kind):
    li=[]
    for it in items:
        t=it[1] if it[0]!='b2' else '<b>%s</b> %s'%(it[1],it[2])
        li.append(ListItem(Paragraph(t,ParagraphStyle('li',parent=body,spaceAfter=0)),leftIndent=18))
    kw=dict(bulletType='1' if kind=='n' else 'bullet',leftIndent=18,bulletFontName='Roboto',bulletFontSize=10)
    if kind!='n': kw['start']='•'
    else: kw['bulletFormat']='%s.'
    return ListFlowable(li,**kw)
def answer_flow(lines):
    fl=[];buf=[];kind=None
    def flush():
        nonlocal buf,kind
        if buf: fl.append(listflow(buf,kind)); fl.append(Spacer(1,6)); buf=[];kind=None
    for it in lines:
        k=None if isinstance(it,str) or it[0]=='q' else ('n' if it[0]=='n' else 'b')
        if k is None:
            flush(); fl.append(Paragraph(it,body) if isinstance(it,str) else Paragraph(it[1],ParagraphStyle('q',parent=body,fontName='Roboto-Italic',leftIndent=14)))
        else:
            if kind not in (None,k): flush()
            kind=k; buf.append(it)
    flush(); return fl
def build(out,title,subt,note,sections,example,cover=None):
    def foot(c,d):
        c.saveState(); c.setFont('Roboto',8.5); c.drawCentredString(W/2,BM-24,'%s • %d'%(FOOT,d.page-1)); c.restoreState()
    doc=BaseDocTemplate(out,pagesize=(W,H),leftMargin=LM,rightMargin=RM,topMargin=TM,bottomMargin=BM,title=title.title() if False else subt if example else title,
        author='Alexander S. Marien',subject='Zay-Marie Press Parable Studies Series')
    def covpage(c,d):
        if cover: c.drawImage(cover,0,0,W,H)
    doc.addPageTemplates([PageTemplate(id='cov',frames=[Frame(0,0,10,10)],onPage=covpage)])
    doc.addPageTemplates([PageTemplate(id='p',frames=[Frame(LM,BM,W-LM-RM,H-TM-BM,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=foot)])
    s=[NextPageTemplate('p'),PageBreak(),Paragraph(title,ttl),Paragraph(subt,sub)]
    if note: s.append(Paragraph(note,hint))
    for head,items in sections:
        block=[Paragraph(head,h1)]; first=True
        for it in items:
            k=it[0]; part=[]
            if k=='field': part=[Field(it[1],it[2])]
            elif k=='box':
                part=[Paragraph(it[1],lab)]
                if it[2]: part.append(Paragraph(it[2],hint))
                part+= [Lines(it[4]),Spacer(1,8)]
            elif k=='ans':
                if it[1]: part.append(Paragraph(it[1],lab))
                part+=answer_flow(it[3])
            elif k=='note': part=[Paragraph(it[1],body)]
            elif k=='quote': part=[Paragraph(it[1],ParagraphStyle('q',parent=body,fontName='Roboto-Italic',leftIndent=14))]
            elif k=='rule': part=[Paragraph('<b>%s</b> %s'%(it[1],it[2]),body)]
            if first: s.append(KeepTogether(block+part)); first=False
            elif k=='ans' and len(it[3])>=7: s.extend(part)
            else: s.append(KeepTogether(part))
    s.append(KeepTogether([Paragraph('Zay-Marie Press',imph),Paragraph(IMPRINT,imp)]))
    doc.build(s)
if __name__=='__main__':
    o=sys.argv[1]; cv=sys.argv[2]; os.makedirs(o,exist_ok=True)
    build(os.path.join(o,'zay-marie-press-parable-study-template.pdf'),C.TEMPLATE_TITLE,C.TEMPLATE_SUB,C.TEMPLATE_NOTE,C.T(),False,os.path.join(cv,'template_1600x2400.jpg'))
    build(os.path.join(o,'zay-marie-press-parable-study-template-worked-example.pdf'),C.EXAMPLE_TITLE,C.EXAMPLE_SUB,None,C.E(),True,os.path.join(cv,'example_1600x2400.jpg'))
