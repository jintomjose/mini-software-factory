# Plan: account deletion

> **Illustrative example.** Modelled on the GDPR account-deletion feature in my habit tracker, simplified and generalised. Names, dates and findings are illustrative, not a verbatim record.

Spec: [spec.md](./spec.md) · Written by: agent in plan mode · Approved by: product owner on <date>
Status: **approved**

## Approach
All deletion logic lives in one database function so it's atomic and can't be bypassed from the browser. The UI only calls it. The user id is read from the session inside the function (FR-006), so no parameter can point it at someone else.

## Files
| File | Change | Covers |
|---|---|---|
| `db/functions/delete_my_account.sql` | new | FR-003, FR-004, FR-006 |
| `src/api/client.js` | add `deleteMyAccount()` | FR-003 |
| `src/pages/Account.jsx` | danger-zone section + confirm dialog | FR-001, FR-002 |
| `src/pages/Goodbye.jsx` | new confirmation page | FR-005 |
| `tests/delete_my_account.test.sql` | new | SC-001, SC-002, FR-006 |
| `docs/privacy-runbook.md` | add manual analytics erasure step | out-of-scope policy note |

## Order of work
1. Failing tests: a user's rows remain after calling the function (SC-001); another user's group survives (SC-002); passing someone else's id does nothing (FR-006)
2. Write the function until the tests pass
3. API client method
4. Account page UI and Goodbye page
5. Runbook note

## Tests
| Test | Proves | Type |
|---|---|---|
| deletes all own rows | SC-001 | database |
| shared group survives, ownership transferred | SC-002, FR-004 | database |
| cannot target another user | FR-006 | database |
| confirm button disabled until DELETE typed | FR-002 | component |

## Risks and rollback
- Irreversible by design. Mitigation: confirmation step, transaction, tested on a copy of production data first
- Rollback = remove the UI section; the function is harmless without a caller

## Not touching
- Sign-in flow, analytics setup, any other user's data paths
