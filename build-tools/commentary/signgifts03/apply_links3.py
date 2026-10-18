"""Reciprocal Related Reading links for Sign Gifts Volume 3 (run from the repo root once). A page already at three Commentary Series links is skipped and reported."""
import re
V='commentary-sign-gifts-03-healing-in-the-body.html'
LBL='The Sign Gifts Series, Volume 3 — Healing in the Body'
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
add('study-86-the-servant-in-isaiah.html','Reads Isaiah 53:4–6 beside Matthew 8:17 and 1 Peter 2:24 and argues none promises healing to the Body; this study reads the servant passages of Isaiah in order.')
add('study-25-the-signs-that-followed.html','Argues what healing was for in each setting and that the gifts of healing ended with the sign-program; this study reports what Mark 16 says of signs.')
add('study-38-why-acts-is-not-a-universal-experience-manual.html','Argues what the healings of Acts were for and where they end; this study reads Acts as history that is not a command for every believer.')
add('commentary-sign-gifts-01-the-sign-gifts.html','Takes healing in full, reading the passages that Volume 1 reports briefly; this volume argues the sign-program.')
add('commentary-sign-gifts-02-tongues-and-prophecy.html','Takes the healing clauses of 1 Corinthians 12 and James 5 in full; this volume argues tongues and prophecy.')
add('commentary-acts-05-acts-28-the-close-of-the-book.html','Applies the suspension at Acts 28 to the gifts of healing; this volume argues the suspension itself.')
add('commentary-pauline-04-the-assembly-in-order.html','Argues what the gifts of healing were and when they ended; this volume argues the order of the assembly.')
add('packet-james.html','A volume in the Commentary Collection that reads James 5 in its Israel setting; this companion stays within the book.')
add('packet-2-corinthians.html','A volume in the Commentary Collection that reads 2 Corinthians 12:7–10; this companion stays within the book.')
add('packet-1-corinthians.html','A volume in the Commentary Collection that reads the healing clauses of 1 Corinthians 12; this companion stays within the book.')
