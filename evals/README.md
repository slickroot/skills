# evals

A way to tell whether a change to a skill actually made it better, instead of hoping it did.

## The idea

Each skill gets a list of **checks** — things it should do, each answerable yes or no.

Each thing you want to fix gets a **scenario** — one fixed prompt you run the skill against.

You loop one scenario at a time until it comes out good.

## The loop

1. Open a fresh Claude session in the real project.
2. Run the skill on the scenario prompt, pasted exactly. Play yourself. Don't coach it —
   if it goes wrong, let it, that is what you came to see.
3. Hand the session log to an agent along with the skill's `CHECKS.md`, and have it score.
4. Change **one** thing in the SKILL.md.
5. Run it again.

Give the agent nothing but the log and the checks. No history, no idea what you changed.

## Layout

```
evals/
  render.py            turns a session log into readable text
  xp-meeting/
    CHECKS.md          the checks, and a tally block to copy per run
    scenarios/s1.md    one prompt per file
    runs/              one tally per run
```

One directory per skill. Add `xp-implement/` and `xp-review/` when you get to them.

## Housekeeping

- Notice something wrong with a skill → new scenario.
- Want to improve something → new scenario.
- Stopped caring about a check → delete it.
- Noticed something no check covers → new check.

Checks and scenarios are yours to churn. The only rule worth keeping is **one edit per
run**, otherwise you can't tell which edit moved anything.

## Finding the session log

Logs live in `~/.claude/projects/<mangled-cwd>/<session-uuid>.jsonl`. Those paths start
with `-`, which most shell tools read as an option — prefix `./` or use an absolute path.

```
python3 render.py <log>
```
