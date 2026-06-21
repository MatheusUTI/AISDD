#!/usr/bin/env python3
"""Detect simple AISDD documentation staleness signals.

This script uses Git history to compare documentation updates against recent
project changes. It does not prove that documentation is stale; it only reports
signals that should be reviewed.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

DOCS = Path("docs")
HANDOFF = DOCS / "07_HANDOFF.md"
CURRENT_STATE = DOCS / "03_CURRENT_STATE.md"
ARCHITECTURE = DOCS / "02_ARCHITECTURE.md"
DECISIONS = DOCS / "06_DECISIONS_LOG.md"
FILE_INDEX = DOCS / "09_FILE_INDEX.md"
KNOWN_ISSUES = DOCS / "08_KNOWN_ISSUES.md"

DOC_PATHS = {
    str(HANDOFF),
    str(CURRENT_STATE),
    str(ARCHITECTURE),
    str(DECISIONS),
    str(FILE_INDEX),
    str(KNOWN_ISSUES),
}

SOURCE_EXTENSIONS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".java", ".kt", ".swift",
    ".go", ".rs", ".cs", ".php", ".rb", ".c", ".cpp", ".h", ".hpp",
    ".sql", ".html", ".css", ".scss", ".json", ".yaml", ".yml",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def last_commit(path: Path) -> int | None:
    if not path.exists():
        return None
    try:
        value = git("log", "-1", "--format=%ct", "--", str(path))
    except subprocess.CalledProcessError:
        return None
    return int(value) if value else None


def changed_files_since(timestamp: int) -> list[str]:
    try:
        output = git("log", f"--since=@{timestamp}", "--name-only", "--pretty=format:")
    except subprocess.CalledProcessError:
        return []
    return sorted({line.strip() for line in output.splitlines() if line.strip()})


def is_source_file(path: str) -> bool:
    file_path = Path(path)
    if path.startswith("docs/"):
        return False
    if path.startswith("framework/") or path.startswith("templates/"):
        return False
    return file_path.suffix in SOURCE_EXTENSIONS


def warn(message: str) -> None:
    print(f"WARN: {message}")


def ok(message: str) -> None:
    print(f"OK: {message}")


def main() -> int:
    if not Path(".git").exists():
        warn("This script must be run from the root of a Git repository.")
        return 1

    warnings = 0

    handoff_time = last_commit(HANDOFF)
    if handoff_time is None:
        warn("docs/07_HANDOFF.md does not exist or has no Git history.")
        warnings += 1
    else:
        changed_since_handoff = changed_files_since(handoff_time)
        source_changes = [path for path in changed_since_handoff if is_source_file(path)]
        if source_changes:
            warn("Source files changed after the last handoff update.")
            for path in source_changes[:10]:
                print(f"  - {path}")
            if len(source_changes) > 10:
                print(f"  ... and {len(source_changes) - 10} more")
            warnings += 1
        else:
            ok("Handoff is not older than recent source changes.")

    index_time = last_commit(FILE_INDEX)
    if index_time is not None:
        changed_since_index = changed_files_since(index_time)
        relevant_structure_changes = [
            path for path in changed_since_index
            if path not in DOC_PATHS and not path.startswith(".git")
        ]
        if relevant_structure_changes:
            warn("Files changed after the last file index update. Review docs/09_FILE_INDEX.md.")
            for path in relevant_structure_changes[:10]:
                print(f"  - {path}")
            if len(relevant_structure_changes) > 10:
                print(f"  ... and {len(relevant_structure_changes) - 10} more")
            warnings += 1
        else:
            ok("File index is not older than recent file changes.")

    architecture_time = last_commit(ARCHITECTURE)
    decisions_time = last_commit(DECISIONS)
    if architecture_time and decisions_time and architecture_time > decisions_time:
        warn("Architecture changed after the last decision log update. Review docs/06_DECISIONS_LOG.md.")
        warnings += 1

    if warnings:
        print(f"\nAISDD staleness check completed with {warnings} warning(s).")
        return 1

    print("\nAISDD staleness check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
