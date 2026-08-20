#!/usr/bin/env python3
"""Dependency-free structural validation for this portfolio repository."""

from pathlib import Path
import csv
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "ingredient-opportunity-research"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "docs" / "PRD.md",
    ROOT / "docs" / "product-case-study.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    ROOT / "evaluation" / "case-audit.md",
    ROOT / "evaluation" / "iteration-log.md",
    ROOT / "evaluation" / "controlled-test" / "README.md",
    ROOT / "evaluation" / "controlled-test" / "evidence-pack.md",
    ROOT / "evaluation" / "controlled-test" / "review-rubric.md",
    ROOT / "evaluation" / "controlled-test" / "blind-review.md",
    ROOT / "evaluation" / "controlled-test" / "memo-a.md",
    ROOT / "evaluation" / "controlled-test" / "memo-b.md",
    ROOT / "evaluation" / "controlled-test" / "memo-c.md",
    ROOT / "evaluation" / "three-case-comparison" / "README.md",
    ROOT / "evaluation" / "three-case-comparison" / "protocol.md",
    ROOT / "evaluation" / "three-case-comparison" / "run-log.md",
    ROOT / "evaluation" / "three-case-comparison" / "scores.csv",
    ROOT / "evaluation" / "three-case-comparison" / "case-01-fermadhax" / "README.md",
    ROOT / "prompts" / "example-prompts.md",
    ROOT / "examples" / "01-isomalt-china-bakery.md",
    ROOT / "examples" / "02-gellan-gum-consumer-products.md",
    ROOT / "examples" / "03-hmo-global-market.md",
    ROOT / "examples" / "04-bisabolol-china-skincare.md",
    SKILL / "references" / "market-size-and-demand.md",
    SKILL / "references" / "product-format-screening.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


for path in REQUIRED:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
frontmatter_match = re.match(r"^---\n(.*?)\n---", skill_text, re.DOTALL)
if not frontmatter_match:
    fail("SKILL.md is missing YAML frontmatter")
frontmatter_lines = frontmatter_match.group(1).splitlines()
frontmatter = {}
for line in frontmatter_lines:
    if line.startswith(" ") or ":" not in line:
        continue
    key, value = line.split(":", 1)
    frontmatter[key] = value.strip().strip('"').strip("'")
allowed_keys = {"name", "description", "license", "allowed-tools", "metadata"}
unexpected_keys = set(frontmatter) - allowed_keys
if unexpected_keys:
    fail(f"unexpected SKILL.md frontmatter keys: {sorted(unexpected_keys)}")
name = frontmatter.get("name", "")
description = frontmatter.get("description", "")
if name != "ingredient-opportunity-research":
    fail("SKILL.md has an unexpected skill name")
if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
    fail("SKILL.md name is not valid hyphen-case")
if not description:
    fail("SKILL.md is missing its description")
if len(description) > 1024 or "<" in description or ">" in description:
    fail("SKILL.md description violates skill metadata constraints")

default_prompt = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
if "$ingredient-opportunity-research" not in default_prompt:
    fail("agents/openai.yaml default prompt does not invoke the skill")

for ref in re.findall(r"\]\((references/[^)#]+\.md)\)", skill_text):
    if not (SKILL / ref).is_file():
        fail(f"SKILL.md points to missing reference: {ref}")

link_pattern = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
for markdown in ROOT.rglob("*.md"):
    text = markdown.read_text(encoding="utf-8")
    for raw_target in link_pattern.findall(text):
        target = raw_target.split("#", 1)[0]
        if not target or target in {"URL", "url"}:
            continue
        if not (markdown.parent / target).resolve().exists():
            fail(
                f"broken local link in {markdown.relative_to(ROOT)}: {raw_target}"
            )

for report in (ROOT / "examples").glob("*.md"):
    text = report.read_text(encoding="utf-8")
    if "执行结论" not in text:
        fail(f"example lacks an executive conclusion: {report.name}")
    if not any(term in text for term in ("完整性", "证据缺口", "最终判断")):
        fail(f"example lacks an evidence-gap/completeness section: {report.name}")

def section(text: str, heading: str, next_heading: str) -> str:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        fail(f"bisabolol example lacks section boundary: {heading}")
    return text[start:end]


bisabolol = (ROOT / "examples" / "04-bisabolol-china-skincare.md").read_text(
    encoding="utf-8"
)
format_section = section(bisabolol, "### 5.1 产品形态筛选", "### 5.2")
market_section = section(bisabolol, "### 9.1 原料市场规模审计", "### 9.2")
adoption_section = section(bisabolol, "## 8. 可验证的产品采用信号", "## 9.")
completeness_section = section(bisabolol, "## 12. 研究完整性检查", "## 主要来源")

required_by_section = {
    "product-format": (
        format_section,
        (
            "基质/工艺与包装",
            "接触模式",
            "证据用量",
            "法规/宣称",
            "替代方案",
            "当前采用",
            "形态市场证据",
            "买家",
            "结果/决定性缺口",
            "`conditional—technical test`",
            "`conditional—market evidence`",
            "`regulatory unresolved`",
            "`do not advance`",
        ),
    ),
    "market-demand": (
        market_section,
        (
            "访问日：",
            "来源动机",
            "独立性",
            "| Supply |",
            "| Trade |",
            "| Downstream use |",
            "敏感性",
            "not reliably estimable from available evidence",
        ),
    ),
    "adoption": (
        adoption_section,
        (
            "便利样本",
            "纳入规则",
            "渠道仅含品牌官网",
            "证据类/观察日",
            "交叉佐证",
            "当前在售状态",
            "possible use",
            "unclassified single-source official-page evidence",
        ),
    ),
    "completeness": (
        completeness_section,
        (
            "| 规则 | 结果 | 支持证据 | 精确缺口 | 对结论的影响 | 下一步 |",
            "Research contract",
            "Generalization",
            "Ingredient identity",
            "Ingredient properties and sources",
            "Property-to-application map",
            "Functional equivalents",
            "Replacement/co-formulation economics",
            "Product-format screening",
            "Regulation and claims",
            "Raw-material price",
            "Market size and demand",
            "Use amount and cost",
            "Application-case/use amount",
            "Technical/literature validation",
            "Product/company adoption",
            "SKU universe/current sale",
            "Effects and adverse evidence",
            "SMART consumer/commercial evidence",
            "Market awareness/education",
            "Target-language terminology",
            "Potential customers/KA priority",
            "Final report integrity",
            "Decision-readiness blockers",
        ),
    ),
}
for audit_name, (audit_section, markers) in required_by_section.items():
    for marker in markers:
        if marker not in audit_section:
            fail(f"bisabolol {audit_name} audit lacks required marker: {marker}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
prd = (ROOT / "docs" / "PRD.md").read_text(encoding="utf-8")
case_audit = (ROOT / "evaluation" / "case-audit.md").read_text(encoding="utf-8")
if "examples/04-bisabolol-china-skincare.md" not in readme:
    fail("README does not register the bisabolol case")
if "Bisabolol pre-audit" not in case_audit:
    fail("case audit does not register the bisabolol pre-audit")

for marker in (
    "化工企业战略发展部",
    "一票否决项",
    "证据台账",
    "可执行验证清单",
    "工艺开发",
    "生产成本",
    "真实成交价",
    "80%–90%",
    "用户报告的初步结果",
    "可组合战略分析工具",
):
    if marker not in prd:
        fail(f"PRD lacks confirmed product input or evidence boundary: {marker}")

controlled = ROOT / "evaluation" / "controlled-test"
controlled_readme = (controlled / "README.md").read_text(encoding="utf-8")
blind_review = (controlled / "blind-review.md").read_text(encoding="utf-8")
memo_c = (controlled / "memo-c.md").read_text(encoding="utf-8")
for marker in (
    "No Skill | 96/100",
    "Skill before repair | 99/100",
    "Skill after one-rule repair | 100/100",
    "not an unbiased market benchmark",
):
    if marker not in controlled_readme:
        fail(f"controlled-test README lacks evidence boundary: {marker}")
for marker in ("96/100", "99/100", "100/100", "Hard failures: none"):
    if marker not in blind_review:
        fail(f"blind review lacks required result: {marker}")
for marker in (
    "活性规格",
    "数量",
    "日期",
    "税费",
    "运费/Incoterms",
    "付款条件",
    "供应商类型",
):
    if marker not in memo_c:
        fail(f"repaired memo lacks named price mismatch: {marker}")

comparison = ROOT / "evaluation" / "three-case-comparison"
for case_name in ("case-02-mycopro-pv9", "case-03-dermabis-a95"):
    for filename in (
        "evidence-pack.md",
        "rubric.md",
        "memo-a.md",
        "memo-b.md",
        "blind-review.md",
        "group-key.md",
    ):
        path = comparison / case_name / filename
        if not path.is_file():
            fail(f"three-case comparison lacks {case_name}/{filename}")

comparison_readme = (comparison / "README.md").read_text(encoding="utf-8")
protocol = (comparison / "protocol.md").read_text(encoding="utf-8")
run_log = (comparison / "run-log.md").read_text(encoding="utf-8")
for marker in (
    "Direct | Skill | Delta",
    "**283**",
    "**298**",
    "**94.3**",
    "**99.3**",
    "Both groups avoided all hard failures",
    "Unsupported claims",
):
    if marker not in comparison_readme:
        fail(f"three-case comparison README lacks result/boundary: {marker}")
for marker in (
    "Every case is synthetic",
    "If Group Direct equals or beats Group Skill",
    "not proof of general model superiority",
):
    if marker not in protocol:
        fail(f"three-case protocol lacks preregistered boundary: {marker}")
for marker in (
    "commit `9b524d0`",
    "commit `1165db3`",
    "first response omitted Case 3",
    "Exact serving model identifiers and sampling seeds were not recorded",
):
    if marker not in run_log:
        fail(f"three-case run log lacks process disclosure: {marker}")

with (comparison / "scores.csv").open(encoding="utf-8", newline="") as handle:
    score_rows = list(csv.DictReader(handle))
if len(score_rows) != 27:
    fail(f"three-case score data expected 27 rows, found {len(score_rows)}")
direct_total = sum(int(row["direct_score"]) for row in score_rows)
skill_total = sum(int(row["skill_score"]) for row in score_rows)
if (direct_total, skill_total) != (283, 298):
    fail(
        "three-case score totals do not match published result: "
        f"Direct={direct_total}, Skill={skill_total}"
    )
if any(
    row["direct_hard_failure"] != "false"
    or row["skill_hard_failure"] != "false"
    for row in score_rows
):
    fail("three-case score data contains an undisclosed hard failure")

print(
    "PASS: project structure, skill references, local links, examples, "
    "controlled tests, and three-case score data validated"
)
sys.exit(0)
