# Changelog

All notable changes to `anti-ai-detector` are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-04-27

### Added

- `examples.md`: before/after rewrite examples for method, experiment, results, abstract, related work, and limitations sections.
- `ai-trace-blacklist.md`: structured blacklist of AI-trace phrases with suggested replacements, plus a whitelist reminder for protected terminology.
- `scripts/check_ai_traces.py`: static checker that flags blacklist phrases and repeated transition starters; exits non-zero when issues are found.
- Repository-level `README.md`, `LICENSE` (MIT), `.gitignore`, and this `CHANGELOG.md` to make the skill GitHub-ready.

### Changed

- `SKILL.md`: tightened description, added `version` and `license` frontmatter fields, expanded the "Additional Resources" block to link to the new files.
- Markdown formatting cleaned up to satisfy `markdownlint` (blank lines around lists and headings).

## [0.1.0] - 2026-04-27

### Added

- Initial `SKILL.md` with frontmatter, when-to-use rules, rewrite constraints (burstiness, perplexity, human reasoning trace), term protection rules, execution workflow, fixed three-part output format, and a quick prompt template.
- `reference.md` with stricter rewrite profile, sentence-rhythm targets, structural variation targets, and a self-check checklist.
