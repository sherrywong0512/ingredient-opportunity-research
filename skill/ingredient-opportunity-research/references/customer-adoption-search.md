# Potential-Customer Adoption Search Protocol

Use this protocol for every shortlisted account. Its purpose is to establish public adoption status, not to infer confidential supplier relationships.

## 1. Define the Account Search Unit

Record:

`legal company | business unit | brand | target market | relevant product category | live-SKU inclusion rule | ingredient identity/synonyms/exclusions | search date`

Search at brand and SKU level, not only at parent-company level. Regional formulations, contract manufacturers, and similarly named ingredients must remain separate.

## 2. Run the Search in Evidence Order

### Pass A — Current commercial products

1. Search the official company and brand sites for the ingredient, synonyms, branded ingredient names, E/INS numbers, relevant claims, and complete ingredient lists.
2. Search official flagship stores, authorized retailers, major e-commerce platforms, and product/label registries. Apply [ecommerce-label-research.md](ecommerce-label-research.md).
3. Check packaging images for every included live SKU and record exact wording, market, pack/variant, label date if shown, and observation date.
4. Corroborate a positive label with a second current source when practical. Treat regional or outdated labels as limited evidence.

### Pass B — Substitute and problem evidence

For live products without the target ingredient, record the complete substitute system and the product need it serves. Search category terms plus relevant functions, claims, complaints, recalls, reformulations, and quality problems. A substitute-containing SKU supports a switching hypothesis only when the target ingredient has evidence for that exact function and matrix.

### Pass C — Development and pipeline evidence

Search company filings, regulatory submissions, patents, clinical-trial records, R&D collaborations, technical presentations, job postings, factory/OEM disclosures, launch announcements, and supplier case studies. Record project stage and date. These sources support `development evidence`, not current commercial use unless tied to a live SKU and current formulation.

### Pass D — Buying and timing signals

Search recent strategy statements, relevant-unit/category growth, category investment, capacity expansion, procurement or quality roles, product-development hiring, formulation changes, tenders, import/manufacturing records, and public supplier qualification requirements. Prefer metrics tied directly to the relevant business, product family, geography, or channel. If only company-wide growth is public, record it as indirect unless the link to the target application is evidenced. These signals inform account timing and access; they do not prove ingredient use or purchase.

Use query families such as:

- `site:official-domain ingredient-name OR synonym OR branded-name`
- `brand + exact ingredient + 配料表/ingredients/包装/label`
- `company + ingredient + patent/trial/研发/合作/launch`
- `company + target category + relevant function/claim/problem/substitute/buying signal`
- exact SKU names across two current retail channels

Record the material queries used, including failed searches, so another researcher can reproduce the coverage.

## 3. Assign Status from Evidence, Not Fit

| Status | Minimum evidence | What may be said |
|---|---|---|
| Verified current user | A1/A2 current SKU-level evidence under the adoption ladder | Exact SKU, market, formulation version and observation date use the ingredient |
| Verified company-level use/procurement | C1 evidence names company, ingredient and period but not SKU | Company-level use/procurement is public; product mapping remains unresolved |
| Development evidence | D1 evidence of trial, patent example, filing, collaboration or pipeline | Company has relevant development activity; commercial adoption is unverified |
| Verified substitute user | Current complete SKU label identifies the substitute and omits the target ingredient | That SKU/market/version uses the named substitute; switching feasibility remains a hypothesis |
| Possible use | Indirect L1 evidence only | Lead requiring label or filing verification |
| No public evidence found | Disclosed search and SKU coverage found no sufficient evidence | No sufficient public evidence was found within the stated coverage |
| Confirmed absent/discontinued | Current complete label omits it for an exact SKU, or authoritative discontinuation evidence | Absence/discontinuation only within the stated SKU, market, version or product |

Do not use `plausible buyer` as an adoption status. It is an account-qualification conclusion and must be shown separately from observed use.

## 4. Capture the Audit Trail

Use:

`company/business unit | brand/SKU/market | relevant-product universe | SKUs found | complete labels checked | labels inaccessible | target ingredient exact wording | substitute exact wording | current-use evidence class | development evidence | relevant growth/momentum signal and scope | buying/timing signal | adoption status | sources/dates | queries/channels | coverage gap | next verification action`

For a company-level conclusion, aggregate only after retaining SKU-level rows. Report numerator and denominator, for example `8 of 12 relevant live SKUs had accessible complete labels; 1 verified target-ingredient SKU`.

## 5. Stop and Escalate Correctly

- Stop calling an account a current user when only patents, supplier logos, marketplace titles, claims, reviews, snippets, or old launches are available.
- Do not conclude non-use when labels are inaccessible, the SKU universe is undefined, or only one market was checked.
- Do not infer the incumbent supplier, contract price, satisfaction, project stage, purchase volume, or decision-maker from ingredient presence.
- For P1 accounts, require either direct adoption evidence or a current substitute/problem signal plus technical and regulatory fit. Otherwise keep the account conditional.
- Escalate the remaining gap to an authorized data source, account interview, distributor/OEM confirmation, sample purchase and label inspection, or internal CRM/procurement evidence as appropriate.

## 6. Adversarial Check

Before publishing, test whether each conclusion survives these challenges:

1. Could this be a different molecule, grade, branded blend, or regional formula?
2. Is the evidence current and tied to the exact SKU, or only to the company/category?
3. Did the search include negative cases and inaccessible labels, or only confirming examples?
4. Does “not found” merely reflect weak coverage?
5. Is a buying-fit inference being presented as observed adoption?
6. Is a supplier relationship, purchasing volume, or satisfaction being invented from a label?
