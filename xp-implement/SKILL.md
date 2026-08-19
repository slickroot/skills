---
name: xp-implement
description: Implement a user story from a GitHub issue the extreme programming way. Split it into thin slices, build each slice with TDD, and open a pull request at the end. Always works in a git worktree. Use when the user asks to implement an issue or a story.
---

# XP Implement

Take a spec file as input and read it. Always start by making a fresh git worktree with its own branch and do all the work there, never on the user's current checkout. 

Make sure you follow the project CONTRIBUTING.md guidance.

The spec is the contract. Build exactly what it describes — no extra error handling, fallback states, validation, abstractions, or UX decisions that aren't in it, even if they'd be "good practice." If you hit something the spec doesn't cover, don't invent a resolution: leave it alone and note it, verbatim, in a "Gaps found" section of the PR description for the reviewer to triage. Never silently decide on the spec's behalf.

Build each slice with TDD when it makes sense: write a failing test first, write just enough code to make it pass, then clean up. Commit after each green slice. When all slices are done and the tests pass, push the branch and open a pull request with `gh pr create` that links back to the issue. Add a QA section for the reviewer to run manual tests.

Keep your own context clean by delegating: use one exploring agent when you need to read through the code. For implementation, spawn exactly one coding agent per slice, one after another — never reuse the same coding agent across more than one slice, even if it still has room left. As soon as a slice is committed, that agent's job is done; start a brand new one for the next slice. Bring back only conclusions and results, so the main conversation holds the plan and decisions rather than file contents.

After I say that I'm happy with the PR, you should merge it and make sure it closes the github issue. Should then pull last main and clean the worktree used. Then move the spec file to the archive, commit to `main` and push to origin.
