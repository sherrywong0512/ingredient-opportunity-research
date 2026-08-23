# Ingredient Opportunity Research

An evidence-led AI research skill for ingredient and raw-material teams: turn fragmented market information into an auditable feasibility report and downstream customer-development actions **before** committing to process development, capacity build-out, or market entry.

Full Chinese narrative (product thinking, case audits, iteration history): [docs/README.zh.md](docs/README.zh.md) · Product requirements: [docs/PRD.md](docs/PRD.md) · Design decisions: [docs/product-case-study.md](docs/product-case-study.md) · Change log: [CHANGELOG.md](CHANGELOG.md)

## What it does

- locks the exact ingredient identity (name, grade, source, strain, jurisdiction) and separates it from similarly named substances;
- traces every proposed application back to a measured property or labels it a hypothesis — never starts from a category list and retrofits benefits;
- applies hard gates (need, regulation, technical fit, use amount, use cost, buyer visibility) before any application advances;
- audits **China, the United States and the European Union as separate columns** for food ingredients, preserving category-specific use levels;
- maps applications to concrete saleable product formats — "bakery", "beverage" or "soothing skincare" is not a format;
- verifies current adoption at SKU level (current label/ingredient list/filing) and keeps adoption status separate from buyer qualification;
- separates price signals (transactions, quotations, shipment estimates, public listings), ingredient cost from manufacturing cost, and legal permission from demonstrated effect;
- runs a supply–demand gap audit whenever an opportunity claim depends on shortage or undersupply;
- forbids a model-authored opportunity grade; outputs `not reliably estimable` instead of false precision;
- ends with evidence gaps, the smallest next validation experiments, and decisions reserved for industry experts.

## Evidence discipline

Every material claim carries an evidence level (E1–E5) and an inline, retrievable source. The level describes the evidence, not how attractive the opportunity is. Supplier marketing, patents, reviews and company statements are labeled as interested evidence; sales, ratings and continued listing never prove ingredient causality. If the required comparison cannot be aligned, the report says so.

## Install

**Cloning this repository alone does not expose the skill** in every project, but the repo ships a discovery copy at `.agents/skills/ingredient-opportunity-research/` — so **if you work inside this repo with Codex, Kimi Code, or DeepSeek Harness, the skill is auto-discovered with zero install**. To use it in *other* projects, install it globally:

### Quickstart after cloning

```bash
git clone <this-repo>
cd ingredient-opportunity-research
# Inside this repo: already usable (auto-discovered from .agents/skills/).
# For other projects:
./install.sh --codex     # personal Codex install, usable in every project
# or ./install.sh --all       codex + repo-level + claude
```

Then, in any Codex session (this repo, or any project after a global install), say:

```text
Use the ingredient-opportunity-research skill. Research the market opportunity
for <ingredient> in <geography/application area>. Output a feasibility report
first, then identify <N> evidence-backed potential customers.
```

### Platform install paths

| Platform | Install location | How the skill is invoked |
|---|---|---|
| Codex (personal) | `~/.codex/skills/ingredient-opportunity-research/` | Auto from task description; or say "use the ingredient-opportunity-research skill" |
| Codex / Kimi Code / DeepSeek Harness (repo-level) | `<project>/.agents/skills/ingredient-opportunity-research/` | Auto-discovery from the skill description; also honored by tools that scan `.agents/skills` |
| Claude Code | `<project>/.claude/skills/ingredient-opportunity-research/` | Auto from task description; or `/skill` / name the skill explicitly |
| Kimi Code (personal) | `~/.kimi-code/skills/` (or `~/.agents/skills/`) | `/skill:ingredient-opportunity-research` |
| Kimi Work (desktop/cloud) | Import via its custom-skill / document-to-skill flow | Use a shorter name such as `ingredient-opportunity` (its name limit) |
| DeepSeek Harness (project) | `<project>/.dsh/skills/ingredient-opportunity-research/` | Auto from task description (scans `.dsh/skills` and `.agents/skills`) |

```bash
# Manual copy equivalents
cp -R skill/ingredient-opportunity-research ~/.codex/skills/        # Codex personal
cp -R skill/ingredient-opportunity-research .agents/skills/         # repo-level (Codex/Kimi/DSH)
cp -R skill/ingredient-opportunity-research .claude/skills/         # Claude Code
cp -R skill/ingredient-opportunity-research .dsh/skills/            # DeepSeek Harness
```

Requires the agent to have web research, file and PDF tools; the skill defines the workflow, it does not bundle tools. After install, ask the agent to confirm it loaded `references/evidence-and-sources.md` before starting — the reference protocols are what make the output evidence-traceable.

### Degraded mode (limited or no web/PDF tools)

If the agent lacks web research or PDF access, the workflow still runs but degrades honestly instead of inventing precision:

- uses the public-source fallback in `references/evidence-and-sources.md` — official product pages, marketplaces, filings, job postings and interviews — instead of paid databases;
- lowers evidence levels (E3–E5, or 已验证→推断→待验证) and labels gaps as `not reliably estimable`;
- lists exactly what could not be verified, so the reader knows which conclusions to distrust;
- never fabricates a source, price, quote, or SKU to fill a gap.

## Usage

Invoke it by describing the task; the model matches the skill from its description. You can also name it explicitly.

```text
Use the ingredient-opportunity-research skill. Research the market opportunity
for <ingredient> in <geography/application area>. Output a feasibility report
first, then identify <N> evidence-backed potential customers.
```

The default output is a Markdown feasibility report. Customer lists, interview guides, key-account cards and presentation outlines are produced only on request, after the report exists. Languages: Chinese, English, or bilingual. More reproducible requests: [prompts/example-prompts.md](prompts/example-prompts.md).

## Examples

| Example | What it exercises | Status |
|---|---|---|
| [00 – Minimal evidence demo](examples/00-minimal-evidence-demo.md) | Core table formats (synthetic, for format reference) | Format demo, not real research |
| [01 – Isomalt, China bakery](examples/01-isomalt-china-bakery.md) | Identity confusion, tolerance risk, use cost, 10 exploratory accounts | Internal self-audit 82/100; not decision-ready |
| [02 – Gellan gum, consumer products](examples/02-gellan-gum-consumer-products.md) | HA/LA grades, beverage regulation, substitute systems, account priority | Internal self-audit 72/100 |
| [03 – HMO, global market](examples/03-hmo-global-market.md) | Molecule family, strain/source authorizations, consumer education, routing | Internal self-audit 68/100 |
| [04 – Bisabolol, China skincare](examples/04-bisabolol-china-skincare.md) | Product-format screen, market demand audit, penetration risk, adoption | Pre-audit; not scored |

Low scores are a product feature: they tell the user where inference must stop and what to buy, ask or experiment next. Index with versions and dates: [examples/README.md](examples/README.md).

## Evaluation (what the repo proves — and does not)

The repo separates structural checks from effect claims:

| Layer | Question | Current evidence | Proves | Does not prove |
|---|---|---|---|---|
| Structural | Is the skill complete, are links valid, do reports honor the contract? | `python3 scripts/validate_project.py` + `python3 scripts/validate_report.py` | File and output contracts are executable | Factual accuracy or business value |
| Case audit | Does the workflow expose identity, regulatory, technical, adoption and price gaps? | Isomalt 82, Gellan 72, HMO 68 self-audits | Gaps are visible and reported | Expert or market validation |
| One-sentence repeat | Does the skill stabilize coverage when the user only says one sentence? | 3 preregistered synthetic cases × 3 fresh sessions each | Skill mean 95.0 vs Direct 85.7; lower within-case range and SD; no hard failures | Industry endorsement, real-market accuracy, cross-model generality |
| Cross-model check | Does the same benchmark hold on a second model family? | DeepSeek replication, same fixtures and rubrics | No overall Skill advantage: 96.8 vs 96.6, Direct more stable; Skill-led on MycoPro-PV9 only | Universal advantage; real-world decisions or ROI |
| Structured calibration | Same frozen evidence pack, Direct vs Skill | 3-case controlled comparison | Direct 283/300, Skill 298/300 | Real-world decisions or ROI |

Details, protocols, anonymized raw outputs and scores: [minimal-prompt-benchmark](evaluation/minimal-prompt-benchmark/README.md) · [three-case-comparison](evaluation/three-case-comparison/README.md) · [case-audit](evaluation/case-audit.md) · [iteration-log](evaluation/iteration-log.md).

Honest limitations: benchmark cases are synthetic and designed around known failure modes; blind review was done by the same model family, not by industry experts; group-key mappings were not hash-committed before scoring; a DeepSeek cross-model replication did **not** reproduce the Skill's overall advantage (96.8 vs 96.6, Direct more stable), so the skill's measured benefit is model-dependent and dimension-specific; and there is no evidence yet of real sales, project-approval or ROI improvement. The strongest supported claim is narrow: in these three synthetic cases on the original model family, a one-sentence request plus the skill produced more complete and more stable decision-framework outputs than direct generation — it did not change the headline investment recommendation, and it did not generalize to an overall mean advantage on DeepSeek.

## Repository structure

```text
.
├── skill/ingredient-opportunity-research/  # the installable skill (SKILL.md + references/)
├── docs/                                   # PRD, product case study, Chinese README
├── examples/                               # five evidence-boundary examples (00–04)
├── evaluation/                             # case audit, iteration log, controlled tests, benchmark
├── prompts/                                # reproducible invocation examples
├── scripts/                                # dependency-free validators and statistics
└── .github/workflows/validate.yml          # CI
```

## Boundaries

- public sources cannot prove confidential formulas, supplier relationships, contract prices or buying intent;
- a legally permitted ingredient is not proof of a finished-product claim;
- a label proves presence, not dosage, causal efficacy or commercial effect;
- patents and supplier application data are experiment starting points, not production recipes;
- all regulatory, price, SKU and company information must be refreshed before commercial use;
- this project supports expert decisions; it does not replace regulatory, formulation, procurement or business owners.

## License

MIT — see [LICENSE](LICENSE).
