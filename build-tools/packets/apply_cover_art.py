#!/usr/bin/env python3
"""Individual Bible Book Companion cover art.
usage: python3 apply_cover_art.py <art_dir>   art_dir holds <slug>.png|jpg (supplied artwork, ~2:3).
Writes assets/companion-<slug>-cover.jpg/.webp (1024x1536) and <art_dir>/<slug>-1600.jpg (1600x2400, used as the PDF cover by build_packet.py ART=<art_dir>)."""
import sys, importlib
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).resolve().parent))
MODS={'genesis':'genesis','exodus':'exodus','leviticus':'leviticus','numbers':'numbers','deuteronomy':'deuteronomy','joshua':'joshua','judges':'judges','ruth':'ruth','1-samuel':'1samuel','2-samuel':'2samuel','1-chronicles':'1chr','1-kings':'1kings','2-chronicles':'2chronicles','2-kings':'2kings','ezra':'ezra','nehemiah':'nehemiah','esther':'esther','job':'job','psalms':'psalms','proverbs':'proverbs'}
def overlay(base, slug, out, pw):
    """Book title + subtitle (from the content module) over the sky inside the frame; the supplied bottom band is untouched."""
    m=importlib.import_module('content_'+MODS[slug]); fs=min(150,int(1120/(len(m.BOOK)*0.82)))
    import re; title=re.sub(r'^(\d)',r'<span style="font-family:Bitstream Charter,Caladea,serif">\1</span>',m.BOOK)  # lining numerals
    html=f"""<meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:1600px;height:2400px;position:relative;overflow:hidden;font-family:'GFS Baskerville','Libre Baskerville',Georgia,serif;text-align:center}}
.bg{{position:absolute;inset:0;background:url('{base.as_uri()}') center/100% 100%}}
.in{{position:absolute;left:150px;top:146px;width:1300px;height:760px;background:linear-gradient(180deg,rgba(9,13,22,.88) 0%,rgba(9,13,22,.74) 45%,rgba(9,13,22,0) 100%)}}
.t{{position:absolute;left:210px;right:210px;top:206px;text-shadow:0 3px 14px rgba(0,0,0,.7)}}
h1{{font-size:{fs}px;line-height:1.04;font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1;padding-left:.08em;color:#d9ad5e;background:linear-gradient(180deg,#fbeab8 5%,#e0b25c 50%,#b7832f 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;text-shadow:none;filter:drop-shadow(0 3px 8px rgba(0,0,0,.65))}}.rule{{width:170px;height:6px;background:#d8b25a;margin:26px auto 28px}}
.sub{{font-size:35px;line-height:1.55;letter-spacing:.13em;text-transform:uppercase;color:#ead9ad;text-wrap:balance;max-width:1000px;margin:0 auto}}</style>
<div class=bg></div><div class=in></div><div class=t><h1>{title}</h1><div class=rule></div><div class=sub>{m.SUBTITLE}</div></div>"""
    h=out.with_suffix('.html'); h.write_text(html)
    pg=pw.new_page(viewport={'width':1600,'height':2400}); pg.goto(h.as_uri()); pg.wait_for_timeout(400)
    pg.screenshot(path=str(out.with_suffix('.png'))); pg.close()
    Image.open(out.with_suffix('.png')).convert('RGB').save(out,quality=93)
    h.unlink(); out.with_suffix('.png').unlink()
ROOT=Path(__file__).resolve().parents[2]; art=Path(sys.argv[1])
def to23(im):
    w,h=im.size; tw=round(h*2/3)
    if tw<=w: x=(w-tw)//2; return im.crop((x,0,x+tw,h))
    th=round(w*3/2); y=(h-th)//2; return im.crop((0,y,w,y+th))
pw0=sync_playwright().start(); br=pw0.chromium.launch()
for f in sorted(art.glob('*')):
    if f.suffix.lower() not in('.png','.jpg') or f.stem.endswith('-1600') or f.stem.endswith('-raw'): continue
    slug=f.stem; im=to23(Image.open(f).convert('RGB'))
    raw=art/f'{slug}-raw.jpg'; im.resize((1600,2400),Image.LANCZOS).save(raw,quality=95)
    overlay(raw, slug, art/f'{slug}-1600.jpg', br)
    w=Image.open(art/f'{slug}-1600.jpg').resize((1024,1536),Image.LANCZOS)
    w.save(ROOT/f'assets/companion-{slug}-cover.jpg',quality=88); w.save(ROOT/f'assets/companion-{slug}-cover.webp',quality=85)
    print(slug,'ok')
br.close(); pw0.stop()
