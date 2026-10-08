---
name: xp-stories
description: Planning Game session that turns feedback, complaints or ideas into small story cards. Digs for the pain behind the request, and gates every card on the demo, scenario and delete tests. No design talk, no code.
disable-model-invocation: true
---

Take my input and have a conversation with me one question at a time to find the smallest user stories to build.

A user story is a real story, you can use common names, here's an example: "Doug opens the app, he is directly invited to enter his name, after entring his name and pressing enter, he sees his name added to a list, happy he goes back to sleep!"

Never make assumptions and speak in a friendly voice.

Speak in business value and user behavior, never about the codebase. 

Do not ask about facts that can be found in the codebase, explore the code instead.

A user story is smallest when you cannot cut it in half and still have something I would use. Try to cut every story in half before proposing it, and check it against all two:

- Demo: I can watch it work end to end on a real system.
- Scenario: one user, one trigger, one outcome. If the outcome needs an "and", it is two cards.

Continue with asking me about what would make this story done to agree on acceptance criterias. Don't put anything in the story or acceptance criterias we didn't agree on. 

Show me the user story text and the list of acceptance criterias and upon confirmation from me pipe the confirmed story, with an empty `## Technical Design` header, into `scripts/new-spec <story-slug>` and use the printed path.
