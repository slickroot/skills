# evals

A way to tell whether a change to a skill actually made it better, instead of hoping it did.

## The idea

Each skill gets a list of **checks** — things it should do, each answerable yes or no.

A **scenario** is a real feature you were going to work on anyway. Every time you use the
skill for real, that's a run. You don't invent prompts for the loop and you don't rerun
them — you build the thing afterwards, so the prompt is spent.

The loop rides along with the work. It costs you one grading step per meeting.

## The loop

1. Use the skill on real work, in the real project. Play yourself. Don't coach it — if it
   goes wrong, let it, that is what you came to see.
2. Save the prompt as the next `scenarios/sN.md`, verbatim.
3. Hand the session log to an agent along with the skill's `CHECKS.md`, and have it score.
4. Change **one** thing in the SKILL.md.
5. Next time you use the skill, that's the next run.

Give the agent nothing but the log and the checks. No history, no idea what you changed.

## Reading the results

There is no before/after on a fixed prompt — every scenario is different, because every
scenario is real. So a single pass proves nothing; it might just have been an easy feature.
What means something is a **streak across different scenarios**:

- A check that fails run after run is a skill problem, and your edits aren't touching it.
- A check that starts passing and keeps passing across several different features is fixed.
- A check that swings is usually badly worded, not badly behaved. Reword it.

Grade the same way every time or the runs aren't comparable — that is the whole reason the
checks are written down before the run rather than after.

## Layout

```
evals/
  render.py            turns a session log into readable text
  xp-meeting/
    CHECKS.md          the checks, and a tally block to copy per run
    scenarios/         one prompt per file, in the order you ran them
    runs/              one tally per run
```

One directory per skill. Add `xp-implement/` and `xp-review/` when you get to them.

## Housekeeping

- Stopped caring about a check → delete it.
- Noticed something no check covers → new check. The notes section of a run is where these
  come from.
- A check keeps failing for a reason you don't care about → rewrite it or drop it. It can't
  detect anything else while it's stuck.

Checks are yours to churn. The only rule worth keeping is **one edit per run**, otherwise
you can't tell which edit moved anything.

## Finding the session log

Logs live in `~/.claude/projects/<mangled-cwd>/<session-uuid>.jsonl`. Those paths start
with `-`, which most shell tools read as an option — prefix `./` or use an absolute path.

```
python3 render.py <log>
```
