# Repository agent instructions

For any research-poster generation, revision, evaluation, publication or catalog maintenance, **read** `.agents/skills/research-poster/SKILL.md` and the relevant on-demand `references/` files before editing.

1. Never invent papers, author identities, experiment numbers, baselines, links or source references.
2. Prefer official proceedings; record exact version/section/table and distinguish arXiv revisions.
3. Never overwrite an existing poster without explicit request; retain source and record version.
4. Use `catalog/taxonomy.json`; put new papers in `posters/<field>/<subfield>/<slug>/`.
5. Check image licensing and secrets before public publishing.
6. Run `python scripts/validate_catalog.py` and `python scripts/build_site.py --output _site` before proposing changes.
7. Do not report GitHub Pages as live unless the actual deployed URL is verified.
8. Keep site functional without npm, external CDN or client-side keys.
