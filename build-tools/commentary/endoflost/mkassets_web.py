"""Website assets for The End of the Lost. usage (repo root): python3 build-tools/commentary/endoflost/mkassets_web.py"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
H = os.path.dirname(os.path.abspath(__file__)); A = 'assets'; N = 'end-of-the-lost'
art = Image.open(os.path.join(H, 'cover_supplied.jpg')).convert('RGB').resize((1024, 1536), Image.LANCZOS)
art.save(f'{A}/{N}-cover.jpg', quality=90, optimize=True); art.save(f'{A}/{N}-cover.webp', quality=84)
for n, s in (('card', (400, 600)), ('thumb', (240, 360))):
    r = art.resize(s, Image.LANCZOS)
    r.save(f'{A}/{N}-cover-{n}.jpg', quality=86, optimize=True); r.save(f'{A}/{N}-cover-{n}.webp', quality=80)
for P in (1, 2, 36, 46):   # interior page numbers; PDF page = P + 1
    subprocess.run(['pdftoppm', '-f', str(P + 1), '-l', str(P + 1), '-scale-to-x', '1041', '-scale-to-y', '1560', '-jpeg', '-jpegopt', 'quality=88', '-singlefile', os.path.join(H, 'out', 'volume.pdf'), f'{A}/{N}-page-{P}'], check=True)
W, Ht = 1200, 630
im = Image.new('RGB', (W, Ht), (16, 14, 18)); d = ImageDraw.Draw(im)
im.paste(art.resize((380, 570), Image.LANCZOS), (50, 30))
D = '/usr/share/fonts/truetype/dejavu/'
f = lambda n, s: ImageFont.truetype(D + n, s)
d.text((470, 86), 'COMMENTARY COLLECTION', font=f('DejaVuSans-Bold.ttf', 24), fill=(196, 160, 86))
d.text((470, 138), 'The End of the Lost', font=f('DejaVuSerif-Bold.ttf', 50), fill=(236, 214, 160))
for i, t in enumerate(['Destruction, Eternal Punishment,', 'and the Case Against', 'Annihilationism']):
    d.text((470, 250 + i * 44), t, font=f('DejaVuSerif.ttf', 33), fill='white')
d.text((470, 562), 'Stand-alone volume  ·  $14.99  ·  Zay-Marie Press', font=f('DejaVuSans.ttf', 25), fill=(236, 214, 160))
im.save(f'{A}/share-commentary-{N}.jpg', quality=88)
print('assets ok')
