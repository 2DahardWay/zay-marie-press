import sys,re,copy,zipfile,shutil,json
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XML='http://www.w3.org/XML/1998/namespace'
def q(t): return '{%s}%s'%(W,t)
src,dst,numsfile,with_bib=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]=='1'
nums=json.load(open(numsfile)) if numsfile!='-' else {}
z=zipfile.ZipFile(src)
doc=etree.fromstring(z.read('word/document.xml'))
body=doc.find(q('body'))
def ptext(p): return ''.join(t.text or '' for t in p.iter(q('t')))
def pstyle(p):
    s=p.find(q('pPr')+'/'+q('pStyle'))
    return s.get(q('val')) if s is not None else None
def mkp(style=None,text='',jc=None,after=None,before=None,left=None,hanging=None,keep=False,runs=None,tabs=None):
    p=etree.Element(q('p')); ppr=etree.SubElement(p,q('pPr'))
    if style: etree.SubElement(ppr,q('pStyle')).set(q('val'),style)
    if keep: etree.SubElement(ppr,q('keepNext'))
    if tabs:
        t=etree.SubElement(ppr,q('tabs')); tb=etree.SubElement(t,q('tab')); tb.set(q('val'),'right'); tb.set(q('leader'),'dot'); tb.set(q('pos'),str(tabs))
    if after is not None or before is not None:
        s=etree.SubElement(ppr,q('spacing'))
        if before is not None: s.set(q('before'),str(before))
        if after is not None: s.set(q('after'),str(after))
    if left is not None:
        i=etree.SubElement(ppr,q('ind')); i.set(q('left'),str(left))
        if hanging: i.set(q('hanging'),str(hanging))
    if jc: etree.SubElement(ppr,q('jc')).set(q('val'),jc)
    for txt,ital in (runs if runs else [(text,False)]):
        r=etree.SubElement(p,q('r'))
        if ital:
            rp=etree.SubElement(r,q('rPr')); etree.SubElement(rp,q('i'))
        t=etree.SubElement(r,q('t')); t.text=txt; t.set('{%s}space'%XML,'preserve')
    return p
# ---- bibliography
if with_bib:
    lastp=[c for c in body if c.tag==q('p')][-1]
    anchor=lastp
    def add(p):
        global anchor
        anchor.addnext(p); anchor=p
    add(mkp('Heading1','Selected Bibliography'))
    add(mkp(text='This bibliography records the works consulted in preparing this book, including its Bible translations and reference tools and a selection from the wider field of biblical studies. Listing a work does not claim dependence on it, agreement with it, doctrinal alignment with it or direct citation of it. The list shows the reader the ground over which the book was worked and where to read further.',jc='both',after=110))
    def h2(t): add(mkp('Heading2',t))
    def e(*runs): add(mkp(runs=list(runs),left=360,hanging=360,after=80,jc='left'))
    N=lambda s:(s,False); I=lambda s:(s,True)
    h2('Bible Translation')
    e(I('The Holy Bible, New Living Translation'),N('. Carol Stream, IL: Tyndale House Publishers, 1996, 2004, 2015. All Scripture quotations in this book are from this translation unless otherwise indicated.'))
    h2('Biblical Reference Works')
    e(N('Aharoni, Yohanan, and Michael Avi-Yonah. '),I('The Macmillan Bible Atlas'),N('. Rev. ed. New York: Macmillan, 1977.'))
    e(N('Brown, Francis, S. R. Driver, and Charles A. Briggs. '),I('The Brown-Driver-Briggs Hebrew and English Lexicon'),N('. Peabody, MA: Hendrickson Publishers. First published 1906.'))
    e(N('Smith, Jerome H., ed. '),I('The New Treasury of Scripture Knowledge'),N('. Nashville: Thomas Nelson, 1992.'))
    e(N('Strong, James. '),I('The Exhaustive Concordance of the Bible'),N('. New York: Hunt & Eaton; Cincinnati: Cranston & Curts, 1890.'))
    e(N('Thayer, Joseph Henry. '),I('A Greek-English Lexicon of the New Testament'),N('. New York: American Book Company, 1889.'))
    e(N('Vine, W. E. '),I('Vine’s Expository Dictionary of New Testament Words'),N('. London: Oliphants, 1940.'))
    h2('Historical and Theological Background: Dispensational History and Pauline Studies')
    e(N('Baker, Charles F. '),I('A Dispensational Theology'),N('. Grand Rapids: Grace Publications, 1971.'))
    e(N('Bullinger, E. W. '),I('The Companion Bible'),N('. London: Oxford University Press, 1922.'))
    e(N('Chafer, Lewis Sperry. '),I('Systematic Theology'),N('. 8 vols. Dallas: Dallas Seminary Press, 1947–1948.'))
    e(N('Ryrie, Charles C. '),I('Dispensationalism'),N('. Chicago: Moody Press, 1965. Rev. ed., 1995.'))
    e(N('Scofield, C. I. '),I('The Scofield Reference Bible'),N('. New York: Oxford University Press, 1909.'))
    e(N('Stam, Cornelius R. '),I('Things That Differ: The Fundamentals of Dispensationalism'),N('. Chicago: Berean Bible Society, 1951.'))
    e(N('Welch, Charles H. '),I('Dispensational Truth: Or, The Place of Israel and the Church in the Purpose of the Ages'),N('. London: The Berean Publishing Trust, 1959.'))
    h2('Acts, the Early Church, and Jewish Background')
    e(N('Bruce, F. F. '),I('The Book of the Acts'),N('. Grand Rapids: Eerdmans, 1954.'))
    e(N('Josephus, Flavius. '),I('The Works of Josephus'),N('. Translated by William Whiston. Peabody, MA: Hendrickson Publishers, 1987. Whiston’s translation first published 1737.'))
    e(N('Marshall, I. Howard. '),I('Acts'),N('. Tyndale New Testament Commentaries. Downers Grove, IL: InterVarsity Press, 1980.'))
    e(N('Polhill, John B. '),I('Acts'),N('. New American Commentary. Nashville: Broadman & Holman, 1992.'))
    h2('Old Testament Covenants and Prophetic Structure')
    e(N('Beale, G. K. '),I('A New Testament Biblical Theology'),N('. Grand Rapids: Baker Academic, 2011.'))
    e(N('Hamilton, Victor P. '),I('Handbook on the Pentateuch'),N('. 2nd ed. Grand Rapids: Baker Academic, 2005.'))
    e(N('Kaiser, Walter C., Jr. '),I('The Messiah in the Old Testament'),N('. Grand Rapids: Zondervan, 1995.'))
    e(N('Walton, John H. '),I('Ancient Near Eastern Thought and the Old Testament'),N('. Grand Rapids: Baker Academic, 2006.'))
    h2('The New Testament’s Use of the Old Testament')
    e(N('Beale, G. K., and D. A. Carson, eds. '),I('Commentary on the New Testament Use of the Old Testament'),N('. Grand Rapids: Baker Academic, 2007.'))
    e(N('Hays, Richard B. '),I('Echoes of Scripture in the Gospels'),N('. Waco, TX: Baylor University Press, 2016.'))
    e(N('Hays, Richard B. '),I('Echoes of Scripture in the Letters of Paul'),N('. New Haven: Yale University Press, 1989.'))
    h2('General Biblical Studies')
    e(N('Carson, D. A. '),I('New Testament Commentary Survey'),N('. 6th ed. Grand Rapids: Baker Academic, 2007.')); anchor.find(q('pPr')).insert(0,etree.Element(q('keepNext')))
    e(N('Fee, Gordon D., and Douglas Stuart. '),I('How to Read the Bible for All Its Worth'),N('. 4th ed. Grand Rapids: Zondervan, 2014. First published 1981.')); anchor.find(q('pPr')).insert(0,etree.Element(q('keepNext')))
    e(N('Longman, Tremper, III, and Raymond B. Dillard. '),I('An Introduction to the Old Testament'),N('. 2nd ed. Grand Rapids: Zondervan, 2006.'))

# ---- layout tweaks to reproduce the proofed page breaks
PB=['Romans 10:9–13 Is Read in Israel’s Setting','Catalog: Every Baptism Reference Cited in This Book']
hits=0
for p in body.iter(q('p')):
    if pstyle(p)=='Heading2' and ptext(p).strip() in PB:
        ppr=p.find(q('pPr')); ps=ppr.find(q('pStyle'))
        pb=etree.Element(q('pageBreakBefore')); ps.addnext(pb); hits+=1
print('pagebreak tweaks',hits)
# ---- TOC rebuild
heads=[p for p in body.iter(q('p')) if pstyle(p)=='Heading1']
titles=[ptext(p) for p in heads]
bid=9000
for i,p in enumerate(heads):
    name='_Toc9100%03d'%i
    bs=etree.Element(q('bookmarkStart')); bs.set(q('id'),str(bid+i)); bs.set(q('name'),name)
    be=etree.Element(q('bookmarkEnd')); be.set(q('id'),str(bid+i))
    ppr=p.find(q('pPr')); (ppr.addnext(bs) if ppr is not None else p.insert(0,bs)); p.append(be)
sdt=body.find(q('sdt')); sc=sdt.find(q('sdtContent'))
for c in list(sc): sc.remove(c)
TXTW=6696
for i,t in enumerate(titles):
    n=nums.get(t,'000')
    p=etree.Element(q('p')); ppr=etree.SubElement(p,q('pPr')); etree.SubElement(ppr,q('pStyle')).set(q('val'),'TOC1')
    tb=etree.SubElement(etree.SubElement(ppr,q('tabs')),q('tab')); tb.set(q('val'),'right'); tb.set(q('leader'),'dot'); tb.set(q('pos'),str(TXTW))
    def fld(typ):
        r=etree.Element(q('r')); f=etree.SubElement(r,q('fldChar')); f.set(q('fldCharType'),typ); return r
    if i==0:
        p.append(fld('begin'))
        r=etree.SubElement(p,q('r')); it=etree.SubElement(r,q('instrText')); it.text='TOC \\h \\o "1-1"'; it.set('{%s}space'%XML,'preserve')
        p.append(fld('separate'))
    h=etree.SubElement(p,q('hyperlink')); h.set(q('anchor'),'_Toc9100%03d'%i); h.set(q('history'),'1')
    r=etree.SubElement(h,q('r')); x=etree.SubElement(r,q('t')); x.text=t; x.set('{%s}space'%XML,'preserve')
    r=etree.SubElement(h,q('r')); etree.SubElement(r,q('tab'))
    r=etree.SubElement(h,q('r')); x=etree.SubElement(r,q('t')); x.text=str(n)
    if i==len(titles)-1: p.append(fld('end'))
    sc.append(p)
out=zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED)
for it in z.infolist():
    data=z.read(it.filename)
    if it.filename=='word/document.xml': data=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
    out.writestr(it,data)
out.close()
json.dump(titles,open('build/titles.json','w'))
print(len(titles),'headings')
