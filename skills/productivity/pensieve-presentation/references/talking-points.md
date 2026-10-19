# Talking points

Every content slide gets talking points in the speaker notes. They help the presenter say more than the slide shows, in the audience's language.

## Format per slide

```
KEY MESSAGE: one sentence, the thing to land on this slide.

• 3 to 6 points, each one sentence the presenter can say out loud.
• Point at what is on screen: "the bar at the top", "the dashed lines on the left".
• Context and sensitive figures (with source and date) go here, not on the slide.

TRANSITION: one sentence that leads into the next slide.
```

In the deck spec this is `"notes": {"key": "", "points": [], "transition": ""}`. For Indonesian decks the labels become PESAN UTAMA and TRANSISI automatically (`meta.language: "id"`).

## Writing them

- Same natural-copy rules as the slides. They are spoken, so even plainer.
- Add what the slide cannot hold: why a number matters, an example, the source of a figure, the ask behind a slide.
- Flag presenter choices in plain words: "Soften this if it does not fit the room."
- Opening slide: greeting, purpose, the order of the talk, duration as `[__]` unless given.
- Closing slide: recap in three points at most, then open questions.

## Exporting for reading on a phone

The presenter often wants the points in a document, not only in the notes.

```bash
python3 scripts/export_notes.py deck.json --format html -o talking-points.html
python3 scripts/export_notes.py deck.json --format md -o talking-points.md
```

**Google Doc.** If the agent has a Google Drive tool that can create files, upload the HTML with `contentMimeType: text/html` and no conversion flag; Drive converts it into a native Google Doc with headings, bold and bullets. Then read the doc back once to confirm the structure. Name it "Talking points: {deck title}". If the Drive tool is not connected, say so and offer the Markdown or a .docx instead.

**Keep in sync.** The doc is a copy. When the speaker notes change, regenerate and update the doc, keeping the same file so the link does not change.
