COMPREHENSIVE RULES FOR BLOG AUDIT AND TUTORING
═══════════════════════════════════════════════════════════════

FOUNDATIONAL AXIOM:
  Audience: counting + coding basics + some math. Nothing else assumed.
  No new words without definition. No new ideas without derivation.
  Every line traces to axioms. Every step justified.

═══════════════════════════════════════════════════════════════
SECTION A: AXIOMATIC DERIVATION (NO FORWARD REFERENCES)
═══════════════════════════════════════════════════════════════

01. Line N uses only {Line 1, Line 2, …, Line N-1}
    Strict sequential dependency.
    No "we will see later."
    No "as mentioned below."
    No forward references.

02. Line 1 = first axiom (no dependencies)
    Example: "count = tally of items" (self-evident)

03. Line 2 = uses only Line 1
    Example: "sum = add counts together"
    ← depends on Line 1's definition of count

04. Line N = uses only Lines 1 to N-1
    Lₙ := f(L₁, L₂, …, Lₙ₋₁)
    No Lₘ where m > n

05. If line N uses value X:
    Line N-1 or earlier MUST have calculated X.
    ✗ "Let α = 0.5 without prior calculation"
    ✓ "Set α ← sum of errors / count of items = 0.5"

06. If line N uses formula F:
    Line N-1 or earlier MUST have derived F.
    ✗ "Apply the gradient descent rule"
    ✓ "Gradient of sum(squared errors) = 2×Σ(error × input)"
       "Apply: move parameter in direction opposite gradient"

07. If line N references address/location A:
    Line N-1 or earlier MUST have computed A.
    ✗ "Look at cell [3,5]"
    ✓ "Row = first group + second group = 3"
       "Column = measurements 1,2,3,4,5 → position 5"
       "Cell [3,5] now defined"

08. NEW THINGS INTRODUCED WITHOUT DERIVATION:
    Track these. If list not empty → FILE REJECTED.
    
    Example violation:
    ✗ L71: "ask-closest rule at k=1"
           (undefined: ask-closest, k)
    ✓ L87: "pick the k closest"
           (defines k via "closest" which was introduced L50)

═══════════════════════════════════════════════════════════════
SECTION B: PRESENTATION ORDER (NUMBERS/SYMBOLS FIRST)
═══════════════════════════════════════════════════════════════

09. Answer starts with practical, numerical actions.
    NOT: "The concept of averaging is important."
    YES: "sum = 5 + 4 + 3 + 4 = 16"
         "count = 4"
         "average = 16 ÷ 4 = 4"

10. Numbers, symbols, arrows → before any English word.
    ✗ "We subtract each rating from the average"
    ✓ "Rᵢⱼ ← Rᵢⱼ - μⱼ"
       "μⱼ = (Σₖ Rₖⱼ) / |present ratings|"

11. Format: [Number] [Operation] [Symbol] = [Result]
    Example line:
      5 - 4 = 1   (concrete)
      Rᵢ ← Rᵢ - μ  (generalized)

═══════════════════════════════════════════════════════════════
SECTION C: TUTORING METHODOLOGY (CRACK-THE-PUZZLE)
═══════════════════════════════════════════════════════════════

12. Do NOT provide the solution.
    Provide STEPS to crack the puzzle.
    Reader must derive conclusion themselves.

13. What to do:
    State the next action in numbers.
    Example: "Calculate 5 + 4 = 9"
    NOT: "We combine the values"

14. Why to do:
    Trace back to prior step.
    "Why? Because step(N-1) gave us the values."
    "Without this step, we cannot proceed to step(N+1)."

15. How to do:
    Numerical simulation. Replace variables with concrete numbers.
    Example: "Let pile = {1, 2, 3}"
             "Mean = (1 + 2 + 3) / 3 = 6 / 3 = 2"

16. How did you figure this from the problem?
    Trace back: "Problem asks for [X]. To find [X], we need [Y].
    Step(N-1) gave us [Y]. Therefore, step(N) must calculate [Z]."

17. Compare to previous + next 10 steps:
    ├─ Step(N-2): [what it computed]
    ├─ Step(N-1): [what it computed] ← we depend on this
    ├─ Step(N):   [THIS STEP] ← you are here
    ├─ Step(N+1): [what needs this output]
    ├─ Step(N+2): [depends on step(N)]
    ...
    └─ Step(N+10): [eventual goal we are building toward]

18. Refresh prior work:
    Each new step, state:
    "We have so far: [L1], [L2], …, [Lₙ₋₁].
     Now step(N) will: [action].
     Then step(N+1) will: [next action]."

19. Reason why doing this:
    Not just "do X."
    State: "We do X because [consequence of not doing X] is [bad].
            Step(N) prevents that by [mechanism]."

═══════════════════════════════════════════════════════════════
SECTION D: PUZZLE-CRACKING PROTOCOL (10-STEP METHOD)
═══════════════════════════════════════════════════════════════

20. Extract meaning from each sentence.
    Word-by-word. Mark: nouns, verbs, numbers, symbols.
    Example: "three-quarters of the sheet is holes"
             → 3/4 = 0.75, sheet = 5000 cells, holes = 3786

21. Numerical action (START HERE).
    Convert text to symbols before explaining.
    Example: 0.75 × 5000 = 3750 (but actual is 3786, discrepancy why?)

22. List relevant shortcuts/tricks.
    "Why squared gaps, not absolute gaps?"
    → Shortcut: monotonicity preserved (order same)
    → Benefit: no root calculation needed

23. Numerical simulation.
    Concrete example with real numbers.
    NOT: "Let X be a variable"
    YES: "Let movie ratings = {5, 4, 3, 4}"

24. Step-by-step with numerical examples.
    Each step shows numbers, not generalizations.
    Step 1: 5 + 4 = 9
    Step 2: 9 + 3 = 12
    Step 3: 12 + 4 = 16
    Step 4: 16 / 4 = 4

25. Key concepts to recall from knowledge base.
    State explicitly: "Recall: mean minimizes squared deviation."
    Then DERIVE this fact, don't just state it.

26. Break down complex problems → smaller parts.
    Example: "Fill blanks" →
    ├─ A. Humble each column
    ├─ B. Zero fill round 0
    ├─ C. Rebuild-restore loop
    └─ D. Un-humble to user scale

27. Highlight and connect patterns.
    Repeating numbers? Geometric shapes? Sequences?
    Example: "Round 1 movement = 0.5"
             "Round 2 movement = 0.1"
             "Pattern: Δ → 0 geometrically, ratio ≈ 0.2 per round"

28. Use visual aids.
    ASCII diagrams. NOT prose.
    Example:
      1   2   3       pile = {1,2,3}
      •   •   •       mean ↓
      \ | /
       \|/
        2            centre = 2

29. Provide checks and balances.
    Verify each step.
    □ "Does sum of humbled values = 0?" ✓
    □ "Did blanks stay blank?" ✓
    □ "Did tightness not worsen?" ✓

30. Pattern recognition exercises.
    Include examples for reader to verify.
    "Given pile = {10, 20, 30}, what is the mean?"
    (Reader calculates, verifies against your formula)

31. Provide shortcuts and reason why.
    "Why not measure every distance?"
    → Shortcut: use max(prior distances)
    → Why: complete linkage definition says max(cross-pair dists)
    → Benefit: O(n²) → O(n) per round

═══════════════════════════════════════════════════════════════
SECTION E: DEEP REASONING (MIDDLE TO BOTH ENDS)
═══════════════════════════════════════════════════════════════

32. Scan from middle, move to end.
    Don't read linearly. Find the crux.
    Example: In a derivation, the crux is often step (N/2).
    Why? Because steps before build toward it.
    Steps after follow from it.

33. Find why the middle part does what it does.
    The middle is the pivot. Understand its purpose.
    Example: In K-means, the middle is: "UPDATE = move centre to mean"
    Why? Because mean minimizes squared deviation (optimal point).
    This enables the loop to converge (what comes after).
    This follows from pile formation (what came before).

34. Reason step-by-step from middle → end.
    Middle: UPDATE
    → Step after: Loop checks "did anything move?"
    → Next: If frozen, STOP; else ASSIGN again
    → Eventually: Convergence guaranteed (UPDATE can't worsen)

35. Reason step-by-step from middle → start.
    Middle: UPDATE
    ← Depends on: ASSIGN (piles formed)
    ← Depends on: K chosen, centres initialized
    ← Depends on: Problem statement (what is K-means?)

36. No greetings. No summaries. No superficial repeating.
    No: "As I mentioned earlier"
    No: "To summarize"
    Only: depth reasoning. Each statement new information.

═══════════════════════════════════════════════════════════════
SECTION F: VERIFICATION (FILE ACCEPTANCE CRITERIA)
═══════════════════════════════════════════════════════════════

37. At end of review, list all:
    NEW THINGS INTRODUCED WITHOUT DERIVATION:
    [ list here, or "none" ]

38. If list not empty → FILE REJECTED.
    Must revise to derive every new thing.

39. File acceptance checklist:
    ☐ Line N only uses {L₁, …, Lₙ₋₁}
    ☐ Numerical examples before generalization
    ☐ Every new symbol defined on prior line
    ☐ Every formula derived on prior line
    ☐ No forward references
    ☐ At least one concrete number example per claim
    ☐ Shortcuts explained with why
    ☐ Reasoning traces middle ↔ both ends
    ☐ Checks and balances provided
    ☐ Puzzle-solving steps (not solutions)
    
    All ☐ checked → FILE ACCEPTED
    Any ☐ unchecked → FILE REJECTED

═══════════════════════════════════════════════════════════════
END OF RULES
═══════════════════════════════════════════════════════════════
