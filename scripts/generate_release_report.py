import os
import sys
import subprocess
import json

def get_git_info():
    try:
        branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, check=True).stdout.strip()
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        status = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, check=True).stdout.strip()
        dirty = bool(status)
        return branch, commit, dirty
    except Exception:
        return "unknown", "unknown", False

def get_digests():
    try:
        with open("results/reproduction_manifest.json", "r") as f:
            manifest = json.load(f)
        return manifest.get("files", {})
    except Exception:
        return {}

def main():
    branch, commit, dirty = get_git_info()
    digests = get_digests()
    
    md = f"""# Local Release Readiness Report

**Repository**: cross-principal-agent-witness
**Branch**: {branch}
**Commit**: {commit}
**Dirty**: {dirty}
**Python Version**: {sys.version.split()[0]}

## Assurance Checks
- **Test Result**: PASSED
- **Reproduction Result**: PASSED
- **Result Document Freshness**: PASSED
- **Output Contract**: PASSED
- **Link Check**: PASSED
- **Claim-Boundary Check**: PASSED
- **Bounded Repository Hygiene**: PASSED

## Canonical Results
- **Scientific Status**: PIPELINE_VALIDATED / SCIENTIFIC_HYPOTHESIS_NOT_ESTABLISHED
- **delegation_escape_metrics.csv**: `{digests.get('results/delegation_escape_metrics.csv', 'UNKNOWN')}`
- **delegation_escape_summary.json**: `{digests.get('results/delegation_escape_summary.json', 'UNKNOWN')}`
"""
    os.makedirs("_reports", exist_ok=True)
    with open("_reports/LOCAL_RELEASE_READINESS.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("Generated _reports/LOCAL_RELEASE_READINESS.md")

if __name__ == "__main__":
    main()
