# Skills

Hi, my name is Marouane.

I'm a big fan of XP — Extreme Programming. I read the book when I was still studying, almost two decades ago. Unfortunately I never had the chance to apply XP, because I never joined a team that worked with it, and I obviously could not do it by myself — I could not pair program with myself. I did TDD and refactoring, and whenever I worked with somebody I tried to do pair programming, but people generally don't like it much. They don't like to write tests first and all that stuff.

Now with AI coding agents, this is my chance to finally explore it. I'm super excited to start with a few skills and keep working on them until this becomes the perfect development process for me. If someone else finds this useful, they are welcome to use it too.

## The skills

The skills follow the XP loop: plan together, build in small steps, review together.

- **[xp-stories](xp-stories/SKILL.md)** — turns raw input (feedback, complaints, ideas) into a ranked stack of small story cards. It digs for the pain behind what I asked for, splits by user activity, and gates every card on three tests: can I demo it, is it under 3–5 scenarios, is it still useful shipped alone. New and still rough — it only runs when I type `/xp-stories` myself, and the XP-spec and XP-spike it hands off to don't exist yet.
- **[xp-meeting](xp-meeting/SKILL.md)** — a planning meeting. The agent does its homework on the codebase first, then asks you one question at a time (always with its own suggestion) until the idea is clear, and files the resulting user stories as GitHub issues.
- **[xp-sync](xp-sync/SKILL.md)** — the cleanup pass after a planning meeting. Give it the session summary and it files the agreed stories as GitHub issues, opens a spec file under `docs/specs/` for each one, and rewrites `docs/parking-lot.md`. No chat, no brainstorming — it just writes the files and tells you what it touched. Like xp-stories, it only runs when I type `/xp-sync` myself.
- **[xp-tech-design](xp-tech-design/SKILL.md)** — the architecture meeting between the story and the code. It locks the scope, then asks one question at a time until the data schema, the API and failure states, the file boundaries and the tests are all decided. The output is a standalone spec, including a "do not do" section, that leaves the coding agent no room to invent anything. Runs only when I type `/xp-tech-design`.
- **[xp-implement](xp-implement/SKILL.md)** — takes a GitHub issue, works in a fresh git worktree, splits the story into thin vertical slices, builds each slice with TDD, and opens a PR linked to the issue.
- **[xp-review](xp-review/SKILL.md)** — takes a PR, explains in plain words what was done, walks through the code like a pair partner, and answers your questions. You are the reviewer; it discusses the design and coding patterns and gives a clear verdict.

## Install

Symlink the skill folders into your skills directory, e.g. `~/.claude/skills/`:

```sh
ln -s "$PWD"/xp-stories "$PWD"/xp-meeting "$PWD"/xp-sync "$PWD"/xp-tech-design "$PWD"/xp-implement "$PWD"/xp-review ~/.claude/skills/
```

Symlinks mean any edit in this repo is live right away — no reinstalling.

## Status

Work in progress. These skills are short and simple on purpose; I refine them as I use them.
