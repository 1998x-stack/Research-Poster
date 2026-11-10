#!/usr/bin/env python3
"""Create a non-destructive draft poster in the canonical CS taxonomy.

Example:
 python scripts/new_poster.py --title 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness' \
   --category machine-learning --subcategory optimization --year 2022 --venue NeurIPS \
   --authors 'Tri Dao; Daniel Y. Fu; Stefano Ermon; Atri Rudra; Christopher Ré' \
   --url https://arxiv.org/abs/2205.14135
"""
from __future__ import annotations
import argparse
from datetime import date
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:90].strip("-")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    for x in ('title', 'category', 'subcategory', 'venue', 'authors', 'url'):
        ap.add_argument('--' + x, required=True)
    ap.add_argument('--year', type=int, required=True)
    ap.add_argument('--slug', help='Explicit ASCII slug (recommended for non-English titles)')
    ap.add_argument('--version', default='author-provided / to verify')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    taxonomy = json.loads((ROOT / 'catalog/taxonomy.json').read_text(encoding='utf-8'))
    valid = {(c['id'], s['id']) for c in taxonomy['categories'] for s in c['subfields']}
    if (args.category, args.subcategory) not in valid:
        ap.error('Unknown taxonomy path; inspect catalog/taxonomy.json')
    slug = args.slug or slugify(args.title)
    if not SLUG.fullmatch(slug):
        ap.error('Provide an ASCII lower-kebab-case --slug')
    parsed = urlsplit(args.url)
    if parsed.scheme != 'https' or not parsed.netloc or parsed.username:
        ap.error('--url must be a public HTTPS paper URL')
    if not 1940 <= args.year <= date.today().year + 1:
        ap.error('Year is out of expected range')
    authors = [x.strip() for x in args.authors.split(';') if x.strip()]
    if not authors:
        ap.error('Provide semicolon-separated authors')

    destination = ROOT / 'posters' / args.category / args.subcategory / slug
    if destination.exists():
        ap.error(f'Poster already exists; refusing overwrite: {destination}')
    print('Scaffolding:', destination.relative_to(ROOT))
    if args.dry_run:
        return
    destination.mkdir(parents=True)
    data = {
        'id': slug, 'title': args.title, 'subtitle': 'TODO: evidence-backed contribution',
        'authors': authors, 'year': args.year, 'venue': args.venue,
        'category': args.category, 'subcategory': args.subcategory,
        'tags': [], 'summary': 'TODO: source-verified summary',
        'takeaway': 'TODO: single defensible takeaway',
        'method': 'TODO: diagram with provenance',
        'limitations': 'TODO: primary-source limitations',
        'source': {'url': args.url, 'version': args.version,
                   'citation': f'{authors[0]} et al. ({args.year}). {args.title}. {args.venue}.'},
        'assets': {'svg': 'poster.svg'},
        'status': 'draft', 'featured': False, 'added': date.today().isoformat()
    }
    (destination / 'poster.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    (destination / 'evidence.md').write_text(
        f'# Evidence ledger: {args.title}\n\nPrimary source: {args.url}\n\n'
        '| Claim | Paper page / table | Experimental setting | Caveat |\n'
        '| --- | --- | --- | --- |\n'
        '| TODO | TODO | TODO | TODO |\n', encoding='utf-8')
    (destination / 'brief.md').write_text(
        f'# Poster brief: {args.title}\n\n'
        '- Main claim: TODO\n- Target audience: TODO\n- Central figure: TODO\n'
        '- Metrics with baselines: TODO\n- Limitations: TODO\n'
        '- Desired visual style: hybrid\n- Export: SVG, PDF, PPTX, PNG\n', encoding='utf-8')
    print('Draft only: it will not appear on Pages until status=published and assets exist.')
    print('Next: read .agents/skills/research-poster/SKILL.md; then validate and build.')


if __name__ == '__main__':
    main()