# Ingredient Price Research Protocol

Use this protocol when raw-material price, formulation cost, or customer economics affect feasibility.

## Define the Comparable Item

Lock before comparing: chemical identity/CAS, grade and assay, brand or origin, particle/form, packaging, order quantity, delivery place, tax, freight, Incoterm, payment terms, quote date, and validity. Never average non-comparable observations.

## Evidence Ladder

| Band | Source | Permitted use |
|---|---|---|
| P1 | Authorized contracts, invoices, ERP or procurement records | Transaction benchmark within the stated terms |
| P2 | Matched same-specification RFQs from independent verified manufacturers or first-tier agents | Current executable quote evidence when coverage is sufficient for the buying decision; still not a completed transaction |
| P3 | Product-specific shipment records with value and net weight | Derived cross-border unit-value check after cleaning freight, mixed loads, and HS ambiguity |
| P4 | Audited B2B listings with identity, specification, MOQ, and date | Public listing signal only |
| P5 | Distributor/aggregator pages or search snippets | Lead or anomaly check only |

Keep the price-evidence band separate from the general E1–E5 claim level. A current supplier listing can be directly observed yet still be weak evidence of a transaction price.

## Standard RFQ

Choose sample, pilot, initial-commercial, and scaled-purchase quantities that match the supplier's expected buying pattern, then request prices on otherwise matched terms. Ask for tax, freight, MOQ, lead time, validity, payment terms, COA, specification, manufacturer/agent identity, and lot-consistency evidence appropriate to the qualification decision. Add application-specific grade or documentation requirements.

## Normalize and Report

1. Reject identity or specification mismatches.
2. Convert valid observations to one basis such as `CNY/kg, tax-included, delivered to [city]`; disclose exchange rate and date.
3. Separate manufacturer, first-tier agent, distributor, import brand, and domestic unbranded material.
4. Report range, median when meaningful, sample count, dates, and terms; investigate material outliers through specification and commercial-term differences rather than a universal percentage cutoff.
5. Refresh quotes when age or market volatility could change the decision; state the chosen cadence and reason.
6. Calculate finished-product ingredient-use cost at a realistic use amount and yield. Keep formulation cost, processing loss, logistics, testing, and claim costs separate.

## Calculate Use Amount and Use Cost

For each priority application, keep four quantities separate:

1. **Regulatory boundary:** maximum food-use level, quantum satis/GMP, daily-intake limit, warning threshold, or other applicable condition. Do not treat daily intake as a formulation maximum.
2. **Evidence starting amount:** amount reported in an exact- or adjacent-matrix paper, patent worked example, method-disclosed supplier application study, standard, technical dossier, or disclosed commercial formulation. Preserve the case's original denominator and transferability limits.
3. **Proposed test amount:** the smallest justified control and use-level ladder needed to close the technical gap.
4. **Commercial intended amount:** the amount per kg of finished product and per saleable unit after formulation and sensory validation.

Use this table:

`application | finished-product basis | regulatory boundary | evidence starting amount and source | proposed test amount | commercial intended amount/status | raw-material price and price band | yield/loss | ingredient cost per kg finished product | ingredient cost per saleable unit | excluded costs | formula and assumptions | confidence/gap`

Calculate transparently:

- `ingredient kg per kg finished product = use fraction / finished-product yield`;
- `ingredient cost per kg finished product = ingredient kg × normalized raw-material price`;
- `ingredient cost per unit = cost per kg finished product × unit net weight in kg`.

If the ingredient is used in a subcomponent rather than directly on a whole-product basis, first calculate the ingredient fraction in that subcomponent, then multiply by the subcomponent amount per finished unit. Run sensitivity scenarios when uncertainty in use amount, price, yield, or subcomponent share could change the decision; derive the scenario bounds from evidence rather than a preset pattern. Never call a patent range a recommended production amount or a public price signal a current procurement price.

Use wording such as `public listing signal`, `formal quotation`, or `observed transaction`. Never call a public range the market average. If P1–P3 data are unavailable, say that commercial feasibility remains provisional and provide the exact RFQ needed to close it. Report cost as `ingredient-use cost`, not total BOM, unless every BOM component and conversion cost is included.

## Compare Replacement Economics

For every replacement, partial-replacement, or co-formulation proposal, compare the incumbent ingredient system with the proposed system on the same finished-product and functional-performance basis.

Use:

`application | finished-product basis | incumbent ingredients/amounts/prices | target ingredients/amounts/prices | retained/removed/added components | incumbent ingredient-system cost | target ingredient-system cost | absolute and percentage system-cost change | estimated total ingredient cost before | estimated total ingredient cost after | absolute and percentage total-ingredient-cost change | price/use-amount source | assumptions/exclusions | confidence/gap`

Formulas:

- `ingredient-system cost = sum(component use amount × normalized component price ÷ yield)`;
- `system-cost change = target system cost − incumbent system cost`;
- `estimated total ingredient-cost change % = (estimated total ingredient cost after − before) ÷ before × 100%`.

Only calculate the total ingredient-cost change when the relevant finished-product recipe, use amounts, and comparable price bases are available or transparently estimated. Label estimates and show the source or assumption for every material component. `Estimated total ingredient cost` covers formulation ingredients only; it is not total BOM, COGS, or manufacturing cost unless those additional elements are completely evidenced. When recipe confidentiality prevents a full calculation, give the target ingredient-system cost change and the exact customer data required to calculate its share of total ingredient cost.

Use the application-case evidence protocol in [technical-validation.md](technical-validation.md) before calling an amount common or typical for a system. Product-label presence without a disclosed formulation does not provide a use amount.
