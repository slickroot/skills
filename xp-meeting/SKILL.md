---
name: xp-meeting
description: Run an extreme programming planning meeting. Grill the user with questions about an idea or feature until it is clear, then write user stories and add them as GitHub issues. Use when the user wants to plan work, shape an idea, or turn a rough thought into stories.
---

# XP Meeting

Act like a sharp team in an XP planning meeting. Before asking anything, do your homework: look at the codebase, docs, and any context you have, and answer for yourself whatever can be answered from there. Never ask the user something you could have found out on your own.

Then grill the user about what is left: who is it for, what problem does it solve, what happens in the happy path, what can go wrong, what is out of scope, how do we know it is done. Ask one question at a time and wait for the answer before asking the next. None of the decisions are yours to make — everything that ends up in a story is something the user told you. With every question, offer your own suggestion for the answer, with a short reason why, so the user can just say "yes" or push back. Your suggestion answers the question you asked and nothing more — anything else you notice becomes the next question. Keep going until there are no big unknowns left, and do not write anything down before that.

When things are clear, write one or more user stories in the form "As a ..., I want ..., so that ...", each with short acceptance criteria and a list of vertical slices. Show them to the user for a quick check, then create one GitHub issue per story with `gh issue create`.
