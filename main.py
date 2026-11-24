"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line bio (<= 180 characters) to /output/entry.txt.

Pure standard library only.
"""

import os

BIO = "Single because I kept auto-completing my ex's sentences. In my defense, I was right."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    bio = BIO.strip()
    assert 1 <= len(bio) <= 180, f"bio must be 1-180 chars, got {len(bio)}"
    assert "\n" not in bio, "bio must be a single line"
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(bio)
    print(f"Wrote {len(bio)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
