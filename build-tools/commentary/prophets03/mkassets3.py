"""Website assets for Prophets Series Volume 3. usage (repo root): python3 build-tools/commentary/prophets03/mkassets3.py"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
H = os.path.dirname(os.path.abspath(__file__)); A = 'assets'
art = Image.open(os.path.join(H, 'out', 'cover3.jpg')).convert('RGB')
c = art.resize((1024, 1536), Image.LANCZOS)
c.save(f'{A}/prophets-03-cover.jpg', quality=88, optimize=True); c.save(f'{A}/prophets-03-cover.webp', quality=82)
for n, s in (('card', (400, 600)), ('thumb', (240, 360))):
    r = art.resize(s, Image.LANCZOS)
    r.save(f'{A}/prophets-03-cover-{n}.jpg', quality=86, optimize=True); r.save(f'{A}/prophets-03-cover-{n}.webp', quality=80)
# previews: interior page P = PDF page P+1
for P in (1, 2, 19, 34):
    out = f'{A}/prophets-03-page-{P}'
    subprocess.run(['pdftoppm', '-f', str(P + 1), '-l', str(P + 1), '-scale-to-x', '1041', '-scale-to-y', '1560', '-jpeg', '-jpegopt', 'quality=88', '-singlefile', os.path.join(H, 'out', 'volume.pdf'), out], check=True)
# share image 1200x630
W, Ht = 1200, 630
im = Image.new('RGB', (W, Ht), (0, 38, 83)); d = ImageDraw.Draw(im)
im.paste(art.resize((380, 570), Image.LANCZOS), (50, 30))
D = '/usr/share/fonts/truetype/dejavu/'
f = lambda n, s: ImageFont.truetype(D + n, s)
d.text((470, 86), 'THE PROPHETS SERIES', font=f('DejaVuSans-Bold.ttf', 24), fill=(176, 168, 140))
d.text((470, 138), 'The Nations', font=f('DejaVuSerif-Bold.ttf', 68), fill='white')
d.text((470, 208), 'Judged', font=f('DejaVuSerif-Bold.ttf', 68), fill='white')
for i, t in enumerate(['The Grounds, the Terms, and', 'the Endings the LORD Gave', 'Each Nation']):
    d.text((470, 330 + i * 41), t, font=f('DejaVuSerif.ttf', 31), fill=(91, 123, 189))
d.text((470, 562), 'Prophets Series Volume 3  ·  $14.99  ·  Zay-Marie Press', font=f('DejaVuSans.ttf', 25), fill='white')
im.save(f'{A}/share-commentary-prophets-03-the-nations-judged.jpg', quality=88)
