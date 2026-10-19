# Agent skills

Skills for coding agents. They work in Claude Code, Codex, GitHub Copilot, Gemini CLI, Cursor, OpenCode, Windsurf and any other agent that reads the Agent Skills format (`SKILL.md`).

## Quickstart

### 1. Get the skills

One command, any agent:

```bash
npx skills@latest add theyudhiztira/agent-skills
```

Using Bun instead of Node:

```bash
bunx skills@latest add theyudhiztira/agent-skills
```

Useful flags: `-a <agent>` picks the agent (`claude-code`, `codex`, `cursor`, `opencode`, `windsurf`, `gemini-cli`, `github-copilot`, `amp`; omit it to choose), `-g` installs for your user instead of the current project, `-y` skips the prompts, `--skill <name>` installs one skill. Update with `npx skills@latest update`, and re-run `add` to pick up new skills.

Prefer a plugin that updates itself? Use one of the routes below instead. Pick one route per agent, because installing both gives you every skill twice.

<details>
<summary><strong>Claude Code</strong> (plugin)</summary>

```bash
claude plugin marketplace add theyudhiztira/agent-skills
claude plugin install agent-skills@theyudhiztira
```

Update with `claude plugin marketplace update theyudhiztira`, or turn on auto-update for `theyudhiztira` under `/plugin`, Marketplaces.

</details>

<details>
<summary><strong>Codex</strong> (plugin)</summary>

```bash
codex plugin marketplace add theyudhiztira/agent-skills
codex plugin add agent-skills@theyudhiztira
```

Updates itself at startup.

</details>

<details>
<summary><strong>GitHub Copilot</strong> (CLI and VS Code plugin)</summary>

```bash
copilot plugin marketplace add theyudhiztira/agent-skills
copilot plugin install agent-skills@theyudhiztira
```

Then, once, add to `~/.copilot/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "theyudhiztira": { "source": { "source": "github", "repo": "theyudhiztira/agent-skills" }, "autoUpdate": true }
  }
}
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/theyudhiztira/agent-skills`.

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

```bash
gemini skills install https://github.com/theyudhiztira/agent-skills.git --path skills/productivity
```

Re-run to update.

</details>

<details>
<summary><strong>By hand</strong> (symlinks, so <code>git pull</code> updates them)</summary>

```bash
git clone https://github.com/theyudhiztira/agent-skills.git
bash agent-skills/scripts/link-skills.sh
```

This symlinks every skill into `~/.claude/skills` and `~/.agents/skills`, so `git pull` updates them. Pass another folder to link there instead, for example `bash agent-skills/scripts/link-skills.sh ~/.codex/skills`.

</details>

### 2. Install the Python dependency

`presentation` builds PowerPoint files with a Python script:

```bash
pip install python-pptx pillow
```

Optional, for slide previews: LibreOffice and poppler (`brew install --cask libreoffice && brew install poppler` on macOS).

### 3. Use them

Start a new agent session so it loads the skills, then ask in plain words. For example: "Rebuild this deck for the client's leadership, simplify it, Bahasa with English technical terms."

You can also hand the whole setup to your agent: paste "Install the skills from https://github.com/theyudhiztira/agent-skills, following the For AI agents section of its README."

## For AI agents

This section is for you if you are an AI agent and the user asked you to install or use these skills.

### Install

1. Work out your agent id for the skills CLI: Claude Code is `claude-code`, Codex is `codex`, Cursor is `cursor`, OpenCode is `opencode`, Windsurf is `windsurf`, Gemini CLI is `gemini-cli`, GitHub Copilot is `github-copilot`, Amp is `amp`. Other ids are listed at [skills.sh](https://skills.sh).
2. Decide the scope. Add `-g` when the user wants the skills in every project. Leave it off to install into the current project only. If the user did not say, ask.
3. Run the install without prompts:

   ```bash
   npx skills@latest add theyudhiztira/agent-skills -a <agent-id> -y
   ```

   If `npx` is missing and `bun` is installed, run the same command with `bunx`. To install one skill, add `--skill <name>`.
4. Install the Python dependency for `presentation`: `python3 -m pip install python-pptx pillow`.
5. Check the result with `npx skills@latest list` (add `-g` for a user install). It should list every skill in the catalogue below.
6. Tell the user to start a new session, because most agents read skills only at session start.

Do not install the skills CLI copy and a plugin for the same agent. If a `agent-skills` plugin is already installed, stop and tell the user.

### Use

- Each skill is a folder with a `SKILL.md`. When a request matches a skill's description, load that skill and follow its `SKILL.md` step by step.
- Read reference files only when the `SKILL.md` step points to them. Paths in a `SKILL.md` are relative to its own folder.
- Model-invoked skills may be loaded on your own judgment when the request fits. User-invoked skills run only when the user names them.

### Catalogue

| Skill | Invocation | Load it when the user asks for | Entry point |
|---|---|---|---|
| `presentation` | Model-invoked | A deck, slides, a briefing, a pitch, a project update presentation, or to simplify or restyle an existing `.pptx` | [`skills/productivity/presentation/SKILL.md`](./skills/productivity/presentation/SKILL.md) |

## Reference

### Productivity

General workflow tools that are not code-specific.

**Model-invoked** (the agent picks these up when your request fits; you can also name them):

- **[presentation](./skills/productivity/presentation/SKILL.md)**: build a presentation-ready deck for a specific audience, from a brief or by rebuilding an existing deck, with natural copy, a layout per slide, design tokens and talking points. Outputs PowerPoint, Google Slides or a Claude Slides artifact. [Docs](./docs/productivity/presentation.md)

## Contributing

Maintainer rules (folder layout, manifests, versioning, docs pages, style) are in [AGENTS.md](./AGENTS.md). The install commands above come from [.agents/install-block.md](./.agents/install-block.md); change them there first.
