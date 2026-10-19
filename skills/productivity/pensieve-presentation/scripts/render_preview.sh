#!/usr/bin/env bash
# Render a .pptx to PNG previews so you can look at every slide before delivering.
# Needs LibreOffice (soffice) and poppler (pdftoppm).
#   bash render_preview.sh deck.pptx [out_dir] [dpi]
set -euo pipefail
pptx="$1"
out="${2:-$(dirname "$pptx")/preview}"
dpi="${3:-48}"
mkdir -p "$out"
command -v soffice >/dev/null || { echo "LibreOffice (soffice) not found; open the .pptx and check it by eye instead."; exit 1; }
soffice --headless --convert-to pdf --outdir "$out" "$pptx" >/dev/null 2>&1
pdf="$out/$(basename "${pptx%.*}").pdf"
command -v pdftoppm >/dev/null || { echo "pdftoppm not found; open $pdf instead."; exit 1; }
pdftoppm -png -r "$dpi" "$pdf" "$out/slide"
echo "previews in $out"
ls "$out"/slide-*.png
