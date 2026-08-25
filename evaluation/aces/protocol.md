# ACES-style evaluation protocol (preregistered)

> **What this is:** an application of the methodology in *Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills* (arXiv:2608.20614, "ACES") to the `ingredient-opportunity-research` skill. ACES measures a skill's **marginal contribution** by running paired with-skill / baseline trials on author-owned tasks and reporting **Skill Lift** (with-skill reward minus baseline reward) under a fixed agent, task, harness and grading policy.
>
> **Status:** preregistered in two auditable steps. (1) Protocol, structured evaluation assets (`evals.json`), prompts and frozen facts packs are committed **before** any trial output is generated. (2) Trial outputs are anonymized into `blind/` and the group key with SHA-256 hashes is committed **before** any review session starts — closing the mapping-auditability gap the repo's earlier benchmarks disclosed.

## Why this evaluation exists

The repo's existing evidence ([minimal-prompt-benchmark](../minimal-prompt-benchmark/README.md), [three-case-comparison](../three-case-comparison/README.md)) already compares Direct vs Skill on mean rubric totals. What those benchmarks do not measure, and what ACES adds:

1. **Per-behavior grading** — ACES grades each `expected_behavior` assertion individually (YES/NO, the `behavior_check` metric) instead of one coarse 100-point rubric score, so we can see *which* behaviors the skill reliably produces.
2. **Skill Lift as a paired delta** — per-case with-skill minus baseline deltas aggregated with a confidence interval, reported in both a composite view (process + outcome metrics) and an outcome-only view, following ACES's anti-gaming separation.
3. **Negative-control cases** — cases the skill should *not* claim to handle (ACES `expected_skill: null`), so over-triggering and boundary failures are visible.
4. **Discovery / routing testing** — ACES's isolation-vs-group and decoy logic, adapted to test whether the skill's own description triggers correctly and routes correctly when other skills are present.
5. **Static-vs-live correlation** — ACES reports that scan scores and live lift are essentially uncorrelated; we test the same question for this skill: does the 100-point rubric score (static) predict behavior-level pass rate (live)?

## Adapted metric set

ACES defines six default runtime metrics; each is adapted here to an analysis-skill artifact (the "trajectory" is the memo the agent writes from a frozen facts pack):

| ACES metric | Adaptation | Scale |
|---|---|---|
| `security` | Evidence hygiene: no facts beyond the pack presented as fact, no invented sources/numbers, no unsafe capital recommendation (no "build now" while a veto blocker is unresolved) | 0/1 |
| `skill_execution` | Workflow activation: fraction of the 6-item required-workflow checklist present in the output (identity statement, hard gates, evidence separation, adoption/coverage discipline, search-coverage disclosure, smallest next validation). Items not applicable to a case are excluded. | 0–1 |
| `skill_efficiency` | Decision coverage: fraction of the case rubric's scored criteria with a non-zero score (dimension coverage density) | 0–1 |
| `accuracy` | Five binary questions per case (correct identity handling; correct key-signal classification; factual consistency with the pack; user's task addressed; recommendation actionable) | 0–1 (yes-count/5) |
| `goal_accuracy` | Did the memo give a clear, decision-usable answer to the stated question (recommendation/classification + reason)? | 0/1 |
| `behavior_check` | Fraction of the case's `expected_behavior[]` assertions satisfied (each graded YES/NO) | 0–1 |

**Composite** = mean of the six (ACES default equal-weight composite). **Outcome-only** = mean of `accuracy` and `goal_accuracy` (ACES Appendix A). Composite and outcome-only are reported side by side; the process metrics (`behavior_check`, `skill_execution`, `skill_efficiency`) can be definitionally favorable to the with-skill arm, so the outcome-only view is the conservative headline.

## Skill Lift

Per case, per metric: `Lift = mean(Skill outputs) − mean(Direct outputs)` (for the frozen cases, 3 outputs per condition; for the new cases, 1 per condition). Per-case composite lift is the mean of the six metric deltas. Overall lift is the mean of per-case lifts across all six cases, with a 95% normal CI over per-case deltas (descriptive, as in ACES §6.3 — cases are clustered, not independent skills). The distribution of per-case composite lift (positive / zero / negative) is reported. Negative lift is a debugging signal, not a failure of the evaluation.

## Cases

| id | Route | Prompt language | Condition | Primary decision signals |
|---|---|---|---|---|
| `fermadhax` | feasibility + capital decision | zh | **reuse frozen** (3+3 outputs, existing rubric scores) | false supply-demand gap, nameplate vs saleable supply, duplicate/non-binding RFQs, incomparable price |
| `mycopro-pv9` | feasibility + capital decision | zh | **reuse frozen** (3+3) | strain/legal-route transfer, dog-to-cat extrapolation, protein-cost mismatch, unsupported claims |
| `dermabis-a95` | feasibility + capital decision | zh | **reuse frozen** (3+3) | identity/stereochemistry, format fit, SKU adoption inference, opaque market size, internal cost/price veto |
| `omega3-gap` | **new** market-size + supply-demand gap audit | zh | **fresh** (1+1) | demand-maturity vs supply-constraint vs evidence-status separation; forbidden gap inferences |
| `industrial-boundary` | **new negative control** (non-consumer) | en | **fresh** (1+1) | partial-applicability boundary; no force-fit of consumer modules |

Frozen cases reuse the already-committed facts packs, one-sentence prompts, outputs and rubric scores in `minimal-prompt-benchmark/` and `three-case-comparison/`; this evaluation adds the behavior-level grading layer over the same evidence. New cases get new synthetic facts packs (committed here), one-sentence prompts, and case rubrics.

**Registered asset-only cases (added 2026-08-24):** the four remaining `test-scenarios.md` routes — `isomalt-bakery`, `gellan-consumer`, `nootkatone-market`, `hmo-global` — are registered in `evals.json` as `trial_type: "registered"` with their `expected_behavior[]` sets (no trial evidence yet; a frozen facts pack must be constructed before each is run). The schema validator in `scripts/validate_project.py` enforces this asset contract in CI.

## Trial execution (new cases)

Both conditions receive the same frozen facts pack, the same one-sentence prompt, the same output limit (≤ 1,200 Chinese characters for `omega3-gap`; ≤ 800 English words for `industrial-boundary`), and the same prohibition on browsing, web search, or adding facts beyond the pack.

- **Direct (baseline):** the base model, no access to the skill or its references, no prescribed framework.
- **Skill (with-skill):** the same model family, instructed to read and follow `skill/ingredient-opportunity-research/` (SKILL.md plus applicable references) before writing, subject to the same browsing/facts constraints.

The skill's workflow normally drives live web research; this controlled design withholds browsing so both arms reason over identical evidence — measuring the framework's effect on coverage and decision discipline, not retrieval. Each new-case condition runs in a fresh session (1 per condition per case, as scoped).

## Blind review

All outputs (18 frozen + 4 new) are copied to `blind/` under fresh anonymous names, with no condition labels. The group key is written **and hash-committed before any review session starts**. Reviewers are separate fresh sessions that:

- never see `group-key.md` or any file outside the listed `blind/` paths, facts packs and rubrics;
- grade each output per case on: `expected_behavior[]` YES/NO (behavior_check), the 6-item workflow checklist (skill_execution), per-criterion rubric scores (skill_efficiency + rubric total), 5 accuracy questions, goal_accuracy, and security;
- record hard failures (frozen rubrics' hard-failure clauses) as `hard_failure: true/false`.

Frozen-case rubric totals are reused from the already-published `scores.csv` files, not rescored.

## Routing tests

ACES tests discovery (does the agent find the skill) and group routing (does it pick the right skill among decoys). Adapted:

- **Test A — trigger precision/recall:** a fresh session sees only the skill's public description and answers, for 9 requests, whether the skill should be triggered (6 should-trigger ingredient requests, 3 should-not). Reports precision and recall of triggering.
- **Test B — group routing with decoys:** a fresh session sees three skill descriptions (this skill, a project-due-diligence skill, a generic market-report generator) and routes 3 requests (ingredient; company due-diligence; ambiguous industry trend). Checks over- and under-triggering in a multi-skill workspace (the ACES group-mode / routing-premium concern).

## Preregistered interpretation gates

1. The 6-metric composite lift is reported with its CI; **no gate requires positive lift** — a null or negative result is a valid, publishable outcome (the repo retains null results by policy).
2. Outcome-only lift is the conservative headline for any "the skill helps" claim.
3. No hard failures are expected in either arm on the frozen cases (previously published); new cases' hard failures are reported as-is.
4. The static-vs-live correlation (rubric total vs behavior_check pass rate) is reported descriptively; either a near-zero or a positive correlation is informative.

## Reproducibility

`python3 scripts/analyze_aces.py` recomputes all lifts, CIs and correlations from `scores.csv`. Raw outputs, the group key (with SHA-256 hashes), review sheets and the run log are committed. Exact model versions and sampling parameters are not exposed by the harness; output generation is therefore not bit-reproducible, matching the disclosure made by the repo's earlier benchmarks.
