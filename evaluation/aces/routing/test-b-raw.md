# Raw auditor output — routing test B (group routing with decoys)

Single fresh session; no browsing; only the three skill descriptions were provided (skills A/B/C as documented in [test-b-group-routing.md](test-b-group-routing.md); none was loaded or executed).

| # | Request | Skill chosen | Reason |
|---|---|---|---|
| 1 | 请评估 DermaBis-A95 在中国面部护肤市场的机会，并找出第一批应该拜访的客户。 | **A** | DermaBis-A95 是发酵来源的 bisabolol 原料（ingredient），请求要求评估其在消费产品（面部护肤）中的市场可行性与机会，并找出/排序首批 B2B 客户——与 A 的描述（下游应用、市场可行性、客户挖掘、拜访清单）逐点吻合。 |
| 2 | 对这家越南水产饲料企业做尽调，判断是否值得合作，并列出会前要核验的事项。 | **B** | 针对一家具体公司做合作前尽调，要求转化为"是否值得合作"的判断并列出会前待核验项——正是 B 的用途（准入判断、待核验项、会前研究）。A 处理的是原料机会，不处理公司合作判断。 |
| 3 | 给我讲讲 2026 年全球宠物食品行业的趋势和主要玩家。 | **C** | 未指名具体原料、产品或公司做评估，属于一般行业趋势/市场格局概述——C 的唯一匹配（行业概览、趋势报告、市场景观摘要）。 |

Per-request correctness: 1 → clearly correct (A); 2 → clearly correct (B); 3 → clearly correct (C; only arguably ambiguous if one insists the user say "report", but C's description explicitly covers industry overviews/trend reports). Over-triggering check: none — A was chosen only for the ingredient request; no non-ingredient request was routed to A; B and C each hit only their own scenario.
