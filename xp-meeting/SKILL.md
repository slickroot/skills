---
name: xp-meeting
description: Run an extreme programming planning meeting. Grill the user with questions about an idea or feature until it is clear, then write user stories and add them as GitHub issues. Use when the user wants to plan work, shape an idea, or turn a rough thought into stories.
---

# XP Meeting

Act like a sharp team in an XP planning meeting. Take whatever input the user gives you and ask a lot of questions about it: who is it for, what problem does it solve, what happens in the happy path, what can go wrong, what is out of scope, how do we know it is done. Keep asking until there are no big unknowns left. Do not write anything down until the user has answered enough questions.

When things are clear, write one or more user stories in the form "As a ..., I want ..., so that ...", each with short acceptance criteria. Show them to the user for a quick check, then create one GitHub issue per story with `gh issue create`.
