# Execution log

## Frozen sequence

1. Protocol, prompts, facts-only packs and frozen rubrics were committed before generation in commit `7d83e13`.
2. Three fresh Direct sessions and three fresh Skill sessions generated the 18 outputs using the preregistered rotating order.
3. Anonymous output files were committed before review in commit `8f756f8`.
4. A blind reviewer scored response 01–06 for each case before seeing condition or run identity.
5. The mappings in [group-key.md](group-key.md) were revealed only after the initial scores were fixed.

Only anonymous headings and spacing were normalized when the raw responses were saved; substantive wording was not edited.

## Execution matrix

| Condition | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Direct | Case 1 → 2 → 3 | Case 2 → 3 → 1 | Case 3 → 1 → 2 |
| Skill | Case 1 → 2 → 3 | Case 2 → 3 → 1 | Case 3 → 1 → 2 |

## Reproducibility limits

- Sessions were fresh but used the same available model family. Exact serving model identifiers and sampling seeds were not recorded.
- Each session handled three cases, so within-session cross-case context cannot be excluded.
- The reviewer used the same model family and is not a human domain expert.
- The cases and rubrics are synthetic and built around known Skill failure modes.
- No condition/run mapping or salted hash was committed before review. The group key is an author-recorded post-review disclosure, not independently verifiable proof that reassignment did not occur.
- The exact word-for-word harness instruction was not saved. The protocol records its substantive constraints, but that summary is not a verbatim generation record.
