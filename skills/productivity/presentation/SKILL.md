---
name: presentation
description: Build a presentation-ready slide deck for a specific audience, from a brief or by rebuilding an existing deck, with natural (non-AI-sounding) copy, a deliberate layout per slide, design tokens, and talking points. Use when someone asks for a deck, slides, a briefing, a pitch, a project update presentation, or to simplify or restyle an existing .pptx. Outputs PowerPoint, Google Slides, or a Claude Slides artifact.
---

# Presentation

This skill turns source material into a deck a senior audience can follow from the headlines alone. It was built from a real briefing for a government defence audience and works for any audience: client pitches, project updates, internal reviews.

The work is always the same ten steps. Do them in order. Each step points to the reference that holds the detail; read a reference when you reach its step, not before.

## Two modes

- **Guided mode** (default). Ask the intake questions before building, one round, at most four questions. Use it when the brief leaves audience, language, purpose or source unclear, or when the person is not technical.
- **Quick mode**. When the brief already states audience, purpose, language, length and output, skip the questions. Say your assumptions in one line at the top of your reply and build.

## The ten steps

1. **Intake.** Pin down audience, purpose (inform, decide, persuade), language, source material, length, output format and preset. Guided questions and quick-mode defaults: `references/intake.md`.
2. **Read the source.** For an existing deck, extract every slide's text, tables, images and notes before planning (python-pptx, or markitdown if installed). List what is unclear or contradictory and ask, or flag it in your reply. Never resolve a contradiction silently.
3. **Plan the storyline.** Cover, summary, numbered sections with dividers, next steps, close. One message per slide; the headline states it. Write the outline (one line per slide) before any layout work. `references/storyline.md`.
4. **Simplify for the audience.** Group long tables, cut flows to five or six steps, move evidence to the notes, keep only real numbers. `references/simplify.md`.
5. **Pick a layout per slide** from the catalogue by what the content is: numbers, a mechanism, a comparison, a ranking, a process, progress, evidence, asks. Never default to a grid of identical cards. `references/layouts.md`.
6. **Write the copy, then run the copy gate.** Audience language for body text, English technical terms kept in English, natural tone. Then the natural-copy audit. `references/writing.md`, `references/natural-copy.md`.
7. **Apply tokens.** Use the preset the person names, else their organisation's design system, else `neutral-light`. Presets live in `tokens/`; how to add one: `tokens/README.md`.
8. **Build** in the requested format:
   - PowerPoint (works in any agent): write a deck spec and run `scripts/build_pptx.py`. `references/deck-spec.md`, `references/output-pptx.md`.
   - Google Slides: build the .pptx, then upload with conversion. `references/output-google-slides.md`.
   - Claude Slides artifact (only inside Claude apps that offer it): `references/output-claude-slides.md`.
9. **Run the design gate.** Render previews (`scripts/render_preview.sh`) and look at every slide. Fix overflow, collisions and anything the gate flags. `references/natural-design.md`.
10. **Talking points.** Key message, three to six points, one transition per slide, in the speaker notes. Export to a Google Doc or Markdown when asked. `references/talking-points.md`.

## Rules that hold on every deck

- **Never invent a fact.** No number, name, date, quote or source that is not in the material or given by the person. Use `[__]` placeholders and list every placeholder in your reply.
- **One message per slide.** If a slide needs two headlines, it is two slides.
- **Headlines are sentences that say the point**, one line where possible, two at most.
- **Minimum text size 24 px on a 1920 px slide** (12 pt). If it does not fit, split the slide; never shrink.
- **No em dashes** in any slide, note or file name. Use a period, comma, colon or parentheses.
- **Every colour carries a meaning** and travels with a word: status, category, or the one accent.
- **Sensitive content** (security incidents, casualties, named people) stays factual, cites source and date, names no individuals on slides, and lives in the notes when it is context rather than the point.
- **Re-read before you edit.** The person may have changed slides by hand since your last write. Start every edit from the current file.
- **Renumber after inserting slides.** Page numbers and section indices (`01_`, `02_`) must stay in order.

## Companion skills

If `antislop`, `antislop-copywriting` or `antislop-ui` are installed, load them at steps 6 and 9; this skill's `natural-copy.md` and `natural-design.md` hold the slide-specific version of their rules, so the gates still work without them.

## Delivering

Say in two or three sentences what you built and where it is. Then list: every `[__]` placeholder, every judgement call (grouping you invented, conflicts you resolved), and anything you could not verify visually. Do not recap every slide.
