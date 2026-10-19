# pensieve-presentation

A skill for coding agents that builds presentation-ready slide decks: from a brief, or by rebuilding an existing deck for a new audience. It plans the storyline, picks a layout per slide, writes natural copy in the audience's language, applies design tokens, checks the result, and writes talking points.

It works in any agent that reads `SKILL.md` skills (Claude Code, Codex and others), and its PowerPoint builder is a plain Python script, so it does not depend on one vendor's tools.

## What you can ask for

- "Rebuild this deck for the ministry's leadership, simplify the use cases, Bahasa with English technical terms."
- "Make a 10-slide proposal for the client from these notes, light theme, PowerPoint."
- "Turn the speaker notes into a Google Doc I can read on my phone."

The agent asks a few questions first when the brief is thin (guided mode), or builds straight away when it is complete (quick mode).

## Install

See the [repository README](../../../README.md#quickstart) for install commands per agent (Claude Code, Codex, Copilot, Gemini CLI, Cursor and others). Then:

```bash
pip install python-pptx pillow
```

## What is inside

```
SKILL.md                 the workflow the agent follows (10 steps, two modes)
references/              detail for each step: intake, storyline, simplify, layouts,
                         deck spec, writing, natural copy and design gates,
                         talking points, and one page per output format
tokens/                  design token presets: neutral-light, neutral-dark, command-dark
scripts/build_pptx.py    deck spec JSON + tokens -> .pptx, with lint warnings
scripts/render_preview.sh  .pptx -> PNG previews to check every slide
scripts/export_notes.py  talking points -> HTML (Google Doc) or Markdown
examples/sample-deck.json  a complete deck spec to start from
```

## Try it without an agent

```bash
python3 scripts/build_pptx.py examples/sample-deck.json -o sample.pptx
bash scripts/render_preview.sh sample.pptx preview
```

## Adding your brand

Copy `tokens/neutral-light.json`, change the colours and fonts, and set `"preset"` in the deck spec. Details in `tokens/README.md`.
