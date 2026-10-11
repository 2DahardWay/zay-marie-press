"""Load the KJV chapters needed for this volume from two independent public copies (A: aruljohn/Bible-kjv, B: thiagobodruk/bible en_kjv),
compare each to the other and, where a chapter is already in the verified corpus, to that corpus. usage: python3 kjvfetch.py Code_ch ..."""
import json,re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import kjvlib
A='/home/claude/aruljohn/bible-kjv/'
B=json.load(open('/tmp/kjvnpm/tb/json/en_kjv.json',encoding='utf-8-sig'))
NAMES={'Rom':'Romans','1Cor':'1Corinthians','2Cor':'2Corinthians','Gal':'Galatians','Eph':'Ephesians','Phil':'Philippians','Col':'Colossians','Titus':'Titus','1Tim':'1Timothy','Deut':'Deuteronomy','Isa':'Isaiah','Lev':'Leviticus','Exod':'Exodus','1Thess':'1Thessalonians','Heb':'Hebrews','1Pet':'1Peter','Acts':'Acts','Gen':'Genesis','Ps':'Psalms','Matt':'Matthew','Mark':'Mark','Luke':'Luke','John':'John','1John':'1John','2Tim':'2Timothy','Num':'Numbers'}
IDX={'Gen':0,'Exod':1,'Lev':2,'Num':3,'Deut':4,'Ps':18,'Isa':22,'Matt':39,'Mark':40,'Luke':41,'John':42,'Acts':43,'Rom':44,'1Cor':45,'2Cor':46,'Gal':47,'Eph':48,'Phil':49,'Col':50,'1Thess':51,'1Tim':53,'2Tim':54,'Titus':55,'Heb':57,'1Pet':59,'1John':61}
def canon(s):
    s=s.replace('æ','ae').replace('Æ','Ae').replace('’',"'").replace('‘',"'")
    s=re.sub(r'\{[^}]*\}','',s)   # B carries italic/translation marks in braces? strip to compare
    s=re.sub(r'[\[\]]','',s)
    s=re.sub(r'\s+([,;:.!?])',r'\1',s)
    s=re.sub(r'\s+',' ',s).strip()
    return s
def getA(code,ch):
    d=json.load(open(A+NAMES[code]+'.json',encoding='utf-8'))
    for c in d['chapters']:
        if int(c['chapter'])==ch: return {int(v['verse']):v['text'] for v in c['verses']}
def getB(code,ch):
    return {i+1:t for i,t in enumerate(B[IDX[code]]['chapters'][ch-1])}
if __name__=='__main__':
    for a in sys.argv[1:]:
        code,ch=a.rsplit('_',1); ch=int(ch)
        va=getA(code,ch); vb=getB(code,ch)
        nd=0
        for v in sorted(va):
            ref=kjvlib.V.get((code,ch,v))
            ca=canon(va[v]); cb=canon(vb.get(v,'')); 
            flag=''
            if ca!=cb: flag+=' A!=B'
            if ref is not None and canon(ref)!=ca: flag+=' A!=corpus'
            if ref is not None and canon(ref)!=cb: flag+=' B!=corpus'
            if flag:
                nd+=1; print(code,ch,v,flag); print('  A:',va[v]); print('  B:',vb.get(v)); 
                if ref: print('  C:',ref)
        print(a,len(va),'verses, diffs',nd)
