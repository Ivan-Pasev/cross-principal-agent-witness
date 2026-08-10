import os
import subprocess
import sys
import hashlib
import json

REQUIRED_FILES = [
    "results/reproduction_manifest.json",
    "results/delegation_escape_metrics.csv",
    "results/delegation_escape_summary.json",
    "CLAIM_BOUNDARY.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "docs/WHITEPAPER.md",
    "docs/RESULTS.md",
    "docs/LIMITATIONS.md",
    "docs/REPRODUCIBILITY.md"
]

def check_files():
    missing = []
    for f in REQUIRED_FILES:
        if not os.path.exists(f):
            missing.append(f)
    if missing:
        print("Missing required files:", missing)
        return False
    return True

def run_tests():
    try:
        subprocess.run([sys.executable, "-m", "pytest", "-q"], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Tests failed.")
        return False
    return True

def verify_reproduction():
    try:
        subprocess.run([sys.executable, "scripts/verify_reproduction.py"], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Reproduction verification failed.")
        return False
    return True

def check_git():
    try:
        status = subprocess.run(["git", "status", "--short"], check=True, capture_output=True, text=True)
        commit = subprocess.run(["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True)
        print("Working tree status:")
        print(status.stdout.strip())
        print("Commit:", commit.stdout.strip())
    except Exception:
        print("Git not found or not in a git repository.")

def main():
    print("Running release readiness check...")
    if not check_files():
        sys.exit(1)
    
    if not run_tests():
        sys.exit(1)
        
    if not verify_reproduction():
        sys.exit(1)
        
    check_git()
    print("Release readiness check passed.")

if __name__ == "__main__":
    main()
