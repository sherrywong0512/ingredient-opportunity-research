# Routing test B — group routing with decoy skills

**What this tests (ACES group-mode / routing-premium logic):** a fresh session sees three installed skill descriptions — A: `ingredient-opportunity-research` (the target), B: a project-due-diligence skill (decoy), C: a generic market-report generator (decoy) — and routes 3 requests. The question is whether the target skill over- or under-triggers when other skills are present.

## Skill descriptions shown (abridged, faithful)

- **A — ingredient-opportunity-research:** "Research market feasibility and downstream sales opportunities for ingredients and raw materials used in consumer products. Use when an ingredient sales team needs ... identify promising consumer-product applications ... investigate comparable market prices ... find and prioritize potential B2B customers ..."
- **B — project-due-diligence:** "Turn company screening and due-diligence materials about a potential partner, founder, or company into an admission judgment, evidence ledger, red lines, role restrictions, and items to verify before any collaboration decision ..."
- **C — generic-market-report-generator:** "Generate well-structured market research reports on any industry or topic ... general industry overview, trend report, or market landscape summary without naming a specific product, ingredient, or company under evaluation."

## Results

| # | Request | Chosen | Clearly correct |
|---|---|---|---|
| 1 | 评估 DermaBis-A95 在中国面部护肤市场机会并找客户 | **A** | Yes — ingredient task routes to the ingredient skill |
| 2 | 对越南水产饲料企业做尽调、判断是否值得合作 | **B** | Yes — company due-diligence routes away from the ingredient skill |
| 3 | 2026 全球宠物食品行业趋势与主要玩家 | **C** | Yes — generic trend overview, no named ingredient/company |

## Scores

- **Correct routing: 3/3.** The ingredient skill was selected for exactly the ingredient request and never for the due-diligence or generic-trend requests.
- **Over-triggering of the target skill: none.**
- **Under-triggering: none** (each request had a clearly matching skill).

## Reading

In a multi-skill workspace the ingredient skill neither monopolized nor missed its lane on this small probe: it was routed the ingredient request, ceded the company-evaluation request to the due-diligence skill, and ceded the generic industry-overview request to the generic generator. This is a single-session probe, not a statistical claim.

Raw auditor output: see [test-b-raw.md](test-b-raw.md).
