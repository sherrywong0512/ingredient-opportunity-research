---
name: ingredient-opportunity-research
version: 1.4.3
updated: 2026-08-23
description: Research market feasibility and downstream sales opportunities for ingredients and raw materials used in consumer products. Use when an ingredient sales team needs to identify promising consumer-product applications, investigate comparable market prices, validate formulation and process feasibility with papers or patents, assess demand, competition, regulation, consumer awareness and market-education burden, find and prioritize potential B2B customers, or prepare optional interview guides, key-account plans, and presentation outlines. Supports professionally edited Chinese, English, and bilingual deliverables.
---

# Ingredient Opportunity Research

Turn fragmented market information into an evidence-traceable feasibility report for ingredient sales teams. Research the downstream consumer-product market, then translate findings into customer-development actions. Do not substitute model judgment for an industry expert's commercial decision.

## Guardrails

Read [references/guardrails.md](references/guardrails.md) **now**, before anything else. Its rules apply to every request and every deliverable; hold them from the first step and do not proceed until you have them loaded.

## Route the Request

**Scope comes from what the user asks, in three shapes:**

- A minimal input — just an ingredient name or a name plus a hint ("HMO", "isomalt in China") — selects **Market feasibility** by default: output the full market-opportunity analysis for that ingredient. Missing research-contract fields become explicit, labeled default assumptions instead of blocking questions: geography defaults to the user's language/location hint when present, otherwise the skill's standard scope (for food ingredients, audit China, the United States and the European Union); downstream scope defaults to the ingredient's consumer applications broadly; business objective defaults to exploring applications. State these defaults at the top of the report and close with what input would narrow the analysis.
- A general market-opportunity request — "analyze the market opportunity for X" — selects **Market feasibility** only: the full chain and the default report. Customer discovery, KA development and sales artifacts are added only when the user asks for them separately.
- A scoped request naming one piece — "I want the KA attack card for HMO", "find potential customers for Y", "draft interview questions for Z" — selects **that piece only**, executed per the table below. A scoped request is not a license to re-run the whole analysis.

Before researching, decompose the request into a deliverable list and write one routing note in your working notes:

`route: [modes] | deliverables: [what you will output] | run: [which stages] | load: [which references] | skip: [what you will not redo]`

| Mode | The user says | What you run | Gate | Output |
|---|---|---|---|---|
| **Market feasibility** | "Analyze the market opportunity for X" (general) | Stages 1–3, then the default report | None | Full feasibility report |
| **Customer discovery** | "Find N potential customers for X" (separate request) | Stages 1–3 + report when none exists, then customer discovery; customer discovery only when a report exists | Account evidence; never invent usage | Report (when missing) + verified customer list |
| **KA development** | "KA attack card for X", "which account to attack" | Start from the existing report and customer list and build the card; produce the report and list first only when neither exists | Feasibility + customer list must exist or be produced | KA card + advance plan |
| **Sales artifact** | "Interview questions / presentation outline for X" | Artifact only, built from existing report evidence; produce the report first only when none exists | Feasibility must exist or be produced | The requested artifact |

**Gates in practice:** a scoped KA or artifact request always starts from report evidence. When no feasibility analysis exists (not from this skill, not from the user, not an archived case the user points to), state that the piece cannot be evidence-backed yet and produce the feasibility analysis first — a KA card or interview guide without a report basis would be unsupported. Match the user's language for both the analysis and the piece.

Required references per route (load them in `Run the Feature-to-Market Chain`, at the step that needs them):

- **Any feasibility or customer-discovery route:** `evidence-and-sources.md`, `feature-application-adoption.md`.
- **Customer discovery / KA:** additionally `customer-adoption-search.md`, `sales-deliverables.md`.
- **Food ingredients:** additionally `regulatory-audit.md`; Chinese or bilingual food deliverables additionally `food-terminology-and-language.md`.
- **Route-specific extras:** `product-format-screening.md` for every shortlisted application; `price-research.md`, `technical-validation.md`, `market-size-and-demand.md` when the corresponding question is decision-relevant; `market-awareness-and-education.md` only when awareness could change the decision; `research-quality-rules.md` before finalizing.

Support ingredients whose downstream applications are consumer products, including food and beverage, nutrition, beauty and personal care, household care, pet care, and similar categories. For industrial or intermediate-only materials, explain that the workflow is only partially applicable; adapt it only if the user accepts replacing consumer, retail, and brand modules with industry-specific demand and procurement analysis.

## Establish the Research Contract

Capture or state reasonable assumptions for:

- ingredient identity, synonyms, grade, function, and relevant claims;
- target geography, language, time window, and downstream scope;
- supplier capabilities and constraints that affect fit, including saleable grades, scale, target-jurisdiction authorizations, production-source restrictions, and available evidence or quality dossiers;
- business objective: explore applications, validate one category, find customers, or prepare an account plan;
- available public and user-authorized data sources;
- requested depth, deadline, and output language.

Ask only questions that would materially change scope. If answers are unavailable, proceed with explicit assumptions and label the resulting limitations. Match the user's language; support Chinese, English, or bilingual output. Do not duplicate the full report in two languages unless requested.

## Run the Feature-to-Market Chain

**Stage gating:** Stages 1–3 build the feasibility analysis. Run them only when your routing note requires a report — a general opportunity request, or a scoped request with no existing report. When the routing note lists only KA development or a sales artifact and a feasibility analysis already exists (this skill's prior output, an equivalent user-supplied analysis, or an archived case the user points to), start from that report: skip stages 1–3, do not re-search or re-derive properties, and produce only the requested piece.

Load references from your routing note at the step that needs them. When the condition for a module is absent, skip it and state the omission.

**Route-list-driven loads** (read from what your routing note lists, not from re-detecting the activity later):

- When your routing note lists **customer discovery** → read [customer-adoption-search.md](references/customer-adoption-search.md) and [sales-deliverables.md](references/sales-deliverables.md) before the customer step.
- When your routing note lists **KA development** → read [customer-adoption-search.md](references/customer-adoption-search.md) for account selection and [sales-deliverables.md](references/sales-deliverables.md) for the KA card workflow.
- When your routing note lists a **sales artifact** → read [sales-deliverables.md](references/sales-deliverables.md) and build the artifact from the existing report's evidence only.
- When your routing note lists only **market feasibility** → load none of the above; the conditional modules below apply as their conditions occur.

Before collecting evidence, read [evidence-and-sources.md](references/evidence-and-sources.md). For every feasibility or customer-discovery request, read [feature-application-adoption.md](references/feature-application-adoption.md).

Conditional modules (condition first, then the read):

- When current SKU adoption, competitor formulations, substitutes, claims, or potential-customer status can be checked through retail or marketplace labels → read [ecommerce-label-research.md](references/ecommerce-label-research.md).
- When identifying, verifying, or prioritizing potential customers → read [customer-adoption-search.md](references/customer-adoption-search.md) and apply its account-level sequence with a SKU-level audit trail for every shortlisted account.
- When the request is food-related → read [regulatory-audit.md](references/regulatory-audit.md); unless the user limits geography, audit China, the United States, and the European Union in one comparison table with category-specific use levels as separate rows.
- When price, cost, value in use, or commercial feasibility affects the decision → read [price-research.md](references/price-research.md).
- When an application, formulation, processing, shelf-life, sensory, efficacy, or experiment recommendation is discussed → read [technical-validation.md](references/technical-validation.md).
- When market size, demand volume, production, capacity, sales volume, market value, growth, TAM/SAM/SOM, supplier financial materiality, or shared-platform value affects the decision → read [market-size-and-demand.md](references/market-size-and-demand.md). When an opportunity claim depends on shortage, undersupply, low penetration, substitution potential, or proposed new capacity → run its supply-demand gap audit.
- For every shortlisted consumer-product application → read [product-format-screening.md](references/product-format-screening.md) and translate the application into concrete saleable product formats before estimating demand or selecting customers.
- When consumer recognition, ingredient-led communication, trust, claim comprehension, or education effort could materially change the application or go-to-market decision → read [market-awareness-and-education.md](references/market-awareness-and-education.md). It is an optional decision module, not a mandatory report section.
- When the deliverable is Chinese or bilingual food content → read [food-terminology-and-language.md](references/food-terminology-and-language.md) and run its target-language audit after the evidence and conclusions are fixed.
- Before finalizing every feasibility report → read [research-quality-rules.md](references/research-quality-rules.md), show whether each applicable rule is met, conditional, not met, or not applicable, and downgrade conclusions when evidence is insufficient.

### Stage 1: Establish Ingredient Properties

1. Normalize the ingredient identity, grade, purity, physical form, production route, and relevant synonyms.
2. Search original studies, standards, patents, and disclosed supplier studies for properties that could create downstream value.
3. Record each material property with its test system, dose, comparator, measured result, exact inline source, source locator, reading depth, limitations, and evidence level.
4. Separate supported properties, mechanistic or adjacent evidence, unsupported marketing claims, and adverse properties or failure modes.

Keep this stage limited to the ingredient's measured intrinsic, physicochemical, processing, sensory, biological, compatibility, safety, and analytical properties. Put finished-product application performance, replacement results, competitor comparison, and formulation strategy in the application deep dive, not in the property table.

A proposed application must trace back to a supported property or be labeled as a hypothesis.

### Stage 2: Map Properties to Applications and Apply Hard Gates

Map `ingredient property -> product problem -> required function -> candidate application`. For each candidate, test:

- **Need:** the product or user has an observable need for the property;
- **Regulation:** the exact ingredient identity and grade can plausibly be used in the target jurisdiction, product class, route, dose, and population;
- **Technical fit:** the ingredient remains compatible and functional under the target matrix, process, storage, and packaging conditions;
- **Use-amount feasibility:** distinguish the regulatory maximum or daily-intake boundary, literature/patent/supplier starting amount, proposed test amount, and commercially intended amount; verify that the intended finished-product amount is achievable;
- **Use cost:** calculate ingredient cost at the intended amount, yield and loss, then keep processing, compliance, testing, logistics, and claim costs separate;
- **Buyer visibility:** identifiable companies make or develop the relevant products.

After an application passes the first screen, map it to concrete product formats. For each format, test matrix/phase, process, contact or consumption mode, pack and dose basis, use amount, claim route, substitutes, current SKU adoption, format-level market pool and buyer set. Keep format retail value separate from ingredient-addressable volume.

For food applications, show China, United States, and European Union regulatory gates as separate columns in the property-to-application map. Give each jurisdiction an explicit `pass`, `conditional`, `fail`, or `unresolved` result with the decisive category, use condition, and source.

For novel, strain-specific, source-specific, or protected ingredients, verify that the supplier's exact product—not merely a same-named molecule—matches the authorization, specification, production source or strain, permitted uses, exclusivity or data-protection conditions, and required dossier.

For food ingredients, absence from one additive list is not prohibition: determine the applicable legal route, then report the exact permitted or excluded categories and use levels for China, the United States, and the European Union in one comparison table.

Classify each application as `advance`, `conditional—experiment required`, `regulatory unresolved`, `technical evidence insufficient`, or `do not advance`. State the failing gate and evidence for exclusions. Keep a small, decision-relevant shortlist rather than filling a preset count.

### Stage 3: Validate Market Adoption and Effects

For each shortlisted application, investigate:

- **Demand:** market direction, consumer need, growth signals, seasonality, and promotion dependence. Keep capacity, production, shipments, sales volume, consumption/demand volume, inventory and sales value as separate measures. When sizing the ingredient market, triangulate supply, trade and downstream-use evidence; a single interested party's estimate or an opaque report is not a verified market total. Classify demand maturity, supply constraint and evidence strength separately using [market-size-and-demand.md](references/market-size-and-demand.md).
- **Market awareness and education, when decision-relevant:** if the ingredient name, benefit explanation, trust, or claim comprehension could affect adoption, assess whether to lead with the ingredient, lead with the benefit, use professional education, or keep the ingredient behind the label. Otherwise omit this module or note it briefly.
- **Products:** representative brands/SKUs, formulation role, claims, format, pack size, price, sales signals, review themes, and launch activity.
- **Product formats:** compare concrete forms within each application and show why the ingredient is technically and commercially better suited to some forms than others. Use format-specific market data when available; if only a parent category total is reliable, allocate formats only with an evidence-supported share.
- **Competition:** for each application, compare the target ingredient with incumbent and credible alternative ingredient systems on a functionally equivalent basis; show each option's advantages, disadvantages, use-amount basis, process and product fit, cost-in-use, regulatory/label implications, evidence comparability, and switching barriers. When data permit, calculate the change in the replaced ingredient system's cost and the resulting change in estimated total ingredient cost for the finished product, keeping ingredient cost separate from manufacturing cost.
- **Replacement versus co-formulation:** decompose the incumbent system's product jobs, then use literature and application evidence to assess full replacement, partial replacement, complementary co-formulation, process-enabled change, retaining the incumbent, or a defined comparative experiment. A synergistic claim requires an appropriate additive/mixture benchmark and interaction evidence.
- **Value in use:** the economic or product value created for the buyer; separate known figures from cost assumptions.
- **Science and technical fit:** mechanism, formulation constraints, dosage or process considerations, human/field evidence where relevant, and evidence limitations.
- **Regulation and claims:** product classification, ingredient status, usage restrictions, claim boundaries, standards, and unresolved legal questions.
- **Route to market:** relevant manufacturers, brands, OEM/ODM partners, distributors, and buying process.

For leading companies and representative SKUs, classify adoption as `verified current use`, `development evidence`, `possible use`, `no public evidence found`, or `confirmed absent/discontinued`. Require product-level evidence for verified use.

Use a current label, ingredient list, filing, or equivalent SKU-level record to verify current use. Treat patents, supplier case studies, launch announcements, recruitment, distributor listings, search snippets, and company-level category fit as development or lead signals unless they identify a current commercial SKU and formulation. Disclose the company/SKU universe, channels, dates, and label-access coverage before interpreting negative search results.

Evaluate “how well it works” across five separate channels: finished-product technical performance; human/use outcomes and adverse effects; finished-product regulatory claim eligibility; consumer evidence; and commercial evidence. Apply the SMART evidence audit in [feature-application-adoption.md](references/feature-application-adoption.md) to consumer and commercial conclusions. Ingredient causality cannot be inferred from sales, ratings, reviews, brand claims, patents, or continued listing; a legally permitted claim is not proof of the claimed outcome.

Do not force every module when it is irrelevant. Explain omissions.

Before recommending an application or validation experiment:

1. verify ingredient identity and grade;
2. search original papers, patents, standards, and supplier application data for the exact product matrix and process;
3. distinguish direct application evidence from transfer by analogy;
4. identify likely failure modes and measurable response variables;
5. recommend only the smallest experiment needed to close a remaining decision-critical gap.

For every priority application, include traceable application cases and their reported use amounts when available. Preserve the original formulation denominator, process, control, outcome, source locator, and transferability. A single case, patent example, supplier formulation, or label presence is not a “typical use amount.”

An untested formulation is an experiment starting point, not a recipe. A patent proves disclosure, not independent performance or freedom to operate. Supplier trials are useful application evidence but remain commercially interested evidence.

## Identify Potential Customers

When requested, find the number of accounts the user specifies. If no number is given, choose a manageable list based on evidence coverage and state the selection rule. Use [sales-deliverables.md](references/sales-deliverables.md) for the customer table and KA workflow.

- Define an ideal customer profile from application fit, geography, product portfolio, innovation activity, regulatory readiness, scale, and accessible buying signals.
- Match accounts to the supplier's actual saleable grades, capacity, authorized jurisdictions, protected-use constraints, and evidence package before assigning priority. If these inputs are unknown, make account priority conditional rather than selecting a universal first target.
- Require account-specific evidence that the company makes, develops, or is likely to buy the relevant downstream product.
- Distinguish `verified current user`, `plausible buyer`, and `exploratory lead`. Never claim ingredient usage without direct evidence.
- Keep adoption status separate from account qualification: a company may be a plausible buyer while its current-use status is `no public evidence found`, `verified substitute user`, or `development evidence`.
- Include both current users with supplier-switch or second-source potential and non-users whose product needs strongly match supported ingredient properties.
- Use growth or momentum in the relevant business unit, category, brand, product family, geography, or channel as a priority modifier when it plausibly increases ingredient demand, project cadence, budget, or urgency. Treat company-wide growth as indirect unless the link is evidenced, disclose the metric and drivers, and do not let growth override technical, regulatory, supplier-fit, or access blockers.
- Prioritize by evidence-backed fit bands and stated rules, not opaque numerical scores.
- Identify likely buying roles by function. Name individuals only when supported by current public or user-provided evidence.

## Produce the Default Report

Always produce a Markdown feasibility report first unless the user already supplies an equivalent current analysis. Follow [feasibility-report-template.md](references/feasibility-report-template.md).

The report must:

- lead with a decision-relevant conclusion, not a generic market overview;
- separate facts, estimates, and hypotheses;
- attach an evidence level and source date to material claims;
- attach an inline citation to every ingredient-property row; a bibliography is optional as a consolidated list and is never the only citation;
- show what supports and what could invalidate each shortlisted application;
- trace every shortlisted application from a supported property through a product need and all applicable hard gates;
- show the concrete product-format screen for every shortlisted application, including matrix/process fit, use/contact pattern, format-level market evidence, current adoption, technical/regulatory barriers, and the format-specific validation needed;
- distinguish product-level adoption evidence from company-level relevance and separate technical, human/use and adverse-effect, regulatory-claim, consumer, and commercial signals;
- show the adoption-evidence class, observation date, SKU-level source, corroboration, and search coverage for every claimed current user or non-user;
- disclose whether decision-critical literature was read as full text, abstract only, review citation, patent example, or supplier material;
- include a normalized price-evidence table when price affects feasibility, clearly separating transactions, formal quotations, shipment-derived estimates, and public listings;
- include a market-size and demand audit when size or growth affects the conclusion, showing the exact metric, identity/grade, geography, period, unit, source method, source incentives, independent corroboration, calculation and uncertainty; output a range or `not reliably estimable` instead of false precision;
- include a supply-demand gap audit when shortage, low penetration, substitution, or capacity supports the opportunity conclusion; apply the gap-specific alignment fields in [market-size-and-demand.md](references/market-size-and-demand.md), report demand maturity, supply constraint and evidence status on separate axes, and state `not reliably estimable` when the required comparison cannot be aligned;
- include a use-amount and use-cost table for each priority application, with the formula, assumptions, source basis, range, unit-product cost, and sensitivity to price and amount;
- include a technical evidence matrix for priority applications and trace each proposed experiment to a documented evidence gap;
- avoid a model-authored opportunity grade or score;
- end with evidence gaps, validation actions, and decisions reserved for industry experts;
- identify the researched ingredient unambiguously at the start; use authoritative food, regulatory and scientific terminology and run a natural-Chinese editing pass, but do not add a terminology table to the report unless multiple names or translations could change identity, regulation, evidence transfer, or the decision;
- use the section and citation conventions in [feasibility-report-template.md](references/feasibility-report-template.md) so every report and example shares the same structure;
- end with the rule-based completeness check required by [research-quality-rules.md](references/research-quality-rules.md); do not call the report decision-ready while a decision-readiness blocker remains.

Create interview questions, KA cards, presentation outlines, or other artifacts only after the report, and only when requested.

When evaluating or revising this skill itself, use [test-scenarios.md](references/test-scenarios.md). Keep research-quality scoring separate from market-opportunity judgment; never turn the evaluation rubric into an ingredient opportunity score.

When improving an existing report or portfolio case, also read [case-improvement.md](references/case-improvement.md). Close decision-readiness blockers before optimizing rubric points or prose, preserve the original evidence boundary, and retain a before/after audit trail.
