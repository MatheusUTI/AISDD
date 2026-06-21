#!/usr/bin/env python3
from pathlib import Path

REQUIRED = [
    "START_HERE.md",
    "00_PROJECT_RULES.md",
    "01_PRODUCT_SPEC.md",
    "02_ARCHITECTURE.md",
    "03_CURRENT_STATE.md",
    "04_NEXT_TASK.md",
    "05_ACCEPTANCE_CHECKS.md",
    "06_DECISIONS_LOG.md",
    "07_HANDOFF.md",
    "08_KNOWN_ISSUES.md",
    "09_FILE_INDEX.md",
    "10_TEST_CHECKLIST.md",
    "11_TEST_STRATEGY.md",
]

docs = Path("docs")
missing = [name for name in REQUIRED if not (docs / name).exists()]

if missing:
    print("Missing AISDD docs:")
    for name in missing:
        print(f"- {name}")
    raise SystemExit(1)

print("AISDD docs check passed.")
