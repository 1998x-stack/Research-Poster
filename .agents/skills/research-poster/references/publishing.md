# GitHub Pages workflow and security

## Build chain
GitHub push/dispatch → checkout → validate source JSON and taxonomy → (optionally) render source-backed PPTX/PDF/preview → regenerate `_site/index.html` + `catalog.json` + poster detail pages → upload Pages artifact → deploy-pages.

## Initial setup
One-time repository admin step: **Settings → Pages → Build and deployment → Source → GitHub Actions**. Site URL for this project is `https://1998x-stack.github.io/Research-Poster/`. Inspect the actual Pages deployment environment and visit public site; do not equate uploaded YAML with a working Pages site.

## Security
- Publish only from `main`; PR checks validate but never deploy untrusted code.
- Pin major workflow actions, keep `contents: read` by default and `pages: write`/`id-token: write` only on deployment job.
- Do not run arbitrary code received with unreviewed PRs using privileged tokens.
- Never place secrets/tokens, submitted private papers, author email addresses, sensitive datasets or API keys inside `_site`.
- Treat all `poster.json` text as untrusted when generating HTML; escape output; whitelist safe local asset paths.
- Site should work offline from static assets and within a project base path.

## Validation
`python scripts/validate_catalog.py` catches bad slugs/categories, duplicate IDs, unsound URLs and missing source fields. `python scripts/build_site.py` generates all pages. CI must fail closed on malformed metadata; no empty green success from a failed subprocess.