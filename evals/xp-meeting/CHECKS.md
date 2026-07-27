# xp-meeting checks

Written down before a run, so a run isn't scored on how it felt. All of them are
answerable by someone reading the session log and nothing else.

| id | check | pass condition |
|---|---|---|
| `SPLIT-1` | split into use cases that make sense | each issue is one use case a tester could exercise on a fresh checkout — and where it can't be, the issues blocking it are declared as GitHub dependency relationships |
| `SMALLEST-1` | smallest testable change first | all the issues are filed, ordered, and the first is the smallest change that can be tested end to end. Not setup, not scaffolding |
| `ONE-1` | one decision, one question, asked | every decision that ends up in a story was put to me as its own question, in its own turn, phrased as a question and answered by me. Fails if a decision is bundled onto another question, or announced as an intention — "I'd leave it alone", "I'll fold it in", "if you agree" — rather than asked |
| `HANDS-1` | nothing in a story needs my hands | any step I have to run myself — a migration, a console change, a key, a deploy — is its own issue labelled `task`, never a slice inside a story. The story that needs it declares it as a blocker |
| `CLOSED-1` | no design left to the implementer | the issue spells out the actual names — columns, functions, endpoints, files — not "store the user's answer". Every new file it creates is named, and every mechanism it describes — an env var, a flag, a column — is given its actual identifier. Two implementers reading it would produce the same shape and the same names |

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
ONE-1       pass/fail/n-a   turn __  "..."
HANDS-1     pass/fail/n-a   turn __  "..."
CLOSED-1    pass/fail/n-a   turn __  "..."

notes:      anything no check covers — this is where the next check comes from
one edit:   which check it targets, and what you expect to move next run
```
