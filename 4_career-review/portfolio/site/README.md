# Personal Site — six drop-in single-pagers

Six complete, **zero-dependency** `index.html` variants (inline CSS + JS, no external fonts/images/CDNs — they work offline and load instantly). Pick one, rename it to `index.html`, ship it.

| File | Vibe | Best if you want… |
|---|---|---|
| [`index-rpg.html`](index-rpg.html) | 🔨 **Fantasy / forge "character sheet"** — ember palette, skill bars, passive abilities, trophy hall, spark cursor | maximum personality; leans into `blacksmith` + fantasy + anime |
| [`index-terminal.html`](index-terminal.html) | 💻 **Interactive CLI** — boots up, then a real command parser (`help`, `neofetch`, `smash`, `sudo`, `cat secret`…), arrow-key history | dev cred + the most "playable" page |
| [`index-modern.html`](index-modern.html) | ✨ **Clean & playful** — typewriter hero, count-up stats, cards, ☕ light/dark toggle, cursor-cat | recruiter-safe default that's still fun |
| [`index-badge.html`](index-badge.html) | 🎟️ **Convention badge / ticket** — lanyard badge, CSS barcode, "SCAN TO ENTER" → confetti | the SMASH/event angle as the whole identity |
| [`index-vaporwave.html`](index-vaporwave.html) | 🌴 **Vaporwave / A E S T H E T I C** — sunset gradient, perspective grid floor, glitch text, retro windows, VHS scanlines, 鍛冶屋 kanji, marquee | the boldest, most fun-forward look |
| [`index-brutalist.html`](index-brutalist.html) | ◼️ **Brutalist** — stark black/white, thick borders, huge type, "MAKE IT MORE BRUTAL" invert toggle, deadpan manifesto | a sharp, design-literate, anti-fluff statement |

## What's real vs. flavour
Load-bearing facts are **true** across all four: 8+ years, 45,000+ attendees, 5 events / 0 critical failures, founding engineer → Director of IT, the stack, the talk link, LinkedIn. The jokes (∞ coffee, "survived 5 C-suites", cat ranks) are obviously jokes. Recruiters *will* click through from LinkedIn, so the real signal still lands on a skim.

## Before you deploy — 2-minute checklist
1. **Replace `https://github.com/YOUR_GITHUB`** with your real GitHub (or delete the link). It's tagged with a `<!-- TODO -->` in each file.
2. Confirm you're happy showing `clementng23@gmail.com` publicly (it's on your résumé already; swap if you prefer a different address).
3. Optional: add a `favicon` — a 🥣 chowder or 🔨 emoji favicon is on-brand. One line in `<head>`:
   `<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 16 16%22><text y=%2214%22 font-size=%2214%22>🔨</text></svg>">`
4. Each file has a console easter egg + Konami code (↑↑↓↓←→←→ B A). Open DevTools to check yours.

## Deploy (any of these, free)
- **GitHub Pages:** put your chosen file as `index.html` in a repo → Settings → Pages.
- **Netlify / Cloudflare Pages / Vercel:** drag-and-drop the file, done.
- **Your existing host:** just upload it.

## Accessibility / polish notes
- All four respect `prefers-reduced-motion` (animations/typewriter/cursor-cat disable).
- Cursor-cat and spark trails are desktop-only (`pointer:fine`) — disabled on touch.
- All responsive down to phone widths.
- They're independent — you can even host more than one (e.g. `/`, `/terminal`, `/badge`) and link between them for fun.

*Content source: [../personal-site-content.md](../personal-site-content.md). Remix freely.* 🔨🐱
