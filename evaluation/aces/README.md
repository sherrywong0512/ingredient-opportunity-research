# ACES-style evaluation — Skill Lift of ingredient-opportunity-research

Applies the methodology of *Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills* (arXiv:2608.20614, "ACES") to this skill: paired with-skill / baseline trials on author-owned tasks, graded per-behavior, and reported as **Skill Lift** (with-skill reward minus baseline reward) under a fixed agent, task and grading policy.

Method and preregistration: [protocol.md](protocol.md) · structured cases: [evals.json](evals.json) · exact prompts: [prompts.md](prompts.md) · blind outputs: [blind/](blind/) · hash-committed group key: [group-key.md](group-key.md) · per-behavior review: [behavior-review.md](behavior-review.md) · accuracy/goal/security review: [accuracy-review.md](accuracy-review.md) · machine-readable scores: [scores.csv](scores.csv) · execution log: [run-log.md](run-log.md) · routing probes: [routing/](routing/README.md) · paper-to-skill improvement mapping: [docs/aces-review.md](../../docs/aces-review.md).

## Design in one paragraph

Six cases: three reuse the frozen benchmark evidence (`fermadhax`, `mycopro-pv9`, `dermabis-a95`, 18 outputs already in the repo), two are new synthetic cases run fresh in paired conditions (`omega3-gap` — a supply-demand gap audit adversarial to the skill's own forbidden-inference rules; `industrial-boundary` — a **negative control** for a non-consumer material the skill should only partially claim), plus routing probes. Each output is graded blindly on six ACES-adapted metrics: `security`, `skill_execution` (6-item workflow checklist), `skill_efficiency` (rubric-criteria coverage), `accuracy` (5 questions), `goal_accuracy`, `behavior_check` (per-`expected_behavior` YES/NO). Composite = equal-weight mean of the six; outcome-only = mean of `accuracy` and `goal_accuracy` (the conservative headline). Reproduce everything with `python3 scripts/analyze_aces.py`.

## Results (headline, honestly stated)

**On this corpus, the skill's measurable Skill Lift is essentially zero.** The composite lift is 0.0076 (95% CI [0.0004, 0.0149] over 5 per-case deltas) and the outcome-only lift is −0.0067 (95% CI [−0.0197, 0.0064]). Distribution: 3 positive, 2 zero, 0 negative per case. Zero hard failures in either condition.

| Metric | Mean lift | Positive in |
|---|---:|---:|
| security | 0.0000 | 0/5 cases |
| skill_execution | 0.0000 | 0/5 |
| skill_efficiency | +0.0222 | 1/5 |
| accuracy | −0.0133 | 0/5 |
| goal_accuracy | 0.0000 | 0/5 |
| behavior_check | **+0.0370** | 2/5 |
| **composite** | **+0.0076** | 3/5 |
| **outcome-only** | **−0.0067** | 0/5 |

This is consistent with the repo's earlier DeepSeek replication (no overall advantage) and narrows the supported claim further: on behavior-level grading, the skill's earlier rubric-level advantage (95.0 vs 85.7) **does not translate into behavior-level lift** — both arms already satisfy nearly every decision-level behavior on the frozen cases.

## What the behavior-level view adds (the one real signal)

The only measurable gains are **two specific classifications the baseline systematically misses**, both explicit decision rules in the skill's gap-audit / evidence-classification guidance:

- case-02 `mycopro-pv9`, B4 adverse/null-finding classification: Direct 0/3 vs Skill 3/3;
- case-04 `omega3-gap`, B3 substitution-whitespace classification: Direct 0/1 vs Skill 1/1.

Counter-signals: on case-02 B7 (nameplate vs qualified saleable supply) Skill missed 2/3 vs Direct 1/3; on case-03 A3 (factual consistency) the only error in all 22 outputs was a Skill output transcribing two billion as 两亿件 (200 million, factor-of-10, recommendation unchanged). Details: [behavior-review.md](behavior-review.md), [accuracy-review.md](accuracy-review.md).

## Static vs live (the paper's ρ≈0 question, reproduced)

| Pair | Spearman (n=22 outputs) |
|---|---:|
| rubric total vs behavior_check | 0.342 |
| rubric total vs composite | 0.741 |
| rubric total vs accuracy | 0.111 |

Static rubric scores predict live behavior-level outcomes only weakly (accuracy 0.111) and composite moderately (0.741, partly definitional — `skill_efficiency` is rubric-criteria coverage). This mirrors ACES's finding that scan scores are not runtime evidence, and it means the repo's 100-point rubric totals should be read as report-structure quality, not as a proxy for per-behavior performance.

## Routing probes

Trigger precision/recall 6/6 and 3/3; group routing 3/3 with no over-triggering. Details: [routing/](routing/README.md).

## What this suggests for the skill

- The skill's marginal value is **dimension-specific, not global** — concentrate claims on the classifications it demonstrably improves (demand-maturity and substitution classification, adverse-finding reporting), and stop citing rubric-total advantage as runtime evidence.
- The negative control (non-consumer boundary) passed in both arms on this probe; keep it as a regression case so the boundary rule stays executable.
- The case-03 transcription error recurred across two benchmarks — a candidate authoring fix (explicit unit/number verification step), though it did not change any decision.

## Honest limitations

- Same model family generated and reviewed (DeepSeek); not an industry-expert review.
- With-skill memos can reveal their condition through structural framing; reviewers graded content and blind names give no hint, but strict blindness is not guaranteed.
- Fresh cases run 1 trial per condition (as scoped); frozen cases carry 3 per condition; CIs are descriptive over per-case deltas (clustered, not independent).
- Synthetic facts packs; not a real-market benchmark. The two fresh cases were designed adversarially against the skill's own rules.
