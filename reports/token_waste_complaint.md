## REDDIT POST — r/ClaudeAI

**Title: Parallel background agents + session limits = you pay twice for the same work. This is a billing bug, not a UX issue.**

I've been using Claude Code on the web (remote container sessions) for a large refactoring project — 23 files to update with a consistent style change. Claude's recommended approach is to spawn 10 parallel background agents that each edit 2-3 files, then push to git.

Here is the exact failure loop I keep hitting:

1. I start a 5-hour usage window. Claude spawns 10 background agents.
2. 9 agents complete their file edits and push. The 10th is still running.
3. My token budget runs out mid-session (all 10 agents are burning tokens in parallel — the burn rate is 10x).
4. Session ends. The container is wiped. The 10th agent's work is gone.
5. Next 5-hour window: I have to re-run the same task from scratch — but I can't see which files were already edited without re-reading all of them, because I cannot peek into the previous container.
6. Tokens burn again for work that was already done.

**The core problem:** Parallel agents multiply your token burn rate by N. Session limits cut the session mid-task. Completed sub-tasks are in a container I cannot inspect after the session ends. So I pay for partial work, then pay again to redo it.

This is not a workflow problem — it is a billing integrity problem. If 9/10 tasks completed, I should only be charged for 1/10 of the retry. Instead I'm charged for 10/10 again because the system has no memory of what was durably committed vs. what was lost.

**What I lost:** An entire weekly token budget across two consecutive 5-hour windows. Both windows spent entirely on the same 23-file task. The work is done now (third attempt, main session, no parallel agents) — but I cannot get those tokens back.

**What I'm asking for:**
- A way to inspect what the previous container's git state was before it was wiped
- OR a "checkpoint" system where completed sub-tasks survive a session reset
- OR token credits when a session ends mid-parallel-task due to a budget limit (not user error)
- At minimum: a warning when spawning N parallel agents that your effective burn rate is N× and your session may not complete

Paying for the same work twice is not a usage policy edge case. It's a product design flaw that disproportionately punishes users who follow Claude's own recommended parallel-agent patterns.

---

## ANTHROPIC SUPPORT MESSAGE

**Subject: Token billing loss due to parallel agent + session limit interaction — request for credit review**

Hi Anthropic support,

I am writing to report a token loss issue that I believe constitutes a billing integrity problem, not a usage edge case.

**What happened:**

I was using Claude Code on the web (remote container, learnrahulrai-ui/ml_blog) to apply a consistent style update across 23 blog post files. Claude Code's own recommended approach for this kind of task is to spawn parallel background agents. I followed that recommendation.

The failure loop:

- Session 1 (5-hour window): 10 parallel background agents spawned. ~9 files completed and pushed to GitHub. Session ended due to token budget exhaustion before the final agent completed. Container wiped.
- Session 2 (next 5-hour window): No way to inspect the previous container state. Forced to re-audit all 23 files to find what was done and what was not. Token budget again depleted on partially-duplicate work.
- Session 3: Abandoned parallel agents entirely. Did all work in the main session. Task completed.

**The billing problem:**

Parallel agents multiply token burn at N× the single-agent rate. Session/budget limits can terminate a session mid-task. Completed sub-task results exist only in the ephemeral container — I cannot read them after the container is wiped, so I cannot selectively redo only the incomplete work. The result is that I paid for the same file edits 2–3 times.

This is not a mistake on my part. I followed Claude's recommended workflow. The architecture creates a situation where a user who follows best practices is penalized.

**What I am requesting:**

1. A review of my recent token usage (account: learn.rahul.rai@gmail.com) and credit for the duplicate burn caused by this loop.
2. A product-level fix or warning: when N parallel background agents are spawned, users should be warned that their effective token burn rate is N× and that incomplete tasks will not survive a session reset.
3. Ideally: a mechanism to inspect a previous container's git diff before it is wiped, so a user can resume from an accurate checkpoint rather than starting over.

I am a paying customer. I am not asking for a refund for productive work. I am asking for a credit for tokens spent doing the same work multiple times due to an architectural gap between the parallel-agent recommendation and the session-limit reality.

Thank you for reviewing this.

Rahul Rai
learn.rahul.rai@gmail.com
