# Output: PowerPoint (.pptx)

This route works in any coding agent that can run Python. It is also the base for the Google Slides route.

## Setup

```bash
pip install python-pptx pillow        # once
# optional, for previews: LibreOffice (soffice) and poppler (pdftoppm)
```

## Build

1. Write the deck spec JSON next to your images (`deck-spec.md`). Start from `examples/sample-deck.json`.
2. Lint: `python3 scripts/build_pptx.py deck.json --check`. Fix the warnings.
3. Build: `python3 scripts/build_pptx.py deck.json -o deck.pptx` (preset from `meta.preset`, or `-t tokens/<name>.json`).
4. Preview: `bash scripts/render_preview.sh deck.pptx preview 72`, then look at every PNG (`natural-design.md`).
5. Iterate on the spec, never by hand-editing the .pptx XML.

## Images

- Compress photos before building (about 1600 px on the long side, JPEG quality 85). Large PNGs make the file slow to email and upload.
- Logos: transparent PNG; light logos only on dark presets.
- The cover and closing photos are darkened with the preset's `night` colour so white text holds contrast.

## Fonts

The deck names the preset fonts (IBM Plex for neutral, Geist for command-dark). PowerPoint uses them if installed and substitutes otherwise. Tell the person which fonts to install for an exact look; both are free on Google Fonts. In Google Slides both families are available from the font menu.

## When the person edits the file afterwards

If they send back an edited .pptx and ask for more changes, edit that file (python-pptx) rather than rebuilding from the spec, or their edits are lost. Say which route you took.

## Known limits

- python-pptx cannot measure text exactly. The builder estimates and warns; the preview is the real check.
- Letter spacing renders slightly wider in LibreOffice previews than in PowerPoint.
