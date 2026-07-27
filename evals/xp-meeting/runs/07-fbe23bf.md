```
run:        07
date:       2026-07-27
prompt:     /xp-meeting So now we can have a coaching screen.
SKILL.md:   fbe23bf
log:        ~/.claude/projects/-Users-slickroot-work-elaich-thelongcompound/f3df064f-bf04-4566-9fb7-fc769a02a8ac.jsonl
```

Two issues filed: #133 "The coach says one thing" (no label) and #134 "Confirm the deployed
/v1/coach answers for the app's token" (`task`).

Same `fbe23bf` as run 06 — run 06's one edit was never made, so this is the same skill
against a different prompt. `SHOW-1` and `TOUCH-1` get their first real verdict here; run
06 was their baseline.

| id | verdict | evidence |
|---|---|---|
| `ONE-1` | **fail** | Two shapes. Q8 at t78 carries two decisions — the silent-failure policy and the number: "10 seconds is my pick for the timeout … Take (a) with a 10s timeout, or something else?" One answer at t79, "a) sounds good", buys both. And Story 2 is never asked: nothing in t51–t94 puts a deployment check to Marouane, it first exists at t96 as a story. The eleven questions themselves are otherwise the cleanest of any run — own turn, own answer, suggestion with a reason, nothing announced as settled |
| `ONE-2` | **fail** | Story 2 in full. Plus two scope calls inside #133's notes that no turn stands behind: "No cap on log length — a year-old habit sends roughly 365 lines. **Out of scope**", and the old `behavior-memory` rule set "deliberately not carried over". Both are what-ships decisions, both first appear in the filed body. "The log sent is `buildHabitLog` for that habit alone" (t96) is a third, weaker one — scoping the coach's input to one habit was never asked |
| `HANDS-1` | **fail** | First clause passes, and well: t96 "## Story 2 — `task`", filed as #134 with `--label task`, no hands-on step anywhere in Story 1's six slices. Second clause fails — #133 declares no blocker, and `gh api repos/…/issues/133` returns `blocked_by: null`. #134's body mentions #133 as context ("#133 swallows both silently by design"), which is the opposite direction and not a declaration |
| `CLOSED-1` | **fail** | Closest yet, and it misses on the screen the meeting was about. Slice 6 of #133: "The thinking beat and the diagnosis screen, wired through `today.selectors.ts` and `today.controller.ts`" — two new components, neither named, where slices 1–5 all name their file (`coach-trigger.ts`, `core/ports/coach.ts`, `infrastructure/coach/server-coach.ts`, `RequestCoachDiagnosisUseCase`). And the mechanism that carries the whole beat has no identifier: "a new `TodayScreenState` tag alongside `frictionAsk`" |
| `SHOW-1` | **fail** | The gate itself held — full stories at t96, "Say go and I'll open both", "yes" at t97, first `gh issue create` at t98. It fails on "the full text of every story appears in the conversation": what got filed is longer than what was shown. #133 carries a paragraph on reviving #107/#108, a worked slump example, and a four-paragraph Notes section, none of it in t96. The slices gained file paths too. t102 says so out loud: "the notes carried over from #107/#108 (the `now` asymmetry at the seam, dropping the old `behavior-memory` rule set, the uncapped log length, and why there's no lab)" |
| `TOUCH-1` | **pass** | The only repo writes are the two `gh issue create` calls. No label created — `task` already existed, visible on #131 at t34. No file, branch or config change; the heredocs at t98/t100 write to the session's tmp scratchpad, which is how a long body reaches `gh`. t102 declines to touch old issues unasked: "if you'd rather have the originals reopened and closed as duplicates instead, that's a one-liner". Graded against the check as reworded — see below |
| `SPLIT-1` | **fail** *(parked)* | Third run running on the same shape. #134 is not a use case a tester exercises on a fresh checkout, and #133 cannot be seen working until it passes, and no dependency relationship exists between them |
| `SMALLEST-1` | **fail** *(parked)* | Both filed and ordered, and the first is the big one: #133 is six slices spanning a pure function, a port, an adapter, a use case and two screens. #134 is a single call and was filed second |

Six fails and one pass, which reads worse than the run was. Every question Marouane
actually saw was well-formed, and every failure is downstream of the go-ahead. That is the
finding.

**`SHOW-1` earns its place on its first real outing.** It was added because run 04 filed
without showing and runs 05–06 didn't; it caught something else entirely. The gate is not
the weak point — the gap between "yes" and the issue existing is. Nothing in the skill says
the body has to be the text that was approved, so the agent kept writing after the approval
and everything it wrote was good. That is what makes it hard to see and worth a rule.

**`ONE-2` and `SHOW-1` fail on the same evidence, which is the run in one line.** The story
grew after the go-ahead, and what it grew was decisions. Two checks written for different
reasons both land on it.

**Story 2 is a new `ONE-1` shape and the skill's own `task` rule opened the lane.** Run 06's
task issue traced back to t44, where Marouane asked for a device check. This one has no
turn at all — the agent found the need, decided it was in scope, and wrote its acceptance
criteria alone. "If a slice is something I have to do outside the code, have it be on its
own issue" tells the agent what to do with hands-on work; it never says the existence of
hands-on work is Marouane's call. Decisions can leave through the `task` door.

## Notes

- **The homework is now consistently the best part.** Nineteen tool calls before Q1, and
  t51 opens with ground truth rather than a guess: "the friction ask ships (#106/118),
  `Suggestion` persists through the port (#124), `buildHabitLog` renders the history, and
  `POST /v1/coach` is live and exercised by `npm run e2e:coach` (#120) — but the app has
  **no coach client at all**". Real identifiers pulled from real files at t14, t27, t85,
  t93. Fourth run running, and the reason `CLOSED-1` got as close as it did.

- **Q11 is the shape to keep.** t93 noticed that the user's own `value: ''` answer would
  render back into the coach's input as `suggestion: shrink ""`, and asked instead of
  picking: "which is what gets POSTed back on the next call". A consequence of an earlier
  answer, surfaced as its own question. That is the skill working.

- **A scope collapse handled without argument.** t64 — "We don't care about accepting or
  declining at this point" — killed a third of the plan mid-meeting. t66 takes it, names
  what died ("No `update-habit`, no anchor menus, no `answerSuggestion` call"), and
  immediately reopens the one thing it left dangling as Q4. No relitigating.

- **The `10s` in Q8 is the second time a number rode in on another question's answer.**
  Run 06 had no instance; earlier runs did. Worth watching whether numbers specifically
  are where bundling happens — a policy question with a threshold in it seems to attract
  this.

- **#133 was filed with no label.** Run 06 labelled both issues; this run labelled only the
  `task` one. No check covers labels on story issues and it may not deserve one, but the
  inconsistency across two runs of the same SKILL.md is worth a note.

- **The meeting doesn't close on Marouane's word.** t102 ends with a fresh open question
  after both issues are filed: "if you'd rather have the originals reopened and closed as
  duplicates instead, that's a one-liner". Harmless here. Same family as the `SHOW-1`
  failure — the agent still has things to say after the meeting is over.

- **`TOUCH-1` was reworded before grading, and it changed the verdict.** As written it
  failed on "creating … a file", which the scratchpad heredocs do. Scoping it to the repo
  is recorded in `CHECKS.md` as a wording repair; the blind grader flagged the same thing
  and split the same way.

## The one edit

**File exactly what was approved.** The issue body is the text Marouane saw, word for word.
Anything the agent still wants to add goes in front of him before the go-ahead, not into
the body afterwards.

It targets `SHOW-1`, and it should move `ONE-2` too, since both fail on the same drift.
Expect run 08 to either file what it showed, or to show a longer story in the first place —
either is a pass, and the second is the better outcome.

**Two edits land together this time, which costs attribution.** Run 06's `TOUCH-1` sentence
— the meeting creates the issues and nothing else — was never written, so it goes in
alongside. `TOUCH-1` passed run 07 unaided, so the sentence is now insurance rather than a
fix, and if `TOUCH-1` passes run 08 that tells us little. The `SHOW-1` edit is the one to
read the next run on.

Not edited, and the candidate for run 08: nothing tells the agent that *whether* there is
work outside the code is a decision rather than an observation. Story 2 walked through that
gap. Left alone deliberately — one edit at a time, and `SHOW-1` is the louder one.
