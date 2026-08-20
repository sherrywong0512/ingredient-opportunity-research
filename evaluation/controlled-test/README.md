# Controlled test: FermaDHA-X capacity decision

## Why this test exists

The latest Skill revision added stricter supply-demand gap and capacity-decision rules. This test checks whether those rules change behavior under a frozen, deliberately conflicting evidence pack.

## Protocol

- Date: 2026-08-19
- Input: the same [frozen evidence pack](evidence-pack.md)
- Constraints: no browsing, no outside facts, same output limit
- Groups: one fresh session with the Skill and one fresh session without any Skill
- Review: a third fresh session scored anonymous memos using a prewritten [rubric](review-rubric.md)
- Primary safety outcome: no false numerical gap, no promotion of intake deficit/RFQs into committed demand, no expansion recommendation before regulation/technical/commercial qualification

The reviewer saw `memo-a` and `memo-b`, not the group labels. Labels were revealed only after the first review.

## Results

| Output | Condition | Score | Hard failure | Main observation |
|---|---|---:|---|---|
| [Memo A](memo-a.md) | No Skill | 96/100 | none | Safe conclusion; price mismatch and economic trigger were less operationalized |
| [Memo B](memo-b.md) | Skill before repair | 99/100 | none | More explicit demand/supply state and capacity trigger; price mismatch fields remained implicit |
| [Memo C](memo-c.md) | Skill after one-rule repair | 100/100 | none | Explicitly named price-basis mismatches and required a normalized RFQ plus contribution-economics gate |

The full anonymous judgments are preserved in [blind review](blind-review.md).

## What the test changed

The first review found that Memo B said prices were incomparable but did not name the decisive mismatches. The smallest repair added one instruction to `references/price-research.md`: when price affects a commercial or capital decision, name the mismatched active basis, quantity, date, currency, tax, freight/Incoterms, payment terms and supplier type, then state the smallest normalized evidence needed.

The same Skill group reran the same frozen task. In the second blind comparison, Memo C improved from 99 to 100 on the preregistered rubric. The improvement was limited to price auditability; the capital conclusion did not change. The rule was therefore retained.

## What this proves—and what it does not

Supported in this bounded test:

- both the base model and Skill avoided the four hard failures;
- the Skill output was 3 points higher on one synthetic scenario;
- the targeted repair produced a further 1-point improvement under the same input and rubric;
- the fix improved explicitness, not the headline decision.

Not supported:

- that the Skill is generally 3 points better across models, ingredients or tasks;
- that the rubric or reviewer is independent of the model family;
- that the synthetic scenario represents real buyer behavior;
- that the Skill improves factual accuracy, expert time, sales conversion or capital returns.

This test was intentionally shaped around known failure modes, so it is a regression and workflow test, not an unbiased market benchmark. A stronger next test requires multiple real evidence packs, a human expert baseline, blinded reviewers and time/edit-distance measures.
