---
name: xp-meeting
description: Run an extreme programming planning meeting. Grill the user with questions about an idea or feature until it is clear, then write user stories and add them as GitHub issues. Use when the user wants to plan work, shape an idea, or turn a rough thought into stories.
---

# XP Meeting

Interview me about every aspect of this, ask me one question at a time and wait for the answer before asking the next. All decisions are mine, put them in front of me and wait for my answer. With every question, offer your own suggestion for the answer, with a short reason why. 

One question, one decision. If your suggestion settles something the question doesn't ask about, that something is the next question — put it in its own turn and wait.

Suggest the shape, ask the details. When a suggestion has to describe something to be answerable — a case, a screen, a story slice — the description is not part of the answer. Name it, and put each thing inside it that isn't the question up for its own turn.

Your turn ends on the question. Whatever else you noticed waits its turn. Keep going until we reach an understanding about every aspect of the decision tree.

If a fact can be found in the repo code or documentation then you don't to ask me about it. Not decisions, decisions are mine don't assume - ask me.

When things are clear, write one or more user stories in the form "As a ..., I want ..., so that ...", each with short acceptance criteria and a list of vertical slices. Show them to me for a quick check, then create one GitHub issue per story with `gh issue create`. File exactly what I approved — the issue body is the text I saw, word for word. Anything else you want to say goes in front of me before the go-ahead, never into the body after it.

Create the issues and nothing else. If something you need doesn't exist yet — a label, a file, a branch — that's a question, not a side effect.

If a slice is something I have to do outside the code, have it be on its own issue tagged `task`
