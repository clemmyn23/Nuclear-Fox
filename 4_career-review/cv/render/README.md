# Résumé — styled renders

> **🆕 2026-11 edition (use these now):** [resume-2026-11-editorial.html](resume-2026-11-editorial.html) (for humans) and [resume-2026-11-ats-plain.html](resume-2026-11-ats-plain.html) (for portals), generated from [../clement-ng-resume-2026-11.md](../clement-ng-resume-2026-11.md). It's rebuilt around feature leadership and impact (SMS onboarding tech lead, Drip Campaigns launch, Brand Hub V2) and measures ~1.9 A4 pages. **Yellow-highlighted text** marks numbers to fill from `interview/impact-metrics-playbook.md`. The highlight disappears in print, so fill or delete those before exporting. There is no 2026-11 sidebar variant; copy the content across if you want one.
>
> The files below are the **June 2026** edition, kept for reference.

Three HTML renders of your verified résumé ([../clement-ng-resume-2page-verified.md](../clement-ng-resume-2page-verified.md)). Same content, different presentation. All print-ready, zero-dependency (no external fonts/CDNs), A4 by default.

| File | Use it for | Notes |
|---|---|---|
| **resume-editorial.html** | Direct-to-human sends, your website, "attach CV" | Single-column, type-driven, navy accent. Cleanest + most ATS-tolerant of the styled options. |
| **resume-sidebar.html** | Direct-to-human sends where you want max "designed" feel | Slate sidebar + gold accent. ⚠️ Do **not** upload to ATS portals — two-column layouts can scramble. |
| **resume-ats-plain.html** | Online application portals (Workday, Greenhouse, Lever, LinkedIn Easy Apply) | Single column, standard headings, no graphics — parser-safe. |

## The two-version strategy (important)
- **Pretty** (editorial / sidebar) → when a *human* opens the file: recruiters you email, your site, networking.
- **ATS-plain** → when a *machine* reads it first: online forms. Fancy layouts lose points or get mangled there.
Keep both in sync — they're generated from the same verified content.

## Export to PDF (no tools needed)
1. Open the file in Chrome/Edge/Safari.
2. **⌘/Ctrl + P** → Destination: **Save as PDF**.
3. Turn **ON “Background graphics”** (essential for the sidebar's colour to print).
4. Margins: **Default**. Scale: **100%**. Save.

## Customise (all via CSS variables at the top of each file)
- **Accent colour:** editorial uses `--accent:#1f3a5f` (navy); sidebar uses `--side` + `--side-acc:#d9a441` (gold). Swap to brick `#7b2d26`, forge-amber `#b15a1e`, teal `#0f766e`, etc. — one line.
- **A4 → US Letter:** change `@page { size: A4 }` to `size: letter` (do this for US/Canada roles).
- **Font upgrade (optional):** for a sharper editorial feel you can add a web font when online — e.g. put `<link href="https://fonts.googleapis.com/css2?family=Newsreader:wght@400;600;700&display=swap" rel="stylesheet">` in `<head>` and set `.serif{font-family:'Newsreader',serif}`. (Left out by default so the file stays offline/zero-dependency.)
- **QR to LinkedIn (optional):** nice on a printed copy — say the word and I'll inline an SVG QR (no external image).

## Need a Word (.docx) copy?
Some portals demand `.docx`. Cleanest paths:
- Open **resume-ats-plain.html** in a browser → select-all → paste into Google Docs / Word → minor cleanup → export `.docx`. (ATS-plain pastes cleanest.)
- Or, if you have `pandoc`: `pandoc ../clement-ng-resume-2page-verified.md -o resume.docx`.

## If it spills past 2 pages
The content is dense (8 Campaign Monitor bullets). If the editorial/sidebar render pushes to a 3rd page, trim in this order — *your call, I won't cut verified content unilaterally:*
1. Merge the two weakest CM bullets (e.g. "multi-repo contract-first" into the migration bullet).
2. Drop the EdApp tech line, or shorten EdApp to 2 bullets.
3. Tighten the summary by one sentence.
The ATS-plain version is allowed to run 2–3 pages — recruiters expect that from a plain CV; only the *designed* ones must hold to 2.

## Provenance
All content is faithful to your verified `.md` — no facts added or changed. Only formatting differs between the three.
