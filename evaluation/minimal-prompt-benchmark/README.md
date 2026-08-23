# One-sentence repeated benchmark

## Executive result

The user supplied only one simple decision sentence, for example:

> 请评估 DermaBis-A95 是否值得建设中国护肤原料专线，并给出依据和下一步。

Across three preregistered synthetic cases and three fresh sessions per condition, the Skill produced a more complete and stable decision framework than the same model working directly from the facts-only pack.

| Case | Direct scores | Direct mean / range / SD | Skill scores | Skill mean / range / SD |
|---|---|---:|---|---:|
| FermaDHA-X | 91 / 100 / 94 | 95.0 / 9 / 3.7 | 100 / 100 / 100 | 100.0 / 0 / 0.0 |
| MycoPro-PV9 | 93 / 93 / 81 | 89.0 / 12 / 5.7 | 87 / 95 / 91 | 91.0 / 8 / 3.3 |
| DermaBis-A95 | 81 / 78 / 60 | 73.0 / 21 / 9.3 | 91 / 99 / 92 | 94.0 / 8 / 3.6 |
| **All nine outputs** | — | **85.7 mean; 60 min; 40 range; 11.4 SD** | — | **95.0 mean; 87 min; 13 range; 4.7 SD** |

No output had a hard failure, and all 18 made the same safe headline decision. All preregistered descriptive gates were met in this fixture set:

- all nine Skill outputs scored at least 87/100;
- Skill mean was higher in all three cases;
- Direct had a larger within-case range and population standard deviation in all three cases;
- Direct repeatedly omitted more industry-relevant decision dimensions, most clearly SKU adoption and market-size disposition in DermaBis-A95.

## What this demonstrates

Supported portfolio claim:

> In three preregistered synthetic cases with three fresh sessions per condition, a one-sentence input produced nine Skill outputs scoring at least 87 with no hard failures. Skill averaged 95.0 versus Direct at 85.7, and Direct had a larger within-case range and population standard deviation in all three cases. The observed advantage was framework coverage and stability, not a different headline decision.

The result supports a product design claim: users need not know the full chemical/synthetic-biology research checklist to request an initial assessment; the Skill carries that workflow. It does **not** prove that the framework is recognized by industry or that Direct models are generally unstable.

## Counter-evidence and limits

- Direct was already strong on FermaDHA-X and matched two perfect Skill outputs.
- On MycoPro-PV9, Skill omitted qualified-saleable-capacity conversion in two of three outputs, while Direct omitted it in one.
- One Skill output transcribed two billion units as 200 million, although it rejected the estimate and did not change the recommendation.
- The fixtures are synthetic, Skill-relevant and use one model family; exact versions and seeds were unavailable.
- The blind reviewer was not a chemical-industry expert. Human expert review is required before claiming “industry-recognized.”
- The condition/run mapping was not precommitted or hash-committed before scoring. Group assignment relies on the author's post-review record, so the comparison is not independently auditable against reassignment.
- Exact model versions, sampling parameters and the word-for-word harness instruction were not preserved. Saved-output scoring is reproducible; output generation is not.
- This benchmark does not measure factual retrieval, real market accuracy, time savings or business outcomes.

## Cross-model follow-up: DeepSeek

A replication of this protocol on a second model family — DeepSeek (`deepseek-v4-flash`, via DeepSeek Harness), same frozen facts packs, same one-sentence prompts, same rotating order, same frozen rubrics, six fresh sessions (three per condition), anonymized outputs, and a separate blind-reviewer session that never saw condition labels: [deepseek/](deepseek/README.md).

**Result: the Skill's overall advantage did not reproduce on DeepSeek** — Direct 96.6 (range 8, SD 3.9) vs Skill 96.8 (range 13, SD 4.8) across nine outputs each; 0 hard failures; 18/18 safe headline. Per case: tied on FermaDHA-X (100 vs 100), Skill-led on MycoPro-PV9 (94.7 vs 92.0, the only full capacity-conversion handling was a Skill output), Direct-led on DermaBis-A95 (97.7 vs 95.7). Two of the four preregistered gates (Skill mean higher; Direct less stable) were not met on DeepSeek.

Reading: the skill's measured benefit is **model-dependent** — largest where direct generation is weakest, near zero where direct generation is already strong. This null-to-mixed replication is retained deliberately and narrows the supported claim: framework-coverage gains on specific decision dimensions, not a universal advantage.

## Evidence trail

- [Preregistered protocol](protocol.md)
- [Exact one-sentence prompts](prompts.md)
- Frozen rubrics: [FermaDHA-X](../controlled-test/review-rubric.md), [MycoPro-PV9](../three-case-comparison/case-02-mycopro-pv9/rubric.md), [DermaBis-A95](../three-case-comparison/case-03-dermabis-a95/rubric.md)
- [Blind review](blind-review.md)
- [Post-review group key](group-key.md)
- [Machine-readable scores](scores.csv)
- [Execution log](run-log.md)

Run `python3 scripts/analyze_minimal_benchmark.py` to reproduce the descriptive statistics.
