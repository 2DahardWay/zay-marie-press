"""Reciprocal Related Reading links for Sign Gifts Volume 2 (run from the repo root once). A page already at three Commentary Series links is skipped and reported."""
import re
V='commentary-sign-gifts-02-tongues-and-prophecy.html'
LBL='The Sign Gifts Series, Volume 2 — Tongues and Prophecy'
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
add('study-81-praying-in-the-spirit.html','Argues what the tongues are, who they were for and that the Corinthian gifts ended at Acts 28; this study reports the passages on praying in the Spirit and takes no position.')
add('study-25-the-signs-that-followed.html','Argues the nature of tongues and prophecy and whether they continue; this study reports what Mark 16 says of signs.')
add('study-38-why-acts-is-not-a-universal-experience-manual.html','Argues what the three instances of tongues in Acts are beside 1 Corinthians 14; this study reads Acts as history that is not a command for every believer.')
add('commentary-pauline-04-the-assembly-in-order.html','Argues what tongues and prophecy are and whether they continue; this volume argues the order of the assembly.')
add('commentary-acts-02-the-spirit-in-acts.html','Argues what the tongues are beside 1 Corinthians 14 and that the Corinthian gifts ended at Acts 28; this volume argues the Spirit scenes in Acts.')
add('packet-1-corinthians.html','A volume in the Commentary Collection that argues 1 Corinthians 12 to 14; this companion stays within the book.')
add('packet-isaiah.html','A volume in the Commentary Collection whose argument draws on Isaiah 28; this companion stays within the book.')
