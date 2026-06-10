RULES FILTERED FOR THIS BLOG
═══════════════════════════════════════════════════════════════

CONTEXT:
  Blog uses example-driven (inductive) teaching.
  Shows patterns in data FIRST, derives why later.
  Opposite of strict axiom-first.

═══════════════════════════════════════════════════════════════
SECTION A: AXIOMATIC DERIVATION — PARTIAL FIT
═══════════════════════════════════════════════════════════════

A1. Line N uses only {1..N-1}
    STATUS: INTENTIONALLY VIOLATED
    WHY: Blog introduces concepts via examples first.
         Example: "Gini impurity" explained as intuition ("chance two grabs disagree")
                  BEFORE formula (1 - p² - q²)
    KEEP? No. This blog prioritizes intuition over axiom order.

A2-A7. Axiomatic foundations
    STATUS: PARTIALLY IMPLEMENTED
    WHERE: Once concept is introduced, derivation follows.
           Example: L71 introduces "ask-closest"
                   L87 defines it ("pick the k closest")
                   L95 derives it ("measure gap formula")
    KEEP? YES. After introduction, derive fully before moving on.

A8. Track NEW THINGS INTRODUCED
    STATUS: IMPLEMENTED
    WHERE: Common Tripwires I Caught sections catch exactly these.
           "TRIPWIRE 1: Standardise first" = catching undefined use of "ruler"
           "TRIPWIRE 2: k-means needs round, similar-sized clumps" = boundary of method
    KEEP? YES. This is the blog's empirical quality control.

═══════════════════════════════════════════════════════════════
SECTION B: PRESENTATION ORDER — PARTIAL FIT
═══════════════════════════════════════════════════════════════

B1. Answer starts with numerical actions
    STATUS: VIOLATED
    PATTERN: Blog structure is: picture → idea → numbers
    Example: PCA post
             1. "Shine flashlight on dots" (intuition/picture)
             2. "Longest shadow is PC1" (idea)
             3. "3², 4² = 25 = 9+16" (numbers)
    KEEP? Partially. Within each section, move faster to numbers.

B2-B3. Numbers/symbols before English
    STATUS: ACHIEVED
    WHERE: Within sections, formulas appear before prose explanation.
           Example: "Rᵢⱼ ← Rᵢⱼ - μⱼ" (formula)
                    "The middle is computed from present values only" (prose)
    KEEP? YES. Already done well.

═══════════════════════════════════════════════════════════════
SECTION C: TUTORING METHODOLOGY — STRONG FIT
═══════════════════════════════════════════════════════════════

C12. Do NOT provide solution; provide steps
    STATUS: IMPLEMENTED
    WHERE: Every post shows worked examples, not closed-form answers.
           Example: K-means post builds the algorithm step-by-step with 6 dots.
                    Reader follows arithmetic themselves.
    KEEP? YES. Core to blog's pedagogy.

C13-C19. What/Why/How, refresh, reason
    STATUS: PARTIALLY IMPLEMENTED
    WHERE: Tripwires provide WHY (catch the trap).
           Worked examples provide HOW.
           Missing: explicit "previous/next 10 steps" comparison.
    KEEP? YES. Add more "this connects to [prior section]" signposts.

═══════════════════════════════════════════════════════════════
SECTION D: 10-STEP PROTOCOL — STRONG FIT
═══════════════════════════════════════════════════════════════

D20-D31. Extract → numerical → shortcuts → simulation → patterns → visuals → checks
    STATUS: IMPLEMENTED ACROSS ALL POSTS
    WHERE:
      D20 Extract: No pure prose; always extract meaning into structure
      D21 Numerical action: Formulas appear early
      D22 Shortcuts: "Why squared gaps, not absolute?" answered in tripwires
      D23 Simulation: Worked examples with real numbers (6 dots, 4 wines, 50 states)
      D24 Step-by-step: Line-by-line arithmetic shown
      D25 Key concepts: "Gini is chance two grabs disagree" stated upfront
      D26 Breakdown: Large ideas split into parts (e.g., "ASSIGN" then "UPDATE")
      D27 Patterns: "Tightness only falls, never rises" (pattern across rounds)
      D28 Visuals: ASCII diagrams at every key step
      D29 Checks: "Is this pure side?" "Does the dendrogram freeze?"
      D30 Exercises: "Try K=3, calculate tightness" (implicit in structure)
      D31 Shortcuts: "Why no root?" answered (monotonicity preserved)
    KEEP? YES. All 12 rules implemented. This is the blog's core strength.

═══════════════════════════════════════════════════════════════
SECTION E: DEEP REASONING — MODERATE FIT
═══════════════════════════════════════════════════════════════

E32. Scan from middle; move to end; then to start
    STATUS: NOT EXPLICIT
    WHERE: Blog structure is linear. Readers follow top-to-bottom.
    KEEP? No (would violate blog's intentional linearity).
    ADAPT: Add section called "The Crux" that explicitly identifies the pivot.
           Example: K-means crux = "UPDATE moves centre to mean"
                   Why? Minimizes squared deviation (back to axiom).
                   What follows? Loop convergence guaranteed.
                   What precedes? Pile formation (needed first).

E33-E36. Reason crux, then forward, then backward
    STATUS: IMPLICIT
    WHERE: Derivations follow logically, but not called out as crux reasoning.
    KEEP? YES. Make it explicit via "The Crux" sections.

═══════════════════════════════════════════════════════════════
SECTION F: VERIFICATION — STRONG FIT
═══════════════════════════════════════════════════════════════

F37-F39. List NEW THINGS; acceptance checklist
    STATUS: IMPLEMENTED AS TRIPWIRES + LABELS
    WHERE:
      "NEW THINGS" = Common Tripwires I Caught (caught empirically)
      Checklist items:
        ☐ No forward refs       → enforced by linear structure
        ☐ Numerical examples    → all posts have 3+ worked examples
        ☐ Every symbol defined  → "Labels, Last" ensures backfill
        ☐ Formula derivation    → shown step-by-step
        ☐ Shortcuts explained   → "Why squared, not absolute?"
        ☐ Puzzle steps, not sol → worked examples don't give closed form
        ☐ Middle→both ends      → not yet (need "Crux" section)
        ☐ Checks provided       → "Check:" appears throughout
    KEEP? YES. Adapt checklist to blog's actual items (Tripwires, Labels, Examples).

═══════════════════════════════════════════════════════════════
SUMMARY: RULES FOR THIS BLOG
═══════════════════════════════════════════════════════════════

KEEP (implement fully):
  ✓ A8    Track empirical tripwires
  ✓ B2-B3 Formulas before prose
  ✓ C12   Steps, not solutions
  ✓ C13-C19 What/Why/How with refresh
  ✓ D20-D31 10-step protocol (extract→checks)
  ✓ F37-F39 Verification via tripwires + labels

ADAPT (modify for blog):
  ~ E32-E36 Add explicit "Crux" sections (middle→both ends reasoning)
  ~ A1     Soften to: "After introduction, maintain sequential logic"
  ~ B1     Change to: "Each section concludes with numerical example before next idea"

REJECT (incompatible):
  ✗ A1 (strict) Line N uses {1..N-1} axiom-first
       Reason: Blog is example-first by design; OK because tripwires catch undefined use.

═══════════════════════════════════════════════════════════════
ADAPTED CHECKLIST FOR THIS BLOG:
═══════════════════════════════════════════════════════════════

Post acceptance requires:
  ☐ At least 3 worked examples with real numbers
  ☐ All formulas derived step-by-step (not just stated)
  ☐ ASCII diagrams before complex ideas
  ☐ One "Crux" section explaining middle→both ends
  ☐ "Common Tripwires" section (empirical catches)
  ☐ "Labels, Last" section (jargon backfill)
  ☐ Code section at end (after all derivation)
  ☐ At least one "Check" verification step per section
  ☐ Shortcuts explained (why squared, not absolute, etc.)
  ☐ Clear sequential path: intro → worked → tripwires → labels → code

All ☐ checked → POST ACCEPTED
Any ☐ unchecked → POST NEEDS REVISION

═══════════════════════════════════════════════════════════════
END OF FILTERED RULES
═══════════════════════════════════════════════════════════════
