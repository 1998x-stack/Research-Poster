# Research Poster — release review checklist

Complete this checklist for **each published paper**. Programmatic checks alone do not verify research truth or legibility.

## 1. Scientific fidelity

- [ ] Official paper identity, venue, author list and **specific version** confirmed.
- [ ] Every headline statement and number linked to a source page/table/figure in `evidence.md`.
- [ ] Comparisons have the same task, split, baseline/model variant, units and evaluation protocol.
- [ ] Schematics distinguish author interpretation from measured result or original figure.
- [ ] Assumptions, negative cases, failure modes, and limitations are clearly visible.
- [ ] External figures, quotes, datasets and fonts satisfy redistribution permissions.

## 2. Visual and editorial quality

- [ ] Layout matches the paper's research archetype and target audience.
- [ ] Central method/proof/system path is correct; no missing arrows or false causal links.
- [ ] Axes and scales are honest; uncertainties are only drawn when actually reported.
- [ ] Title and key takeaway readable at conference distance; body legible at print scale.
- [ ] No clipped text, overflow, low-contrast labels, tiny legends or misaligned elements.
- [ ] Captions, math symbols, acronyms and reference/QR URL visually checked.

## 3. Artifact and publication

- [ ] Editable source committed, plus `poster.svg` or preview for web use.
- [ ] PDF opens, is one page with correct dimensions, and text/vector content is readable.
- [ ] PPTX opens and is editable **if** PPTX is part of the agreed deliverables.
- [ ] PNG is not blank or corrupt; SVG has useful title/description.
- [ ] Run `python .agents/skills/research-poster/scripts/preflight.py <paper-dir> --strict`.
- [ ] Run `python scripts/validate_catalog.py --strict-assets` and unit tests.
- [ ] Build site and check gallery card, detail route and download links.
- [ ] Inspect mobile and desktop; keyboard focus and semantic alt text intact.
- [ ] Public Pages deployment only reported after actual verification.

## Review record

- Research reviewer / date:
- Design reviewer / date:
- Generator / source commit:
- Source version and known open risks:
- Status: **APPROVED / CHANGES REQUIRED / PARTIAL**
