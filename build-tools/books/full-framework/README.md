# The Full Framework (Book 1), print interior files

Current, submit-ready files (2026-10-18, with the Selected Bibliography, Rule 36):

- `The_Full_Framework_Print_Interior_Editable_6x9_v11_with_Bibliography.docx`: editable source. Start every revision here.
- `Full_Framework_Print_Interior_6x9_240pp.pdf`: print interior built from that DOCX (6 x 9, Caladea embedded, 240 pages; page 240 is a blank pad so the count is even; bibliography is printed pages 231-233).
- `source/Print_Interior_Editable_6x9_v10_as_supplied.docx`: the DOCX exactly as the publisher supplied it (its Table of Contents was stale).
- `tools/make.py`: v10 -> v11 (appends the bibliography, rebuilds the Table of Contents from the Heading 1 paragraphs, two forced page breaks that reproduce the proofed layout). `tools/nums.py`: measures each Heading 1's printed page from a rendered PDF. `tools/toc_page_numbers.json`: the numbers used.
- `Selected_Bibliography_Insert_Full_Framework.*`: the earlier stand-alone insert, superseded by the files above.

Rebuild recipe: render with LibreOffice 24.2 (`soffice --headless --convert-to pdf`), never Word (Word paginates differently and uses real Cambria). Run `make.py` with `-` as the numbers file, render, run `nums.py`, run `make.py` again with the measured numbers, render, crop the page boxes to 432 x 648 pt (LibreOffice rounds the height to 649.16), append one blank page if the count is odd, and check the fonts with `pdffonts`.

Older versions: the 236-page `03_Print_Interior_6x9_236pp.pdf` the publisher once supplied is an OLDER text ("Great Commission" wording) and must not be used. The IngramSpark proof (243 pages) and the v10 DOCX carry the current text ("Kingdom Commission").
