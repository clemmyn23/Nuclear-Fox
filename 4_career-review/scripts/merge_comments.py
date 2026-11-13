"""
Merge per-PR comment JSON files in data/comments-per-pr/ into review-comments.csv
and own-pr-comments.csv. Run after all comments-fetch agents finish.
"""
import json
import csv
import glob
import os
from collections import Counter, defaultdict

ROOT = '/Users/clementng/dev/code-knowledge-graph/career-review'
PER_PR_DIR = f'{ROOT}/data/comments-per-pr'

def tenure_year(created_at):
    if not created_at:
        return None
    y, m = int(created_at[:4]), int(created_at[5:7])
    start_year = y if m >= 4 else (y - 1)
    return start_year - 2020

# Reviewed-PR review comments
review_files = sorted([f for f in glob.glob(f'{PER_PR_DIR}/*.json') if not os.path.basename(f).startswith('own-')])
print(f"Found {len(review_files)} review-comment files")

review_rows = []
for fp in review_files:
    try:
        with open(fp) as f:
            d = json.load(f)
        for c in d.get('comments', []):
            review_rows.append({
                'comment_created_at': c.get('created_at', ''),
                'comment_path': c.get('path', '') or '',
                'comment_html_url': c.get('html_url', ''),
                'pr_repo': d.get('pr_repo', ''),
                'pr_number': d.get('pr_number', ''),
                'pr_author': d.get('pr_author', ''),
                'pr_title': d.get('pr_title', ''),
                'pr_created_at': d.get('pr_created_at', ''),
                'comment_body': (c.get('body', '') or '').replace('\n', '\\n').replace('\r', '').replace('\t', '\\t'),
            })
    except Exception as e:
        print(f"Skip {fp}: {e}")

review_rows.sort(key=lambda r: r['comment_created_at'])
out_csv = f'{ROOT}/data/review-comments.csv'
with open(out_csv, 'w', newline='') as f:
    if review_rows:
        w = csv.DictWriter(f, fieldnames=list(review_rows[0].keys()))
        w.writeheader()
        w.writerows(review_rows)
    else:
        f.write('comment_created_at,comment_path,comment_html_url,pr_repo,pr_number,pr_author,pr_title,pr_created_at,comment_body\n')
print(f"Wrote {out_csv} — {len(review_rows)} comments")

# Own-PR comments
own_files = sorted([f for f in glob.glob(f'{PER_PR_DIR}/own-*.json')])
print(f"Found {len(own_files)} own-comment files")

own_rows = []
for fp in own_files:
    try:
        with open(fp) as f:
            d = json.load(f)
        for c in d.get('own_comments', []) or d.get('comments', []):
            own_rows.append({
                'comment_created_at': c.get('created_at', ''),
                'comment_html_url': c.get('html_url', ''),
                'pr_repo': d.get('pr_repo', ''),
                'pr_number': d.get('pr_number', ''),
                'pr_title': d.get('pr_title', ''),
                'pr_created_at': d.get('pr_created_at', ''),
                'comment_body': (c.get('body', '') or '').replace('\n', '\\n').replace('\r', '').replace('\t', '\\t'),
            })
    except Exception as e:
        print(f"Skip {fp}: {e}")

own_rows.sort(key=lambda r: r['comment_created_at'])
out_csv2 = f'{ROOT}/data/own-pr-comments.csv'
with open(out_csv2, 'w', newline='') as f:
    if own_rows:
        w = csv.DictWriter(f, fieldnames=list(own_rows[0].keys()))
        w.writeheader()
        w.writerows(own_rows)
    else:
        f.write('comment_created_at,comment_html_url,pr_repo,pr_number,pr_title,pr_created_at,comment_body\n')
print(f"Wrote {out_csv2} — {len(own_rows)} comments")

# Stats
print("\n=== REVIEW COMMENTS — YEAR BREAKDOWN ===")
y_counts = Counter(tenure_year(r['comment_created_at']) for r in review_rows)
for y in sorted(k for k in y_counts if k is not None):
    print(f"  Y{y}: {y_counts[y]}")

print("\n=== TOP PR AUTHORS REVIEWED (by comment count) ===")
author_counts = Counter(r['pr_author'] for r in review_rows)
for a, c in author_counts.most_common(20):
    print(f"  {a}: {c}")

print("\n=== TOP FILE PATHS ===")
path_counts = Counter(r['comment_path'] for r in review_rows if r['comment_path'])
for p, c in path_counts.most_common(15):
    print(f"  {p}: {c}")

print("\n=== TOP FILE EXTENSIONS ===")
ext_counts = Counter(os.path.splitext(r['comment_path'])[1] for r in review_rows if r['comment_path'])
for e, c in ext_counts.most_common(15):
    print(f"  {e}: {c}")
