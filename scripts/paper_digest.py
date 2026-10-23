#!/usr/bin/env python3
"""Print the past-paper questions that match a topic, with their mark schemes.

Usage: python3 scripts/paper_digest.py <subject> "<regex>" [--paper N] [--calculations]
  e.g. python3 scripts/paper_digest.py physics "polaris|stationary wave|coheren"
       python3 scripts/paper_digest.py computer-science "pipelin|register" --paper 1

Reads every combined paper under sources/<subject>/<level>/papers and, for each question
or part question whose text matches the pattern, prints the question, the mark
scheme and the examiner report comment. --paper keeps only paper 1 or paper 2.
Questions whose mark scheme has little wording (calculations, traces, code) are
skipped unless --calculations is given, because they rarely affect a card.
"""

import re
import sys
from pathlib import Path

SOURCES = Path(__file__).resolve().parent.parent / "sources"
MIN_WORDS = 22


def squash(text):
    return re.sub(r"\s+", " ", text).strip()


def examiner_comments(combined):
    """Examiner report sections by question number. The reports sit in a sibling folder."""
    report = combined.parent.parent / "reports" / f"{combined.stem}-er.md"
    if not report.exists():
        return {}
    comments = {}
    for section in re.split(r"\n(?=## Q)", report.read_text())[1:]:
        heading, _, body = section.partition("\n")
        comments[heading[3:].strip()] = body
    return comments


def comment_for(number, comments):
    """The report's comment on one part. The AS reports have a section per part. The
    A-level reports have one per question: take the part's own **Qnn.n** block, else
    the paragraphs that name the part, else the whole section."""
    if number in comments:
        return squash(comments[number])
    whole = comments.get(re.split(r"[.(]", number)[0])
    if whole is None:
        return None
    part = number[1:]
    labelled = re.split(r"\*\*Q(\d+\.\d+)\*\*", whole)
    if part in labelled[1::2]:
        return squash(labelled[labelled.index(part) + 1])
    named = [p for p in re.split(r"\n\s*\n", whole) if part in p]
    return squash("\n".join(named or [whole]))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    paper_number = None
    if "--paper" in flags:
        paper_number = args.pop()
    if len(args) != 2:
        sys.exit(__doc__)
    subject, pattern = args[0], re.compile(args[1], re.I)
    keep_calculations = "--calculations" in flags
    shown = 0
    papers = (SOURCES / subject).glob("*/papers/*.md")
    for paper in sorted(papers):
        if paper_number and not paper.stem.endswith(f"p{paper_number}"):
            continue
        level = paper.parent.parent.name
        comments = examiner_comments(paper)
        for part in re.split(r"\n(?=#{2,3} Q)", paper.read_text())[1:]:
            if "**MS:**" not in part or not pattern.search(part):
                continue
            heading, _, rest = part.partition("\n")
            heading = heading.lstrip("# ").strip()
            question, scheme = rest.split("**MS:**", 1)
            points = " ".join(l for l in scheme.split("\n") if "*Guidance" not in l)
            words = re.findall(r"[A-Za-z]{2,}", re.sub(r"\$[^$]*\$|```.*?```", "", points, flags=re.S))
            if len(words) < MIN_WORDS and not keep_calculations:
                continue
            number = heading.split(" ")[0]
            print(f"\n##### {level} {paper.stem} {heading}")
            print("Q:", squash(re.sub(r"!\[[^\]]*\]\([^)]*\)", "", question)))
            print("MS:", "\n".join(squash(l) for l in scheme.split("\n") if l.strip()))
            comment = comment_for(number, comments)
            if comment:
                print("ER:", comment)
            shown += 1
    print(f"\n{shown} questions matched", file=sys.stderr)


if __name__ == "__main__":
    main()
