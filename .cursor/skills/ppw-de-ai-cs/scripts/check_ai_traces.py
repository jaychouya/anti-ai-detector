#!/usr/bin/env python3
"""
check_ai_traces.py

Scan an English academic text file for high-risk AI-trace phrases
defined by the ppw-de-ai-cs skill.

Usage:
    python scripts/check_ai_traces.py path/to/paper.tex
    python scripts/check_ai_traces.py path/to/text.md --json
    cat draft.txt | python scripts/check_ai_traces.py -

Exit code:
    0  - clean (no high-risk phrases hit a configured threshold)
    1  - flagged (one or more issues found)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


BLACKLIST: dict[str, list[str]] = {
    "hype": [
        "comprehensively",
        "seamlessly",
        "robust and scalable",
        "state-of-the-art",
        "novel",
        "paramount",
        "crucial",
        "remarkable",
        "significantly",
        "groundbreaking",
        "paving the way",
        "plays a vital role",
        "play a vital role",
    ],
    "filler": [
        "it is worth noting that",
        "in the context of",
        "in conclusion",
        "in this paper",
        "in this work",
    ],
    "hedge": [
        "delve into",
        "shed light on",
        "a wide range of",
        "a myriad of",
        "pivotal",
    ],
    "empty_compare": [
        "outperforms existing methods",
        "achieves superior performance",
        "demonstrates the effectiveness",
        "various datasets",
        "diverse settings",
    ],
}

REPEAT_CONNECTORS = [
    "moreover",
    "furthermore",
    "additionally",
    "therefore",
    "thus",
    "hence",
]


@dataclass
class Hit:
    category: str
    phrase: str
    count: int
    line_examples: list[int]


def load_text(source: str) -> str:
    if source == "-":
        return sys.stdin.read()
    p = Path(source)
    if not p.exists():
        raise FileNotFoundError(f"input not found: {source}")
    return p.read_text(encoding="utf-8")


def find_phrase(text: str, phrase: str) -> list[int]:
    """Return 1-indexed line numbers where phrase occurs (case-insensitive)."""
    lines: list[int] = []
    pattern = re.compile(r"\b" + re.escape(phrase) + r"\b", flags=re.IGNORECASE)
    for i, line in enumerate(text.splitlines(), start=1):
        if pattern.search(line):
            lines.append(i)
    return lines


def scan_blacklist(text: str) -> list[Hit]:
    hits: list[Hit] = []
    for category, phrases in BLACKLIST.items():
        for phrase in phrases:
            line_nums = find_phrase(text, phrase)
            if line_nums:
                hits.append(
                    Hit(
                        category=category,
                        phrase=phrase,
                        count=len(line_nums),
                        line_examples=line_nums[:5],
                    )
                )
    return hits


def scan_repeat_connectors(text: str) -> list[Hit]:
    """Flag adjacent sentences that start with the same transition word."""
    hits: list[Hit] = []
    sentences = re.split(r"(?<=[.!?])\s+", text)
    prev_starter: str | None = None
    repeats: dict[str, int] = {}
    for s in sentences:
        first = s.strip().split(" ")[0].strip(",;:").lower() if s.strip() else ""
        if first and first == prev_starter and first in REPEAT_CONNECTORS:
            repeats[first] = repeats.get(first, 0) + 1
        prev_starter = first
    for word, n in repeats.items():
        hits.append(
            Hit(
                category="repeat_connector",
                phrase=word,
                count=n,
                line_examples=[],
            )
        )
    return hits


def render_text(hits: Iterable[Hit]) -> str:
    hits = list(hits)
    if not hits:
        return "OK: no high-risk AI-trace phrases detected."
    out = ["AI-trace phrases detected:"]
    for h in hits:
        loc = (
            f" (lines: {', '.join(map(str, h.line_examples))})"
            if h.line_examples
            else ""
        )
        out.append(f"  [{h.category}] {h.phrase} x{h.count}{loc}")
    out.append("")
    out.append("Hint: see ai-trace-blacklist.md for suggested rewrites.")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan text for AI-trace phrases (ppw-de-ai-cs)."
    )
    parser.add_argument("input", help="path to text file, or '-' for stdin")
    parser.add_argument(
        "--json", action="store_true", help="emit JSON report instead of text"
    )
    args = parser.parse_args()

    text = load_text(args.input)
    hits = scan_blacklist(text) + scan_repeat_connectors(text)

    if args.json:
        print(json.dumps([asdict(h) for h in hits], ensure_ascii=False, indent=2))
    else:
        print(render_text(hits))

    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
