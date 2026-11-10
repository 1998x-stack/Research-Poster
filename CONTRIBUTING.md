# Contributing a research poster

We welcome reproducible poster designs for published computer-science papers.

1. Verify the paper, venue/year, authors and original URL.
2. Check \`catalog/taxonomy.json\` for the right field/subfield.
3. Use lower-kebab-case names; create \`posters/<field>/<subfield>/<slug>/\`.
4. Copy \`.agents/skills/research-poster/assets/poster.json.template\` and fill the factual fields. Include at least one main contribution, a complete citation and limitations.
5. Draw or permission-check figures. Generate \`poster.svg\` and, where possible, \`poster.pptx\`, \`poster.pdf\`, \`preview.png\`.
6. Record exact experimental protocol, *not* cherry-picked baseline numbers.
7. Run \`python scripts/validate_catalog.py\`, \`python scripts/build_site.py --output _site\`, then verify responsive layouts and print export.
8. Open a PR with a rendered thumbnail, source references, a claim/evidence checklist and known limitations.

**Never** commit copyrighted paper PDFs by default, sensitive drafts, author-private data or API secrets. Preserve old artifacts on revisions by version or documented changelog.