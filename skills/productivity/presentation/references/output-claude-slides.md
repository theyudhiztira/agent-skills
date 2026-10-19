# Output: Claude Slides artifact

Use this route only inside Claude apps that offer a Slides artifact type. Everywhere else, use the PowerPoint route. The artifact type ships its own instructions; follow them first. This page holds what we learned the hard way building a real deck that way.

## Before writing

- Read the artifact first. Its type instructions say where content lives (an index file plus one HTML file per slide).
- If the person has a design system selected, install it as the type instructions describe (tokens file plus record) so the editor offers its colours. Brand fonts and logos may live as uploaded assets rather than files: copy them server side by asset id instead of by path.
- Upload photos as assets once and reuse their URLs on every slide.

## Slide HTML rules that bit us

- **Empty boxes disappear.** An empty `<div>` with no background, border or content is dropped by the editor, and in a grid that shifts every later cell one position. Build tables and matrices as separate flex rows, and put a real label in corner cells.
- **`gap` takes one value.** `gap: 14px 32px` is rejected.
- **Text at least 24 px.** Labels, cells and footers too.
- **Backdrops first.** Full-bleed images, scrims and grid SVGs must be the first children of the section, or they paint over the text.
- **Size boxes to the longest word** (about 0.6 x font size per character), or words break mid-word.
- **Estimate heights** before you write: about 2.1 x font size per table row; the safe area is 1920 x 1080 minus the preset margins.

## Editing safely

- **Re-read before every edit.** The person edits slides by hand. A publish over their change is refused; when that happens, read the slide again, re-apply your change on top of theirs, and publish again. Never resend your old copy.
- **Keep their edits.** If they changed a title or removed an element, your later edit must keep that.
- **Renumber after inserting slides.** Page numbers and section indices are written into each slide; update every later slide, and update `order` and `sections` in the index.
- **Speaker notes** live in each slide's `<aside>`; write talking points there.
- **Do not verify by rendering** unless the person asks; the type instructions forbid it. Estimate carefully instead, and tell the person what you could not check.
