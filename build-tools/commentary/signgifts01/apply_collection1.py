"""Add The Sign Gifts Series (Volume 1) to commentary.html as an in-progress series: strip card, jump item, fit row, index column, series section.
Counts, bundle and Library price stay as they are until the series is complete (Master Standard v1.168). Run from the repo root once."""
p='commentary.html'; s=open(p,encoding='utf-8').read()
def rep(a,b,count=1):
    global s
    assert s.count(a)==count,(a[:80],s.count(a)); s=s.replace(a,b)
rep('<em>223 pages · $43.99 bundle</em></a></div>','<em>223 pages · $43.99 bundle</em></a><a href="#sign-gifts"><strong>The Sign Gifts</strong><span>1 volume so far</span><em>55 pages · series in progress</em></a></div>')
rep('<li><a href="#prophets">Prophets</a></li>','<li><a href="#prophets">Prophets</a></li><li><a href="#sign-gifts">Sign Gifts</a></li>')
rep('<td><a href="#prophets">The Prophets Series</a></td></tr></tbody>','<td><a href="#prophets">The Prophets Series</a></td></tr><tr><td>What were signs for, to whom were they given, and what ended at Acts 28?</td><td><a href="#sign-gifts">The Sign Gifts Series</a></td></tr></tbody>')
rep('<li><a href="commentary-prophets-04-elijah-must-first-come.html">Elijah Must First Come</a></li></ol></div>','<li><a href="commentary-prophets-04-elijah-must-first-come.html">Elijah Must First Come</a></li></ol></div><div class="com-idx-col"><h3><a href="#sign-gifts">The Sign Gifts</a></h3><ol><li><a href="commentary-sign-gifts-01-the-sign-gifts.html">The Sign Gifts</a></li></ol></div>')
tile=('<div class="vol-tile"><a href="commentary-sign-gifts-01-the-sign-gifts.html"><picture><source srcset="assets/sign-gifts-01-cover-card.webp" type="image/webp"><img src="assets/sign-gifts-01-cover-card.jpg" alt="The Sign Gifts cover" loading="lazy" width="400" height="600"></picture></a>'
 '<div class="vol-no">Volume 1</div><h3>The Sign Gifts</h3><p class="vol-blurb">Scripture uses one set of words, sign, wonder, miracle and token, for what God does to mark a messenger, to move a nation and to answer a doubter. The volume reads each one for who gave it, who received it and what it was set to prove, from Exodus to Acts 28 and Paul’s own letters. It argues that the signs belonged to Israel’s line, that the last sign Acts records falls in chapter 28, and that signs do not continue into the Mystery. It names modern writers who hold that the gifts continue and others who hold that they ended, and rules on each objection.</p>'
 '<p class="vol-meta">$14.99 · 55 pages</p><a class="vol-link" href="commentary-sign-gifts-01-the-sign-gifts.html">View Volume 1 →</a><a class="vol-sample" aria-label="Read a sample of The Sign Gifts" href="commentary-sign-gifts-01-the-sign-gifts.html#look-inside">Read a sample →</a></div>')
sec=('<section class="set-series" id="sign-gifts"><div class="wrap"><div class="eyebrow">SERIES 10 · IN PROGRESS · 1 VOLUME AVAILABLE</div><h2>The Sign Gifts Series</h2>'
 '<p class="set-desc">A topic series built around one narrower question at a time about the signs of Scripture. Volume 1 asks what signs were for, to whom they were given and what ended at Acts 28. More volumes will follow.</p>'
 '<div class="vol-grid">'+tile+'</div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section>')
rep('</div></section><section class="detail-section com-intro" id="every-volume">','</div></section>'+sec+'<section class="detail-section com-intro" id="every-volume">')
open(p,'w',encoding='utf-8').write(s); print('ok')
