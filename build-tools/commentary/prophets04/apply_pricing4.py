"""Apply the approved Prophets Series pricing to commentary.html (series complete at 4 volumes). Run once from the repo root."""
import re
p='commentary.html'
t=open(p).read()
def rep(a,b,n=1):
    global t
    assert t.count(a)==n,(a[:70],t.count(a))
    t=t.replace(a,b)
# counts and prices
rep('40 Commentary Volumes in eight series','44 Commentary Volumes in nine series',2)
rep('39 Commentary Volumes in eight series','44 Commentary Volumes in nine series')
rep('$14.99 each, $54.99 per five-volume series, $364.99 for all 40.','$14.99 each, $54.99 per five-volume series, $43.99 for The Prophets Series, $409.99 for all 44.',2)
rep('every volume is $14.99; each series of five is $54.99, and all 40 volumes are $364.99.','every volume is $14.99; each series of five is $54.99, The Prophets Series of four is $43.99, and all 44 volumes are $409.99.')
rep('Browse all 40 volumes','Browse all 44 volumes')
# strip
rep('<span>4 volumes so far</span><em>223 pages · series in progress</em>','<span>4 volumes</span><em>223 pages · $43.99 bundle</em>')
# prophets section
rep('SERIES 9 · IN PROGRESS · 4 VOLUMES AVAILABLE','SERIES 9 · 4 VOLUMES')
rep(' and whether the promise has been met. More volumes will follow.</p><div class="vol-grid">',' and whether the promise has been met.</p><p class="set-buy">Own all four volumes: <strong>$43.99</strong> <span>save $15.97</span> · <a href="#bundle-prophets">See the series bundle →</a></p><div class="vol-grid">')
# bundles intro
rep('Each bundle contains all five volumes of its series.','Each bundle contains all the volumes of its series: five in eight series and four in The Prophets Series.')
# bundle card
def pic(n): return f'<picture><source srcset="assets/prophets-0{n}-cover-thumb.webp" type="image/webp"><img src="assets/prophets-0{n}-cover-thumb.jpg" alt="" loading="lazy" width="240" height="360"></picture>'
card='<article id="bundle-prophets"><h3>The Prophets Series</h3><div class="com-covers" aria-hidden="true">'+''.join(pic(n) for n in range(1,5))+'</div><p>4 volumes, 223 pages in all</p><p><strong>$43.99</strong> <span>individually $59.96 · save $15.97</span></p><a class="com-bundle-link" href="#prophets">Browse The Prophets volumes →</a></article>'
rep('Browse the Pauline Doctrine volumes →</a></article></div>','Browse the Pauline Doctrine volumes →</a></article>'+card+'</div>')
# library
rep('The 40 volumes of the eight series, together in one digital set: Prophecy &amp; Mystery, Prophetic Identity, Covenantal, Typology, Prophetic Commentary, Gospel, Acts and Pauline Doctrine,','The 44 volumes of the nine series, together in one digital set: Prophecy &amp; Mystery, Prophetic Identity, Covenantal, Typology, Prophetic Commentary, Gospel, Acts, Pauline Doctrine and The Prophets,')
rep('40 VOLUMES <span>•</span> EIGHT SERIES','44 VOLUMES <span>•</span> NINE SERIES')
rep('<strong>$364.99</strong><span>$599.60 value when purchased individually</span><b>SAVE $234.61 · 39%</b>','<strong>$409.99</strong><span>$659.56 value when purchased individually</span><b>SAVE $249.57 · 38%</b>')
rep('The 40 volumes of the eight series. Save $74.93 compared with purchasing all eight series bundles separately.','The 44 volumes of the nine series. Save $73.92 compared with purchasing all nine series bundles separately.')
# library cover strip
rep('<picture><source srcset="assets/pauline-01-cover-thumb.webp" type="image/webp"><img src="assets/pauline-01-cover-thumb.jpg" alt="" loading="lazy" width="240" height="360"></picture></div></div><div class="com-complete-offer">','<picture><source srcset="assets/pauline-01-cover-thumb.webp" type="image/webp"><img src="assets/pauline-01-cover-thumb.jpg" alt="" loading="lazy" width="240" height="360"></picture>'+pic(1)+'</div></div><div class="com-complete-offer">')
# zoom js
rep("'acts','pauline'];","'acts','pauline','prophets'];")
rep('The Complete Commentary Library: eight series','The Complete Commentary Library: nine series')
open(p,'w').write(t)
print('ok')
