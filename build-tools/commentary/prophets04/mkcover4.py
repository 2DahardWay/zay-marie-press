"""Letter the publisher's Volume 4 artwork (same lettering as Volume 1): gold Lora title in the upper sky, VOLUME 2 upper right,
subtitle and series line at the foot over a dark gradient. usage: mkcover_final.py art.png out.jpg"""
import sys, os
from PIL import Image as _I; _I.MAX_IMAGE_PIXELS=None
from PIL import Image, ImageDraw, ImageFont
import content
src, out = sys.argv[1], sys.argv[2]
W, H = 1600, 2400
art = Image.open(src).convert('RGB').resize((W, H), Image.LANCZOS)
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); px = ov.load()
for y in range(H):
    a = 0
    if y < 520: a = int(190 * (1 - y / 520) ** 1.4)
    if y > 1900: a = max(a, int(215 * ((y - 1900) / 500) ** 1.1))
    for x in range(W): px[x, y] = (5, 8, 18, a)
art = Image.alpha_composite(art.convert('RGBA'), ov).convert('RGB')
d = ImageDraw.Draw(art)
def lora(sz):
    f = ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf', sz); f.set_variation_by_name('Bold'); return f
def rob(sz): return ImageFont.truetype(os.path.expanduser('~/.fonts/Roboto-Bold.ttf'), sz)
def spaced(t, f, sp): return sum(d.textlength(c, font=f) for c in t) + sp * (len(t) - 1)
def draw_spaced(cx, y, t, f, sp, fill):
    x = cx - spaced(t, f, sp) / 2
    for c in t:
        d.text((x + 3, y + 4), c, font=f, fill=(0, 0, 0)); d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + sp
gold = (226, 184, 96); cream = (244, 238, 226)
lab = 'VOLUME %d' % content.META['vol']; fl = rob(54); x = W - 110 - spaced(lab, fl, 6)
for c in lab:
    d.text((x + 2, 93), c, font=fl, fill=(0, 0, 0)); d.text((x, 90), c, font=fl, fill=cream); x += d.textlength(c, font=fl) + 6
ft = lora(96)
draw_spaced(W / 2, 150, 'ELIJAH MUST', ft, 9, gold)
draw_spaced(W / 2, 258, 'FIRST COME', ft, 9, gold)
fs = rob(42)
draw_spaced(W / 2, 2150, 'MALACHI’S PROMISE, JOHN’S ANSWER,', fs, 4, cream)
draw_spaced(W / 2, 2208, 'AND THE COMING THE LORD STILL NAMES', fs, 4, cream)
draw_spaced(W / 2, 2290, content.META['series'].upper(), rob(46), 8, gold)
print('title width', spaced('FIRST COME', ft, 9))
art.save(out, quality=95)
