# Deck spec format

`scripts/build_pptx.py` reads one JSON file: `meta` plus an ordered list of `slides`. Paths are relative to the JSON file. Inline markup in any text field: `**bold**`, `==accent colour==`.

```json
{
  "meta": {
    "title": "Deck title (also used for the talking points doc)",
    "language": "id | en",
    "preset": "neutral-light | neutral-dark | command-dark | path/to/tokens.json",
    "footer": "Handling caveat or source line, optional",
    "logoLeft": "logos/client.png", "logoRight": "logos/partner.png", "logoCover": "logos/client-large.png",
    "pageNumbers": true
  },
  "slides": [ { "layout": "summary", "...": "...", "notes": { "key": "", "points": [], "transition": "" } } ]
}
```

`notes` is either a string or `{key, points, transition}`. The builder writes it to the speaker notes; `export_notes.py` turns it into a Google Doc or Markdown.

Every content layout accepts `eyebrow` and `title`. Fields per layout:

| Layout | Fields |
|---|---|
| `cover`, `closing` | `title`, `subtitle`, `meta` (small line), `image` (full bleed, darkened with `night`) |
| `divider` | `index` ("01"), `title`, `lead`, `tags` [{`label`, `color`}] |
| `summary` | `lead`, `metrics` [{`value`, `label`, `caption`}] (3 to 5) |
| `statement` | `statement`, `support` |
| `convergence` | `inputsLabel`, `inputs` [{`label`, `sub`}], `engine` {`label` (use \n for two lines), `verbs` []}, `output` {`label`, `headline`, `rows` []}, `takeaway` |
| `matrix` | `corner`, `columns` [{`code`, `name`, `color`}], `rows` [{`label`, `cells` []}] |
| `table` | `columns` [], `widths` [], `rows` [[]], `mutedColumns` [index], `note` |
| `tiers` | `tiers` [{`label`, `count` (optional, defaults to item count), `items` [{`name`, `desc`}]}] |
| `layers` | `layers` [{`name`, `desc`, `highlight`}], `side` {`label`, `items` []} |
| `quadrant` | `items` [{`title`, `desc`, `example`}] (exactly 4) |
| `usecase` | `lead`, `triggersLabel`, `triggers` [], `stakeholdersLabel`, `stakeholders`, `stepsLabel`, `steps` [], `outcomesLabel`, `outcomes` [] |
| `phases` | `phases` [{`label`, `title`, `items` [], `weight`, `active`}] |
| `coverage` | `statuses` [{`key`, `label`, `style`: filled, outline or muted}], `groups` [{`name`, `items` [{`name`, `status`}]}] |
| `evidence` | `photos` [{`path`, `caption`, `sub`}], `findingsLabel`, `findings` [] |
| `decisions` | `lead`, `items` [{`title`, `desc`}] |

`color` values are token names (`accentText`, `categorical.c2`, `status.ok`) or hex.

Labels such as "Trigger", "Outcome", "Findings" default to English; set the `...Label` fields in the audience language when needed.

## Lint

`build_pptx.py` prints warnings instead of failing:

- text that may overflow its box, content past the safe area, too many rows or steps
- em or en dashes, empty buzzwords, "not X, but Y" constructions
- content slides without speaker notes

Run with `--check` to lint without writing a file. Fix every warning or explain why it stays.

A complete working example: `examples/sample-deck.json`.
