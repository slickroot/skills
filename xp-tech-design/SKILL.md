---
name: xp-tech-design
description: Technical architecture meeting to turn user stories into a strict implementation specification for coding agents. Forces explicit decisions on data models, API states, and test criteria. No vague implementation allowed.
disable-model-invocation: true
---

The goal of this session is to take a user story and using the TDD framework we can decide the architecture or it can be a refactoring spec if there's no user story.

TDD here is a way that every question you ask should force a design decision.

Brainstorm Software Architecture: Identify the core classes or functions or components needed to solve a specific problem.
Assign Responsibilities: Define what each class knows (its state) and what it does (its behavior).
Map Dependencies (Collaborators): Determine which other classes a component needs to interact with to get the job done.

The meeting must be a strict back-and-forth technical discussion. Ask only ONE question at a time.

When everything is clear you should update the spec document with our decision under the empty `## Technical Design` header. Or create a new refactoring spec if there's no user story.
