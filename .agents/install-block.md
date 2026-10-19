# The canonical install block

One install story, one wording. The Quickstart in `README.md` must say **this** and nothing else. Change it here first, then copy it into the README.

## Two kinds of install

- **skills CLI** (`npx skills` or `bunx skills`, from [skills.sh](https://skills.sh)): works for every agent. It copies (or symlinks) editable skill files into the agent's skills folder. Updates are manual.
- **Plugin**: Claude Code, Codex and Copilot install from this repo's own marketplace (`.claude-plugin/marketplace.json`, named `theyudhiztira`, plugin `agent-skills`). Plugins reinstall only when `version` in `.claude-plugin/plugin.json` changes, so bump `package.json` and run `npm run sync-plugin-version` on every release.

The two routes are exclusive. Installing both gives the agent every skill twice, so always tell users to pick one per agent.

## Any agent (skills CLI)

The skills CLI reads every `SKILL.md` under `skills/` and needs no manifest. `-a` preselects the agent; valid ids include `claude-code`, `codex`, `cursor`, `opencode`, `windsurf`, `gemini-cli`, `github-copilot`, `amp`, `cline`, `roo`, `goose`, `zed`.

<canonical-block name="skills-cli">

```bash
npx skills@latest add theyudhiztira/agent-skills
```

Using Bun instead of Node:

```bash
bunx skills@latest add theyudhiztira/agent-skills
```

Useful flags: `-a <agent>` picks the agent (`claude-code`, `codex`, `cursor`, `opencode`, `windsurf`, `gemini-cli`, `github-copilot`, `amp`; omit it to choose), `-g` installs for your user instead of the current project, `-y` skips the prompts, `--skill <name>` installs one skill. Update with `npx skills@latest update`, and re-run `add` to pick up new skills.

</canonical-block>

Use the single-skill form wherever one skill is named on its own.

<canonical-block name="skills-cli-one-skill">

```bash
npx skills@latest add theyudhiztira/agent-skills --skill <name>
```

</canonical-block>

`skills@latest` is the pinned spelling everywhere.

## Claude Code

Third-party marketplaces do not auto-update by default in Claude Code.

<canonical-block name="claude-code">

```bash
claude plugin marketplace add theyudhiztira/agent-skills
claude plugin install agent-skills@theyudhiztira
```

Update with `claude plugin marketplace update theyudhiztira`, or turn on auto-update for `theyudhiztira` under `/plugin`, Marketplaces.

</canonical-block>

## Codex

<canonical-block name="codex">

```bash
codex plugin marketplace add theyudhiztira/agent-skills
codex plugin add agent-skills@theyudhiztira
```

Updates itself at startup.

</canonical-block>

## GitHub Copilot (CLI and VS Code)

Use the marketplace, not a direct repo install: direct installs cannot auto-update.

<canonical-block name="copilot">

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

</canonical-block>

## Gemini CLI

Gemini does not read `.claude-plugin`, and `--path` takes one bucket. Add one line per promoted bucket.

<canonical-block name="gemini">

```bash
gemini skills install https://github.com/theyudhiztira/agent-skills.git --path skills/productivity
```

Re-run to update.

</canonical-block>

## By hand (maintainers)

<canonical-block name="manual">

```bash
git clone https://github.com/theyudhiztira/agent-skills.git
bash agent-skills/scripts/link-skills.sh
```

This symlinks every skill into `~/.claude/skills` and `~/.agents/skills`, so `git pull` updates them. Pass another folder to link there instead, for example `bash agent-skills/scripts/link-skills.sh ~/.codex/skills`.

</canonical-block>
