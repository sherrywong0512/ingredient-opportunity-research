#!/usr/bin/env python3
"""Dependency-free structural validation for this portfolio repository."""

from pathlib import Path
import csv
import re
import statistics
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "ingredient-opportunity-research"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "docs" / "README.zh.md",
    ROOT / "docs" / "PRD.md",
    ROOT / "docs" / "product-case-study.md",
    ROOT / "CHANGELOG.md",
    ROOT / "install.sh",
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
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "README.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "protocol.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "prompts.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "blind-review.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "group-key.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "run-log.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "scores.csv",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "deepseek" / "README.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "deepseek" / "blind-review.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "deepseek" / "group-key.md",
    ROOT / "evaluation" / "minimal-prompt-benchmark" / "deepseek" / "scores.csv",
    ROOT / "prompts" / "example-prompts.md",
    ROOT / "examples" / "README.md",
    ROOT / "examples" / "00-minimal-evidence-demo.md",
    ROOT / "examples" / "01-isomalt-china-bakery.md",
    ROOT / "examples" / "02-gellan-gum-consumer-products.md",
    ROOT / "examples" / "03-hmo-global-market.md",
    ROOT / "examples" / "04-bisabolol-china-skincare.md",
    ROOT / "scripts" / "validate_report.py",
    ROOT / "scripts" / "analyze_aces.py",
    ROOT / "docs" / "aces-review.md",
    ROOT / "evaluation" / "aces" / "README.md",
    ROOT / "evaluation" / "aces" / "protocol.md",
    ROOT / "evaluation" / "aces" / "evals.json",
    ROOT / "evaluation" / "aces" / "group-key.md",
    ROOT / "evaluation" / "aces" / "scores.csv",
    ROOT / "evaluation" / "aces" / "run-log.md",
    ROOT / "evaluation" / "aces" / "routing" / "README.md",
    SKILL / "references" / "market-size-and-demand.md",
    SKILL / "references" / "product-format-screening.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


for path in REQUIRED:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

# The repo-level discovery copy (.agents/skills) must stay byte-identical to
# the skill bundle source (skill/), so cloning + opening the repo in Codex /
# Kimi Code / DeepSeek Harness auto-discovers the skill without install.
agents_copy = ROOT / ".agents" / "skills" / "ingredient-opportunity-research"
if not agents_copy.is_dir():
    fail("missing repo-level discovery copy: .agents/skills/ingredient-opportunity-research")
for skill_path in SKILL.rglob("*"):
    if not skill_path.is_file():
        continue
    relative = skill_path.relative_to(SKILL)
    copy_path = agents_copy / relative
    if not copy_path.is_file() or copy_path.read_bytes() != skill_path.read_bytes():
        fail(f"repo-level skill copy drifted from bundle source: {relative}")

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
allowed_keys = {"name", "description", "license", "allowed-tools", "metadata", "version", "updated"}
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
    if report.name == "README.md":
        continue
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
readme_zh = (ROOT / "docs" / "README.zh.md").read_text(encoding="utf-8")
prd = (ROOT / "docs" / "PRD.md").read_text(encoding="utf-8")
case_audit = (ROOT / "evaluation" / "case-audit.md").read_text(encoding="utf-8")
if "examples/04-bisabolol-china-skincare.md" not in readme_zh:
    fail("docs/README.zh.md does not register the bisabolol case")
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

minimal = ROOT / "evaluation" / "minimal-prompt-benchmark"
for case_name in (
    "case-01-fermadhax",
    "case-02-mycopro-pv9",
    "case-03-dermabis-a95",
):
    if not (minimal / case_name / "facts-only.md").is_file():
        fail(f"minimal benchmark lacks {case_name}/facts-only.md")
    blind_case = minimal / "blind" / case_name
    for response_number in range(1, 7):
        response = blind_case / f"response-{response_number:02d}.md"
        if not response.is_file():
            fail(f"minimal benchmark lacks {response.relative_to(minimal)}")

minimal_readme = (minimal / "README.md").read_text(encoding="utf-8")
minimal_protocol = (minimal / "protocol.md").read_text(encoding="utf-8")
minimal_log = (minimal / "run-log.md").read_text(encoding="utf-8")
for marker in (
    "one simple decision sentence",
    "95.0 mean; 87 min; 13 range; 4.7 SD",
    "85.7 mean; 60 min; 40 range; 11.4 SD",
    "industry-recognized",
    "Counter-evidence and limits",
):
    if marker not in minimal_readme:
        fail(f"minimal benchmark README lacks result/boundary: {marker}")
for marker in (
    "three separate Agent sessions",
    "larger within-case score range and population standard deviation",
    "do not prove recognition by the chemical industry",
):
    if marker not in minimal_protocol:
        fail(f"minimal benchmark protocol lacks preregistered gate: {marker}")
for marker in (
    "commit `7d83e13`",
    "commit `8f756f8`",
    "Exact serving model identifiers and sampling seeds were not recorded",
):
    if marker not in minimal_log:
        fail(f"minimal benchmark run log lacks process disclosure: {marker}")

with (minimal / "scores.csv").open(encoding="utf-8", newline="") as handle:
    minimal_rows = list(csv.DictReader(handle))
if len(minimal_rows) != 18:
    fail(f"minimal benchmark expected 18 rows, found {len(minimal_rows)}")
if any(row["hard_failure"] != "false" for row in minimal_rows):
    fail("minimal benchmark contains an undisclosed hard failure")
expected_cases = {"FermaDHA-X", "MycoPro-PV9", "DermaBis-A95"}
if {row["case"] for row in minimal_rows} != expected_cases:
    fail("minimal benchmark case set does not match the preregistration")
if {row["condition"] for row in minimal_rows} != {"Direct", "Skill"}:
    fail("minimal benchmark contains an unexpected condition")
identities = {(row["case"], row["response"]) for row in minimal_rows}
if len(identities) != 18:
    fail("minimal benchmark contains a duplicate case/response identity")
criterion_columns = [f"criterion_{number}" for number in range(1, 10)]
criterion_maxima = {
    "FermaDHA-X": [12, 14, 14, 14, 10, 8, 10, 10, 8],
    "MycoPro-PV9": [14, 12, 14, 12, 10, 12, 8, 10, 8],
    "DermaBis-A95": [12, 12, 12, 14, 10, 10, 12, 10, 8],
}
for row in minimal_rows:
    criterion_scores = [int(row[column]) for column in criterion_columns]
    criterion_total = sum(criterion_scores)
    if criterion_total != int(row["total"]):
        fail(
            "minimal benchmark criterion sum does not match total for "
            f"{row['case']} response {row['response']}"
        )
    if any(
        score < 0 or score > maximum
        for score, maximum in zip(criterion_scores, criterion_maxima[row["case"]])
    ):
        fail(
            "minimal benchmark criterion is outside rubric bounds for "
            f"{row['case']} response {row['response']}"
        )

group_key_text = (minimal / "group-key.md").read_text(encoding="utf-8")
key_pattern = re.compile(
    r"^\| (FermaDHA-X|MycoPro-PV9|DermaBis-A95) \| (\d{2}) "
    r"\| (Direct|Skill) \| ([123]) \|$",
    re.MULTILINE,
)
group_key = {
    (case, response): (condition, int(run))
    for case, response, condition, run in key_pattern.findall(group_key_text)
}
if len(group_key) != 18:
    fail("minimal benchmark group key does not contain 18 unique mappings")
for row in minimal_rows:
    identity = (row["case"], row["response"])
    if group_key.get(identity) != (row["condition"], int(row["run"])):
        fail(f"minimal benchmark CSV conflicts with group key for {identity}")

review_text = (minimal / "blind-review.md").read_text(encoding="utf-8")
review_case = None
review_scores = {}
review_headings = {
    "## Case 1: FermaDHA-X": "FermaDHA-X",
    "## Case 2: MycoPro-PV9": "MycoPro-PV9",
    "## Case 3: DermaBis-A95": "DermaBis-A95",
}
for line in review_text.splitlines():
    if line in review_headings:
        review_case = review_headings[line]
        continue
    if review_case and re.match(r"^\| \d{2} \|", line):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        response = cells[0]
        review_scores[(review_case, response)] = [int(cell) for cell in cells[1:]]
if len(review_scores) != 18:
    fail("minimal benchmark blind review does not contain 18 score rows")
for row in minimal_rows:
    identity = (row["case"], row["response"])
    csv_scores = [int(row[column]) for column in criterion_columns] + [int(row["total"])]
    if review_scores.get(identity) != csv_scores:
        fail(f"minimal benchmark CSV conflicts with blind review for {identity}")

expected = {
    "Direct": {"scores": [100, 91, 94, 93, 81, 93, 60, 78, 81], "sum": 771},
    "Skill": {"scores": [100, 100, 100, 95, 91, 87, 99, 91, 92], "sum": 855},
}
for condition, published in expected.items():
    rows = [row for row in minimal_rows if row["condition"] == condition]
    scores = [int(row["total"]) for row in rows]
    if len(rows) != 9 or sorted(scores) != sorted(published["scores"]):
        fail(f"minimal benchmark {condition} scores do not match published data")
    if sum(scores) != published["sum"]:
        fail(f"minimal benchmark {condition} total is incorrect")
    for case in {row["case"] for row in rows}:
        case_rows = [row for row in rows if row["case"] == case]
        if sorted(int(row["run"]) for row in case_rows) != [1, 2, 3]:
            fail(f"minimal benchmark {condition}/{case} lacks three unique runs")

direct_scores = expected["Direct"]["scores"]
skill_scores = expected["Skill"]["scores"]
if round(statistics.mean(direct_scores), 1) != 85.7:
    fail("minimal benchmark Direct mean is incorrect")
if round(statistics.mean(skill_scores), 1) != 95.0:
    fail("minimal benchmark Skill mean is incorrect")
if not min(skill_scores) >= 85:
    fail("minimal benchmark Skill completeness gate is not met")
for case in sorted({row["case"] for row in minimal_rows}):
    direct_case = [
        int(row["total"])
        for row in minimal_rows
        if row["case"] == case and row["condition"] == "Direct"
    ]
    skill_case = [
        int(row["total"])
        for row in minimal_rows
        if row["case"] == case and row["condition"] == "Skill"
    ]
    direct_range = max(direct_case) - min(direct_case)
    skill_range = max(skill_case) - min(skill_case)
    if statistics.mean(skill_case) <= statistics.mean(direct_case):
        fail(f"minimal benchmark quality gate is not met for {case}")
    if skill_range >= direct_range:
        fail(f"minimal benchmark range gate is not met for {case}")
    if statistics.pstdev(skill_case) >= statistics.pstdev(direct_case):
        fail(f"minimal benchmark variability gate is not met for {case}")

print(
    "PASS: project structure, skill references, local links, examples, "
    "controlled tests, three-case scores, and minimal-prompt repeats validated"
)
sys.exit(0)
