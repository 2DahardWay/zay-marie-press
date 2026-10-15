#!/usr/bin/env python3
"""Full-bleed individual cover art (no frame or border): title, subtitle and the series line are set over the artwork.
usage: python3 apply_cover_art_fullbleed.py <art_dir> [--asis slug,slug]   <art_dir> holds <slug>.png|jpg (~2:3). --asis: covers already lettered by the publisher (used as supplied, no overlay).
Writes assets/companion-<slug>-cover.jpg/.webp (1024x1536) and <art_dir>/<slug>-1600.jpg (PDF cover, build_packet.py ART=<art_dir>)."""
import sys, importlib, re
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).resolve().parent))
asis=set(sys.argv[sys.argv.index('--asis')+1].split(',')) if '--asis' in sys.argv else set()
def overlay(base, slug, out, pw):
    m=importlib.import_module('content_'+slug.replace('-','')); fs=min(150,int(1250/(len(m.BOOK)*0.82)))
    title=re.sub(r'^(\d)',r'<span style="font-family:Bitstream Charter,Caladea,serif">\1</span>',m.BOOK)
    html=f"""<meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:1600px;height:2400px;position:relative;overflow:hidden;font-family:'GFS Baskerville','Libre Baskerville',Georgia,serif;text-align:center}}
.bg{{position:absolute;inset:0;background:url('{base.as_uri()}') center/100% 100%}}
.top{{position:absolute;left:0;top:0;width:1600px;height:980px;background:linear-gradient(180deg,rgba(8,11,19,.9) 0%,rgba(8,11,19,.78) 45%,rgba(8,11,19,0) 100%)}}
.bot{{position:absolute;left:0;bottom:0;width:1600px;height:420px;background:linear-gradient(0deg,rgba(8,11,19,.92) 0%,rgba(8,11,19,.7) 55%,rgba(8,11,19,0) 100%)}}
.t{{position:absolute;left:150px;right:150px;top:140px}}
h1{{font-size:{fs}px;line-height:1.04;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding-left:.08em;background:linear-gradient(180deg,#fbeab8 5%,#e0b25c 50%,#b7832f 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;filter:drop-shadow(0 3px 8px rgba(0,0,0,.65))}}.rule{{width:170px;height:6px;background:#d8b25a;margin:26px auto 28px}}
.sub{{font-size:35px;line-height:1.55;letter-spacing:.13em;text-transform:uppercase;color:#ead9ad;text-wrap:balance;max-width:1050px;margin:0 auto;text-shadow:0 2px 10px rgba(0,0,0,.8)}}
.b{{position:absolute;left:0;right:0;bottom:92px;text-transform:uppercase;font-weight:700}}
.b1{{font-size:38px;letter-spacing:.14em;color:#e9d29a;text-shadow:0 2px 10px rgba(0,0,0,.85)}}.b2{{font-size:46px;letter-spacing:.14em;color:#f4e6bf;margin-top:18px;text-shadow:0 2px 10px rgba(0,0,0,.85)}}</style>
<div class=bg></div><div class=top></div><div class=bot></div><div class=t><h1>{title}</h1><div class=rule></div><div class=sub>{m.SUBTITLE}</div></div><div class=b><div class=b1>Bible Book Companion Series</div><div class=b2>Zay-Marie Press</div></div>"""
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
    if slug in asis: Image.open(raw).save(art/f'{slug}-1600.jpg',quality=93)
    else: overlay(raw, slug, art/f'{slug}-1600.jpg', br)
    w=Image.open(art/f'{slug}-1600.jpg').resize((1024,1536),Image.LANCZOS)
    w.save(ROOT/f'assets/companion-{slug}-cover.jpg',quality=88); w.save(ROOT/f'assets/companion-{slug}-cover.webp',quality=85)
    print(slug,'ok')
br.close(); pw0.stop()
