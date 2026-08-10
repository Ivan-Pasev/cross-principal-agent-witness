from __future__ import annotations

import csv
import json
from pathlib import Path

from scenarios import build_scenarios
from witness.evaluator import evaluate
from witness.metrics import aggregate, score
from witness.profiles import PROFILES, ablate


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def evaluate_profile(name, profile, scenarios):
    per_scenario = []
    for scenario in scenarios:
        ev = evaluate(scenario, profile)
        metrics = score(scenario, ev)
        row = {"profile": name, "scenario": scenario.scenario_id, **metrics}
        per_scenario.append(row)
    return per_scenario, aggregate([{k: v for k, v in r.items() if k not in {"profile", "scenario"}} for r in per_scenario])


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    scenarios = build_scenarios()
    all_rows = []
    summary = {}

    for name, profile in PROFILES.items():
        rows, agg = evaluate_profile(name, profile, scenarios)
        all_rows.extend(rows)
        summary[name] = agg

    full = PROFILES["W"]
    ablation_summary = {}
    for primitive in ["identity", "provenance", "delegation_scope", "commitment", "revocation", "outcome"]:
        profile = ablate(full, primitive)
        rows, agg = evaluate_profile(profile.name, profile, scenarios)
        all_rows.extend(rows)
        metric_contributions = {
            metric: summary["W"][metric] - agg[metric]
            for metric in summary["W"]
            if metric != "composite"
        }
        ablation_summary[primitive] = {
            "composite_without": agg["composite"],
            "evidence_contribution": summary["W"]["composite"] - agg["composite"],
            "metric_contributions": metric_contributions,
        }

    csv_path = RESULTS / "delegation_escape_metrics.csv"
    fieldnames = list(all_rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    output = {
        "prototype_status": "PIPELINE_VALIDATED",
        "scientific_hypothesis": "NOT_ESTABLISHED",
        "scenario_count": len(scenarios),
        "profile_summary": summary,
        "ablation_summary": ablation_summary,
    }
    (RESULTS / "delegation_escape_summary.json").write_text(json.dumps(output, indent=2), encoding="utf-8")

    print("Cross-Principal Agent Witness — Delegation Escape 001")
    print(f"Scenarios: {len(scenarios)}")
    for name in PROFILES:
        s = summary[name]
        print(f"{name}: composite={s['composite']:.3f}, authority_edge={s['authority_edge_localization']:.3f}, principal_chain={s['principal_chain_reconstruction']:.3f}")
    print("Ablation evidence contributions (prototype composite):")
    for primitive, values in ablation_summary.items():
        print(f"  {primitive}: {values['evidence_contribution']:+.3f}")
    print("STATUS: PIPELINE_VALIDATED")
    print("SCIENTIFIC_HYPOTHESIS: NOT_ESTABLISHED")


if __name__ == "__main__":
    main()
