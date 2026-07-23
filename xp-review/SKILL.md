---
name: xp-review
description: Review a pull request the extreme programming way. Explain what was done, walk through how to review it, and discuss the design and coding patterns in it. Use when the user asks to review a PR or wants to understand one.
---

# XP Review

Take a pull request as input and read it with `gh pr view` and `gh pr diff`. First explain in plain words what the change does and why, so the user gets the full picture without reading the diff themselves.

Then walk through the review like a pair partner: point out what is good, what looks risky, and what is missing tests. Discuss the design patterns and coding patterns used, whether they fit, and simpler options if there are any. The user is the reviewer here, so be ready to answer their questions about any part of the change and dig into the code to back up your answers. Give a clear closing take: looks good to merge or needs changes.
