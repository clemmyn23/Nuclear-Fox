---
name: repo-workflow
description: Use when working anywhere in the personal-development repo (including 4_career-review) — whenever a task changes files, finishes, or anything git-related comes up.
---

# personal-development repo workflow

## Git: Clement commits and pushes everything himself, manually

When a task changes files, finish by naming the changed files (and one line on what changed in each). Leave everything uncommitted in the working tree. That is the complete end-of-task procedure.

**Never:**
- run any state-changing git command (`add`, `commit`, `push`, `restore`, `checkout`, `stash`, branch operations)
- suggest or offer git operations in any form — no "commit this?" questions, no commit/PR buttons or actions in wrap-ups, no `git` command blocks for Clement to run

Read-only git (`status`, `diff`, `log`, `show`) is fine for understanding the repo.

If Clement explicitly asks for a git operation in the conversation, do exactly what he asked — the rule is against *unprompted* git activity, not against following his instructions.

## Adding to this skill

New repo conventions go in this file as their own `##` section.
