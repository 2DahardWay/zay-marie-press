"""Add Sign Gifts Series Volume 3 to commentary.html (strip card, series intro, fit row, index, tile). Run from the repo root once. Bundle and Library price unchanged until the series is complete."""
p='commentary.html'; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep('<span>2 volumes so far</span><em>110 pages · series in progress</em>','<span>3 volumes so far</span><em>165 pages · series in progress</em>')
rep('2 VOLUMES AVAILABLE','3 VOLUMES AVAILABLE')
rep('Volume 2 asks what tongues and prophecy are and whether they continue in the Body. More volumes will follow.','Volume 2 asks what tongues and prophecy are and whether they continue in the Body; Volume 3 asks what healing is for and what the Body does with sickness. More volumes will follow.')
rep('what are tongues and prophecy, and what ended at Acts 28?','what are tongues and prophecy, what is healing for, and what ended at Acts 28?')
rep('<li><a href="commentary-sign-gifts-02-tongues-and-prophecy.html">Tongues and Prophecy</a></li></ol>','<li><a href="commentary-sign-gifts-02-tongues-and-prophecy.html">Tongues and Prophecy</a></li><li><a href="commentary-sign-gifts-03-healing-in-the-body.html">Healing in the Body</a></li></ol>')
tile=('<div class="vol-tile"><a href="commentary-sign-gifts-03-healing-in-the-body.html"><picture><source srcset="assets/sign-gifts-03-cover-card.webp" type="image/webp"><img src="assets/sign-gifts-03-cover-card.jpg" alt="Healing in the Body cover" loading="lazy" width="400" height="600"></picture></a>'
 '<div class="vol-no">Volume 3</div><h3>Healing in the Body</h3><p class="vol-blurb">Healing runs through Scripture from Exodus to James, and the passages that name it do not all say the same thing. The volume reads them in order and argues that healing in the Gospels and Acts 1 to 8 confirmed a messenger to Israel, that James 5 is Israel’s passage, that the gifts of healing belong to the Corinthian overlap and end with the sign-program at Acts 28, and that the letters to the Body meet sickness with prayer, care and the mercy of God. It states plainly that no verse states the end, names modern writers on both sides, and rules on each objection.</p>'
 '<p class="vol-meta">$14.99 · 55 pages</p><a class="vol-link" href="commentary-sign-gifts-03-healing-in-the-body.html">View Volume 3 →</a><a class="vol-sample" aria-label="Read a sample of Healing in the Body" href="commentary-sign-gifts-03-healing-in-the-body.html#look-inside">Read a sample →</a></div>')
rep('Read a sample →</a></div></div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section><section class="detail','Read a sample →</a></div>'+tile+'</div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section><section class="detail')
open(p,'w',encoding='utf-8').write(s)
m='sitemap.xml'; t=open(m,encoding='utf-8').read(); a='<url><loc>https://zaymariepress.com/commentary-sign-gifts-02-tongues-and-prophecy.html</loc></url>'
assert t.count(a)==1; t=t.replace(a,a+'<url><loc>https://zaymariepress.com/commentary-sign-gifts-03-healing-in-the-body.html</loc></url>'); open(m,'w',encoding='utf-8').write(t); print('ok')
