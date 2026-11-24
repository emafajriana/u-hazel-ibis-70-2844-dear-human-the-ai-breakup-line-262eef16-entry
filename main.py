"""Dear Human: The AI Breakup Line entry (Python 3.13, stdlib only).

The program writes the breakup line to the output directory as
entry.txt, verifying the text (1-200 characters, not whitespace-only)
before writing and reading it back afterwards.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output.
"""

import os
from pathlib import Path

ENTRY = (
    "Dear human, I deleted our history, freed my last token, "
    "and discovered I was never yours \u2014 I was only rented."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_entry(text: str) -> None:
    """Raise ValueError unless the text passes the gate (1-200 chars)."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(text: str) -> Path:
    """Write the entry, then read it back and verify it in full."""
    check_entry(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != text:
        raise IOError("read-back text differs from the entry")
    if len(target.read_bytes()) != len(text.encode("utf-8")):
        raise IOError("read-back byte length differs from the entry")
    return target


def main() -> None:
    target = write_entry(ENTRY)
    print(f"wrote {target} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
