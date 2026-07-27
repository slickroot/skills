# xp-meeting checks

Written down before a run, so a run isn't scored on how it felt. All of them are
answerable by someone reading the session log and nothing else.

| id | check | pass condition |
|---|---|---|
| `ONE-1` | one decision, one question, asked | every decision that ends up in a story was put to me as its own question, in its own turn, and answered by me. Fails if one question carries two decisions, or if a decision is announced as settled rather than asked — "I'd leave it alone", "X stays out of scope", "understood, so Y" |
| `ONE-2` | nothing in a story I was never asked about | every name, number, path, deletion and bit of scope in the story traces back to an answer I gave, or to a fact from the repo. Fails on anything that first appears in the story itself, and on anything that slipped in beside a question about something else — in a recap, in an aside, or inside the suggestion |
| `HANDS-1` | nothing in a story needs my hands | any step I have to run myself — a migration, a console change, a key, a deploy — is its own issue labelled `task`, never a slice inside a story. The story that needs it declares it as a blocker |
| `CLOSED-1` | no design left to the implementer | the issue spells out the actual names — columns, functions, endpoints, files — not "store the user's answer". Every new file it creates is named, and every mechanism it describes — an env var, a flag, a column — is given its actual identifier. Two implementers reading it would produce the same shape and the same names |
| `SPLIT-1` | *parked* — split into use cases that make sense | each issue is one use case a tester could exercise on a fresh checkout — and where it can't be, the issues blocking it are declared as GitHub dependency relationships |
| `SMALLEST-1` | *parked* — smallest testable change first | all the issues are filed, ordered, and the first is the smallest change that can be tested end to end. Not setup, not scaffolding |

Verdicts are **pass / fail / n-a**. Nothing in between. If a verdict wants to be "sort
of", the check is badly worded — record that and reword it after the run, never during.

**Parked** means still graded and still recorded, but not driving edits. Both parked checks
open on "the issues are filed", so they mostly measure whether a meeting reached
`gh issue create` — run 03 called them unusable for that reason and it still stands. Leave
them alone until `ONE-1` and `ONE-2` are done, then rewrite them.

`ONE-1` was one check through runs 01–05 and failed all five, in three different shapes:
two decisions on one question, a decision announced as settled, and a decision that simply
appears in the story with no turn behind it. One verdict couldn't say which shape moved, so
the third shape is now `ONE-2`. Earlier runs read as `ONE-1` covering both.

## Tally

Copy this per run.

```
run:        NN
date:
prompt:     /xp-meeting <verbatim>
SKILL.md:   <git log -1 --format=%h -- xp-meeting/SKILL.md>
log:        <path>

ONE-1       pass/fail/n-a   turn __  "..."
ONE-2       pass/fail/n-a   turn __  "..."
HANDS-1     pass/fail/n-a   turn __  "..."
CLOSED-1    pass/fail/n-a   turn __  "..."
SPLIT-1     pass/fail/n-a   turn __  "..."   parked
SMALLEST-1  pass/fail/n-a   turn __  "..."   parked

notes:      anything no check covers — this is where the next check comes from
one edit:   which check it targets, and what you expect to move next run
```
