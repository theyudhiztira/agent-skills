# Maintaining this repo

Rules for anyone (human or agent) adding or changing skills here. Claude Code users: there is deliberately no `CLAUDE.md` at the root, because the plugin validator rejects one; point Claude at this file.

## Layout

- Every skill is a folder `skills/<bucket>/<skill-name>/` with a `SKILL.md` at its root. The folder name equals the `name` in the frontmatter.
- Buckets:
  - `productivity/`: workflow tools that are not code-specific (decks, documents, planning).
  - `engineering/`: daily code work. Create it when the first engineering skill arrives.
  - `in-progress/`: beta skills, not in the plugin.
  - `deprecated/`: retired skills, not in the plugin, skipped by `scripts/link-skills.sh`.
- Promoted buckets (`productivity/`, `engineering/`) must appear in the top-level `README.md`, in `.claude-plugin/plugin.json` `skills`, and in their bucket `README.md`. Non-promoted buckets appear in none of them.
- Every promoted skill has a row in the README's "For AI agents" catalogue table: name, invocation, when to load it, and the path to its `SKILL.md`.
- A new promoted bucket also needs its own `gemini skills install ... --path skills/<bucket>` line in the install block.
- Skill-owned scripts, references, tokens and examples live inside the skill folder, so a skill works when copied alone.

## Invocation

Each `SKILL.md` is one of:

- **Model-invoked**: the agent may load it when a request fits. No extra frontmatter. `agents/openai.yaml` sets `allow_implicit_invocation: true`.
- **User-invoked**: runs only when the user names it. Frontmatter has `disable-model-invocation: true`; `agents/openai.yaml` sets `allow_implicit_invocation: false`.

Every skill folder has `agents/openai.yaml` with `interface.display_name`, `interface.short_description` and `policy.allow_implicit_invocation`.

## Manifests and versions

- `.claude-plugin/plugin.json` lists every promoted skill path. `.claude-plugin/marketplace.json` makes the repo a single-plugin marketplace named `pensieve`.
- The version lives in `package.json`. After bumping it, run `npm run sync-plugin-version`; `npm run check-plugin-version` fails if they differ.
- After changing either manifest, run `npm run validate` (`claude plugin validate . --strict`). Keep the repo root free of `CLAUDE.md` so strict validation passes.
- Record user-visible changes in `CHANGELOG.md`.
- Install commands live in `.agents/install-block.md`; keep the README Quickstart identical to it. The skills CLI (`npx skills add` or `bunx skills add`) finds every `SKILL.md` on its own; test discovery with `npx skills@latest add . --list` before a release.

## Docs pages

Each promoted skill has `docs/<bucket>/<skill-name>.md` with four sections: What it does, When to reach for it, Common questions, It's working if.

## Local linking

`bash scripts/link-skills.sh` symlinks every skill into `~/.claude/skills` and `~/.agents/skills`. Re-run it after adding, removing or renaming a skill.

## Style

- No em dashes or en dashes in any repo prose, skill text, token file or example. Rewrite with a comma, colon, period, parentheses or a conjunction.
- No confidential client material in the repo: no client decks, logos, names of people, or figures from client work. Presets carry colours and fonts only.
- Plain, specific language. The natural-copy rules in `skills/productivity/pensieve-presentation/references/natural-copy.md` apply to this repo's own docs too.
