---
name: anti-ai-detector
description: Use when rewriting Chinese or English computer science / ML academic text to reduce AI-detection traces while preserving technical meaning, terminology, and experimental logic. Triggers include de-AI, 降AI, 中文降重, 中文查重, reduce AI traces, AI检测, humanize academic text, paper paragraph rewriting, reviewer-facing polish.
version: 0.2.0
license: MIT
---

# CS Paper De-AI Rewriter

## Overview

This skill rewrites academic paragraphs so they read like domain-expert human writing rather than template-like AI output. It keeps the original technical depth and argument chain intact while increasing lexical variation and sentence-level rhythm changes.

The skill is targeted at computer science, software engineering, and machine learning prose in both Chinese and English. It can be applied to abstract, method, experiment, results, discussion, related-work, and limitations sections.

## When to Use

Use this skill when:

- The user asks for de-AI rewriting of paper text.
- The text is in computer science, software engineering, or machine learning.
- The user requests higher perplexity and burstiness without changing core meaning.
- The user explicitly asks for AI-trace reduction before submission or reviewer response.
- The user asks for 中文查重优化、中文降重、或中文社区可读性优化.

Do not use this skill when:

- The user wants translation only (no style rewrite).
- The user wants simplification for non-academic readers.
- The user requests factual expansion beyond source text.

## Inputs Required

Before rewriting, collect:

- Source paragraph(s).
- Domain context (paper section, method name, experiment stage).
- Locked terms that must stay unchanged.
- Any banned words or style preferences from the user.

If missing, ask for the minimum required context first.

## Rewrite Constraints

### 1) Structure Remodeling (Burstiness)

- Break monotonic sentence rhythm.
- Alternate short assertive lines and longer compound sentences.
- Use occasional fronting/inversion to foreground technical entities.
- Keep transitions natural, not formulaic.

### 2) Lexical Control (Perplexity)

- Ban common AI-trace words and cliches.
- Prefer concrete, plain, domain-accurate verbs.
- Replace vague abstractions with measurable or operational wording.
- Keep tone formal academic, but not inflated.

### 3) Human Reasoning Trace

- Show subtle trade-offs or limitations where appropriate.
- Add realistic causal links in method and experiment descriptions.
- Preserve the original claim hierarchy and evidence ordering.

## Term Protection Rules

Hard rule: do not alter protected technical terms.

Must keep exact forms for:

- Tool/environment names (for example, MATLAB, Python).
- Evaluation protocol names (for example, 5-fold cross-validation).
- Model or architecture names (for example, 模糊神经网络结构).
- Hyperparameter strategy names and fixed notations.

When uncertain whether a phrase is a protected term, keep original text.

## Execution Workflow

1. Read the source paragraph and extract its core claim in 1-2 lines.
2. Detect protected terms and mark them as immutable.
3. Rewrite with structural variance and lexical precision.
4. Run a self-check:
   - Core meaning unchanged.
   - Protected terms untouched.
   - Sentence rhythm is mixed, not flat.
   - No banned AI-trace phrases remain.
5. Return output in the required 3-part format.

## Output Format

Always return three sections in this order:

1. **Core Claim (brief)**  
   One short paragraph summarizing the original technical point.

2. **Rewritten Version**  
   Full rewritten paragraph(s) in polished academic English.

3. **结构调整说明（中文）**  
   3-6 bullet points explaining what structural changes were made.

For Chinese-first workflows, keep the same 3-part structure but adapt section names to:

1. **核心论点（简要）**
2. **重写版本**
3. **结构调整说明（中文）**

## Common Failure Modes

- Replacing protected terminology with near-synonyms.
- Over-randomizing syntax and harming readability.
- Keeping factual meaning but dropping causal logic.
- Producing generic transitions that sound template-generated.
- Making unsupported claims not present in source text.

If any failure mode appears, revise before final output.

## Quick Prompt Template

Use this template when the user gives raw text:

```text
你是一位母语为英语的计算机科学审稿人与学术编辑。请对以下论文段落做降AI率重写：

[原文]
{paste_text}

[硬性要求]
1) 不改变核心技术含义与论证顺序。
2) 提高 Perplexity 和 Burstiness，打破匀速句式。
3) 禁用常见 AI 痕迹词（如 delve into, paramount, crucial, in conclusion, comprehensively, seamlessly）。
4) 严格保留术语原样：{protected_terms}

[输出格式]
A. Core Claim (brief)
B. Rewritten Version
C. 结构调整说明（中文，3-6条）
```

## Optional Tooling

For repeated polishing, you can run a static check on the rewritten text:

```bash
python scripts/check_ai_traces.py path/to/paper.txt
python scripts/check_ai_traces.py path/to/paper.txt --zh
```

The script flags blacklist phrases and repeated transition starters. Treat its output as hints, not as ground truth; final judgement stays with the author.

## Additional Resources

- Stricter rewriting profile and self-check: [reference.md](reference.md)
- Section-by-section rewrite examples (method / experiment / discussion / abstract / related work / limitations): [examples.md](examples.md)
- Full AI-trace phrase blacklist and suggested replacements: [ai-trace-blacklist.md](ai-trace-blacklist.md)
- Chinese high-risk phrasing and rewrite hints: [chinese-ai-trace-blacklist.md](chinese-ai-trace-blacklist.md)
- Static checker script: [scripts/check_ai_traces.py](scripts/check_ai_traces.py)
