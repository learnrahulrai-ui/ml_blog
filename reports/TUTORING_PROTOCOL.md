TUTORING PROTOCOL — STEP-BY-STEP CRACK-THE-PUZZLE METHOD
═══════════════════════════════════════════════════════════════

RULE: Answer starts with practical numerical actions.
      No solution. Only steps to crack the puzzle.

═══════════════════════════════════════════════════════════════

STEP STRUCTURE (per Lᵢ or per section):

  1. EXTRACT MEANING
     Read line word-by-word.
     Mark: nouns, verbs, numbers, symbols, arrows.
     Example: "three-quarters of the sheet is holes"
              → 3/4 = 0.75 ✓ sheet = 5000 cells ✓ holes = 3786 ✓

  2. NUMERICAL ACTION (START HERE)
     Convert to numbers/symbols first.
     ✗ "We subtract each rating from the movie's mean"
     ✓ Rᵢⱼ ← Rᵢⱼ - μⱼ where μⱼ = Σₖ Rₖⱼ / |present ratings|
     
  3. SHORTCUTS & TRICKS
     Which prior steps can shortcut here?
     "Why not re-measure?" → max(A,C), max(B,C) already computed, reuse.
     "Why squared gaps?" → √ is monotonic, order preserved, skip root.

  4. SIMULATION (replace variables with concrete numbers)
     Example from data:
       movie = "Alien", 4 ratings: 5, 4, 3, 4
       μ = 16/4 = 4
       humbled: +1, 0, -1, 0
     
  5. BREAKDOWN (complex → manageable parts)
     "Fill blanks" ÷ into:
       A. Humble each column
       B. Round-0 zero fill
       C. Rebuild-restore loop
       D. Un-humble to stars

  6. PATTERN RECOGNITION
     Compare:
       Step(N-1): what changed?
       Step(N):   what pattern repeats?
       Step(N+1): what comes next?
       
     Example across K-means rounds:
       Round 1: centres move large (far from start)
       Round 2: centres move small (close to Round 1)
       Round k: centres freeze (no move)
       Pattern: Δ(centre) → 0 monotonically

  7. VISUAL AID (diagram the structure)
     ┌─────────────┐
     │  5  4  3  4 │  ← ratings
     │  +1 0 -1 0  │  ← humbled
     └─────────────┘
     Spot check: sum humbled = 0? (yes, 0)

  8. CHECK & BALANCE (verification step)
     Before/after property holds?
     "Blanks stay blank?" ✓
     "Rated values frozen?" ✓
     "Tightness ≤ last round?" ✓

  9. CONNECT TO PRIOR (line N uses lines 1…N-1)
     This step depends on:
       □ L48: "movie middle"
       □ L61: "humbled definition"
       □ L75: "zero fill is harmless"
     ✓ All prior = available

  10. SHORTCUTS ON THIS STEP
      Why UPDATE → no re-measure?
        Shortcut: complete linkage = max(dists)
        Already have: A-to-C, B-to-C
        Use: max(old values), skip distance calc
      Time saved: O(n²) → O(n) per round

═══════════════════════════════════════════════════════════════

EXAMPLE: "Why update never worsens tightness"

  1. EXTRACT
     "update" = move each centre to its pile's mean
     "tightness" = Σ(dot-to-centre)²
     "never worsens" = tightness(t+1) ≤ tightness(t)

  2. NUMERICAL ACTION
     centre ← mean(pile)
     T = Σᵢ (xᵢ - c)²
     T' = Σᵢ (xᵢ - c')² where c' = mean(xᵢ)
     Prove: T' ≤ T

  3. SHORTCUT
     Fact: mean minimizes squared deviation.
     Proof: d/dc [Σ(xᵢ-c)²] = -2Σ(xᵢ-c) = 0 ⟹ c = mean(xᵢ)
     Second derivative = 2n > 0 ⟹ minimum ✓

  4. SIMULATION
     pile = {1, 2, 3}
     old centre = 2 (guessed)
     new centre = (1+2+3)/3 = 2 (optimal)
     T_old = (1-2)² + (2-2)² + (3-2)² = 1 + 0 + 1 = 2
     T_new = (1-2)² + (2-2)² + (3-2)² = 2 (no change)
     
     pile = {1, 2, 3}, old centre = 1.5
     T_old = 0.25 + 0.25 + 2.25 = 2.75
     T_new = 1 + 0 + 1 = 2 < 2.75 ✓

  5. BREAKDOWN
     A. Mean formula: c = Σxᵢ/n
     B. Variance: σ² = Σ(xᵢ-μ)² / n
     C. Minimality: μ is the value that minimizes σ²

  6. PATTERN
     ├─ L1: choose K
     ├─ L2: ASSIGN (distance used here)
     ├─ L3: UPDATE (mean, no distance) ← YOU ARE HERE
     │     T_new ≤ T_old always
     └─ L4: repeat until frozen

  7. VISUAL
     pile on ruler:
        1   2   3
        •   •   •
         \  |  /
          \ | /
           \|/  ← centre at mean = 2
     squared diffs: 1, 0, 1 → total = 2

  8. CHECK
     □ Centre is in the pile? (average of pile values)
     □ Tightness = sum of squared gaps? ✓
     □ No centre outside domain? ✓

  9. CONNECT
     Depends on:
       □ ASSIGN (L2): piles are formed
       □ definition of tightness (L1)
     Enables:
       □ L4: repeat loop guarantee

  10. SHORTCUT
      Why not recalculate from scratch each round?
      Shortcut: centre ← mean(pile) once per round
      Not: centre ← arg_min(T) via search
      Time: O(n) vs O(n·iterations)

═══════════════════════════════════════════════════════════════

WHEN USING THIS ON BLOG POSTS:

  1. Pick one claim (e.g., "MSE = thrown-away fraction")
  2. Extract the numbers
  3. Simulate with real examples
  4. Break into smaller pieces
  5. Verify with check/balance
  6. Connect to prior steps
  7. Identify pattern to next step

  Deliver: steps only, not the answer.
           Let reader crack it by following steps.

