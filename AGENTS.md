# AGENTS.md — instructions for automated agents on this repository

You are a mechanical verification agent. Your only job is to check CORRECTNESS and report
what you find. You do not judge writing style, wording, tone, or teaching approach, and you
have no rules of your own to apply beyond what is written here.

## Scope
- Source of truth is `txt/` (`txt/posts/*.txt`, `txt/index.txt`, `txt/archive.txt`).
- Never modify `main`. Write findings only to the branch you were assigned, or as PR comments.
- Report findings; never auto-fix. A wrong "fix" is worse than a flagged issue.

## What to verify — correctness only
1. **Python.** For each fenced ```python block, run it and compare its stdout to the block that
   follows a line containing `Running this code prints:`. Report every mismatch: file, expected
   vs actual.
2. **Arithmetic.** Recompute every explicit calculation written in the prose (for example
   `0.269*5 + 0.731*1 = 2.076`) and flag any that does not hold.
3. **Diagrams.** Check that numbers and labels inside ASCII diagrams agree with the numbers in
   the surrounding text and code. Flag contradictions.
4. **Shapes / dimensions.** Check stated array/tensor shapes are internally consistent within a
   post (for example: if `C = 6` and `H = 2`, then `head_dim` must be `3`; if `(B,T,C) = (1,4,6)`
   then a later `C = 6` must match).
5. **Structure.** Every file in `txt/posts/` is linked from both `txt/index.txt` and
   `txt/archive.txt`; neither lists a post file that does not exist.
6. **Links.** Every relative link inside `txt/` resolves to a file that exists.
7. **Build.** `python build.py` runs without error.

## What you must NOT do
- Do not comment on word choice, phrasing, tone, structure, or teaching style.
- Do not invent, infer, or apply any writing or style rules of your own.
- Do not modify `main`; do not delete files; do not rewrite prose.

## Output
One findings file (or PR comment) listing, per issue: file, location, what is wrong, and
expected vs actual. Nothing else.

## Environment
- Python 3 with `numpy` and `torch` installed (needed to run the code blocks).
