# Read the tape

GitHub issue: https://github.com/slickroot/skills/issues/1

## User Story

As the owner of the xp-stories skill, I want to list my past planning sessions and read any one of them as plain dialogue, so I can see for myself how the skill behaves and decide what to change in its text.

## Acceptance Criteria

- I run one command with a number of days (default 7) and get every `/xp-stories` session in that window: date, the request I opened with, and how many turns it took.
- The list can be sorted by length, so I can pick short and long ones deliberately.
- I pick one session and get the whole back-and-forth as clean readable dialogue — my turns and the skill's turns, in order.
- Tool output, internal chatter, and sub-agent work are stripped out; I see only the conversation.
- Read-only: it reads history already on this machine, and changes nothing about any skill.
- It works across all projects on this machine, not just the current one.

## Estimate

2 points

## Technical Design

### Approach

A single standalone script, `tools/tape`, executable with a `#!/usr/bin/env python3` shebang, Python 3 standard library only. No new dependencies, no package manifest, no skill file. It reads Claude Code's session transcripts that already exist on this machine and prints to stdout.

Two subcommands:

- `tools/tape list [--days N] [--sort length|date]` — every `/xp-stories` invocation in the window, one row each.
- `tools/tape read <index>` — the full dialogue of one row from the last listing.

`list` writes the ordered listing to a cache file so `read` can resolve a short index instead of a 36-character session UUID.

### Where the data comes from

Session transcripts live at `~/.claude/projects/<slugified-project-path>/<session-id>.jsonl`. One directory per project; scanning the whole tree is what makes this work across all projects. Each line is one JSON object.

Relevant line shapes:

- `type: "user"` with `message.role: "user"`. `message.content` is either a plain string (a real message) or a list of blocks. A list whose blocks are `type: "tool_result"` is tool output, not a person talking.
- `type: "assistant"` with `message.content` a list of blocks, each `type` being `text`, `thinking`, or `tool_use`.
- Every line may carry `isSidechain: true`, meaning it belongs to a sub-agent, not the main conversation.
- Conversation lines carry `timestamp` (ISO 8601, UTC) and `cwd` (the project path).
- Other line types appear interleaved: `attachment`, `system`, `mode`, `permission-mode`, `file-history-snapshot`, `file-history-delta`, `cost-state`, `bridge-session`, `ai-title`, `last-prompt`, `atis-latch`.

An `/xp-stories` invocation is a `user` line whose content contains the literal string `<command-name>/xp-stories</command-name>`. That marker, and only that marker, identifies a session. Matching the bare word `xp-stories` anywhere is wrong — many sessions merely discuss the skill.

The text typed after the command sits in the same content, inside `<command-args>` … `</command-args>`.

### Definitions to apply exactly

**Human turn.** A line where `type` is `user`, `isSidechain` is not `true`, and `message.content` is not a list of `tool_result` blocks. Nothing else is a human turn — not assistant lines, not any of the non-conversation line types above.

**Session.** One `/xp-stories` invocation plus every line after it to the end of the file. A file containing two invocations yields two sessions; the second starts at the second invocation. Content before an invocation belongs to no session and is never shown.

**Session date.** The `timestamp` of the invocation line, converted to local time and rendered `YYYY-MM-DD`. Never file modification time.

**Turn count.** The number of human turns in the session, with the invocation itself counted as turn 1.

**Opening request.** The `<command-args>` text of the invocation, whitespace collapsed to single spaces. If the args are empty or absent, fall back to the text of the first human turn after the invocation, same whitespace treatment. For the `list` display only, truncate to 160 characters and append `…` when truncated.

**Project path.** The `cwd` value from the invocation line.

### Configuration

Two environment variables, each with a default. They exist so tests can point the script at fixture data; they are not part of the everyday command surface.

- `XP_TAPE_PROJECTS_DIR` — root of the transcript tree. Default `~/.claude/projects`.
- `XP_TAPE_CACHE` — path of the listing cache file. Default `~/.cache/xp-tape/last-list.json`.

### The cache file

Written by `list` on every run, replacing whatever was there. Created along with any missing parent directories. It records, in listing order, one entry per row: the absolute path of the transcript file, the line number (or equivalent stable position) of the invocation within that file, the session id, the date string, the turn count, and the project path. `read` needs enough to reproduce a session without rescanning, and the file path plus invocation position is enough.

This is the only file the tool writes.

### `tools/tape list`

1. Resolve the window: `--days N`, default 7. Keep sessions whose invocation timestamp is within the last N days from the moment the command runs.
2. Walk every `*.jsonl` file under `XP_TAPE_PROJECTS_DIR`, at any depth.
3. In each file, find every invocation line, and for each one build a session per the definitions above.
4. Drop sessions outside the window.
5. Order them. Default `--sort date`: most recent invocation first. `--sort length`: by turn count, longest first.
6. Print one row per session: a 1-based index, the date, the turn count, and the truncated opening request. Columns aligned so the listing reads as a table.
7. Write the cache file.

The session id is not printed; the index is how a session is selected.

### `tools/tape read <index>`

1. Load the cache file. If it does not exist, print `no listing found, run: tools/tape list` to stderr and exit with a non-zero status.
2. If the index is outside the range of cached entries, print `only <N> sessions in the last listing` to stderr and exit with a non-zero status.
3. Open the recorded transcript file and take the session starting at the recorded invocation position through the end of the file.
4. Print the header: date, turn count, and project path, separated by ` · `. For example `2026-08-28 · 32 turns · /Users/dev/code/skills`. Then a blank line.
5. Walk the session's lines in file order and print the conversation, turns separated by blank lines, each turn being a speaker label on its own line followed by the text.
   - A human turn prints under the label `Me:`.
   - An assistant line prints under the label `xp-stories:`, showing the concatenation of its `text` blocks only.
   - The invocation prints as the first `Me:` turn, showing only the `<command-args>` text with the `<command-message>` and `<command-name>` tags and their contents removed. If the args were empty, that turn prints `/xp-stories`.
6. Text within a turn is printed as it appears; do not reflow, re-wrap, or reformat it.

Stripped, and never printed:

- `tool_use` blocks and the `tool_result` user lines that answer them
- `thinking` blocks
- every line with `isSidechain: true`
- every line whose `type` is not `user` or `assistant`
- inside human turns, any `<system-reminder>` … `</system-reminder>` and `<local-command-stdout>` … `</local-command-stdout>` block, tags and contents both
- an assistant line with no `text` blocks, or whose text is empty after stripping, produces no turn at all — no label, no blank line

### Slices

1. `list` for the current project only: window filter, detection by command marker, date and turn count and opening request, default ordering.
2. Extend the walk to the whole projects tree, and add `--sort length`.
3. The cache file.
4. `read`, including the header, labels, stripping rules, and the two error states.

### Do not do

- Do not add any third-party dependency, package manifest, lockfile, virtualenv, or build step.
- Do not write a `SKILL.md` or any skill wrapper for this. The user runs the script directly.
- Do not write anything anywhere except the cache file. Nothing under `XP_TAPE_PROJECTS_DIR` is ever opened for writing, moved, or deleted.
- Do not modify, read for modification, or otherwise touch any skill in this repo.
- Do not detect sessions by searching for the bare string `xp-stories`; only the `<command-name>` marker counts.
- Do not add subcommands, flags, or output formats beyond those specified — no `--json`, no `--limit`, no search, no export, no grep-across-sessions.
- Do not add colour, a pager, interactive selection, or a TUI. Plain text to stdout.
- Do not summarise, shorten, redact, or otherwise alter turn text in `read`. `list` truncation at 160 characters is the only truncation in the tool.
- Do not add caching, indexing, or a database beyond the single listing cache file.
- Do not handle failure states other than the two specified for `read`. A malformed or unreadable line is skipped silently; do not build error reporting, recovery, or repair around it.
- Do not print the session UUID in the `list` output.

### Verification

Tests use `unittest` from the standard library, live in `tools/test_tape.py`, and run with `python3 -m unittest discover tools`. Each test builds handcrafted `.jsonl` fixtures inside a `tempfile.TemporaryDirectory()`, points `XP_TAPE_PROJECTS_DIR` and `XP_TAPE_CACHE` at it, and asserts on the script's stdout, stderr, and exit status.

`list`:

1. A session invoked inside the window appears; one invoked before the window does not.
2. A session that mentions `xp-stories` in prose but never invokes the command does not appear.
3. A file containing two invocations produces two rows.
4. Fixtures under two different project directories both appear in a single listing.
5. `--sort length` orders rows by turn count, and produces a different order than the default for the same fixtures.
6. Turn count counts only human turns: a fixture padded with assistant lines, `tool_result` user lines, and `isSidechain: true` lines reports the same count as the equivalent fixture without them.
7. The opening request is taken from `<command-args>`; with empty args, it falls back to the first human message.
8. A request longer than 160 characters is truncated and ends with `…`.

`read`:

9. Turns print in file order with `Me:` and `xp-stories:` labels, and the header carries the date, the turn count, and the project path.
10. A fixture containing `tool_use`, `tool_result`, `thinking`, an `isSidechain: true` line, and a `<system-reminder>` block emits none of that text.
11. An assistant line that is only a tool call produces no empty turn.
12. Content appearing before the invocation line is not printed.
13. `read 2` returns the second session of the preceding `list`, and still does so after `--sort length` has reordered the listing.
14. `read` with no cache file, and `read` with an out-of-range index, each exit non-zero with the specified message.

Read-only:

15. Content hashes of every fixture file under the projects directory are identical before and after running both subcommands.

### Open questions

None. Anything not covered above is out of scope for this story.
