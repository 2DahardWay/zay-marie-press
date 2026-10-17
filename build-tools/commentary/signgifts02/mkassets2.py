"""Website assets for Sign Gifts Series Volume 2. usage (repo root): python3 build-tools/commentary/signgifts02/mkassets1.py"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
H = os.path.dirname(os.path.abspath(__file__)); A = 'assets'
art = Image.open(os.path.join(H, 'cover_source_1024.jpg')).convert('RGB')   # the publisher's supplied 1024x1536 cover, lettered
assert art.size == (1024, 1536)
art.save(f'{A}/sign-gifts-02-cover.jpg', quality=90, optimize=True); art.save(f'{A}/sign-gifts-02-cover.webp', quality=84)
for n, s in (('card', (400, 600)), ('thumb', (240, 360))):
    r = art.resize(s, Image.LANCZOS)
    r.save(f'{A}/sign-gifts-02-cover-{n}.jpg', quality=86, optimize=True); r.save(f'{A}/sign-gifts-02-cover-{n}.webp', quality=80)
# previews: interior page P = PDF page P+1 (footer number)
for P in (1, 2, 9, 34):
    out = f'{A}/sign-gifts-02-page-{P}'
    subprocess.run(['pdftoppm', '-f', str(P + 1), '-l', str(P + 1), '-scale-to-x', '1041', '-scale-to-y', '1560', '-jpeg', '-jpegopt', 'quality=88', '-singlefile', os.path.join(H, 'out', 'volume.pdf'), out], check=True)
# share image 1200x630
W, Ht = 1200, 630
im = Image.new('RGB', (W, Ht), (26, 19, 13)); d = ImageDraw.Draw(im)
im.paste(art.resize((380, 570), Image.LANCZOS), (50, 30))
D = '/usr/share/fonts/truetype/dejavu/'
f = lambda n, s: ImageFont.truetype(D + n, s)
d.text((470, 86), 'THE SIGN GIFTS SERIES', font=f('DejaVuSans-Bold.ttf', 24), fill=(196, 160, 86))
d.text((470, 138), 'Tongues and Prophecy', font=f('DejaVuSerif-Bold.ttf', 54), fill=(236, 214, 160))
for i, t in enumerate(['Whether Tongues and Prophecy', 'Continue in the Body']):
    d.text((470, 270 + i * 44), t, font=f('DejaVuSerif.ttf', 33), fill='white')
d.text((470, 562), 'Sign Gifts Series Volume 2  ·  $14.99  ·  Zay-Marie Press', font=f('DejaVuSans.ttf', 25), fill=(236, 214, 160))
im.save(f'{A}/share-commentary-sign-gifts-02-tongues-and-prophecy.jpg', quality=88)
print('assets ok')
