# Output: Google Slides

Google Slides decks are built as a .pptx first, then uploaded to Google Drive with conversion. This keeps one build path for every agent.

## Steps

1. Build and preview the .pptx (`output-pptx.md`).
2. Upload it with the agent's Google Drive tool (the call is usually named `create_file`):
   - `title`: the deck title
   - `contentMimeType`: `application/vnd.openxmlformats-officedocument.presentationml.presentation`
   - `base64Content`: the file, base64 encoded
   - leave conversion on, so Drive creates a native Google Slides file
3. Read the result's link and share it with the person, as a link inside the sentence that says what you did.
4. If a Google Slides editing tool is available, use it for later changes so the link stays the same. If only Drive is connected, every change means a new upload and a new link: say so before the second change.

## Keep the upload small

The whole file travels inside one tool call. Compress images first; aim for under 5 MB. If the upload fails for size, give the person the .pptx to import with File > Import slides, and say why.

## No Google tools

If the agent has no Google Drive tool, say that the Google Drive connector is not available, hand over the .pptx, and tell the person they can open it with Google Slides (Drive converts it on open).

## After conversion

- Speaker notes come across as notes.
- Fonts: IBM Plex and Geist are in the Google Slides font list. If text looks different, the font name did not match; re-pick it from the font menu.
- Check one slide with a table and one with a diagram after conversion; dashed curves become line shapes and stay editable.
