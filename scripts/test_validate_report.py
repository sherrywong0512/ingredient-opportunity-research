#!/usr/bin/env python3
"""Regression tests for validate_report.py structural checks."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import validate_report


def write_report(tmp: Path, body: str) -> Path:
    path = tmp / "report.md"
    path.write_text(body, encoding="utf-8")
    return path


class HeadingChecksTests(unittest.TestCase):
    def test_fully_compliant_report_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = write_report(
                Path(tmp),
                "# 报告\n\n"
                "## 1. 执行结论\n\n结论：暂不建设。\n\n"
                "## 2. 特性证据\n\n"
                "| 特性 | 结果 | 来源 | 证据等级 |\n"
                "|---|---|---|---|\n"
                "| 甜度 | 200 倍 | https://example.org/1 | E1 |\n"
                "| 热稳定 | 91% | https://example.org/2 | E2 |\n"
                "| 耐受 | 无数据 | https://example.org/3 | U |\n\n"
                "## 3. 证据缺口与下一步\n\n缺口：法规未闭环。下一步：查 GB 2760。\n\n"
                "## Sources\n\n- [来源](https://example.org/1)\n",
            )
            errors: list[str] = []
            warnings: list[str] = []
            with mock.patch.object(validate_report, "ROOT", Path(tmp)):
                rc = validate_report.check_report(path)
            self.assertEqual(rc, 0)

    def test_bibliography_prefix_heading_is_allowed(self) -> None:
        self.assertTrue(validate_report.is_bibliography_heading("Sources（合并文献目录）"))
        self.assertTrue(validate_report.is_bibliography_heading("主要来源（行内引用已在各表）"))
        self.assertTrue(validate_report.is_bibliography_heading("Sources"))
        self.assertFalse(validate_report.is_bibliography_heading("1. Sources of demand"))
        self.assertFalse(validate_report.is_bibliography_heading("来源与缺口"))

    def test_bibliography_only_citations_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = write_report(
                Path(tmp),
                "# 报告\n\n## 1. 执行结论\n\n结论：暂不建设。\n\n"
                "## 2. 特性证据\n\n| 特性 | 结果 |\n|---|---|\n| 甜度 | 200 倍 |\n\n"
                "## Sources\n\n- [来源一](https://example.org/1)\n"
                "- [来源二](https://example.org/2)\n"
                "- [来源三](https://example.org/3)\n",
            )
            errors: list[str] = []
            warnings: list[str] = []
            with mock.patch.object(validate_report, "ROOT", Path(tmp)):
                rc = validate_report.check_report(path)
            self.assertNotEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
