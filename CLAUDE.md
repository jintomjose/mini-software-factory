# CLAUDE.md

Read this at the start of every session. Keep it short, true and current: when the agent makes the same mistake twice, the fix goes in **Known mistakes**.

## What this product is
<!-- One paragraph: who uses it, what problem it solves, what "working" means. -->

## Commands
```bash
npm install          # install
npm run dev          # local dev server
npm test             # unit tests (must pass before any PR)
npm run build        # production build (must pass before any PR)
```

## Architecture
<!-- Stack, where things live, the one or two seams that matter. Example:
- Frontend: Vite + React. All data access goes through src/api/client.js. Never call the database from a component.
- Backend: Postgres with row-level security. Ownership is by user id.
- Hosting: push to main deploys production. Every PR gets a preview URL. -->

## How work flows here (the factory)
1. No code without an approved `plan.md` in `work/<feature>/`. If there's no plan, use plan mode and write one.
2. `intent.md` → `spec.md` → `plan.md` live together in `work/<feature>/`. Read all three before building.
3. Anything marked `[NEEDS CLARIFICATION]` or `[POLICY]` in the spec is a stop sign. Ask, don't guess.
4. When done, run the verifier subagent, then `/review-pr`. Never approve or merge your own PR.

## Conventions
- Small PRs: one plan, one PR.
- Tests first for bug fixes: write the failing test, confirm it fails for the right reason, then fix the code (never the test).
- No new dependencies without saying why in the plan.

## Never
- Commit secrets, `.env*` files, or real user data (emails, names) in seed files or fixtures.
- Edit protected paths (see `.claude/hooks/protect_paths.py`): migrations that already ran, CI config, this file's **Never** section.
- Touch production data or settings directly. Production changes go through a PR.

## Known mistakes
<!-- The most valuable section. Add one line every time the agent gets something wrong twice. Example:
- The account page reads `email`, `full_name` and `created_date` from the user object. Dropping any one of them crashes the page.
- Auth redirect URLs must be listed in the auth provider for every origin, or sign-in lands on the wrong host. -->
