#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 (burn account).

Prints a single sentence, at most 200 characters, explaining the modern
internet to a time traveler from 1800 -- with no word coined after 1800.
The picture: a letter that crosses an ocean in the blink of an eye,
borne on thin wires, so any soul on earth may speak with any other soul.
Deterministic, standard library only.
"""

ENTRY = (
    "Think of a letter that crosses an ocean in the blink of an eye, "
    "borne on thin wires, so that any soul on earth may speak with "
    "any other soul at once."
)

# Validated locally 2026-11-24: 149 chars (limit 200), one line, no
# trailing spaces. Output sha256:
# e4093743890ff25bc0cc85962159fc8f90958af4bcb0b8aa16340cec79229f20
assert len(ENTRY) == 149, "entry must stay at 149 chars"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
