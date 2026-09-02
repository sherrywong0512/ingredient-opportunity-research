# Feasibility Report Template

Use this as the default Markdown deliverable. Match the user's language and shorten sections that lack decision value.

## Formatting and source-placement conventions

These conventions keep every report and every example structurally consistent. Apply them before delivery; `scripts/validate_report.py` checks the machine-verifiable parts.

- **Section headings:** numbered Arabic headings, `## 1.`, `## 2.`, … in the order below; the executive conclusion is always section 1. Do not use Chinese numerals or unnumbered headings for top-level sections.
- **Inline citations:** every material claim in a table carries its source inside the same row (an `Exact source and locator` column, a URL/DOI, or a directly attached `来源：` line under the table). The trailing `## Sources` section is a consolidated bibliography only; it is never the sole citation for a material claim.
- **Synthesis rows:** when a row synthesizes multiple studies (e.g., a mechanism summary), state it explicitly — `综合多源，见 Sources：<entry>` — instead of leaving the row uncited or inventing a single source.
- **Lists and emphasis:** use `- ` for bullet lists; lead conclusions with a bold label such as `**结论：**` / `**Conclusion:**`; keep one bullet level per list; do not mix indentation styles.
- **Conclusion presentation:** Section 1 opens with one bold, decision-relevant verdict sentence, then rationale as plain text or bullets. Verdict labels stay consistent (`**结论：**` / `**Conclusion:**`).
- **Evidence markers:** every material claim shows its evidence level (E1–E5 or the 已验证/推断/待验证 equivalents) and observation/source date.
- **Terminology table:** only when identity, regulation, evidence transfer, or the decision depends on ambiguous naming; otherwise one identity statement at the start.

```markdown
# [Ingredient] Downstream Market Feasibility — [Geography / Date]

## 1. Executive conclusion
- What the evidence currently supports
- Most plausible downstream applications and why
- Main constraints or reasons not to proceed
- Decisions that require supplier or industry-expert judgment

## 2. Scope and assumptions
| Item | Definition |
|---|---|
| Ingredient identity | Preferred local name, English name/abbreviation, exact grade/source, and easily confused substance to exclude |
| Geography and product classes | |
| Time window | |
| Supplier saleable grade/scale/authorized markets/evidence package | |
| Data coverage and exclusions | |

## 3. Ingredient properties and evidence
| Property/value or risk | Ingredient identity/grade | Test matrix, dose and conditions | Comparator/method | Measured result | Exact source and locator | Reading depth | Transferability | Limitation | Evidence level |
|---|---|---|---|---|---|---|---|---|---|

Keep this table limited to measured ingredient properties and risks. Put finished-product replacement percentages, application performance, competitor comparison, sensory acceptance, and formulation strategy in Section 5.

### Property conclusion
- Supported properties
- Mechanistic or adjacent evidence
- Unsupported marketing claims
- Adverse properties and failure modes

## 4. Property-to-application map and hard-gate results
| Supported property and source | Product problem | Required function | Application | Need evidence | China regulatory gate | United States regulatory gate | European Union regulatory gate | Technical gate | Use amount and basis | Use cost and basis | Buyers | Overall result | Decisive evidence/gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### China–United States–European Union food regulatory table

For food ingredients, insert one concise comparison table from `regulatory-audit.md`. Use one row per jurisdiction-and-category combination so different use levels or conditions remain visible. Show the legal route, relevant category, use level and original unit/basis, restrictions or warnings, supplier applicability when relevant, application conclusion, official source, and unresolved gap.

## 5. Shortlisted application deep dives
### [Application]
- Trace: supported property -> product need -> application
- Demand and consumer problem
- Representative products, brands, formats and price signals
- Ingredient role, substitutes and switching barriers
- Buyer value in use and economic assumptions
- Science/technical evidence and limitations
- Regulatory/claim boundaries
- Evidence supporting entry
- Evidence or event that would invalidate the hypothesis

### Application cases and reported use amounts

| Application/matrix | Case/source | Evidence type | Ingredient identity/grade | Functional role | Formulation and amount basis | Reported use amount/original unit | Normalized amount/assumptions | Process/conditions | Control/benchmark | Measured outcome | Commercial-status evidence | Transferability | Exact source/locator | Limitation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Label each amount as a reported case amount, observed span, source-supported common/typical amount, proposed test amount, or confirmed commercial amount. Do not infer undisclosed amounts from label order or product claims.

### Same-application ingredient alternatives

| Application/matrix | Required function and benchmark | Target ingredient/grade | Incumbent or alternative | Why relevant | Target advantage/evidence | Alternative advantage/evidence | Trade-off/failure condition | Use-amount basis | Incumbent system cost | Target system cost | System-cost change | Estimated total ingredient cost before/after | Total ingredient-cost change | Transferability | Label/regulatory implication | Conclusion/gap |
|---|---|---|---|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|

Compare on a functionally equivalent basis. If the evidence is not like-for-like, label the comparison directional and specify the controlled benchmark needed. Calculate the replaced ingredient-system cost before and after. When the full formulation and comparable prices are supportable, also estimate total ingredient cost before and after and show the absolute and percentage change. Do not call ingredient cost total production cost.

### Replacement, partial-replacement and co-formulation options

| Application/matrix | Incumbent product jobs | Target-ingredient jobs | Uncovered jobs | Strategy | Partner/incumbent retained | Total amount basis | Component amounts/ratio | Process conditions | Comparator design | Measured outcome | Synergy evidence status | Exact source/locator | Transferability | Regulatory/label/cost implication | Risk | Validation action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Treat literature formulations as reference options, not production recipes. Use `synergy` only when the evidence demonstrates interaction beyond an appropriate additive or mixture benchmark.

### Market awareness and education, only when decision-relevant

Include a brief conclusion or the full table from `market-awareness-and-education.md` only when ingredient recognition, benefit explanation, trust, claim comprehension, or education effort could materially change this application's positioning, channel, launch cost, or customer decision. Otherwise omit it; novelty alone is not sufficient.

### Product-format screen

| Application | Concrete product format | Product need | Ingredient job | Matrix/phase and process fit | Contact/consumption pattern | Evidence/use amount | Regulatory/claim gate | Alternatives | Current SKU adoption | Format market evidence | Buyers | Result/gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Keep the finished-product format market, ingredient-addressable output, ingredient demand and supplier-addressable demand separate. Do not convert retail value directly into ingredient tonnage.

## 6. Market size and demand, when decision-relevant

Define the exact measure before giving a number. Keep capacity, production, shipments, sales volume, consumption/demand volume and sales value separate.

| Estimate/source | Exact measure | Ingredient identity/grade | Geography/base year | Method/inputs | Source incentive | Independence | Included/excluded | Result | Evidence status/gap |
|---|---|---|---|---|---|---|---|---|---|

### Triangulation
| View | Evidence used | Calculation | Result/range | Limitation | Reconciliation |
|---|---|---|---|---|---|
| Supply | | | | | |
| Trade | | | | | |
| Downstream use | | | | | |

State `verified estimate`, `corroborated range`, `directional range`, or `not reliably estimable`. Show volume and value separately and disclose every conversion formula.

### Supply-demand gap audit, when the opportunity depends on shortage, low penetration, substitution or capacity

| Application/specification | Demand maturity | Demand evidence/basis | Supply constraint | Supply evidence/basis | Alignment and applicable gates | Calculation/range | Gap conclusion | Evidence status | Invalidation/next evidence |
|---|---|---|---|---|---|---|---|---|---|

Use the demand-maturity, supply-constraint and evidence-status axes, conclusions and formulas from `market-size-and-demand.md`. Treat non-binding RFQs, LOIs, interviews and price interest as stated buyer interest. Complete the table only when every decision-relevant claim includes all three axes, applicable alignment fields, calculation or reason not to calculate, and an invalidation/next-evidence condition.

### Supplier financial materiality and platform value, when decision-relevant

| View | Inputs and formula | Result | Evidence status | Decision use | Gap |
|---|---|---|---|---|---|
| Standalone scenario revenue | Saleable volume × realized price × utilization/sell-through | | | | |
| Relevant business denominator | Business-unit or group revenue/profit basis | | | | |
| Demonstrated platform reuse | Shared process, dossier, application, qualification or channel asset | | | | |
| Adjacent-product hypothesis | Named products and incremental bottleneck/cost | | | | |

Keep scenario revenue separate from a forecast. State scale-up triggers as evidence-derived economics or explicit management choices; do not present an arbitrary order-coverage percentage as an industry rule.

## 7. Leading companies, SKU adoption and observed effects

Coverage: `[company universe] | [relevant SKUs found] | [labels checked] | [channels/markets] | [dates] | [labels inaccessible]`

### E-commerce label audit

| Platform/store type | Company/brand | Exact SKU/variant/market | Current availability | Complete label accessible | Exact ingredient wording or substitute | Label/observation date | Evidence capture/corroboration | Adoption class | Limitation |
|---|---|---|---|---|---|---|---|---|---|

| Application | Company | Brand/SKU/market | Adoption status | Ingredient/substitute and exact label wording | Evidence class | Primary SKU evidence/date | Corroboration | Current-sale status | Coverage/gap |
|---|---|---|---|---|---|---|---|---|---|

### Regulatory claim eligibility

| Jurisdiction | Proposed claim | Exact finished-product threshold/conditions | Final-product evidence available | Permitted wording/status | Mandatory qualifier/warning | Official source/version/date | Remaining gap |
|---|---|---|---|---|---|---|---|

Claim eligibility is a finished-product legal conclusion, not evidence that the ingredient caused a technical, health, consumer, or commercial outcome.

### Effect evidence and SMART audit

| Effect channel | Exact claim/outcome | Object/SKU/market | Metric/method | Sample/denominator | Comparator/baseline | Time window | Exact source/date | SMART check (S/M/A/R/T) | Observed result | Attribution allowed | Limitation |
|---|---|---|---|---|---|---|---|---|---|---|---|

Search and report adverse effects, withdrawals, null results, complaints, and negative commercial signals as actively as positive evidence. Use `pass` or the exact gap for each SMART element; do not convert SMART completeness into a numeric opportunity score.

## 8. Raw-material price, use amount and use cost
| Observation | Identity/specification | Quantity and terms | Normalized price | Price evidence band | Date | Limitation |
|---|---|---|---|---|---|---|

- Use-amount basis: regulatory boundary, literature/patent/supplier starting amount, proposed test amount, and commercial intended amount
- Ingredient-use cost scenarios; do not label them total BOM unless all other ingredients and conversion costs are included
- Which price conclusion is executable and which is only a public signal

| Application | Finished-product/subcomponent basis | Regulatory boundary | Evidence starting amount and source | Proposed test amount | Commercial intended amount/status | Raw-material price/band | Yield/loss | Ingredient cost per kg finished product | Ingredient cost per unit | Excluded costs | Formula/assumptions | Confidence/gap |
|---|---|---|---|---|---|---|---|---:|---:|---|---|---|

### Replacement-economics comparison

| Application | Finished-product basis | Incumbent ingredients/amounts/prices | Target ingredients/amounts/prices | Retained/removed/added components | Incumbent system cost | Target system cost | System-cost change | Estimated total ingredient cost before | Estimated total ingredient cost after | Total ingredient-cost change | Sources/assumptions/exclusions | Confidence/gap |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|

## 9. Potential customers (when requested)
| Account/business unit | Relevant products and SKU coverage | Geography | Why it fits | Observed adoption status/evidence class | Substitute or development evidence | Relevant-unit growth/momentum evidence and scope | Buying/timing signal | Likely role | Priority band/rule | Sources/dates and coverage gap | Next verification |
|---|---|---|---|---|---|---|---|---|---|---|---|

### Customer growth and momentum evidence

| Company | Relevant unit/category/brand | Target-product link | Metric | Scope/geography/channel | Period/comparison basis | Direction and disclosed driver | Source/date | Directness to ingredient demand | Priority implication | Counter-risk | Limitation/next check |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 10. Risks and evidence gaps
| Gap/risk | Why it matters | Current evidence | Validation action | Owner/expert needed |
|---|---|---|---|---|

## 11. Rule-based research-completeness check
| Rule | Result (met/conditional/not met/not applicable) | Supporting evidence | Exact gap | Effect on conclusion | Next action |
|---|---|---|---|---|---|

List every applicable rule from `research-quality-rules.md`. These are research-quality controls, not numeric thresholds or an opportunity score.

## 12. Recommended validation sequence
For every action state: literature-supported starting point; remaining gap; control and variants; measurements and time points; success/failure rule; decision unlocked.

## Sources
- [Title](URL) — publisher, date/access date, evidence level, literature reading depth when relevant, claim supported
```

For Chinese or bilingual food reports, identify the researched ingredient clearly at the start and run the final audit in `food-terminology-and-language.md`. Do not output a terminology table unless ambiguity could change identity, regulation, evidence transfer, or the decision.

Do not write an overall model-generated opportunity score. If comparison is necessary, show hard-gate results, evidence completeness, and unresolved decisions.
