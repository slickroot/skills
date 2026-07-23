# Skills

A small set of Claude skills inspired by extreme programming.

- **xp-meeting** — grills you with questions about an idea, then turns it into user stories filed as GitHub issues.
- **xp-implement** — takes a GitHub issue, works in a git worktree, builds it in thin slices with TDD, and opens a PR.
- **xp-review** — takes a PR, explains what was done, and discusses how to review it, including design and coding patterns.

## Install

Symlink the skill folders into your skills directory, e.g. `~/.claude/skills/`:

```sh
ln -s "$PWD"/xp-meeting "$PWD"/xp-implement "$PWD"/xp-review ~/.claude/skills/
```
