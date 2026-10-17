# Intent: let users delete their own account

Author: product owner · Captured by: /capture-intent · Date: <date>
Status: committed

> **Illustrative example.** Modelled on the GDPR account-deletion feature in my habit tracker, simplified and generalised. Names, dates and findings are illustrative, not a verbatim record.

## Problem
"Users have no way to delete their own account. Today they have to ask me, and I do it by hand in the database." (product owner)

## Who has it
Every user who wants to leave. Today there's no way to do it without emailing me.

## What it costs today
Each request is a manual job for me in the database, and the GDPR right to erasure is only met by hand.

## Proposed outcome
A signed-in user can delete their account and all their data themselves, in under a minute, without contacting anyone.

## How we'll know
Manual deletion requests: from "every one" to zero. A deleted user's rows: zero left in any table.

## Constraints
- Must delete *everything* that user owns, and nothing anyone else owns
- Shared groups they created must not break for other members
- No new personal data collected to do it
- Must not be triggerable by accident

## Smallest version that proves it
A "Delete my account" button on the account page, a confirmation step, and one server-side function that deletes the user's data.

## Open questions
- What happens to groups the user created that still have other members? → resolved in spec (FR-004)
- Analytics provider holds a person profile too: can we erase that from the app? → resolved in spec: no, manual step
