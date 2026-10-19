# Natural copy gate

Run this on every headline, body line, note and talking point before you build. It is the slide version of the `antislop-copywriting` skill; load that skill too if it is installed.

## The loop

1. **Draft** the copy.
2. **Audit.** Answer two questions in a sentence each: "What here reads as AI-written?" and "Is there any fact, number, name, date or source that is not in the material?"
3. **Final.** Fix both. Search for em and en dashes one last time. `build_pptx.py` also flags dashes and common buzzwords; treat its warnings as part of the audit.

## Patterns to remove

| Pattern | Before | After |
|---|---|---|
| Empty AI vocabulary (unlock, seamless, elevate, empower, robust, game-changer, leverage, journey, landscape; revolusioner, terdepan, kelas dunia) | "Platform revolusioner untuk sinergi data" | "Satu tampilan untuk data dari 20+ instansi" |
| Significance inflation | "A new era of operational awareness" | "Watch officers see one track per vessel" |
| Not X, but Y | "Bukan sekadar dashboard, tetapi pusat komando" | "Dashboard menampilkan data yang dipilih" |
| Forced groups of three | "Faster, smarter, safer" | Use as many items as the content has |
| Staccato drama | "No sensors. No new budget. No waiting." | "It uses data the agencies already hold." |
| Generic upbeat close | "The future looks bright" | End on the last concrete fact or ask |
| Weasel attribution | "Experts agree…" | Name the source or cut the sentence |
| Signposting | "Let's dive in", "Mari kita bahas" | Just say the thing |
| Filler | "In order to", "Perlu diketahui bahwa" | "To", or cut |
| Stacked hedges | "could potentially possibly" | "may" |
| Inline-header bullets | "**Speed:** It is faster" | A sentence, or a table |
| Bold everywhere | Every key term bold | Bold one phrase per slide at most |
| Scare quotes and ALL-CAPS emphasis | The "solution" MUST be adopted NOW | Write the emphasis into the sentence |
| Em dashes (the long dash, U+2014, also en dash U+2013 and " -- ") | "The policy [em dash] announced without warning [em dash] affects…" | "The policy, announced without warning, affects…" |

## Not slop

- Uppercase **labels** set by a preset (eyebrows, table headers) are a design choice, not shouting.
- One short sentence for emphasis is fine; a run of them is the tell.
- A list of three is fine when there are three things.
- Formal vocabulary that is precise is fine. The tell is specific words, not long words.

## Voice

Stripping tells is half the job. Copy with no voice reads as machine-made too. When the person gives a sample of how they write, match it. Otherwise write like a capable presenter speaking to people they respect: direct, specific, calm.

## Checklist

- [ ] No invented numbers, names, dates, quotes or sources; every gap is `[__]`
- [ ] No buzzwords from the table above
- [ ] No em or en dashes anywhere, including titles and file names
- [ ] No "not X, but Y", forced trios, staccato runs or generic closers
- [ ] Every headline states a point
- [ ] Read aloud, it sounds like a person
