# Parallel Background Agents and Duplicated Prefix Billing: A Detailed Technical Write-up

**Author:** Rahul Rai (learn.rahul.rai@gmail.com)
**Date:** 2026-06-11
**Context:** Claude Code on the web (remote ephemeral container), repository `learnrahulrai-ui/ml_blog`
**Status:** Reproduced across 3 consecutive sessions; root cause identified; credit + engineering fix requested

---

## 0. TL;DR

When Claude Code spawns *N* parallel background agents, each agent is an **independent, stateless inference session that does not share a KV cache with its siblings**. The read-only prefix common to all of them — system prompt, conversation history, and the file contents already read into context — is **re-encoded and re-billed once per agent** instead of once total. That shared prefix is typically **80–90% of each agent's input-token cost**, so a 10-agent fan-out can cost close to **10× the input tokens** of the equivalent shared-prefix design.

This interacts catastrophically with two other facts:

1. **Session/budget limits terminate the session mid-task.** The 5-hour usage window or token budget runs out while the Nth agent is still working.
2. **The container is ephemeral and wiped on session end, and cannot be inspected afterward.** Completed sub-task results that were not yet pushed to git are lost, and even pushed work cannot be diffed against the wiped working tree on resume.

The combined result: a single 23-file task was paid for **2–3 times**, because each retry re-encoded the entire shared prefix for every agent again. This is not user error — it is the *recommended* parallel-agent workflow behaving exactly as designed, and the design has a billing-integrity gap.

---

## 1. The task that triggered this

A mechanical, repetitive edit applied uniformly across 23 plain-text blog posts (`txt/posts/*.txt`): the "1950 Charter" rollout — adding IN HAND refresher blocks, YOUR TURN drills with checked answers, clerk-step cost counts, and code-section preambles to every post.

This is the textbook case for parallelism: 23 independent files, no cross-file dependencies, identical transformation. Claude Code's own guidance is to fan this out across multiple background agents working on non-overlapping files. I followed that guidance. Ten agents, ~2-3 files each.

---

## 2. The observed failure loop

```
SESSION 1  (5-hour window)
  - 10 parallel background agents spawned, each handed 2-3 files.
  - Each agent independently re-receives: system prompt + full conversation
    history + the file contents it must read.
  - ~9 agents complete their edits and push to GitHub.
  - Token budget exhausted (burn rate ~10x single-agent) before agent #10 finishes.
  - Session ends. Container wiped.

SESSION 2  (next 5-hour window)
  - Fresh container. No memory of session 1's working state.
  - Cannot inspect the previous container -> cannot see which files were
    actually finished vs. half-finished.
  - Forced to RE-READ all 23 files to reconstruct state. Spawn agents again.
  - Token budget again depleted on partially-duplicate work.

SESSION 3
  - Abandoned parallel agents entirely.
  - Did all 23 files sequentially in the main session.
  - Task finally completed.
```

Two full weekly windows were spent almost entirely re-paying for the same work.

---

## 3. Root cause: the shared prefix is `private`, not `shared`

### 3.1 How LLM serving normally avoids this

Modern inference servers (vLLM, TensorRT-LLM, SGLang, etc.) implement **prefix caching** (a.k.a. automatic prefix caching / radix-tree KV reuse). When two requests share a leading token sequence, the **KV cache for that shared prefix is computed once and reused**. The second request only pays compute/tokens for the *new* suffix. This is what makes multi-turn chat and shared-system-prompt fan-out affordable.

The critical precondition: the requests must hit the **same server with a warm cache for that prefix**, and the billing/accounting layer must recognize the reuse.

### 3.2 What breaks in the parallel-agent path

Each background agent is launched as an **independent inference session**. Empirically, the shared prefix is **not** deduplicated across these sibling sessions — each agent's full context is encoded and billed as fresh input:

```
Shared, identical across ALL agents (the read-only "prefix"):
  [ system prompt        ~3K tokens ]
  [ conversation history ~8K tokens ]
  [ file context read in ~5K tokens ]
  -----------------------------------
  ~16K tokens of IDENTICAL prefix

Billing actually observed:
  Agent 0:  16K input  (3K + 8K + 5K)   <- billed
  Agent 1:  16K input  (3K + 8K + 5K)   <- billed again, byte-identical prefix
  Agent 2:  16K input  (3K + 8K + 5K)   <- billed again
   ...
  Agent 9:  16K input  (3K + 8K + 5K)   <- billed again
  -----------------------------------
  Total: 160K input tokens, of which ~144K is the SAME prefix re-encoded 9 extra times.
```

Only the small, per-agent suffix (the specific 2-3 filenames and instructions) actually differs. Everything above it is replicated.

### 3.3 The OpenMP analogy (the exact mental model)

The orchestrator forks the agents as if the shared context were a thread-`private` variable — each thread gets its own full copy — when it should be a `shared` variable encoded once and pointed at by all threads:

```c
/* CURRENT BEHAVIOR -- shared context copied into every thread */
#pragma omp parallel for private(shared_context)
for (int i = 0; i < N; i++)
    edit_file(i, shared_context);   /* 16K prefix re-materialized per i */

/* CORRECT BEHAVIOR -- prefix encoded once, all threads reuse it */
#pragma omp parallel for shared(shared_context)
for (int i = 0; i < N; i++)
    edit_file(i, shared_context);   /* prefix KV computed once, suffix per i */
```

This is a classic data-scoping bug. The fix is conceptually a one-word change in scoping intent: the shared prefix must be `shared`, not `private`.

### 3.4 Why this is STRICTLY WORSE than a normal false-share

In ordinary parallel programming, the penalty for redundant work or false-sharing is **wasted CPU cycles** — undesirable, but free to retry and invisible on the bill. Here the redundant work is **billed input tokens**:

- **Not retryable for free.** Every re-encode of the prefix costs real money.
- **The budget cut is mid-task.** The session is terminated before the last agent finishes, so the work is both incomplete *and* already paid for.
- **The redo re-pays the whole prefix again.** Because the container is wiped and uninspectable, the next session re-reads everything and re-forks, re-billing the entire prefix N times over. The replication **compounds across sessions**, not just within one.

So the cost model is not `O(useful work)`. It is `O(N × prefix × number_of_retries)`.

---

## 4. The two amplifiers that turn waste into total loss

The prefix-replication bug alone would merely be expensive. Two architectural facts turn it into *unrecoverable* loss:

### 4.1 Session/budget limits terminate mid-task

The 5-hour window and token budget are wall-clock/quota limits that do not align with task boundaries. With burn rate at ~N×, a parallel fan-out reaches the limit far faster, and it reaches it **in the middle** of the agent set — after 9 of 10 agents but before completion. There is no "finish the current unit of work then stop" semantics.

### 4.2 The container is ephemeral AND uninspectable

The remote container is wiped on session end. Two distinct losses follow:

1. **Unpushed work is gone.** Any agent that finished editing but had not yet pushed loses its edits entirely.
2. **State cannot be reconstructed cheaply.** Even for pushed work, the next session cannot diff against the previous working tree — I cannot "peek into" the old container. So I cannot tell which files were truly done vs. half-done without **re-reading all of them**, which itself re-loads the context and re-incurs cost.

There is no checkpoint. There is no resumable transcript of "these 9 units committed, this 1 pending." The system has no durable memory of what was completed vs. lost, so it cannot bill the retry as "1/10 of the work remaining" — it bills it as "10/10 again."

---

## 5. Cost model: what should have been paid vs. what was paid

Let:
- `P` = shared prefix size (system prompt + history + file context) ≈ 16K tokens
- `s` = per-agent unique suffix ≈ 1K tokens
- `N` = number of parallel agents = 10
- `R` = number of session retries forced by budget cuts ≈ 3

**Ideal (prefix shared, single pass):**
```
cost = P + N*s = 16K + 10*1K = 26K input tokens
```

**Actual (prefix private, re-billed per agent, re-run per retry):**
```
cost = R * (N * (P + s)) = 3 * (10 * 17K) = 510K input tokens
```

**Overpayment factor ≈ 510K / 26K ≈ 19.6×.**

Even charitably ignoring the retries (`R=1`), the single-session factor is `170K / 26K ≈ 6.5×`. The numbers are illustrative, not metered exactly, but the order of magnitude is the point: the dominant cost term is the prefix, and it is being multiplied by both `N` and `R`.

---

## 6. What I am requesting

### 6.1 Immediate (billing)
A review of recent token usage on account `learn.rahul.rai@gmail.com`, and a **credit for the duplicated prefix burn** — the tokens spent re-encoding the identical shared prefix across sibling agents and across forced retries.

### 6.2 Engineering fix (the real one)
Apply **cross-session prefix-cache deduplication across the parallel agent fork.** The shared system-prompt + conversation-history + file-context prefix should be encoded **once** and reused by all `N` agents (`shared`, not `private`), rather than re-billed per agent. This is the same prefix-caching that already exists for sequential warm-cache requests — it simply needs to span the agent-fork boundary.

### 6.3 Guardrail (user-facing)
A **spawn-time warning**: "N parallel agents ≈ N× input-token burn on the shared prefix; incomplete tasks will not survive a session reset." Users following the recommended parallel pattern should be told its true cost and failure mode up front.

### 6.4 Durability (resumability)
A **checkpoint / inspection mechanism**: make a wiped container's git state (or at least a manifest of completed vs. pending units) readable on resume, so a session can continue from an accurate state instead of re-paying to re-audit from scratch. Equivalently: align session-limit termination with unit-of-work boundaries, and bill retries as remaining-work, not whole-work.

---

## 7. Why this matters beyond one account

This is not a personal edge case. It is a structural penalty on **exactly the workflow Claude Code recommends** for large mechanical tasks. Any user who fans out across background agents — the documented best practice — pays the prefix `N` times, and if a budget limit lands mid-fan-out, pays it again on every retry. The users hit hardest are the ones doing the largest, most legitimate batch work. The fix (prefix sharing across the fork) is well within the capability of the existing serving stack; it is an accounting/orchestration gap, not a fundamental limitation.

---

*This document accompanies `reports/token_waste_complaint.md`, which contains the ready-to-send Reddit post and Anthropic support ticket drafted from this analysis.*
