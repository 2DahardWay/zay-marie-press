#!/usr/bin/env python3
"""Build a Bible Companion (new ten-section structure) as a PDF: genre cover + Roboto interior.
Usage: python3 build_packet.py <content_module> <out_dir>
Interior page 483.846 x 725.754 pt, margins per Master Standard 1.47; Roboto only; cover is an image page."""
import sys, importlib, subprocess, re, os, json
from pathlib import Path
from playwright.sync_api import sync_playwright
import pikepdf

ROOT = Path(__file__).resolve().parents[2]
mod = importlib.import_module(sys.argv[1]); out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
slug = mod.BOOK.lower().replace(" ", "-")
NAVY, GOLD, SLATE = "#1B3350", "#b8871c", "#3B6E91"
OT = mod.TESTAMENT == "Old Testament"
PANEL = "#082d45" if OT else "#0b3a24"

def cover_png(path):
    photo = (ROOT / f"assets/genre/packet-genre-{mod.GENRE}.jpg").as_uri()
    html = f"""<meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:1200px;height:1800px;background:{PANEL};position:relative;overflow:hidden;font-family:Georgia,'DejaVu Serif',serif;color:#fff;text-align:center}}
.ph{{position:absolute;left:0;top:0;width:1200px;height:1020px;background:url('{photo}') center/cover}}
.fade{{position:absolute;left:0;top:560px;width:1200px;height:470px;background:linear-gradient(180deg,rgba(0,0,0,0),{PANEL} 96%)}}
.bar{{position:absolute;left:0;top:0;width:1200px;height:14px;background:{GOLD}}}
.t{{position:absolute;left:90px;right:90px;top:960px}}
.k{{font:700 28px Arial,sans-serif;letter-spacing:.26em;color:#e2c47c;margin-bottom:14px}}.tt{{font:700 24px Arial,sans-serif;letter-spacing:.2em;color:#cfe0ec;margin-bottom:34px;text-transform:uppercase}}
h1{{font-size:124px;line-height:1.04;margin:0 0 30px;font-weight:700}}.rule{{width:150px;height:6px;background:{GOLD};margin:0 auto 30px}}
.sub{{font-style:italic;font-size:44px;line-height:1.38;color:#dbe6ee}}
.foot{{position:absolute;left:0;right:0;bottom:70px}}.foot b{{display:block;font:700 28px Arial,sans-serif;letter-spacing:.24em;color:#e2c47c;margin-bottom:12px}}.foot span{{font:24px Arial,sans-serif;letter-spacing:.12em;color:#cfe0ec}}</style>
<div class=ph></div><div class=fade></div><div class=bar></div>
<div class=t><div class=k>BIBLE COMPANION SERIES</div><div class=tt>{mod.TESTAMENT}</div><h1>{mod.BOOK}</h1><div class=rule></div><div class=sub>{mod.SUBTITLE}</div></div>
<div class=foot><b>ZAY-MARIE PRESS</b><span>Scripture: King James Version</span></div>"""
    Path("/tmp/_cover.html").write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width":1200,"height":1800}); pg.goto("file:///tmp/_cover.html"); pg.wait_for_timeout(500)
        pg.screenshot(path=str(path)); b.close()

def esc(s): return s  # content is trusted markup (<b>, <i>)

def blocks_html(blocks):
    h = []
    for b in blocks:
        k = b[0]
        if k == "p": h.append(f"<p>{b[1]}</p>")
        elif k == "h3": h.append(f"<p class='sub'>{b[1]}</p>")
        elif k == "ul": h.append("<ul>" + "".join(f"<li>{x}</li>" for x in b[1]) + "</ul>")
        elif k == "ol": h.append("<ol>" + "".join(f"<li>{x}</li>" for x in b[1]) + "</ol>")
        elif k == "olr": h.append("<ol class='roman'>" + "".join(f"<li>{x}</li>" for x in b[1]) + "</ol>")
        elif k == "box": h.append(f"<div class='box'><div class='bt'>{b[1].upper().rstrip(':')}</div><p>{b[2]}</p></div>")
        elif k == "table":
            head, rows, widths = b[1], b[2], b[3]
            cg = "".join(f"<col style='width:{w}%'>" for w in widths)
            th = "".join(f"<th>{x}</th>" for x in head)
            tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
            h.append(f"<table><colgroup>{cg}</colgroup><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>")
    return "\n".join(h)

def interior_html(toc_pages):
    toc = "".join(f"<div class='toc'><span>{n}. {t}</span><i></i><span>{toc_pages.get(n, '00')}</span></div>" for n, t, _ in mod.SECTIONS)
    body = "".join(f"<h1 id='s{n}'>{n}. {t}</h1>{blocks_html(bl)}" for n, t, bl in mod.SECTIONS)
    return f"""<!doctype html><meta charset=utf-8><style>
@page{{size:483.846pt 725.754pt;margin:43.2pt 51.55pt 61.2pt 51.55pt;@bottom-center{{content:"ZAY-MARIE PRESS BIBLE COMPANION SERIES • " counter(page);font:400 8pt Roboto;color:#000}}}}
*{{box-sizing:border-box}}body{{margin:0;font:400 10pt/1.08 Roboto;color:#000}}
#s10{{break-before:page}}p{{margin:0 0 6pt}}h1{{font:700 17pt/1.15 Roboto;color:{NAVY};margin:12pt 0 8pt;break-after:avoid}}
.kicker{{font:700 9pt Roboto;letter-spacing:.12em;color:{NAVY};margin:0 0 6pt}}
.title{{font:700 24pt/1.12 Roboto;color:{NAVY};margin:0 0 6pt}}.subtitle{{font:italic 12pt/1.25 Roboto;margin:0 0 12pt}}
.rule{{height:2pt;background:{GOLD};margin:0 0 12pt}}
.toch{{font:700 12pt Roboto;color:{NAVY};margin:10pt 0 6pt}}
.toc{{display:flex;align-items:baseline;margin:0 0 6pt;line-height:1.08}}.toc i{{flex:1;border-bottom:1pt dotted #000;margin:0 4pt;transform:translateY(-2pt)}}
.sub{{margin:5pt 0 1pt;break-after:avoid}}h1+.sub{{margin-top:0}}
ul,ol{{margin:0 0 6pt;padding-left:22pt}}li{{margin:0 0 4pt}}ul li:last-child,ol li:last-child{{margin-bottom:0}}ol.roman{{list-style:upper-roman}}
.box{{background:#EAF1F8;border:1pt solid {NAVY};padding:7pt 9pt;margin:10pt 0;break-inside:avoid}}.bt{{font:700 10pt Roboto;letter-spacing:.04em;color:{NAVY};margin:0 0 4pt}}.box p{{margin:0}}
table{{break-inside:avoid;width:100%;border-collapse:collapse;margin:10pt 0;table-layout:fixed}}th{{background:{SLATE};color:#fff;font:700 9pt Roboto;text-align:left;padding:4pt 5pt;border:.75pt solid {SLATE}}}
td{{font:400 9pt/1.15 Roboto;padding:4pt 5pt;border:.75pt solid #9bb0c2;vertical-align:top;background:#fff}}tr{{break-inside:avoid}}thead{{display:table-header-group}}
</style><body>
<div class=kicker>ZAY-MARIE PRESS | BIBLE COMPANIONS</div><div class=title>Bible Companion — {mod.BOOK}</div><div class=subtitle>{mod.SUBTITLE}</div><div class=rule></div>
<div class=toch>Table of Contents</div>{toc}
{body}"""

def render(html, pdf):
    Path("/tmp/_int.html").write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto("file:///tmp/_int.html"); pg.wait_for_timeout(700)
        pg.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True, display_header_footer=False); b.close()

def page_map(pdf):
    res = {}
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout).group(1))
    for pg in range(1, n+1):
        txt = subprocess.run(["pdftotext", "-f", str(pg), "-l", str(pg), "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
        for num, t, _ in mod.SECTIONS:
            if num not in res and re.search(rf"^\s*{num}\. {re.escape(t)}\s*$", txt, re.M):
                res[num] = pg
    return res

tmp = out / f"_{slug}-interior.pdf"
render(interior_html({}), tmp)
pm = page_map(tmp)
render(interior_html(pm), tmp)
pm2 = page_map(tmp)
assert pm == pm2, (pm, pm2)
cov = out / f"{slug}-cover.png"; cover_png(cov)
final = out / f"doctrinal-packet-{slug}.pdf"
coverpdf = out / "_cover.pdf"
from PIL import Image
Image.open(cov).convert("RGB").save(coverpdf, "PDF", resolution=1200/6.7200)
c = pikepdf.open(coverpdf); i = pikepdf.open(tmp)
c.pages[0].MediaBox = [0, 0, 483.846, 725.754]
dst = pikepdf.Pdf.new(); dst.pages.append(c.pages[0])
for p in i.pages: dst.pages.append(p)
dst.save(final)
print(final, "pages:", len(dst.pages), "toc:", pm)
