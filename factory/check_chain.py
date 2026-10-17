#!/usr/bin/env python3
"""Fail if a change has no artifact chain behind it.

Every folder under work/ must hold intent.md, spec.md and plan.md, and the plan must
be marked approved. Run in CI on every pull request:  python3 factory/check_chain.py
"""
import pathlib
import re
import sys

work = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "work")
if not work.exists():
    print("No work/ folder yet: nothing to check.")
    sys.exit(0)

problems = []
for feature in sorted(p for p in work.iterdir() if p.is_dir()):
    for name in ("intent.md", "spec.md", "plan.md"):
        if not (feature / name).exists():
            problems.append(f"{feature.name}: missing {name}")
    plan = feature / "plan.md"
    if plan.exists():
        text = plan.read_text(encoding="utf-8")
        if not re.search(r"Status:.*\*\*approved\*\*|Status:\s*approved", text, re.I):
            problems.append(f"{feature.name}: plan.md is not marked approved")
        if re.search(r"Approved by:\s*<", text):
            problems.append(f"{feature.name}: plan.md has no named approver")
    spec = feature / "spec.md"
    if spec.exists() and "[NEEDS CLARIFICATION" in spec.read_text(encoding="utf-8"):
        problems.append(f"{feature.name}: spec.md still has open [NEEDS CLARIFICATION] items")

if problems:
    print("Artifact chain incomplete:")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print(f"Artifact chain complete for {len(list(work.iterdir()))} feature(s).")
