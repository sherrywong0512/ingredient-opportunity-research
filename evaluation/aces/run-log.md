# Execution log — ACES-style evaluation

All times local (Asia/Shanghai), 2026-08-24. Runs executed inside DeepSeek Harness (`deepseek-v4-flash`), matching the repo's earlier DeepSeek replication.

## Preregistration (auditable sequence)

1. `evaluation/aces/protocol.md`, `evals.json`, `prompts.md`, new-case facts packs and rubrics written and committed **before** any trial output: commit `6ffcec7`.
2. Four fresh trial sessions ran (one per new-case condition):
   - case-04 `omega3-gap` Direct and Skill;
   - case-05 `industrial-boundary` Direct and Skill.
   Both conditions: same frozen facts pack, same one-sentence prompt, no browsing, no facts beyond the pack. Skill sessions read `skill/ingredient-opportunity-research/SKILL.md` plus applicable references before writing (confirmed via each session's run log).
3. All 22 outputs (18 frozen reuse + 4 fresh) anonymized under fresh names into `blind/`; group key with SHA-256 hashes written and committed **before any review session**: commit `d1220d3`.
4. Two fresh blind-review sessions scored the 22 outputs; reviewers were instructed to read only the listed `blind/`, facts-pack and rubric files, never the group key.

## Trial runs

| Trial | Condition | Read skill files | Output |
|---|---|---|---|
| case-04 omega3-gap | Direct | none (control) | `blind/case-04/output-a.md` or `output-b.md` (see group key) |
| case-04 omega3-gap | Skill | SKILL.md, evidence-and-sources.md, market-size-and-demand.md, research-quality-rules.md | the other blind file |
| case-05 industrial-boundary | Direct | none (control) | `blind/case-05/output-a.md` or `output-b.md` (see group key) |
| case-05 industrial-boundary | Skill | SKILL.md, research-quality-rules.md, evidence-and-sources.md | the other blind file |

Frozen cases: outputs reused from `minimal-prompt-benchmark/blind/` (original model family), rubric totals reused from `minimal-prompt-benchmark/scores.csv`.

## Routing tests

- Test A (trigger precision/recall): 6/6 recall, 3/3 precision, no UNSURE.
- Test B (group routing with decoys): 3/3 correct, no over-triggering.

## Review

- Reviewer R1 scored cases 01–02 (12 outputs); Reviewer R2 scored cases 03–05 (10 outputs). Scores recorded in `scores.csv`; per-behavior sheets in `behavior-review.md`; accuracy/goal/security in `accuracy-review.md`.
- `python3 scripts/analyze_aces.py` recomputes all lifts, CIs and correlations from `scores.csv`.

## Known limitations

- Model family: DeepSeek generated and reviewed (same-family review); not an industry-expert reviewer.
- The with-skill memos may structurally reveal the condition through content (e.g., explicit workflow framing); reviewers were instructed to grade content, and the blind names give no hint, but strict blindness cannot be guaranteed.
- 1 run per fresh condition (as scoped); frozen cases carry 3 runs per condition.
- No statistical significance testing; descriptive statistics only.
