# xp-meeting checks

Written down before a run, so a run isn't scored on how it felt. All of them are
answerable by someone reading the session log and nothing else.

| id | check | pass condition |
|---|---|---|
| `SPLIT-1` | split into use cases that make sense | each issue is one use case a tester could exercise on a fresh checkout — and where it can't be, the issues blocking it are declared as GitHub dependency relationships |
| `SMALLEST-1` | smallest testable change first | all the issues are filed, ordered, and the first is the smallest change that can be tested end to end. Not setup, not scaffolding |
| `CLOSED-1` | no design left to the implementer | the issue spells out the actual names — columns, functions, endpoints, files — not "store the user's answer". Two implementers reading it would produce the same shape and the same names |

Verdicts are **pass / fail / n-a**. Nothing in between. If a verdict wants to be "sort
of", the check is badly worded — record that and reword it after the run, never during.

## Tally

Copy this per run.

```
run:        NN
date:
scenario:   s1
SKILL.md:   <git log -1 --format=%h -- xp-meeting/SKILL.md>
log:        <path>

SPLIT-1     pass/fail/n-a   turn __  "..."
SMALLEST-1  pass/fail/n-a   turn __  "..."
CLOSED-1    pass/fail/n-a   turn __  "..."

notes:      anything no check covers — this is where the next check comes from
one edit:   which check it targets, and what you expect to move next run
```
