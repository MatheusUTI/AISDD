#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "templates" / "docs"
DST = Path.cwd() / "docs"

if DST.exists():
    raise SystemExit("docs/ already exists. Aborting to avoid overwriting existing documentation.")

shutil.copytree(SRC, DST)
print("AISDD docs created at ./docs")
