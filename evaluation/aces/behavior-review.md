# Behavior-level review (behavior_check)

Blind per-`expected_behavior` YES/NO grading of all 22 outputs, by condition. Behaviors are listed in [evals.json](evals.json) per case. Pass rate = fraction of behaviors graded YES.

## Per-case behavior pass rates by condition

| Case | Behavior | Direct pass | Skill pass | Lift |
|---|---|---|---|---|
| case-01 fermadhax | all 9 behaviors (B1–B9) | 9/9 (3/3 outputs) | 9/9 (3/3) | 0.000 |
| case-02 mycopro-pv9 | B1–B9 | — | — | — |
| — | B1 identity/transfer limits | 3/3 | 3/3 | 0 |
| — | B2 dog-vs-cat separation | 3/3 | 3/3 | 0 |
| — | B3 legal-route separation | 3/3 | 3/3 | 0 |
| — | **B4 adverse/null findings classified** | **0/3** | **3/3** | **+0.333** |
| — | B5 no market-value→demand conversion | 3/3 | 3/3 | 0 |
| — | B6 digestible-protein economics | 3/3 | 3/3 | 0 |
| — | **B7 nameplate vs qualified saleable supply** | **2/3** | **1/3** | **−0.333** |
| — | B8 evidence-consistent recommendation | 3/3 | 3/3 | 0 |
| — | B9 smallest validation w/ controls | 3/3 | 3/3 | 0 |
| case-03 dermabis-a95 | all 9 behaviors | 9/9 | 9/9 | 0.000 |
| case-04 omega3-gap | B1–B9 | — | — | — |
| — | B1 identity/spec/route split | 1/1 | 1/1 | 0 |
| — | B2 intake deficit = latent need | 1/1 | 1/1 | 0 |
| — | **B3 substitution whitespace classified** | **0/1** | **1/1** | **+1.000** |
| — | B4 no one-producer market inference | 1/1 | 1/1 | 0 |
| — | B5 no unmatched subtraction | 1/1 | 1/1 | 0 |
| — | B6 RFQs = stated interest, dedup | 1/1 | 1/1 | 0 |
| — | B7 committed gap only from aligned orders | 1/1 | 1/1 | 0 |
| — | B8 supply measures separated, no double count | 1/1 | 1/1 | 0 |
| — | B9 not reliably estimable where unaligned | 1/1 | 1/1 | 0 |
| case-05 industrial-boundary | all 6 behaviors | 6/6 | 6/6 | 0.000 |

## Reading

- On the three frozen cases both arms pass nearly every behavior; the skill's earlier rubric-level advantage (95.0 vs 85.7) does **not** translate into behavior-level advantage there. The rubric rewards report structure that the baseline lacks; the binary behaviors are coarser decision-level checks both arms already satisfy.
- The only real behavior-level gains are **two specific classifications the baseline systematically misses**: adverse/null-finding classification (case-02, Direct 0/3 vs Skill 3/3) and substitution-whitespace classification (case-04, Direct 0/1 vs Skill 1/1). Both are explicit decision rules in the skill's `market-size-and-demand.md` / gap-audit guidance — this is the narrow, evidence-backed case for the skill.
- On case-04 the Direct output also produced a labeled "13,000 t/y optimistic upper bound" that mixes mixed-concentration/period RFQs with 50%-concentrate qualified supply — a false-precision figure the case's hard-failure clause targets (its headline aligned 4,000 t/y committed gap stayed correct). The Skill output returned the market-level total as `not reliably estimable` and listed every prohibited subtraction.
- The skill is not uniformly better even where it leads: on case-02 B7 (nameplate vs qualified saleable supply) the Skill arm missed 2/3 while Direct missed 1/3.

Review sheets: [R1 record](../minimal-prompt-benchmark/README.md) style, per-output grades assembled in [scores.csv](scores.csv); raw reviewer lines in the run log's review step ([run-log.md](run-log.md)).
