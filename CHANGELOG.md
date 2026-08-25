# Changelog

All notable changes to this repository are recorded here. The version in this
changelog tracks the skill's own frontmatter `version` field
(`skill/ingredient-opportunity-research/SKILL.md`).

### Added

- DeepSeek cross-model replication of the one-sentence benchmark (`evaluation/minimal-prompt-benchmark/deepseek/`): six fresh sessions, anonymized outputs, separate blind reviewer, scores and group key. Result is a retained null-to-mixed finding: no overall Skill advantage on DeepSeek (96.8 vs 96.6, Direct more stable); Skill-led only on MycoPro-PV9 capacity-conversion separation.
- `install.sh` (one-command install) and a repo-level discovery copy at `.agents/skills/` so cloning the repo auto-exposes the skill in Codex / Kimi Code / DeepSeek Harness.
- README: clone-and-use quickstart, per-platform install/invocation table, degraded-mode section for agents without web/PDF tools.

### Changed

- README Install section rewritten around the discovery-root model (clone alone is not enough; repo ships a discovery copy).
- Main README evaluation table and honest-limitations paragraph updated with the DeepSeek null result.

### Added

- README synced to PRD v1.2: current-phase statement, north-star metric (expert-agreed decision-blocker recall), preregistered next-validation gates, roadmap (v1.x/v2/v3), and non-goal boundaries; both English and Chinese READMEs updated.
- zh README: DeepSeek cross-model section and corrected clone-and-use install statement.

### Changed

- docs/README.zh.md install section corrected: cloning the repo now auto-exposes the skill (repo ships .agents/skills discovery copy); install needed only for other projects.

## [1.2.0] - 2026-08-23

### Added

- Explicit `version` and `updated` fields in the skill frontmatter; versioned behavior is now pinned and auditable.
- `scripts/validate_report.py`: dependency-free structural validator for generated feasibility reports (executive conclusion first, E1–E5 evidence levels, inline citations, no model-authored opportunity score, evidence-gap/completeness section, CN/US/EU audit for food, supply–demand gap audit on shortage claims). Wired into CI via `--examples`.
- `examples/00-minimal-evidence-demo.md`: compact synthetic format demo showing the core table formats and evidence-boundary rules.
- `examples/README.md`: index with versions and dates for all examples.
- `CHANGELOG.md` (this file) and `LICENSE` (MIT).

### Changed

- `references/food-terminology-and-language.md` expanded from 35 to ~130 lines: identity traps (family vs molecule vs salt vs source/strain), cross-jurisdiction terminology (GB 2760 / 21 CFR / EU 1333/2008), false friends and literal-translation traps, units and denominators, transliteration policy, and an extended bilingual final-audit checklist.
- `README.md` rewritten in English as the primary landing page; the full Chinese narrative moved to `docs/README.zh.md`.
- `scripts/validate_project.py`: registers the new docs/examples/scripts files, skips `examples/README.md` in the report-content check, and checks both language READMEs.

### Fixed

- Skill behavior previously drifted silently across copies; versioning plus the repo validators now make drift detectable.

## [1.1.0] - 2026-08-20

- Direct-vs-Skill benchmark merged (minimal-prompt-benchmark): 3 preregistered synthetic cases, 3 fresh sessions per condition, 18 anonymized outputs. Skill mean 95.0 (min 87, SD 4.7, range 13) vs Direct mean 85.7 (min 60, SD 11.4, range 40); no hard failures; headline decision unchanged.
- Structured calibration added (three-case-comparison): Direct 283/300, Skill 298/300.
- Controlled-test, iteration-log and case-audit consolidated; `scripts/analyze_minimal_benchmark.py` added.

## [1.0.0] - 2026-08-16

- Initial public release of the skill and repository structure.
