# evals/: regression tests for the agent's configuration

Tests check the code. Evals check the *setup that steers the agent*: `CLAUDE.md`, skills, subagents and hooks. When you change any of those, re-run the evals. If the pass rate drops, the change doesn't merge.

## How it works
- Each eval is one real task with an expected outcome (`case-template.md`).
- Start with **three cases from real past mistakes**. Grow toward 20–50.
- **Every production incident becomes a new eval.** That's how the factory learns.
- Run them by hand at first (start a fresh session, give the task, score against the pass criteria). Automate later with your agent's headless or SDK mode.

## Scoring
| Case | Last run | Result | Notes |
|---|---|---|---|
| 001-... | YYYY-MM-DD | pass / fail | |

Pass rate: __ / __
