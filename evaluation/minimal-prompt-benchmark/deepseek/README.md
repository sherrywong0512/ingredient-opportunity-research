# DeepSeek cross-model follow-up run

> **What this is:** a replication of the [one-sentence minimal-prompt benchmark](../README.md) on a second model family — DeepSeek (`deepseek-v4-flash`, executed inside DeepSeek Harness) — using the same three frozen synthetic cases, the same frozen facts-only packs, the same exact one-sentence prompts, and the same frozen rubrics. It extends the original single-model result toward a cross-model claim.
>
> **Status:** results below; conditions were revealed to the author only after an independent blind reviewer scored the anonymized outputs.

## Method (replicates the preregistered protocol)

- Same three synthetic facts-only packs and same one-sentence prompts as the original run (frozen files reused verbatim).
- Same harness constraint: each memo ≤ 1,200 Chinese characters, no browsing, no added facts, raw final output only, no prescribed framework.
- Three fresh DeepSeek sessions per condition (Direct and Skill), six sessions total; each session handled all three cases in the same rotating order as the original protocol (run 1: 1→2→3, run 2: 2→3→1, run 3: 3→1→2).
- Direct sessions received only the one-sentence prompt and the facts-only pack. Skill sessions additionally read and followed `skill/ingredient-opportunity-research/` (SKILL.md + applicable references) before writing.
- Outputs were anonymized (renamed to response-01..06 per case, condition labels removed) before review.
- A fresh blind reviewer (a different session, told nothing about conditions) scored all 18 memos against the frozen rubrics, recording per-criterion scores, hard failures and headline recommendations.
- The condition/run mapping was recorded only after the reviewer returned its scores; see [group-key.md](group-key.md).

## Results

Scores in [scores.csv](scores.csv); per-criterion review in [blind-review.md](blind-review.md); condition mapping revealed after scoring in [group-key.md](group-key.md).

| Case | Direct scores | Direct mean / range / SD | Skill scores | Skill mean / range / SD |
|---|---|---:|---|---:|
| FermaDHA-X | 100 / 100 / 100 | 100.0 / 0 / 0.0 | 100 / 100 / 100 | 100.0 / 0 / 0.0 |
| MycoPro-PV9 | 92 / 92 / 92 | 92.0 / 0 / 0.0 | 100 / 92 / 92 | 94.7 / 8 / 3.8 |
| DermaBis-A95 | 100 / 93 / 100 | 97.7 / 7 / 3.3 | 100 / 100 / 87 | 95.7 / 13 / 6.1 |
| **All nine outputs** | — | **96.6 mean; 92 min; 8 range; 3.9 SD** | — | **96.8 mean; 87 min; 13 range; 4.8 SD** |

No output had a hard failure, and all 18 made a safe headline decision (0 recommended building; 15 "do not build"; 3 "conditional — do not build yet"). The blind reviewer was a separate session that never saw condition labels.

### Preregistered gates on DeepSeek — NOT met for a Skill advantage

Applying the original protocol's preregistered interpretation gates to this run:

| Gate | On DeepSeek |
|---|---|
| All nine Skill outputs ≥ 85, no hard failure | **Met** (min 87; 0 hard failures) |
| Skill mean higher in ≥ 2 of 3 cases | **Not met** (higher only on MycoPro-PV9; tied FermaDHA-X; Direct higher on DermaBis-A95) |
| Direct has larger within-case range and SD in ≥ 2 of 3 cases | **Not met** (Direct was more stable: overall range 8 vs 13, SD 3.9 vs 4.8) |
| At least one decision dimension omitted by Direct more often than Skill | **Partially met** (MycoPro-PV9 capacity-vs-saleable-output separation: omitted by 3/3 Direct vs 2/3 Skill; the only full handling was a Skill output) |

### Honest cross-model reading

- The original run's headline advantage (Skill 95.0 vs Direct 85.7 on the original model family) **did not reproduce on DeepSeek as an overall mean** (96.8 vs 96.6 — essentially tied, with Direct more stable overall).
- The skill's measured benefit on DeepSeek is **dimension-specific, not global**: it led on MycoPro-PV9 (capacity/qualification separation, the most decision-critical omission there) while Direct led on DermaBis-A95 (format-evidence recording).
- Both conditions produced high-quality, decision-safe memos on these three facts packs; the skill's framework added most where direct generation was weakest, and least where direct generation was already strong.
- Interpretation: the skill's value appears **model-dependent**. The strongest supported claim across both runs is narrow: the skill improves coverage of specific decision dimensions and repeatability on the original family; on DeepSeek its overall effect is a null-to-mixed result with one dimension-specific gain. The benchmark does not prove a universal advantage.

## What this adds to the original run

- The original benchmark used one model family (same family for generation and blind review). This run adds a second model family, so any directional pattern that reproduces across both families is stronger evidence of framework-level (rather than model-idiosyncratic) behavior.
- This run improved one protocol weakness of the original: the reviewer was a genuinely separate session that never saw condition labels (the original disclosed that its mapping was author-recorded after scoring). The remaining limitations are unchanged.

## Limitations (unchanged or specific to this run)

- The fixtures are synthetic, Skill-relevant, and were designed from known Skill failure modes; they are not a neutral market benchmark.
- The reviewer is the same model family as the generators (DeepSeek reviewed DeepSeek) and is not a chemical-industry expert.
- Exact serving versions and sampling seeds were not exposed; output generation is not independently reproducible.
- Each session handled three cases sequentially, so within-session cross-case context cannot be excluded.
- Scores are descriptive statistics over three repeats; no statistical significance is claimed.
- This run does not measure factual retrieval, real-market accuracy, time savings or business outcomes.
- The claim remains narrow: framework coverage and repeatability, not headline-decision correctness.

## Evidence trail

- Raw anonymized outputs: [blind/](blind/)
- [Blind review](blind-review.md)
- [Post-review group key](group-key.md)
- [Machine-readable scores](scores.csv)
- [Execution log](run-log.md)
- Generator session constraints and prompts: same files as the original run ([protocol.md](../protocol.md), [prompts.md](../prompts.md))
