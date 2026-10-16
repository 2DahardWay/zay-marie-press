"""Reciprocal Related Reading links for Volume 4 (run from the repo root once)."""
import re
V='commentary-prophets-04-elijah-must-first-come.html'
def edit(f, fn):
    s=open(f,encoding='utf-8').read(); t=fn(s); assert t!=s,f; open(f,'w',encoding='utf-8').write(t); print('edited',f)
def add_to_commentary_col(note):
    def fn(s):
        m=re.search(r'<h4>Commentary Series</h4>(.*?)</div>',s,re.S)
        assert len(re.findall(r'<p><a ',m.group(1)))<3
        link='<p><a href="%s">The Prophets Series, Volume 4 — Elijah Must First Come</a> %s</p>'%(V,note)
        return s[:m.end(1)]+link+s[m.end(1):]
    return fn
#edit('commentary-02-beast-false-prophet.html',add_to_commentary_col('Argues who the genuine Elijah is whom Malachi says will be sent, and whether the promise has been met; this volume argues the false prophet of Revelation 13 as the counterfeit and does not argue the genuine prophet.'))
#edit('commentary-gospel-02-the-lords-ministry-to-israel.html',add_to_commentary_col('Argues who the Elijah is that Malachi says will be sent, and whether the promise has been met; this volume argues the Lord’s ministry to Israel and reads John’s errand only within it.'))
def mal(s):
    a='<div class="rel-col"><h4>Digital Studies</h4>'
    i=s.index(a); j=s.index('</div>',i)+len('</div>')
    col='<div class="rel-col"><h4>Commentary Series</h4><p><a href="%s">The Prophets Series, Volume 4 — Elijah Must First Come</a> A volume in the Commentary Collection whose argument draws on Malachi; this companion stays within the book.</p></div>'%V
    return s[:j]+col+s[j:]
edit('packet-malachi.html',mal)
