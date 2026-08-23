# Execution log — DeepSeek cross-model run

## Frozen sequence

1. The original protocol, one-sentence prompts, facts-only packs and frozen rubrics were reused verbatim from the initial run (they were committed earlier in this repository).
2. Six fresh DeepSeek sessions (three Direct, three Skill) generated the 18 memos using the same rotating order as the original run; each memo was limited to ≤1,200 Chinese characters, used only its facts-only pack, and did not browse.
3. Outputs were anonymized (condition labels removed, renamed response-01..06 per case) before review; the condition/run mapping was held outside the repository.
4. A fresh blind reviewer session (never shown the condition labels) scored all 18 memos against the frozen rubrics.
5. The mapping in [group-key.md](group-key.md) was written only after the reviewer's scores were returned.

Only heading normalization was applied when saving anonymized copies; substantive wording was not edited.

## Execution matrix

| Condition | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Direct | Case 1 → 2 → 3 | Case 2 → 3 → 1 | Case 3 → 1 → 2 |
| Skill | Case 1 → 2 → 3 | Case 2 → 3 → 1 | Case 3 → 1 → 2 |

## Generation environment

- Model family: DeepSeek (`deepseek-v4-flash`), executed as fresh sessions inside DeepSeek Harness (this session's own runtime).
- Skill-condition sessions read `skill/ingredient-opportunity-research/` (SKILL.md and applicable references) before writing; Direct-condition sessions received only the prompt and facts pack.
- Exact serving version and sampling seeds were not exposed.

## Reproducibility limits

- Sessions were fresh but within one model family; the blind reviewer was also the same model family and is not a human domain expert.
- Each session handled three cases, so within-session cross-case context cannot be excluded.
- The reviewer never saw condition labels (an improvement over the original run's author-recorded mapping), but the mapping is still an author record rather than a salted hash commitment.
- The exact word-for-word session instructions are summarized here, not recorded verbatim.
