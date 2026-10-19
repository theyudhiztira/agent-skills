# Intake

The goal of intake is to know six things before you plan a single slide. Ask only for what the brief does not already answer.

| Need | Why it changes the deck | Default when unknown (quick mode) |
|---|---|---|
| Audience | Depth, vocabulary, what to cut, light or dark | Senior decision makers who are not technical |
| Purpose | Inform, decide or persuade decides the ending slide | Inform, ending with next steps |
| Language | Body text language; technical terms stay English | The language the person wrote in |
| Source material | Rebuild vs write from scratch | Ask; never invent content to fill a deck |
| Length | Slide budget | 12 to 18 slides for a 20 minute slot |
| Output and preset | Build route and tokens | PowerPoint, `neutral-light` |

## Guided mode: one round of questions

Ask in a single round, multiple choice where the tool allows it, four questions at most. Good questions for this skill:

1. **Language.** "Body text in Bahasa Indonesia with English technical terms, full Bahasa, or full English?"
2. **Depth.** "Keep every use case at one to two slides each, keep only the strongest, or one flagship case in depth?"
3. **Output.** "PowerPoint file, Google Slides in your Drive, or a Claude Slides artifact?"
4. **Look.** "Your organisation's design system, the neutral light preset, or the dark briefing preset?"

Only ask what changes the build. Do not ask about things with a sensible default (fonts, page numbers, footer).

## Reading the person

- A non-technical requester gets guided mode, plain explanations of choices, and a short list of judgement calls at the end.
- A requester who gives audience, purpose and language in the first message gets quick mode.
- When the person says the audience is senior (ministers, generals, a CEO, a board), assume they read headlines only: every headline must carry the point, and detail goes to notes or an appendix.

## Sensitive material

Ask once, early, if the material looks confidential (classification markings, "do not distribute", security incidents): "Should the deck carry a handling caveat, and are there names or numbers that must stay off the slides?" Put the caveat in `meta.footer`.
