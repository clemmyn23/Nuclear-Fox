#!/usr/bin/env python3
"""Second pass: clean up grammar issues from redaction substitutions.

Mostly capitalizing 'the X' / 'a X' that ended up at sentence starts."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    "00-executive-summary.md",
    "01-year1-onboarding.md",
    "02-year2-sms.md",
    "03-year3-commerce.md",
    "04-year4-journeys.md",
    "05-year5-platform.md",
    "06-year6-current.md",
    "07-growth-signals.md",
    "08-jira-projects.md",
    "09-notable-prs.md",
    "10-jscrew-review-activity.md",
    "11-repo-breakdown.md",
    "12-review-comment-patterns.md",
    "13-slack-architecture-discussions.md",
    "14-confluence-design-docs.md",
    "README.md",
    "cv/clement-ng-cv.md",
    "cv/experience-section.md",
    "data/jira-projects-summary.md",
]

# Sentence-start capitalisations.
# A sentence starts after: newline, period+space, question mark+space, exclamation+space, ">  " (blockquote+space), or "**" markdown emphasis or bullet "- ".
# We focus on the specific role tokens we introduced.
CAPITALIZATION_PATTERNS = [
    # After period/question/exclamation followed by space
    (r"([.!?])\s+the (DBA|platform engineer|junior engineer|senior engineer|squad product lead|project manager|architect|teammate|JS-crew teammate|CEO|Journeys tribe engineer)\b",
     lambda m: f"{m.group(1)} The {m.group(2)}"),
    (r"([.!?])\s+a (DBA|platform engineer|junior engineer|senior engineer|teammate|JS-crew teammate)\b",
     lambda m: f"{m.group(1)} A {m.group(2)}"),
    # Start of line (after newline)
    (r"(^|\n)the (DBA|platform engineer|junior engineer|senior engineer|squad product lead|project manager|architect|teammate|JS-crew teammate|CEO|Journeys tribe engineer)\b",
     lambda m: f"{m.group(1)}The {m.group(2)}"),
    (r"(^|\n)a (DBA|platform engineer|junior engineer|senior engineer|teammate|JS-crew teammate)\b",
     lambda m: f"{m.group(1)}A {m.group(2)}"),
    # Inside bullets and bold markers
    (r"(\n- \*\*[^*]*?\*\* — )the (DBA|platform engineer|junior engineer|senior engineer|squad product lead|project manager|architect|teammate|JS-crew teammate)",
     lambda m: f"{m.group(1)}The {m.group(2)}"),
    (r"(\n- \*\*[^*]*?\*\* — )a (DBA|platform engineer|junior engineer|senior engineer|teammate|JS-crew teammate)",
     lambda m: f"{m.group(1)}A {m.group(2)}"),
]

# Phrase grammar fixes
PHRASE_FIXES = [
    ("design call with junior engineer", "design call with a junior engineer"),
    ("with the junior engineer the junior engineer", "with the junior engineer"),
    ("with a junior engineer a junior engineer", "with a junior engineer"),
    ("DM with the DBA", "DM with a DBA"),
    ("DMs with a DBA", "DMs with DBAs"),
    # Avoid duplicate role prefixes when first-name substitution already produced 'the X' inline
    ("the the ", "the "),
    ("a a ", "a "),
]


def apply(text: str) -> str:
    for pat, repl in CAPITALIZATION_PATTERNS:
        text = re.sub(pat, repl, text)
    for old, new in PHRASE_FIXES:
        text = text.replace(old, new)
    return text


def main():
    changed = 0
    for rel in TARGETS:
        p = ROOT / rel
        if not p.exists():
            continue
        old = p.read_text()
        new = apply(old)
        if new != old:
            p.write_text(new)
            changed += 1
            print(f"cleaned: {rel}")
    print(f"\n{changed} files cleaned.")


if __name__ == "__main__":
    main()
