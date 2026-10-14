"""Convert a packet-<slug>.html page to the Bible Book Companion format.
Usage: python3 convert_page.py <slug> <book name> <pdf> <cover.png> ; run from repo root."""
import re,sys,subprocess,glob,shutil,tempfile
from PIL import Image
slug,name,pdf,coverpng=sys.argv[1:5]
f=f'packet-{slug}.html'; s=open(f,encoding='utf-8').read()
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
# images
im=Image.open(coverpng).convert('RGB').resize((1024,1536),Image.LANCZOS)
im.save(f'assets/companion-{slug}-cover.jpg',quality=88); im.save(f'assets/companion-{slug}-cover.webp',quality=85)
tmp=tempfile.mkdtemp()
subprocess.run(['pdftoppm','-f','2','-l','2','-r','200','-jpeg','-jpegopt','quality=88','-scale-to-x','1041','-scale-to-y','1560',pdf,tmp+'/pv'],check=True)
shutil.copy(glob.glob(tmp+'/pv-*.jpg')[0],f'assets/companion-{slug}-page-1.jpg')
# subtitle from the PDF builder content
mod={}; exec(open(f'build-tools/packets/content_{("1chr" if slug=="1-chronicles" else slug.replace("-",""))}.py',encoding='utf-8').read().split('SECTIONS = []')[0],mod)
sub=mod['SUBTITLE']
old=re.search(r'detail-subtitle">([^<]*)',s).group(1)
s=s.replace(old,sub)
desc=f'A {n}-page printable Bible Book Companion on {name}: book overview, narrative flow, program-specific and universal truths tables, an application grid, and a teaching outline. Preview page 1.'
s=re.sub(r'A \d-page printable Bible Book Companion on [^"]*?Preview the packet\.',desc,s)
s=re.sub(r'Digital PDF · \d+ Pages',f'Digital PDF · {n} Pages',s)
s=re.sub(r'\d-page digital PDF',f'{n}-page digital PDF',s)
s=re.sub(r'takes the next step and interprets\. It selects the passages that carry the book’s doctrine, reads them in the King James Version, and sets them in a structure you can teach from\.','takes the next step and interprets. It reads the book’s doctrine in the King James Version and sets it in a structure you can teach from.',s)
s=s.replace('This packet takes the next step','This companion takes the next step')
s=re.sub(r'Charts, a program flow, a cross-reference network labeled by program, a teaching outline, and application questions are all in a five-page printable PDF, cover included\.','Eleven sections cover the book’s overview, narrative flow, themes, Christ in the book, and what belongs to which program. Two tables, an application grid, and a teaching outline come in a printable PDF, cover included.',s)
s=s.replace('Preview the Packet Before You Purchase','Preview the Companion Before You Purchase').replace('Click any page to enlarge it for reading.','Click the page to enlarge it for reading.')
s=re.sub(r'A packet selects\. It does not walk through the whole book verse by verse\. It reads the passages that carry the book’s doctrine closely and summarizes the rest by structure and theme, then places the book within God’s dealings as Acts Overlap Theology reads them\.','A Bible Book Companion is an eleven-section guide to one book. It gives the book’s setting and program identity, follows its movements, traces its themes and its witness to Christ, separates what belongs to a program from what holds for all people, and ends with a teaching outline and usage notes.',s)
pts=[('Program Identity','See where the book stands and who it addresses, stated in the opening overview.'),('Narrative Flow','Follow the book’s movements from start to finish in the order the book gives them.'),('Themes and Christ','Trace the book’s main themes and how it speaks of Christ.'),('What Belongs to Whom','Learn to separate truths that belong to one program from truths that hold for all people.'),('Application','Test each application against the truths the book itself states.'),('Teaching Outline','Use a seven-part outline with Scripture references as a basis for a lesson.')]
html='<div class="study-points">'+''.join(f'<div class="study-point"><h3>{a}</h3><p>{b}</p></div>' for a,b in pts)+'</div>'
s=re.sub(r'(<h2>Trace the Book’s Turning Points</h2>)<div class="study-points">.*?</div></div>(?=\s*\n|<)',lambda m:m.group(1)+html,s,count=1,flags=re.S)
pv=f'<div class="preview-grid"><div class="preview-card"><a class="preview-image-link" data-preview-lightbox href="assets/companion-{slug}-page-1.jpg"><img src="assets/companion-{slug}-page-1.jpg" alt="{name} Bible Book Companion, page 1: title, contents, and the opening of the book overview"></a><div class="page-no">Page 1</div><h3>Contents and Overview</h3><p>See the eleven sections and how the companion opens.</p></div></div>'
s=re.sub(r'<div class="preview-grid">.*?</div></div>(?=\s*\n|<)',lambda m:pv,s,count=1,flags=re.S)
inc=[('Printable PDF',f'{n} pages with the cover, ready to print or use on screen.'),('Book Overview','Setting, audience, and program identity.'),('Narrative Flow','The book’s movements in order.'),('Themes and Christ','The main themes and the book’s witness to Christ.'),('Truths Tables','What belongs to a program and what holds for all people.'),('Application Grid','Eight applications drawn from the book’s own truths.'),('Teaching Outline','A seven-part outline with Scripture references.'),('Study Suggestions','How to use it alone, in a group, and within the series.')]
ih='<div class="includes-grid">'+''.join(f'<div class="include-item"><h3>{a}</h3><p>{b}</p></div>' for a,b in inc)+'</div>'
s=re.sub(r'<div class="includes-grid">.*?</div></div>(?=\s*\n|<)',lambda m:ih,s,count=1,flags=re.S)
s=s.replace('ABOUT THIS PACKET','ABOUT THIS COMPANION').replace('A Focused Packet on One Book','A Focused Companion to One Book')
new=f'<div class="detail-cover"><picture><source srcset="assets/companion-{slug}-cover.webp" type="image/webp"><img src="assets/companion-{slug}-cover.jpg" alt="{name} Bible Book Companion cover"></picture></div>'
s=re.sub(r'<div class="packet-card.*?<div class="pc-foot">Zay-Marie Press</div></div>',new,s,count=1,flags=re.S)
s=s.replace('This packet follows','This companion follows').replace('This packet surveys the whole book','This companion follows the whole book').replace('this packet stays','this companion stays').replace('; the packet ','; the companion ').replace('A packet sits between','A companion sits between').replace(' through its key passages in five pages;',' through its eleven sections;')
s=re.sub(r'<div class="pk-sample">.*?pk-sample-note">[^<]*</p></div>','',s,flags=re.S)
open(f,'w',encoding='utf-8').write(s)
print(slug,n,'old-format leftovers:',[k for k in ('five-page','5 Pages','Preview the Packet','packet-card','Doctrinal') if k in s])
