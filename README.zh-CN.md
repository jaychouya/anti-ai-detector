# anti-ai-detector · jaychouya

[English](README.en.md) | [中文](README.zh-CN.md)

`anti-ai-detector` 是一个专为降低学术写作 AI 检测率而设计的开源技能。  
它通过结构与词汇层面的重写，让文本更接近真实研究者写作风格，同时严格保留原文技术语义、术语和论证顺序。

## 核心能力

- 学术降 AI 痕迹重写（中英双语场景）。
- 中文社区友好的查重/降重增强（`--zh`）。
- 专业术语保护（如 `MATLAB`、`Python`、`5-fold cross-validation`）。
- 结构节奏优化（Burstiness）与词汇多样性优化（Perplexity）。

## 适用场景

- 论文摘要、方法、实验、讨论、相关工作、局限性等段落优化。
- 投稿前文本润色，降低模板感。
- 中文社区内容改写，减少“套话句”和重复短语。

## 快速开始

### 1) 作为项目内 Skill 使用

本仓库已包含路径：`skill/skills/anti-ai-detector/`  
在 Cursor / Claude Code 中直接调用即可。

### 2) 安装为个人 Skill（可选）

```bash
mkdir -p ~/.cursor/skills
cp -r skill/skills/anti-ai-detector ~/.cursor/skills/
```

## 中文查重模式（推荐）

```bash
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/chinese_draft.txt --zh
```

该模式会检测：

- 中文高风险模板短语（如“综上所述”“值得注意的是”等）
- 局部高频重复 n-gram（用于提示模板化复读）

## 输出格式

Skill 默认返回三段：

1. `核心论点（简要）`
2. `重写版本`
3. `结构调整说明（中文）`

## 目录结构

```text
skill/skills/anti-ai-detector/
├── SKILL.md
├── reference.md
├── examples.md
├── ai-trace-blacklist.md
├── chinese-ai-trace-blacklist.md
└── scripts/check_ai_traces.py
```

## 文档

- 安装说明：`INSTALL.md`
- 路线图：`ROADMAP.md`
- 贡献指南：`CONTRIBUTING.md`
- 更新记录：`CHANGELOG.md`

## 许可证

MIT，见 `LICENSE`。
