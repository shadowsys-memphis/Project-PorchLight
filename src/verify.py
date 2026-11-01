"""Synthetic outcome-verification demonstration, NOT a security boundary."""
import json
from pathlib import Path
import sys


def verify(task):
    required = task.get("acceptance_criteria", [])
    present = set(task.get("evidence", []))
    if not isinstance(required, list) or not required:
        return {"status": "BLOCKED", "missing": ["acceptance_criteria"]}
    missing = [criterion for criterion in required if criterion not in present]
    if missing:
        return {"status": "UNVERIFIED", "missing": missing}
    if not task.get("owner_approved", False):
        return {"status": "AWAITING_APPROVAL", "missing": []}
    return {"status": "VERIFIED", "missing": []}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 src/verify.py examples/demo-card.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(verify(data["task"]), indent=2))
