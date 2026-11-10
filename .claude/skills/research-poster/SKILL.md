---
name: research-poster
description: Create and publish conference-quality, evidence-checked research posters for computer-science papers, including printable PDF, editable source, metadata and a searchable gallery.
license: MIT
---
# Research Poster

Claude Code skill entrypoint.

The authoritative workflow and references are in the repository root:
- `.agents/skills/research-poster/SKILL.md`
- `.agents/skills/research-poster/references/`
- `.agents/skills/research-poster/assets/`

**Read the canonical SKILL.md fully before acting.** Apply its claim-evidence verification, scientific diagram and QA gates. Add papers under `posters/<field>/<subfield>/<slug>/`, run `python scripts/validate_catalog.py` and `python scripts/build_site.py --output _site`, then verify the result. If working outside the repository, clone it first rather than assuming relative paths.