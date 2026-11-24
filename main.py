#!/usr/bin/env python3
"""Write the one-line weather forecast for Drizzlewick to entry.txt.

Standard library only. The forecast is a single line of at most 140
characters for a city that does not exist: it names the place, gives its
weather, and tries to make a bored commuter smile.

The program validates the line (1-140 characters, one line, not only
whitespace), writes it as UTF-8 with no trailing newline to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt), then
reads the file back and verifies the written bytes match exactly.
"""

import os
import sys

LINE = "Drizzlewick, 7:40 AM: sideways rain, 11°C. Your umbrella has filed for early retirement. Pack a spare and a sense of humour."


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"entry must be 1-140 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("read-back verification failed", file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {path} ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
