import json,re,sys,os
S='/tmp/claude-0/-home-claude/8e45a26c-54c3-5f5e-8290-111dc44c1ba2/scratchpad/kjv/'
sys.path.insert(0,'.')
import kjvlib
B=json.load(open(S+'b/json/en_kjv.json',encoding='utf-8-sig'))
canon="Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov Eccl Song Isa Jer Lam Ezek Dan Hos Joel Amos Obad Jonah Mic Nah Hab Zeph Hag Zech Mal Matt Mark Luke John Acts Rom 1Cor 2Cor Gal Eph Phil Col 1Thess 2Thess 1Tim 2Tim Titus Phlm Heb Jas 1Pet 2Pet 1John 2John 3John Jude Rev".split()
names={'Gen': 'Genesis', 'Exod': 'Exodus', 'Lev': 'Leviticus', 'Num': 'Numbers', 'Deut': 'Deuteronomy', 'Josh': 'Joshua', 'Judg': 'Judges', 'Ruth': 'Ruth', '1Sam': '1 Samuel', '2Sam': '2 Samuel', '1Kgs': '1 Kings', '2Kgs': '2 Kings', '1Chr': '1 Chronicles', '2Chr': '2 Chronicles', 'Ezra': 'Ezra', 'Neh': 'Nehemiah', 'Esth': 'Esther', 'Job': 'Job', 'Ps': 'Psalms', 'Prov': 'Proverbs', 'Eccl': 'Ecclesiastes', 'Song': 'Song of Solomon', 'Isa': 'Isaiah', 'Jer': 'Jeremiah', 'Lam': 'Lamentations', 'Ezek': 'Ezekiel', 'Dan': 'Daniel', 'Hos': 'Hosea', 'Joel': 'Joel', 'Amos': 'Amos', 'Obad': 'Obadiah', 'Jonah': 'Jonah', 'Mic': 'Micah', 'Nah': 'Nahum', 'Hab': 'Habakkuk', 'Zeph': 'Zephaniah', 'Hag': 'Haggai', 'Zech': 'Zechariah', 'Mal': 'Malachi', 'Matt': 'Matthew', 'Mark': 'Mark', 'Luke': 'Luke', 'John': 'John', 'Acts': 'Acts', 'Rom': 'Romans', '1Cor': '1 Corinthians', '2Cor': '2 Corinthians', 'Gal': 'Galatians', 'Eph': 'Ephesians', 'Phil': 'Philippians', 'Col': 'Colossians', '1Thess': '1 Thessalonians', '2Thess': '2 Thessalonians', '1Tim': '1 Timothy', '2Tim': '2 Timothy', 'Titus': 'Titus', 'Phlm': 'Philemon', 'Heb': 'Hebrews', 'Jas': 'James', '1Pet': '1 Peter', '2Pet': '2 Peter', '1John': '1 John', '2John': '2 John', '3John': '3 John', 'Jude': 'Jude', 'Rev': 'Revelation'}
def n(s): return re.sub(r'[\s\-]','',re.sub(r'\s+([,.;:?!])',r'\1',s.replace('’',"'"))).lower()
def A(code,ch,v):
    f=S+'a/'+names[code].replace(' ','')+'.json'
    if not os.path.exists(f):
        import glob; f=[x for x in glob.glob(S+'a/*.json') if os.path.basename(x).lower()==names[code].replace(' ','').lower()+'.json'][0]
    d=json.load(open(f,encoding='utf-8-sig'))
    return d['chapters'][ch-1]['verses'][v-1]['text']
out=[]
for ref in sys.argv[1:]:
    m=re.match(r'(\w+):(\d+):(\d+)(?:-(\d+))?',ref); c,ch,a,b=m.group(1),int(m.group(2)),int(m.group(3)),int(m.group(4) or m.group(3))
    for v in range(a,b+1):
        ta=A(c,ch,v).strip(); tb=B[canon.index(c)]['chapters'][ch-1][v-1]
        ta=re.sub(r'\s+',' ',ta)
        ta2=re.sub(r'^#\s*','',ta)
        if n(ta2)!=n(tb): print('DIFF',ref,v,'\n A',ta2,'\n B',tb)
        if (c,ch,v) in kjvlib.V: continue
        out.append(f'{c}_{ch}\t{v}\t{ta2}\n')
print(len(out),'new verses')
open('kjv_all.txt','a',encoding='utf-8').writelines(out)
