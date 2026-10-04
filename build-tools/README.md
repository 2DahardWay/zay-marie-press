# Study build tools

Scripts used to rebuild each Digital Study's interior (PDF and DOCX) to the Master Standard. They are working tools, not part of the website, and nothing on the site reads them.

Layout
- `step1.py N`: reads the publisher's DOCX and writes `bNN/elsNN.json` (the study as a list of elements); also prints the Step 1 report.
- `base.py`, `build.py`, `build2.py` (adds two-level bullets), `clean.py`, `edcommon.py`: template, builder and helper functions. Standing doctrine sentences (overlap, Rule 17, Rule 18, Rule 11, Romans 11) live in `base.py`.
- `post.py`, `post2.py`, `post3.py`, `fixnum2.py`, `keepimp.py`, `toc2.py`: spacing, numbering, imprint keep-together and table-of-contents passes. `keepimp.py` reads env `KEEPFROM` (default "Final Synthesis").
- `runNN.sh`: the build recipe for one study. `conv*.py`, `ed50.py`, `ed51.py`, `ed62.py` and the `run*post.py` files are one-off conversions.
- `studies/bNN/`: per-study `edNN.py` (the exact wording edits applied) and `cfgNN.json` (cover, title, image map). These record every wording change made in the retrofit.
- `fc.conf`: font config that points at `fonts/` (Roboto only).

To use: copy this folder to a scratch directory, create `bNN/` from `studies/bNN/`, run `step1.py N` on the DOCX, then `runNN.sh` (set `W` and the `fc.conf` cache path at the top of `fc.conf` and the scripts to the scratch directory; `export FONTCONFIG_FILE=$W/fc.conf`). Covers and source DOCX files are not stored here.
