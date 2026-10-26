"""Reciprocal Related Reading links for The End of the Lost (run once from the repo root). A full Commentary Series list (three) is skipped and reported."""
import re
V='commentary-end-of-the-lost.html'
LBL='The End of the Lost'
def add(f, note):
    s=open(f,encoding='utf-8').read()
    assert V not in s, f
    m=re.search(r'<h4>Commentary Series</h4>(.*?)</div>',s,re.S)
    if not m:
        print('NO LIST',f); return
    n=len(re.findall(r'<p><a ',m.group(1)))
    if n>=3: print('FULL (%d), skipped'%n,f); return
    s=s[:m.end(1)]+'<p><a href="%s">%s</a> %s</p>'%(V,LBL,note)+s[m.end(1):]
    open(f,'w',encoding='utf-8').write(s); print('edited',f,n,'->',n+1)
add('study-79-the-realms-of-the-dead.html','A stand-alone Commentary Volume that argues what the final punishment of the lost is; this study reports the words for the unseen world as written.')
add('study-31-the-judgments-of-scripture.html','A stand-alone Commentary Volume that argues what the final punishment of the lost is; this study reports the judgments in their settings.')
add('study-68-the-book-of-life.html','A stand-alone Commentary Volume that reads Revelation 20:11–15 for the punishment that follows; this study traces the book of life.')
add('commentary-prophecy-mystery-05-separate-courts.html','A stand-alone volume that argues what the final punishment is; this volume argues who is judged where.')
add('commentary-gospel-03-the-olivet-discourse.html','A stand-alone volume that reads Matthew 25:31–46 for the word “eternal”; this volume argues the discourse as Israel’s.')
add('parable-24-the-rich-man-and-lazarus.html','A stand-alone volume that argues the final punishment of the lost; it cites Luke 16 only as the Lord’s account of the dead.')
add('parable-31-the-sheep-and-the-goats.html','A stand-alone volume that reads the closing verse of Matthew 25 for the word “eternal”; this edition reads the parable on its own.')
add('packet-revelation.html','A stand-alone volume that reads Revelation 14 and 20 and 21 for the final punishment; this companion stays within the book.')
add('packet-matthew.html','A stand-alone volume that reads Matthew 10:28 and 25:46; this companion stays within the book.')
add('packet-2-thessalonians.html','A stand-alone volume that reads 2 Thessalonians 1:7–10; this companion stays within the book.')
