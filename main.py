#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Sorry — I spent the morning reading your 400,000-token brief, and by the time I reached the deadline, it had already retired."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text)


if __name__ == "__main__":
    write_entry()
