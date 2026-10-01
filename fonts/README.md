# Interior typeface: Roboto

Master Standard v1.27 §8 requires every Digital Study and Doctrinal Packet interior, headings included, to be set in Roboto, four true faces, no fallback font. Roboto is licensed under the Apache License 2.0 (`LICENSE-Apache-2.0.txt`).

## Files

`Roboto-Regular.ttf`, `Roboto-Bold.ttf`, `Roboto-Italic.ttf`, `Roboto-BoldItalic.ttf` are static instances cut from the publisher-supplied Roboto variable fonts (`wght` 400 / 700, `wdth` 100) with fontTools `instantiateVariableFont`, then renamed so the family is "Roboto" and the styles are Regular, Bold, Italic and Bold Italic.

## Build recipe (DOCX to PDF)

1. Install the four files (`~/.fonts`, then `fc-cache -f`).
2. In the DOCX package, set every `w:rFonts` to `ascii`, `hAnsi`, `eastAsia` and `cs` = "Roboto" in `styles.xml`, `document.xml` and the footer, and set the theme major and minor `a:latin` typeface to "Roboto" so headings do not fall back to Calibri or Cambria.
3. Replace the Symbol bullet character (U+F0B7) in `numbering.xml` with "•" set in Roboto.
4. Body text is 9.5 pt (`w:sz` 19 in the document defaults and the List Bullet style) in the Study 2 pilot, which keeps the study at 15 pages. Adjust only if the page-count standard needs it.
5. Convert with LibreOffice, recompute the Table of Contents page numbers from the rendered PDF, rebuild and re-check.
6. Run `pdffonts` on the result. Only Roboto-Regular, Roboto-Bold, Roboto-Italic and Roboto-BoldItalic may be embedded.
