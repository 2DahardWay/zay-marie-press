"""Reciprocal Related Reading links for Sign Gifts Volume 1 (run from the repo root once)."""
import re
V='commentary-sign-gifts-01-the-sign-gifts.html'
LBL='The Sign Gifts Series, Volume 1 — The Sign Gifts'
def add(f, note):
    s=open(f,encoding='utf-8').read()
    m=re.search(r'<h4>Commentary Series</h4>(.*?)</div>',s,re.S)
    assert m and len(re.findall(r'<p><a ',m.group(1)))<3, f
    assert V not in s, f
    s=s[:m.end(1)]+'<p><a href="%s">%s</a> %s</p>'%(V,LBL,note)+s[m.end(1):]
    open(f,'w',encoding='utf-8').write(s); print('edited',f)
add('study-25-the-signs-that-followed.html','Argues what signs were for, to whom they were given and where the record of signs in Acts ends; this study reports Mark 16 and its textual question and does not argue that question.')
add('study-38-why-acts-is-not-a-universal-experience-manual.html','Argues what the signs in Acts were for and where the record of them ends; this study reads Acts as history that is not a command for every believer and does not argue the end of signs.')
add('commentary-acts-02-the-spirit-in-acts.html','Argues what signs were for, to whom they were given and where the record of signs ends; this volume argues the Spirit scenes from Pentecost to Ephesus.')
add('commentary-acts-05-acts-28-the-close-of-the-book.html','Argues what signs were for and that the last sign in the record falls in Acts 28; this volume argues the national suspension in the same chapter.')
add('commentary-gospel-02-the-lords-ministry-to-israel.html','Argues what signs were for, whom they were given to and where the record of them ends; this volume argues the Lord’s ministry to Israel.')
add('packet-exodus.html','A volume in the Commentary Collection whose argument draws on Exodus; this companion stays within the book.')
add('packet-john.html','A volume in the Commentary Collection whose argument draws on John; this companion stays within the book.')
