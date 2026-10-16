"""Add Volume 4 to commentary.html (strip, fit table, index, Prophets section). Run from the repo root once."""
import re
p='commentary.html'; s=open(p,encoding='utf-8').read()
def rep(a,b,count=1):
    global s
    assert s.count(a)==count,(a,s.count(a)); s=s.replace(a,b)
rep('<span>3 volumes so far</span><em>168 pages · series in progress</em>','<span>4 volumes so far</span><em>223 pages · series in progress</em>')
rep('<tr><td>What does each oracle against a nation say of its own ground, its term and its ending?</td><td><a href="#prophets">The Prophets Series</a></td></tr>',
    '<tr><td>What does each oracle against a nation say of its own ground, its term and its ending?</td><td><a href="#prophets">The Prophets Series</a></td></tr><tr><td>Who is the Elijah that Malachi says will be sent, and has the promise been met?</td><td><a href="#prophets">The Prophets Series</a></td></tr>')
rep('<li><a href="commentary-prophets-03-the-nations-judged.html">The Nations Judged</a></li></ol>','<li><a href="commentary-prophets-03-the-nations-judged.html">The Nations Judged</a></li><li><a href="commentary-prophets-04-elijah-must-first-come.html">Elijah Must First Come</a></li></ol>')
rep('SERIES 9 · IN PROGRESS · 3 VOLUMES AVAILABLE','SERIES 9 · IN PROGRESS · 4 VOLUMES AVAILABLE')
rep('Volume 3 asks what each oracle against a nation says of its own ground, term and ending. More volumes will follow.','Volume 3 asks what each oracle against a nation says of its own ground, term and ending. Volume 4 asks who the Elijah is that Malachi says will be sent, and whether the promise has been met. More volumes will follow.')
m=re.search(r'<div class="vol-tile"><a href="commentary-prophets-03-the-nations-judged.html">.*?#look-inside">Read a sample →</a></div>',s,re.S)
tile=('<div class="vol-tile"><a href="commentary-prophets-04-elijah-must-first-come.html"><picture><source srcset="assets/prophets-04-cover-card.webp" type="image/webp"><img src="assets/prophets-04-cover-card.jpg" alt="Elijah Must First Come cover" loading="lazy" width="400" height="600"></picture></a>'
 '<div class="vol-no">Volume 4</div><h3>Elijah Must First Come</h3><p class="vol-blurb">Malachi promises Elijah the prophet before the day of the LORD. Gabriel says John will go in the spirit and power of Elias, John says “I am not,” and the Lord says “if ye will receive it, this is Elias” and, after John’s death, “Elias truly shall first come.” The volume argues that these are three statements in three settings and that the text points to a further coming of Elijah before the day, in Israel’s line. It sets its reading beside modern writers who agree in part and others who hold the promise closed in John, and answers the objections by name.</p>'
 '<p class="vol-meta">$14.99 · 55 pages</p><a class="vol-link" href="commentary-prophets-04-elijah-must-first-come.html">View Volume 4 →</a><a class="vol-sample" aria-label="Read a sample of Elijah Must First Come" href="commentary-prophets-04-elijah-must-first-come.html#look-inside">Read a sample →</a></div>')
s=s[:m.end()]+tile+s[m.end():]
open(p,'w',encoding='utf-8').write(s); print('ok')
