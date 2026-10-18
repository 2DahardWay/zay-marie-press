"""Add Sign Gifts Series Volume 4 and complete the series pricing on commentary.html, resources.html, sitemap.xml. Run once from the repo root."""
p='commentary.html'; s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a)); s=s.replace(a,b)
# series strip and section
rep('<span>3 volumes so far</span><em>165 pages · series in progress</em>','<span>4 volumes</span><em>217 pages · $43.99 bundle</em>')
rep('SERIES 10 · IN PROGRESS · 3 VOLUMES AVAILABLE','SERIES 10 · 4 VOLUMES')
rep('Volume 3 asks what healing is for and what the Body does with sickness. More volumes will follow.</p><div class="vol-grid">','Volume 3 asks what healing is for and what the Body does with sickness; Volume 4 asks what the offices of apostle and prophet are and whether they continue.</p><p class="set-buy">Own all four volumes: <strong>$43.99</strong> <span>save $15.97</span> · <a href="#bundle-sign-gifts">See the series bundle →</a></p><div class="vol-grid">')
rep('what are tongues and prophecy, what is healing for, and what ended at Acts 28?','what are tongues and prophecy, what is healing for, what are the offices of apostle and prophet, and what ended at Acts 28?')
rep('<li><a href="commentary-sign-gifts-03-healing-in-the-body.html">Healing in the Body</a></li></ol>','<li><a href="commentary-sign-gifts-03-healing-in-the-body.html">Healing in the Body</a></li><li><a href="commentary-sign-gifts-04-apostles-and-prophets.html">Apostles and Prophets</a></li></ol>')
tile=('<div class="vol-tile"><a href="commentary-sign-gifts-04-apostles-and-prophets.html"><picture><source srcset="assets/sign-gifts-04-cover-card.webp" type="image/webp"><img src="assets/sign-gifts-04-cover-card.jpg" alt="Apostles and Prophets cover" loading="lazy" width="400" height="600"></picture></a>'
 '<div class="vol-no">Volume 4</div><h3>Apostles and Prophets</h3><p class="vol-blurb">The New Testament names apostles and prophets and says the household of God is built upon their foundation, yet it uses “apostle” of the Twelve, of Paul and of sent ones such as Barnabas and Epaphroditus. The volume reads each passage in order and argues that the Twelve’s office is suspended with Israel’s program and resumes in the Kingdom, that the apostolic office as a sign-authenticated witness ends with the sign-program at Acts 28 while Paul’s authority continues in his letters, and that the prophets of Ephesians 2:20 and 3:5 are prophets of the Mystery. It states plainly that no verse names a successor, names modern writers on both sides, and rules on each objection.</p>'
 '<p class="vol-meta">$14.99 · 52 pages</p><a class="vol-link" href="commentary-sign-gifts-04-apostles-and-prophets.html">View Volume 4 →</a><a class="vol-sample" aria-label="Read a sample of Apostles and Prophets" href="commentary-sign-gifts-04-apostles-and-prophets.html#look-inside">Read a sample →</a></div>')
rep('Read a sample →</a></div></div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section><section class="detail-section com-intro"','Read a sample →</a></div>'+tile+'</div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section><section class="detail-section com-intro"')
# pricing and counts
rep('44 Commentary Volumes in nine series','48 Commentary Volumes in ten series',3)
rep('$14.99 each, $54.99 per five-volume series, $43.99 for The Prophets Series, $409.99 for all 44.','$14.99 each, $54.99 per five-volume series, $43.99 for each four-volume series, $454.99 for all 48.',2)
rep('The Prophets Series of four is $43.99, and all 44 volumes are $409.99.','The Prophets Series and The Sign Gifts Series, of four each, are $43.99, and all 48 volumes are $454.99.')
rep('Browse all 44 volumes','Browse all 48 volumes')
rep('five in eight series and four in The Prophets Series.','five in eight series and four in each of the last two.')
def pic(n): return f'<picture><source srcset="assets/sign-gifts-0{n}-cover-thumb.webp" type="image/webp"><img src="assets/sign-gifts-0{n}-cover-thumb.jpg" alt="" loading="lazy" width="240" height="360"></picture>'
card='<article id="bundle-sign-gifts"><h3>The Sign Gifts Series</h3><div class="com-covers" aria-hidden="true">'+''.join(pic(n) for n in range(1,5))+'</div><p>4 volumes, 217 pages in all</p><p><strong>$43.99</strong> <span>individually $59.96 · save $15.97</span></p><a class="com-bundle-link" href="#sign-gifts">Browse The Sign Gifts volumes →</a></article>'
i=s.index('<article id="bundle-prophets">'); j=s.index('</article>',i)+len('</article>')
s=s[:j]+card+s[j:]
rep('The 44 volumes of the nine series, together in one digital set: Prophecy &amp; Mystery, Prophetic Identity, Covenantal, Typology, Prophetic Commentary, Gospel, Acts, Pauline Doctrine and The Prophets,','The 48 volumes of the ten series, together in one digital set: Prophecy &amp; Mystery, Prophetic Identity, Covenantal, Typology, Prophetic Commentary, Gospel, Acts, Pauline Doctrine, The Prophets and The Sign Gifts,')
rep('44 VOLUMES <span>•</span> NINE SERIES','48 VOLUMES <span>•</span> TEN SERIES')
rep('<strong>$409.99</strong><span>$659.56 value when purchased individually</span><b>SAVE $249.57 · 38%</b>','<strong>$454.99</strong><span>$719.52 value when purchased individually</span><b>SAVE $264.53 · 37%</b>')
rep('The 44 volumes of the nine series. Save $73.92 compared with purchasing all nine series bundles separately.','The 48 volumes of the ten series. Save $72.91 compared with purchasing all ten series bundles separately.')
rep('<picture><source srcset="assets/prophets-01-cover-thumb.webp" type="image/webp"><img src="assets/prophets-01-cover-thumb.jpg" alt="" loading="lazy" width="240" height="360"></picture></div></div><div class="com-complete-offer">','<picture><source srcset="assets/prophets-01-cover-thumb.webp" type="image/webp"><img src="assets/prophets-01-cover-thumb.jpg" alt="" loading="lazy" width="240" height="360"></picture>'+pic(1)+'</div></div><div class="com-complete-offer">')
rep("'acts','pauline','prophets'];","'acts','pauline','prophets','sign-gifts'];")
rep('The Complete Commentary Library: nine series','The Complete Commentary Library: ten series')
open(p,'w',encoding='utf-8').write(s)
r='resources.html'; t=open(r,encoding='utf-8').read()
assert t.count('44 volumes in nine series')==1; t=t.replace('44 volumes in nine series','48 volumes in ten series'); open(r,'w',encoding='utf-8').write(t)
m='sitemap.xml'; t=open(m,encoding='utf-8').read(); a='<url><loc>https://zaymariepress.com/commentary-sign-gifts-03-healing-in-the-body.html</loc></url>'
assert t.count(a)==1; t=t.replace(a,a+'<url><loc>https://zaymariepress.com/commentary-sign-gifts-04-apostles-and-prophets.html</loc></url>'); open(m,'w',encoding='utf-8').write(t); print('ok')
