# Standing instructions for Claude in this repo

## NEVER create background / polling tasks
Do NOT spawn background tasks, monitoring loops, "wait until live" checks,
sleep-and-retry loops, or any recurring job — ever. If the user wants to check
whether something is live they will ask explicitly. No TaskCreate, no Bash
run_in_background polling, no Monitor loops for deployment status.

## "Awesome" means technical depth, not infra
When the user says "make it awesome" or similar, interpret that as:
deepen the technical content, add worked examples, sharpen explanations.
Do NOT add infra (RSS, sitemap, dark mode, favicons, share previews, etc.)
unless explicitly asked. Infra is already done. For any infra request: answer
yes/no and do nothing.

## Word rules (banbluff + 1950s-auditor)
All teaching content must obey MASTER_RULES (see reports/MASTER_RULES.md).
Key banned words in teaching path: intuition, crucial, robust, understand,
concept (as noun), framework, iteration. Substitution table is in MASTER_RULES.

## Branch
Development branch: claude/quirky-goodall-XcgGO
Never push to a different branch without explicit permission.
Never create a PR unless the user explicitly asks.
