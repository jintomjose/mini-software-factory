---
name: write-spec
description: Turn a committed intent.md into spec.md (requirements and design in one artifact), with policy concerns and open decisions flagged inline. Use after capture-intent and before plan mode.
---

# Write spec

Input: `work/<feature>/intent.md`. Output: `work/<feature>/spec.md` from `factory/templates/spec.md`.

1. Read `intent.md`, `CLAUDE.md` and the parts of the codebase the change will touch. A spec written without reading the code misses constraints; that is the most common failure.
2. Write user stories in priority order (P1, P2, P3). Each P1 story must be independently shippable and testable.
3. Give every functional requirement a stable ID (`FR-001`) and every success criterion one too (`SC-001`). Reviews and tests refer to these.
4. Flag inline, never silently resolve:
   - `[NEEDS CLARIFICATION: ...]` for any decision the intent doesn't settle
   - `[POLICY: privacy | security | legal | money | brand]` wherever a rule applies, with the rule
5. Write the design section only as deep as the plan needs: data changes, interfaces, states, error cases.
6. List what is explicitly **out of scope**.
7. Show the spec, resolve every `[NEEDS CLARIFICATION]` with the human, then save. Committing `spec.md` is the trigger for plan mode.
