# Layout catalogue

Pick the layout from what the content is. The question to ask: "If I had to draw this on a whiteboard, what shape would it be?" A comparison is a matrix, a ranking is a ladder, a mechanism is a diagram. A grid of identical cards is almost never the answer.

Every layout below exists in `scripts/build_pptx.py` under the same name. Field details: `deck-spec.md`.

| Layout | Use when the content is | Limits | Avoid when |
|---|---|---|---|
| `cover` | The opening | Title one line if possible; photo optional, darkened | |
| `divider` | The start of a numbered section | Index, title, one lead line, optional tags | More than 5 sections (merge) |
| `summary` | One message backed by 3 to 5 numbers | Numbers must be real or `[__]` | The numbers are not comparable |
| `statement` | The single most important sentence of the deck | One sentence, one support line | Used more than once or twice |
| `convergence` | A mechanism: many separate inputs become one output | 2 to 6 inputs, 3 to 5 output rows | The inputs do not actually combine |
| `matrix` | Two dimensions: 2 to 4 categories by 2 to 4 aspects | Cells of 20 words or fewer | One dimension only (use a table or tiers) |
| `table` | Real reference data people may want to read | 8 rows, 3 to 4 columns | A list that could be a sentence |
| `tiers` | Ranked groups, each led by its count | 3 tiers, up to 9 items in the first | Items of equal rank |
| `layers` | An architecture or stack with one layer in focus | 4 to 7 layers, one highlight, optional side note | A sequence in time (use phases) |
| `quadrant` | Exactly four parallel ideas | Title, one line, one example each | Three or five ideas |
| `usecase` | A scenario: trigger, numbered steps, outcome | 5 or 6 steps, 3 outcomes | A generic process with no trigger |
| `phases` | A roadmap or phased plan | 2 to 4 phases; weight the current one | Dates you do not have (leave them out) |
| `coverage` | Progress across many items | 3 statuses, up to 6 groups, about 25 items | Fewer than 6 items (use a sentence) |
| `evidence` | Proof of activity: photos plus findings | 1 to 3 photos, 2 to 4 findings | Stock or decorative images |
| `decisions` | What you need from the audience | 2 to 4 numbered asks | Asks you cannot justify in one line |
| `closing` | The end | One line that restates the summary | |

## How these replaced generic cards in the reference deck

- Four KPI cards became a **ruled readout strip** with hairline dividers (`summary`).
- A "before/after" with three boxes became a **real diagram**: dashed lines from each source converge on the engine, one solid line leaves it (`convergence`).
- Three domain cards became a **matrix** (domains as columns, sources and outputs as rows).
- Three priority columns became a **ladder** led by counts 7, 5, 1 (`tiers`).
- Four equal function cards became a **quadrant** split by hairlines.
- Step rows with a coloured left stripe became a **vertical timeline** with square nodes (`usecase`).
- Three phase cards became a **rail** where the active phase is filled and wider (`phases`).
- A tick-mark table of agencies became a **coverage tracker** with a progress bar and groups.

## Rhythm across the deck

- Vary layouts between neighbouring slides. Two `table` slides in a row is a sign one should become something else.
- Keep shared furniture in fixed places: eyebrow and headline at the top margin, footer and page number at the bottom. Content moves; chrome does not.
- Dividers make the structure visible. Use them for every section, not only some.
