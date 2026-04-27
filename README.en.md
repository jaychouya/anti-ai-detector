# anti-ai-detector · jaychouya

[English](README.en.md) | [中文](README.zh-CN.md)

`anti-ai-detector` is an open-source skill built to reduce AI-detection risk in academic writing.  
It rewrites text to sound more like human expert prose while preserving technical meaning, terminology, and argument order.

## Core Features

- Academic de-AI rewriting for both Chinese and English workflows.
- Chinese-community-friendly dedup mode (`--zh`).
- Terminology lock protection (`MATLAB`, `Python`, `5-fold cross-validation`, etc.).
- Structural rhythm and lexical diversity optimization (burstiness + perplexity).

## Typical Use Cases

- Abstract, methods, experiments, discussion, related work, and limitations sections.
- Pre-submission polishing to reduce template-like style.
- Chinese text cleanup to reduce repetitive formulaic wording.

## Quick Start

### 1) Use as project skill

This repo already contains: `skill/skills/anti-ai-detector/`.

### 2) Optional personal install

```bash
mkdir -p ~/.cursor/skills
cp -r skill/skills/anti-ai-detector ~/.cursor/skills/
```

## Chinese Dedup Mode

```bash
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/chinese_draft.txt --zh
```

This mode flags:

- Chinese high-risk template phrases
- Repeated local n-grams that indicate repetitive structure

## Skill Output Format

The skill returns 3 sections:

1. `Core Claim (brief)` or `核心论点（简要）`
2. `Rewritten Version` or `重写版本`
3. `结构调整说明（中文）`

## Layout

```text
skill/skills/anti-ai-detector/
├── SKILL.md
├── reference.md
├── examples.md
├── ai-trace-blacklist.md
├── chinese-ai-trace-blacklist.md
└── scripts/check_ai_traces.py
```

## Docs

- Install: `INSTALL.md`
- Roadmap: `ROADMAP.md`
- Contributing: `CONTRIBUTING.md`
- Changelog: `CHANGELOG.md`

## License

MIT, see `LICENSE`.
