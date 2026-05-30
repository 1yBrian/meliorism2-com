#!/usr/bin/env python3
"""no_anthropic_in_cron.py — CI guard: no paid API in automation.

Brian's iron rule: cron paths must never call Anthropic (or any paid API).
This script greps for forbidden imports/strings in files that run unattended.

Pass = no violations. Fail = file path printed.

Usage:
    python3 _engine/scripts/no_anthropic_in_cron.py
"""
import re, sys, pathlib

# Files/dirs that run via cron, pre-flight, or release pipeline
GUARDED_PATHS = [
    ".github/workflows",
    ".github/scripts",
    "_engine/scripts",
]

# Files that are EXPLICITLY allowed to mention Anthropic identifiers (chat-invoked, or this guard itself)
EXCEPTIONS = {
    "_engine/truth_agent.py",                  # chat-invoked only — never on cron path
    "_engine/scripts/no_anthropic_in_cron.py", # this guard file references the strings to scan for
}

FORBIDDEN_PATTERNS = [
    r'\bimport\s+anthropic\b',
    r'from\s+anthropic\s+import',
    r'ANTHROPIC_API_KEY',
    r'api\.anthropic\.com',
    r'\bclaude-3\b',
    r'\bclaude-opus\b',
    r'\bclaude-sonnet\b',
    r'\bclaude-haiku\b',
]

def main():
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    violations = []
    for guarded in GUARDED_PATHS:
        base = repo_root / guarded
        if not base.exists(): continue
        for p in base.rglob("*"):
            if not p.is_file(): continue
            rel = p.relative_to(repo_root).as_posix()
            if rel in EXCEPTIONS: continue
            if p.suffix not in (".py", ".yml", ".yaml", ".sh", ".js"): continue
            try:
                content = p.read_text(errors="ignore")
            except Exception:
                continue
            for pat in FORBIDDEN_PATTERNS:
                if re.search(pat, content, re.IGNORECASE):
                    violations.append(f"  {rel}: matches {pat!r}")
                    break
    if violations:
        print(f"FAIL: paid-API references found in cron-invoked paths:")
        for v in violations: print(v)
        print("\nFix: move the Anthropic call into a Brian-invoked chat skill, not automation.")
        sys.exit(1)
    print("PASS: no paid-API references in cron paths.")
    sys.exit(0)

if __name__ == "__main__":
    main()
