MASTER AUDIT RULES -- THE BLOG'S OPERATING STANDARD
══════════════════════════════════════════════════════════════
Synthesises: CHARTER_1950.md, ::news, ::banbluff, and the
1950s-auditor ruleset supplied 2026-06-13.
Governs every .txt file under txt/posts/ and txt/*.txt.
══════════════════════════════════════════════════════════════

TIER 0 -- THE CONSTITUTION (CHARTER_1950.md, never changes)
──────────────────────────────────────────────────────────────
  Tier 0 outranks everything.  If any rule below conflicts with
  the 7 Charter Laws, the Charter wins.
  The 7 Laws (summary):
    L1  No machine in teaching path.
    L2  Redo every calculation, every time.
    L3  IN HAND blocks at each major section.
    L4  YOUR TURN drills with checked answers.
    L5  Cost in clerk-steps, never Big-O.
    L6  Axioms first; new word gets its gloss in same sentence.
    L7  Label every claim THEOREM / CHOICE / IOU.

TIER 1 -- ::news  (zero-memory standard)
──────────────────────────────────────────────────────────────
  N1  NO UNDEFINED TERM IN PROSE BODY.
      Every word that is not plain English must be glossed
      inline, in the same sentence, on first use in the post.
      The labels section at the bottom does NOT count.
      ✗  "use the gradient descent update"
      ✓  "use the downhill step (gradient descent -- pick the
          direction that shrinks the loss most, step a little)"

  N2  ZERO WORKING MEMORY.
      A post may not write "from the last post" or "as we
      showed" or "recall that" without IMMEDIATELY restating
      the thing in the same sentence.
      ✗  "As we saw in Part 1, the notepad holds 320,000 dials."
      ✓  "The notepad (the 10,000x32 table where each word gets
          32 dials) holds 320,000 dials."

  N3  EVERY ARITHMETIC STEP SHOWN.
      No jump from line A to line C if line B is missing.
      ✗  "so the answer is 0.73"
      ✓  "1 - 0.27 = 0.73"

  N4  PARADOX BEFORE FORMULA.
      Show the problem that forced the math to be invented
      BEFORE showing the formula.  The reader must feel the
      pain before seeing the cure.
      ✗  "The formula for variance is (1/n) sum (xi - mean)^2."
      ✓  "Without a spread measure, two sets -- {5,5,5} and
          {1,5,9} -- look identical: both have mean 5.  So we
          square the gaps from the mean, add, and divide:
          (1/n) sum (xi - mean)^2."

TIER 2 -- ::banbluff  (word-level substitutions)
──────────────────────────────────────────────────────────────
  These substitutions apply in the TEACHING PATH only.
  Labels-section jargon is exempt (Charter L6: "Jargon waits
  for The Labels, Last").

  TEACHER VOICE -- REPLACE:
    understand   -> calculate / build
    learn        -> practice / repeat
                    EXCEPTION: "the dials learn" / "the machine
                    learns" = valid ML technical term; keep.
                    "learn.rahul.rai@gmail.com" = untouchable.
    explore      -> look at
    dive into    -> start
    journey      -> task
    concept      -> rule
    theory       -> guess / blueprint
    methodology  -> steps
    framework    -> toolbox
    paradigm     -> way of doing things
    perspective  -> angle
    intuition    -> gut feeling
    heuristic    -> shortcut
    optimal      -> best
    efficient    -> fast
    robust       -> strong / handles X well
    scalable     -> handles big piles
    fundamental  -> basic
    crucial      -> needed
    innovative   -> new
    comprehensive -> all of it
    overview     -> quick look
    holistic     -> whole
    nuance       -> tiny detail
    context      -> background

  CORPORATE BUZZWORDS -- REPLACE:
    leverage     -> use
    synergy      -> working together
    utilize      -> use
    implement    -> do / build
    deploy       -> launch
    optimize     -> make faster
    streamline   -> clean up
    ecosystem    -> group
    agile        -> fast
    disruptive   -> rule-breaking
    bandwidth    -> time / space
    align        -> match
    pivot        -> turn
    iterate      -> try again
    onboard      -> teach
    drill down   -> look closer
    ideate       -> think
    impactful    -> strong
    proactive    -> acting early

  ACADEMIC JARGON -- REPLACE (in teaching path, not labels):
    abstract     -> hard to see
    empirical    -> from testing
    quantitative -> measured with numbers
    qualitative  -> measured with words
    hypothesis   -> guess
    correlation  -> moving together
    causation    -> causing
    variable     -> blank box   [EXCEPT when naming the concept]
    parameter    -> dial        [EXCEPT when naming the concept]
    dimension    -> direction
    topology     -> shape
    stochastic   -> random
    deterministic -> always same result
    iteration    -> one try / one pass
    convergence  -> hitting the bottom / end
    divergence   -> flying apart
    infinity     -> never ending
    magnitude    -> size
    vector       -> arrow       [EXCEPT when naming the concept]
    scalar       -> single number

  FLUFF TO CUT ENTIRELY (do not replace, just delete):
    "In conclusion"
    "To summarize"
    "As you can see"
    "It's important to note"
    "Let's take a step back"
    "Without further ado"
    "It is worth mentioning"
    "Delve" / "Navigate" / "Embark"

TIER 3 -- 1950s AUDITOR CHECKS
──────────────────────────────────────────────────────────────
  A1  SMELL TEST.
      Flag and delete conversational fluff, AI praise, modern
      buzzwords ("superintelligence", "magic", "elegant",
      "powerful").

  A2  5-LINE CHAIN.
      Within a derivation block, line N may reference only
      what lines N-5 through N-1 put on the slate.
      If a line needs invisible context older than 5 lines,
      mark it IOU (Charter L7) and re-derive locally.

  A3  AXIOM FLOOR.
      Every concept must trace back to: counting, add,
      subtract, multiply, divide, fractions, squares, roots.
      Abstract concepts with no physical grounding
      (no desk-and-paper equivalent) must be flagged.

  A4  ZERO MAGIC NUMBERS.
      No unexplained number may appear mid-derivation.
      Every constant must be defined in the same paragraph.

  A5  THE WORD "the" -- AUDIT NOTE.
      The 1950s auditor rule flags "the" as banned.
      IN PRACTICE: "the" appears ~4,748 times across 28 posts
      and is present in the Charter itself.  Literal deletion
      would make every sentence nonsense.
      APPLIED RULE: Flag bare anaphoric "the X" where "X" was
      defined more than one paragraph ago and is not
      immediately re-glossed.  Do NOT delete "the" from prose.

  A6  ASCII DIAGRAM STANDARD.
      Every new data structure or algorithm step must have an
      ASCII diagram before the first calculation on that step.
      A diagram is: a labelled box, table, arrow chain, or
      coordinate sketch -- minimum 3 rows x 5 columns.
      Posts that derive without drawing first fail A6.

TIER 4 -- NUMERICAL PROOF STANDARD
──────────────────────────────────────────────────────────────
  P1  CONCRETE NUMBERS BEFORE SYMBOLS.
      Introduce any formula with a worked numerical example
      first.  Symbols come after the reader has calculated.

  P2  SHOW THE PARADOX FIRST.
      Before deriving a formula, show the specific case where
      not having the formula produces a wrong or impossible
      answer.  This is mandatory for every THEOREM.

  P3  EVERY CODE SNIPPET PRECEDED BY HAND DERIVATION.
      No function call appears before its paper equivalent.

══════════════════════════════════════════════════════════════
RULE INTERACTION MATRIX
──────────────────────────────────────────────────────────────
  Charter L6 + N1 + N2  = no undefined terms, no bare memory
  Charter L2 + N3 + A2  = no arithmetic jumps, 5-line chain
  Charter L7 + N4 + P2  = paradox first, then THEOREM label
  Charter L3 + A6       = IN HAND block = ASCII diagram first
  ::banbluff + A1       = purge fluff words and fluff tone

══════════════════════════════════════════════════════════════
WHAT IS EXEMPT
──────────────────────────────────────────────────────────────
  - Navigation header (home | about | archive | glossary)
  - Email address in nav (learn.rahul.rai@gmail.com)
  - "The Labels, Last" section at post bottom
  - Common Tripwires section (real lab struggles, not teaching)
  - "Code, If You Want It" endnotes
  - Post PATH metadata (post N of 28, prev/next links)
  - Anything in the axiom floor (add, subtract, multiply ...)

══════════════════════════════════════════════════════════════
RUNNING THIS AUDIT
──────────────────────────────────────────────────────────────
  Tier 0: Charter self-enforces; check ROLLOUT CHECKLIST.
  Tier 1 (::news): grep for "from the last", "as we showed",
           "recall"; check for undefined terms in prose body.
  Tier 2 (::banbluff): grep each word list above; fix in
           teaching path; skip labels + nav + exempt sections.
  Tier 3 (A2, A3, A4): manual read per post.
  Tier 3 (A5 "the"): do not run mechanically -- see note.
  Tier 3 (A6 diagrams): check that each algorithm section
           opens with an ASCII block before equations.
  Tier 4: check that every THEOREM has a paradox preceding it.

══════════════════════════════════════════════════════════════
