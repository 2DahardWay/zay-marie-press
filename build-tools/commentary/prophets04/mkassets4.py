"""Website assets for Prophets Series Volume 4. usage (repo root): python3 build-tools/commentary/prophets04/mkassets4.py"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
H = os.path.dirname(os.path.abspath(__file__)); A = 'assets'
art = Image.open(os.path.join(H, 'out', 'cover4.jpg')).convert('RGB')
c = art.resize((1024, 1536), Image.LANCZOS)
c.save(f'{A}/prophets-04-cover.jpg', quality=88, optimize=True); c.save(f'{A}/prophets-04-cover.webp', quality=82)
for n, s in (('card', (400, 600)), ('thumb', (240, 360))):
    r = art.resize(s, Image.LANCZOS)
    r.save(f'{A}/prophets-04-cover-{n}.jpg', quality=86, optimize=True); r.save(f'{A}/prophets-04-cover-{n}.webp', quality=80)
# previews: interior page P = PDF page P+1
for P in (1, 2, 26, 34):
    out = f'{A}/prophets-04-page-{P}'
    subprocess.run(['pdftoppm', '-f', str(P + 1), '-l', str(P + 1), '-scale-to-x', '1041', '-scale-to-y', '1560', '-jpeg', '-jpegopt', 'quality=88', '-singlefile', os.path.join(H, 'out', 'volume.pdf'), out], check=True)
# share image 1200x630
W, Ht = 1200, 630
im = Image.new('RGB', (W, Ht), (0, 38, 83)); d = ImageDraw.Draw(im)
im.paste(art.resize((380, 570), Image.LANCZOS), (50, 30))
D = '/usr/share/fonts/truetype/dejavu/'
f = lambda n, s: ImageFont.truetype(D + n, s)
d.text((470, 86), 'THE PROPHETS SERIES', font=f('DejaVuSans-Bold.ttf', 24), fill=(176, 168, 140))
d.text((470, 138), 'Elijah Must', font=f('DejaVuSerif-Bold.ttf', 68), fill='white')
d.text((470, 208), 'First Come', font=f('DejaVuSerif-Bold.ttf', 68), fill='white')
for i, t in enumerate(['Malachi’s Promise, John’s Answer,', 'and the Coming the', 'LORD Still Names']):
    d.text((470, 330 + i * 41), t, font=f('DejaVuSerif.ttf', 31), fill=(91, 123, 189))
d.text((470, 562), 'Prophets Series Volume 4  ·  $14.99  ·  Zay-Marie Press', font=f('DejaVuSans.ttf', 25), fill='white')
im.save(f'{A}/share-commentary-prophets-04-elijah-must-first-come.jpg', quality=88)
