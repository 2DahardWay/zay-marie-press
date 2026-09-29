from pathlib import Path
from xml.sax.saxutils import escape
from lxml import html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

root=Path(__file__).parent
site='https://zaymariepress.com/'
doc=html.parse(str(root/'study-connections.html'))
fonts='/usr/share/fonts/truetype/dejavu'
for name,file in [('GSans','DejaVuSans.ttf'),('GSansBold','DejaVuSans-Bold.ttf'),('GSerif','DejaVuSerif.ttf'),('GSerifBold','DejaVuSerif-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,f'{fonts}/{file}'))
pdfmetrics.registerFontFamily('GSans',normal='GSans',bold='GSansBold')
pdfmetrics.registerFontFamily('GSerif',normal='GSerif',bold='GSerifBold')
navy=HexColor('#082d45');green=HexColor('#143823');gold=HexColor('#b8871c');body=HexColor('#28322d')
styles={
 'kicker':ParagraphStyle('kicker',fontName='GSansBold',fontSize=8.3,leading=12,textColor=green,spaceAfter=10),
 'title':ParagraphStyle('title',fontName='GSansBold',fontSize=25,leading=30,textColor=green,spaceAfter=15,alignment=TA_CENTER),
 'subtitle':ParagraphStyle('subtitle',fontName='GSerif',fontSize=12.4,leading=18,textColor=navy,spaceAfter=15,alignment=TA_CENTER),
 'intro':ParagraphStyle('intro',fontName='GSerif',fontSize=10.2,leading=15.8,textColor=body,spaceAfter=13),
 'theme':ParagraphStyle('theme',fontName='GSansBold',fontSize=15,leading=20,textColor=green,spaceBefore=13,spaceAfter=8),
 'themeindex':ParagraphStyle('themeindex',fontName='GSansBold',fontSize=10.4,leading=15,textColor=navy,spaceBefore=12,spaceAfter=3),
 'indexbody':ParagraphStyle('indexbody',fontName='GSerif',fontSize=9.2,leading=13.5,textColor=body,spaceAfter=4),
 'entry':ParagraphStyle('entry',fontName='GSansBold',fontSize=10.8,leading=14.5,textColor=navy,spaceBefore=13,spaceAfter=5,keepWithNext=True),
 'entryintro':ParagraphStyle('entryintro',fontName='GSerif',fontSize=9.25,leading=13.8,textColor=body,spaceAfter=5),
 'link':ParagraphStyle('link',fontName='GSerif',fontSize=9.1,leading=13.5,textColor=body,leftIndent=12,firstLineIndent=-9,spaceAfter=4),
 'small':ParagraphStyle('small',fontName='GSerif',fontSize=8.5,leading=12.5,textColor=body,spaceAfter=5),
}
def tx(node):return ' '.join(node.text_content().split())
def P(text,style):return Paragraph(escape(text),styles[style])
def footer(canv,doc):
    canv.saveState();canv.setStrokeColor(gold);canv.setLineWidth(.4);canv.line(54,744,558,744);canv.line(54,48,558,48)
    canv.setFont('GSans',7.2);canv.setFillColor(navy);canv.drawString(54,753,'ZAY-MARIE PRESS  |  STUDY CONNECTIONS GUIDE')
    canv.drawString(54,36,'Digital Studies Series');canv.drawRightString(558,36,str(doc.page));canv.restoreState()
themes=[]
for s in doc.xpath('//section[starts-with(@id,"theme-")]'):
    title=tx(s.xpath('.//div[@class="theme-heading"]/h2')[0]);question=tx(s.xpath('.//div[@class="theme-heading"]/p')[0]);entries=[]
    for e in s.xpath('.//details[@class="guide-entry"]'):
        n=int(e.get('id').split('-')[1]);name=tx(e.xpath('./summary/span[@class="entry-title"]')[0]);intro=tx(e.xpath('.//p[@class="entry-intro"]')[0]);links=[]
        for item in e.xpath('.//div[@class="guide-link"]'):
            a=item.xpath('./a')[0];links.append((tx(a),a.get('href'),tx(item.xpath('./p')[0])))
        entries.append((n,name,intro,links))
    themes.append((title,question,entries))
nums_all=sorted(x[0] for t in themes for x in t[2])
TOTAL=len(nums_all)
assert nums_all==list(range(1,TOTAL+1)),'guide entries must cover studies 1..N exactly once'
story=[Spacer(1,54),P('ZAY-MARIE PRESS  |  DIGITAL STUDIES SERIES','kicker'),P('Study Connections Guide','title'),P(f'A question-based reading guide to all {TOTAL} Digital Studies','subtitle'),HRFlowable(width='100%',thickness=1.5,color=gold,spaceBefore=8,spaceAfter=20),P('Each study answers a defined question. This companion explains what a connected study adds, why that connection helps, and where to read next. Follow the linked titles to preview each study on the website.','intro'),P('Choose a Question','theme')]
for name,q,entries in themes:
    nums=', '.join(str(x[0]) for x in entries)
    story.extend([P(name,'themeindex'),P(f'{q} Studies {nums}.','indexbody')])
story.extend([Spacer(1,12),P('Study numbers identify catalog entries; they do not prescribe a single reading sequence. Every study remains available individually.','small'),PageBreak()])
for name,q,entries in themes:
    story.extend([P(name,'theme'),P(q,'intro'),HRFlowable(width='100%',thickness=.5,color=gold,spaceAfter=8)])
    for n,title,intro,links in entries:
        entry=[Paragraph(f'<link href="{site}study-connections.html#study-{n:02d}" color="#082d45"><b>Study {n} — {escape(title)}</b></link>',styles['entry']),P(intro,'entryintro')]
        for label,href,why in links:
            entry.append(Paragraph(f'• <link href="{site}{escape(href)}" color="#176b3a"><b>{escape(label)}</b></link> — {escape(why)}',styles['link']))
        story.append(KeepTogether(entry))
    story.append(Spacer(1,12))
out=root/'assets/zay-marie-press-study-connections-guide.pdf'
SimpleDocTemplate(str(out),pagesize=letter,rightMargin=54,leftMargin=54,topMargin=67,bottomMargin=63,title='Zay-Marie Press Study Connections Guide',author='Zay-Marie Press').build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
