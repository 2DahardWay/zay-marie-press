# Interior typeface: Roboto

Master Standard v1.27 §8 requires every Digital Study and Doctrinal Packet interior, headings included, to be set in Roboto, four true faces, no fallback font. Roboto is licensed under the Apache License 2.0 (`LICENSE-Apache-2.0.txt`).

## Files

`Roboto-Regular.ttf`, `Roboto-Bold.ttf`, `Roboto-Italic.ttf`, `Roboto-BoldItalic.ttf` are static instances cut from the publisher-supplied Roboto variable fonts (`wght` 400 / 700, `wdth` 100) with fontTools `instantiateVariableFont`, then renamed so the family is "Roboto" and the styles are Regular, Bold, Italic and Bold Italic.

## Build recipe (DOCX to PDF)

1. Install the four files (`~/.fonts`, then `fc-cache -f`).
2. In the DOCX package, set every `w:rFonts` to `ascii`, `hAnsi`, `eastAsia` and `cs` = "Roboto" in `styles.xml`, `document.xml` and the footer, and set the theme major and minor `a:latin` typeface to "Roboto" so headings do not fall back to Calibri or Cambria.
3. Replace the Symbol bullet character (U+F0B7) in `numbering.xml` with "•" set in Roboto.
4. Body text is 9 pt: set `w:sz` 18 in the document defaults, the Normal style (if it carries its own size) and the List Bullet style. Studies 1 and 2 were rebuilt at 9 pt and reflow cleanly (14 pages each including the cover). Use the same size for every study.
4a. Roboto has no glyph for "→" or "□". Replace "→" with "›" and "□" with "[ ]" in the document text so no fallback font is embedded.
5. Convert with LibreOffice, recompute the Table of Contents page numbers from the rendered PDF, rebuild and re-check.
6. Run `pdffonts` on the result. Only Roboto-Regular, Roboto-Bold, Roboto-Italic and Roboto-BoldItalic may be embedded.

7. Keep the approved production cover as physical page 1: take it from the existing PDF (remove its unused /Font resources), and append pages 2 onward from the rebuilt PDF with pikepdf. The DOCX cover image can differ from the approved cover.

## Table of Contents spacing (Master Standard v1.29)

From Study 6 forward, remove any hand-set `w:spacing` from the Table of Contents entry paragraphs so they take the Normal style (6 pt after, 1.08 line spacing). Studies 1-5 and 9 keep their earlier TOC spacing unless reopened.

## Heading 1 spacing (Master Standard v1.30)

From Study 6 forward, set the Heading 1 style to 12 pt space-before and 8 pt space-after (`w:before="240" w:after="160"` in `styles.xml`); Heading 2 stays 10 pt / 5 pt. Strip any per-paragraph spacing overrides so every heading takes the style value. Studies 1-5 and 9 were built at 14 pt before and are not reopened for this.
