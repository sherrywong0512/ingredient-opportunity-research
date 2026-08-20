# Run log

## Sequence and immutable checkpoints

| Step | Date | Evidence |
|---|---|---|
| Case 1 preregistration, outputs and review | 2026-08-19 | `evaluation/controlled-test/` and earlier Git history |
| Three-case protocol, Case 2/3 packs and rubrics frozen | 2026-08-20 | commit `9b524d0` |
| Anonymous Case 2/3 raw outputs committed before scoring | 2026-08-20 | commit `1165db3` |
| Blind scores and group keys recorded | 2026-08-20 | this comparison update |

## Group execution

### Direct/no-Skill group

- Separate Agent session.
- Instructed not to read any Skill, references, rubric, existing output, review, README or PRD.
- Read only the frozen Case 2 and Case 3 evidence packs.
- No browsing and no added facts.
- The first response omitted Case 3, so Case 3 was requested in a follow-up turn in the same Direct session. This is disclosed as a procedural deviation; no evidence, rubric or competing output was supplied in the follow-up.

### Skill group

- Separate Agent session from Direct.
- Required to use `ingredient-opportunity-research` and applicable references.
- Instructed not to read rubrics, existing outputs, blind reviews, README or PRD.
- Read only the frozen evidence packs in addition to the Skill.
- No browsing and no added facts.

### Blind reviewer

- Separate Agent session from the generation groups.
- Read only each case's frozen evidence pack, rubric and anonymous memos.
- Was explicitly instructed not to read group keys, Skill, references, protocol, README, PRD or Git history.
- Group mapping was revealed only after the initial scores were returned.

## Output preservation

The returned final memos were preserved without substantive editing. Only anonymous file headings and Markdown spacing were normalized. Case 2 deliberately maps Skill to A and Direct to B; Case 3 reverses the order to reduce trivial label guessing.

## Known limitations

- Exact serving model identifiers and sampling seeds were not recorded; sessions used the same model family.
- Each group handled Case 2 and Case 3 sequentially, so within-group cross-case context is possible and symmetric.
- The benchmark author selected cases from known Skill failure modes.
- The reviewer belongs to the same model family and is not a human domain expert.
- Synthetic packs test workflow behavior, not factual retrieval accuracy or real-market prediction.
- One run per condition does not estimate variance.
