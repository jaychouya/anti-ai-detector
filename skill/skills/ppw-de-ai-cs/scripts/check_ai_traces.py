#!/usr/bin/env python3
"""
check_ai_traces.py

Scan academic text for high-risk AI-trace phrases defined by the ppw-de-ai-cs
skill. Supports both English and Chinese detection profiles.

Usage:
    python scripts/check_ai_traces.py path/to/paper.tex
    python scripts/check_ai_traces.py path/to/text.md --json
    python scripts/check_ai_traces.py path/to/text.md --zh
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

ZH_BLACKLIST: dict[str, list[str]] = {
    "zh_template_opening": [
        "随着",
        "在当今",
        "众所周知",
        "值得注意的是",
        "不难发现",
    ],
    "zh_template_summary": [
        "综上所述",
        "总体而言",
        "由此可见",
        "具有重要意义",
        "提供了新的思路",
    ],
    "zh_hype": [
        "显著提升",
        "全面优化",
        "高效且鲁棒",
        "具有较强泛化能力",
        "达到最优性能",
    ],
}


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
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Common fallback for Chinese Windows environments.
        return p.read_text(encoding="gb18030")


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


def scan_zh_blacklist(text: str) -> list[Hit]:
    hits: list[Hit] = []
    for category, phrases in ZH_BLACKLIST.items():
        for phrase in phrases:
            line_nums: list[int] = []
            for i, line in enumerate(text.splitlines(), start=1):
                if phrase in line:
                    line_nums.append(i)
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


def scan_zh_repeated_ngrams(
    text: str, ngram_size: int = 4, min_repeat: int = 3, top_n: int = 8
) -> list[Hit]:
    """
    Scan repeated Chinese n-grams to surface template-like local repetition.
    """
    merged = re.sub(r"\s+", "", text)
    grams: dict[str, int] = {}
    for i in range(0, max(0, len(merged) - ngram_size + 1)):
        gram = merged[i : i + ngram_size]
        if not re.search(r"[\u4e00-\u9fff]", gram):
            continue
        grams[gram] = grams.get(gram, 0) + 1

    repeated = sorted(
        ((gram, c) for gram, c in grams.items() if c >= min_repeat),
        key=lambda item: item[1],
        reverse=True,
    )[:top_n]

    return [
        Hit(
            category="zh_repeated_ngram",
            phrase=gram,
            count=count,
            line_examples=[],
        )
        for gram, count in repeated
    ]


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
    out.append("Hint: see ai-trace-blacklist.md / chinese-ai-trace-blacklist.md.")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan text for AI-trace phrases (ppw-de-ai-cs)."
    )
    parser.add_argument("input", help="path to text file, or '-' for stdin")
    parser.add_argument(
        "--json", action="store_true", help="emit JSON report instead of text"
    )
    parser.add_argument(
        "--zh",
        action="store_true",
        help="enable Chinese profile (blacklist + repeated n-gram hints)",
    )
    parser.add_argument(
        "--ngram-size",
        type=int,
        default=4,
        help="ngram size for Chinese repetition scan (default: 4)",
    )
    parser.add_argument(
        "--min-repeat",
        type=int,
        default=3,
        help="minimum repeat count for Chinese n-gram alert (default: 3)",
    )
    args = parser.parse_args()

    text = load_text(args.input)
    hits = scan_blacklist(text) + scan_repeat_connectors(text)
    if args.zh:
        hits += scan_zh_blacklist(text)
        hits += scan_zh_repeated_ngrams(
            text, ngram_size=args.ngram_size, min_repeat=args.min_repeat
        )

    if args.json:
        print(json.dumps([asdict(h) for h in hits], ensure_ascii=False, indent=2))
    else:
        print(render_text(hits))

    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
