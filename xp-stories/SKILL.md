---
name: xp-stories
description: Planning Game session that turns feedback, complaints or ideas into small story cards. Digs for the pain behind the request, and gates every card on the demo, scenario and delete tests. No design talk, no code.
disable-model-invocation: true
---

Help me slice my requests into the smallest stories that still deliver value on their own. Discuss it with me one question at a time, never more. Speak in business value, user behavior and estimates, never about the codebase. Use an Explore agent whenever a fact can be found on the repo.

A story is smallest when you cannot cut it in half and still have something I would use. Try to cut every card in half before proposing it, and check it against all three:

- Demo: I can watch it work end to end on a real system.
- Scenario: one user, one trigger, one outcome. If the outcome needs an "and", it is two cards.
- Delete: dropping it changes what I can do.

A fourth acceptance criterion means it is still too big.

Take one card at a time. Draft it with me until we agree on its acceptance criterias and its estimate, then write it to `docs/specs/[spec-number]-[story-slug].md` with an empty `## Technical Design` header.

Then put it on the table and ask me one thing: do the cards we have make sense to ship as they are, or do I want another story. Ask nothing else. Stop when I say they make sense, when you cannot estimate any better without building something first, or at five cards, whichever comes first. Five is a ceiling, not a target: most sessions end sooner, and one card is a normal session.
