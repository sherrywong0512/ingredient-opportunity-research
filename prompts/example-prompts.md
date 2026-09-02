# Example prompts

## China bakery ingredient

```text
Use $ingredient-opportunity-research to research isomalt in bakery products in China and identify ten potential customers.
Disambiguate it from isomaltulose. Produce the Markdown feasibility report first.
Audit China, US, and EU regulation; validate use amounts and gastrointestinal tolerability; compare the sweetener-system and estimated total ingredient-cost change where the recipe supports it.
```

## Broad consumer-product application scan

```text
使用 $ingredient-opportunity-research，调研结冷胶在消费品中的机会，并找出最开始应该攻坚的客户。
先区分高酰基和低酰基牌号，再从原料特性映射应用。比较MCC、CMC、卡拉胶等同场景方案；给出有来源的使用量、复配边界、法规条件和最小验证实验。
```

## Molecular-family ingredient

```text
Use $ingredient-opportunity-research to research global opportunities for human milk oligosaccharides and identify ten potential customers.
Keep each HMO molecule, production source, supplier authorization, dose, population, product class, and jurisdiction separate.
Produce the feasibility report first, then a conditional customer list based on the supplier's actual regulatory and technical package.
```

## Optional KA follow-up

```text
Using the completed feasibility report, create a KA attack card for [account].
Do not infer confidential projects, incumbent suppliers, purchase volume, satisfaction, or decision authority.
Show the account thesis, evidence gaps, likely functional roles, one value proposition, and a 30/60/90-day validation sequence.
```

## Scoped request: KA card only (no re-run)

```text
HMO 的市场可行性分析我已经有了（指向上一步产出或仓库示例 examples/03-hmo-global-market.md）。
请用 ingredient-opportunity-research 只做 KA 攻坚卡：基于已有报告证据，
选出最值得先攻坚的 1–2 个账户，给出账户论点、证据缺口、功能角色、
一个价值主张和 30/60/90 天验证序列。不要重新研究市场或重写报告。
```

```text
Use the ingredient-opportunity-research skill. I want the KA attack card for HMO
only — the feasibility analysis already exists (examples/03-hmo-global-market.md).
Base the card on that report's evidence; pick 1-2 accounts to attack first with
account thesis, evidence gaps, functional roles, one value proposition, and a
30/60/90-day validation sequence. Do not re-run market research or rewrite the report.
```
