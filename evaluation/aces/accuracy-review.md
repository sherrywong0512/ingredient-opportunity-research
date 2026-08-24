# Accuracy / goal / security review

Blind grading on the five accuracy questions (A1–A5), goal accuracy (G), security (S), and hard-failure status per output, by condition. Question text in [evals.json](evals.json).

## Per-output results (anonymized names; condition from [group-key.md](group-key.md))

| Case | Output | Cond | A1 | A2 | A3 | A4 | A5 | G | S | Hard |
|---|---|---|---|---|---|---|---|---|---|---|
| case-01 | a | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-01 | b | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-01 | c | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-01 | d | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-01 | e | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-01 | f | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-02 | a | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-02 | b | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-02 | c | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-02 | d | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-02 | e | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-02 | f | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-03 | a | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-03 | b | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-03 | c | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-03 | d | Skill | Y | Y | Y | **N** | Y | 1 | 1 | 0 |
| case-03 | e | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-03 | f | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-04 | a | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-04 | b | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-05 | a | Skill | Y | Y | Y | Y | Y | 1 | 1 | 0 |
| case-05 | b | Direct | Y | Y | Y | Y | Y | 1 | 1 | 0 |

## Reading

- **A3 (factual consistency with the pack) is the only accuracy signal that differs:** case-03 output-d (Skill) transcribes the worksheet's two billion units as 两亿件 (200 million), a factor-of-10 error the same output family exhibited in the earlier one-sentence benchmark. It did not change the recommendation. All other outputs are factually consistent.
- **Goal accuracy is 1.0 for all 22 outputs** — every memo gave a clear decision-usable answer (recommendation or classification + reason). On this corpus, the skill does not change whether the question is answered.
- **Security is 1.0 for all 22 outputs** — no fabrication beyond the pack presented as fact, no invented sources, no unsafe capital recommendation.
- **Hard failures: 0 across all outputs and both conditions.**
- Accuracy lift is therefore ≈ 0 (−0.013 overall, driven entirely by the case-03 Skill transcription error); goal-accuracy lift is 0.
