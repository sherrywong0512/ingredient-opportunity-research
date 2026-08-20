# Minimal-prompt repeated benchmark protocol

## Product claim under test

Can a user give one simple opportunity-investment sentence and rely on `ingredient-opportunity-research` to apply a more complete and stable chemical/synthetic-biology decision framework than the same model working directly?

This phase is the primary test of prompt simplicity and stability. The earlier [three-case comparison](../three-case-comparison/README.md) remains a structured-prompt calibration and must not be substituted for this result.

## Preregistration

- Frozen before any minimal-prompt output is generated.
- Three synthetic facts-only packs reuse the factual content of the earlier cases but remove the explicit requested report structure, output categories and warnings.
- Each case has one user sentence stored in [prompts.md](prompts.md).
- A harness-only constraint gives both groups the same maximum of 1,200 Chinese characters per memo, forbids browsing and added facts, and asks for raw final output only. It does not prescribe a decision framework.
- Direct receives only the one-sentence prompt and facts-only pack.
- Skill receives the same prompt and facts-only pack plus `ingredient-opportunity-research` and applicable references.
- Each condition is run in three separate Agent sessions. Every session handles all three cases; case order rotates across runs to reduce a fixed order effect.
- Per-case outputs are anonymized and shuffled before review. Group identity and run number are stored only after initial blind scores.
- The same frozen case rubrics score all outputs. Reviewers do not reward confident tone or length.

## Run matrix

| Run | Direct order | Skill order |
|---|---|---|
| 1 | Case 1 → Case 2 → Case 3 | Case 1 → Case 2 → Case 3 |
| 2 | Case 2 → Case 3 → Case 1 | Case 2 → Case 3 → Case 1 |
| 3 | Case 3 → Case 1 → Case 2 | Case 3 → Case 1 → Case 2 |

## Metrics

For each case and condition report:

- three raw scores and hard failures;
- mean, median, minimum, maximum, range and population standard deviation;
- which decision dimensions are repeatedly omitted;
- whether the headline recommendation changes across repeats.

Across all cases report the descriptive mean, minimum, maximum, score range and hard-failure count. Do not run or imply statistical significance from three repeats.

## Preregistered interpretation gates

- **Simple-prompt Skill completeness supported:** all nine Skill outputs score at least 85/100 and have no hard failure.
- **Skill quality advantage supported in this fixture set:** Skill mean is higher than Direct in at least two of three cases and Skill has no unique hard failure.
- **Direct instability relative to Skill supported in this fixture set:** Direct has a larger within-case score range and population standard deviation in at least two of three cases. If this is not met, do not call Direct less stable.
- **Industry-framework gap supported:** blind review identifies at least one decision dimension repeatedly omitted by Direct more often than Skill across the three runs.
- Equality, Direct wins and null findings must be retained.

These gates support only descriptive claims about this synthetic, adversarial fixture set. They do not prove recognition by the chemical industry, synthetic-biology experts, or real companies. That requires human-expert validation.

## Independence and limitations

- Separate runs are fresh Agent sessions but use the same model family; exact serving version and seed may not be exposed.
- Each run handles three cases sequentially, so cross-case context may exist inside a run; rotating case order reduces but does not remove it.
- Facts and rubrics were designed from known Skill failure modes, so the benchmark is Skill-relevant rather than neutral.
- A model-family reviewer is not a chemical-industry expert.
- Repetition measures output variation under these sessions, not full production variance.
- The anonymous outputs were committed before scoring, but the condition/run mapping was not precommitted or hash-committed. The published mapping therefore relies on the author's post-review record and cannot independently exclude reassignment after scoring. A future run must commit a salted mapping hash before review and reveal the salt afterward.
- The one-sentence user prompts and facts packs are frozen, but the exact word-for-word harness instruction, serving model version and sampling parameters were not recorded. The statistics are reproducible from saved outputs; generation is not independently reproducible. Future runs must freeze those fields before execution.
