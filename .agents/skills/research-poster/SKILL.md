---
name: research-poster
description: Turn published computer-science papers into source-verified, aesthetically rigorous conference research posters with editable PPTX, print PDF, SVG/PNG previews, metadata, quality checks, topic classification, and automatic GitHub Pages gallery publishing. Use for paper-to-poster creation, revision, evaluation, categorization or publication.
license: MIT
compatibility: Python 3.10+, optional python-pptx, qrcode, LibreOffice, GitHub for publishing
metadata:
  author: 1998x-stack
  version: "1.0.0"
---
# Research Poster — paper → evidence → visual argument → reproducible publication

## Trigger
Activate when asked to create/convert/review a computer-science research poster, improve an existing poster, register a new paper, or publish/update the gallery. Do not activate for an ordinary slide deck or document summary with no poster intent.

## Completion contract
A completed paper has: correct source/venue/year and version; evidence ledger; credible distilled narrative; readable and honest visualizations; accessible poster in PDF and SVG/PNG; editable PPTX where tooling permits; \`poster.json\`; stable folder and links; passing validation; a visually checked gallery entry. Clearly label outputs that were not generated or Pages deployments that were not verified.

## Workflow (do not skip verification)
1. **Read & identify**: Obtain the official proceedings/PDF, author/title/year/DOI or URL, version date, figures and result tables. Avoid relying on secondary summaries for numbers. Read [research-methodology.md](references/research-methodology.md).
2. **Build a claim ledger**: For each claim record source URL, exact page/section/table, quote or paraphrase, experimental setting, baseline and caveat. Separate empirically supported results from illustrative cartoons. Resolve contradictions across paper versions, or disclose both.
3. **Choose storyline**: One sentence for the actual finding; 3 audience questions: *problem? mechanism? evidence?* Prefer one dominant architecture/figure + 2–3 results to nine equally weighted text boxes. Choose traditional, hybrid or headline-first layout based on density; consult [visual-design.md](references/visual-design.md).
4. **Design system**: Set size before authoring (default 48×36 in landscape); 0.8–1.2 in margins, 3-column hierarchy if useful, clear typography from 3–6 feet, accessible contrast; choose a visual grammar for method, datasets, results and limits. Avoid copying copyrighted poster artwork.
5. **Redraw technically**: Reconstruct diagrams as editable vector shapes, preserve the model's causal/data-flow edges, label assumptions, axes, units, mask direction, comparison conditions. See [scientific-figures.md](references/scientific-figures.md).
6. **Write with evidence**: Use title, authors, contribution, motivation, method, results and limits with short captions. Give full reference and QR to official paper. Do not inflate BLEU/mAP/accuracy claims or use results from another version without explicit disclosure.
7. **Generate artifacts**: Save source (\`.py\`, \`.svg\` or an equivalent editable representation), editable \`poster.pptx\`, print \`poster.pdf\`, \`preview.png\` and/or \`poster.svg\`. Keep all outputs in one paper folder. Use \`scripts/render_posters.py\` when supplied render sources exist. See [export-and-qa.md](references/export-and-qa.md).
8. **Register & classify**: Read \`catalog/taxonomy.json\`. Use stable path \`posters/<field>/<subfield>/<paper-slug>/\`, add \`poster.json\` per [metadata-and-taxonomy.md](references/metadata-and-taxonomy.md) and the template in \`assets/\`. Never promote a placeholder to published.
9. **Validate**: Run \`python scripts/validate_catalog.py\` and \`python scripts/build_site.py --output _site\`. Inspect actual poster at full print resolution and gallery on desktop/mobile. Fix text overflow, illegible labels, broken links and inconsistent figures. See [export-and-qa.md](references/export-and-qa.md).
10. **Publish**: Submit a reviewable change, confirm checks, deploy via GitHub Pages and verify the public URL *before* reporting success. See [publishing.md](references/publishing.md).

## Hard rules
- Scientific fidelity > aesthetics > coverage. A beautiful incorrect poster is a failure.
- Never fabricate diagrams, experiments, affiliations, venue acceptance, numbers or citations.
- Always distinguish **original research claim** from **poster author's visual interpretation**.
- Model comparison numbers must match their experiment protocol, datasets, version and single/ensemble designation.
- No unexplained cropped axes, fake uncertainty, chart junk, unreadable math or vanity logos.
- Never publish confidential inputs, private manuscripts or copyrighted source figures without rights.
- Do not mutate another paper's folder unless tasked. Keep sources, not only rendered artifacts.
- A missing actual PDF/PPTX is a **partial delivery**, not a completed poster; name the missing output.

## References on demand
- [research-methodology.md](references/research-methodology.md) — evidence/version extraction.
- [visual-design.md](references/visual-design.md) — poster layout and typography.
- [scientific-figures.md](references/scientific-figures.md) — attention/graphs/plots.
- [export-and-qa.md](references/export-and-qa.md) — preflight, PDF, PPTX.
- [metadata-and-taxonomy.md](references/metadata-and-taxonomy.md) — corpus and JSON contract.
- [publishing.md](references/publishing.md) — Pages workflow and security.
- [references-and-standards.md](references/references-and-standards.md) — external authoritative guides.
- [transformer-case-study.md](references/transformer-case-study.md) — exact NeurIPS 2017 showcase.
