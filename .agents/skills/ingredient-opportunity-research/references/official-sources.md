# Official Source Registry

Consult this registry for evidence types that have a canonical official source.
Where a row lists an official registry, consult it **first** and cite the
official entry as the E1 anchor; third-party aggregators (e.g. foodmate,
commercial databases) are search aids, not substitutes for the official text.
For evidence types with **no official source**, the row says so explicitly —
never dress up non-official data in official-sounding language.

> Official deep URLs move (FDA restructures its site, CNHC republishes).
> Record the registry name and the search path you used, not only a deep link;
> when a direct link fails, verify via the Wayback Machine before calling it dead.

## Chemical identity, names, identifiers

| Question | Official source (by jurisdiction/scope) | What it establishes |
|---|---|---|
| Molecule identity, CAS/UNII/INCI normalization | Global: CAS Registry (via SciFinder / cas.org); open fallback: PubChem (NLM). US official: FDA GSRS — Global Substance Registration System / UNII (`precision.fda.gov/ginas`, `precision.fda.gov/uniisearch`). Cosmetics nomenclature: INCI (PCPC) | The exact substance, its identifiers, and which similar names must not be conflated |
| Name/grade/source disambiguation | IUPAC nomenclature; the registry above; the jurisdiction's positive list (below) | Which authorized identity the ingredient matches |

## Food-additive and ingredient regulatory status

| Jurisdiction | Official registry / text | What it establishes |
|---|---|---|
| China | National Health Commission (NHC) food-safety standards: GB 2760 (food additives), GB 14880 (nutrition fortifiers), GB 2762/GB 29921 (safety), new-food-ingredient announcements; authoritative search via the NHC site and 国家食品安全风险评估中心 (CFSA). Official texts, not aggregator mirrors | Permitted category, use level, legal route (additive / fortifier / novel food / general food) |
| United States | eCFR Title 21 (esp. 21 CFR 170–199); FDA GRAS Notice Inventory and FDA letters; FDA Food Additive Status List; FDA "Ingredients added to food" | GRAS or additive status, permitted conditions, current regulatory framework |
| European Union | EUR-Lex consolidated text of Regulation (EC) No 1333/2008; EFSA opinions; EU Novel Food Union List | Permitted category and conditions (E number), novel-food authorisation |

## Claims, nutrition, standards

| Question | Official source | What it establishes |
|---|---|---|
| Nutrition/claim thresholds (CN) | GB 28050 (nutrition labelling and claims) | Legal thresholds (low-sugar, no-added-sugar, etc.) |
| Claims (US/EU) | FDA structure/function vs health-claim framework; EFSA claim register | Which claim wording is permitted |
| Specifications/standards | FAO/WHO JECFA, Codex Alimentarius, ISO, national standards (GB), pharmacopoeias | The standard the ingredient/grade is measured against |

## Patents and literature

| Question | Official source | What it establishes |
|---|---|---|
| Patent disclosure/existence | USPTO, CNIPA, EPO Espacenet, WIPO (official patent offices) | Disclosure exists — never independent performance or freedom to operate |
| Published studies | PubMed (NLM), Crossref DOI records, ChiCTR / ClinicalTrials.gov registries | The study exists and where; reading depth must still be disclosed |

## Cosmetics and pet food (special categories)

| Question | Official source | What it establishes |
|---|---|---|
| Cosmetics ingredients (CN) | NMPA 《已使用化妆品原料目录》and 《化妆品安全技术规范》 | Whether the ingredient is in the used-ingredient inventory and under what conditions |
| Cosmetics ingredients (EU/US) | EU CosIng; US FDA cosmetics pages (no pre-approval regime) + INCI | EU inventory status / US regulatory posture |
| Pet food (US/CN) | AAFCO (US definitions); 农业农村部饲料原料目录 (CN) | Legal definition and permitted feed-material status |

## No official source exists — apply evidence-level discipline

The following evidence types have **no canonical official source**. Do not
invent "officialness": label the source type, its interest, and its evidence
level per `evidence-and-sources.md`.

- Market size, demand volume, growth forecasts (E3–E4 at best; supplier decks are interested evidence)
- Prices and price trends (public listings are signals, not transactions)
- SKU adoption, brand usage, customer status (label-level evidence; never infer causality)
- Company scale, financial contribution, buying intent (decompose; filings ≠ orders)
- Consumer awareness and education burden (survey-method dependent)
