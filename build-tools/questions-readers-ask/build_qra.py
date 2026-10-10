#!/usr/bin/env python3
"""Rebuild assets/zay-marie-press-questions-readers-ask.pdf from questions.md.
Roboto only (fonts/ must be installed for the footer: cp fonts/Roboto-*.ttf ~/.fonts && fc-cache -f).
Study page size 483.846 x 725.754 pt, margins 0.6in top / 0.85in bottom / 0.716in sides,
body Roboto 10 pt black, headings Roboto Bold 17 pt navy #1b3350, footer 'ZAY-MARIE PRESS DIGITAL STUDIES SERIES • N'.
Usage: python3 build_qra.py   (run from the repo root; needs playwright + chromium)"""
import re,html,os,sys
from playwright.sync_api import sync_playwright
ROOT=os.getcwd(); HERE=os.path.join(ROOT,'build-tools','questions-readers-ask')
OUT=os.path.join(ROOT,'assets','zay-marie-press-questions-readers-ask.pdf'); TMP=os.path.join(HERE,'_qra.html')
slugs={}
for f in os.listdir(ROOT):
    m=re.match(r'study-(\d\d)-.*\.html$',f)
    if m: slugs[int(m.group(1))]=f
md=open(os.path.join(HERE,'questions.md')).read(); cats=[];cur=None
for line in md.splitlines():
    if line.startswith('## '): cur=[line[3:].strip(),[]];cats.append(cur)
    m=re.match(r'(\d+)\. (.*) → (\d+) (.*)$',line)
    if m: cur[1].append((int(m.group(1)),m.group(2),int(m.group(3)),m.group(4)))
total=sum(len(q) for _,q in cats)
blurbs={'Foundations':'How is Scripture built, and how should it be read?','Israel & Prophecy':'Who are Israel, the remnant and the covenant people, and what does prophecy say?','Body of Christ':'What is the Mystery, and how does it shape life now?','Passages':'What does one passage or tight cluster actually say?','Doctrinal Themes':'How does one doctrine or term run across Scripture?'}
CSS=''.join('@font-face{font-family:Roboto;font-weight:%d;font-style:%s;src:url("file://%s")}'%(w,st,os.path.join(ROOT,'fonts','Roboto-%s.ttf'%n)) for n,w,st in (('Regular',400,'normal'),('Bold',700,'normal'),('Italic',400,'italic'),('BoldItalic',700,'italic')))
CSS+='''body{font:400 10pt/1.08 Roboto,sans-serif;color:#000;margin:0}p{margin:0 0 6pt}
.kick{font:700 8pt Roboto;color:#1b3350;letter-spacing:.04em;margin:0 0 10pt}h1{font:700 17pt Roboto;color:#1b3350;margin:0 0 4pt}
.sub{font:400 10pt Roboto;margin:0 0 10pt}hr{border:0;border-top:1px solid #1b3350;margin:8pt 0 10pt;break-after:avoid}
h2{font:700 17pt Roboto;color:#1b3350;margin:14pt 0 8pt;break-after:avoid}.q{margin:0 0 5pt;break-inside:avoid}.qt{font:700 10pt/1.08 Roboto}
.qa{margin:1pt 0 0 14pt;font:400 10pt Roboto}a{color:#1b3350;text-decoration:underline}.sec{margin-top:10pt}.sec:first-of-type{break-before:page;margin-top:0}
.note{font:400 10pt Roboto;margin:0 0 4pt;break-after:avoid}.idx p{margin:0 0 6pt}.idx b{font:700 10pt Roboto}'''
H='<!doctype html><meta charset="utf-8"><style>'+CSS+'</style>'
H+='<div class="kick">ZAY-MARIE PRESS | DIGITAL STUDIES SERIES</div><h1>Questions Readers Ask</h1><div class="sub">A starting-point guide to all %d Digital Studies</div><hr>'%total
H+='<p>Most readers do not begin with a study number. They begin with a question. This guide lists the questions readers bring to Scripture and points each one to the Digital Study that takes it up, so you can start where your question is.</p><p>Each entry gives the question and the study that examines it. Follow the linked title to preview that study on the website. Every study stands on its own, and none of these entries prescribes a reading order.</p><h2>Choose a Category</h2><div class="idx">'
for c,qs in cats: H+='<p><b>%s</b><br>%s Questions %d–%d.</p>'%(html.escape(c),html.escape(blurbs[c]),qs[0][0],qs[-1][0])
H+='<p class="note">To see how studies connect once you have begun, open the Study Connections Guide: <a href="https://zaymariepress.com/study-connections.html">zaymariepress.com/study-connections.html</a>. To browse every study by subject, visit <a href="https://zaymariepress.com/digital-studies.html">zaymariepress.com/digital-studies.html</a>.</p></div>'
for c,qs in cats:
    H+='<div class="sec"><h2>%s</h2><div class="note">%s</div><hr>'%(html.escape(c),html.escape(blurbs[c]))
    for n,q,sn,t in qs: H+='<div class="q"><div class="qt">%d. %s</div><div class="qa"><a href="https://zaymariepress.com/%s">Study %d — %s</a></div></div>'%(n,html.escape(q),slugs[sn],sn,html.escape(t))
    H+='</div>'
open(TMP,'w').write(H)
ftr='<div style="font-family:Roboto;font-size:8pt;color:#000;width:100%;text-align:center">ZAY-MARIE PRESS DIGITAL STUDIES SERIES • <span class="pageNumber"></span></div>'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.goto('file://'+TMP);pg.wait_for_timeout(500)
    pg.pdf(path=OUT,width='6.72in',height='10.08in',print_background=True,display_header_footer=True,header_template='<div></div>',footer_template=ftr,margin={'top':'0.6in','bottom':'0.85in','left':'0.716in','right':'0.716in'})
os.remove(TMP);print('wrote',OUT,total,'questions')
