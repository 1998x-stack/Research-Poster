#!/usr/bin/env python3
"""Read-only, stdlib-first integrity preflight for a research-poster folder.

Validates metadata and archive/image structure. With --strict, requires a
published, source-backed printable PDF and uses Poppler pdfinfo for page count.
It does NOT establish scientific accuracy or print-size legibility.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from urllib.parse import urlsplit

ALLOWED = {"svg": ".svg", "pdf": ".pdf", "pptx": ".pptx", "preview": ".png"}
PNG_HEADER = b"\x89PNG\r\n\x1a\n"


def inspect_folder(folder: Path, strict: bool = False) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    checked: list[str] = []

    if not folder.is_dir():
        return {"ok": False, "checked": checked,
                "errors": [f"Not a directory: {folder}"], "warnings": warnings}
    metadata = folder / "poster.json"
    if not metadata.is_file():
        return {"ok": False, "checked": checked,
                "errors": ["Missing poster.json"], "warnings": warnings}
    try:
        paper = json.loads(metadata.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return {"ok": False, "checked": checked,
                "errors": [f"Invalid poster.json: {exc}"], "warnings": warnings}

    if not isinstance(paper, dict):
        return {"ok": False, "checked": checked,
                "errors": ["poster.json must be an object"], "warnings": warnings}
    for field in ("id", "title", "year", "venue", "takeaway", "limitations"):
        if not paper.get(field):
            errors.append(f"Missing metadata field: {field}")
    if not isinstance(paper.get("authors"), list) or not paper["authors"]:
        errors.append("Missing authors array")
    status = paper.get("status")
    if status not in ("draft", "published"):
        errors.append("status must be draft or published")
    elif status == "draft":
        warnings.append("Draft poster: not eligible for public gallery")
        if strict:
            errors.append("Strict preflight requires status=published")

    source = paper.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
    else:
        url = source.get("url")
        if not isinstance(url, str):
            errors.append("source.url must be a public HTTPS URL")
        else:
            parts = urlsplit(url)
            if parts.scheme != "https" or not parts.netloc or parts.username:
                errors.append("source.url must be a public HTTPS URL")
        for field in ("version", "citation"):
            if not source.get(field):
                errors.append(f"Missing source.{field}")

    evidence = folder / "evidence.md"
    if evidence.is_file() and evidence.stat().st_size > 40:
        checked.append("evidence.md")
    elif status == "published":
        (errors if strict else warnings).append("Missing or empty evidence.md")

    assets = paper.get("assets")
    if not isinstance(assets, dict) or not assets:
        errors.append("assets must be a nonempty object")
        assets = {}

    if status == "published" and not ("svg" in assets or "preview" in assets):
        errors.append("Published posters need an SVG or preview")
    if strict and "pdf" not in assets:
        errors.append("Strict preflight requires a printable PDF asset")
    if strict and "pptx" not in assets:
        warnings.append("No editable PPTX declared; document the alternative editable source")

    for kind, filename in assets.items():
        if kind not in ALLOWED:
            errors.append(f"Unsupported asset type: {kind}")
            continue
        if (not isinstance(filename, str) or not filename or
                Path(filename).name != filename or
                filename.startswith(".") or
                Path(filename).suffix.lower() != ALLOWED[kind]):
            errors.append(f"Unsafe or mismatched {kind} filename: {filename!r}")
            continue
        path = folder / filename
        if not path.is_file() or path.stat().st_size == 0:
            if status == "published" or strict:
                errors.append(f"Missing or empty {kind}: {filename}")
            else:
                warnings.append(f"Draft asset not yet generated: {filename}")
            continue

        try:
            if kind == "svg":
                root = ET.parse(path).getroot()
                if root.tag.rsplit("}", 1)[-1] != "svg":
                    raise ValueError("root element is not SVG")
                labels = {e.tag.rsplit("}", 1)[-1] for e in root.iter()}
                if "title" not in labels or "desc" not in labels:
                    warnings.append("SVG lacks <title> or <desc> accessibility labels")
                for element in root.iter():
                    tag = element.tag.rsplit("}", 1)[-1].lower()
                    if tag in ("script", "foreignobject"):
                        raise ValueError(f"active SVG element disallowed: {tag}")
                    for key, value in element.attrib.items():
                        attr = key.rsplit("}", 1)[-1].lower()
                        if attr.startswith("on"):
                            raise ValueError(f"SVG event attribute disallowed: {attr}")
                        if attr == "href" and value.lstrip().lower().startswith(
                                ("javascript:", "data:text/html")):
                            raise ValueError("unsafe SVG href")
            elif kind == "pptx":
                with zipfile.ZipFile(path) as z:
                    if z.testzip() is not None:
                        raise ValueError("corrupted PPTX ZIP member")
                    names = set(z.namelist())
                    if "ppt/presentation.xml" not in names:
                        raise ValueError("missing ppt/presentation.xml")
                    slides = [x for x in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", x)]
                    if not slides:
                        raise ValueError("PPTX contains no slides")
                    ET.fromstring(z.read("ppt/presentation.xml"))
            elif kind == "pdf":
                with path.open("rb") as stream:
                    if stream.read(5) != b"%PDF-":
                        raise ValueError("missing PDF header")
                pdfinfo = shutil.which("pdfinfo")
                if pdfinfo:
                    result = subprocess.run(
                        [pdfinfo, str(path)], capture_output=True, text=True,
                        timeout=30, check=False)
                    if result.returncode:
                        raise ValueError("pdfinfo cannot parse PDF")
                    pages = re.search(r"^Pages:\s*(\d+)\s*$", result.stdout, re.M)
                    if not pages:
                        raise ValueError("pdfinfo did not report page count")
                    if int(pages.group(1)) != 1:
                        raise ValueError(f"PDF must have one page; found {pages.group(1)}")
                elif strict:
                    raise ValueError("pdfinfo missing; install Poppler for strict PDF verification")
                else:
                    warnings.append("pdfinfo unavailable; PDF page count not verified")
            elif kind == "preview":
                with path.open("rb") as stream:
                    header = stream.read(24)
                if len(header) != 24 or not header.startswith(PNG_HEADER) or header[12:16] != b"IHDR":
                    raise ValueError("invalid PNG signature or IHDR")
                width, height = struct.unpack(">II", header[16:24])
                if width < 1 or height < 1:
                    raise ValueError("invalid PNG dimensions")
            checked.append(filename)
        except (OSError, ValueError, ET.ParseError, zipfile.BadZipFile,
                subprocess.TimeoutExpired, struct.error) as exc:
            errors.append(f"Invalid {kind} ({filename}): {exc}")

    return {"ok": not errors, "checked": checked, "errors": errors,
            "warnings": warnings, "paper": paper.get("id", "")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("poster_dir", type=Path, help="Directory containing poster.json")
    parser.add_argument("--strict", action="store_true",
                        help="Require published status and PDF with verifiable single page")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable report")
    args = parser.parse_args()
    report = inspect_folder(args.poster_dir, args.strict)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(("PASS" if report["ok"] else "FAIL") + " poster preflight: " +
              str(args.poster_dir))
        for entry in report["checked"]:
            print("  OK:", entry)
        for entry in report["warnings"]:
            print("  WARNING:", entry)
        for entry in report["errors"]:
            print("  ERROR:", entry, file=sys.stderr)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
