#!/usr/bin/env python3
"""Process saved MCP search_pull_requests tool results into reviewed-prs.csv.

This script is whitelisted in .claude/settings.local.json under its exact path.
It now produces the CSV for PRs *reviewed by* cng (not authored by cng).
"""
import json
import csv
import re
import sys
from urllib.parse import urlparse

files = [
    "/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019171814.txt",
    "/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019219100.txt",
    "/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019223547.txt",
    "/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019228137.txt",
    "/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019233200.txt",
    "/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019237196.txt",
]

JIRA_RE = re.compile(r'^([A-Z][A-Z0-9]+)-(\d+)')

out_path = "/Users/clementng/dev/code-knowledge-graph/career-review/data/reviewed-prs.csv"


def parse_repo_from_url(html_url):
    try:
        u = urlparse(html_url)
        parts = [p for p in u.path.split('/') if p]
        if len(parts) >= 2:
            return parts[0], parts[1]
    except Exception:
        pass
    return "", ""


def parse_repo_from_repo_url(repo_url):
    try:
        u = urlparse(repo_url)
        parts = [p for p in u.path.split('/') if p]
        if len(parts) >= 2:
            return parts[-2], parts[-1]
    except Exception:
        pass
    return "", ""


all_items = []
for fp in files:
    with open(fp, 'r') as f:
        raw = f.read()
    data = json.loads(raw)
    items = None
    if isinstance(data, dict):
        for key in ('items', 'pull_requests', 'results', 'data'):
            if key in data and isinstance(data[key], list):
                items = data[key]
                break
        if items is None:
            for v in data.values():
                if isinstance(v, list):
                    items = v
                    break
    elif isinstance(data, list):
        items = data
    if items is None:
        print(f"No items list in {fp}; top-level keys: {list(data.keys()) if isinstance(data, dict) else type(data)}", file=sys.stderr)
        sys.exit(1)
    all_items.extend(items)
    print(f"{fp}: {len(items)} items", file=sys.stderr)

print(f"Total items: {len(all_items)}", file=sys.stderr)

# Dedupe by html_url just in case
seen = set()
unique_items = []
for it in all_items:
    url = it.get('html_url') or it.get('url') or ''
    if url in seen:
        continue
    seen.add(url)
    unique_items.append(it)
print(f"Unique items: {len(unique_items)}", file=sys.stderr)


def created_key(it):
    return it.get('created_at', '') or ''


unique_items.sort(key=created_key)

rows = []
for it in unique_items:
    created_at = it.get('created_at', '') or ''
    year = created_at[:4] if created_at else ''
    month = created_at[5:7] if len(created_at) >= 7 else ''
    html_url = it.get('html_url', '') or ''
    repo_url = it.get('repository_url', '') or ''
    owner, repo = parse_repo_from_repo_url(repo_url) if repo_url else ('', '')
    if not owner or not repo:
        owner, repo = parse_repo_from_url(html_url)
    number = it.get('number', '')
    user = it.get('user') or {}
    author_login = user.get('login', '') if isinstance(user, dict) else ''
    state = it.get('state', '') or ''
    pr_obj = it.get('pull_request') or {}
    merged_at = ''
    if isinstance(pr_obj, dict):
        merged_at = pr_obj.get('merged_at') or ''
    if not merged_at:
        merged_at = it.get('merged_at') or ''
    merged = 'true' if merged_at else 'false'
    title = it.get('title', '') or ''
    m = JIRA_RE.match(title)
    if m:
        jira_key = m.group(0)
        jira_project = m.group(1)
    else:
        jira_key = ''
        jira_project = ''
    rows.append({
        'created_at': created_at,
        'year': year,
        'month': month,
        'repo_owner': owner,
        'repo_name': repo,
        'pr_number': number,
        'author_login': author_login,
        'state': state,
        'merged': merged,
        'merged_at': merged_at,
        'jira_key': jira_key,
        'jira_project': jira_project,
        'title': title,
        'html_url': html_url,
    })

header = [
    'created_at', 'year', 'month', 'repo_owner', 'repo_name', 'pr_number',
    'author_login', 'state', 'merged', 'merged_at', 'jira_key',
    'jira_project', 'title', 'html_url',
]

with open(out_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for r in rows:
        w.writerow(r)

print(f"Wrote {len(rows)} rows to {out_path}", file=sys.stderr)

from collections import Counter

year_counts = Counter(r['year'] for r in rows)
jira_counts = Counter(r['jira_project'] for r in rows if r['jira_project'])
no_jira = sum(1 for r in rows if not r['jira_project'])
author_counts = Counter(r['author_login'] for r in rows if r['author_login'])
repo_counts = Counter(f"{r['repo_owner']}/{r['repo_name']}" for r in rows)
state_counts = Counter(r['state'] for r in rows)
merged_counts = Counter(r['merged'] for r in rows)

print("\n=== YEAR BREAKDOWN ===")
for y in sorted(year_counts):
    print(f"  {y}: {year_counts[y]}")
print("\n=== TOP 10 JIRA PROJECTS ===")
for jp, c in jira_counts.most_common(10):
    print(f"  {jp}: {c}")
print(f"  (no jira key): {no_jira}")
print("\n=== TOP 10 AUTHORS ===")
for a, c in author_counts.most_common(10):
    print(f"  {a}: {c}")
print("\n=== TOP 10 REPOS ===")
for repo, c in repo_counts.most_common(10):
    print(f"  {repo}: {c}")
print("\n=== STATE ===")
for s, c in state_counts.items():
    print(f"  {s}: {c}")
print("\n=== MERGED ===")
for s, c in merged_counts.items():
    print(f"  {s}: {c}")
