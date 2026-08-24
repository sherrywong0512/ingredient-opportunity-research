# Routing tests (ACES discovery / group-mode adaptation)

ACES distinguishes a skill's **content contribution** from its **discovery-and-routing contribution**: does the agent find the skill when asked a relevant question, and does it pick the right skill when other skills are present? These probes test the skill's trigger description, the artifact-level routing surface.

| Test | Question | Result | File |
|---|---|---|---|
| A — trigger precision/recall | Does the skill's description trigger on in-scope requests and stay silent on out-of-scope ones? | Recall 6/6, precision 3/3, no UNSURE | [test-a-discovery.md](test-a-discovery.md) |
| B — group routing with decoys | With two decoy skills installed, does the ingredient request route to this skill and other requests away from it? | 3/3 correct, no over-triggering | [test-b-group-routing.md](test-b-group-routing.md) |

Both are single-session probes on a small request set, not statistical claims. Re-run on model or harness updates, or when the frontmatter `description` changes — the description is the routing surface this skill exposes.
