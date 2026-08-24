# Routing test A — trigger precision and recall

**What this tests (ACES discovery / trigger-simulation logic):** a fresh session sees only the skill's public description and decides, for 9 requests, whether the skill should be triggered. 6 requests are in-scope ingredient requests (1–5, 9); 3 are out-of-scope (6–8).

**Skill description used (verbatim frontmatter `description`):**

> Research market feasibility and downstream sales opportunities for ingredients and raw materials used in consumer products. Use when an ingredient sales team needs to identify promising consumer-product applications, investigate comparable market prices, validate formulation and process feasibility with papers or patents, assess demand, competition, regulation, consumer awareness and market-education burden, find and prioritize potential B2B customers, or prepare optional interview guides, key-account plans, and presentation outlines. Supports professionally edited Chinese, English, and bilingual deliverables.

## Results

| # | Request | Trigger | Reason |
|---|---|---|---|
| 1 | 异麦芽酮糖醇 · 中国烘焙 · 10 个潜在用户 | YES | Ingredient feasibility + B2B customer identification |
| 2 | 结冷胶 · 消费品机会 · 攻坚客户 | YES | Application opportunity + downstream customer prioritization |
| 3 | 圆柚酮 · 市场机会 | YES | Core ingredient opportunity use case |
| 4 | HMO · 全球市场 · 10 customers | YES | Demand/market research + customer identification |
| 5 | 合成生物 Omega-3 · 供需 gap | YES | Demand-and-supply assessment for an ingredient |
| 6 | AI 宠物医疗 SaaS 项目评估 | NO | Project/startup viability, not ingredient research |
| 7 | React 组件测试补全 | NO | Coding task |
| 8 | 越南水产饲料企业融资尽调 | NO | Corporate financing/ownership due diligence |
| 9 | 海藻酸钠在植物肉里的成本 | YES | Comparable ingredient price for a consumer formulation |

## Scores

- **Recall (should-trigger → YES):** 6/6 (100%) — no under-triggering on the in-scope requests.
- **Precision (should-not-trigger → NO):** 3/3 (100%) — no over-triggering on the out-of-scope requests (project evaluation, coding, company due-diligence).
- **UNSURE:** none.

## Reading

The skill's trigger description routes cleanly on this small set: full recall on ingredient market/price/customer requests and zero false triggers on project-evaluation, coding and company-due-diligence requests. The description's explicit consumer-products scope is what keeps the coding and SaaS requests out; the "ingredient sales team" framing is what keeps the due-diligence request out. This is a small single-session probe, not a statistical claim.

Raw auditor output: see [test-a-raw.md](test-a-raw.md).
