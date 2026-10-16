set -e
cd "$(dirname "$0")"; mkdir -p out
LO="soffice -env:UserInstallation=file:///tmp/lo_profile_s87 --headless --convert-to pdf --outdir out"
rm -f toc.json
python3 build.py out/study.docx && $LO out/study.docx >/dev/null 2>&1
python3 tocmap.py out/study.pdf
python3 build.py out/study.docx && $LO out/study.docx >/dev/null 2>&1
python3 tocmap.py out/study.pdf --check
