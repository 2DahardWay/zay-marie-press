from pathlib import Path
import re
from lxml import html, etree

root=Path(__file__).parent
def replace_one(s,old,new):
    assert s.count(old)==1,(old,s.count(old))
    return s.replace(old,new,1)

p=root/'digital-studies.html';s=p.read_text()
s=s.replace('Explore 54 Zay-Marie Press Digital Studies','Explore 55 Zay-Marie Press Digital Studies')
s=s.replace('data-count="studies">54<','data-count="studies">55<')
s=s.replace('all 54 studies. See','all 55 studies. See')
card='<article class="study-card"><div class="study-type">Study 55 · Biblical Doctrine</div><h3><a href="study-55-reconciled-to-god.html" style="color:inherit;text-decoration:none">Reconciled to God</a></h3><p>How do former enemies receive peace with God? Follow Paul’s account of Christ’s reconciling work, the entrusted appeal, peace in one Body, and the reach of “all things,” while keeping reconciliation distinct from redemption and justification.</p><div class="study-meta"><span class="study-price">$5.99</span><a class="study-action" href="study-55-reconciled-to-god.html" style="text-decoration:none">Preview Study</a></div></article>'
end='<a class="study-action" href="study-54-justification.html" style="text-decoration:none">Preview Study</a></div></article></div>'
s=replace_one(s,end,end.replace('</div>', '</div>',1).replace('</article></div>','</article>'+card+'</div>'))
p.write_text(s)

entry='''<details class="guide-entry" id="study-55"><summary><span class="entry-top">STUDY 55</span><span class="entry-title">Reconciled to God</span></summary><div class="entry-body"><p class="entry-intro"><strong>What this study answers.</strong> Study 55 follows Paul’s account of former enmity, God’s reconciling work in Christ, peace received, and the appeal entrusted to ambassadors. It reads Romans 5, 2 Corinthians 5, Ephesians 2, and Colossians 1 without turning the breadth of the message into universal personal reception.</p><h4>How the connected studies help</h4><div class="guide-link"><a href="study-53-redemption.html">Study 53 — Redemption</a><p>Identify the bondage and price named by redemption before asking the different relational question of what peace Christ’s work establishes.</p></div><div class="guide-link"><a href="study-54-justification.html">Study 54 — Justification</a><p>Establish the verdict received by faith in Romans 3–5; then see why Romans 5:1 calls peace with God its present result.</p></div><div class="guide-link"><a href="study-37-what-does-paul-mean-by-new-creation.html">Study 37 — What Does Paul Mean by “New Creation”?</a><p>Read 2 Corinthians 5:17 in its own setting so the following reconciliation passage is connected to, but not substituted for, Paul’s new-creation claim.</p></div><div class="guide-link"><a href="study-52-sonship-and-adoption.html">Study 52 — Sonship and Adoption</a><p>Compare reconciliation’s answer to enmity and peace with adoption’s distinct question of sonship and inheritance.</p></div><div class="entry-footer"><a href="study-55-reconciled-to-god.html">Preview Study 55 →</a><a href="#study-number-index">Study index ↑</a></div></div></details>'''
p=root/'study-connections.html';s=p.read_text()
s=s.replace('all 54 studies','all 55 studies').replace('Browse all 54 studies','Browse all 55 studies')
s=replace_one(s,'aria-label="Study 54: Justification">54</a></nav>','aria-label="Study 54: Justification">54</a><a href="#study-55" aria-label="Study 55: Reconciled to God">55</a></nav>')
s=replace_one(s,'id="study-54"', 'id="study-54"') if False else s
pos=s.index('<details class="guide-entry" id="study-54">')
end=s.index('</details>',pos)+len('</details>')
s=s[:end]+entry+s[end:]
s=replace_one(s,'THEME 1 · 17 STUDIES','THEME 1 · 18 STUDIES')
s=replace_one(s,'How do you identify the people of God and their distinct covenant claims? · 17 studies','How do you identify the people of God and their distinct covenant claims? · 18 studies') if 'How do you identify the people of God and their distinct covenant claims? · 17 studies' in s else s
# The theme card count is a separate visible span; update its exact current text.
s=s.replace('· 17 studies</span></a>','· 18 studies</span></a>',1)
for n,anchor in [(53,'study-53-redemption.html'),(54,'study-54-justification.html')]:
    opening=f'<details class="guide-entry" id="study-{n}">'; start=s.index(opening);end=s.index('</details>',start)
    addition='<div class="guide-link"><a href="study-55-reconciled-to-god.html">Study 55 — Reconciled to God</a><p>Follow the distinct question of former enmity and peace with God after identifying '+('redemption’s price.' if n==53 else 'justification’s verdict.')+'</p></div>'
    at=s.index('<div class="entry-footer">',start,end)
    s=s[:at]+addition+s[at:]
p.write_text(s)

for n,extra in [(53,'<p><a href="study-55-reconciled-to-god.html">Study 55 — Reconciled to God</a> Follow Christ’s work into the distinct question of former enmity and peace with God, which redemption’s price makes possible.</p>'),(54,'<p><a href="study-55-reconciled-to-god.html">Study 55 — Reconciled to God</a> Romans 5:1 joins the verdict received by faith to its relational result: peace with God.</p>')]:
    p=next(root.glob(f'study-{n:02d}-*.html'));s=p.read_text()
    anchor='<p class="connection-guide-link">'
    assert s.count(anchor)==1
    s=s.replace(anchor,extra+anchor,1);p.write_text(s)

p=root/'sitemap.xml';s=p.read_text()
url='<url><loc>https://zaymariepress.com/study-55-reconciled-to-god.html</loc></url>'
assert 'study-55-reconciled-to-god' not in s
s=s.replace('</urlset>',url+'</urlset>');p.write_text(s)
