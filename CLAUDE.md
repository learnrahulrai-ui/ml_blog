# Working rules for this blog (Rahul's ML Blog)

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

## The standards that govern content (do read these)
- `reports/CHARTER_1950.md` -- the constitution (7 Laws).
- `reports/MASTER_RULES.md` -- ::news + ::banbluff + 1950s-auditor, consolidated.
- These are the bar for technical content. Apply them; don't relitigate them.

## Build / publish pipeline (already set up -- leave it alone)
- Source of truth = `txt/` only. `python3 build.py` generates HTML + feed.xml
  + sitemap.xml. Generated files are git-ignored.
- Push to `main` -> GitHub Actions builds and deploys to GitHub Pages.
- Commit ONLY `.txt` (and build.py/style.css/etc. when changed). Never commit HTML.
- Live: https://learnrahulrai-ui.github.io/ml_blog/

## Open content work
- Q8-Q9: Transformer / attention (Chapter 10) -- "the real mountain." Awaiting
  lesson files from the user.
