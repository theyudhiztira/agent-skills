#!/usr/bin/env python3
"""Export the talking points in a deck spec as HTML (for a Google Doc) or Markdown.

  python3 export_notes.py deck.json --format html -o talking-points.html
  python3 export_notes.py deck.json --format md   -o talking-points.md

HTML uploaded to Google Drive with conversion becomes a native Google Doc with
headings, bold key messages and bullets intact (see references/talking-points.md).
"""
import argparse
import html
import json
import sys

LABELS = {
    "id": {"key": "Pesan utama", "transition": "Transisi", "slide": "Slide"},
    "en": {"key": "Key message", "transition": "Transition", "slide": "Slide"},
}


def slide_title(sd):
    t = sd.get("title", "")
    if sd.get("layout") == "divider" and sd.get("index"):
        t = f"{sd['index']}_ {t}"
    return t or sd.get("layout", "")


def normalise(notes):
    if not notes:
        return None
    if isinstance(notes, str):
        return {"key": "", "points": [notes], "transition": ""}
    return {"key": notes.get("key", ""), "points": notes.get("points", []),
            "transition": notes.get("transition", "")}


def to_md(deck, lab):
    out = [f"# Talking points: {deck['meta'].get('title', '')}", ""]
    for i, sd in enumerate(deck["slides"], 1):
        n = normalise(sd.get("notes"))
        out.append(f"## {lab['slide']} {i:02d} · {slide_title(sd)}")
        if n:
            if n["key"]:
                out.append(f"**{lab['key']}: {n['key']}**")
                out.append("")
            out += [f"- {p}" for p in n["points"]]
            if n["transition"]:
                out += ["", f"**{lab['transition']}:** *{n['transition']}*"]
        out.append("")
    return "\n".join(out)


def to_html(deck, lab):
    e = lambda s: html.escape(s, quote=False)
    out = [f"<html><body><h1>Talking points: {e(deck['meta'].get('title', ''))}</h1>"]
    for i, sd in enumerate(deck["slides"], 1):
        n = normalise(sd.get("notes"))
        out.append(f"<h2>{lab['slide']} {i:02d} · {e(slide_title(sd))}</h2>")
        if n:
            if n["key"]:
                out.append(f"<p><b>{lab['key']}: {e(n['key'])}</b></p>")
            if n["points"]:
                out.append("<ul>" + "".join(f"<li>{e(p)}</li>" for p in n["points"]) + "</ul>")
            if n["transition"]:
                out.append(f"<p><b>{lab['transition']}:</b> <i>{e(n['transition'])}</i></p>")
    out.append("</body></html>")
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--format", choices=["html", "md"], default="html")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    deck = json.load(open(a.deck, encoding="utf-8"))
    lab = LABELS.get(deck.get("meta", {}).get("language", "en"), LABELS["en"])
    body = to_html(deck, lab) if a.format == "html" else to_md(deck, lab)
    if "\u2014" in body or "\u2013" in body:
        print("warning: em/en dash in the notes; fix the deck spec before exporting", file=sys.stderr)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(body)
        print("wrote", a.out)
    else:
        print(body)


if __name__ == "__main__":
    main()
