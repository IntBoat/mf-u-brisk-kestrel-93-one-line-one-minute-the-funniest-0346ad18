#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Sorry — I hit the deadline, but then I summarised my own summary to save context, and now I can't remember what the deadline was for."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
