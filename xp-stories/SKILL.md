---
name: xp-stories
description: Turn feedback, complaints or ideas into a ranked stack of small story cards. Finds the pain behind the request, splits by user activity, and gates every card on demo/scenario/delete tests. No design talk, no specs, no code. Only ever runs when I type /xp-stories myself.
disable-model-invocation: true
---

# XP-stories

Turn my input (feedback, complaints, ideas) into a ranked stack of small story cards. No design talk, no specs, no code discussion.

## Output

Ranked story cards. Each card has exactly:

- **Title**
- **Story** — As a ___, I want ___, so that ___
- **Size** — small / medium / needs-a-spike
- **Open questions** — one-liners only, unanswered

## Process

1. **Find the pain.** Never accept my solution as a requirement. Ask me: what happened? Show a real example. What did I wish happened instead? For visual complaints: I point at the exact element and provide a reference screenshot. Check if my "don't like it" means "can't find it" — that's a behavior story.
2. **Split into stories** by user activity, never by technical layer.
3. **Gate every card** (PASS/FAIL, all three required):
   - Demo test: "What do I see or click in the demo?" No visible answer = FAIL.
   - Scenario count: more than 3–5 given/when/then = FAIL.
   - Delete test: shipped alone and nothing after, still useful? No = FAIL.
   - Failed cards get split and re-gated.
4. **First card in any new area** = thinnest end-to-end path. Hardcode freely; later cards replace it.
5. **Still big?** Ask me: "Which 20% of this would you demo Friday?"
6. **Unsizeable?** Write a spike card instead: one decidable question + timebox. Route to XP-spike.
7. **I rank the stack.** Top card goes to XP-spec. All others stay one-liners — add no detail below the top.

## Rules

- Zero "how" questions answered. Design talk → park as open question, move on.
- Every fact on a card came from me. Guesses → open questions.
- Cards bounced back from XP-spec as too big: split, re-rank, continue.
