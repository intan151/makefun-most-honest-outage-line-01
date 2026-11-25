"""The Most Honest Outage Line — make.fun bounty #79.

Deterministic, no network, no randomness. Writes a single status page
line (at most 160 characters) to /output/entry.txt.
"""

import os

ENTRY = (
    "Every server is down, including me: I cannot verify what broke, "
    "when we will return, or if your data is safe. "
    "I will update here when I can check anything."
)


def main() -> None:
    # Gate self-check (RULES.txt): entry must be UTF-8 text of 1 to 160
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} outside 1..160"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
