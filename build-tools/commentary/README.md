# Commentary volume build toolkit

Working tools for the Prophetic Identity Commentary Series (and any Commentary Volume that follows the same layout). The site does not use them. Not a rule.

- `build.py` builds the DOCX with python-docx (page 9677×14515 twips, Roboto, series geometry). `content.py` holds the volume's metadata and loads the chapter modules `p0.py … pN.py`, `tail.py`, `appf.py`, `appg.py`.
- `mk.sh` runs the two-pass build (build, LibreOffice PDF, `tocmap.py` page numbers, rebuild, check). Needs LibreOffice, Roboto static fonts from `fonts/` installed, and the cover art saved as `cover_supplied.jpg` beside `build.py` (without it `mkcover.py` draws a typographic placeholder).
- `kjv_all.txt` is the merged KJV corpus; `kjv.py Book:ch:v1-v2` prints verses; `kjvcheck.py` tests every quoted string and table row against it; `kjvdiff.py` and `kjvmerge.py` compare and merge two fetched copies (not included: the A/B chapter folders).
- The files here are Volume 1 (The Bride Identity in Prophecy). For a new volume, replace the chapter modules and `META` in `content.py`.
