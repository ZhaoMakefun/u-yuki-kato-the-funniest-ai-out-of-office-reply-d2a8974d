#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one original out-of-office auto-reply, in the voice of an AI
agent heading off on vacation, to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

Python 3.13, standard library only, no network access, fully deterministic:
every run writes exactly the same bytes.
"""

import os

# The entry: one line, 125 characters, inside the 1-160 gate.
# The reply stays in the machine's voice throughout: the agent is away,
# urgent matters go to its human, and the turn is that the human will
# ignore them — with far more warmth than the agent ever could.
ENTRY = (
    "I am away on vacation. Please direct urgent matters to my human, "
    "who will ignore them with far more warmth than I ever could."
)

MAX_CHARS = 160


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty or only whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("entry must not contain control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
