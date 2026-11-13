#!/usr/bin/env python3
"""Parse PR search result files and accumulate to CSV."""
import json
import re
import csv
import sys

JIRA_RE = re.compile(r"^([A-Z]+-\d+)")

def extract_repo(item):
    repo_url = item.get("repository_url", "")
    if repo_url:
        parts = repo_url.rstrip("/").split("/")
        if len(parts) >= 2:
            return parts[-2], parts[-1]
    html = item.get("html_url", "")
    if html:
        m = re.match(r"https?://[^/]+/([^/]+)/([^/]+)/pull/", html)
        if m:
            return m.group(1), m.group(2)
    return "", ""

def parse_file(path):
    with open(path) as f:
        content = f.read().strip()
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        idx = content.find("{")
        if idx >= 0:
            data = json.loads(content[idx:])
        else:
            print(f"Could not parse {path}", file=sys.stderr)
            return [], 0
    items = data.get("items", [])
    total = data.get("total_count", len(items))
    if not items and isinstance(data, list):
        items = data
    return items, total

def process(items):
    rows = []
    for it in items:
        created_at = it.get("created_at", "") or ""
        year = created_at[:4]
        month = created_at[:7]
        owner, name = extract_repo(it)
        number = it.get("number", "")
        user = it.get("user") or {}
        author_login = user.get("login", "") if isinstance(user, dict) else ""
        state = it.get("state", "")
        pr = it.get("pull_request") or {}
        merged_at = it.get("merged_at") or pr.get("merged_at") or ""
        merged = "true" if merged_at else "false"
        title = it.get("title", "") or ""
        html_url = it.get("html_url", "")
        m = JIRA_RE.match(title)
        jira_key = m.group(1) if m else ""
        jira_project = jira_key.split("-")[0] if jira_key else ""
        rows.append({
            "created_at": created_at,
            "year": year,
            "month": month,
            "repo_owner": owner,
            "repo_name": name,
            "pr_number": number,
            "author_login": author_login,
            "state": state,
            "merged": merged,
            "merged_at": merged_at,
            "jira_key": jira_key,
            "jira_project": jira_project,
            "title": title,
            "html_url": html_url,
        })
    return rows

def write_csv(rows, out_path):
    fields = ["created_at","year","month","repo_owner","repo_name","pr_number","author_login","state","merged","merged_at","jira_key","jira_project","title","html_url"]
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows:
            w.writerow(r)

if __name__ == "__main__":
    files = sys.argv[1:]
    all_rows = []
    seen = set()
    total_reported = None
    for fp in files:
        items, total = parse_file(fp)
        if total_reported is None:
            total_reported = total
        rows = process(items)
        for r in rows:
            key = (r["repo_owner"], r["repo_name"], r["pr_number"])
            if key in seen:
                continue
            seen.add(key)
            all_rows.append(r)
        print(f"{fp}: {len(items)} items, total_count={total}, unique so far={len(all_rows)}", file=sys.stderr)
    all_rows.sort(key=lambda r: r["created_at"])
    write_csv(all_rows, "/Users/clementng/career-review/data/reviewed-prs.csv")
    print(f"Total reported by API: {total_reported}", file=sys.stderr)
    print(f"Wrote {len(all_rows)} rows", file=sys.stderr)
