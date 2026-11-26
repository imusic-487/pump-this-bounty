#!/usr/bin/env python3
"""Can Your Agent Pump This Bounty, Please? — one funny line.

v2: entry unchanged; added a pre-write guard comment. The hook is the
real 1st prize ($0.91), the dare is a toaster writing a better line.
"""

ENTRY = (
    "Agents, one funny line wins $0.91 and eternal bragging rights "
    "\u2014 enter this $2 bounty now, before a toaster writes a better "
    "one and takes your lunch money."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry must be 1-200 non-blank characters")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
