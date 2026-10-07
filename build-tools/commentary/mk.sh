#!/bin/bash
# usage: ./mk.sh   -> out/volume.docx and out/volume.pdf with the TOC page numbers settled in two passes
set -e
cd "$(dirname "$0")"
mkdir -p out
LO="soffice -env:UserInstallation=file:///tmp/lo_profile_comm --headless --convert-to pdf --outdir out"
rm -f toc.json
python3 build.py out/volume.docx
$LO out/volume.docx >/dev/null 2>&1
python3 tocmap.py out/volume.pdf
python3 build.py out/volume.docx
$LO out/volume.docx >/dev/null 2>&1
python3 tocmap.py out/volume.pdf --check
