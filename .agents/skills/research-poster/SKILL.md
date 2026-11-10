---
name: research-poster
description: Transform published computer-science research papers from any subfield into source-verified, readable conference posters with reusable visual templates, an evidence ledger, editable assets, print exports, metadata and quality preflight. Use for drafting, reviewing, revising or publishing research posters and research-paper galleries.
license: MIT
compatibility: Python 3.10+; standalone preflight uses stdlib; optional PowerPoint rendering uses Python packages, LibreOffice and Poppler
metadata:
  author: 1998x-stack
  version: "1.1.0"
---

# Research Poster — evidence-first, domain-aware, reproducible

## When to use

Activate for turning a scholarly paper into a conference research poster, reviewing the scientific or visual quality of a poster, adding a paper to a gallery, or preparing editable and print-quality exports. The scope is **all computer-science disciplines**, not just AI or Transformer papers. Do not use for slide decks without poster intent.

## Inputs and outputs

**Input:** DOI, official paper URL, public PDF or an authorized local manuscript; optional poster dimensions, audience, language, venue guidelines, visual design constraints and category.

**Output contract:** `evidence.md` (version-specific claims), `brief.md` (audience, argument, diagram and layout), source artwork/program, `poster.json` (when adding to gallery), a viewable `poster.svg` or preview, `poster.pdf`, editable `poster.pptx` and `preview.png` when supported. Report missing assets explicitly; do not present partially generated files as a complete delivery.

## End-to-end procedure

1. **Source and permissions.** Confirm the paper's identity, authors, venue/year, stable URL, version and right to use any third-party figures. Prioritize official archival sources. Read [research-methodology.md](references/research-methodology.md).
2. **Evidence ledger.** Record every headline claim, equation, visual relationship and numeric result with exact section/page/table, model variant, experimental protocol, baseline, units and caveat. Use [`assets/templates/claim-ledger.md`](assets/templates/claim-ledger.md). Contradictory paper versions must be disclosed, not blended.
3. **Audience and archetype.** Select the actual research question and audience. Read [paper-archetypes.md](references/paper-archetypes.md). Choose a mechanism-led, results-led, proof-led, study-led or hybrid visual story; don't make all papers look like a neural architecture.
4. **Storyboarding.** Complete [`poster-storyboard.md`](assets/templates/poster-storyboard.md). Express the central defensible takeaway in one short sentence; decide which evidence supports it and which limitations must remain visible.
5. **Lay out.** Match venue size, orientation and readability constraints before drawing. Use [visual-design.md](references/visual-design.md) and optional editable [layout wireframes](assets/templates/) as **geometry only**—never copy a figure or claim from a sample.
6. **Redraw scientific content.** Recreate conceptual diagrams using editable vectors, explicit semantics, axes/units and source citations. The figure must preserve the method's logic. Use [scientific-figures.md](references/scientific-figures.md); for Transformer-specific fidelity only, see [transformer-case-study.md](references/transformer-case-study.md).
7. **Export reproducibly.** Keep source code/SVG/PPTX and print PDF/preview together. Prefer live editable text and vector shapes. Read [dependencies-and-tooling.md](references/dependencies-and-tooling.md) and [export-and-qa.md](references/export-and-qa.md). The repository's `scripts/render_posters.py` handles only known `make_poster.py` sources; other source formats need their own renderer.
8. **Preflight artifacts.** Use the portable, stdlib [`scripts/preflight.py`](scripts/preflight.py) on the paper directory, e.g. `python .agents/skills/research-poster/scripts/preflight.py posters/<field>/<subfield>/<slug> --strict`. Strict PDF page-count verification requires `pdfinfo`. The script checks structural basics, not scientific truth or visual readability. Apply the [human review checklist](assets/templates/review-checklist.md).
9. **Register safely.** In this repository, select a real category/subfield from `catalog/taxonomy.json` and create `posters/<field>/<subfield>/<slug>/poster.json` from the metadata contract. Keep drafts unlisted; never overwrite unrelated papers. Read [metadata-and-taxonomy.md](references/metadata-and-taxonomy.md).
10. **Validate and publish.** Run `python scripts/validate_catalog.py`, `python -m unittest discover -s tests -v` and `python scripts/build_site.py --output _site`. Check web cards and paper-detail pages at mobile/desktop widths and PDF print scale. Use [publishing.md](references/publishing.md) for Pages; do not claim it is deployed until verified.

## Non-negotiable gates

- **Scientific accuracy > visual polish > quantity.** Never fabricate an experiment, number, figure, venue, attribution or source.
- Comparison plots require the actual dataset, split, model configuration, metric direction, baseline, paper version and any uncertainty supplied by authors.
- Theory proofs require precise assumptions; security diagrams require an explicit threat model; human-subject studies require study limits. A universal architecture diagram is wrong for these cases.
- Posters must show limitations, not just successful experiments. Cite original research and distinguish schematic interpretations.
- Never embed private files, unlicensed graphics, secret tokens or unpublished sensitive information in an open gallery.
- Make a reproducible, non-destructive change; assess copyright and publication rights before copying visuals.
- A working command is not evidence that text is readable at print distance or that a Page is public. Report evidence of actual verification.

## Resource map and dependency policy

| Resource | Purpose | Load / run when |
| --- | --- | --- |
| [research-methodology.md](references/research-methodology.md) | Primary sources and numerical fidelity | Every new paper |
| [paper-archetypes.md](references/paper-archetypes.md) | Domain-sensitive poster strategy | Every new paper |
| [visual-design.md](references/visual-design.md) | Layout, type and contrast | Storyboarding |
| [scientific-figures.md](references/scientific-figures.md) | Accurate technical diagrams | Drawing |
| [export-and-qa.md](references/export-and-qa.md) | Print/edit exports and final inspection | Export |
| [dependencies-and-tooling.md](references/dependencies-and-tooling.md) | Install / fallback behavior | Before rendering |
| [metadata-and-taxonomy.md](references/metadata-and-taxonomy.md) | Gallery data contract | Registering paper |
| [publishing.md](references/publishing.md) | Release, Pages and safety | Publishing |
| [references-and-standards.md](references/references-and-standards.md) | Original standards and references | When choosing standards |
| [transformer-case-study.md](references/transformer-case-study.md) | **One illustrative paper**, not the default | Transformer paper only |

**Portable skill files:** `requirements.txt` holds optional render dependencies, `scripts/preflight.py` checks artifacts with the standard library, and `assets/templates/` supplies evidence/brief/review layouts. **Repository-owned tools** stay in root `scripts/`. Copy the full skill directory to reuse it, and do not assume root scripts exist in another repo.
