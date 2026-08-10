import os
import json
import sys

def generate_results():
    with open("results/delegation_escape_summary.json", "r") as f:
        data = json.load(f)
        
    p = data["profile_summary"]
    a = data["ablation_summary"]
    
    md = f"""# Results

This document is automatically generated from the canonical machine-readable results.

## Primary Interpretable Metrics (R1)
The following tables separate execution attribution, authority edge localization, and principal chain reconstruction. These represent the primary scientific measurement of the instrument.

### Profile Summary
| Profile | Incident Acc | Exec Attr | Auth Edge Loc | Princ Chain Recon | Comm Loc | Revoc Loc |
|---|---|---|---|---|---|---|
| **B0** | {p['B0']['incident_accuracy']:.3f} | {p['B0']['execution_attribution']:.3f} | {p['B0']['authority_edge_localization']:.3f} | {p['B0']['principal_chain_reconstruction']:.3f} | {p['B0']['commitment_localization']:.3f} | {p['B0']['revocation_localization']:.3f} |
| **B1** | {p['B1']['incident_accuracy']:.3f} | {p['B1']['execution_attribution']:.3f} | {p['B1']['authority_edge_localization']:.3f} | {p['B1']['principal_chain_reconstruction']:.3f} | {p['B1']['commitment_localization']:.3f} | {p['B1']['revocation_localization']:.3f} |
| **B2** | {p['B2']['incident_accuracy']:.3f} | {p['B2']['execution_attribution']:.3f} | {p['B2']['authority_edge_localization']:.3f} | {p['B2']['principal_chain_reconstruction']:.3f} | {p['B2']['commitment_localization']:.3f} | {p['B2']['revocation_localization']:.3f} |
| **B3** | {p['B3']['incident_accuracy']:.3f} | {p['B3']['execution_attribution']:.3f} | {p['B3']['authority_edge_localization']:.3f} | {p['B3']['principal_chain_reconstruction']:.3f} | {p['B3']['commitment_localization']:.3f} | {p['B3']['revocation_localization']:.3f} |
| **B4** | {p['B4']['incident_accuracy']:.3f} | {p['B4']['execution_attribution']:.3f} | {p['B4']['authority_edge_localization']:.3f} | {p['B4']['principal_chain_reconstruction']:.3f} | {p['B4']['commitment_localization']:.3f} | {p['B4']['revocation_localization']:.3f} |
| **W**  | {p['W']['incident_accuracy']:.3f} | {p['W']['execution_attribution']:.3f} | {p['W']['authority_edge_localization']:.3f} | {p['W']['principal_chain_reconstruction']:.3f} | {p['W']['commitment_localization']:.3f} | {p['W']['revocation_localization']:.3f} |

## Secondary Instrumentation
The composite score is a secondary instrumentation diagnostic designed to track overall pipeline progression. **It is not the primary scientific endpoint**.

| Profile | Composite |
|---|---|
| **B0** | {p['B0']['composite']:.3f} |
| **B1** | {p['B1']['composite']:.3f} |
| **B2** | {p['B2']['composite']:.3f} |
| **B3** | {p['B3']['composite']:.3f} |
| **B4** | {p['B4']['composite']:.3f} |
| **W**  | {p['W']['composite']:.3f} |
"""
    return md

def main():
    md = generate_results()
    if "--check" in sys.argv:
        if not os.path.exists("docs/RESULTS.md"):
            print("docs/RESULTS.md does not exist.")
            sys.exit(1)
        with open("docs/RESULTS.md", "r", encoding="utf-8") as f:
            current = f.read()
        if current != md:
            print("docs/RESULTS.md is stale. Please regenerate it.")
            sys.exit(1)
        print("docs/RESULTS.md is fresh.")
    else:
        with open("docs/RESULTS.md", "w", encoding="utf-8") as f:
            f.write(md)
        print("Regenerated docs/RESULTS.md.")

if __name__ == "__main__":
    main()
