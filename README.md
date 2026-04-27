# anti-ai-detector

`anti-ai-detector` is a production-ready Cursor/Claude skill pack for rewriting CS/ML academic text to reduce AI-detection traces, while preserving technical meaning, term fidelity, and experiment logic.

这是一套面向论文场景的“降 AI 痕迹”技能包，强调术语不变、逻辑不丢、表达更像真实研究者写作。

---

## Features

- Rewrites academic paragraphs with higher **perplexity** (lexical diversity) and **burstiness** (sentence rhythm variation).
- Preserves protected technical terms exactly (e.g., `MATLAB`, `Python`, `5-fold cross-validation`).
- Applies strict anti-template constraints from `reference.md`.
- Provides section-level examples in `examples.md`.
- Includes a static checker script for high-risk AI-trace phrases.
- Includes a Chinese profile (`--zh`) for 中文查重高风险短语和重复 n-gram 提示.

It does **not** invent facts, alter protected terminology, or replace rigorous reasoning with generic wording.

---

## Repository Layout

```text
skill/skills/anti-ai-detector/
├── SKILL.md                  # main skill definition (frontmatter + instructions)
├── reference.md              # stricter rewrite profile + self-check protocol
├── examples.md               # before/after examples for common paper sections
├── ai-trace-blacklist.md     # full phrase blacklist + suggested replacements
└── scripts/
    └── check_ai_traces.py    # static checker for AI-trace phrases
```

---

## Quick Start

### 1) Use as a project skill

This repo already contains `skill/skills/anti-ai-detector/`. Open the folder in Cursor and invoke the skill with prompts like:

- `降一下这段方法部分的AI率，术语保持不变`
- `帮我做中文查重优化，保持术语不变，减少模板句`
- `Rewrite this paragraph to sound less AI-generated`
- `Use strict profile and show Chinese structure notes`

### 2) Install as personal skill (optional)

```bash
mkdir -p ~/.cursor/skills
cp -r skill/skills/anti-ai-detector ~/.cursor/skills/
```

### Option B: Project skill (this repo only)

The skill is already at `skill/skills/anti-ai-detector/`. Cursor will pick it up automatically when the workspace is opened.

### Option C: Claude Code

Skills under `skill/skills/` are also discoverable by Claude Code's `Skill` tool. No extra setup needed.

---

## Usage Pattern

In Cursor or Claude Code, ask things like:

- "Help me reduce AI traces in this paragraph."
- "降一下这段方法部分的 AI 率。"
- "Rewrite my abstract so it doesn't read like ChatGPT."

The skill returns a fixed 3-part output:

1. `Core Claim (brief)`
2. `Rewritten Version`
3. `结构调整说明（中文）`

### Optional: Static Check

```bash
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/paper.txt
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/chinese_draft.txt --zh
```

Output (example):

```text
AI-trace phrases detected:
  [hype] comprehensively x1 (lines: 12)
  [filler] it is worth noting that x2 (lines: 7, 33)
  [empty_compare] outperforms existing methods x1 (lines: 41)
Hint: see ai-trace-blacklist.md / chinese-ai-trace-blacklist.md.
```

Exit code is `1` when issues are found, so this can be integrated into CI.

---

## Included Files

- `SKILL.md`: main entry and workflow rules
- `reference.md`: strict rewrite profile and self-check checklist
- `examples.md`: before/after examples by paper section
- `ai-trace-blacklist.md`: phrase blacklist + replacement hints
- `chinese-ai-trace-blacklist.md`: 中文高风险表达词表（查重/降重）
- `scripts/check_ai_traces.py`: static checker

---

## Design Principles

- **Triggering description, not workflow summary.** The frontmatter only describes when to use the skill. The agent must open the skill body to see the workflow, which prevents shortcut behavior.
- **Term-protection first.** A locked-term pass runs before rewriting, so that aggressive style changes never overwrite protected technical entities.
- **Three-part output is fixed.** Core claim, rewrite, Chinese change-log. This makes the skill auditable: a reviewer can immediately see what was changed and why.
- **Static check is non-binding.** The Python script is a hint generator, not a gate. Human judgement still decides.

---

## Version

See `CHANGELOG.md`.

Current version: **0.2.0** (see `CHANGELOG.md`).

---

## License

MIT. See [LICENSE](LICENSE).

---

## Contributing

Pull requests welcome. Suggested directions:

- Additional section templates (rebuttal letter, cover letter, response to reviewers).
- Domain extensions (NLP-specific, systems-specific, theory-specific phrasebooks).
- Multilingual inputs (Chinese-to-English rewriting style guide).
- Better static checks (n-gram cliché detection, sentence-length distribution analyzer).

When proposing rewrites, please include both a "before" and "after" example so the change in style is reproducible.

---

## Acknowledgment

If this skill helps your writing workflow, feel free to star the repository:
[github.com/jaychouya/anti-ai-detector](https://github.com/jaychouya/anti-ai-detector)
