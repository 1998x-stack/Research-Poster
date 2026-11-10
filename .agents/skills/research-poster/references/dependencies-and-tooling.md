# Dependencies, portable scripts and reproducible outputs

This repository deliberately separates the **portable agent skill** from **repository-specific publication tooling**. Keep dependencies optional until a task requires actual rendering.

## Dependency tiers

| Tier | What runs | Installation |
| --- | --- | --- |
| Baseline | `new_poster.py`, `validate_catalog.py`, `build_site.py`, unit tests, skill `preflight.py` | Python 3.10+ **stdlib only** |
| Editable PowerPoint source | `make_poster.py` (when supplied) and QR artwork | `python -m pip install -r .agents/skills/research-poster/requirements.txt`; root `requirements-render.txt` forwards to this file |
| PDF + preview rendering | `scripts/render_posters.py` | System **LibreOffice** CLI and **Poppler** (`pdftoppm`, `pdfinfo`) in PATH |
| Visual audit | Inspect actual print PDF, preview, and website in a renderer/browser | Human/agent visual inspection; not a pip install |

The skill `requirements.txt` is the single source of truth for Python rendering dependencies. Root `requirements-render.txt` is a compatibility forwarding file used by CI. **Neither file installs LibreOffice or Poppler.** Do not install unrelated heavy ML frameworks merely to draw or export a poster.

## Portable, self-contained QA

From within this repository:

~~~bash
python .agents/skills/research-poster/scripts/preflight.py \
  posters/artificial-intelligence/natural-language-processing/attention-is-all-you-need

# Enforce completeness and one-page PDF checks (requires pdfinfo):
python .agents/skills/research-poster/scripts/preflight.py \
  posters/artificial-intelligence/natural-language-processing/attention-is-all-you-need \
  --strict --json
~~~

When copying the skill to another repository, call `<installed-skill-dir>/scripts/preflight.py /path/to/paper`. The script never creates or modifies source assets; it only inspects them.

## Render and publish pipeline in this repository

~~~bash
python -m pip install -r requirements-render.txt
python scripts/render_posters.py
python scripts/validate_catalog.py --strict-assets
python -m unittest discover -s tests -v
python scripts/build_site.py --output _site
~~~

The current renderer executes tracked `make_poster.py` programs under `posters/`, then converts generated PPTX into a PDF with LibreOffice and into a PNG preview with Poppler. **Only execute trusted, reviewed authoring scripts.** For LaTeX, Inkscape, manually edited PPTX or other tools, supply a distinct, documented build process instead of implying the Python renderer supports them.

## Failure and fallback behavior

- No optional dependencies: still produce evidence, storyboard, SVG or a template; report PPTX/PDF as **not generated**.
- No `pdfinfo`: non-strict preflight can perform signature checks but must warn that page count was not verified. Strict preflight fails rather than quietly certifying the PDF.
- Missing/unreadable PNG, SVG, PPTX or PDF: do not promote the record to published until artifacts meet the stated publication contract.
- Unavailable official paper: label claims unverified; do not invent results, source pages or citations.
- Existing published paper: preserve assets and source. A new version needs deliberate review and coherent regenerated outputs.
