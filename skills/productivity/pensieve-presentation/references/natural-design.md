# Natural design gate

Run this on the rendered slides before you deliver. It is the slide version of the `antislop-ui` skill; load that skill too if it is installed.

## Render and look

```bash
bash scripts/render_preview.sh out.pptx preview 72
```

Open every PNG. A tool accepting your file does not mean the slide is right. Look for: text past its box or the safe area, items colliding, empty columns, a slide that looks like the one before it.

## What the gate checks

| Check | Fails when | Fix |
|---|---|---|
| Layout follows content | Every slide is a grid of equal cards | Pick from `layouts.md` by what the content is |
| One accent | The accent colour is on titles, borders, icons and fills at once | Accent marks only the key number, the active step, the focus layer, or the section index |
| Colour has a meaning | A colour appears with no label (a green dot with no word) | Every status or category colour travels with its word or code |
| No decorative stripes | Coloured left bars on cards or rows that mark nothing | Remove, or let them mark a real state |
| No glow, no shadows, no pill shapes | Soft shadows under everything, rounded pills everywhere | Flat surfaces, hairline rules, square corners |
| Cards only for equal sets | A card per idea when the ideas differ in weight | Use a ladder, matrix or list |
| Rhythm | Two neighbours share the same layout and density | Change one, or merge them |
| Chrome stays put | The headline jumps between slides | Eyebrow and headline at the top margin on every content slide |
| Real images only | Stock people, illustration blobs, decorative textures | Photos that prove something, or no image |
| Breathing room | Content fills to every edge | Respect the margins in the preset; split the slide |

## Decor that needs a written reason

`antislop-ui` flags background grids, wide-tracked uppercase labels, dark-by-default themes and default fonts. They are allowed only when a preset or brand system asks for them and says why, in the token file's `reasons` block. `neutral-light` and `neutral-dark` switch them all off. `command-dark` switches them on, with its reasons recorded. Do not add decor a preset does not ask for.

## Checklist

- [ ] Every slide rendered and looked at
- [ ] No overflow, no collisions, nothing past the footer band
- [ ] Layouts vary and each fits its content
- [ ] Accent used only where it means something
- [ ] Every colour has a word
- [ ] Decor present only if the preset gives a reason
