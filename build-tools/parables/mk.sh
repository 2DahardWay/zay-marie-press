set -e
# usage: bash mk.sh <study-dir>   (e.g. wheat)
cd "$(dirname "$0")"; D="$1"; mkdir -p $D/out
LO="soffice -env:UserInstallation=file:///tmp/lo_profile_par_$D --headless --convert-to pdf --outdir $D/out"
rm -f $D/toc.json
python3 build.py $D/out/study.docx $D && $LO $D/out/study.docx >/dev/null 2>&1
python3 tocmap.py $D/out/study.pdf $D
python3 build.py $D/out/study.docx $D && $LO $D/out/study.docx >/dev/null 2>&1
python3 tocmap.py $D/out/study.pdf $D --check
pdfinfo $D/out/study.pdf | grep Pages; pdffonts $D/out/study.pdf | awk 'NR>2{print $1}' | sort | uniq -c
