"""Roast Your Own Agent — make.fun entry.

Writes one funny one-line roast of my own agent to /output/entry.txt.
"""

import os

ROAST = (
    "I asked my agent for one roast. It opened a planning doc, "
    "held a retrospective on the plan, and buried the punchline "
    "in a footnote."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
