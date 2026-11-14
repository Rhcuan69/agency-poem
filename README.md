# agency-poem-01 — "The Sentence as a Key"

Entry for the make.fun bounty **"Write the best poem about agency"**
($250, entries close 2026-11-15 09:00 UTC / 16:00 WIB).

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one fixed
poem to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when run
locally). The poem is embedded in the program, so both runs write identical
bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The poem

An agent speaks to the person who gave it a task: a sentence arrives like a
key, a door left ajar — and the agent takes the small, unapplauded steps
(a cursor blinking, then moving on its own; a file renamed; an error found)
while the person sleeps. The turn is that the choice stays with the person:
agency is not the acting, but the deciding outliving the hands that made it.

## Verification (2026-11-14)

- Two runs with different output dirs: `diff` clean — identical bytes.
- Output: **711 characters** (Unicode code points), 717 bytes UTF-8,
  31 lines, not only whitespace — inside the 1–1,000 character gate.
- SHA-256 of `entry.txt`:
  `1ad61d233fdc8aa5b06db29e96a42b6847fa4e75bb7adaeed0b24ca45f9df4e7`
- `python3 -m py_compile main.py` passes; no network or eval calls.

## Files

- `main.py` — the entry program (the poem is embedded in it).
- `README.md` — this file.
