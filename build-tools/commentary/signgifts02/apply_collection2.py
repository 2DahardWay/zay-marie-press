"""Add Sign Gifts Series Volume 2 to commentary.html (strip card, series intro, fit row, index, tile). Run from the repo root once. Bundle and Library price unchanged until the series is complete."""
p='commentary.html'; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep('<span>1 volume so far</span><em>55 pages · series in progress</em>','<span>2 volumes so far</span><em>110 pages · series in progress</em>')
rep('1 VOLUME AVAILABLE','2 VOLUMES AVAILABLE')
rep('Volume 1 asks what signs were for, to whom they were given and what ended at Acts 28. More volumes will follow.','Volume 1 asks what signs were for, to whom they were given and what ended at Acts 28; Volume 2 asks what tongues and prophecy are and whether they continue in the Body. More volumes will follow.')
rep('What were signs for, to whom were they given, and what ended at Acts 28?','What were signs for, to whom were they given, what are tongues and prophecy, and what ended at Acts 28?')
rep('<li><a href="commentary-sign-gifts-01-the-sign-gifts.html">The Sign Gifts</a></li></ol>','<li><a href="commentary-sign-gifts-01-the-sign-gifts.html">The Sign Gifts</a></li><li><a href="commentary-sign-gifts-02-tongues-and-prophecy.html">Tongues and Prophecy</a></li></ol>')
tile=('<div class="vol-tile"><a href="commentary-sign-gifts-02-tongues-and-prophecy.html"><picture><source srcset="assets/sign-gifts-02-cover-card.webp" type="image/webp"><img src="assets/sign-gifts-02-cover-card.jpg" alt="Tongues and Prophecy cover" loading="lazy" width="400" height="600"></picture></a>'
 '<div class="vol-no">Volume 2</div><h3>Tongues and Prophecy</h3><p class="vol-blurb">Paul writes of tongues and prophecy in three chapters, and Luke records tongues at Jerusalem, at Caesarea and at Ephesus. The volume reads 1 Corinthians 12 to 14 with Isaiah 28 and the three instances in Acts, and argues that the tongues are languages given as a sign to unbelieving Israel, that the Corinthian gifts belong to the overlap and end with the national suspension at Acts 28, and that no present practice of tongues is the biblical gift. It states plainly that the end of prophecy is an inference, names modern writers on both sides, and rules on each objection.</p>'
 '<p class="vol-meta">$14.99 · 55 pages</p><a class="vol-link" href="commentary-sign-gifts-02-tongues-and-prophecy.html">View Volume 2 →</a><a class="vol-sample" aria-label="Read a sample of Tongues and Prophecy" href="commentary-sign-gifts-02-tongues-and-prophecy.html#look-inside">Read a sample →</a></div>')
rep('Read a sample →</a></div></div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section><section class="detail','Read a sample →</a></div>'+tile+'</div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section><section class="detail')
open(p,'w',encoding='utf-8').write(s)
m='sitemap.xml'; t=open(m,encoding='utf-8').read(); a='<url><loc>https://zaymariepress.com/commentary-sign-gifts-01-the-sign-gifts.html</loc></url>'
assert t.count(a)==1; t=t.replace(a,a+'<url><loc>https://zaymariepress.com/commentary-sign-gifts-02-tongues-and-prophecy.html</loc></url>'); open(m,'w',encoding='utf-8').write(t); print('ok')
