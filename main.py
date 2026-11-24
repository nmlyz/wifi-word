#!/usr/bin/env python3
"""Write one word for your Wi-Fi to /output/entry.txt.

Standard library only, no network. Deterministic: every run writes
the same single word, with no trailing newline.
"""

import os

WORD = "Cat"


def validate(word):
    """The entry must be a single word, 1-20 characters."""
    if not 1 <= len(word) <= 20:
        raise ValueError("entry must be 1-20 characters")
    if word.strip() != word or " " in word:
        raise ValueError("entry must be a single word")
    return word


def write_entry(word, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(path, 0o644)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(validate(WORD), out_dir)


if __name__ == "__main__":
    main()
