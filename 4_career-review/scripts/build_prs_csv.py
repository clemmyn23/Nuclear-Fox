import json
import csv
import re
import os
from collections import Counter

FILES = [
    '/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019017523.txt',
    '/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019018012.txt',
    '/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019019612.txt',
    '/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019021115.txt',
    '/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019021659.txt',
    '/Users/clementng/.claude/projects/-Users-clementng-dev-code-knowledge-graph/24e3d0ab-2418-4584-886f-1ae33b8e2c87/tool-results/mcp-gitcampmon-search_pull_requests-1780019021857.txt',
]

OUT = '/Users/clementng/dev/code-knowledge-graph/.tmp_authored-prs.csv'
FINAL_OUT = '/Users/clementng/career-review/data/authored-prs.csv'
JIRA_RE = re.compile(r'^([A-Z]+-\d+)')

all_items = []
total_count_seen = None

for path in FILES:
    with open(path) as f:
        d = json.load(f)
    if total_count_seen is None:
        total_count_seen = d.get('total_count')
    items = d.get('items', [])
    print(f"{os.path.basename(path)}: {len(items)} items (total_count={d.get('total_count')})")
    all_items.extend(items)

print(f"Total items collected: {len(all_items)}")
print(f"API total_count: {total_count_seen}")

# Dedup by html_url (just in case)
seen_urls = set()
unique = []
for it in all_items:
    url = it.get('html_url')
    if url in seen_urls:
        continue
    seen_urls.add(url)
    unique.append(it)
print(f"Unique items: {len(unique)}")

os.makedirs(os.path.dirname(OUT), exist_ok=True)

with open(OUT, 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow([
        'created_at','year','month','repo_owner','repo_name','pr_number',
        'state','merged','merged_at','jira_key','jira_project',
        'comments_count','title','html_url'
    ])
    for it in unique:
        created_at = it.get('created_at', '') or ''
        year = created_at[:4] if created_at else ''
        month = created_at[:7] if created_at else ''
        html_url = it.get('html_url', '') or ''
        repo_owner = ''
        repo_name = ''
        m = re.match(r'https?://[^/]+/([^/]+)/([^/]+)/pull/\d+', html_url)
        if m:
            repo_owner = m.group(1)
            repo_name = m.group(2)
        else:
            ru = it.get('repository_url','') or ''
            m2 = re.match(r'.*/repos/([^/]+)/([^/]+)$', ru)
            if m2:
                repo_owner = m2.group(1)
                repo_name = m2.group(2)
        pr_number = it.get('number','')
        state = it.get('state','') or ''
        pr_sub = it.get('pull_request') or {}
        merged_at = pr_sub.get('merged_at') or ''
        merged = 'true' if merged_at else 'false'
        title = it.get('title','') or ''
        jm = JIRA_RE.match(title)
        jira_key = jm.group(1) if jm else ''
        jira_project = jira_key.split('-')[0] if jira_key else ''
        comments_count = it.get('comments', 0)
        writer.writerow([
            created_at, year, month, repo_owner, repo_name, pr_number,
            state, merged, merged_at, jira_key, jira_project,
            comments_count, title, html_url
        ])

year_counts = Counter()
proj_counts = Counter()
repo_counts = Counter()
for it in unique:
    ca = it.get('created_at','') or ''
    if ca: year_counts[ca[:4]] += 1
    t = it.get('title','') or ''
    jm = JIRA_RE.match(t)
    proj = jm.group(1).split('-')[0] if jm else '(none)'
    proj_counts[proj] += 1
    hu = it.get('html_url','') or ''
    m = re.match(r'https?://[^/]+/([^/]+)/([^/]+)/pull/\d+', hu)
    if m:
        repo_counts[f"{m.group(1)}/{m.group(2)}"] += 1

print("\n=== YEAR BREAKDOWN ===")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}")

print("\n=== JIRA PROJECT BREAKDOWN ===")
for p, c in sorted(proj_counts.items(), key=lambda x: -x[1]):
    print(f"  {p}: {c}")

print("\n=== TOP 10 REPOS ===")
for r, c in repo_counts.most_common(10):
    print(f"  {r}: {c}")

print(f"\nCSV written to: {OUT}")
