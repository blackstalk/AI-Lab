# NeoVim Cheat Sheet

## MODES
| Key        | Action                          |
|------------|---------------------------------|
| i          | Insert before cursor            |
| a          | Insert after cursor             |
| I          | Insert at start of line         |
| A          | Insert at end of line           |
| o          | New line below, insert          |
| O          | New line above, insert          |
| v          | Visual (character)              |
| V          | Visual (line)                   |
| Ctrl-v     | Visual block                    |
| Esc        | Back to Normal mode             |

---

## NAVIGATION (Normal mode)
| Key        | Action                          |
|------------|---------------------------------|
| h j k l    | Left / Down / Up / Right        |
| w          | Next word start                 |
| b          | Previous word start             |
| e          | End of word                     |
| 0          | Start of line                   |
| ^          | First non-blank of line         |
| $          | End of line                     |
| gg         | Top of file                     |
| G          | Bottom of file                  |
| {  }       | Jump between blank lines        |
| Ctrl-d     | Half page down (centered)       |
| Ctrl-u     | Half page up (centered)         |
| %          | Jump to matching bracket        |
| *          | Search word under cursor        |
| #          | Search word under cursor (back) |

---

## OPERATORS + MOTIONS   [operator][motion]
| Operator   | Meaning                         |
|------------|---------------------------------|
| d          | Delete                          |
| c          | Change (delete + insert mode)   |
| y          | Yank (copy)                     |
| >          | Indent right                    |
| <          | Indent left                     |

| Motion     | Meaning                         |
|------------|---------------------------------|
| w          | To next word                    |
| $          | To end of line                  |
| gg         | To top of file                  |
| G          | To bottom of file               |
| iw         | Inside word                     |
| i"         | Inside quotes                   |
| i(         | Inside parentheses              |
| i{         | Inside braces                   |
| a"         | Around quotes (includes them)   |

| Combo      | Meaning                         |
|------------|---------------------------------|
| dw         | Delete word                     |
| d$         | Delete to end of line           |
| dd         | Delete whole line               |
| ciw        | Change inner word               |
| ci"        | Change inside quotes            |
| ci(        | Change inside parens            |
| yy         | Yank whole line                 |
| >G         | Indent from here to bottom      |
| 3dd        | Delete 3 lines                  |
| 5j         | Move down 5 lines               |

---

## EDIT ACTIONS
| Key        | Action                          |
|------------|---------------------------------|
| u          | Undo                            |
| Ctrl-r     | Redo                            |
| p          | Paste below                     |
| P          | Paste above                     |
| x          | Delete character under cursor   |
| r          | Replace character under cursor  |
| .          | Repeat last change              |
| ~          | Toggle case of character        |

---

## SEARCH
| Key        | Action                          |
|------------|---------------------------------|
| /pattern   | Search forward                  |
| ?pattern   | Search backward                 |
| n          | Next match (centered)           |
| N          | Previous match (centered)       |
| Esc        | Clear highlights                |

---

## WINDOWS & SPLITS
| Key        | Action                          |
|------------|---------------------------------|
| Ctrl-h     | Move to left window             |
| Ctrl-j     | Move to window below            |
| Ctrl-k     | Move to window above            |
| Ctrl-l     | Move to right window            |
| :sp        | Horizontal split                |
| :vsp       | Vertical split                  |
| :q         | Close window                    |

---

## CUSTOM KEYMAPS (leader = Space)
| Key          | Action                        |
|--------------|-------------------------------|
| Space w      | Save file                     |
| Space q      | Quit                          |
| -            | Open oil.nvim (file tree)     |
| Space f f    | Telescope: find files         |
| Space f g    | Telescope: live grep          |
| Space f b    | Telescope: open buffers       |
| Space f h    | Telescope: help tags          |
| Space f r    | Telescope: recent files       |

---

## OIL.NVIM (filesystem buffer)
| Key        | Action                          |
|------------|---------------------------------|
| -          | Open parent directory           |
| Enter      | Open file or directory          |
| -          | Go up one directory             |
| _          | Open current working directory  |
| r          | Rename (edit inline, then :w)   |
| d          | Mark for delete (then :w)       |
| g?         | Show all oil keymaps            |

---

## TELESCOPE
| Key        | Action                          |
|------------|---------------------------------|
| Type       | Fuzzy filter results            |
| Ctrl-j/k   | Move down / up results          |
| Enter      | Open file                       |
| Ctrl-x     | Open in horizontal split        |
| Ctrl-v     | Open in vertical split          |
| Ctrl-t     | Open in new tab                 |
| Esc        | Close                           |
| Ctrl-/     | Show all Telescope keymaps      |

### Telescope pickers (Space f _)
| Picker       | What it searches                |
|--------------|---------------------------------|
| find_files   | File names (uses fd)            |
| live_grep    | File contents (uses ripgrep)    |
| buffers      | Currently open buffers          |
| help_tags    | NeoVim built-in docs            |
| oldfiles     | Recently opened files           |

### fzf-native
A C extension that replaces Telescope's default Lua sorter.
Faster matching, especially on large projects.
Loaded automatically — no extra keymaps needed.

### plenary.nvim
Utility library used internally by Telescope (and many other plugins).
You don't interact with it directly.

---

## LAZY.NVIM (plugin manager)
| Command        | Action                        |
|----------------|-------------------------------|
| :Lazy          | Open plugin manager UI        |
| :Lazy update   | Update all plugins            |
| :Lazy sync     | Install missing, remove extra |
| :Lazy clean    | Remove unused plugins         |
| q              | Close Lazy UI                 |
