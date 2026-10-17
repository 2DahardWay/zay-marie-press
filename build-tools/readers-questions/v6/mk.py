import sys,os,asyncio
from playwright.sync_api import sync_playwright
from pypdf import PdfReader,PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from PIL import Image,ImageDraw,ImageFont
import io
D=sys.argv[1]; F='/home/claude/zay-marie-press/fonts'
W,H=483.846,725.754
pdfmetrics.registerFont(TTFont('Rob',F+'/Roboto-Regular.ttf'))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto('file://'+D+'/v6.html'); pg.wait_for_timeout(500)
    pg.pdf(path=D+'/body.pdf',print_background=True,prefer_css_page_size=True)
    b.close()
# cover placeholder
im=Image.open(D+'/reader-questions-06-cover-1600.png').convert('RGB'); d=ImageDraw.Draw(im)
fb=lambda s:ImageFont.truetype(F+'/Roboto-Bold.ttf',s)
im.save(D+'/cover.jpg',quality=92)
c=canvas.Canvas(D+'/cover.pdf',pagesize=(W,H),initialFontName='Rob'); c.drawImage(D+'/cover.jpg',0,0,W,H); c.save()
body=PdfReader(D+'/body.pdf'); n=len(body.pages)
out=PdfWriter(); out.add_page(PdfReader(D+'/cover.pdf').pages[0])
for i,pgx in enumerate(body.pages,1):
    buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=(W,H),initialFontName='Rob'); c.setFont('Rob',8); c.setFillColor(HexColor('#000000'))
    c.drawCentredString(W/2,28,f'ZAY-MARIE PRESS READERS QUESTION SERIES, VOLUME 6 • {i}'); c.save(); buf.seek(0)
    pgx.merge_page(PdfReader(buf).pages[0]); out.add_page(pgx)
out.write(open(D+'/reader-questions-06-review.pdf','wb')); print('pages with cover',n+1)
