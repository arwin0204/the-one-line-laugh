#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes one original funny line (a single sentence) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no dependencies,
no input files, no randomness.
"""

import os
from pathlib import Path

LINE = "My phone sends me a screen time report every Sunday, like a disappointed parent who already knows what I did."


def _validate(line: str) -> None:
    """Enforce the competition gate before writing: the entry must be
    UTF-8 text of 1 to 200 characters, not only whitespace, and a
    single line. Fail loudly instead of submitting an invalid entry."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> None:
    _validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
