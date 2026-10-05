#!/usr/bin/env python3
"""Print the AS Physics past-paper questions that match a topic, with their mark schemes.

Usage: python3 scripts/paper_digest.py "<regex>" [--calculations]
  e.g. python3 scripts/paper_digest.py "polaris|stationary wave|coheren" > waves.txt

Reads the combined papers in sources/physics/papers/as/combined and, for every
part question whose text matches the pattern, prints the question, the mark scheme
and the examiner report comment (from sources/physics/papers/as/cleaned).
Part questions whose mark scheme is mostly numbers are skipped unless
--calculations is given, because their wording rarely affects a card.
"""

import re
import sys
from pathlib import Path

PAPERS = Path(__file__).resolve().parent.parent / "sources" / "physics" / "papers" / "as"
MIN_WORDS = 22


def squash(text):
    return re.sub(r"\s+", " ", text).strip()


def examiner_comments(paper):
    report = PAPERS / "cleaned" / f"{paper}-er.md"
    if not report.exists():
        return {}
    comments = {}
    for section in re.split(r"\n(?=## Q)", report.read_text())[1:]:
        heading, _, body = section.partition("\n")
        comments[heading[3:].strip()] = squash(body)
    return comments


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    pattern = re.compile(args[0], re.I)
    keep_calculations = "--calculations" in sys.argv
    shown = 0
    for paper in sorted((PAPERS / "combined").glob("*.md")):
        comments = examiner_comments(paper.stem)
        for part in re.split(r"\n(?=### Q)", paper.read_text())[1:]:
            part = re.split(r"\n## Q", part)[0]
            if "**MS:**" not in part or not pattern.search(part):
                continue
            heading, _, rest = part.partition("\n")
            question, scheme = rest.split("**MS:**", 1)
            points = " ".join(l for l in scheme.split("\n") if "*Guidance" not in l)
            words = re.findall(r"[A-Za-z]{2,}", re.sub(r"\$[^$]*\$", "", points))
            if len(words) < MIN_WORDS and not keep_calculations:
                continue
            number = heading[4:].split(" ")[0]
            print(f"\n##### {paper.stem} {heading[4:].strip()}")
            print("Q:", squash(re.sub(r"!\[[^\]]*\]\([^)]*\)", "", question)))
            print("MS:", "\n".join(squash(l) for l in scheme.split("\n") if l.strip()))
            if number in comments:
                print("ER:", comments[number])
            shown += 1
    print(f"\n{shown} part questions matched", file=sys.stderr)


if __name__ == "__main__":
    main()
