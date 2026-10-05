#!/usr/bin/env python3
"""Download AQA Physics topic questions and mark schemes into sources/.

Usage: python3 scripts/pull_mark_schemes.py <pmt-topic> "<n>. <Topic name>"
  e.g. python3 scripts/pull_mark_schemes.py waves "3. Waves"

<pmt-topic> is the last part of the topic page address on Physics & Maths Tutor,
https://www.physicsandmathstutor.com/physics-revision/a-level-aqa/<pmt-topic>/
Each PDF is saved next to a plain-text copy made with pdftotext, for searching.
The papers are copyrighted. sources/ is ignored by git and must stay that way.
"""

import html
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "sources" / "physics" / "Physics AQA Topic Questions (PMT)"
INDEX = "https://www.physicsandmathstutor.com/physics-revision/a-level-aqa/{}/"
AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"


def fetch(url, out=None):
    command = ["curl", "-sL", "--fail", "-A", AGENT, url]
    if out:
        return subprocess.run(command + ["-o", str(out)]).returncode == 0
    return subprocess.run(command, capture_output=True, text=True).stdout


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    topic, folder = sys.argv[1], DEST / sys.argv[2]
    page = fetch(INDEX.format(topic))
    links = sorted({html.unescape(u) for u in re.findall(r'href="([^"]*Topic-Qs/AQA/[^"]*\.pdf)"', page)})
    if not links:
        sys.exit(f"No topic question links found for '{topic}'. Check the topic name.")
    folder.mkdir(parents=True, exist_ok=True)
    saved = 0
    for url in links:
        # Multiple choice mark schemes are only answer letters, so they are skipped.
        if "/MCQ/" in url or "Multiple Choice" in url:
            continue
        match = re.search(r"/(Set-[A-Z])/(.+\.pdf)$", url)
        if not match:
            continue
        pdf = folder / f"{match.group(1)} {match.group(2)}"
        if not pdf.exists() and not fetch(urllib.parse.quote(url, safe=":/"), pdf):
            print(f"failed: {url}")
            continue
        subprocess.run(["pdftotext", "-layout", str(pdf), str(pdf.with_suffix(".txt"))])
        saved += 1
    print(f"{saved} papers in {folder}")


if __name__ == "__main__":
    main()
