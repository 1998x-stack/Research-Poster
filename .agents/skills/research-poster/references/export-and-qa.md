# Artifact generation, print quality and acceptance checks

## Required artifact checklist
- \`poster.json\` with source/version and factual claims.
- \`poster.svg\` semantic, navigable preview (or accessible raster preview).
- \`poster.pptx\` editable PowerPoint when supported.
- \`poster.pdf\` one-page print PDF, appropriate dimensions and embedded fonts.
- \`preview.png\` or WebP screenshot/thumbnail.
- Render source (Python, LaTeX, PPTX, etc.) for reproducibility.

## Recommended authoring
Use PowerPoint vector primitives or source SVG; avoid rasterizing figures to look editable. Convert PPTX with LibreOffice, render PDF with pdfium/Poppler/PyMuPDF. Typical local seed command:

\`\`\`bash
python -m pip install -r requirements-render.txt
python scripts/render_posters.py
python scripts/validate_catalog.py
python scripts/build_site.py --output _site
\`\`\`

## Programmatic QA
1. Open PDF: check exactly one page, expected aspect/size (48×36 in → 3456×2592 pt), extracted text and images not blank.
2. Render PNG at ~120–160 dpi for visual QA; high-res printing uses vector PDF, not a low-resolution PNG.
3. Inspect preview for text overflow, clipping, background bands, alignment, and chart labels.
4. Check every numeric label against the evidence ledger.
5. Check PPTX reopenable, at least one slide, fonts supported and objects structurally editable.
6. Validate SVG/XML, JSON metadata, alt text, DOI/URL, QR destination, and all gallery paths.
7. Test mobile (360px), tablet (768px), desktop (1440px), keyboard focus, reduced motion and print.

## Reject conditions
Missing major architectural edge, unsourced big metric, paper-version mismatch, illegible print body, citation absent, inaccessible or broken navigation, empty generated PDF, corrupted PPTX, or silently missing binaries. Mark the task partial with specific gaps; never claim “passed” based solely on process exit code.