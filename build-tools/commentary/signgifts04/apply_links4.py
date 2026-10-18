"""Reciprocal Related Reading links for Sign Gifts Volume 4 (run from the repo root once). A page already at three Commentary Series links is skipped and reported."""
import re
V='commentary-sign-gifts-04-apostles-and-prophets.html'
LBL='The Sign Gifts Series, Volume 4 — Apostles and Prophets'
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
add('study-18-peter-and-paul-distinct-apostolic-commissions.html','Reads what an apostle is in each passage and whether the office continues; this study reads the two commissions as the passages state them.')
add('study-36-jews-gentiles-and-the-church-of-god.html','Reads the foundation of Ephesians 2:20 and the prophets of Ephesians 3:5; this study reads the identity of Jew, Gentile and the church.')
add('study-14-acts-9-and-the-beginning-of-mystery.html','Reads Paul’s apostleship and the signs of an apostle; this study reads Acts 9 and the beginning of the Mystery.')
add('commentary-sign-gifts-01-the-sign-gifts.html','Takes the offices of apostle and prophet in full; this volume argues what signs were for and where the record ends.')
add('commentary-sign-gifts-02-tongues-and-prophecy.html','Takes the persons called apostles and prophets; this volume argues tongues and prophecy as gifts.')
add('commentary-sign-gifts-03-healing-in-the-body.html','Takes the offices of apostle and prophet in full; this volume argues what healing is for.')
add('commentary-acts-03-paul-called-and-sent.html','Reads Paul’s apostleship and the signs of an apostle; this volume argues his call and sending.')
add('commentary-pauline-04-the-assembly-in-order.html','Argues the offices of apostle and prophet and the foundation of Ephesians 2:20; this volume argues the order of the assembly.')
add('packet-ephesians.html','A volume in the Commentary Collection that reads Ephesians 2:19–22, 3:1–13 and 4:7–16; this companion stays within the book.')
add('packet-galatians.html','A volume in the Commentary Collection that reads Galatians 1 and 2 on Paul’s apostleship; this companion stays within the book.')
add('packet-2-corinthians.html','A volume in the Commentary Collection that reads 2 Corinthians 11 and 12 on the signs of an apostle; this companion stays within the book.')
