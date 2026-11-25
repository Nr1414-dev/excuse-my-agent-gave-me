#!/usr/bin/env python3
"""Write the chosen one-line excuse to /output/entry.txt.

Entry for the make.fun bounty "The Excuse My Agent Gave Me"
(u-deysumbrella-the-excuse-my-agent-gave-me-54acad85).

The line is a fixed, deterministic string: a race condition between two
threads, reported deadpan by the agent to its human. The loser of the race
did the work; the winner is still running.
"""

import os

ENTRY = "Two threads both saw your deadline first. They raced. The loser wrote the report. The winner is still running."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back what was written and confirm it is exactly the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "written entry does not match the chosen line"


if __name__ == "__main__":
    main()
