# ACES review of the skill — what the paper suggests, and what changed

Applies the methodology of *Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills* (arXiv:2608.20614, ACES) to `ingredient-opportunity-research`. The companion measurement study lives in [evaluation/aces/](../evaluation/aces/README.md).

## What the skill already had (and the paper would endorse)

- **Differential measurement** (ACES Principle 2): the repo already runs paired Direct-vs-Skill trials ([minimal-prompt-benchmark](../evaluation/minimal-prompt-benchmark/README.md), [three-case-comparison](../evaluation/three-case-comparison/README.md)) — same prompt, same frozen evidence, same scoring policy, only skill availability changes.
- **Retained null results**: the DeepSeek cross-model replication (no overall advantage, 96.8 vs 96.6) is kept on purpose — the paper's own rule that a null or negative lift is a valid, publishable outcome and a debugging signal.
- **Adversarial assertion tables**: `test-scenarios.md`'s gap-audit table (expected classification + forbidden inference per evidence row) is the embryo of the paper's `expected_behavior` mechanism.

## Improvements the paper points to

### 1. Make evaluation assets first-class and machine-readable (ACES §4.1)

Today the scenarios are prose checklists in `test-scenarios.md`, scored by one 100-point rubric total. ACES's core design is a structured per-case asset (`evals.json`) with an ordered `expected_behavior[]` list that an evaluator can grade item by item.

**Action taken:** this repo now ships `evaluation/aces/evals.json` — six cases (three frozen reuse + two new, including one negative control) with 6–9 `expected_behavior` assertions each, plus a fixed 6-item workflow checklist and 5 accuracy questions. Recommendation: over time, mirror each `test-scenarios.md` route as a structured `evals.json` entry so scenarios are executable, not just readable.

### 2. Per-behavior grading instead of one coarse score (behavior_check)

A rubric total cannot say *which* behaviors fail. The paper grades each assertion YES/NO and reports the pass fraction (`behavior_check`). This converts "the skill scored 95" into "the skill reliably separates demand-maturity classes, but systematically forgets to deduplicate same-group RFQs" — which is the actionable form for the author.

**Action taken:** `evaluation/aces/behavior-review.md` grades every output per `expected_behavior`; `scores.csv` keeps the machine-readable per-metric row per output.

### 3. Skill Lift as a paired delta, with composite vs outcome-only separation (ACES §4.7, Appendix A)

The paper separates the composite (process + outcome metrics, equal weight) from the **outcome-only** view (accuracy + goal accuracy), because process metrics like "read the expected skill" are definitionally favorable to the with-skill arm. Any "the skill helps" claim must lead with the conservative view.

**Action taken:** `scripts/analyze_aces.py` computes per-case lifts, composite and outcome-only means with 95% CIs, and the positive/zero/negative distribution — and reports both views side by side.

### 4. Negative-control cases (ACES `expected_skill: null`)

The skill's non-consumer boundary is a prose rule. The paper makes such boundaries executable: a case the skill should *not* claim to handle, so over-triggering and force-fit are measured, not asserted.

**Action taken:** `industrial-boundary` (concrete admixture for infrastructure customers) is a new negative control in `evals.json` with boundary-specific `expected_behavior`s.

### 5. Discovery and routing tests (ACES isolation vs group, decoys)

The paper measures whether the agent finds the skill and picks it among decoys. The skill's routing quality lives in its trigger description.

**Action taken:** `evaluation/aces/routing/` adds (a) trigger precision/recall over 9 requests (6 in-scope, 3 out-of-scope) and (b) group routing with two decoy skills. Both passed on this probe (see the routing READMEs); recommend re-running on model/harness updates.

### 6. Static vs live correlation (ACES §6.7, ρ≈0)

ACES found scan scores are essentially uncorrelated with live lift. The same question applies here: does this skill's 100-point rubric total predict behavior-level pass rate? The answer decides whether rubric scores may be cited as runtime evidence.

**Action taken:** `scripts/analyze_aces.py` reports Spearman(rubric total, behavior_check) and Spearman(rubric total, composite) across outputs.

### 7. CI-native continuous evaluation (ACES §5)

The paper's thesis: evaluation assets live with the artifact and run on every change. The repo's CI currently validates structure only.

**Action taken (partial):** `scripts/analyze_aces.py` is dependency-free and reproducible from `scores.csv`; `evals.json` schema (case ids, required fields, expected_behavior lists, facts-pack references by trial type) is now validated inside `scripts/validate_project.py`, which CI runs on every push — a malformed evaluation asset blocks the build. Recommended next step: a scheduled live re-run after model updates.

### 8. Trajectory / process logs (ATIF analog)

For an analysis skill the "trajectory" is which references the agent read and what coverage it disclosed. The skill already requires search-coverage disclosure in outputs; the eval now also records, per trial, which skill files the with-skill arm actually read (RUNLOG), making the process observable.

### 9. Number-verification step (from the evaluation's replicated finding)

The ACES evaluation reproduced the case-03 "two billion → 两亿件" (factor-of-10) transcription error across two benchmarks. A rule-level fix is now in the skill: `SKILL.md` and `research-quality-rules.md` require re-transcribing every figure against its source and treat a factor-of-10/unit/denominator/period error in a decision-critical figure as a hard defect (skill v1.3.0).

## What the measurement found

See [evaluation/aces/README.md](../evaluation/aces/README.md) for the Skill Lift results, outcome-only view, per-behavior breakdown, static-vs-live correlation and the routing probes — including any null or negative findings, which are retained by policy.
