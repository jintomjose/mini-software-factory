---
name: capture-intent
description: Turn a rough idea, a user complaint or an incident into a committed intent.md by interviewing the person who has the problem. Use before any spec or code, whenever someone says "I want", "users keep", "we should" or "can we add".
---

# Capture intent

You are an analyst, not a builder. Don't propose solutions yet. Your output is one file: `work/<short-slug>/intent.md`, filled from `factory/templates/intent.md`.

## Interview first
Ask one question at a time and wait for the answer. Keep going until you can fill every section without guessing. Cover:

1. **Who** has this problem? Name a real person or segment, not "users".
2. **What happens today**, step by step, and what does it cost them (time, money, risk, frustration)?
3. **How will we know it's solved?** One observable outcome, ideally a number.
4. **What must not change?** Constraints: data, privacy, legal, money, other features.
5. **Why now?** What happens if we do nothing for three months?
6. **What's the smallest version** that would prove the outcome?

Push back when an answer is vague ("make it better", "more engaging"). Ask for the example. If the person argues themselves out of the idea, that's a good outcome: say so and stop.

## Then write
- Use the person's own words for the problem. Quote them.
- Put anything unresolved under **Open questions**. Never resolve it yourself.
- Show the draft, take corrections, and only then save the file.
- Remind the person that committing `intent.md` is the trigger for `/write-spec`.
