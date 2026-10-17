# Review: account deletion

> **Illustrative example.** Modelled on the GDPR account-deletion feature in my habit tracker, simplified and generalised. Names, dates and findings are illustrative, not a verbatim record.

Verifier: **PASS** · Tests 4/4 · Build ok · Outside the plan: none

## Findings
- **MAJOR** `Account.jsx`: on error the dialog closes and the user sees nothing. Show the error and keep the dialog open (spec: error state). *Fixed in follow-up commit.*
- **MINOR** `delete_my_account.sql`: add a comment explaining the ownership-transfer order (oldest member first).
- **NIT** `Goodbye.jsx`: copy says "deleted forever"; spec says "permanently". Pick one.

## Policy check
- `[POLICY: privacy]` complete erasure: ✅ covered by test SC-001
- `[POLICY: security]` id from session only: ✅ no parameter accepted; test passes
- `[POLICY: privacy]` analytics manual step: ✅ in runbook

## For the human
Look at the ownership-transfer logic yourself (FR-004); it's the only part that touches other users' data.

Approved by: product owner · Merged: <date>
