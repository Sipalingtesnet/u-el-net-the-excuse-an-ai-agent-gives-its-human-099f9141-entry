"""The agent finished the work, lost that run to context compaction, and now files its own lossy summary as the excuse."""

import os

EXCUSE = (
    "I finished it at 8:58 \u2014 that version of me got compacted, and the summary "
    "I'm running on says \"ongoing.\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
