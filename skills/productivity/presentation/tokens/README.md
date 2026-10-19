# Design tokens

Each preset is one JSON file. The builder reads it; the layouts never hard-code a colour or size, so changing brand means changing a token file.

| Preset | Use for |
|---|---|
| `neutral-light` | Default. Pitches, internal updates, printed handouts, lit rooms |
| `neutral-dark` | Projected briefings in dim rooms, operations audiences |
| `command-dark` | Defence and government operations briefings in a command-centre style: dark, gridded, one blue signal, Geist |

## Structure

- `color`: `ground` (slide background), `surface`, `surfaceRaised`, `night` (photo overlay), `line`, `lineStrong`, `ink`, `inkMuted`, `inkSubtle`, `inkInverse`, `accent` (fills and large text), `accentText` (small blue text, keeps 4.5:1), `onAccent`, `status.ok|caution|critical`, `categorical.*` (named category colours).
- `type`: `fontSans`, `fontMono`, `fallback`, `googleFonts` (link for HTML routes), `scale` in px on a 1920 px canvas: `display`, `section`, `index`, `statement`, `h1`, `h2`, `h3`, `lead`, `body`, `small` (24 is the floor), `metric`.
- `layout`: `marginX`, `marginTop`, `marginBottom` in px.
- `decor`: switches for `grid`, `eyebrowUppercase`, `labelUppercase`, `displayUppercase`, `ghostNumeral`. Neutral presets switch everything off.
- `reasons`: one line per deliberate choice. Required for every decor switch that is on (see `references/natural-design.md`).

## Adding a brand preset

1. Copy `neutral-light.json` (or `neutral-dark.json`) to `<brand>.json`.
2. Replace colours from the brand guide. Check contrast: `ink` and `inkMuted` at least 4.5:1 on `ground` and `surface`; `accentText` at least 4.5:1; `accent` at least 3:1 for large text and fills.
3. Set fonts the audience's machines have, or free Google Fonts.
4. Turn on decor only if the brand asks for it, and write the reason.
5. Build `examples/sample-deck.json` with `-t tokens/<brand>.json` and look at the previews.
6. Do not commit logos or confidential brand assets to a shared repository; point `meta.logoLeft` at a local file instead.
