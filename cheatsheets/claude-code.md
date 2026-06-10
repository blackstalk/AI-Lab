# Claude Code Cheat Sheet

## HOW CC STARTS EVERY SESSION
CC reads context in this order on startup:
  1. ~/.claude/CLAUDE.md         — global instructions (all projects)
  2. <project>/CLAUDE.md         — project-level instructions
  3. <subdir>/CLAUDE.md          — directory-level instructions (if present)
  4. Memory files                — persistent facts from past sessions
  5. Current working directory   — file tree, git log, git status

Everything in CLAUDE.md is injected into every conversation automatically.
You never have to repeat yourself if it's in CLAUDE.md.

---

## CLAUDE.md — what to put in it
| Section              | What goes here                                      |
|----------------------|-----------------------------------------------------|
| Project description  | What this repo is and who it's for                  |
| Conventions          | File structure, naming, commit style                |
| How to work with me  | Tone, depth, what to avoid                          |
| Stack                | Languages, frameworks, tools in use                 |
| Current progress     | Active work so CC has context without re-explaining |
| Banned actions       | Things CC should never do (force push, rm -rf, etc) |

CLAUDE.md is code — keep it updated as the project evolves.

---

## MEMORY SYSTEM
CC maintains memory files at:
  ~/.claude/projects/<project-path>/memory/

| Memory type | What it stores                                      |
|-------------|-----------------------------------------------------|
| user        | Who you are, your background, your preferences      |
| feedback    | Corrections and confirmations about how to work     |
| project     | Goals, decisions, deadlines, context                |
| reference   | Where to find things (Linear, Grafana, Slack, etc.) |

Memory is written automatically when CC learns something worth keeping.
You can ask CC to remember or forget something explicitly.

---

## SLASH COMMANDS (built-in)
| Command          | Action                                              |
|------------------|-----------------------------------------------------|
| /help            | Show all available commands                         |
| /clear           | Clear conversation context (keeps memory)           |
| /memory          | Show current memory files                           |
| /config          | Open settings (theme, model, etc.)                  |
| /cost            | Show token usage for this session                   |
| /review          | Run a code review on current branch                 |
| /init            | Generate a CLAUDE.md for the current project        |

---

## SKILLS (user-invocable slash commands)
Skills are extensions — more powerful than built-in commands.

| Skill              | When to use it                                      |
|--------------------|-----------------------------------------------------|
| /code-review       | Review current diff (low/medium/high/ultra depth)   |
| /run               | Launch and drive the app to verify a change         |
| /verify            | Confirm a fix actually works end-to-end             |
| /simplify          | Clean up changed code for reuse and efficiency      |
| /security-review   | Security audit of pending changes                   |
| /update-config     | Modify settings.json, add permissions, set env vars |
| /schedule          | Schedule a recurring remote agent                   |

---

## TOOL PERMISSIONS
CC asks before running tools that could be destructive.
You can pre-approve tools to avoid repeated prompts.

Permission levels:
  - Auto-approved   — read-only tools (Read, Grep, LS)
  - Prompt once     — write tools (Edit, Write, Bash)
  - Always prompt   — destructive tools (rm, git push, etc.)

To add a permission: ask CC to "/update-config allow <command>"

---

## CONTEXT WINDOW TIPS
| Situation                        | What to do                        |
|----------------------------------|-----------------------------------|
| CC seems to forget earlier work  | It was compressed — check memory  |
| Starting a new task              | /clear to drop irrelevant context |
| CC doesn't know project layout   | Update CLAUDE.md with structure   |
| Repeating yourself session after | Add it to CLAUDE.md or memory     |

---

## AGENTS & SUBAGENTS
CC can spawn specialized subagents for parallel or isolated work:

| Agent type       | Use case                                            |
|------------------|-----------------------------------------------------|
| Explore          | Search/locate code across large codebases           |
| Plan             | Design implementation strategy before writing code  |
| general-purpose  | Research, multi-step tasks, web fetch               |

Subagents start with no context from the parent conversation —
always write self-contained prompts when spawning them.

---

## KEY MENTAL MODELS
1. CC reads files — it doesn't hallucinate your code, it reads it
2. CLAUDE.md is a prompt — write it like you're briefing a new teammate
3. Memory persists, context doesn't — /clear is safe, losing memory isn't
4. Permissions are durable — set them once in settings, not per-session
5. CC is an agent, not a chat — it can take actions, not just answer questions
