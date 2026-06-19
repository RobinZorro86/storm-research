import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.render_report import render
from scripts.select_perspectives import select
from scripts.validate_session import validate

ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def test_selects_explainable_perspectives(self):
        result = select(["tech", "biz"], "medium")
        self.assertEqual(5, len(result["selected"]))
        self.assertTrue(all(item["reason"] for item in result["selected"]))
        self.assertIn("biz-customer", [item["id"] for item in result["selected"]])

    def test_rejects_empty_domains(self):
        with self.assertRaises(ValueError):
            select([], "simple")

    def test_valid_session_passes(self):
        session = json.loads((ROOT / "tests/fixtures/valid-session.json").read_text())
        errors, metrics = validate(session)
        self.assertEqual([], errors)
        self.assertEqual(1.0, metrics["claim_citation_coverage"])

    def test_unsupported_claim_fails(self):
        session = json.loads((ROOT / "tests/fixtures/invalid-session.json").read_text())
        errors, _ = validate(session)
        self.assertGreaterEqual(len(errors), 2)

    def test_report_contains_source_and_counter_evidence(self):
        session = json.loads((ROOT / "tests/fixtures/valid-session.json").read_text())
        report = render(session)
        self.assertIn("Official docs", report)
        self.assertIn("Counter-evidence", report)


if __name__ == "__main__":
    unittest.main()
