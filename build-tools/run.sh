set -e
export FONTCONFIG_FILE=/tmp/s55/fc.conf
n=$1; cd /tmp/s5960/w/b$n
cp ../ed$n.py ../clean.py .
python3 build.py cfg$n.json >/dev/null
python3 ../post.py out0.docx; python3 ../post2.py out0.docx; python3 ../post3.py out0.docx; python3 ../fixnum2.py out0.docx >/dev/null
cp out0.docx conf.docx; soffice --headless --convert-to pdf conf.docx >/dev/null 2>&1
N=$(pdfinfo conf.pdf | grep Pages | awk '{print $2}')
python3 ../toc2.py $N >/dev/null; soffice --headless --convert-to pdf conf.docx >/dev/null 2>&1
pdfinfo conf.pdf | grep Pages
