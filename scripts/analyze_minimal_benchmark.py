#!/usr/bin/env python3
"""Recompute descriptive minimal-prompt benchmark metrics from scores.csv."""

from collections import defaultdict
import csv
from pathlib import Path
import statistics


ROOT = Path(__file__).resolve().parents[1]
SCORES = ROOT / "evaluation" / "minimal-prompt-benchmark" / "scores.csv"


def summarize(values: list[int]) -> dict[str, float]:
    return {
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
        "range": max(values) - min(values),
        "pstdev": statistics.pstdev(values),
    }


with SCORES.open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))

if len(rows) != 18:
    raise SystemExit(f"expected 18 responses, found {len(rows)}")

grouped: dict[tuple[str, str], list[tuple[int, int]]] = defaultdict(list)
overall: dict[str, list[int]] = defaultdict(list)
for row in rows:
    if row["hard_failure"] != "false":
        raise SystemExit("published no-hard-failure result conflicts with scores.csv")
    score = int(row["total"])
    grouped[(row["case"], row["condition"])].append((int(row["run"]), score))
    overall[row["condition"]].append(score)

for key, run_scores in grouped.items():
    if len(run_scores) != 3 or sorted(run for run, _ in run_scores) != [1, 2, 3]:
        raise SystemExit(f"expected runs 1-3 for {key}, found {run_scores}")

print("| Case | Condition | Scores | Mean | Median | Min | Max | Range | Pop SD |")
print("|---|---|---|---:|---:|---:|---:|---:|---:|")
for case in ("FermaDHA-X", "MycoPro-PV9", "DermaBis-A95"):
    for condition in ("Direct", "Skill"):
        values = [score for _, score in sorted(grouped[(case, condition)])]
        stats = summarize(values)
        print(
            f"| {case} | {condition} | {'/'.join(map(str, values))} | "
            f"{stats['mean']:.1f} | {stats['median']:.1f} | "
            f"{stats['min']:.0f} | {stats['max']:.0f} | "
            f"{stats['range']:.0f} | {stats['pstdev']:.1f} |"
        )

print()
print("| Overall | Condition | Mean | Median | Min | Max | Range | Pop SD |")
print("|---|---|---:|---:|---:|---:|---:|---:|")
for condition in ("Direct", "Skill"):
    stats = summarize(overall[condition])
    print(
        f"| 9 outputs | {condition} | {stats['mean']:.1f} | "
        f"{stats['median']:.1f} | {stats['min']:.0f} | "
        f"{stats['max']:.0f} | {stats['range']:.0f} | "
        f"{stats['pstdev']:.1f} |"
    )
