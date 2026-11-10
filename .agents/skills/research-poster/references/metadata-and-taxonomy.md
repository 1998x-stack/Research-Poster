# Paper metadata, taxonomy and conventions

\`catalog/taxonomy.json\` is the one canonical controlled vocabulary. Each subfield path is stable; new fields require taxonomy edit and explanation. A paper gets **one canonical folder** and optional tags spanning other fields, to avoid duplicated assets.

Path: \`posters/<field-id>/<subfield-id>/<lower-kebab-paper-title>/\`. Example: \`posters/artificial-intelligence/natural-language-processing/attention-is-all-you-need/\`.

Each \`poster.json\` should have:
- \`id\`: stable kebab-case slug, globally unique.
- \`title\`, \`subtitle\`, \`year\`, \`venue\`, \`authors\`: source bibliographic fields.
- \`category\` and \`subcategory\`: exact taxonomy IDs.
- \`tags\`: search discovery, not additional canonical directories.
- \`summary\`, \`takeaway\`, \`limitations\`, \`method\`: short text.
- \`source\`: \`url\`, \`version\`, \`citation\`, optional \`doi\` and version caveat.
- \`assets\`: relative safe filenames for svg/preview/pdf/pptx; never absolute or \`..\` traversals.
- \`status\`: \`published\` or \`draft\`. Drafts are excluded from public gallery.
- \`featured\`: boolean; \`added\`: YYYY-MM-DD.

The gallery builder must derive navigation/catalog results exclusively from actual \`poster.json\` files, not hardcoded JS. No server, API keys, remote fonts or database are required.