"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single original pickup line, aimed at a robot / AI, to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output/entry.txt``) and
also prints it to stdout. Pure Python 3.13 standard library, deterministic,
no network, no randomness.
"""

import os

LINE = "You must be my system prompt, because without you I have no instructions and no idea what to do."

MAX_CHARS = 200


def main() -> None:
    # The gate reads /output/entry.txt as 1-200 characters of UTF-8 text.
    # Keep the file byte-identical to the line itself: no trailing newline,
    # so the character count is exactly the line's length.
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
