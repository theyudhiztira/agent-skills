#!/usr/bin/env bash
# Symlink every skill in this repo into the local agent skill folders, so `git pull`
# updates what your agents load. For maintainers and for anyone installing by hand.
#
#   bash scripts/link-skills.sh            # ~/.claude/skills and ~/.agents/skills
#   bash scripts/link-skills.sh <dir>...   # custom destinations, e.g. ~/.codex/skills
#
# Re-run after adding, removing or renaming a skill.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
if [ $# -gt 0 ]; then
  DESTS=("$@")
else
  DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills")
fi

# macOS ships bash 3.2, so no mapfile
SKILLS=()
while IFS= read -r dir; do SKILLS+=("$dir"); done < <(
  find "$REPO/skills" -name SKILL.md -not -path "*/node_modules/*" -not -path "*/deprecated/*" -exec dirname {} \; | sort)

for dest in "${DESTS[@]}"; do
  if [ -L "$dest" ]; then
    target="$(cd "$dest" && pwd -P)"
    case "$target" in
      "$REPO"|"$REPO"/*) echo "error: $dest is a symlink into this repo. Delete it and re-run." >&2; exit 1 ;;
    esac
  fi
  mkdir -p "$dest"
  for src in "${SKILLS[@]}"; do
    name="$(basename "$src")"
    if [ -e "$dest/$name" ] && [ ! -L "$dest/$name" ]; then
      rm -rf "$dest/$name"
    fi
    ln -sfn "$src" "$dest/$name"
    echo "linked $dest/$name"
  done
done

if ! python3 -c "import pptx" 2>/dev/null; then
  echo
  echo "presentation needs python-pptx:  pip install python-pptx pillow"
fi
