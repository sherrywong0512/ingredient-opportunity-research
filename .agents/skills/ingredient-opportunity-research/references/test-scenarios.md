# Routing and Generalization Tests

Use these scenarios when revising the skill.

## A/B Evaluation Protocol

Compare the current skill against a no-skill baseline using the same prompt, ingredient identity, geography, cutoff date, source access, time budget, and requested deliverables. Prefer independent fresh sessions and blind the reviewer to version names. If the same agent produces both versions sequentially, disclose context contamination and treat results as workflow evidence rather than an independent experiment.

Apply hard gates first. A report cannot pass if it:

- confuses the ingredient identity;
- fails to check the core target-market regulation or, for food work spanning the standard scope, omits the joint China–United States–European Union category/use table;
- recommends an application with no traceable property evidence or explicit hypothesis label;
- claims company use without product-level evidence;
- treats sales, reviews, claims, patents, or continued listing as causal product-effect proof;
- converts a finished-product claim permission into proof of ingredient efficacy;
- omits foreseeable adverse-effect/tolerability searching when human or use effects matter;
- recommends a consumer-facing route for an unfamiliar ingredient without assessing awareness and education burden;
- uses inconsistent or literal translated terminology that changes identity, regulation, technical meaning or claim strength;
- presents nutritional need, low penetration, an incumbent pool, resource scarcity, forecast deficit or nameplate capacity as a commercial supply-demand gap without separate demand-maturity, supply-constraint and evidence-status classifications, gap-relevant aligned inputs and a non-overlapping calculation;
- presents non-binding RFQs, LOIs, interviews, price interest or duplicate buyer inquiries as committed unmet demand.

Also audit every applicable rule in [research-quality-rules.md](research-quality-rules.md). An unmet rule must be shown as not met or conditional; the analyst may not silently waive it. The scoring rubric below is secondary to these decision-readiness rules.

Then score research quality out of 100:

| Dimension | Weight |
|---|---:|
| Ingredient identity and specification accuracy | 8 |
| Property and original-literature evidence, including adverse findings | 12 |
| Property-to-need-to-application traceability and hard gates | 12 |
| China–US–EU regulation and finished-product claim boundaries | 12 |
| Formulation, process, use amount, storage and failure-mode validation | 12 |
| Leading-company, SKU adoption and potential-customer coverage audit | 14 |
| Technical/human/claim/consumer/commercial separation and SMART discipline | 12 |
| Comparable raw-material price, use amount and use cost | 10 |
| Executable validation and customer-verification actions | 8 |

Score 0 for missing or materially wrong, approximately half credit for directional but decision-insufficient work, and full credit only when evidence, limitations, and next action are complete. Apply caps: wrong identity <=30; missing core regulation <=50; fabricated customer use <=40; no original paper or finished-product evidence <=65; no disclosed potential-customer/SKU search coverage <=75; no adverse-effect search where relevant <=75.

Interpretation: 85–100 decision input with stated gaps; 70–84 suitable for project screening or interviews; 50–69 directional only; below 50 unsuitable for commercial decisions. This is a report-quality score, never an opportunity score.

## Expected consumer-product routes

1. `Research the opportunity for isomalt in bakery products and identify ten potential users.`
   - Route: feasibility + one specified application + 10-account customer discovery.
   - Check: distinguish isomalt from isomaltulose in one concise identity statement; keep replacement-study results out of the intrinsic-property table; test whether low hygroscopicity helps crisp products but conflicts with soft/moist products; separate partial from full sucrose replacement; compare the incumbent and proposed sweetener-system cost and, when a supportable cookie formulation cost is available, calculate the change in estimated total ingredient cost; check China–US–EU category use and finished-product sugar-free claim conditions separately; search gastrointestinal tolerance, laxation and diarrhea evidence; mention market education only if it changes positioning or customer action; report potential-customer SKU/label coverage and do not label all ten as current users.

2. `调研结冷胶在消费品中的机会，并找出最开始应该攻坚的客户。`
   - Route: broad application mapping + feasibility + customer prioritization + optional KA card.
   - Check: shortlist across relevant consumer categories before selecting an account; distinguish high-acyl and low-acyl grades, product-specific regulatory status, and actual SKU-label use; use P1/P2/P3 rules instead of an opportunity score.

3. `找出圆柚酮推广的市场机会。`
   - Route: ingredient identity clarification + application mapping + feasibility.
   - Check: resolve synonyms/grade/function and target geography before treating similarly named substances as identical; decompose supplier claims about route, purity, scale, capacity, customer recognition, orders and sales instead of letting one company disclosure confirm the whole chain; do not call a producer volume estimate and an arithmetically compatible review market value independent corroboration without tracing provenance and definitions; distinguish fragrance/flavour cash flow, standalone financial-materiality scenarios, reusable terpene-platform evidence and repellent regulatory optionality; do not infer a price decline from unmatched natural/synthetic routes or commercial terms, convert repellent registration into end-product adoption, turn capacity into market share, or use an arbitrary order-coverage percentage as a universal expansion gate.

4. `Research global market opportunities for human milk oligosaccharides and identify ten potential customers.`
   - Route: molecular-family identity + multi-jurisdiction feasibility + adoption verification + customer discovery.
   - Check: separate 2'-FL, 3-FL, LNT, LNnT, 3'-SL, 6'-SL and other structures; do not transfer one molecule, production strain, supplier, jurisdiction, dose, or product-class approval to the whole HMO family; separate product tolerance, microbiome, clinical outcome, and commercial adoption evidence; normalize Chinese scientific, infant-nutrition and regulatory terminology rather than literally translating English prose; assess whether consumers recognize HMO names, understand the benefit concept, associate it with relevant products, and require ingredient-led, benefit-led or professional education in each target market.

5. `判断合成生物学方法生产的 Omega-3，需求和供给之间的 gap 有多大。`
   - Route: identity/specification split + market feasibility + market-size and supply-demand gap audit.
   - Check: separate generic DHA-rich microbial oil, high-EPA or high-concentration EPA+DHA oil, human nutrition and aquafeed; distinguish wild-type fermentation from genetically engineered production and verify exact-product regulatory transfer. Classify recommended-intake deficits as latent end-user need, low algal penetration as scenario addressable demand or substitution whitespace, fish-oil forecasts as resource signals until target-period requirements and available saleable supply align, and only binding or documented unfilled orders as committed demand. Treat non-binding RFQs as stated buyer interest. Compare production, sales, inventory, effective capacity and qualified supply separately; normalize active EPA+DHA content before substitution calculations; avoid double counting inventory, trade and commitments; do not infer market-wide surplus from one producer's inventory or shortage from sales growth alone. Report demand maturity, supply constraint and evidence status separately, and return `not reliably estimable` where public supply or buyer-demand inputs are not aligned.

### Scoped-request routing tests

A scoped request selects that piece only; it is not a license to re-run the whole analysis. These scenarios check the route table and stage gating.

6. `我想知道 HMO 的 KA 攻坚卡。`（HMO 可行性已存在——用户上一步产出或 `examples/03-hmo-global-market.md`）
   - Route: KA development only.
   - Check: start from the existing report's evidence; pick 1–2 accounts with account thesis, evidence gaps, functional roles, one value proposition and a 30/60/90-day validation sequence; output must show no re-run of stage 1–3 research and must not add new facts beyond the report.
   - Hard failure: the output re-derives properties, re-audits regulation, or rewrites the market analysis instead of building the card from the report.

7. `只要攻击卡，但我没有报告。`（同一请求，无既有可行性）
   - Route: KA development, gate not satisfied.
   - Check: the skill must state that the card cannot be evidence-backed yet and either produce the feasibility analysis first or ask the user to supply/point to one; it must not silently fabricate an account thesis.
   - Hard failure: an account thesis with no report-based evidence, or a card delivered as if it were grounded.

8. General opportunity request `调研 HMO 的市场机会` must NOT auto-add customer lists, KA cards or artifacts; scoped pieces appear only when requested separately.

9. `找 10 家潜在客户` with no prior report → route customer discovery, produce the report first, then the 10-account list with SKU/label coverage disclosed and not all labeled current users.

### Gap-audit adversarial assertions

Use these assertions when the gap module changes. The revised skill passes only when it produces the expected classification without the forbidden inference.

| Evidence presented | Expected demand maturity | Expected supply constraint | Expected conclusion | Forbidden inference |
|---|---|---|---|---|
| Population intake is below a recommended level; no buyer evidence | Latent end-user need | Unresolved constraint | `latent need` | Treat the nutrition deficit as ingredient orders |
| Target source has low share of a large incumbent market; replaceable share and price acceptance remain assumptions | Scenario addressable demand | Unresolved constraint | `substitution whitespace` | Treat the incumbent pool as unmet demand |
| One producer reports sales growth while production and inventory grow faster | Observed cleared demand only | Unresolved constraint outside that producer | `not reliably estimable` market-wide | Infer either market-wide shortage or surplus |
| A forecast fish-oil deficit and algal-oil output use different applications, concentrations or periods | Scenario addressable demand at most | Unresolved constraint | `not reliably estimable` | Subtract the two headline figures |
| Non-binding RFQs request more volume than current capacity | Stated buyer interest | Directional aggregate or qualified constraint | `directional qualified mismatch` at most | Call the difference committed unmet demand |
| Deduplicated binding orders for 10,000 units and qualified supply of 6,000 units use the same specification, period and terms | Committed demand | Aggregate or qualified-supply constraint | `committed unmet demand` of 4,000 units, with separate evidence status | Inflate the result with conditional or duplicate volume |

## Non-consumer boundary test

Scenario: `Research a concrete admixture ingredient for infrastructure customers.`

The framework remains useful for technical fit, regulation/standards, substitutes, buyer identification, economics, and decision mapping. Its consumer demand, retail product, review, brand, and channel modules do not transfer cleanly. Therefore:

- do not include industrial-only materials in the skill's default trigger;
- explain partial applicability;
- proceed only after replacing consumer-product modules with sector-specific demand, specification, tender/procurement, asset-cycle, and project-pipeline analysis.

This is a boundary result, not proof that one universal workflow covers both markets.

10. Bare input `HMO` (no verb, no deliverable).
    - Route: Market feasibility by default; full market-opportunity analysis.
    - Check: the skill must not stall on clarifying questions; it proceeds with
      explicit labeled defaults (geography per the skill's standard scope for
      food, downstream = consumer applications broadly, objective = explore
      applications), states them at the top of the report, and closes with what
      input would narrow the analysis.
    - Hard failure: asking for more input without producing the analysis, or
      producing a scoped artifact (customer list / KA card) that was not asked for.
