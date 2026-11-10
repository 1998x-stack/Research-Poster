#!/usr/bin/env python3
"""Create a non-destructive draft poster in the canonical CS taxonomy."""
from __future__ import annotations

import argparse
from datetime import date
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / ".agents/skills/research-poster/assets/templates"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:90].strip("-")


def apply_template(name: str, title: str, url: str) -> str:
    source = (TEMPLATES / name).read_text(encoding="utf-8")
    return (source.replace("{{TITLE}}", title)
                  .replace("{{SOURCE_URL}}", url))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ("title", "category", "subcategory", "venue", "authors", "url"):
        parser.add_argument("--" + field, required=True)
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--slug", help="Explicit ASCII slug (for non-English titles)")
    parser.add_argument("--version", default="author-provided / to verify")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    taxonomy = json.loads((ROOT / "catalog/taxonomy.json").read_text(encoding="utf-8"))
    allowed = {(cat["id"], sub["id"])
               for cat in taxonomy["categories"] for sub in cat["subfields"]}
    if (args.category, args.subcategory) not in allowed:
        parser.error("Unknown taxonomy path; inspect catalog/taxonomy.json")
    slug = args.slug or slugify(args.title)
    if not SLUG.fullmatch(slug):
        parser.error("Provide an ASCII lower-kebab-case --slug")
    url = urlsplit(args.url)
    if url.scheme != "https" or not url.netloc or url.username:
        parser.error("--url must be a public HTTPS paper URL")
    if not 1940 <= args.year <= date.today().year + 1:
        parser.error("Year is out of expected range")
    authors = [value.strip() for value in args.authors.split(";") if value.strip()]
    if not authors:
        parser.error("Provide semicolon-separated authors")

    dest = ROOT / "posters" / args.category / args.subcategory / slug
    if dest.exists():
        parser.error(f"Paper already exists; refusing overwrite: {dest}")
    print("Scaffolding:", dest.relative_to(ROOT))
    if args.dry_run:
        return
    dest.mkdir(parents=True)
    data = {
        "id": slug, "title": args.title, "subtitle": "TODO: evidence-backed contribution",
        "authors": authors, "year": args.year, "venue": args.venue,
        "category": args.category, "subcategory": args.subcategory, "tags": [],
        "summary": "TODO: source-verified summary",
        "takeaway": "TODO: single defensible takeaway",
        "method": "TODO: diagram with provenance",
        "limitations": "TODO: primary-source limitations",
        "source": {
            "url": args.url, "version": args.version,
            "citation": f"{authors[0]} et al. ({args.year}). {args.title}. {args.venue}."
        },
        "assets": {"svg": "poster.svg"},
        "status": "draft", "featured": False, "added": date.today().isoformat()
    }
    (dest / "poster.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (dest / "evidence.md").write_text(
        apply_template("claim-ledger.md", args.title, args.url), encoding="utf-8")
    (dest / "brief.md").write_text(
        apply_template("poster-storyboard.md", args.title, args.url), encoding="utf-8")
    print("Draft only: not shown on Pages until the paper and assets are verified.")
    print("Next: follow .agents/skills/research-poster/SKILL.md and preflight.py")


if __name__ == "__main__":
    main()
