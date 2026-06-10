# Lab — AI Engineering Learning Repository

## What this repo is
A hands-on lab for learning NeoVim, Claude Code, GitHub Actions, MCP servers,
and agent workflows. Every directory is an exercise or a reference artifact.

## My learning goals
1. NeoVim — modal editing, plugins, LSP
2. Claude Code — primitives, memory, permissions, skills
3. GitHub Actions — CI/CD, automation
4. MCP servers — building and connecting tool servers
5. Agent workflows — multi-agent orchestration

## How to mentor me
- Explain *why* before *how* — I want to understand the model, not just copy commands
- Build progressively — each exercise should reference what came before
- Call out when I'm about to do something that would be bad practice in production
- Short responses over long ones — I can ask for more

## Repo conventions
- Exercises live in /exercises/<track>/<exercise-name>/
- Each exercise gets a README.md with goal and success criteria
- Reference material (cheat sheets, notes) lives in /cheatsheets/
- Never commit secrets, API keys, or .env files

## Current progress
- NeoVim A-1 ✓  Minimal config: options, keymaps, lazy.nvim, catppuccin, oil.nvim
- NeoVim A-2 ✓  Telescope with fzf-native
- Claude Code B-1 → in progress

## Stack
- macOS, zsh, Homebrew
- NeoVim 0.12+ with Lua config
- Python 3, Node.js (via nvm), Bun
