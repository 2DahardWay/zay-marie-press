#!/usr/bin/env python3
"""Commentary volume builder (python-docx). Usage: python3 build.py [out.docx]
Reads content.py (META, ALL) and toc.json (heading -> footer page number; optional on first pass).
Page geometry follows the series standard: 9677 x 14515 twips, Roboto 10 pt body, margins top 864,
bottom 1224, left/right 1031, header 400, footer 475; tables and callouts 7615 twips wide, indent 100,
cell margins 100; cover is its own full-bleed section with no footer."""
import sys, os, re, json, zipfile, shutil, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from docx import Document
from docx.shared import Pt, Twips, RGBColor, Emu
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import content

NAVY = RGBColor(0x1B, 0x33, 0x50)
SLATE = '3B6E91'
CALL_FILL = 'E3EDF7'
FONT = 'Roboto'
TW = 7615  # text width, twips
META = content.META


# ---------- low-level helpers ----------
def rfonts(el, name=FONT):
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if el.get(qn(a)) is not None:
            del el.attrib[qn(a)]
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        el.set(qn(a), name)


def set_run_font(run, size=None, bold=None, italic=None, color=None):
    rPr = run._r.get_or_add_rPr()
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rPr.insert(0, rf)
    rfonts(rf)
    if size is not None: run.font.size = Pt(size)
    if bold is not None: run.font.bold = bold
    if italic is not None: run.font.italic = italic
    if color is not None: run.font.color.rgb = color


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn('w:shd')): tcPr.remove(old)
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def cell_margins(tbl, top=60, bottom=60, left=100, right=100):
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn('w:tblCellMar')): tblPr.remove(old)
    mar = OxmlElement('w:tblCellMar')
    for side, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement('w:' + side); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa'); mar.append(e)
    tblPr.append(mar)


def table_geometry(tbl, widths_tw, border_sz=6, border_color='1B3350', inside=True):
    tblPr = tbl._tbl.tblPr
    for tag in ('w:tblW', 'w:tblInd', 'w:tblLayout', 'w:tblBorders', 'w:jc'):
        for old in tblPr.findall(qn(tag)): tblPr.remove(old)
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), str(sum(widths_tw))); w.set(qn('w:type'), 'dxa'); tblPr.append(w)
    ind = OxmlElement('w:tblInd'); ind.set(qn('w:w'), '100'); ind.set(qn('w:type'), 'dxa'); tblPr.append(ind)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    b = OxmlElement('w:tblBorders')
    names = ['top', 'left', 'bottom', 'right'] + (['insideH', 'insideV'] if inside else [])
    for n in names:
        e = OxmlElement('w:' + n)
        e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), str(border_sz)); e.set(qn('w:space'), '0'); e.set(qn('w:color'), border_color)
        b.append(e)
    tblPr.append(b)
    grid = tbl._tbl.tblGrid
    for gc, wd in zip(grid.findall(qn('w:gridCol')), widths_tw):
        gc.set(qn('w:w'), str(wd))
    for row in tbl.rows:
        for c, wd in zip(row.cells, widths_tw):
            tcPr = c._tc.get_or_add_tcPr()
            for old in tcPr.findall(qn('w:tcW')): tcPr.remove(old)
            tcw = OxmlElement('w:tcW'); tcw.set(qn('w:w'), str(wd)); tcw.set(qn('w:type'), 'dxa'); tcPr.insert(0, tcw)


def row_flags(row, header=False):
    trPr = row._tr.get_or_add_trPr()
    cs = OxmlElement('w:cantSplit'); trPr.append(cs)
    if header:
        h = OxmlElement('w:tblHeader'); trPr.append(h)


def widths_from(fracs):
    tw = [int(round(TW * f)) for f in fracs]
    tw[-1] += TW - sum(tw)
    return tw


# inline markup: **bold**  //italic//
TOK = re.compile(r'(\*\*.+?\*\*|//.+?//)')


def add_runs(par, text, size=10, bold=None, italic=None, color=None):
    for part in TOK.split(text):
        if not part: continue
        if part.startswith('**') and part.endswith('**'):
            r = par.add_run(part[2:-2]); set_run_font(r, size, True, italic, color)
        elif part.startswith('//') and part.endswith('//'):
            r = par.add_run(part[2:-2]); set_run_font(r, size, bold, True, color)
        else:
            r = par.add_run(part); set_run_font(r, size, bold, italic, color)


# ---------- document ----------
class Builder:
    def __init__(self, toc):
        self.toc = toc
        self.doc = Document()
        self.last = None          # last body paragraph (for table spacing)
        self.after_table = False
        self.prev_kind = None
        self.setup_styles()
        self.cover()
        self.body_section()

    # styles
    def setup_styles(self):
        st = self.doc.styles
        for el in st.element.xpath('.//w:rFonts'): rfonts(el)
        dd = st.element.find(qn('w:docDefaults'))
        n = st['Normal']
        n.font.name = FONT; n.font.size = Pt(10)
        n.font.color.rgb = RGBColor(0, 0, 0)
        pf = n.paragraph_format
        pf.space_before = Pt(0); pf.space_after = Pt(6)
        pf.line_spacing = 1.08
        pf.widow_control = True
        h = st['Heading 1']
        h.font.name = FONT; h.font.size = Pt(17); h.font.bold = True; h.font.italic = False
        h.font.color.rgb = NAVY
        hp = h.paragraph_format
        hp.space_before = Pt(12); hp.space_after = Pt(8); hp.keep_with_next = True
        hp.line_spacing = 1.0
        for s in (n, h):
            rPr = s.element.get_or_add_rPr()
            rf = rPr.find(qn('w:rFonts'))
            if rf is None:
                rf = OxmlElement('w:rFonts'); rPr.insert(0, rf)
            rfonts(rf)
            c = rPr.find(qn('w:color'))
            if c is not None and c.get(qn('w:themeColor')) is not None:
                for a in ('w:themeColor', 'w:themeShade', 'w:themeTint'):
                    if c.get(qn(a)) is not None: del c.attrib[qn(a)]
        # kill the template's other heading/title styles' theme fonts (already done by xpath above)
        cp = self.doc.core_properties
        cp.title = META['title'] + ': ' + META['subtitle']
        cp.author = 'Zay-Marie Press'
        cp.subject = META['series']
        cp.keywords = ''; cp.comments = ''

    def page_setup(self, sec, cover=False):
        sec.page_width = Twips(9677); sec.page_height = Twips(14515)
        if cover:
            sec.top_margin = sec.bottom_margin = sec.left_margin = sec.right_margin = Twips(0)
            sec.header_distance = Twips(0); sec.footer_distance = Twips(0)
        else:
            sec.top_margin = Twips(864); sec.bottom_margin = Twips(1224)
            sec.left_margin = Twips(1031); sec.right_margin = Twips(1031)
            sec.header_distance = Twips(400); sec.footer_distance = Twips(475)

    def cover(self):
        sec = self.doc.sections[0]
        self.page_setup(sec, cover=True)
        p = self.doc.paragraphs[0] if self.doc.paragraphs else self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        img = os.path.join(HERE, 'cover_supplied.jpg')
        if not os.path.exists(img):
            import mkcover; mkcover.make(img)
        run = p.add_run()
        # text area: (9677-720)/20 pt wide, (14515-720)/20 pt tall; keep a hair under to avoid spill
        run.add_picture(img, width=Twips(9677), height=Twips(14515 - 80))

    def body_section(self):
        sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
        self.page_setup(sec)
        sec.footer.is_linked_to_previous = False
        sec.header.is_linked_to_previous = False
        pg = OxmlElement('w:pgNumType'); pg.set(qn('w:start'), '1')
        sec._sectPr.append(pg)
        fp = sec.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.paragraph_format.space_after = Pt(0)
        r = fp.add_run('ZAY-MARIE PRESS %s, VOLUME %d • ' % (META['series'].upper(), META['vol']))
        set_run_font(r, 9, False, False, RGBColor(0x40, 0x40, 0x40))
        r2 = fp.add_run(); set_run_font(r2, 11, False, False, RGBColor(0, 0, 0))
        for typ, txt in (('begin', None), (None, ' PAGE '), ('end', None)):
            if typ:
                fc = OxmlElement('w:fldChar'); fc.set(qn('w:fldCharType'), typ); r2._r.append(fc)
            else:
                it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = txt; r2._r.append(it)

    # ---- element writers ----
    def _gap_before(self, par, minimum=10):
        if self.after_table:
            cur = par.paragraph_format.space_before
            if cur is None or cur < Pt(minimum): par.paragraph_format.space_before = Pt(minimum)
            self.after_table = False

    def _gap_after_prev(self, minimum=10):
        if self.last is not None:
            cur = self.last.paragraph_format.space_after
            if cur is None or cur < Pt(minimum): self.last.paragraph_format.space_after = Pt(minimum)

    def h1(self, text, new_page=False):
        p = self.doc.add_paragraph(text, style='Heading 1')
        for r in p.runs: set_run_font(r)
        if new_page: p.paragraph_format.page_break_before = True
        self._gap_before(p, 12)
        self.last = p; self.prev_kind = 'h1'
        return p

    def sub(self, text):
        p = self.doc.add_paragraph()
        add_runs(p, text, 10, bold=True)
        pf = p.paragraph_format
        pf.space_before = Pt(4); pf.space_after = Pt(4); pf.keep_with_next = True
        self._gap_before(p)
        self.last = p; self.prev_kind = 'sub'

    def p(self, text, keep=False):
        par = self.doc.add_paragraph()
        add_runs(par, text, 10)
        par.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if keep: par.paragraph_format.keep_with_next = True
        self._gap_before(par)
        self.last = par; self.prev_kind = 'p'

    def lst(self, items, numbered=False):
        n = len(items)
        for i, t in enumerate(items, 1):
            par = self.doc.add_paragraph()
            pf = par.paragraph_format
            ind, hang = (480, 480) if numbered else (360, 260)
            pf.left_indent = Twips(ind); pf.first_line_indent = Twips(-hang)
            pf.space_after = Pt(6 if i == n else 0)
            pf.tab_stops.add_tab_stop(Twips(ind))
            lead = ('%d.' % i) if numbered else '•'
            r = par.add_run(lead + '\t'); set_run_font(r, 10)
            add_runs(par, t, 10)
            if i == 1: self._gap_before(par)
            self.last = par
        self.prev_kind = 'list'

    def _table(self, rows, widths_tw, header_fill=SLATE, header_white=True, kjv_col=None):
        self._gap_after_prev()
        t = self.doc.add_table(rows=len(rows), cols=len(widths_tw))
        t.alignment = WD_TABLE_ALIGNMENT.LEFT
        cell_margins(t)
        table_geometry(t, widths_tw)
        for ri, row in enumerate(rows):
            tr = t.rows[ri]
            row_flags(tr, header=(ri == 0))
            for ci, txt in enumerate(row):
                c = tr.cells[ci]
                par = c.paragraphs[0]
                par.paragraph_format.space_after = Pt(0); par.paragraph_format.space_before = Pt(0)
                par.paragraph_format.line_spacing = 1.08
                if ri == 0:
                    shade(c, header_fill)
                    add_runs(par, txt, 10, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
                else:
                    add_runs(par, txt, 10)
        self.after_table = True; self.last = None; self.prev_kind = 'table'
        return t

    def tbl(self, intro, rows, widths):
        if intro: self.p(intro)
        if self.prev_kind == 'table': raise SystemExit('two tables adjacent: put a paragraph between them')
        data = [['Verse', 'KJV text', 'What to observe']] + [list(r) for r in rows]
        self._table(data, widths_from(widths))

    def ctbl(self, intro, rows, widths):
        if intro: self.p(intro)
        if self.prev_kind == 'table': raise SystemExit('two tables adjacent: put a paragraph between them')
        self._table([list(r) for r in rows], widths_from(widths))

    def call(self, title, text):
        if self.prev_kind == 'table': raise SystemExit('callout directly after a table: put a paragraph between them')
        self._gap_after_prev()
        t = self.doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.LEFT
        cell_margins(t, top=100, bottom=100)
        table_geometry(t, [TW], border_sz=8, inside=False)
        row_flags(t.rows[0])
        c = t.rows[0].cells[0]
        shade(c, CALL_FILL)
        par = c.paragraphs[0]
        par.paragraph_format.space_after = Pt(2); par.paragraph_format.space_before = Pt(0)
        r = par.add_run(title.upper()); set_run_font(r, 10, True, False, NAVY)
        par.paragraph_format.keep_with_next = True
        body = c.add_paragraph()
        body.paragraph_format.space_after = Pt(0); body.paragraph_format.line_spacing = 1.08
        add_runs(body, text, 10)
        self.after_table = True; self.last = None; self.prev_kind = 'table'

    def bib(self, text):
        par = self.doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Twips(360); pf.first_line_indent = Twips(-360); pf.space_after = Pt(4)
        add_runs(par, text, 10)
        self._gap_before(par)
        self.last = par; self.prev_kind = 'bib'

    def imprint(self):
        par = self.doc.add_paragraph()
        par.paragraph_format.space_before = Pt(14); par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.keep_together = True
        add_runs(par, META['imprint'], 9, italic=False)
        self._gap_before(par, 14)

    def toc_page(self):
        self.h1('Table of Contents')
        for el in content.ALL:
            if el[0] != 'h1': continue
            title = el[1]
            par = self.doc.add_paragraph()
            par.paragraph_format.tab_stops.add_tab_stop(Twips(TW), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
            pg = self.toc.get(title, 0)
            r = par.add_run(title + '\t' + (str(pg) if pg else '0')); set_run_font(r, 10)
            self.last = par
        self.prev_kind = 'toc'

    def build(self):
        self.toc_page()
        first = True
        for el in content.ALL:
            k = el[0]
            if k == 'h1':
                self.h1(el[1], new_page=(el[1] in ('Preface','Bibliography')))
            elif k == 'sub': self.sub(el[1])
            elif k == 'p': self.p(el[1])
            elif k == 'call': self.call(el[1], el[2])
            elif k == 'ctbl': self.ctbl(el[1], el[2], el[3])
            elif k == 'tbl': self.tbl(el[1], el[2], el[3])
            elif k == 'bul': self.lst(el[1], False)
            elif k == 'num': self.lst(el[1], True)
            elif k == 'bib': self.bib(el[1])
            else: raise SystemExit('unknown element %r' % (k,))
        self.imprint()


def patch_theme(path):
    """Set the theme fonts to Roboto so no heading falls back to Calibri/Cambria."""
    tmp = path + '.tmp'
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.startswith('word/theme/') and item.filename.endswith('.xml'):
                s = data.decode('utf-8')
                s = re.sub(r'(<a:(?:major|minor)Font>\s*<a:latin typeface=")[^"]*(")', r'\1Roboto\2', s)
                data = s.encode('utf-8')
            zout.writestr(item, data)
    shutil.move(tmp, path)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out', 'volume.docx')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    tocp = os.path.join(HERE, 'toc.json')
    toc = json.load(open(tocp)) if os.path.exists(tocp) else {}
    b = Builder(toc)
    b.build()
    b.doc.save(out)
    patch_theme(out)
    print('built', out)


if __name__ == '__main__':
    main()
