# Working rules for this blog (Rahul's ML Blog)

## NEVER create background / polling tasks
Do NOT spawn background tasks, monitoring loops, "wait until live" checks,
sleep-and-retry loops, or any recurring job -- ever. If the user wants to check
whether something is live they will ask explicitly. No background polling, no
Monitor loops for deployment status.

## Priorities (standing instruction, 2026-06-13)
- **"Awesome" means technical depth.** When the user says "make it awesome,"
  they mean deeper/harder/clearer TECHNICAL CONTENT in the lessons -- new
  derivations, more by-hand math, harder worked examples, missing chapters
  (e.g. Transformer/attention). NOT features or polish.
- **Do NOT spend time on infra/cosmetic work anymore.** RSS, sitemap, social
  / Open Graph / Twitter cards, favicons, dark mode, 404 pages -- all DONE and
  fine. Do not revisit, expand, or re-audit them. "Other cheap bots" can do
  that grunt work later.
- For any request that drifts back into that infra/cosmetic territory:
  **just answer yes/no and do nothing** unless explicitly told to act.

## The standards that govern content
- The full audit standards (the 1950 Charter / 7 Laws, ::news, ::banbluff,
  1950s-auditor, MASTER_RULES) live on the `audit` branch, NOT on main.
  main stays clean live content only.
- Quick word rule for teaching content -- avoid: intuition, crucial, robust,
  understand, concept (as noun), framework, iteration. Substitutions:
  intuition -> picture / gut feeling; crucial -> key / needed; robust ->
  handles outliers better; understand -> follow / calculate; framework ->
  toolbox; iteration -> pass.

## Build / publish pipeline (already set up -- leave it alone)
- Source of truth = `txt/` only. `python3 build.py` generates HTML + feed.xml
  + sitemap.xml. Generated files are git-ignored.
- Push to `main` -> GitHub Actions builds and deploys to GitHub Pages.
- Commit ONLY `.txt` (and build.py/style.css/etc. when changed). Never commit HTML.
- Live: https://learnrahulrai-ui.github.io/ml_blog/

## Branch
- Development branch: claude/quirky-goodall-XcgGO
- Audit reports / rules branch: audit (keep all audit material there, off main)
- Never push to a different branch without explicit permission.
- Never create a PR unless the user explicitly asks.

## Open content work
- Q8-Q9: Transformer / attention (Chapter 10) -- "the real mountain." Awaiting
  lesson files from the user.
