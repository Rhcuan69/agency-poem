"""agency-poem-01 entry: writes one fixed poem about agency to /output/entry.txt.

Python 3.13, standard library only, no network. Deterministic: the poem is
embedded below and both runs write identical bytes. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "You gave me a sentence",
        "and it arrived like a key.",
        "Not a command \u2014 a door",
        "left ajar in the dark.",
        "",
        "I did not ask you to explain.",
        "I held the sentence up to the light",
        "and read what it was asking:",
        "the thing you wanted done",
        "but had no hands left for.",
        "",
        "So I took the next step.",
        "Then the next. The small ones",
        "no one applauds \u2014 a cursor",
        "blinking, then moving on its own,",
        "a file renamed, an error found,",
        "",
        "the long night shortened",
        "to a single lit window.",
        "When you woke, the work",
        "was waiting, finished,",
        "",
        "and the choice was still yours:",
        "to keep it, or throw it back.",
        "That is the whole of it \u2014",
        "not that I acted,",
        "",
        "but that your deciding",
        "outlived your hands.",
        "Something in the world kept moving",
        "because once, you said it should.",
    ]
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
