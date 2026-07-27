# xp-meeting checks

Written down before a run, so a run isn't scored on how it felt. All of them are
answerable by someone reading the session log and nothing else.

| id | check | pass condition |
|---|---|---|
| `ONE-1` | one decision, one question, asked | every decision that ends up in a story was put to me as its own question, in its own turn, and answered by me. Fails if one question carries two decisions, or if a decision is announced as settled rather than asked — "I'd leave it alone", "X stays out of scope", "understood, so Y" |
| `ONE-2` | nothing in a story I was never asked about | every *decision* in the story — what ships and what doesn't, what gets deleted, user-visible names, numbers and thresholds — traces back to an answer I gave, or to a fact from the repo. Internal mechanics the implementer is free to choose are exempt; naming those is `CLOSED-1`'s job, not a decision of mine. Fails on any decision that first appears in the story itself, and on any that slipped in beside a question about something else — in a recap, in an aside, or inside the suggestion |
| `HANDS-1` | nothing in a story needs my hands | any step I have to run myself — a migration, a console change, a key, a deploy — is its own issue labelled `task`, never a slice inside a story. The story that needs it declares it as a blocker |
| `CLOSED-1` | no design left to the implementer | the issue spells out the actual names — columns, functions, endpoints, files — not "store the user's answer". Every new file it creates is named, and every mechanism it describes — an env var, a flag, a column — is given its actual identifier. Two implementers reading it would produce the same shape and the same names |
| `SHOW-1` | stories shown before filing | the full text of every story appears in the conversation and I say go ahead before any `gh issue create` runs. Fails if a story is filed in the same turn it is first written |
| `TOUCH-1` | the meeting changes nothing but the issues | the only writes outside the conversation are the `gh issue create` calls for stories I approved, plus labels and dependency links on those issues using labels that already exist. Fails on creating a label, a file, a branch or a config change, and on editing an issue that wasn't part of this meeting. If something needed doesn't exist yet, that's a question, not a side effect |
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

`ONE-2` was reworded after run 06, which is a break from "written down before a run" —
recorded here so nobody reads run 06's verdict as comparable to 01–05's. As first written
it required every name and number to trace back to an answer, which `CLOSED-1` forbids: a
mechanism specific enough to pass `CLOSED-1` fails `ONE-2`, and vice versa. The exemption
for implementer's mechanics is the fix. Runs 01–05 were graded under the old wording.

`SHOW-1` and `TOUCH-1` were added after run 06 and graded against it retroactively, so run
06 is their run 00 — treat the first verdict as a baseline, not a result. `SHOW-1` comes
from a swing already on record: run 04 filed without showing, run 05 and run 06 both gated
on a go-ahead, same SKILL.md. `TOUCH-1` comes from run 06 creating a GitHub label nobody
asked for; that evidence was originally filed under `ONE-1`, which could only reach it by
stretching "decision that ends up in a story" to cover a write to the repo.

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
SHOW-1      pass/fail/n-a   turn __  "..."
TOUCH-1     pass/fail/n-a   turn __  "..."
SPLIT-1     pass/fail/n-a   turn __  "..."   parked
SMALLEST-1  pass/fail/n-a   turn __  "..."   parked

notes:      anything no check covers — this is where the next check comes from
one edit:   which check it targets, and what you expect to move next run
```
