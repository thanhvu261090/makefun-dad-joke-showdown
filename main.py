#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt, after checking it
against the competition gate: UTF-8 text, 1 to 200 characters, not only
whitespace, and a single line.
"""

import os

JOKE = (
    "My dad says working the elevator has its ups and downs, "
    "but he loves lifting people's spirits."
)

MAX_CHARS = 200


def gate_check(text):
    """Enforce the kit's gate limits on the entry text.

    The gate is the sealed scorer's check: UTF-8 text of 1 to 200
    characters, not only whitespace, written as a single line.
    Returns True when the text passes; raises ValueError otherwise.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return True


def main():
    gate_check(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    print("wrote %d characters to /output/entry.txt" % len(JOKE))


if __name__ == "__main__":
    main()
