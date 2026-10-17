import sys,os,re,html,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import kjvlib
from c1 import ENTRIES as E1
from c2 import ENTRIES as E2
E=E1+E2
import rev; rev.apply(E)
VOL=6
OUT=sys.argv[1] if len(sys.argv)>1 else '.'
FONTS='/home/claude/zay-marie-press/fonts'
TITLE_Q=[e['title']+' ('+e['sub']+')' for e in E]
def esc(s): return s
def kjvcell(ref):
    parts=[p.strip() for p in ref.split(';')]
    return ' … '.join('“'+kjvlib.text(p)+'”' for p in parts)
def kjvtable(e):
    rows=''.join(f'<tr><td class="v">{html.escape(r[0])}</td><td>{kjvcell(r[1])}</td><td>{r[2]}</td></tr>' for r in e['rows'])
    return f'<table><tr><th style="width:17%">Verse</th><th style="width:50%">KJV text</th><th>What to observe</th></tr>{rows}</table>'
def entry(e):
    h=[f'<h1 style="margin-bottom:2pt">{e["title"]}</h1><p style="font-style:italic;margin:0 0 8pt 0">{e["sub"]}</p>']
    h.append(f'<table class="call"><tr><td><div class="ct">THE ANSWER</div>{e["answer"]}</td></tr></table>')
    h.append('<h2>Where the Verses Stand</h2>'+''.join(f'<p>{p}</p>' for p in e['stand']))
    h.append(kjvtable(e))
    h.append('<h2>What Carries the Weight</h2>'+''.join(f'<p class="li"><b>{t}:</b> {x}</p>' for t,x in e['carry']))
    h.append('<h2>The Other Readings</h2>'+''.join(f'<p class="li">{x}</p>' for x in e['other']))
    h.append('<table class="rt"><tr><th style="width:24%">Reading</th><th style="width:40%">What it must say</th><th>Where it strains</th></tr>'+''.join(f'<tr><td class="v">{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in e['rtbl'])+'</table>')
    h.append('<h2>What It Means for the Reader</h2>'+''.join(f'<p>{p}</p>' for p in e['means']))
    h.append('<h2>Related Reading</h2><p>'+e['related']+'</p>')
    return '\n'.join(h)
def short(t):  # contents line
    return t
BIB=[
"Heiser, Michael S. <i>The Unseen Realm: Recovering the Supernatural Worldview of the Bible</i>. Bellingham, WA: Lexham Press, 2015.",
"Morse, Greg. “‘Oh Slay the Wicked.’” Desiring God, September 6, 2023. desiringgod.org/articles/oh-slay-the-wicked.",
"Neyrey, Jerome H. “‘I Said: You Are Gods’: Psalm 82:6 and John 10.” <i>Journal of Biblical Literature</i> 108, no. 4 (1989): 647–63.",
]
IMPR="Copyright © 2026 Alexander S. Marien. All rights reserved. Published by Zay-Marie Press. Free for the personal use of the reader; no part may be reproduced or distributed without permission. Scripture quotations are from the King James Version (KJV)."
css=f'''
@font-face{{font-family:R;src:url("file://{FONTS}/Roboto-Regular.ttf");font-weight:400}}
@font-face{{font-family:R;src:url("file://{FONTS}/Roboto-Bold.ttf");font-weight:700}}
@font-face{{font-family:R;src:url("file://{FONTS}/Roboto-Italic.ttf");font-weight:400;font-style:italic}}
@font-face{{font-family:R;src:url("file://{FONTS}/Roboto-BoldItalic.ttf");font-weight:700;font-style:italic}}
@page{{size:483.846pt 725.754pt;margin:43.2pt 51.55pt 61.2pt 51.55pt}}
body{{font-family:R;font-size:10pt;color:#000;line-height:1.08;margin:0;text-align:left}}
p{{margin:0 0 6pt 0}} p.li{{margin:0 0 6pt 0}}
h1{{font-size:17pt;color:#1B3350;font-weight:700;margin:12pt 0 8pt 0;line-height:1.1;break-after:avoid}}
h2{{font-size:12pt;color:#1B3350;font-weight:700;margin:10pt 0 5pt 0;break-after:avoid}}
.ct{{font-size:10pt;color:#1B3350;font-weight:700;margin:0 0 4pt 0}}
table{{border-collapse:collapse;width:100%;margin:10pt 0;table-layout:fixed}}
th{{background:#3B6E91;color:#fff;font-weight:700;text-align:left;padding:3pt 4pt;border:.5pt solid #3B6E91}}
td{{background:#fff;padding:3pt 4pt;border:.5pt solid #3B6E91;vertical-align:top;font-size:10pt}}
td.v{{font-weight:700}}
tr{{break-inside:avoid}} table.rt tr{{break-inside:avoid}} tr:first-child{{break-after:avoid}} table.rt{{break-inside:avoid}}
table.call td{{border:1pt solid #1B3350;background:#EAF1F8;padding:6pt 8pt}}
.pb{{break-before:page}}
.imp{{margin-top:14pt}}
'''
toc=''.join(f'<p style="margin:0 0 6pt 0">{t}</p>' for t in TITLE_Q)
front=f'''<div style="text-align:left"><p style="font-size:24pt;color:#1B3350;font-weight:700;margin:8pt 0 2pt 0">Reader Questions</p>
<p style="font-size:14pt;color:#1B3350;font-weight:700;margin:0 0 14pt 0">Volume 6: Questions on Difficult Bible Verses</p></div>
<h1 style="font-size:12pt;margin-top:10pt">HOW TO READ THIS VOLUME</h1>
<p>Each entry takes one question a reader has asked about one verse or short passage. This volume takes ten questions on psalms that the New Testament quotes. Each entry states what the verse means, and then argues that meaning from the verse’s own passage and the chapter or chapters before it. The Scripture elsewhere is used as support, not as the foundation. Each entry marks what the text states, what the context shows, and what is inferred, so that the reader can see what carries the weight and judge it. The entries argue a position. Where other readings are held by named writers, they are set beside it with the places where each strains.</p>
<p>Scripture is quoted from the King James Version (KJV). Modern writers are named by author and work; their views are described in the entry’s own words, and no quotation marks are used for them.</p>
<h2>Contents</h2>{toc}'''
body=front+''.join(f'<div class="pb">{entry(e)}</div>' if i==0 else f'<div class="pb">{entry(e)}</div>' for i,e in enumerate(E))
idx=[]
for i,e in enumerate(E,1):
    for r in e['rows']:
        for ref in r[1].split(';'): idx.append((ref.strip().replace('–','-'),i,ref.strip()))
rows=''.join(f'<tr><td class="v">{html.escape(x[2])}</td><td>Entry {x[1]}</td></tr>' for x in idx)
body+='<div class="pb"><h1>Passages Quoted in This Volume</h1><p>Each passage is printed in full in the KJV table of the entry named.</p><table><tr><th style="width:60%">Passage</th><th>Where it is read</th></tr>'+rows+f'</table><p class="imp">{IMPR}</p></div>'
open(f'{OUT}/v6.html','w').write(f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')
