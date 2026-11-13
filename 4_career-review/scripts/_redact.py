#!/usr/bin/env python3
"""Apply name, handle, and customer redactions across narrative + CV files."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ----- File scope -----
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

# ----- Role mapping for handles -----
# Junior: people the narrative explicitly describes as junior or being coached.
# Senior: people the narrative explicitly tags as senior IC / architect / hiring screener.
# Everyone else defaults to "engineer".
JUNIOR_HANDLES = {"chris-luong", "fan-li", "sherry-lotfi"}
SENIOR_HANDLES = {"alex-zissis", "azissis", "james-dunlop"}

ALL_HANDLES = [
    "alex-zissis", "alexis-tzanos", "amy-diaz", "anthony-alexis", "azissis",
    "brian-luc", "challowes", "chris-luong", "chrisw", "clewis",
    "daniel-keith", "darkmode-list-and-subscribers", "david-connell",
    "david-vanlaarveth", "dmitry-antonov", "eddie-zeng", "fan-li",
    "francois-naude", "genevieve-bruno", "georgiel", "hbrink", "henry-bai",
    "henrys", "ishworg", "james-dunlop", "jamesr", "jari-talka", "jbustamante",
    "jeromec", "jflood", "jianjun-chen", "jowers", "kai-wang", "lcallaway",
    "leoc", "markg", "masoudc", "mattheww", "michael-yin", "nazif-ahmed",
    "niaw", "oliver-toon", "rashmita-pinto", "rowena-kite", "russella",
    "sam-henry", "samanthac", "sha", "sherry-lotfi", "steven-li",
    "subrat-shrestha", "tai-woodley", "timl", "ttruong", "yzein", "zhartmann",
]

def role_for(handle: str) -> str:
    if handle in JUNIOR_HANDLES:
        return "junior engineer"
    if handle in SENIOR_HANDLES:
        return "senior engineer"
    return "engineer"

# ----- Full-name replacements (apply BEFORE handle replacements) -----
# Order matters: longer/more specific first.
FULL_NAME_REPLACEMENTS = [
    # Two-word names
    ("Christopher Luong", "a junior engineer"),
    ("Christopher Wright", "a JS-crew teammate"),
    ("Sha Kong-Brooks", "a teammate"),
    ("David van Laar Veth", "a teammate"),
    ("David vanLaarVeth", "a teammate"),
    ("David Connell", "a teammate"),
    ("Lance Smith", "an architect"),
    ("Mark Green", "a platform engineer"),
    ("Mick Proust", "a DBA"),
    ("Hien Dang", "a DBA"),
    ("Tom Evans", "a teammate"),
    ("Greg Smith", "a teammate"),
    ("Sam Crome", "the squad product lead"),
    ("Liam Callaway", "a JS-crew teammate"),
    ("Alex Zissis", "a senior engineer"),
    ("Sharareh Lotfi", "a junior engineer"),
    ("Shenny Mackie", "the project manager"),
    ("Adel Helal", "a teammate"),
    ("Farnaz Sassani", "a Journeys tribe engineer"),
    ("James Dunlop", "a senior engineer"),
    ("Zac Hartmann", "a teammate"),
    ("Fan Li", "a junior engineer"),
    # First-name-only references (after the full-name forms have been replaced, the
    # remaining bare first names must also map to roles). These run AFTER the
    # full-name substitutions above so we don't double-replace.
    # Note: "Sam" alone is ambiguous in some places — handle carefully via context replacements.
]

# First-name-only references — these are applied after full-name replacement.
# Each tuple is (regex_pattern, replacement). Use word boundaries.
FIRST_NAME_REPLACEMENTS = [
    (r"\bMick\b(?!\sProust)", "the DBA"),
    (r"\bHien\b(?!\sDang)", "the DBA"),
    (r"\bHeini\b", "a teammate"),
    (r"\bShenny\b(?!\sMackie)", "the project manager"),
    (r"\bChristopher\b(?!\s(?:Luong|Wright))", "the junior engineer"),
    (r"\bFan\b(?=\s(?:and|wrote|asked|replied|posted|noticed))", "the junior engineer"),
    (r"\bLiam\b(?!\sCallaway)", "the JS-crew teammate"),
    (r"\bJerome\b", "an earlier teammate"),
    (r"\bChrisW\b", "the JS-crew teammate"),
    (r"ChrisW's", "the JS-crew teammate's"),
    (r"\bBilly\b", "the senior engineer"),
    (r"\bLuke\b(?!')", "the CEO"),
    (r"Luke's", "the CEO's"),
    (r"\bKai\b(?='s\spost)", "a teammate"),
    (r"\bLance\b(?!\sSmith)", "the architect"),
    (r"\bTom\b(?=\s(?:replied|wrote|posted|asked|said|'s))", "the teammate"),
    (r"Tom's", "the teammate's"),
    (r"\bSam\b(?=\sasked\swhere)", "the squad product lead"),
    (r"\bSam\b(?=\sultimately|\sat\sthe\ssame\stime|\sCrome|\:)", "the squad product lead"),
    (r"\bMark\b(?=\sredirected)", "the platform engineer"),
    # Generic isolated mentions where the person is clearly the DBA / platform / etc
    # Avoid Sam (could be Sam Henry handle reference). Already explicit forms above.
]

# Specific phrase fixes to avoid awkward grammar after replacements
PHRASE_FIXES = [
    ("Clem has gone mad with power after becoming feature lead", "Clem has gone mad with power after becoming feature lead"),  # keep
    # Personal-fork repo path identifiers
    ("`lcallaway/cm-rsc`", "`[teammate]/cm-rsc`"),
    ("lcallaway/cm-rsc (React Server Components POC", "[teammate]/cm-rsc (React Server Components POC"),
    ("React Server Components POC (lcallaway/cm-rsc)", "React Server Components POC ([teammate]/cm-rsc)"),
    # Slack handle of Clement, "Hey @blacksmith" mentions
    # Keep @blacksmith since it's Clement's handle
    # "@brian-luc" inline mentions
    ("Had a chat with @brian-luc about this", "Had a chat with a teammate about this"),
    # "with sha and ishworg" — both are teammates
    ("sha, ishworg, lcallaway all submitted to your reviewer team", "three teammates all submitted to your reviewer team"),
    ("for sha and ishworg on the prototype", "for two teammates on the prototype"),
    # Tom's quoted reply
    ("Tom replied with the famous", "The teammate replied with the famous"),
    ("Tom Evans (onboarding survey", "a teammate (onboarding survey"),
    # Hien-specific phrases
    ("with Hien (11pm", "with a teammate (11pm"),
    ("Hien followed up", "the DBA followed up"),
    ("Hien noticed", "The teammate noticed"),
    ("Hien:", "teammate:"),
    ("Co-authored with Hien Dang", "Co-authored with a DBA"),
    # Mark-specific
    ("Mark redirected to Zoom", "the platform engineer redirected to Zoom"),
    ("Mark redirected to a Zoom", "the platform engineer redirected to a Zoom"),
    # Lance/Architect already in place from architect references
    ("the OK from architects (Lance)", "the OK from architects"),
    # CEO video
    ("transcript for Luke's video", "transcript for the CEO's video"),
    # "chatted with Mick" + similar
    ("chatted with Mick", "chatted with the DBA"),
    ("Chatted with DBA (Mick)", "Chatted with the DBA"),
    ("DBA (Mick)", "the DBA"),
    ("DBA (Mick Proust)", "the DBA"),
    ("DBA (Mick Proust, Hien Dang, Mark Green)", "DBAs and platform engineers"),
    # Onboarding stats request to Tom Evans
    ("Onboarding stats request to Tom Evans", "Onboarding stats request to a teammate"),
    ("asking Tom Evans whether", "asking a teammate whether"),
    # Christopher Luong narrative
    ("design call with junior", "design call with junior engineer"),
    # Sam Crome lines
    ("with the Boole product lead Sam Crome", "with the squad product lead"),
    ("Sam Crome asked where", "The squad product lead asked where"),
    # Lance Smith's LDR template
    ("Lance Smith's", "the architect's"),
    # Adel Helal etc — already covered above
]

# ----- Customer / company-name redactions -----
CUSTOMER_REPLACEMENTS = [
    ("Glidewell Dental P2", "Enterprise-customer P2"),
    ("Glidewell P2", "Enterprise-customer P2"),
    ("Glidewell Dental", "an enterprise customer"),
    # The Feb 2026 Glidewell Dental incident → generic enterprise-customer incident
    ("Feb 2026 Glidewell Dental incident", "a Feb 2026 enterprise-customer incident"),
]

# ----- Handle replacements -----
def build_handle_substitutions():
    subs = []
    # Sort by length DESC so longer handles match first (e.g. "david-vanlaarveth" before "david")
    for handle in sorted(ALL_HANDLES, key=len, reverse=True):
        role = role_for(handle)
        # In table cells: `| handle |`
        subs.append((rf"\| {re.escape(handle)} \|", f"| {role} |"))
        # In "Top reviewed authors" / similar inline lists: `handle (N)` -> `engineer (N)`
        subs.append((rf"\b{re.escape(handle)} \((\d+)\)", lambda m, r=role: f"{r} ({m.group(1)})"))
        # In "reviewing X's PR" phrasing: `reviewing handle's PR`
        subs.append((rf"reviewing {re.escape(handle)}'s PR", f"reviewing a teammate's PR"))
        # In "— handle's PR" markdown
        subs.append((rf"— {re.escape(handle)}'s PR", f"— a teammate's PR"))
        # Just standalone `handle` followed by certain tokens (apostrophe s, etc.)
        # — too risky to globally replace; we'll catch known cases above.
    return subs

HANDLE_SUBS = build_handle_substitutions()


def apply(text: str) -> str:
    # 1) Full names (longest first)
    for old, new in FULL_NAME_REPLACEMENTS:
        text = text.replace(old, new)
    # 2) Customer-specific phrases
    for old, new in CUSTOMER_REPLACEMENTS:
        text = text.replace(old, new)
    # 3) Phrase fixes (with names embedded)
    for old, new in PHRASE_FIXES:
        text = text.replace(old, new)
    # 4) First-name-only via regex
    for pat, repl in FIRST_NAME_REPLACEMENTS:
        text = re.sub(pat, repl, text)
    # 5) Handle substitutions
    for pat, repl in HANDLE_SUBS:
        if callable(repl):
            text = re.sub(pat, repl, text)
        else:
            text = re.sub(pat, repl, text)
    return text


def main():
    changed = 0
    for rel in TARGETS:
        p = ROOT / rel
        if not p.exists():
            print(f"SKIP (missing): {rel}", file=sys.stderr)
            continue
        old = p.read_text()
        new = apply(old)
        if new != old:
            p.write_text(new)
            changed += 1
            print(f"updated: {rel}")
        else:
            print(f"unchanged: {rel}")
    print(f"\n{changed} files changed.")


if __name__ == "__main__":
    main()
