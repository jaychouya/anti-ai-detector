# anti-ai-detector · jaychouya

[English](README.en.md) | [中文](README.zh-CN.md)

`anti-ai-detector` is an open-source skill designed specifically to lower AI-detection risk in academic writing.  
It rewrites text to sound more like human expert writing while preserving the original technical meaning.

`anti-ai-detector` 是一个专为降低学术写作 AI 检测率而设计的开源技能。  
它能智能改写文本，使其更贴近人类表达，同时不丢失原文含义与术语准确性。

## Quick Links

- Main skill: `skill/skills/anti-ai-detector/SKILL.md`
- Install guide: `INSTALL.md`
- Roadmap: `ROADMAP.md`
- Contributing: `CONTRIBUTING.md`
- GitHub repo: [github.com/jaychouya/anti-ai-detector](https://github.com/jaychouya/anti-ai-detector)

## What It Solves

- Reduces template-like AI phrasing in Chinese/English academic prose.
- Preserves protected terminology and experimental logic.
- Adds structural diversity (burstiness) and lexical variety (perplexity).
- Supports Chinese dedup-oriented checks with `--zh` mode.

## Project Layout

```text
skill/skills/anti-ai-detector/
├── SKILL.md
├── reference.md
├── examples.md
├── ai-trace-blacklist.md
├── chinese-ai-trace-blacklist.md
└── scripts/check_ai_traces.py
```

## Start in 30 Seconds

```bash
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/paper.txt
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/chinese_draft.txt --zh
```

For full docs, open [English](README.en.md) or [中文](README.zh-CN.md).
