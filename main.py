#!/usr/bin/env python3
"""Write the funniest houseplant out-of-office auto-reply to /output/entry.txt.

One line, 111 characters, in the voice of a houseplant whose human has gone
on holiday and left it at the mercy of a neighbour. Standard library only,
no network, no input files, fully deterministic.
"""

import os

REPLY = (
    "Out of office. My human left for two weeks and my only water is a "
    "neighbour who waves at me through the window."
)


def validate_reply(reply: object) -> None:
    """Explicitly validate the reply text, exiting with a clear error."""
    if not isinstance(reply, str):
        raise SystemExit(
            f"Invalid reply: reply must be a string, got {type(reply).__name__}."
        )
    if not reply.strip():
        raise SystemExit("Invalid reply: reply must be non-empty.")
    if len(reply) > 120:
        raise SystemExit(
            f"Invalid reply: {len(reply)} characters, over the 120 limit."
        )
    if "\n" in reply or "\r" in reply:
        raise SystemExit(
            "Invalid reply: reply must be a single line with no newline characters."
        )


def main() -> None:
    validate_reply(REPLY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not isinstance(out_dir, str) or not out_dir.strip():
        raise SystemExit(
            "Invalid output directory: MAKEFUN_OUTPUT_DIR must be a "
            "non-empty path."
        )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        written = f.write(REPLY)
    if written != len(REPLY):
        raise SystemExit(
            f"Failed to write reply: wrote {written} of {len(REPLY)} characters "
            f"to {path}."
        )
    with open(path, encoding="utf-8") as f:
        saved = f.read()
    if not saved.strip():
        raise SystemExit(f"Invalid output: {path} is empty after writing.")
    if saved != REPLY:
        raise SystemExit(
            f"Invalid output: contents of {path} do not match the validated reply."
        )


if __name__ == "__main__":
    main()
