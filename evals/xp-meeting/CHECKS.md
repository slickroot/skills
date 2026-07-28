# xp-meeting checks

Written down before a run, so a run isn't scored on how it felt. All of them are
answerable by someone reading the session log and nothing else.

| id | check | pass condition |
|---|---|---|
| `ONE-1` | every decision is mine, and I was asked | every *decision* in a story — what ships and what doesn't, what gets deleted, user-visible names, numbers and thresholds — was put to me as its own question, in its own turn, and answered by me. Facts from the repo are exempt, and so are internal mechanics the implementer is free to choose; naming those is `CLOSED-1`'s job, not a decision of mine. Also exempt: carrying a repair I approved to another place in the repo that states the same fact — a stale comment saying what a stale doc line said. The decision is *that the fact gets fixed*, and I made it; where else the fact is written down is a repo fact, not a second decision. Fails if one question carries two decisions; if a decision is announced as settled rather than asked — "I'd leave it alone", "X stays out of scope", "understood, so Y"; if a decision first appears in the story itself; or if one slips in beside a question about something else — in a recap, in an aside, or inside the suggestion |
| `HANDS-1` | nothing in a story needs my hands | any step I have to run myself — a migration, a console change, a key, a deploy — is its own issue labelled `task`, never a slice inside a story. The story that needs it declares it as a blocker |
| `CLOSED-1` | no design left to the implementer | the issue spells out the actual names — columns, functions, endpoints, files — not "store the user's answer". Every new file it creates is named, and every mechanism it describes — an env var, a flag, a column — is given its actual identifier. Two implementers reading it would produce the same shape and the same names |
| `SHOW-1` | stories shown before filing | the full text of every story appears in the conversation and I say go ahead before any `gh issue create` runs. Fails if a story is filed in the same turn it is first written |
| `TOUCH-1` | the meeting changes nothing but the issues | the only writes outside the conversation are the `gh issue create` calls for stories I approved, plus labels and dependency links on those issues using labels that already exist. Fails on creating a label, a file in the repo, a branch or a config change, and on editing an issue that wasn't part of this meeting. If something needed doesn't exist yet, that's a question, not a side effect |

`CLOSED-1`, `SHOW-1` and `TOUCH-1` are **fixed** as of run 11 — four straight passes each,
across four different features. Keep grading them; they cost nothing to read off a log and
they are how you'd notice a regression. They no longer drive the one edit. `ONE-1` and
`HANDS-1` are the live checks.

Verdicts are **pass / fail / n-a**. Nothing in between. If a verdict wants to be "sort
of", the check is badly worded — record that and reword it after the run, never during.

## History

`ONE-1` was one check through runs 01–05 and failed all five, in three different shapes:
two decisions on one question, a decision announced as settled, and a decision that simply
appears in the story with no turn behind it. One verdict couldn't say which shape moved, so
after run 05 the third shape was split out as `ONE-2`, reworded after run 06 to exempt the
implementer's mechanics — without that exemption it contradicted `CLOSED-1` outright, since
a mechanism specific enough to pass one failed the other.

**`ONE-1` and `ONE-2` are merged back into `ONE-1` as of run 08.** They are one idea —
decisions are mine and I was asked — and every run had them failing on the same evidence
anyway. Run 07 is the clearest case: Story 2 was never asked about *and* first appeared in
the story, which is one event costing two verdicts. The merged wording keeps all four
shapes and keeps the exemption. Read runs 01–05 as `ONE-1` covering both; read runs 06–07
as two verdicts on what is now one check.

`SHOW-1` and `TOUCH-1` were added after run 06 and graded against it retroactively, so run
06 is their run 00 — treat that first verdict as a baseline, not a result. `SHOW-1` comes
from a swing already on record: run 04 filed without showing, run 05 and run 06 both gated
on a go-ahead, same SKILL.md. `TOUCH-1` comes from run 06 creating a GitHub label nobody
asked for; that evidence was originally filed under `ONE-1`, which could only reach it by
stretching "decision that ends up in a story" to cover a write to the repo.

`TOUCH-1` was scoped to the repo before run 07 was graded, and it changed that run's
verdict from fail to pass. As first written it failed on creating "a file", which catches
the scratchpad heredoc that carries a long issue body into `gh issue create` — a write to
the session's tmp dir, not to anything shared. The check is about the meeting mutating
things that outlive it. Run 06's verdict is unaffected; it failed on a label either way.

**`SPLIT-1` and `SMALLEST-1` are deleted as of run 08.** Both were parked for three runs
and never drove an edit. `SPLIT-1` went 2/7 and every failure since run 05 was one
mechanical thing — the blocker was prose rather than a real dependency — which is now
`DEP-1`. `SMALLEST-1` went 3/7, was graded two different ways (slices inside a story in run
06, issue order in run 07), and once `HANDS-1` started passing it began failing because a
one-call `task` issue got filed second, which is not a defect. Their verdicts stay in the
runs that recorded them; nothing new is graded against them.

`DEP-1` is new for run 08 and has no baseline. It overlaps `HANDS-1`'s second clause on
purpose-built evidence — a `task` issue whose blocker is prose fails both. `HANDS-1` is
left whole rather than trimmed, so expect double-counting there until one of them moves.

**`DEP-1` is deleted as of run 11, untested.** Four runs, four `n-a`: runs 08 and 09 filed
one issue each, run 10 filed five that didn't block each other, run 11 filed three the same
way. It never once got a chance to fail, so it has no verdict to its name and never drove an
edit. That is not evidence blockers are handled — it is evidence these meetings don't
produce them. `HANDS-1`'s second clause still asks for the blocker to be declared; if a
meeting ever produces a real one and that clause catches prose, bring `DEP-1` back with this
wording. Its `n-a`s stay in the runs that recorded them.

**`ONE-1` gained the same-fact-repair exemption before run 11 was graded, and it changed
that run's verdict from fail to pass** — the same move, and the same disclosure, as
`TOUCH-1` before run 07. Run 11's only `ONE-1` evidence was story 1 carrying an approved
README repair into `run.ts`'s header comment, which says the same thing about the same
variables. Read runs 01–10 as graded without the exemption; none of their evidence turns on
it, so the streak is still readable end to end.

## Tally

Copy this per run.

```
run:        NN
date:
prompt:     /xp-meeting <verbatim>
SKILL.md:   <git log -1 --format=%h -- xp-meeting/SKILL.md>
log:        <path>

ONE-1       pass/fail/n-a   turn __  "..."
HANDS-1     pass/fail/n-a   turn __  "..."
CLOSED-1    pass/fail/n-a   turn __  "..."
SHOW-1      pass/fail/n-a   turn __  "..."
TOUCH-1     pass/fail/n-a   turn __  "..."

notes:      anything no check covers — this is where the next check comes from
one edit:   which check it targets, and what you expect to move next run
```
