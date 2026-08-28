#!/usr/bin/env python3
"""Dependency-free structural validation for generated feasibility reports.

This script checks the report-level contract that the skill promises in
references/feasibility-report-template.md and
references/research-quality-rules.md:

  - a decision-relevant executive conclusion exists near the top;
  - material claims carry evidence levels (E1-E5) and inline sources;
  - no model-authored opportunity grade or score (research-quality
    self-assessment is allowed and must not be confused with an
    opportunity score);
  - an explicit evidence-gap / completeness / decision-readiness section
    closes the report;
  - food reports audit China, the United States and the European Union
    instead of one global regulatory status;
  - shortage/undersupply claims trigger a supply-demand gap audit instead
    of being asserted as committed demand.

It validates structure, not facts. Passing does not mean the report is
factually correct or commercially valid; it means the report honours the
format and evidence-boundary contract.

Usage:
  python3 scripts/validate_report.py <report.md> [<report.md> ...]
  python3 scripts/validate_report.py --examples   # validate examples/*.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"

# A model-authored opportunity grade/score is forbidden by the skill.
# Research-quality self-assessment (质量自审/自审) is allowed and must be
# kept separate from market-opportunity judgment.
OPPORTUNITY_SCORE_RE = re.compile(
    r"(机会分|机会评分|opportunity\s+score|attractiveness\s+score|"
    r"投资评分|market\s+opportunity\s+score|机会指数)"
)
ALLOWED_SELF_ASSESSMENT = ("自审", "质量自审", "research-quality", "完整性检查")

EVIDENCE_LEVEL_RE = re.compile(r"\bE[1-5]\b")
# Examples and older reports may use the 已验证/推断/待验证 marker system
# instead of E1-E5; both are accepted evidence-level conventions.
LEGACY_EVIDENCE_RE = re.compile(
    r"(已验证|推断|待验证|confirmed|development evidence|possible use|verified current use)"
)
INLINE_SOURCE_RE = re.compile(
    r"(https?://[^\s\)\]\|]+|doi:\s*10\.\d{4,}|10\.\d{4,}/[^\s\)\]\|]+)"
)
FOOD_MARKERS = ("GB 2760", "GB 14880", "食品添加剂", "食品类别", "营养强化剂", "新食品原料")
JURISDICTIONS = (("中国", "CN"), ("美国", "US"), ("欧盟", "EU"))
GAP_MARKERS = (
    "完整性",
    "证据缺口",
    "not reliably estimable",
    "decision-ready",
    "决策就绪",
    "阻断",
    "待验证",
)
SHORTAGE_MARKERS = (
    "供不应求",
    "短缺",
    "undersupply",
    "shortage",
    "产能不足",
    "低渗透",
    "供给不足",
)
GAP_AUDIT_MARKERS = (
    "需求成熟度",
    "demand maturity",
    "supply constraint",
    "供给约束",
    "供需",
    "supply-demand",
    "evidence status",
)


BIBLIO_HEADING_PREFIXES = ("Sources", "主要来源", "References", "参考来源")


def is_bibliography_heading(heading: str) -> bool:
    """A bibliography heading may carry a parenthetical note (e.g.
    'Sources（合并文献目录；行内引用已在各表）'); match by prefix."""
    return any(heading.startswith(prefix) for prefix in BIBLIO_HEADING_PREFIXES)


def check_report(path: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    name = path.relative_to(ROOT).as_posix()

    if "# " not in text:
        errors.append(f"{name}: missing a top-level title")

    # 1. Executive conclusion is the first major section.
    first_h2 = re.search(r"^##\s+(.+)$", text, re.M)
    if first_h2 is None:
        errors.append(f"{name}: no second-level section heading found")
    elif not re.search(r"结论|Conclusion", first_h2.group(1)):
        errors.append(
            f"{name}: the first major section is {first_h2.group(1)!r}; "
            "the executive conclusion must come first"
        )

    # 1b. Top-level sections use Arabic numbering (## 1., ## 2., ...);
    # a trailing bibliography heading (Sources / 主要来源) is the only exception.
    for line in text.splitlines():
        if not re.match(r"^##\s", line):
            continue
        heading = line[3:].strip()
        if re.match(r"^\d+\.", heading):
            continue
        if is_bibliography_heading(heading):
            continue
        errors.append(
            f"{name}: unnumbered top-level heading {heading!r}; "
            "use Arabic numbering (## 1., ## 2., ...)"
        )
        break

    # 2. Evidence levels and inline sources.
    if not EVIDENCE_LEVEL_RE.search(text) and not LEGACY_EVIDENCE_RE.search(text):
        errors.append(
            f"{name}: no evidence level found (E1-E5 or 已验证/推断/待验证) "
            "on material claims"
        )
    if len(INLINE_SOURCE_RE.findall(text)) < 3:
        errors.append(
            f"{name}: fewer than 3 inline sources (URL/DOI) found; "
            "material claims need inline citations"
        )

    # 2b. A trailing bibliography must not be the only citation source.
    body = re.split(
        r"^##\s+(?:Sources|主要来源|References|参考来源)", text, flags=re.M
    )[0]
    if len(INLINE_SOURCE_RE.findall(text)) >= 3 and len(INLINE_SOURCE_RE.findall(body)) < 3:
        errors.append(
            f"{name}: inline citations appear only in the trailing bibliography; "
            "material claims need per-claim inline sources"
        )

    # 3. No model-authored opportunity score.
    for match in OPPORTUNITY_SCORE_RE.finditer(text):
        context = text[max(0, match.start() - 60): match.end() + 60]
        if any(marker in context for marker in ALLOWED_SELF_ASSESSMENT):
            continue
        errors.append(
            f"{name}: model-authored opportunity score marker {match.group()!r}; "
            "keep research-quality assessment separate from opportunity judgment"
        )

    # 4. Evidence-gap / completeness / decision-readiness section.
    if not any(marker in text for marker in GAP_MARKERS):
        errors.append(
            f"{name}: missing an evidence-gap / completeness / decision-readiness section"
        )

    # 5. Food reports audit CN/US/EU separately.
    if any(marker in text for marker in FOOD_MARKERS):
        present = [label for label, _ in JURISDICTIONS if label in text]
        if len(present) < 2:
            warnings.append(
                f"{name}: food report covers {', '.join(present) or 'none'} of "
                "CN/US/EU; expected a cross-jurisdiction comparison"
            )

    # 6. Shortage/undersupply claims require a supply-demand gap audit.
    if any(marker in text for marker in SHORTAGE_MARKERS):
        if not any(marker in text for marker in GAP_AUDIT_MARKERS):
            warnings.append(
                f"{name}: shortage/undersupply language found without a "
                "supply-demand gap audit (demand maturity / supply constraint / "
                "evidence status)"
            )

    for issue in errors:
        print(f"[ERROR] {issue}")
    for issue in warnings:
        print(f"[WARN]  {issue}")
    if errors:
        print(f"validate_report: FAILED ({len(errors)} error(s)) in {name}")
    return 1 if errors else 0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args == ["--examples"]:
        targets = sorted(EXAMPLES.glob("*.md"))
    else:
        targets = [ROOT / arg for arg in args]
    if not targets:
        print("no report files found", file=sys.stderr)
        return 2
    failures = 0
    for target in targets:
        if target.name == "README.md":
            continue
        if not target.is_file():
            print(f"[ERROR] missing report file: {target}", file=sys.stderr)
            failures += 1
            continue
        failures += check_report(target)
    if failures:
        print(f"validate_report: {failures} file(s) failed")
        return 1
    print("validate_report: all reports passed structural checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
