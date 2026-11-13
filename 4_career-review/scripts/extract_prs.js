#!/usr/bin/env node
const fs = require('fs');

const [inPath, outPath] = process.argv.slice(2);
const data = JSON.parse(fs.readFileSync(inPath, 'utf8'));
const items = data.items || [];
const out = [];
for (const it of items) {
  const repoUrl = it.repository_url || '';
  const parts = repoUrl.replace(/\/+$/, '').split('/');
  let owner = parts.length >= 2 ? parts[parts.length - 2] : '';
  let repo = parts.length >= 1 ? parts[parts.length - 1] : '';
  if (!owner || !repo) {
    const m = (it.html_url || '').replace('https://git.campmon.com/', '').split('/');
    if (m.length >= 2) { owner = m[0]; repo = m[1]; }
  }
  out.push({
    number: it.number,
    title: it.title || '',
    created_at: it.created_at || '',
    author: (it.user && it.user.login) || '',
    owner,
    repo,
    html_url: it.html_url || '',
  });
}
const mode = fs.existsSync(outPath) ? 'a' : 'w';
const fd = fs.openSync(outPath, mode === 'a' ? 'a' : 'w');
for (const row of out) {
  fs.writeSync(fd, JSON.stringify(row) + '\n');
}
fs.closeSync(fd);
console.log(`Extracted ${out.length} PRs to ${outPath}`);
console.log(`Total reported: ${data.total_count}`);
