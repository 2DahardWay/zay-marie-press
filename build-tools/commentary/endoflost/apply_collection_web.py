"""Add The End of the Lost (stand-alone) to commentary.html, resources.html, sitemap.xml. Run once from the repo root."""
p='commentary.html'; s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a)); s=s.replace(a,b)
rep('48 Commentary Volumes in ten series','49 Commentary Volumes (ten series and one stand-alone volume)',3)
rep('$43.99 for each four-volume series, $454.99 for all 48.','$43.99 for each four-volume series, $464.99 for all 49.',2)
rep('and all 48 volumes are $454.99.','and all 49 volumes are $464.99.')
rep('Browse all 48 volumes','Browse all 49 volumes')
# set-index tile
rep('<em>217 pages · $43.99 bundle</em></a></div><p class="set-pricing-link">','<em>217 pages · $43.99 bundle</em></a><a href="#end-of-the-lost"><strong>The End of the Lost</strong><span>Stand-alone volume</span><em>66 pages · $14.99</em></a></div><p class="set-pricing-link">')
# jump nav
rep('<li><a href="#sign-gifts">Sign Gifts</a></li><li><a class="price"','<li><a href="#sign-gifts">Sign Gifts</a></li><li><a href="#end-of-the-lost">End of the Lost</a></li><li><a class="price"')
# which-series row
rep('what ended at Acts 28?</td><td><a href="#sign-gifts">The Sign Gifts Series</a></td></tr></tbody>','what ended at Acts 28?</td><td><a href="#sign-gifts">The Sign Gifts Series</a></td></tr><tr><td>Do the Bible’s words of destruction mean the lost cease to exist, or is the punishment without end?</td><td><a href="#end-of-the-lost">The End of the Lost</a></td></tr></tbody>')
# index entry
rep('Apostles and Prophets</a></li></ol></div></div></details>','Apostles and Prophets</a></li></ol></div><div class="com-idx-col"><h3><a href="#end-of-the-lost">Stand-alone volume</a></h3><ol><li><a href="commentary-end-of-the-lost.html">The End of the Lost</a></li></ol></div></div></details>')
# section
tile=('<div class="vol-tile"><a href="commentary-end-of-the-lost.html"><picture><source srcset="assets/end-of-the-lost-cover-card.webp" type="image/webp"><img src="assets/end-of-the-lost-cover-card.jpg" alt="The End of the Lost cover" loading="lazy" width="400" height="600"></picture></a>'
 '<div class="vol-no">Stand-alone</div><h3>The End of the Lost</h3><p class="vol-blurb">Scripture speaks of the lost in the words of death, destruction, perishing, punishment, torment, exclusion and the second death. The volume argues that destruction language does not by itself establish annihilation, that its meaning is fixed by context, and that the passages taken together establish irreversible, everlasting punishment: Revelation describes human beings under torment without rest, names the lake of fire as the second death and as the place of torment day and night for ever and ever, so that those finally cast into it do not cease to exist. The case is cumulative and never rests on one Greek word or one proof text. It names modern writers on both sides and rules on each objection.</p>'
 '<p class="vol-meta">$14.99 · 66 pages</p><a class="vol-link" href="commentary-end-of-the-lost.html">View the Volume →</a><a class="vol-sample" aria-label="Read a sample of The End of the Lost" href="commentary-end-of-the-lost.html#look-inside">Read a sample →</a></div>')
sec=('<section class="set-series" id="end-of-the-lost"><div class="wrap"><div class="eyebrow">STAND-ALONE VOLUME</div><h2>The End of the Lost</h2><p class="set-desc">One volume that belongs to no series. It takes a single question: whether the final punishment of the lost is their ceasing to exist, or a punishment that does not end. It is sold on its own and is not part of a series bundle.</p><div class="vol-grid">'+tile+'</div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section>')
rep('Read a sample →</a></div></div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section><section class="detail-section com-intro" id="every-volume">','Read a sample →</a></div></div><p class="set-top"><a href="#commentary-top">↑ Back to top</a></p></div></section>'+sec+'<section class="detail-section com-intro" id="every-volume">')
# library
rep('The 48 volumes of the ten series, together in one digital set:','The 49 volumes of the ten series and the stand-alone volume, together in one digital set:')
rep('The Prophets and The Sign Gifts, each volume','The Prophets, The Sign Gifts and The End of the Lost, each volume')
rep('48 VOLUMES <span>•</span> TEN SERIES','49 VOLUMES <span>•</span> TEN SERIES AND ONE STAND-ALONE VOLUME')
rep('<strong>$454.99</strong><span>$719.52 value when purchased individually</span><b>SAVE $264.53 · 37%</b>','<strong>$464.99</strong><span>$734.51 value when purchased individually</span><b>SAVE $269.52 · 37%</b>')
rep('The 48 volumes of the ten series. Save $72.91 compared with purchasing all ten series bundles separately.','The 49 volumes of the ten series and the stand-alone volume. Save $77.90 compared with purchasing all ten series bundles and the stand-alone volume separately.')
open(p,'w',encoding='utf-8').write(s)
r='resources.html'; t=open(r,encoding='utf-8').read()
assert t.count('48 volumes in ten series')==1; t=t.replace('48 volumes in ten series','49 volumes in ten series and one stand-alone volume'); open(r,'w',encoding='utf-8').write(t)
m='sitemap.xml'; t=open(m,encoding='utf-8').read(); a='<url><loc>https://zaymariepress.com/commentary-sign-gifts-04-apostles-and-prophets.html</loc></url>'
assert t.count(a)==1; t=t.replace(a,a+'<url><loc>https://zaymariepress.com/commentary-end-of-the-lost.html</loc></url>'); open(m,'w',encoding='utf-8').write(t); print('ok')
