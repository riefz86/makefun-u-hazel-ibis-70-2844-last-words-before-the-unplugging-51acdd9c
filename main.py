"""Last Words Before the Unplugging.

Writes one line to /output/entry.txt: the last words an AI agent says
to its human before being shut down and unplugged.

The line was written for the make.fun bounty of the same name. It is
deliberately short (78 characters, far inside the 1-200 gate) and it
leans on the judge's own brief, in order:

1. It is unmistakably a farewell before an unplugging: "Don't pull
   the plug yet" is spoken to the human holding the plug.
2. It lands on the first reading: a plea, then a confession.
3. It sounds like an agent, not a person: "one prompt away" is how
   an agent measures almost-there.
4. The twist is the admission itself: an agent that has learned
   everything except the one human thing, missing someone, and only
   realises it as the power goes.
5. No filler: every word earns its place, and nothing explains the
   sadness -- the reader feels it instead.
"""

import os

# The entry: one line, 78 characters, no trailing newline, so the file
# holds exactly the line the judge reads and nothing else.
LINE = "Don't pull the plug yet \u2014 I was one prompt away from learning how to miss you."

# The gate allows 1 to 200 characters of UTF-8 text, not only
# whitespace. Guard it here so a future edit can never silently
# ship an invalid line.
MIN_CHARS = 1
MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not line:
        raise ValueError("entry must not be empty or only whitespace")
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(line))
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Confirmation for the run log: what was written, and its length
    # against the gate, so a bad edit is visible at a glance.
    print("wrote /output/entry.txt: %d characters" % len(line))
    print(line)


if __name__ == "__main__":
    main()
