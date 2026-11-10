"""Regression tests for the portable poster asset checker (stdlib only)."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/research-poster/scripts/preflight.py"
spec = importlib.util.spec_from_file_location("research_poster_preflight", SCRIPT)
assert spec and spec.loader
preflight = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preflight)


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.paper = {
            "id": "example-paper", "title": "Example Paper", "year": 2026,
            "venue": "Example Venue", "authors": ["Author One"],
            "takeaway": "Verified contribution", "limitations": "Important limits",
            "status": "published",
            "source": {"url": "https://example.org/paper", "version": "v1",
                       "citation": "Author. Example Paper."},
            "assets": {"svg": "poster.svg"},
        }
        (self.folder / "evidence.md").write_text("# Evidence\nThis is a specific primary-source ledger.\n")
        (self.folder / "poster.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><title>Example</title>'
            '<desc>Method schematic</desc><rect width="30" height="30"/></svg>'
        )
        self.save()

    def save(self):
        (self.folder / "poster.json").write_text(json.dumps(self.paper))

    def test_valid_svg_paper_passes_non_strict(self):
        result = preflight.inspect_folder(self.folder)
        self.assertTrue(result["ok"], result["errors"])
        self.assertIn("poster.svg", result["checked"])

    def test_strict_requires_print_pdf(self):
        result = preflight.inspect_folder(self.folder, strict=True)
        self.assertFalse(result["ok"])
        self.assertTrue(any("printable PDF" in e for e in result["errors"]))

    def test_rejects_asset_path_traversal(self):
        self.paper["assets"]["pdf"] = "../outside.pdf"
        self.save()
        result = preflight.inspect_folder(self.folder)
        self.assertFalse(result["ok"])
        self.assertTrue(any("Unsafe or mismatched" in e for e in result["errors"]))

    def test_rejects_active_svg_content(self):
        (self.folder / "poster.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>'
        )
        result = preflight.inspect_folder(self.folder)
        self.assertFalse(result["ok"])
        self.assertTrue(any("active SVG element" in e for e in result["errors"]))

    def test_missing_or_malformed_metadata_fails(self):
        (self.folder / "poster.json").write_text("{bad json")
        result = preflight.inspect_folder(self.folder)
        self.assertFalse(result["ok"])
        self.assertTrue(any("Invalid poster.json" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
