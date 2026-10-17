---
name: review-pr
description: Run the review station on the current branch. Calls the verifier, then the reviewer subagent, and writes a findings summary for the human. Use when a change is ready for review.
---

# Review PR

1. Run the **verifier** subagent. If its verdict is FAIL, stop and report what must be fixed. Don't review broken work.
2. Run the **reviewer** subagent against `REVIEW.md`.
3. Write `work/<feature>/review.md` with the verifier verdict, all findings by severity, and the reviewer's one-line summary for the human.
4. Open or update the pull request with that summary as the description, and link `intent.md`, `spec.md` and `plan.md`.
5. Stop. Tell the human the PR is ready for *their* review. Never approve or merge.
