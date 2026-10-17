#!/usr/bin/env python3
"""PreToolUse hook: refuse to write anything that looks like a secret or a private key."""
import json
import re
import sys

PATTERNS = {
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "AWS access key": r"AKIA[0-9A-Z]{16}",
    "GitHub token": r"gh[pousr]_[A-Za-z0-9]{36,}",
    "Stripe secret key": r"sk_(live|test)_[A-Za-z0-9]{16,}",
    "Anthropic API key": r"sk-ant-[A-Za-z0-9_\-]{20,}",
    "OpenAI API key": r"sk-[A-Za-z0-9]{32,}",
    "Supabase service role key": r"service_role[\"']?\s*[:=]\s*[\"']eyJ",
    "generic secret assignment": r"(?i)(secret|password|api_key|token)\s*[:=]\s*[\"'][^\"'\s]{16,}[\"']",
}

call = json.load(sys.stdin)
ti = call.get("tool_input") or {}
text = "\n".join(str(ti.get(k, "")) for k in ("content", "new_string"))
for edit in ti.get("edits", []) or []:
    text += "\n" + str(edit.get("new_string", ""))

for name, pattern in PATTERNS.items():
    if re.search(pattern, text):
        print(f"Blocked: this change contains what looks like a {name}. "
              "Secrets go in environment variables or the secret store, never in files.",
              file=sys.stderr)
        sys.exit(2)
sys.exit(0)
