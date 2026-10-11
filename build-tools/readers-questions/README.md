Generator for the Readers Question Series question pages (Master Standard v1.105 Rule 31).
gen_question_pages.py reads each volume's source HTML (the same HTML the PDF is printed from; paths at the top of the file point to the working copies) and the volume pages, writes the 50 question pages and assets/reader-questions-index.json.
wire_pages_and_search.py was the one-time wiring (volume-page row links, Questions-page search, sitemap); it is not re-run.
Working tools only; the site does not use them. Not a rule.
