#!/usr/bin/env python3
"""Recompute ACES-style Skill Lift, CIs and static-vs-live correlations.

Reads evaluation/aces/scores.csv (one row per output) and reports, per the
protocol in evaluation/aces/protocol.md:

- per-case condition means per metric, and per-case Skill Lift
  (with-skill mean minus baseline mean) for each metric;
- composite lift (mean of six metric lifts per case) and outcome-only lift
  (mean of accuracy and goal-accuracy lifts), with 95% normal CIs over
  per-case deltas (descriptive; cases are clustered, not independent);
- the distribution of per-case composite lift (positive / zero / negative);
- static-vs-live Spearman correlations (rubric total vs behavior_check and
  vs composite) across all outputs;
- hard-failure counts per condition.

Dependency-free, matching the repo's other analysis scripts.
"""

from collections import defaultdict
import csv
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parents[1]
SCORES = ROOT / "evaluation" / "aces" / "scores.csv"

METRICS = [
    "security",
    "skill_execution",
    "skill_efficiency",
    "accuracy",
    "goal_accuracy",
    "behavior_check",
]


def mean(values):
    return statistics.mean(values) if values else float("nan")


def spearman(xs, ys):
    """Spearman rank correlation (dependency-free)."""
    n = len(xs)
    if n < 3:
        return float("nan")
    order_x = {v: i for i, v in enumerate(sorted(xs))}
    order_y = {v: i for i, v in enumerate(sorted(ys))}
    rx = [order_x[v] for v in xs]
    ry = [order_y[v] for v in ys]
    mx, my = mean(rx), mean(ry)
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    vx = sum((a - mx) ** 2 for a in rx)
    vy = sum((b - my) ** 2 for b in ry)
    if vx == 0 or vy == 0:
        return float("nan")
    return cov / (vx * vy) ** 0.5


def ci95(values):
    """95% normal CI (mean ± 1.96 * sem) over a list of per-case deltas."""
    n = len(values)
    if n < 2:
        return float("nan"), float("nan")
    m = mean(values)
    sd = statistics.stdev(values)
    half = 1.96 * sd / (n ** 0.5)
    return m - half, m + half


def main():
    with SCORES.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise SystemExit("scores.csv is empty")

    # per (case, condition) means per metric
    grouped = defaultdict(lambda: defaultdict(list))
    rubric_by_output = {}
    hard_by_condition = defaultdict(int)
    for row in rows:
        case, cond = row["case"], row["condition"]
        for m in METRICS:
            grouped[(case, cond)][m].append(float(row[m]))
        rubric_by_output[(case, row["response"])] = (
            float(row["rubric_total"]) if row.get("rubric_total") not in (None, "") else float("nan")
        )
        if row.get("hard_failure", "").strip() == "1":
            hard_by_condition[cond] += 1

    cases = sorted({row["case"] for row in rows})
    print(f"Cases: {len(cases)}  Outputs: {len(rows)}")
    print(f"Hard failures by condition: {dict(hard_by_condition) or 'none'}")
    print()

    # per-case lift per metric
    case_lift = {}
    for case in cases:
        skill = grouped[(case, "Skill")]
        direct = grouped[(case, "Direct")]
        lift = {}
        for m in METRICS:
            lift[m] = mean(skill[m]) - mean(direct[m])
        lift["composite"] = mean([lift[m] for m in METRICS])
        lift["outcome_only"] = (lift["accuracy"] + lift["goal_accuracy"]) / 2.0
        case_lift[case] = lift

    # headline table
    print("Per-case Skill Lift (with-skill mean minus baseline mean):")
    header = f"{'case':<18}" + "".join(f"{m:>16}" for m in METRICS) + f"{'composite':>12}{'outcome':>10}"
    print(header)
    print("-" * len(header))
    for case in cases:
        lift = case_lift[case]
        cells = "".join(f"{lift[m]:>16.3f}" for m in METRICS)
        print(f"{case:<18}{cells}{lift['composite']:>12.3f}{lift['outcome_only']:>10.3f}")
    print()

    comp = [case_lift[c]["composite"] for c in cases]
    outc = [case_lift[c]["outcome_only"] for c in cases]
    lo, hi = ci95(comp)
    print(f"Overall composite lift: {mean(comp):.4f}  95% CI [{lo:.4f}, {hi:.4f}]  (n={len(comp)} cases)")
    lo, hi = ci95(outc)
    print(f"Overall outcome-only lift: {mean(outc):.4f}  95% CI [{lo:.4f}, {hi:.4f}]  (n={len(outc)} cases)")

    pos = sum(1 for v in comp if v > 0)
    zero = sum(1 for v in comp if v == 0)
    neg = sum(1 for v in comp if v < 0)
    print(f"Composite-lift distribution: {pos} positive, {zero} zero, {neg} negative (per case)")

    print("\nMean lift by metric (across cases):")
    for m in METRICS + ["composite", "outcome_only"]:
        vals = [case_lift[c][m] for c in cases]
        posn = sum(1 for v in vals if v > 0)
        print(f"  {m:<16} {mean(vals):.4f}   positive in {posn}/{len(vals)} cases")

    # static vs live correlation (per output)
    outputs = [(row["case"], row["response"]) for row in rows]
    rubric_vals = [rubric_by_output[k] for k in outputs]
    bc_vals = [float(row["behavior_check"]) for row in rows]
    comp_vals = []
    for row in rows:
        comp_vals.append(mean([float(row[m]) for m in METRICS]))
    acc_vals = [float(row["accuracy"]) for row in rows]

    pairs = [(r, b) for r, b in zip(rubric_vals, bc_vals) if r == r and b == b]
    if len(pairs) >= 3:
        rho_bc = spearman([p[0] for p in pairs], [p[1] for p in pairs])
        print(f"\nStatic-vs-live (per output, n={len(pairs)}):")
        print(f"  Spearman(rubric_total, behavior_check) = {rho_bc:.3f}")
    pairs_c = [(r, c) for r, c in zip(rubric_vals, comp_vals) if r == r and c == c]
    if len(pairs_c) >= 3:
        rho_c = spearman([p[0] for p in pairs_c], [p[1] for p in pairs_c])
        print(f"  Spearman(rubric_total, composite)       = {rho_c:.3f}")
    pairs_a = [(r, a) for r, a in zip(rubric_vals, acc_vals) if r == r and a == a]
    if len(pairs_a) >= 3:
        rho_a = spearman([p[0] for p in pairs_a], [p[1] for p in pairs_a])
        print(f"  Spearman(rubric_total, accuracy)        = {rho_a:.3f}")


if __name__ == "__main__":
    main()
