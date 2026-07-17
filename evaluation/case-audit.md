# Case quality audit

> Audit date: 2026-07-17. This evaluates research quality, not market opportunity. Scores follow `skill/ingredient-opportunity-research/references/test-scenarios.md`; hard-gate caps are applied before interpreting totals.

## Summary

| Case | Raw rubric result | Applied cap | Published quality result | Decision-readiness blocker |
|---|---:|---:|---:|---|
| Isomalt — China bakery | 79 | 75 | **75/100** | no reproducible current-SKU/label coverage; US legal route unresolved |
| Gellan gum — consumer products | 63 | 50 | **50/100** | target-market China regulation was not extracted to exact product-category/use rows |
| HMO — global market | 61 | 50 | **50/100** | China molecule × source × use regulation and industrial price evidence remain incomplete |

Interpretation: the isomalt report is suitable for project screening with stated gaps. The gellan gum and HMO reports are directional examples, not commercial decision inputs.

## Rubric breakdown

| Dimension | Weight | Isomalt | Gellan gum | HMO |
|---|---:|---:|---:|---:|
| Identity and specification accuracy | 8 | 8 | 8 | 8 |
| Property/original-literature evidence and adverse findings | 12 | 9 | 8 | 8 |
| Property → need → application trace and hard gates | 12 | 10 | 9 | 8 |
| China–US–EU regulation and claim boundaries | 12 | 9 | 5 | 5 |
| Formulation, process, use amount, storage and failure modes | 12 | 10 | 9 | 7 |
| Company/SKU adoption and customer coverage audit | 14 | 6 | 5 | 7 |
| Technical/human/claim/consumer/commercial separation | 12 | 10 | 7 | 8 |
| Comparable price, use amount and use cost | 10 | 9 | 5 | 2 |
| Executable validation and customer actions | 8 | 8 | 7 | 8 |
| **Raw total** | **100** | **79** | **63** | **61** |

## Hard-gate review

| Gate | Isomalt | Gellan gum | HMO |
|---|---|---|---|
| Exact identity | met | met; HA/LA distinction retained | met; family members separated |
| Core target-market regulation | conditional; China verified, US unresolved | **not met**; China exact category/use rows absent | **not met**; China molecule/source/use matrix absent |
| Application has property trace or hypothesis label | met | met/conditional | met/conditional |
| Company use requires product evidence | met in wording; coverage not reproducible | conditional | conditional |
| Claims separated from efficacy | met | met | met |
| Foreseeable adverse-effect search | met | conditional; primarily formulation failure modes | conditional; tolerance separated but original-study coverage incomplete |
| Consumer-facing education dependency | not decision-critical; appropriately brief | consumer ingredient education not required | applied and decision-relevant |
| Professional terminology | met | met; terminology table justified by HA/LA ambiguity | met; terminology table justified by molecular family |

## What changed in the latest workflow

The current skill is stricter than parts of the example set. It now requires:

- a category-specific joint China–US–EU regulatory table;
- inline, row-level property evidence with reading depth and transferability;
- current SKU-level label coverage before declaring adoption or non-use;
- separate technical, human/adverse, claim, consumer, and commercial effect channels;
- application cases with the original use-amount denominator;
- incumbent-versus-target ingredient-system cost and, when supportable, total ingredient-cost change;
- a rule-by-rule completeness check rather than an opaque opportunity score.

## Upgrade backlog

### Isomalt

1. Define the ten-account SKU universe and record labels checked, inaccessible labels, platforms, dates, and exact ingredient/substitute wording.
2. Add the complete rule-based checklist required by `research-quality-rules.md`.
3. Resolve the US legal basis for the exact supplier product before any US recommendation.
4. Replace illustrative non-sweetener component prices with matched current inputs if total ingredient-cost percentage will drive a decision.

### Gellan gum

1. Extract exact GB 2760-2024 and EU Annex II rows for each shortlisted beverage/dessert category.
2. Add row-level citations, methods, reading depth, source locator, and transferability to the property table.
3. Audit current labels for every P1/P2 account and preserve complete substitute systems.
4. Compare gellan systems with MCC/CMC/carrageenan on matched functional performance and full system cost.

### HMO

1. Build the supplier-specific `molecule × production source/strain × use × dose × population × jurisdiction` matrix.
2. Obtain matched industrial RFQs; research-reagent prices must remain excluded.
3. Rebuild the ten-account table around current regional SKU labels and supplier authorization fit.
4. Retrieve original full-text clinical evidence for decision-critical tolerance and outcome statements.

## Portfolio interpretation

The strongest project evidence is not that every report is complete. It is that the workflow makes incompleteness auditable, prevents unsupported sales conclusions, and converts each blocker into a specific research, experiment, RFQ, label-audit, or customer-validation action.
