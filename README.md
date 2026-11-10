# Research Poster · Paper to Poster, by Design

> **A reproducible computer-science research-poster studio, multi-agent skill, and browsable paper gallery.**

[![Pages](https://github.com/1998x-stack/Research-Poster/actions/workflows/pages.yml/badge.svg)](https://github.com/1998x-stack/Research-Poster/actions/workflows/pages.yml)
[![CI](https://github.com/1998x-stack/Research-Poster/actions/workflows/validate.yml/badge.svg)](https://github.com/1998x-stack/Research-Poster/actions/workflows/validate.yml)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-standard-0d9488)](https://agentskills.io/specification)

**[Explore the poster gallery](https://1998x-stack.github.io/Research-Poster/)** · [Skill](.agents/skills/research-poster/SKILL.md) · [Research references](.agents/skills/research-poster/references/) · [Categories](catalog/taxonomy.json) · [Contribute](CONTRIBUTING.md)

## Why this exists

Great research posters are not condensed papers. They are **evidence-backed visual arguments**: a readable title, one memorable finding, a carefully redrawn method, a fair empirical comparison, a limitations box, and a traceable source. This repository converts this workflow into a reusable Agent Skill and a growing public collection of computer-science research posters.

**Pipeline:** Verify paper → Extract claims & numbers → Select visual narrative → Redraw architecture and evidence → Produce editable source → Export PDF/PPTX/preview → QA → Add metadata → Build searchable Pages gallery.

## Featured poster

**[Attention Is All You Need](posters/artificial-intelligence/natural-language-processing/attention-is-all-you-need/)** · Vaswani et al., NeurIPS 2017

- Main contribution: the Transformer replaces recurrence with attention in a sequence-to-sequence model.
- Method: encoder–decoder stacks, self-/cross-attention, masking, and positional encoding.
- Results: **28.4 BLEU** (WMT14 English→German) and **41.0 BLEU** (English→French), according to the *2017 proceedings version*, Table 2. A later arXiv revision reports 41.8; never silently mix versions.
- The **original V2 poster source** is reconstructed as a reproducible, editable PowerPoint + printable PDF + web preview by the repository's generation workflow. The committed SVG serves as an immediate, no-build preview.

## One-prompt workflow

Paste this into a compatible coding agent after cloning this repository:

\`\`\`text
Use the research-poster skill in .agents/skills/research-poster/SKILL.md.
For the paper <PAPER_URL_OR_PDF>, verify the source and official results;
select the correct category in catalog/taxonomy.json; prepare a
claim/evidence ledger; design a compelling conference-quality poster;
generate editable PPTX, print PDF and web thumbnail; add poster.json;
run python scripts/validate_catalog.py and python scripts/build_site.py;
and propose a reviewable commit/PR without overwriting previous posters.
\`\`\`

**Skills**: Codex discovers \`.agents/skills/research-poster/SKILL.md\`; OpenCode also sees \`.opencode/skills/\`; Claude Code sees \`.claude/skills/\`; Pi sees \`.pi/skills/\`. A \`.codex/\` compatibility guide is included, but modern Codex project auto-discovery happens in \`.agents/skills\`.

## Repository map

\`\`\`text
.agents/skills/research-poster/
  SKILL.md                 # canonical end-to-end contract
  references/              # sourcing, design, visualization, QA, publishing
  assets/                  # reusable briefs and metadata templates
.codex/ .claude/ .opencode/ .pi/
  skills/research-poster/  # platform entrypoints
catalog/taxonomy.json      # machine-readable CS taxonomy
posters/<field>/<subfield>/<paper-slug>/
  poster.json              # required, validated metadata
  poster.svg               # versioned, universally viewable preview
  make_poster.py           # optional reproducible render source
  poster.pptx              # generated editable deliverable
  poster.pdf               # generated print deliverable
  preview.png              # generated raster thumbnail
scripts/
  build_site.py            # generates a searchable static gallery
  validate_catalog.py      # taxonomy, uniqueness, security & asset checks
  render_posters.py        # regenerates known source-backed posters
site/                      # CSS, JS, HTML templates and artwork
.github/workflows/         # CI validation and Pages publication
\`\`\`

## Adding a paper

1. Check official proceedings and version-specific tables; create an evidence ledger.
2. Choose a category/subcategory from \`catalog/taxonomy.json\`. If needed, add a category with an explanation.
3. Create \`posters/<field>/<subfield>/<slug>/poster.json\` and source artwork. Do not overwrite an existing poster version.
4. Produce SVG/web preview, PDF, and PPTX. Put source code and provenance in the paper folder.
5. Run \`python scripts/validate_catalog.py\` then \`python scripts/build_site.py --output _site\`. Inspect the PDF at print size and mobile/desktop cards.
6. Open a PR. The GitHub Actions Pages workflow rebuilds the catalog from \`poster.json\` files: **no hand-maintained card list**.

## Local preview

Requires Python 3.10+ (standard library for catalog/site; poster rendering adds \`python-pptx\`, \`qrcode[pil]\`, and LibreOffice).

\`\`\`bash
python scripts/validate_catalog.py
python scripts/build_site.py --output _site
python -m http.server 8000 --directory _site
# open http://localhost:8000
\`\`\`

To render the seed PowerPoint, PDF and PNG, install dependencies in \`requirements-render.txt\`, then run \`python scripts/render_posters.py\`. GitHub Actions automates those steps on publication.

## Deployment

The workflow in \`.github/workflows/pages.yml\` requests only the Pages deployment scopes needed for publishing. To activate the site, open **Settings → Pages → Build and deployment → Source: GitHub Actions**. The expected project-site URL is **https://1998x-stack.github.io/Research-Poster/**. A workflow existing in the repo does *not*, by itself, prove Pages is activated; check the deployment status in Actions/Settings.

## Values and safeguards

- **No invented claims:** figures, quotes and metrics must have source links, version and table/figure identifiers.
- **No deceptive plots:** disclose axis limits, baselines, data transformations and important limitations.
- **Editable and accessible:** save vector diagrams, text-accessible PDF, alt captions, contrast-tested figures.
- **Safe publishing:** never commit private PDFs, unpublished datasets, API keys or copyrighted figures without rights. Redraw with attribution.
- **Non-destructive:** each paper is independently versioned; existing posters are immutable without explicit review.

## Attribution

The demonstration summarizes *Attention Is All You Need* (Vaswani et al., NeurIPS 2017). Research claims and figures are credited to the original authors; poster layout and redraw are a separate educational reinterpretation. See the [provenance record](posters/artificial-intelligence/natural-language-processing/attention-is-all-you-need/poster.json).

License: repository code, templates and original layouts MIT; individual paper copyrights and citations remain with their respective owners.