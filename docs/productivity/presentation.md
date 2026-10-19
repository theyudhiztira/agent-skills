# presentation

## What it does

Builds a deck a senior audience can follow from the headlines alone. It plans the storyline, simplifies dense source material, picks a layout per slide from a catalogue of 16, writes the copy in the audience's language (keeping English technical terms), applies a design token preset, checks the result for overflow and AI-sounding copy, and writes talking points into the speaker notes.

Outputs a PowerPoint file (any agent), a Google Slides deck (when the agent has a Google Drive tool) or a Claude Slides artifact (inside Claude apps that offer it).

## When to reach for it

- Rebuilding an existing deck for a different audience: "simplify this for the ministry's leadership".
- Turning notes or a brief into a pitch, a project update or a review deck.
- Restyling a deck into your brand or a preset.
- Getting talking points for a deck you already have, as speaker notes or a Google Doc.

## Common questions

**Do I need to know the layouts?** No. Describe the content and the audience; the skill picks layouts. You can ask for a specific one ("make slide 5 a timeline").

**Will it make up numbers?** No. Any figure not in your material becomes a `[__]` placeholder, listed at the end so you can fill it in.

**Can it use our brand?** Yes. Copy `tokens/neutral-light.json`, change colours and fonts, and name the preset. See `tokens/README.md` in the skill.

**Which language does it write in?** The audience's language for body text, with English technical terms kept in English. Say so if you want something else.

**What if I edit the deck by hand afterwards?** It re-reads the current file before every change and keeps your edits.

## It's working if

- Every headline states a point, and reading only the headlines tells the story.
- Neighbouring slides use different layouts that fit their content; no grids of identical cards.
- There are no em dashes, buzzwords or "not X, but Y" lines.
- Every content slide has talking points with a key message and a transition.
- The reply ends with a short list of placeholders and judgement calls, not a recap of every slide.
