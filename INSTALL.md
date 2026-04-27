# Installation

This project uses a `colleague-skill`-style repository layout:

- root docs and entry files at repository root
- actual skill implementation in `skill/skills/anti-ai-detector/`

## Cursor (personal install)

```bash
mkdir -p ~/.cursor/skills
cp -r skill/skills/anti-ai-detector ~/.cursor/skills/
```

## Verify

Run a quick checker smoke test:

```bash
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/paper.txt
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/chinese_draft.txt --zh
```

## Notes

- `--zh` enables Chinese profile (high-risk phrases + repeated n-gram hints).
- Checker output is advisory; human review remains final.
