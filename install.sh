#!/usr/bin/env bash
# Install the ingredient-opportunity-research skill into your agent's skill path.
#
# Cloning this repository alone does NOT expose the skill: Codex discovers
# skills from ~/.codex/skills (personal) or <project>/.agents/skills
# (repo-level), Claude Code from .claude/skills, Kimi Code from
# ~/.kimi-code/skills, and DeepSeek Harness from .dsh/skills or
# .agents/skills. This script copies the whole skill bundle (SKILL.md +
# references/) to the target so it is actually discovered.
#
# Usage:
#   ./install.sh                     # interactive
#   ./install.sh --codex             # personal Codex  -> ~/.codex/skills/
#   ./install.sh --claude            # Claude Code     -> .claude/skills/  (repo)
#   ./install.sh --project           # repo-level      -> .agents/skills/  (Codex/Kimi/DSH)
#   ./install.sh --kimi              # Kimi Code       -> ~/.kimi-code/skills/
#   ./install.sh --dsh               # DeepSeek Harness-> .dsh/skills/     (repo)
#   ./install.sh --all               # codex + project + claude
set -euo pipefail
cd "$(dirname "$0")"

SKILL_SRC="skill/ingredient-opportunity-research"
SKILL_NAME="ingredient-opportunity-research"
if [ ! -f "$SKILL_SRC/SKILL.md" ]; then
  echo "error: skill bundle not found at $SKILL_SRC" >&2
  exit 1
fi

install_to() {
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  if [ -e "$dest" ]; then
    rm -rf "$dest"
  fi
  cp -R "$SKILL_SRC" "$dest"
  echo "installed: $dest"
}

mode="${1:-interactive}"
case "$mode" in
  --codex)   install_to "$HOME/.codex/skills/$SKILL_NAME" ;;
  --claude)  install_to ".claude/skills/$SKILL_NAME" ;;
  --project) install_to ".agents/skills/$SKILL_NAME" ;;
  --kimi)    install_to "$HOME/.kimi-code/skills/$SKILL_NAME" ;;
  --dsh)     install_to ".dsh/skills/$SKILL_NAME" ;;
  --all)
    install_to "$HOME/.codex/skills/$SKILL_NAME"
    install_to ".agents/skills/$SKILL_NAME"
    install_to ".claude/skills/$SKILL_NAME"
    ;;
  interactive)
    echo "Where should the skill be installed?"
    echo "  1) Personal Codex      (~/.codex/skills)      — usable in every project"
    echo "  2) Repo-level          (.agents/skills)       — Codex / Kimi Code / DSH in this repo"
    echo "  3) Claude Code         (.claude/skills)       — in this repo"
    echo "  4) Kimi Code personal  (~/.kimi-code/skills)"
    echo "  5) DeepSeek Harness    (.dsh/skills)          — in this repo"
    read -rp "Choose 1-5: " choice
    case "$choice" in
      1) install_to "$HOME/.codex/skills/$SKILL_NAME" ;;
      2) install_to ".agents/skills/$SKILL_NAME" ;;
      3) install_to ".claude/skills/$SKILL_NAME" ;;
      4) install_to "$HOME/.kimi-code/skills/$SKILL_NAME" ;;
      5) install_to ".dsh/skills/$SKILL_NAME" ;;
      *) echo "invalid choice" >&2; exit 2 ;;
    esac
    ;;
  *)
    echo "usage: ./install.sh [--codex|--claude|--project|--kimi|--dsh|--all]" >&2
    exit 2
    ;;
esac

echo
echo "Next step: in the agent, say"
echo '  Use the ingredient-opportunity-research skill. Research the market opportunity for <ingredient> in <geography/application area>.'
