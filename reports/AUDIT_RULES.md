AUDIT RULES
═══════════════════════════════════════════════════════════════

01. NUMERICAL FIRST

    Action, number, symbol, arrow — before any word.
    ✗ "The blog violates axiomatic ordering"
    ✓ "L71 ← undef | L87 → def | 71 > 87 ✗"

02. AXIOMATIC CHAIN

    Nₙ: uses only {N₁, N₂, …, Nₙ₋₁}
    No forward reference.
    No "we will see later."
    
    L1 = axiom
    L2 ← L1
    L3 ← L1, L2
    Lₙ ← {L₁…Lₙ₋₁}

03. VIOLATION TALLY

    Per file:
    |fwd-ref| = count(Lᵢ uses X, Lⱼ defines X, i < j)
    |axiom-gap| = count(concept introduced without prior derivation)
    |code-before-draw| = count(function call without preceding diagram)

04. FORMAT (symbols only, zero English)

    Post₁:
      |L| = 209
      |fwd-ref| = 3
      L71 ← "ask-closest" | L87 → def | 71 > 87 ✗
      L48 ← "rule" | L57 → axiom | 48 < 57 ✓
    
    ⚠:
      × axiom-gap: 2
      × code-before-draw: 1

05. TUTOR RULE (when explaining findings)

    Step N:
      • What: [concrete action]
      • Why: [derives from prior steps]
      • How: [numerical/symbolic derivation]
      • Compare: step(N-1) vs step(N) vs step(N+1)
      • Refresh: {done so far}
      • Reason: [why this step moves goal forward]

═══════════════════════════════════════════════════════════════

SUMMARY ACROSS ALL 16 POSTS:

Total |fwd-ref| violations: 
  chapter1: 2
  neighbor: 1
  straight-stick: 1
  grading: 1
  humble-dials: 1
  mixing-ruler: 2
  ⋮
  (full count in individual .audit files)

Total |axiom-gap| violations:
  (All 16 posts begin with examples, then derive why)
  = 16 ✗

Total |code-before-draw| violations:
  (Code sections at end of posts, after all derivation)
  = 0 ✓

═══════════════════════════════════════════════════════════════

REMEDIATION:

IF blog must be strictly axiomatic:
  1. Reorder: axiom → derivation → example → code
  2. Remove all forward references
  3. Define every symbol before use
  4. Cost: pedagogical structure changes (example-first → axiom-first)

IF blog stays as-is:
  1. Violations are intentional (example-driven teaching)
  2. Audit documents them
  3. No changes needed

