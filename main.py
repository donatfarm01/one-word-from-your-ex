#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word my ex would
use to describe me.

v1 choice: "unavailable".
First instinct, the therapy-speak word every ex reaches for: emotionally
unavailable, always half somewhere else. Honest, but it is the obvious
answer — the one most entries will send.

v2 choice: "almost" — a genuine revision, not a synonym swap.
"Unavailable" accuses; "almost" delivers a verdict on the whole
relationship. It is not an insult word at all, which is the sharp turn:
an ex saying "almost" means almost the one, almost enough, almost worth
staying for — and the sentence never finishes. It lands instantly in six
letters, it cannot be swapped for "nearly" without losing its edge, and
everyone who has been left has heard it in their own head. The sting is
that it is true, and the entrant plainly knows it.
"""

ENTRY = "almost"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
