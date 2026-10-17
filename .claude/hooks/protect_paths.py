#!/usr/bin/env python3
"""PreToolUse hook: block edits to protected paths.

Claude Code passes the tool call as JSON on stdin. Exit code 2 blocks the call and
shows stderr to the agent, so it knows why and can ask a human instead.
Skills advise; this enforces.
"""
import fnmatch
import json
import os
import sys

# Edit for your repo. Patterns are matched against the path relative to the project root.
PROTECTED = [
    ".github/workflows/*",        # CI is changed by a human, in its own PR
    "supabase/migrations/*",      # migrations that already ran are history
    "migrations/*",
    ".claude/hooks/*",            # the agent may not weaken its own guardrails
    ".claude/settings.json",
    ".env",
    ".env.*",
]

call = json.load(sys.stdin)
path = (call.get("tool_input") or {}).get("file_path", "")
root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
rel = os.path.relpath(path, root) if os.path.isabs(path) else path

for pattern in PROTECTED:
    if fnmatch.fnmatch(rel, pattern):
        print(f"Blocked: '{rel}' is a protected path ({pattern}). "
              "Ask the human to make this change, or explain in the plan why it is needed.",
              file=sys.stderr)
        sys.exit(2)
sys.exit(0)
