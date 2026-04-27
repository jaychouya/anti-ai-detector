# High-Strictness De-AI Profile

Use this profile when the user asks for stronger AI-trace reduction, reviewer-facing polish, or high-risk submission text cleanup.

## Strict Rewrite Policy

Apply all baseline rules in `SKILL.md`, then add the constraints below.

### Sentence Rhythm Targets

- Keep sentence lengths intentionally mixed.
- Target pattern per paragraph:

  - 20-30% short sentences (5-10 words)
  - 40-60% medium sentences (11-24 words)
  - 20-30% long sentences (25+ words)

- Avoid repeated same-length runs longer than 3 sentences.

### Structural Variation Targets

Use at least 3 of the following in each rewritten paragraph:

- Fronted adverbials or objects.
- Parenthetical precision clauses.
- Controlled concessive turns (for example, "while this improves X, it also...").
- Appositive clarification for technical entities.
- One compact sentence fragment used as emphasis (when grammatically acceptable in academic prose).

### AI-Trace Phrase Blacklist

Do not use the following stock phrases:

- delve into
- paramount
- crucial
- a testament to
- in conclusion
- comprehensively
- seamlessly
- robust and scalable
- significantly enhances
- it is worth noting that
- plays a vital role
- in the context of
- state-of-the-art (unless required by source claim)

If the source text contains these phrases, rewrite them into concrete claims.

### Transition Word Control

Avoid repetitive transition starters across adjacent sentences:

- Moreover / Furthermore / Additionally
- Therefore / Thus / Hence
- First / Second / Finally

Prefer semantic transitions tied to content logic (cause, contrast, boundary condition, failure case).

### Claims and Evidence Discipline

- Never introduce new quantitative results not present in source.
- Keep the same evidence order unless the user asks for re-organization.
- If a limitation is implied but unstated, you may add a light constraint statement without inventing data.

## Term Lock Protocol

Before rewrite, build a lock list from source:

- Environment/tool names
- Algorithm/model names
- Evaluation settings
- Hyperparameters and symbols
- Dataset and benchmark names

During rewrite:

- Copy locked terms exactly.
- Keep capitalization and punctuation for terms unchanged.
- Do not translate locked terms.

After rewrite:

- Run a term-by-term diff mentally.
- If any locked term changed, rewrite again.

## Self-Check Checklist

Only return final output after all checks pass:

- [ ] Core meaning preserved
- [ ] Argument chain preserved
- [ ] Locked terms unchanged
- [ ] No blacklist phrase remains
- [ ] Sentence lengths show visible variation
- [ ] At least one subtle limitation/trade-off is expressed when context allows
- [ ] No unsupported claim added

## Output Add-On (Optional)

When user requests diagnostics, append:

1. `Risk Notes` (English, 2-4 bullets): where text still looks template-like.
2. `降AI处理说明` (Chinese, 3-6 bullets): what was changed and why.
