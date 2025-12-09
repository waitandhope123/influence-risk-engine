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
