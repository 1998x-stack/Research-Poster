# Portable poster templates

All files here are **reusable inputs to the research-poster skill**, not examples of verified scientific results.

| Template | Use |
| --- | --- |
| [`claim-ledger.md`](claim-ledger.md) | Record source/version/page/protocol for each scientific claim |
| [`poster-storyboard.md`](poster-storyboard.md) | Plan audience, one defensible argument, visual grammar and limitations |
| [`review-checklist.md`](review-checklist.md) | Document source, quality, accessibility, export and deployment checks |
| [`layout-hybrid.svg`](layout-hybrid.svg) | Mechanism-led narrative with large central diagram |
| [`layout-results-led.svg`](layout-results-led.svg) | Measurements, comparisons and trade-offs as the visual center |
| [`layout-proof-led.svg`](layout-proof-led.svg) | Formal premise, central theorem and proof flow |

The SVGs are **wireframes with placeholder text** and editable vector geometry; they must never be published with placeholders or treated as a source for diagrams or empirical results. Choose a layout based on [paper archetypes](../../references/paper-archetypes.md) and adapt sizes to the venue. They use a 4:3 landscape canvas for preview convenience, not a promise of print-scale font sizes.

The repository's `scripts/new_poster.py` initializes `evidence.md` and `brief.md` using the Markdown templates, replacing `{{TITLE}}` and `{{SOURCE_URL}}`. In an external project, the templates can be copied manually and edited with any text editor.
