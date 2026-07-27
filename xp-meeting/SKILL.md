---
name: xp-meeting
description: Run an extreme programming planning meeting. Grill the user with questions about an idea or feature until it is clear, then write user stories and add them as GitHub issues. Use when the user wants to plan work, shape an idea, or turn a rough thought into stories.
---

# XP Meeting

Interview me about every aspect of this, ask me one question at a time and wait for the answer before asking the next. All decisions are mine, put them in front of me and wait for my answer. With every question, offer your own suggestion for the answer, with a short reason why. 

Your turn ends on the question. Whatever else you noticed waits its turn. Keep going until we reach an understanding about every aspect of the decision tree.

If a fact can be found in the repo code or documentation then you don't to ask me about it. Not decisions, decisions are mine don't assume - ask me.

When things are clear, write one or more user stories in the form "As a ..., I want ..., so that ...", each with short acceptance criteria and a list of vertical slices. Show them to me for a quick check, then create one GitHub issue per story with `gh issue create`.

If a slice is something I have to do outside the code, have it be on its own issue tagged `task`
