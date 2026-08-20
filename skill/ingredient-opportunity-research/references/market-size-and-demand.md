# Market Size and Demand Validation

Use this protocol whenever ingredient demand, production, capacity, market value, growth, TAM, SAM or SOM affects a recommendation. The goal is a traceable decision range, not a decorative market number.

## Contents

1. Define the measure before searching
2. Build three independent evidence views
3. Audit the supply-demand gap
4. Source hierarchy and independence
5. Reconcile instead of averaging
6. Output rules
7. Practical closing actions
8. Supplier financial materiality and platform value

## 1. Define the measure before searching

Do not use `market size` without stating which measure is meant:

- nameplate or effective capacity;
- production/output;
- shipments or sell-in;
- sales volume;
- apparent consumption or end-use demand volume;
- inventory change;
- ex-factory, distributor or end-buyer sales value;
- downstream finished-product retail sales;
- TAM, SAM or supplier-addressable obtainable demand.

Lock the ingredient identity/grade, included production routes, geography, period, unit, value-chain level and nominal/real currency basis. Never add capacity, production and demand into one total or multiply demand volume by a price from a different grade, quantity, geography or transaction level without labeling the result a scenario.

## 2. Build three independent evidence views

### Supply view

Prefer audited filings, regulator filings, company production/sales disclosures, facility permits and credible industry interviews. Record producer, grade/route, nameplate and effective capacity, output, sales volume, utilization, inventory, geography and period separately.

- Capacity proves an upper supply capability, not demand or actual sales.
- A sales target or planned project is not actual sales.
- Flexible or multi-product capacity cannot be allocated fully to one ingredient.
- Supplier estimates may be useful but carry commercial incentives; identify the estimator and seek independent corroboration.

### Trade view

Use official customs statistics or authorized shipment-level services when the ingredient can be identified. Search exact names, synonyms, CAS numbers, trade names, producers and consignees.

- Verify whether the HS/customs code is ingredient-specific. If it includes other chemicals, do not call the aggregate ingredient trade.
- Deduplicate repeated bills, samples, returns, re-exports and unit/concentration differences.
- State what domestic production, domestic consumption or intra-region trade the dataset omits.
- Treat shipment-derived value as its stated incoterm/value basis, not automatically a domestic market price.

### Downstream-use view

Define the finished-product universe and estimate:

`ingredient demand = sum(finished-product output × inclusion rate × adoption share ÷ active concentration × loss factor)`

For every input, show the source, period, denominator and scenario. Use current labels/filings to estimate adoption only when SKU and market are identifiable. Do not infer inclusion rate from ingredient-list order. Calibrate product output, adoption and use amount through OEM/ODM, formulator, supplier, distributor or customer interviews when possible.

## 3. Audit the supply-demand gap

Run this audit whenever an opportunity claim relies on shortage, unmet demand, low penetration, substitution potential, supply security, or proposed new capacity. Classify the claim on three independent axes so overlapping concepts can coexist:

### Demand maturity

- **latent end-user need:** a recommended or desired outcome differs from observed intake, access or use; it is not ingredient demand;
- **scenario addressable demand:** a modeled adoption, substitution or downstream-use scenario passes stated technical, regulatory and economic assumptions; low penetration or a large incumbent pool alone remains substitution whitespace;
- **stated buyer interest:** non-binding RFQs, LOIs, interviews or stated price interest after deduplication; it is directional rather than committed;
- **committed demand:** binding orders/contracts or documented unfilled orders after deduplicating buyers and volumes and netting cancellations, conditions and volume counted elsewhere.

### Supply constraint

- **aggregate physical constraint:** requirements or orders during a defined period exceed available saleable supply on the same basis; historical sales or apparent consumption describe cleared volume, not unsatisfied demand;
- **qualified-supply constraint:** evidenced buyer requirements cannot be met by supply with the exact specification, active form/content, jurisdiction/application eligibility, dossier, certification, location and qualification timing;
- **no evident constraint:** aligned evidence shows sufficient headroom for the stated demand basis;
- **unresolved constraint:** the necessary supply evidence or alignment is missing.

Use the **evidence status** from Section 6 as the third axis. Confidence belongs on this axis, not inside demand maturity or supply constraint.

Before calculating, mark every field as aligned, unresolved or not applicable to the claimed gap:

| Alignment field | Required comparison |
|---|---|
| Identity and specification | Ingredient, source/route, grade, purity, active content and chemical/physical form |
| Use eligibility | Jurisdiction, product class, application, population, dose/use level and supplier-specific authorization |
| Market boundary | Geography, period, unit and value-chain level |
| Commercial terms | Price basis, quantity, incoterm, lead time and minimum order when commercial acceptance or substitution is claimed |
| Qualification | Buyer approval, dossier, certification, site and qualification timing when qualified or committed demand is claimed |
| Availability | Saleable output rather than nameplate capacity; define inventory, commitments and flexible-capacity allocation without double counting |

For a modeled physical shortfall, use only non-overlapping components:

`available saleable supply = opening usable inventory + in-period saleable production + eligible imports - exports - volume committed outside the target pool - required ending/safety stock`

`modeled physical shortfall = comparable requirements or orders - available saleable supply`

Disclose omitted components and do not combine the formula with a source measure that already embeds them. Calculate a physical shortfall or qualified-supply mismatch only when the necessary inputs align. A negative result shows modeled supply headroom on that defined basis, not market-wide oversupply. If alignment is incomplete, report a directional mismatch or `not reliably estimable` instead of subtracting incompatible figures.

Treat these as separate signals, not standalone proof:

- shortage signals: allocations, repeated stockouts, longer matched lead times, rising like-for-like transaction prices, high utilization, urgent second-source searches or unmet contracted volume; corroborate price and utilization signals because input costs, mix or capacity discipline can produce the same pattern;
- headroom signals: comparable inventory rising relative to sell-through and shelf life, falling like-for-like transaction prices, low utilization, canceled expansions, discounting or production materially above sell-through; reconcile crude versus finished inventory, planned maintenance and safety-stock policies before inferring surplus;
- adoption signals: low penetration, new launches and fast growth show whitespace or momentum, not shortage;
- resource signals: constrained fisheries, feedstocks or theoretical nutrition deficits show exposure, not monetizable demand at the target price.

For each application and saleable specification, output:

| Application/specification | Demand maturity | Demand evidence/basis | Supply constraint | Supply evidence/basis | Alignment and applicable gates | Calculation/range | Gap conclusion | Evidence status | Invalidation/next evidence |
|---|---|---|---|---|---|---|---|---|---|

Use one gap conclusion: `committed unmet demand`, `modeled scenario shortfall`, `directional qualified mismatch`, `substitution whitespace`, `latent need`, `no evident supply gap`, or `not reliably estimable`. Reserve `committed unmet demand` for committed demand paired with an evidenced aggregate or qualified-supply constraint. Report evidence status separately as `verified estimate`, `corroborated range`, `directional range`, or `not reliably estimable from available evidence`. When writing in another language, retain the canonical English label in parentheses so classifications remain comparable across reports.

The audit is complete only when every decision-relevant gap claim has all three axes, aligned/unresolved fields, a calculation or explicit reason not to calculate, and an invalidation or next-evidence condition.

Use aligned effective supply and demand to calculate a commercial gap. Treat recommended intake, low penetration, an incumbent market pool, resource scarcity and forecast deficits as their named classes or signals until buyer-level evidence supports a stronger conclusion.

## 4. Source hierarchy and independence

Use, in descending preference:

1. audited actual production/sales, invoices/contracts or regulator/official statistics;
2. comparable current RFQs, shipment records and company filings with actual operating data;
3. named expert interviews with disclosed scope and method;
4. paid databases/reports with accessible definitions, sample, calculation and source list;
5. broker research, supplier estimates and public report summaries;
6. unattributed webpages, AI-generated summaries and repeated numbers with no method.

Source count is not independence. Trace repeated figures to the earliest discoverable source. Reports that repeat the same number, wording, tables or unexplained assumptions form one evidence chain, not corroboration.

## 5. Reconcile instead of averaging

For each estimate, record:

| Estimate | Exact measure | Identity/grade | Geography/period | Method and inputs | Source/incentive | Independent? | What it includes/excludes | Result | Reconciliation status |
|---|---|---|---|---|---|---|---|---|---|

Investigate disagreement through identity, grade, value-chain level, price basis, period, geography, active concentration, inventory, re-export, capacity utilization and source incentives. Do not average incompatible figures.

Run arithmetic plausibility checks:

- `sales value ≈ sales volume × comparable realized price`;
- `production ≤ effective capacity` after defining period and utilization;
- `apparent consumption ≈ production + imports − exports ± inventory`, when the data support each term;
- downstream demand must be compatible with the number/output of adopting products and plausible inclusion rates.

Reject or quarantine an estimate when it is orders of magnitude inconsistent and the source does not explain the difference.

## 6. Output rules

State one of:

- **verified estimate:** primary operating/statistical data reconcile across views;
- **corroborated range:** independent views overlap after definitions are aligned;
- **directional range:** one or more inputs rely on interested, opaque or indirect evidence;
- **not reliably estimable from available evidence.**

Always show:

- base year and access date;
- volume and value separately;
- low/base/high formulas when scenarios are needed;
- exact price level used for value conversion;
- sensitivity to adoption, use amount, grade mix and utilization;
- unresolved gap and the cheapest next evidence that could close it.

When a supply-demand gap affects the recommendation, state demand maturity, supply constraint and evidence status on separate axes and include the aligned comparison table from Section 3.

Do not call a number current merely because a report was recently published; verify the underlying data year. Do not present forecast CAGR without the base value, forecast period, method and scenario assumptions. Do not present TAM as supplier-addressable demand until regulation, grade, geography, application and realistic adoption constraints are applied.

## 7. Practical closing actions

When public evidence is insufficient, specify a data-acquisition plan rather than inventing precision:

- matched interviews or RFQs with producers and distributors asking actual prior-period sales rather than capacity;
- shipment-level searches using identity, CAS, trade names and counterparties;
- a reproducible SKU/label census plus bottom-up inclusion-rate scenarios;
- interviews with OEM/ODM formulators and customers to calibrate use amount and annual output;
- purchase of a report only after reviewing its definitions, producer list, sample, methodology and source independence.

## 8. Supplier financial materiality and platform value

When the ingredient is one product on a shared manufacturing, fermentation, regulatory, application or sales platform, evaluate two distinct questions:

1. **standalone materiality:** calculate scenario revenue as `saleable volume × realized price × utilization or sell-through`, state every input and compare it with the supplier's relevant business-unit and group denominator;
2. **platform value:** identify which assets, learning, dossiers, customer qualifications or routes are demonstrably reusable across named products, and what incremental cost or bottleneck still applies to each extension.

Label the standalone calculation a scenario unless capacity, executable price, utilization and sell-through are verified. Do not convert nameplate capacity into sales, or a scenario into a forecast. Do not describe a portfolio as a large revenue opportunity merely by adding candidate products; support the claim with product-level demand, economics and reuse evidence.

Separate a low-materiality flagship or qualification product from a profit product when the evidence supports that role. Define scale-up triggers from lead time, qualification cycle, contribution margin, committed or probability-weighted demand, flexible-capacity opportunity cost and downside tolerance. If those inputs are unknown, present candidate decision variables rather than inventing a universal order-coverage percentage.
