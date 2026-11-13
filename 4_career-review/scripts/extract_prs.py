#!/usr/bin/env python3
"""Extract minimal PR fields from a search_pull_requests JSON output file."""
import json
import sys
import os

def extract(in_path, out_path):
    with open(in_path) as f:
        data = json.load(f)
    items = data.get('items', [])
    out = []
    for it in items:
        repo_url = it.get('repository_url', '')
        parts = repo_url.rstrip('/').split('/')
        owner = parts[-2] if len(parts) >= 2 else ''
        repo = parts[-1] if len(parts) >= 1 else ''
        if not owner or not repo:
            html = it.get('html_url', '')
            m = html.replace('https://git.campmon.com/', '').split('/')
            if len(m) >= 2:
                owner = m[0]
                repo = m[1]
        out.append({
            'number': it.get('number'),
            'title': it.get('title', ''),
            'created_at': it.get('created_at', ''),
            'author': (it.get('user') or {}).get('login', ''),
            'owner': owner,
            'repo': repo,
            'html_url': it.get('html_url', ''),
        })
    mode = 'a' if os.path.exists(out_path) else 'w'
    with open(out_path, mode) as f:
        for row in out:
            f.write(json.dumps(row) + '\n')
    print(f"Extracted {len(out)} PRs to {out_path}")
    print(f"Total reported: {data.get('total_count')}")

if __name__ == '__main__':
    extract(sys.argv[1], sys.argv[2])
