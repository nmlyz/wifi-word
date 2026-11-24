#!/usr/bin/env python3
"""Write one word for your Wi-Fi to /output/entry.txt.

Standard library only, no network. Deterministic: every run writes
the same single word, with no trailing newline.
"""

import os

LINE = "Cat"


def main():
    assert 1 <= len(LINE) <= 20, "entry must be 1-20 characters"
    assert LINE.strip() == LINE and " " not in LINE, "entry must be a single word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
