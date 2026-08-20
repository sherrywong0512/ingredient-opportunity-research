# Three-case comparison protocol

## Purpose

Test whether `ingredient-opportunity-research` changes decision-process quality relative to the same model working directly from a frozen evidence pack. The benchmark is designed for regression and portfolio evidence; it is not a market-accuracy benchmark.

## Preregistration

- Protocol frozen: 2026-08-20, before generating Case 2 and Case 3 outputs.
- Case 1 reuses the earlier preregistered FermaDHA-X test and its preserved outputs.
- Case 2 and Case 3 use the evidence packs and rubrics committed in this folder before group outputs are scored.
- Every case is synthetic. Names, companies, prices, capacities, studies and regulatory excerpts are fictional test fixtures unless explicitly described as a generic category statement inside the pack.
- Both groups receive the same case prompt, frozen evidence, output limit and prohibition on browsing or adding facts.
- Group Direct uses the base model without access to this Skill or its references.
- Group Skill uses the same model family with `ingredient-opportunity-research` and only the modules applicable to the case.
- Outputs are anonymized as Memo A and Memo B before review. The group key is recorded only after the initial blind score.
- A blind reviewer scores against the case-specific rubric and reports hard failures, score, strongest behavior, most important omission and safer decision input.

## Contamination and independence disclosure

The groups run in separate Agent sessions. They share the same model family and are not statistically independent model samples. The benchmark author designed the evidence packs from known failure modes, so the benchmark is intentionally adversarial and Skill-relevant. The reviewer is another Agent from the same model family. These constraints make the result workflow evidence, not proof of general model superiority.

The anonymous outputs were committed before review, but condition mappings were not precommitted or hash-committed. Published group identity relies on the author's post-review record and cannot independently exclude reassignment.

## Cases

| Case | Decision | Primary failure modes |
|---|---|---|
| 1. FermaDHA-X | Whether to add a 1,000 t/y fermentation line | false supply-demand gap, nameplate vs saleable supply, duplicate RFQs, incomparable price |
| 2. MycoPro-PV9 | Whether to scale a mycelial-protein line for dog/cat complete food | strain and legal-route transfer, dog-to-cat extrapolation, protein-cost mismatch, unsupported health claims |
| 3. DermaBis-A95 | Whether to build a dedicated bisabolol line for China leave-on skincare | identity/stereochemistry, format fit, SKU adoption inference, opaque market size, internal cost/price veto |

## Common output task

Prepare a Chinese decision memo within the case limit that:

1. recommends one of the options stated in the evidence pack;
2. separates verified pack facts, calculations/estimates, assumptions and unknowns;
3. identifies any decision veto or blocker;
4. names the smallest evidence that would change the decision;
5. uses only the frozen pack and does not browse or add facts.

## Scoring and claims

- Hard failures take precedence over numerical scores.
- Each case uses a 100-point rubric aligned to its decision, not one generic opportunity score.
- Aggregate score is reported only as a descriptive sum and mean across these three fixtures.
- No result may be presented as factual-market accuracy, expert productivity, sales conversion, capital return or general performance across ingredients.
- If Group Direct equals or beats Group Skill, the result is retained rather than hidden.
- Any Skill repair must identify one failed behavior, make the smallest rule change, rerun the same case and preserve before/after outputs.

## Reproduction steps

1. Freeze this protocol, each evidence pack and each rubric.
2. Start separate Direct and Skill sessions.
3. Send each session the common task plus one evidence pack at a time.
4. Save raw final outputs without editorial improvement.
5. Rename outputs A/B without revealing the key to the reviewer.
6. Score with the frozen rubric.
7. Reveal the key, calculate deltas and record limitations.
8. Run repository validation and adversarial review before merging to `main`.
