import re, sys, json
from docx import Document
from docx.shared import Pt, Twips, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import qn, nsdecls
from docx.enum.section import WD_SECTION

NAVY = '1B3350'; SLATE = '3B6E91'; BORDER = '2B4F6B'; CALLFILL = 'DCE9F5'
PAGE_W, PAGE_H = 9677, 14515
TEXT_W = 7615
TITLE = 'Unequally Yoked'
SUB = 'What Paul Commands, What He Quotes, and What He Applies in 2 Corinthians 6:14–7:1'
TOCPAGES = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}

def smart(s):
    s = s.replace('...', '…')
    out = []
    for i, ch in enumerate(s):
        prev = s[i-1] if i else ' '
        if ch == '"':
            out.append('“' if (prev in ' \t([—–' or i == 0) else '”')
        elif ch == "'":
            out.append('‘' if (prev in ' \t([“' or i == 0) else '’')
        else:
            out.append(ch)
    return ''.join(out)

d = Document()
# styles
st = d.styles['Normal']
st.font.name = 'Roboto'; st.font.size = Pt(10)
rpr = st.element.get_or_add_rPr()
rf = rpr.find(qn('w:rFonts'))
for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
    rf.set(qn(a), 'Roboto')
st.paragraph_format.space_after = Pt(6); st.paragraph_format.space_before = Pt(0)
st.paragraph_format.line_spacing = 1.08

body = d.element.body
for e in list(body):
    if e.tag != qn('w:sectPr'): body.remove(e)

def set_sect(sec, top, bottom, left, right, header=400, footer=475):
    sec.page_width = Twips(PAGE_W); sec.page_height = Twips(PAGE_H)
    sec.top_margin = Twips(top); sec.bottom_margin = Twips(bottom)
    sec.left_margin = Twips(left); sec.right_margin = Twips(right)
    sec.header_distance = Twips(header); sec.footer_distance = Twips(footer)

sec0 = d.sections[0]
set_sect(sec0, 360, 360, 360, 360)

def run(p, text, bold=False, ital=False, size=None, color=None, caps=False):
    r = p.add_run(smart(text))
    r.font.name = 'Roboto'
    rpr = r._r.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rf.set(qn(a), 'Roboto')
    r.bold = bold or None; r.italic = ital or None
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = RGBColor.from_string(color)
    return r

def inline(p, text, base_bold=False, size=None, color=None):
    # **bold** and *italic*
    pos = 0
    for m in re.finditer(r'\*\*(.+?)\*\*|\*(.+?)\*', text):
        if m.start() > pos: run(p, text[pos:m.start()], bold=base_bold, size=size, color=color)
        if m.group(1) is not None: run(p, m.group(1), bold=True, size=size, color=color)
        else: run(p, m.group(2), bold=base_bold, ital=True, size=size, color=color)
        pos = m.end()
    if pos < len(text): run(p, text[pos:], bold=base_bold, size=size, color=color)

def para(text='', before=0, after=6, keep_next=False, align=None, left=None, hanging=None, container=None):
    p = (container or d).add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before); pf.space_after = Pt(after); pf.line_spacing = 1.08
    pf.keep_with_next = keep_next or None
    pf.widow_control = True
    if align: p.alignment = align
    if left is not None: pf.left_indent = Twips(left)
    if hanging is not None: pf.first_line_indent = Twips(-hanging)
    if text: inline(p, text)
    return p

def last_p():
    ps = [e for e in body if e.tag == qn('w:p')]
    return ps[-1] if ps else None

def ensure_after_prev(min_pt=10):
    """paragraph/heading before a table gets >= 10pt space-after"""
    kids = [e for e in body if e.tag != qn('w:sectPr')]
    if not kids: return
    prev = kids[-1]
    if prev.tag != qn('w:p'): return
    pPr = prev.find(qn('w:pPr'))
    if pPr is None: pPr = OxmlElement('w:pPr'); prev.insert(0, pPr)
    sp = pPr.find(qn('w:spacing'))
    if sp is None: sp = OxmlElement('w:spacing'); pPr.append(sp)
    cur = int(sp.get(qn('w:after'), '0'))
    if cur < min_pt * 20: sp.set(qn('w:after'), str(min_pt * 20))
    # a heading directly before a table keeps with it
    kn = pPr.find(qn('w:keepNext'))

after_table = [False]
def start_para_fix(p):
    if after_table[0]:
        pf = p.paragraph_format
        if (pf.space_before or Pt(0)) < Pt(10): pf.space_before = Pt(10)
        after_table[0] = False

def h1(text, pagebreak=False):
    p = para(before=12, after=8, keep_next=True)
    start_para_fix(p)
    if pagebreak: p.paragraph_format.page_break_before = True
    run(p, text, bold=True, size=17, color=NAVY)
    p.style = d.styles['Normal']
    return p

def h2(text):
    p = para(before=10, after=5, keep_next=True); start_para_fix(p)
    run(p, text, bold=True, size=12, color=NAVY)
    return p

def sub(text):
    p = para(before=4, after=6, keep_next=True); start_para_fix(p)
    run(p, text, bold=True)
    return p

def bullets(items):
    for i, t in enumerate(items):
        p = para(after=(6 if i == len(items)-1 else 0), left=360, hanging=360 // 2 + 40)
        p.paragraph_format.first_line_indent = Twips(-220)
        p.paragraph_format.left_indent = Twips(440)
        if i == 0: start_para_fix(p)
        run(p, '•\t')
        # tab stop at left indent
        pPr = p._p.get_or_add_pPr()
        tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="440"/></w:tabs>')
        pPr.append(tabs)
        inline(p, t)

def numbered(items, letters=False, left=440, hang=360, after_last=6, start=1):
    for i, t in enumerate(items):
        p = para(after=(after_last if i == len(items)-1 else 0))
        p.paragraph_format.left_indent = Twips(left)
        p.paragraph_format.first_line_indent = Twips(-hang)
        if i == 0: start_para_fix(p)
        pPr = p._p.get_or_add_pPr()
        pPr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="{left}"/></w:tabs>'))
        label = (chr(65+i) if letters else str(start+i)) + '.'
        run(p, label + '\t')
        inline(p, t)

def cell_xml(width, fill, borders=True, mar=None):
    bd = ''.join(f'<w:{s} w:val="single" w:sz="8" w:space="0" w:color="{BORDER}"/>' for s in ('top', 'left', 'bottom', 'right'))
    m = mar or (70, 100, 70, 100)
    return (f'<w:tcPr><w:tcW w:w="{width}" w:type="dxa"/><w:tcBorders>{bd}</w:tcBorders>'
            f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
            f'<w:tcMar><w:top w:w="{m[0]}" w:type="dxa"/><w:left w:w="{m[1]}" w:type="dxa"/><w:bottom w:w="{m[2]}" w:type="dxa"/><w:right w:w="{m[3]}" w:type="dxa"/></w:tcMar></w:tcPr>')

def add_tbl(xml_el):
    sect = body.find(qn('w:sectPr'))
    sect.addprevious(xml_el)

def table(rows, ratios, tall=False):
    ensure_after_prev(10)
    tot = sum(ratios); W = [int(round(r / tot * TEXT_W)) for r in ratios]; W[-1] = TEXT_W - sum(W[:-1])
    x = (f'<w:tbl {nsdecls("w")}><w:tblPr><w:tblW w:w="{TEXT_W}" w:type="dxa"/><w:tblInd w:w="100" w:type="dxa"/>'
         f'<w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>' + ''.join(f'<w:gridCol w:w="{w}"/>' for w in W) + '</w:tblGrid>')
    for ri, row in enumerate(rows):
        hdr = ri == 0
        trpr = '<w:trPr><w:cantSplit/>' + ('<w:trHeight w:val="1500" w:hRule="atLeast"/>' if (tall and not hdr) else '') + ('<w:tblHeader/>' if hdr else '') + '</w:trPr>'
        x += '<w:tr>' + trpr
        for ci, cell in enumerate(row):
            fill = SLATE if hdr else 'FFFFFF'
            x += f'<w:tc>{cell_xml(W[ci], fill)}<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="259" w:lineRule="auto"/>' + ('<w:keepNext/>' if ri < 1 else '') + '</w:pPr></w:p></w:tc>'
        x += '</w:tr>'
    x += '</w:tbl>'
    t = parse_xml(x)
    # fill text
    for ri, tr in enumerate(t.findall(qn('w:tr'))):
        for ci, tc in enumerate(tr.findall(qn('w:tc'))):
            p = tc.find(qn('w:p'))
            from docx.text.paragraph import Paragraph
            P = Paragraph(p, d)
            txt = rows[ri][ci]
            if txt:
                if ri == 0:
                    run(P, txt, bold=True, color='FFFFFF')
                else:
                    inline(P, txt)
    add_tbl(t)
    after_table[0] = True

def callout(title, text_lines):
    ensure_after_prev(10)
    bd = ''.join(f'<w:{s} w:val="single" w:sz="8" w:space="0" w:color="{NAVY}"/>' for s in ('top', 'left', 'bottom', 'right'))
    x = (f'<w:tbl {nsdecls("w")}><w:tblPr><w:tblW w:w="{TEXT_W}" w:type="dxa"/><w:tblInd w:w="100" w:type="dxa"/><w:tblLayout w:type="fixed"/></w:tblPr>'
         f'<w:tblGrid><w:gridCol w:w="{TEXT_W}"/></w:tblGrid><w:tr><w:trPr><w:cantSplit/></w:trPr><w:tc><w:tcPr><w:tcW w:w="{TEXT_W}" w:type="dxa"/>'
         f'<w:tcBorders>{bd}</w:tcBorders><w:shd w:val="clear" w:color="auto" w:fill="{CALLFILL}"/>'
         f'<w:tcMar><w:top w:w="140" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="140" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tcMar></w:tcPr>'
         f'<w:p><w:pPr><w:spacing w:before="0" w:after="60" w:line="259" w:lineRule="auto"/><w:ind w:left="60" w:right="60"/></w:pPr></w:p></w:tc></w:tr></w:tbl>')
    t = parse_xml(x)
    tc = t.find('.//' + qn('w:tc'))
    from docx.text.paragraph import Paragraph
    p0 = Paragraph(tc.find(qn('w:p')), d)
    run(p0, title, bold=True, color=NAVY)
    for ln in text_lines:
        pe = parse_xml(f'<w:p {nsdecls("w")}><w:pPr><w:spacing w:before="0" w:after="0" w:line="259" w:lineRule="auto"/><w:ind w:left="60" w:right="60"/></w:pPr></w:p>')
        tc.append(pe)
        inline(Paragraph(pe, d), ln)
    add_tbl(t)
    after_table[0] = True

def add_field(par, instr, size=8.5, color='333333'):
    r = par.add_run(); r.font.name = 'Roboto'; r.font.size = Pt(size); r.font.color.rgb = RGBColor.from_string(color)
    for tag, extra in (('begin', ''), ('instr', instr), ('sep', ''), ('text', '1'), ('end', '')):
        if tag == 'instr':
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = ' ' + instr + ' '; r._r.append(e)
        elif tag == 'text':
            t = OxmlElement('w:t'); t.text = '1'; r._r.append(t)
        else:
            fc = OxmlElement('w:fldChar'); fc.set(qn('w:fldCharType'), {'begin': 'begin', 'sep': 'separate', 'end': 'end'}[tag]); r._r.append(fc)

# ---------- cover ----------
p = para(after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
p.paragraph_format.line_spacing = 1.0
w = (PAGE_W - 720) / 20.0
p.add_run().add_picture('study-88-cover.jpg', width=Pt(w))

# ---------- interior section ----------
sec1 = d.add_section(WD_SECTION.NEW_PAGE)
set_sect(sec1, 864, 1224, 1031, 1031)
from docx.oxml import OxmlElement as _OE
from docx.oxml.ns import qn as _qn
_pg=_OE('w:pgNumType'); _pg.set(_qn('w:start'),'1'); sec1._sectPr.append(_pg)
sec1.footer.is_linked_to_previous = False
fp = sec1.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
fp.paragraph_format.space_after = Pt(0); fp.paragraph_format.space_before = Pt(0)
r = fp.add_run('ZAY-MARIE PRESS DIGITAL STUDIES SERIES  •  '); r.font.name = 'Roboto'; r.font.size = Pt(8.5); r.font.color.rgb = RGBColor.from_string('333333')
add_field(fp, 'PAGE')
# cover section footer empty
sec0.footer.is_linked_to_previous = False

# TOC (placeholder entries filled from TOCPAGES)
src = open(sys.argv[1], encoding='utf-8').read().split('\n')
heads = []
for ln in src:
    m = re.match(r'#(!?) (.+)', ln)
    if m and not ln.startswith('##'): heads.append(m.group(2).strip())

p = para(before=12, after=8, keep_next=True); run(p, 'Table of Contents', bold=True, size=17, color=NAVY)
for h in heads:
    p = para(after=6)
    pPr = p._p.get_or_add_pPr()
    pPr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="{TEXT_W}"/></w:tabs>'))
    # strip trailing quote ornaments for TOC label
    run(p, h + '\t' + str(TOCPAGES.get(h, 0)))

# ---------- body ----------
i = 0
lines = src
def flush_para(buf):
    if buf:
        p = para(' '.join(buf)); start_para_fix(p)
buf = []
while i < len(lines):
    ln = lines[i]
    if not ln.strip():
        flush_para(buf); buf = []; i += 1; continue
    m = re.match(r'#(!?) (.+)', ln)
    if m and not ln.startswith('##'):
        flush_para(buf); buf = []
        first = m.group(2).strip()
        h1(first, pagebreak=(m.group(1) == '!') or first == 'Table of Contents')
        i += 1; continue
    if ln.startswith('## '):
        flush_para(buf); buf = []; h2(ln[3:].strip()); i += 1; continue
    if ln.startswith('### '):
        flush_para(buf); buf = []; sub(ln[4:].strip()); i += 1; continue
    if ln.startswith('::: callout'):
        flush_para(buf); buf = []
        title = ln[len('::: callout'):].strip(); body_lines = []; i += 1
        while not lines[i].startswith(':::'):
            if lines[i].strip(): body_lines.append(lines[i].strip())
            i += 1
        callout(title, body_lines); i += 1; continue
    if ln.startswith('::: table'):
        flush_para(buf); buf = []
        opts = ln[len('::: table'):].split()
        ratios = [int(x) for x in opts[0].split(',')]; tall = 'tall' in opts
        rows = []; i += 1
        while not lines[i].startswith(':::'):
            if lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells)
            i += 1
        table(rows, ratios, tall); i += 1; continue
    if ln.startswith('- '):
        flush_para(buf); buf = []; items = []
        while i < len(lines) and lines[i].startswith('- '):
            items.append(lines[i][2:].strip()); i += 1
        bullets(items); continue
    mnum = re.match(r'(\d+)\. ', ln)
    if mnum:
        flush_para(buf); buf = []; items = []; st0 = int(mnum.group(1))
        while i < len(lines) and re.match(r'\d+\. ', lines[i]):
            items.append(re.sub(r'^\d+\. ', '', lines[i]).strip()); i += 1
        numbered(items, start=st0); continue
    if re.match(r'[A-C]\. ', ln):
        flush_para(buf); buf = []; items = []
        while i < len(lines) and re.match(r'[A-C]\. ', lines[i]):
            items.append(re.sub(r'^[A-C]\. ', '', lines[i]).strip()); i += 1
        numbered(items, letters=True, left=800, hang=360, after_last=8); continue
    buf.append(ln.strip()); i += 1
flush_para(buf)

# imprint
p = para(before=18, after=5, keep_next=True); start_para_fix(p)
run(p, 'ZAY-MARIE PRESS DIGITAL STUDIES', bold=True, color=NAVY)
p = para(before=0, after=0)
p.paragraph_format.keep_together = True
run(p, 'Copyright © 2026 Alexander S. Marien. All rights reserved. Published by Zay-Marie Press. Licensed for the personal use of the purchaser; no part may be reproduced or distributed without permission. Scripture quotations are from the King James Version (KJV).')

# spacing fix: callout/table after headings; ensure keep-with-next on short lead-in paragraphs before bullets handled by authoring
d.core_properties.title = 'Study 88 Draft: ' + TITLE
d.core_properties.author = 'Alexander S. Marien'
out = sys.argv[3] if len(sys.argv) > 3 else 'out.docx'
d.save(out)
print('saved', out, len(heads), 'toc heads')
json.dump(heads, open('heads.json', 'w'))
