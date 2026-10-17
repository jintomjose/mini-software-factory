# Spec: account deletion

> **Illustrative example.** Modelled on the GDPR account-deletion feature in my habit tracker, simplified and generalised. Names, dates and findings are illustrative, not a verbatim record.

Intent: [intent.md](./intent.md) · Author: /write-spec + product owner · Date: <date> · Status: approved

## Summary
Signed-in users can permanently delete their account and all data they own from the account page. One server-side function does the deletion in a single transaction, so it either fully happens or doesn't happen at all.

## User stories
### P1: Delete my account
As a user who wants to leave, I want to delete my account and data myself, so that I don't have to ask anyone.
**Independent test:** create a user with habits, logs and a group; delete; confirm zero rows remain for that user and they can't sign in.

### P2: Know what will happen
As a user about to delete, I want to see exactly what gets deleted, so that I'm not surprised.

## Functional requirements
- **FR-001** A "Delete account" section on the account page, visually separated as a danger zone
- **FR-002** Deletion requires typing the word DELETE to confirm
- **FR-003** One database function, running with elevated rights but only for the calling user, deletes the user's logs, habits, group memberships, profile and auth record in one transaction `[POLICY: privacy] erasure must be complete (GDPR art. 17)`
- **FR-004** Groups the user created: deleted if they have no other members; otherwise ownership passes to the longest-standing member
- **FR-005** After deletion the user is signed out and sees a confirmation page
- **FR-006** The function can only ever delete the caller's own data `[POLICY: security] the user id comes from the session, never from a parameter`

## Success criteria
- **SC-001** Zero rows referencing the deleted user in any table after deletion
- **SC-002** Other users' shared groups keep working

## Design
- **Data:** new function `delete_my_account()`; no schema changes
- **Interface:** called from the account page through the existing API client
- **States:** confirm → deleting (button disabled) → done / error (nothing deleted, message shown)

## Out of scope
- Data export (separate intent)
- Erasing the analytics person profile: no browser-safe way to do it. Documented as a manual step for the owner `[POLICY: privacy] owner erases it within 30 days`

## Open decisions
| # | Decision | Options | Decided by | Answer |
|---|---|---|---|---|
| 1 | Groups with other members | delete / transfer | product owner | transfer (FR-004) |
| 2 | Analytics profile | automate / manual | product owner | manual, documented |
