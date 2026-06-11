PR #13 ADJUDICATION -- WHAT THE FOUR RULE REPORTS GOT RIGHT AND WRONG
═══════════════════════════════════════════════════════════════

METHOD: every finding checked against the actual file content
(grep + read), not taken on trust.  Three buckets:
  ACCEPTED     -- real gap, blog fixed or queued
  REJECTED     -- the blog already does what the finding demands,
                  or the demand contradicts the blog's charter
  HALLUCINATED -- the file does not contain the claimed content

THE AXIOM FLOOR (new charter ruling, prompted by rule 2):
  The blog's stated audience axioms are: counting, add, subtract,
  multiply, divide, squares, roots, fractions.  Findings that
  reject content for "using square root without derivation"
  (rule2 #1) fall BELOW the floor and are rejected wholesale.
  Everything ABOVE the floor must be derived -- or be named
  out loud as a CHOICE (model choices are not theorems).

RULE 3 ("zero English words") AND RULE 4 ("no prose, no headings"):
  REJECTED AS STANDARDS.  A teaching blog made of prose cannot
  comply and should not.  What survives from them:
  - rule 4's "User exercise" idea = the charter's YOUR TURN drills
  - rule 4's worked hex-style traces = the charter's "numbers
    before words" inside derivations
  Their arithmetic was spot-checked and is correct (25.29 ->
  sqrt = 5.028; sqrt(27) = 5.196; MSE 17/3 = 5.667; R^2 = 0.83).

═══════════════════════════════════════════════════════════════
RULE 1 / RULE 2 FINDINGS, ONE BY ONE
═══════════════════════════════════════════════════════════════

ACCEPTED (real gaps):

  A1. sorting-into-bins: sig(z) = 1/(1+e^-z) stated, never
      justified.  -> FIXED this commit: derived from odds
      (chance against, multiplied per step), worked by hand.
  A2. chapter1: gap(a,b) formula used before Part 2 derives it.
      -> FIXED this commit: named as a promissory note in place.
  A3. wobble-bands: WHY re-dealing the pile mimics fresh visits
      is asserted ("fake 200 visits") not argued.  The ~37% IS
      derived (the post has "WHY ABOUT 37% SIT OUT EVERY DEAL",
      (1-1/n)^n -> 1/e).  -> FIXED this commit: the stand-in
      argument added in plain words.
  A4. grading-the-guess: E[MSE] = bias^2 + variance + noise is
      named with meanings but not derived.  -> FLAGGED this
      commit as an honest IOU in the post; full pencil
      demonstration queued (needs a two-rule worked example).

REJECTED (blog already does it -- evidence quoted):

  R1. "Gini formula stated as fact" -- mixing-ruler L174:
      "## Why That Formula Is Not Astrology"; Gini derived as
      the chance two random grabs disagree, by hand.
  R2. "(X^T X)^-1 X^T y introduced as fact" -- the-dial-by-hand
      L41/L68: "this post is where those eleven numbers come
      from" ... "The flat-bottom solve collapses to one famous
      line".  The derivation IS the post.
  R3. "AUC without deriving trapezoidal rule" -- the-trade-curve
      L135-147: all six strips computed by pencil, summed to 1.0.
      The strip-area rule (width x average height) sits at the
      axiom floor.
  R4. "F1 without harmonic-mean necessity" -- sorting-into-bins
      L273: "## F1: Why the Harmonic Mean" exists.
  R5. "~37% / resampling without derivation" (rule2 #23 in part)
      -- wobble L45-67 derives (1-1/n)^n -> 1/e ~ 0.37.
  R6. "K-means objective without derivation" -- grouping post
      derives tightness, and update-never-worsens (the mean is
      the minimising spot) is proven in place.
  R7. "PCA variance maximisation without rotation derivation" --
      the stick^2 = shadow^2 + perp^2 section IS the derivation
      that most-kept = least-lost; eigenvectors never enter the
      teaching path (they live in Labels, Last).
  R8. "Linkage merge criteria without derivation" -- single/
      complete/average are CHOICES, and the family-tree post says
      so in place: "a RULE defines its diff".  Choices are named,
      not derived.
  R9. "Slope-intercept form assumed" (straight-stick) -- the
      LINE is a model CHOICE (now the charter's choices-vs-
      theorems ruling); the dials of that line are then derived
      from the bowl.  No fix required.
  R10. Rule 2's "square root / Euclidean distance / mean used
      without derivation" -- below the axiom floor.  Rejected.

HALLUCINATED (file does not contain the claimed content):

  H1. "nci60 uses the Gap statistic / W_k" -- grep finds neither
      anywhere in the post.
  H2. "committees introduces AdaBoost weights" -- the post
      teaches bagging, random forest, gradient boosting; the
      word AdaBoost never appears.
  H3. Rule 3's quoted lines ("Imagine a cloud of points",
      "@title Chapter 1") do not match the actual files.

LESSON (same as the v2 audits): an audit that never opens the
file produces confident garbage.  Adjudicate before incorporating.

═══════════════════════════════════════════════════════════════
SCORE: 4 accepted . 10 rejected . 3 hallucinated
       2 standards rejected wholesale (rules 3, 4)
       1 charter amendment gained (THE AXIOM FLOOR)
═══════════════════════════════════════════════════════════════
