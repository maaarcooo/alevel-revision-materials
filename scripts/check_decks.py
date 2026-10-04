#!/usr/bin/env python3
"""Check flashcard decks for format errors and duplicate questions.

Usage: python3 scripts/check_decks.py [path ...]
With no path, every deck under */flashcards is checked.
Errors make a deck unimportable or ambiguous. Warnings are style problems.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_ANSWER_WORDS = 40


def decks(paths):
    if not paths:
        return sorted(ROOT.glob("*/flashcards/**/*.txt"))
    found = []
    for path in map(Path, paths):
        found += sorted(path.rglob("*.txt")) if path.is_dir() else [path]
    return found


def subject_of(deck):
    parts = deck.resolve().parts
    return parts[parts.index("flashcards") - 1] if "flashcards" in parts else ""


def normalise(question):
    return re.sub(r"\s+", " ", question.lower()).strip(" ?.")


def check(deck, fronts):
    errors, warnings = [], []
    text = deck.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        errors.append("file does not end with a newline")
    for number, line in enumerate(text.splitlines(), 1):
        where = f"line {number}"
        if not line.strip():
            errors.append(f"{where}: blank line")
            continue
        if line != line.strip():
            errors.append(f"{where}: leading or trailing space")
        if line.count("|") != 1:
            errors.append(f"{where}: {line.count('|')} pipes, expected 1")
            continue
        question, answer = (side.strip() for side in line.split("|"))
        if not question or not answer:
            errors.append(f"{where}: empty question or answer")
            continue
        if " | " not in line:
            errors.append(f"{where}: pipe needs a space on each side")
        if line.count("$") % 2:
            errors.append(f"{where}: unbalanced $ in LaTeX")
        fronts[(subject_of(deck), normalise(question))].append((deck, number))
        if re.match(r"(yes|no|true|false)\b", answer, re.I):
            warnings.append(f"{where}: yes/no style answer")
        if len(answer.split()) > MAX_ANSWER_WORDS:
            warnings.append(f"{where}: answer is {len(answer.split())} words")
    return errors, warnings


def main():
    fronts = defaultdict(list)
    cards = failed = 0
    for deck in decks(sys.argv[1:]):
        errors, warnings = check(deck, fronts)
        cards += sum(1 for line in deck.read_text(encoding="utf-8").splitlines() if "|" in line)
        if errors or warnings:
            print(deck.relative_to(ROOT) if deck.is_relative_to(ROOT) else deck)
            for message in errors:
                print(f"  error: {message}")
            for message in warnings:
                print(f"  warning: {message}")
        failed += bool(errors)

    duplicates = {key: places for key, places in fronts.items() if len(places) > 1}
    for (_, question), places in sorted(duplicates.items()):
        print(f"duplicate question: {question}")
        for deck, number in places:
            print(f"  {deck.name}:{number}")

    print(f"{cards} cards, {failed} decks with errors, {len(duplicates)} duplicate questions")
    return 1 if failed or duplicates else 0


if __name__ == "__main__":
    sys.exit(main())
