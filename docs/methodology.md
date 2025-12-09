# Methodology — How to Use the Influence Risk Engine

This document describes how to score a real country using the
Influence Risk Engine in a consistent, defensible way.

The goal is **comparability and directional accuracy**, not precision.

---

## 1. General Principles

1. Scores are **relative**, not absolute.
2. Use the **same logic and thresholds** across countries.
3. Prefer conservative estimates over extreme ones.
4. When uncertain, document assumptions explicitly.

The engine works best when inputs are:
- transparent
- repeatable
- grounded in observable trends or data

---

## 2. Step-by-Step Workflow

### Step 1: Collect Structural Inputs (BIS)

Gather high-level data for:
- GDP (nominal and PPP)
- population and demographics
- military spending and projection
- geographic position and chokepoints
- technological and industrial capacity

Normalize these into 0–100 component scores
relative to peer states.

Populate:
```text
BIS_INPUTS
BIS_BOUNDS
BIS_WEIGHTS

```

BIS should change slowly and rarely.

---

Step 2: Score Unique Leverage (ULIʳ)

Evaluate each leverage dimension:

Narrative Leverage (NL)

Elite Fungibility (EF)

Contradiction Tolerance (CT)

Legibility & Administrative Depth (LAD)

Peripheral Assimilation Rate (PAR)

Time-Horizon Elasticity (THE)

Redundancy of Leverage (RoL)

External Substitutability Index (ESI)


Use:

historical behavior

institutional performance

external dependency analysis


Populate:

ULI_LEVERAGES
ULI_WEIGHTS

Apply redundancy adjustment afterward.


---

Step 3: Score Fragility (UFIʳ)

Assess break risk across:

identity rigidity

coordination friction

dependence asymmetry

shock absorption capacity

elite–mass feedback quality

narrative balance

temporal mismatch risk


These scores should reflect stress sensitivity, not weakness.

Populate:

UFI_FRAGILITIES
UFI_WEIGHTS


---

Step 4: Determine Trends (ΔULI, ΔUFI)

Use multi-year observation where possible:

political polarization

fiscal stress

alliance cohesion

institutional performance

demographic and technological change


Assign:

"up" if risk/leverage is clearly increasing

"down" if clearly decreasing

"flat" if mixed or stable


Populate:

DELTA_ULI
DELTA_UFI


---

Step 5: Compute IFP

Run the engine to compute:

BIS

adjusted ULIʳ

UFIʳ

Influence Failure Probability (IFP)


Interpret IFP as:

an early warning indicator

not a forecast with a fixed date



---

3. Validation and Calibration

Where possible:

compare outputs to historical analogs

run shock scenarios to test sensitivity

track how scores evolve year over year


Rising IFP paired with rising ΔUFI is the key warning signal.


---

4. Common Mistakes to Avoid

Overfitting scores to recent events

Treating IFP as a prediction, not a probability

Changing weights per country

Hiding assumptions in code instead of documenting them



---

5. Versioning Discipline

When major scoring logic changes:

document rationale

bump version

re-run historical backcasts


Consistency over time matters more than perfect scores.


---

6. Final Note

The strength of this engine is not precision, but structure.

It is designed to help reason clearly about:

where influence comes from

where it is fragile

and how it is most likely to break


---

✅ At this point, the repository is **complete, documented, and usable**.

If you want to stop here, you’re already in great shape.

If you want one last optional polish, the only remaining high-value addition would be a very short **`docs/limitations.md`** explaining what the model deliberately does *not* do.
