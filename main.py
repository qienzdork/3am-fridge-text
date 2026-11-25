#!/usr/bin/env python3
"""The 3AM Fridge Text -- one line a smart fridge texts its owner at 3am.

Stdlib only. Writes the entry text to /output/entry.txt
(or $ENTRY_OUTPUT when set, for local validation).
"""

LINE = "You woke me up at 3am to stare at a jar of pickles like it owes you money. Go back to bed."


import os


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
