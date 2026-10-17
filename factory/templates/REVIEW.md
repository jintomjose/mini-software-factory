# REVIEW.md: the review standard

The reviewer subagent applies this to every PR before a human looks. Keep it to what you'd actually block a merge for.

## BLOCKER: must fix
- Secrets, keys or tokens anywhere in the diff
- Real user data (emails, names) in code, seeds, fixtures or logs
- Authorisation gaps: can a user read or change someone else's data?
- Data loss: destructive migrations or deletes without a confirmation step or backup
- Behaviour that contradicts the spec, or an FR with no test
- Tests deleted, skipped or weakened to make the suite pass

## MAJOR: fix before merge
- Errors swallowed silently; no user-facing state for failures
- New dependency not justified in the plan
- Files changed outside the plan without explanation
- Privacy: new personal data collected without a stated purpose

## MINOR: can follow up
- Naming, duplication, missing comments on non-obvious code
- Performance concerns without a measured problem

## Always check
- [ ] The chain exists: `intent.md`, `spec.md`, approved `plan.md`
- [ ] Every `[POLICY]` item in the spec is honoured
- [ ] Verifier verdict is PASS
- [ ] A human, not the author, approves
