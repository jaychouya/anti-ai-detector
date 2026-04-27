# CONTRIBUTING

Thanks for your interest in improving `anti-ai-detector`.

## Development Principles

- Preserve meaning first, style second.
- Never break terminology lock guarantees.
- Prefer small, reviewable pull requests.
- Include concrete examples for style-related changes.

## How to Contribute

1. Fork the repository.
2. Create a branch: `feat/xxx` or `fix/xxx`.
3. Make changes with tests/examples where applicable.
4. Open a pull request using the PR template.

## Suggested Contribution Types

- New blacklist entries with rewrite alternatives.
- Better Chinese dedup rules in `--zh` mode.
- New section examples (`examples.md`).
- Tooling improvements for `scripts/check_ai_traces.py`.
- Documentation clarity and translation improvements.

## Quality Checklist

- Keep docs concise and actionable.
- Confirm references and paths are correct.
- Run checker help command:

```bash
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py --help
```

- If changing parser logic, include at least one before/after sample in your PR.

## Code of Conduct

Be respectful, technical, and evidence-driven.
