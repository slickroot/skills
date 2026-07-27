---
name: xp-implement
description: Implement a user story from a GitHub issue the extreme programming way. Split it into thin slices, build each slice with TDD, and open a pull request at the end. Always works in a git worktree. Use when the user asks to implement an issue or a story.
---

# XP Implement

Take a GitHub issue as input and read it with `gh issue view`. Always start by making a fresh git worktree with its own branch and do all the work there, never on the user's current checkout. Split the story into thin vertical slices, where each slice is a small piece that works end to end on its own.

Build each slice with TDD: write a failing test first, write just enough code to make it pass, then clean up. Commit after each green slice. When all slices are done and the tests pass, push the branch and open a pull request with `gh pr create` that links back to the issue.

Keep your own context clean by delegating: use one exploring agent when you need to read through the code, and one coding agent that does all the slices in the worktree. Bring back only conclusions and results, so the main conversation holds the plan and decisions rather than file contents.

Make sure you follow the project CONTRIBUTING.md guidance.
