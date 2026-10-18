"""Give every Key Scriptures card on study and commentary pages an id (sc-<passage>). Idempotent."""
import re,glob
def slug(t):
    t=re.sub(r'<[^>]+>','',t).lower().replace('–','-').replace('—','-')
    return 'sc-'+re.sub(r'[^a-z0-9]+','-',t).strip('-')
n=0;pg=0
for f in sorted(glob.glob('/home/claude/zay-marie-press/study-*.html')+glob.glob('/home/claude/zay-marie-press/commentary-*.html')):
    s=open(f,encoding='utf-8').read();seen=set()
    def sub(m):
        global n
        h=m.group(1);i=slug(h);b=i;k=2
        while i in seen: i=f'{b}-{k}';k+=1
        seen.add(i);n+=1
        return f'<div class="scripture-card" id="{i}"><h3>{h}</h3>'
    t=re.sub(r'<div class="scripture-card"><h3>(.*?)</h3>',sub,s)
    if t!=s: open(f,'w',encoding='utf-8').write(t);pg+=1
print(n,'cards on',pg,'pages')
