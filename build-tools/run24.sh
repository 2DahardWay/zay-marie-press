set -e; export PYTHONPATH=.
W=/tmp/claude-0/-home-claude/c0ed2e22-30fa-5e68-8953-7079a3cff252/scratchpad/w
export FONTCONFIG_FILE=$W/fc.conf
cd $W/b24
cp ../clean.py ../base.py .
python3 ../build.py cfg24.json >/dev/null
python3 ../post.py out0.docx; python3 ../post2.py out0.docx; python3 ../post3.py out0.docx; python3 ../fixnum2.py out0.docx >/dev/null
cp out0.docx conf.docx; soffice --headless --convert-to pdf conf.docx >/dev/null 2>&1
N=$(pdfinfo conf.pdf | grep Pages | awk '{print $2}')
python3 ../toc2.py $N >/dev/null; soffice --headless --convert-to pdf conf.docx >/dev/null 2>&1
pdfinfo conf.pdf | egrep "Pages|Page size"
