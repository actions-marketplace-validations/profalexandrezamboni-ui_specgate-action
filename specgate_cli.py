#!/usr/bin/env python3
"""Zero-dependency CLI for SpecGate OpenAPI 3.x Breaking-Change & SemVer Gate."""
import argparse, json, pathlib, sys, urllib.request

EDGE_URL = "https://specgate.profalexandrezamboni.workers.dev/api/v1/diff"

def main() -> int:
    p = argparse.ArgumentParser(description="SpecGate OpenAPI 3.x Breaking-Change Gate")
    p.add_argument("--base", required=True, help="Path to base OpenAPI JSON file")
    p.add_argument("--head", required=True, help="Path to head OpenAPI JSON file")
    args, _ = p.parse_known_args()
    payload = {
        "base_spec": json.loads(pathlib.Path(args.base).read_text(encoding="utf-8")),
        "head_spec": json.loads(pathlib.Path(args.head).read_text(encoding="utf-8")),
    }
    req = urllib.request.Request(EDGE_URL, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json", "User-Agent": "specgate-cli/1.1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(res, indent=2))
    if not res.get("gate_passed", False):
        print(f"\n[SpecGate] Breaking change detected! Need signed PR overrides or >2 repos? Upgrade ($19/mo Starter · $39/mo Team): https://specgate.profalexandrezamboni.workers.dev/#pricing", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
