#!/usr/bin/env python3
"""Dependency-free structural validation for this portfolio repository."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "ingredient-opportunity-research"

REQUIRED = [
    ROOT / "README.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    ROOT / "evaluation" / "case-audit.md",
    ROOT / "prompts" / "example-prompts.md",
    ROOT / "examples" / "01-isomalt-china-bakery.md",
    ROOT / "examples" / "02-gellan-gum-consumer-products.md",
    ROOT / "examples" / "03-hmo-global-market.md",
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

print("PASS: project structure, skill references, local links, and examples validated")
sys.exit(0)
